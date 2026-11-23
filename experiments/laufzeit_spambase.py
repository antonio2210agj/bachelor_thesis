"""Laufzeittest: TabPFN-3.5 und LightGBM auf Spambase.

Misst Rechenzeit und GPU-Speicher je Bedingung als Grundlage fuer die Planung
des Hauptversuchs. Kein Hauptversuch: ein Split, eine Maske je Fehlrate, nur
MCAR, Standardkonfigurationen. Die Metriken dienen nur der Plausibilitaet.
"""

import json
import platform
import time
from datetime import datetime
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd
import sklearn
import tabpfn
import torch
from sklearn.impute import SimpleImputer
from sklearn.metrics import balanced_accuracy_score, log_loss
from sklearn.model_selection import StratifiedGroupKFold
from tabpfn import TabPFNClassifier

SEED = 42
RATES = [0.0, 0.1, 0.3, 0.5]
N_SPLITS = 3  # ein Fold als Test, also etwa 67/33

here = Path(__file__).parent
df = pd.read_csv(here / "data" / "spambase" / "spambase.data", header=None)
X = df.iloc[:, :-1].to_numpy(dtype=float)
y = df.iloc[:, -1].to_numpy(dtype=int)

# Identische Merkmalsvektoren bilden eine Gruppe und bleiben in einer Partition
_, groups = np.unique(X, axis=0, return_inverse=True)
groups = groups.ravel()
splitter = StratifiedGroupKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
tr, te = next(splitter.split(X, y, groups))
assert not set(groups[tr]) & set(groups[te])
X_tr, X_te, y_tr, y_te = X[tr], X[te], y[tr], y[te]

# Konstante Spalten anhand des unmaskierten Trainingsanteils entfernen
keep = X_tr.std(axis=0) > 0
X_tr, X_te = X_tr[:, keep], X_te[:, keep]

cuda = torch.cuda.is_available()


def sync():
    if cuda:
        torch.cuda.synchronize()


def run(model, Xtr, Xte):
    if cuda:
        torch.cuda.reset_peak_memory_stats()
    sync()
    t0 = time.perf_counter()
    model.fit(Xtr, y_tr)
    sync()
    t1 = time.perf_counter()
    proba = model.predict_proba(Xte)
    sync()
    t2 = time.perf_counter()
    return {
        "fit_s": round(t1 - t0, 3),
        "predict_s": round(t2 - t1, 3),
        "total_s": round(t2 - t0, 3),
        "gpu_peak_mb": round(torch.cuda.max_memory_allocated() / 2**20, 1) if cuda else None,
        "balanced_accuracy": round(float(balanced_accuracy_score(y_te, proba.argmax(axis=1))), 4),
        "log_loss": round(float(log_loss(y_te, proba)), 4),
    }


def models():
    return {
        "TabPFN-3.5": TabPFNClassifier(random_state=SEED, memory_saving_mode=True),
        "LightGBM": lgb.LGBMClassifier(random_state=SEED, verbose=-1),
    }


# Aufwaermlauf, damit Modellladen und CUDA-Start nicht in die Messung eingehen
t0 = time.perf_counter()
TabPFNClassifier(random_state=SEED, memory_saving_mode=True).fit(X_tr[:200], y_tr[:200]).predict_proba(X_te[:50])
warmup_s = round(time.perf_counter() - t0, 3)
print(f"n_train={len(y_tr)}, n_test={len(y_te)}, Merkmale={X_tr.shape[1]}, Aufwaermlauf {warmup_s}s", flush=True)

# Skalierung mit der Zahl der Trainingsfaelle (vollstaendige Daten, alle Testfaelle)
scaling = []
for n in [500, 1000, 2000, len(y_tr)]:
    y_full = y_tr
    y_tr = y_full[:n]
    res = run(TabPFNClassifier(random_state=SEED, memory_saving_mode=True), X_tr[:n], X_te)
    y_tr = y_full
    scaling.append({"n_train": n, **res})
    print(f"Skalierung n_train={n:5d}: {res['total_s']:7.2f}s  GPU {res['gpu_peak_mb']} MB", flush=True)

rows = []
for rate in RATES:
    rng = np.random.default_rng([SEED, int(rate * 100)])
    Xtr_m, Xte_m = X_tr.copy(), X_te.copy()
    mask_tr = rng.random(X_tr.shape) < rate
    mask_te = rng.random(X_te.shape) < rate
    Xtr_m[mask_tr] = np.nan
    Xte_m[mask_te] = np.nan

    pipelines = {"intern": (Xtr_m, Xte_m)}
    if rate > 0:
        imp = SimpleImputer(strategy="median").fit(Xtr_m)
        Xtr_i, Xte_i = imp.transform(Xtr_m), imp.transform(Xte_m)
        pipelines["median"] = (Xtr_i, Xte_i)
        pipelines["median_indikator"] = (
            np.hstack([Xtr_i, mask_tr.astype(float)]),
            np.hstack([Xte_i, mask_te.astype(float)]),
        )

    for pipe, (a, b) in pipelines.items():
        for name, model in models().items():
            res = run(model, a, b)
            rows.append(
                {
                    "modell": name,
                    "fehlrate": rate,
                    "pipeline": pipe,
                    "n_merkmale": a.shape[1],
                    "fehlanteil_train": round(float(mask_tr.mean()), 4),
                    "fehlanteil_test": round(float(mask_te.mean()), 4),
                    **res,
                }
            )
            print(f"{name:11s} {rate:4.0%} {pipe:17s} {res['total_s']:7.2f}s  "
                  f"GPU {res['gpu_peak_mb']} MB  BA={res['balanced_accuracy']:.4f}", flush=True)

out = {
    "zweck": "Laufzeittest, kein Ergebnis des Hauptversuchs",
    "zeitpunkt": datetime.now().isoformat(timespec="seconds"),
    "datensatz": "Spambase",
    "konfiguration": {
        "seed": SEED,
        "fehlmechanismus": "MCAR",
        "fehlraten": RATES,
        "split": f"StratifiedGroupKFold(n_splits={N_SPLITS}), erster Fold als Test",
        "gruppen": "identische Merkmalsvektoren",
        "modelle": "Standardkonfiguration, random_state=SEED; TabPFN mit memory_saving_mode=True",
        "maskierung": "Training und Test getrennt, unabhaengige Masken je Fehlrate",
    },
    "daten": {
        "n_gesamt": int(len(y)),
        "n_train": int(len(y_tr)),
        "n_test": int(len(y_te)),
        "n_merkmale": int(X_tr.shape[1]),
        "n_gruppen": int(len(np.unique(groups))),
        "zeilen_in_duplikatgruppen": int((np.bincount(groups)[groups] > 1).sum()),
        "klassenanteil_train": round(float(y_tr.mean()), 4),
        "klassenanteil_test": round(float(y_te.mean()), 4),
    },
    "umgebung": {
        "python": platform.python_version(),
        "torch": torch.__version__,
        "tabpfn": tabpfn.__version__,
        "lightgbm": lgb.__version__,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scikit-learn": sklearn.__version__,
        "geraet": torch.cuda.get_device_name(0) if cuda else "CPU",
    },
    "aufwaermlauf_s": warmup_s,
    "skalierung_tabpfn_0_prozent": scaling,
    "laeufe": rows,
}
res_dir = here / "results"
res_dir.mkdir(exist_ok=True)
path = res_dir / f"laufzeit_spambase_{datetime.now():%Y%m%d_%H%M%S}.json"
path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

t = pd.DataFrame(rows)
print("\nSumme je Modell (s):")
print(t.groupby("modell")["total_s"].agg(["sum", "min", "max"]).round(2))
print(f"\nGespeichert: {path}")

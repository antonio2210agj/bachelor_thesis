"""Technischer Pilot: TabPFN-3.5 und LightGBM auf WDBC.

Prueft Ausfuehrbarkeit, Checkpoint-Download, NaN-Verarbeitung und
Median-Imputation. Kein Hauptversuch: feste Seeds, ein Split, eine Fehlrate.
"""

import hashlib
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import balanced_accuracy_score, log_loss
from sklearn.model_selection import train_test_split

SEED = 42
RATE = 0.3  # MCAR-Pilotfehlrate

data_path = Path(__file__).parent / "data" / "breast+cancer+wisconsin+diagnostic" / "wdbc.data"
df = pd.read_csv(data_path, header=None)
y = (df[1] == "M").astype(int).to_numpy()
X = df.drop(columns=[0, 1]).to_numpy(dtype=float)  # ID und Ziel entfernen
print(f"WDBC: X={X.shape}, Klassenanteil M={y.mean():.3f}")

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=SEED
)

rng = np.random.default_rng(SEED)
X_tr_m = X_tr.copy()
X_te_m = X_te.copy()
X_tr_m[rng.random(X_tr.shape) < RATE] = np.nan
X_te_m[rng.random(X_te.shape) < RATE] = np.nan
print(f"Realisierte Fehlanteile: Train={np.isnan(X_tr_m).mean():.3f}, Test={np.isnan(X_te_m).mean():.3f}")

imp = SimpleImputer(strategy="median")
X_tr_i = imp.fit_transform(X_tr_m)
X_te_i = imp.transform(X_te_m)

import lightgbm as lgb
import tabpfn
from tabpfn import TabPFNClassifier

print(f"\ntabpfn={tabpfn.__version__}, lightgbm={lgb.__version__}")

results = {}


def run(name, model, Xtr, ytr, Xte, yte):
    t0 = time.time()
    model.fit(Xtr, ytr)
    proba = model.predict_proba(Xte)
    pred = proba.argmax(axis=1)
    ba = balanced_accuracy_score(yte, pred)
    ll = log_loss(yte, proba)
    results[name] = (ba, ll, time.time() - t0)
    print(f"{name:35s} BA={ba:.4f}  LogLoss={ll:.4f}  ({time.time()-t0:.1f}s)")


# Vollstaendige Referenz
run("TabPFN  0% (Referenz)", TabPFNClassifier(random_state=SEED), X_tr, y_tr, X_te, y_te)
run("LightGBM 0% (Referenz)", lgb.LGBMClassifier(random_state=SEED, verbose=-1), X_tr, y_tr, X_te, y_te)

# 30% MCAR, interne Verarbeitung (NaN-Eingaben)
run("TabPFN  30% intern (NaN)", TabPFNClassifier(random_state=SEED), X_tr_m, y_tr, X_te_m, y_te)
run("LightGBM 30% intern (NaN)", lgb.LGBMClassifier(random_state=SEED, verbose=-1), X_tr_m, y_tr, X_te_m, y_te)

# 30% MCAR, Median-Imputation
run("TabPFN  30% Median", TabPFNClassifier(random_state=SEED), X_tr_i, y_tr, X_te_i, y_te)
run("LightGBM 30% Median", lgb.LGBMClassifier(random_state=SEED, verbose=-1), X_tr_i, y_tr, X_te_i, y_te)

# Checkpoint-Identitaet dokumentieren
print("\nCheckpoint-Dateien im Cache:")
cache_candidates = [
    Path(os.environ.get("APPDATA", "")) / "tabpfn",  # Windows-Standardcache
    Path.home() / ".cache" / "tabpfn",
]
for base in cache_candidates:
    if base.exists():
        for f in base.rglob("*"):
            if f.is_file() and f.suffix in (".safetensors", ".ckpt", ".pt") and f.stat().st_size > 1e6:
                h = hashlib.sha256()
                with open(f, "rb") as fh:
                    for chunk in iter(lambda: fh.read(1 << 20), b""):
                        h.update(chunk)
                print(f"  {f}\n    SHA256={h.hexdigest()}  ({f.stat().st_size/1e6:.1f} MB)")

"""Diagnose zum Laufzeittest: Speicheroptionen von TabPFN auf Spambase.

Aufruf: python laufzeit_diagnose.py <n_train> <memory_saving: auto|true|false> <test_batch: 0 = alle>
Gibt eine JSON-Zeile aus. Wird je Konfiguration als eigener Prozess gestartet.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedGroupKFold
from tabpfn import TabPFNClassifier

n_train = int(sys.argv[1])
msm = {"auto": "auto", "true": True, "false": False}[sys.argv[2]]
batch = int(sys.argv[3])

df = pd.read_csv(Path(__file__).parent / "data" / "spambase" / "spambase.data", header=None)
X = df.iloc[:, :-1].to_numpy(dtype=float)
y = df.iloc[:, -1].to_numpy(dtype=int)
_, groups = np.unique(X, axis=0, return_inverse=True)
tr, te = next(StratifiedGroupKFold(n_splits=3, shuffle=True, random_state=42).split(X, y, groups.ravel()))
X_tr, y_tr, X_te, y_te = X[tr][:n_train], y[tr][:n_train], X[te], y[te]

torch.cuda.reset_peak_memory_stats()
t0 = time.perf_counter()
model = TabPFNClassifier(random_state=42, memory_saving_mode=msm).fit(X_tr, y_tr)
if batch:
    proba = np.vstack([model.predict_proba(X_te[i:i + batch]) for i in range(0, len(X_te), batch)])
else:
    proba = model.predict_proba(X_te)
torch.cuda.synchronize()
print(json.dumps({
    "n_train": len(y_tr), "n_test": len(y_te), "memory_saving_mode": sys.argv[2], "test_batch": batch,
    "total_s": round(time.perf_counter() - t0, 2),
    "gpu_peak_allocated_mb": round(torch.cuda.max_memory_allocated() / 2**20),
    "gpu_peak_reserved_mb": round(torch.cuda.max_memory_reserved() / 2**20),
    "balanced_accuracy": round(float(balanced_accuracy_score(y_te, proba.argmax(axis=1))), 4),
}))

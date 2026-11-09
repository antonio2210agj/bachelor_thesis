# Pilotprotokoll: TabPFN-3.5 und LightGBM auf WDBC

Durchgeführt am 9. November 2026 mit
[pilot_tabpfn_wdbc.py](./pilot_tabpfn_wdbc.py).
Zweck: technischer Machbarkeitsnachweis vor der Anmeldung
(Exposé, Abschnitt „Umfang und weitere Planung"). Kein Hauptversuch:
ein Split, ein Seed, eine Fehlrate.

## Umgebung (fixierbar)

| Komponente | Wert |
|---|---|
| Python | 3.12 (lokale venv) |
| tabpfn | 9.2.0 (Paketlizenz Apache-2.0) |
| lightgbm | 4.7.0 (MIT) |
| numpy / pandas / scikit-learn | 2.5.3 / 3.0.6 / 1.9.1 |
| Checkpoint | `tabpfn-v3.5-20260909.safetensors` (835,4 MB) |
| SHA256 | `ECE4D67EADFEA42EB0E610DF5189BEA60CB7F31073D81E9C7A019B76EACF0BE3` |
| Cache-Pfad | `%APPDATA%\tabpfn\` |
| Hardware | CPU-Inferenz (keine GPU) |

## Modellzugang und Lizenz

- Checkpoint-Download erfordert einmalige Lizenzakzeptanz mit
  Prior-Labs-Konto (`tabpfn-3-5-license-v1.0`): Forschung, Tests und
  Evaluation erlaubt, nicht-kommerziell — die Bachelorarbeit ist abgedeckt.
- API-Token liegt lokal in `~/.cache/tabpfn/auth_token`
  (nicht im Repository; niemals committen).
- Download lief danach automatisch beim ersten `fit()`.

## Versuchsaufbau des Piloten

WDBC lokal geladen (569×30, ohne ID/Ziel), stratifizierter 70/30-Split
(Seed 42), MCAR-Maskierung mit 30 % separat auf Train und Test
(realisiert: 0,303 / 0,299), Median-Imputation nur aus beobachteten
Trainingswerten. Beide Modelle mit Standardkonfiguration.

## Ergebnisse (ein Split — nicht belastbar, nur Machbarkeit)

| Pipeline | TabPFN-3.5 BA | TabPFN LogLoss | LightGBM BA | LightGBM LogLoss |
|---|---|---|---|---|
| 0 % (Referenz) | 0,9844 | 0,0512 | 0,9531 | 0,1083 |
| 30 % intern (NaN) | 0,9922 | 0,0446 | 0,9219 | 0,1376 |
| 30 % Median | 0,9719 | 0,0561 | 0,9375 | 0,1412 |

Laufzeiten: TabPFN ~68–114 s pro Bedingung (CPU), LightGBM ~1–2 s.

## Befunde für die Hauptplanung

1. **Machbarkeit nachgewiesen:** Zugang, Lizenz, Download, NaN-Eingaben,
   Median-Pipeline und Metriken funktionieren End-to-End. Der letzte
   offene Anmeldepunkt aus der Evaluation ist damit erledigt.
2. **Richtungshinweis (nicht überinterpretieren):** intern > Median bei
   TabPFN, Median > intern bei LightGBM — die Behandlung verschiebt den
   Abstand gegenläufig; konsistent mit der Motivation von FF2.
   Dass TabPFN bei 30 % intern nominell über der Referenz liegt, ist
   Einzelsplit-Rauschen.
3. **Budgetplanung:** ~1–2 min pro TabPFN-Bedingung auf CPU bei n≈570.
   Hochgerechnet auf 4 Datensätze × 4 Fehlraten × 3 Behandlungen ×
   Wiederholungen ist der Hauptversuch auf CPU machbar, aber mehrstündig;
   Spambase (n=4601) wird deutlich langsamer sein — im Pilotumfang vor dem
   Hauptversuch einmal auf Spambase testen.
4. **Reproduzierbarkeit:** Checkpoint-Datei und SHA256 sind oben fixiert;
   Paketversionen in [requirements.txt](../requirements.txt) ergänzt.

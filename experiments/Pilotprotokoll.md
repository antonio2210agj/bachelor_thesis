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

## Wiederholung am PC mit GPU (23. November 2026)

Dasselbe Skript unverändert am PC: NVIDIA GeForce RTX 5070 Ti (16 GB),
torch 2.11.0+cu128, tabpfn 9.2.0, lightgbm 4.7.0, numpy 2.5.3, pandas 3.0.6,
scikit-learn 1.9.1. TabPFN wählt das Gerät automatisch (`device='auto'`).

- Balanced Accuracy und Log-Loss stimmen in allen sechs Zeilen auf vier
  Nachkommastellen mit der Tabelle oben überein; realisierte Fehlanteile
  ebenfalls (0,303 / 0,299).
- Checkpoint mit derselben SHA256 (geprüft am 19. November 2026).
- Laufzeit TabPFN: 2,0 s für den ersten Lauf einschließlich Laden des Modells,
  danach 0,3 s je Bedingung; LightGBM unter 0,1 s.

Das ist eine einzelne Messung auf WDBC, kein Laufzeitvergleich. Spambase ist
noch nicht gemessen.

## Laufzeittest auf Spambase am PC (23. November 2026)

Skript [laufzeit_spambase.py](./laufzeit_spambase.py), gespeicherte Messung
[results/laufzeit_spambase_20261123_131211.json](./results/laufzeit_spambase_20261123_131211.json)
mit Konfiguration, Seed, Paketversionen und realisierten Fehlanteilen. Kein
Hauptversuch: ein Split, eine Maske je Fehlrate, nur MCAR, keine Abstimmung. Die
Metriken in der Datei dienen nur der Plausibilität.

Aufbau: Gruppensplit identischer Merkmalsvektoren (`StratifiedGroupKFold`, drei
Folds, einer als Test), 3 067 Trainings- und 1 534 Testfälle, 57 Merkmale;
Fehlraten 0, 10, 30, 50 %; interne Verarbeitung, Median, Median mit Indikatoren
(114 Merkmale).

| Modell | Bedingungen | Zeit je Bedingung | Summe |
|---|---|---|---|
| TabPFN-3.5 (GPU) | 10 | 15,4 bis 46,5 s | 267,7 s |
| LightGBM | 10 | 0,07 bis 0,12 s | 1,0 s |

Bei TabPFN brauchen interne Verarbeitung und Median 15 bis 22 s, die
Indikator-Pipeline mit doppelter Merkmalszahl 44 bis 46 s. Der belegte
GPU-Speicher lag bei etwa 7,6 GB.

**Wichtig für den Hauptversuch: `memory_saving_mode=True` setzen.** Mit der
Standardeinstellung `"auto"` lief der Grafikspeicher (16 GB) ab etwa 2 000
Trainingsfällen voll, und ein einzelner Lauf war nach über fünf Minuten nicht
fertig; zwei Versuche wurden abgebrochen. Einzelmessungen dazu mit
[laufzeit_diagnose.py](./laufzeit_diagnose.py), jeweils eigener Prozess,
vollständige Daten, alle 1 534 Testfälle (Konsolenausgabe, hier festgehalten):

| Trainingsfälle | `memory_saving_mode` | Testfälle je Aufruf | Zeit | Balanced Accuracy |
|---|---|---|---|---|
| 1 500 | auto | alle | 2,0 s | 0,9048 |
| 2 000 | auto | alle | abgebrochen (> 5 min) | – |
| 2 000 | True | alle | 2,5 s | 0,9380 |
| 2 000 | auto | 256 | 5,9 s | 0,9380 |
| 3 067 | True | alle | 3,2 s | 0,9670 |
| 3 067 | True | 512 | 5,9 s | 0,9662 |
| 3 067 | auto | 512 | 5,8 s | 0,9662 |

Zwei Beobachtungen, beide nicht weiter untersucht:

- Dieselbe Bedingung (3 067 Fälle, 0 %) braucht im frischen Prozess 3,2 s, im
  langen Lauf nach mehreren Modellen 13,6 bis 15,4 s. Die Zeiten der Tabelle
  oben sind deshalb eher eine Obergrenze; Speicherfreigabe zwischen den Läufen
  könnte sie senken.
- Die Vorhersage in Teilmengen der Testfälle ändert die Balanced Accuracy
  leicht (0,9662 statt 0,9670). Im Hauptversuch die Testfälle deshalb für alle
  Bedingungen auf dieselbe Weise übergeben.

Hochrechnung für Spambase aus der gespeicherten Messung, unter der Annahme,
dass MAR und MNAR so lange rechnen wie MCAR:

| Umfang | TabPFN-Läufe je Wiederholung | Zeit je Wiederholung | 20 Wiederholungen |
|---|---|---|---|
| nur MCAR | 10 | 4,5 min | 1,5 h |
| drei Mechanismen | 28 | 12,9 min | 4,3 h |

Die drei kleineren Datensätze sind nicht gemessen; WDBC brauchte 0,3 s je
Bedingung. Nicht enthalten sind die LightGBM-Abstimmung und die
Sensitivitätsanalyse bei 50 %.

## Befunde für die Hauptplanung

1. **Machbarkeit nachgewiesen:** Zugang, Lizenz, Download, NaN-Eingaben,
   Median-Pipeline und Metriken funktionieren End-to-End. Der letzte
   offene Anmeldepunkt aus der Evaluation ist damit erledigt.
2. **Richtungshinweis (nicht überinterpretieren):** intern > Median bei
   TabPFN, Median > intern bei LightGBM — die Behandlung verschiebt den
   Abstand gegenläufig; konsistent mit der Motivation von FF2.
   Dass TabPFN bei 30 % intern nominell über der Referenz liegt, ist
   Einzelsplit-Rauschen.
3. **Budgetplanung (CPU-Stand vom 9. November; am PC mit GPU deutlich
   schneller, siehe oben):** ~1–2 min pro TabPFN-Bedingung auf CPU bei n≈570.
   Hochgerechnet auf 4 Datensätze × 4 Fehlraten × 3 Behandlungen ×
   Wiederholungen ist der Hauptversuch auf CPU machbar, aber mehrstündig;
   Spambase (n=4601) wird deutlich langsamer sein — im Pilotumfang vor dem
   Hauptversuch einmal auf Spambase testen.
4. **Reproduzierbarkeit:** Checkpoint-Datei und SHA256 sind oben fixiert;
   Paketversionen in [requirements.txt](../requirements.txt) ergänzt.

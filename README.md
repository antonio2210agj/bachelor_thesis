# Bachelorarbeit: TabPFN

Arbeitsrepository für eine kritische Literaturanalyse zu Methoden,
Einsatzmöglichkeiten und Grenzen von TabPFN sowie eine empirische
Anschlussuntersuchung zum Einfluss der Behandlung fehlender Merkmalswerte
auf den Leistungsvergleich zwischen TabPFN-3.5 und LightGBM.

## Struktur

- `literature/`: Literatur-PDFs und Literaturnotizen mit Quellenstellen in `notes/`.
- `writing/`: Gliederung, LaTeX-Quellen, Bibliografie und kompilierte PDFs.
- `experiments/`: Python-Experimente und der aktuell verwendete Datensatz.
- `experiments/Pilotprotokoll.md`: Protokoll des technischen
  TabPFN-3.5-/LightGBM-Piloten; kein Ergebnis des Hauptversuchs.

Die PDFs in `literature/` sind thematisch abgelegt:

- `01_Grundlagen_KI_PFN/`: LLM-/In-Context-Learning- und PFN-Grundlagen.
- `02_TabPFN_Kernmodelle/`: TabPFN-Originalarbeit, Nature/TabPFNv2 und Modellberichte.
- `03_Benchmarks_Baumverfahren/`: vergleichende Benchmarks und Baumverfahren.
- `04_Merkmalszahl_und_Selektion/`: Zusatzmerkmale, Merkmalsauswahl und breite Tabellen.
- `07_Missing_Data_und_Imputation/`: Missing-Data- und Imputationsliteratur;
  ergänzende Quellen und Lizenzhinweise stehen im Abschlussabgleich.
  Bestehende Modellberichte mit Missing-Data-Bezug bleiben bei den Kernmodellen,
  statt doppelt abgelegt zu werden. Die Nummerierung bleibt trotz nicht mehr
  vorhandener Themenordner 05 und 06 erhalten, um bestehende Links zu bewahren.
- `notes/`: Literaturnotizen und der
  [abschliessende Missing-Data-Literaturabgleich](literature/notes/Missing_Data_Abschlussabgleich.md)
  mit Quellenstellen, Abgrenzung und Empfehlungen zur Frageformulierung.

Literatur-PDFs dürfen nur dann ins Repository aufgenommen werden, wenn die
Lizenz und die Weitergaberechte dies erlauben. Ein privates Repository ersetzt
diese Prüfung nicht. Die virtuelle Python-Umgebung und temporäre LaTeX-Dateien
bleiben lokal.

## Einrichtung auf einem zweiten Windows-Rechner

Git, Python (empfohlen: 3.12) und VS Code müssen installiert sein. Für das
Kompilieren der LaTeX-Dateien wird zusätzlich beispielsweise MiKTeX benötigt.

In PowerShell:

```powershell
git clone https://github.com/antonio2210agj/bachelor_thesis.git
Set-Location bachelor_thesis
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe experiments\test_loader.py
```

Die Befehle für Experimente werden aus dem Projekt-Hauptordner ausgeführt.
In VS Code `.venv\Scripts\python.exe` als Python-Interpreter auswählen.
Die Abhängigkeiten umfassen den Datenlader sowie TabPFN und LightGBM für den
technischen Pilot. Vor dem ersten TabPFN-Lauf müssen die geltenden
Nutzungsbedingungen akzeptiert und der erforderliche Modellzugang eingerichtet
sein. Der Pilot kann aus dem Projekt-Hauptordner mit folgendem Befehl gestartet
werden:

```powershell
.\.venv\Scripts\python.exe experiments\pilot_tabpfn_wdbc.py
```

Das Pilotprotokoll dokumentiert die getestete lokale Umgebung und den
Checkpoint. `requirements.txt` enthält derzeit Versionsbereiche, keine
vollständige Umgebungs- oder Checkpoint-Sperre; für den Hauptversuch müssen
die tatsächlich verwendeten Paketversionen und die geladene Checkpointdatei
zusätzlich festgehalten werden.

## Zwischen Desktop und Laptop wechseln

Vor Arbeitsbeginn:

```powershell
git pull --ff-only
```

Nach der Arbeit:

```powershell
git status
git add <Dateien>
git commit -m "Beschreibung der Änderungen"
git push
```

Vor dem Wechsel auf den anderen Rechner immer committen und pushen.
Nicht gleichzeitig dieselben Dateien auf beiden Rechnern bearbeiten.
Bei einem fehlgeschlagenen Pull zuerst die Meldung prüfen; keine lokalen
Änderungen mit einem Reset verwerfen.

## Speicherort

Auf dem Laptop am besten außerhalb eines OneDrive-Synchronisationsordners
klonen, zum Beispiel nach `C:\Users\<Name>\Projects\bachelor_thesis`.
Git synchronisiert nur durch Commit, Push und Pull; es synchronisiert nicht
automatisch und ermöglicht für sich genommen keine Remote-Ausführung.

## Zugriff und Datenschutz

Das Repository soll privat bleiben. Keine API-Schlüssel, Passwörter oder
vertraulichen Datensätze committen. Neue Datensätze vor dem Hochladen auf
Weitergaberechte und personenbezogene Inhalte prüfen.

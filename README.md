# Bachelorarbeit: TabPFN

Arbeitsrepository fuer die Literaturrecherche, Schreibdateien und Experimente
zur kontrollierten Untersuchung der Robustheit von TabPFN-3.5 gegenueber
irrelevanten Merkmalen im Vergleich zu LightGBM.

## Struktur

- `literature/`: Literatur-PDFs und Literaturnotizen mit Quellenstellen in `notes/`.
- `writing/`: Gliederung, LaTeX-Quellen, Bibliografie und kompilierte PDF.
- `experiments/`: Python-Experimente und der aktuell verwendete Datensatz.

Literatur-PDFs koennen zusammen mit den Notizen im privaten Repository versioniert
werden und stehen nach Commit, Push und Pull auch auf dem anderen Rechner bereit.
Vor dem Hinzufuegen neuer Papers die Lizenz und Weitergaberechte pruefen;
ein privates Repository ersetzt diese Pruefung nicht.
Die virtuelle Python-Umgebung und temporaere LaTeX-Dateien bleiben lokal.

## Auf einem zweiten Windows-Rechner einrichten

Git, Python (empfohlen: 3.12) und VS Code muessen installiert sein.
Fuer das Kompilieren der LaTeX-Dateien wird zusaetzlich beispielsweise MiKTeX
benoetigt.

In PowerShell:

```powershell
git clone https://github.com/antonio2210agj/bachelor_thesis.git
Set-Location bachelor_thesis
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe experiments\test_loader.py
```

Die Befehle fuer Experimente werden aus dem Projekt-Hauptordner ausgefuehrt.
In VS Code `.venv\Scripts\python.exe` als Python-Interpreter auswaehlen.
Die Python-Abhaengigkeiten decken den aktuellen Datenlader ab; TabPFN ist noch
nicht Teil der Implementierung.

## Zwischen Desktop und Laptop wechseln

Vor Arbeitsbeginn:

```powershell
git pull --ff-only
```

Nach der Arbeit:

```powershell
git status
git add <Dateien>
git commit -m "Beschreibung der Aenderungen"
git push
```

Vor dem Wechsel auf den anderen Rechner immer committen und pushen.
Nicht gleichzeitig dieselben Dateien auf beiden Rechnern bearbeiten.
Bei einem fehlgeschlagenen Pull zuerst die Meldung pruefen; keine lokalen
Aenderungen mit einem Reset verwerfen.

## Speicherort

Auf dem Laptop am besten ausserhalb eines OneDrive-Synchronisationsordners
klonen, zum Beispiel nach `C:\Users\<Name>\Projects\bachelor_thesis`.
Git synchronisiert nur durch Commit, Push und Pull; es synchronisiert nicht
automatisch und ermoeglicht fuer sich genommen keine Remote-Ausfuehrung.

## Zugriff

Das Repository soll privat bleiben. Keine API-Schluessel, Passwoerter oder
vertraulichen Datensaetze committen. Neue Datensaetze vor dem Hochladen auf
Weitergaberechte und personenbezogene Inhalte pruefen.

# Bachelorarbeit: TabPFN

Arbeitsrepository für die Literaturrecherche, Schreibdateien und Experimente
zur kontrollierten Untersuchung der Robustheit von TabPFN-3.5 gegenüber
irrelevanten Merkmalen im Vergleich zu LightGBM.

## Struktur

- `literature/`: Literatur-PDFs und Literaturnotizen mit Quellenstellen in `notes/`.
- `writing/`: Gliederung, LaTeX-Quellen, Bibliografie und kompilierte PDFs.
- `experiments/`: Python-Experimente und der aktuell verwendete Datensatz.

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
Die Python-Abhängigkeiten decken den aktuellen Datenlader ab; TabPFN ist noch
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

# Arbeitsanweisungen für KI-Assistenten in diesem Repository

Diese Datei wird in jedem Chat automatisch geladen. Sie enthält nur Dauerhaftes.
Der veränderliche Stand (Entscheidungen, offene Punkte, nächste Schritte) steht
in [PROJEKTSTAND.md](../PROJEKTSTAND.md) und ist **zu Beginn jeder Sitzung zu lesen**.

## Zu Beginn jeder Sitzung (PC und Laptop)

1. `PROJEKTSTAND.md` vollständig lesen, bevor inhaltlich gearbeitet wird.
2. Mit dem eigenen Wissen aus dem laufenden Chat abgleichen. Fehlt dort etwas,
   das im Chat entschieden oder erledigt wurde und noch gilt, den Projektstand
   ergänzen, mit Datum und Rechner.
3. Ist das eigene Wissen älter als der Projektstand oder widerspricht es einer
   dort später datierten Entscheidung, gilt der Projektstand; Veraltetes wird
   nicht eingetragen. Im Zweifel den Nutzer fragen.
4. Ergänzungen dem Nutzer kurz nennen.

## Projekt

Bachelorarbeit von Marco Garcia Jung, Universität Regensburg, Lehrstuhl für
Prozessbasierte Informationssysteme. Titel: „Tabular Foundation Models bei
fehlenden Merkmalswerten: Ein Vergleich mit Gradient Boosting bei
Klassifikationsaufgaben“.

- FF1 (Literaturanalyse): Befunde und Grenzen der Literatur zu fehlenden
  Merkmalswerten bei Tabular Foundation Models und Gradient Boosting, daraus
  abgeleiteter Untersuchungsbedarf.
- FF2 (Experiment): Veränderung des Leistungsunterschieds zwischen beiden
  Modellansätzen bei steigender Fehlrate und unterschiedlichen Behandlungen.
- Vertreter: TabPFN-3.5 und LightGBM. Verglichen werden Verarbeitungsprinzipien,
  nicht Modellversionen.

Antworte auf Deutsch. Der Nutzer schreibt oft knapp und mit Tippfehlern; bei
echter Mehrdeutigkeit nachfragen, sonst sinngemäß umsetzen.

## Welche Datei gilt

Bei Widersprüchen gilt die höhere Zeile.

1. `PROJEKTSTAND.md`: datierte Entscheidungen, auch solche aus Betreuergesprächen.
2. `writing/Expose.tex`: abgestimmtes Design (Forschungsfragen, Abgrenzung,
   Versuchsaufbau, Auswertung).
3. `writing/thesis/chapters/*.tex` und `writing/Gliederung.tex`: Struktur der Arbeit.
4. `literature/notes/Suchprotokoll.md` und `literature/notes/Konzeptmatrix.csv`:
   Dokumentation für FF1 (Kapitel 3.1 und Anhang A).
5. `literature/notes/Missing_Data_Abschlussabgleich.md` (Stand 6. November 2026)
   und die Notizen `1_` bis `5_`: Hintergrund. Der Abschlussabgleich ist in
   Teilen überholt (dort noch ohne MAR/MNAR und vor dem Pilot).

Vor inhaltlicher Arbeit je nach Aufgabe lesen:

| Aufgabe | Zuerst lesen |
|---|---|
| Literaturanalyse, Kapitel 3 | Suchprotokoll, Konzeptmatrix, Exposé Abschnitt 1 |
| Methodik, Kapitel 4 | Exposé Abschnitte 2 und 3, `experiments/Pilotprotokoll.md` |
| Experimentcode | Exposé „Experiment und Auswertung“, Pilotprotokoll, `experiments/pilot_tabpfn_wdbc.py` |
| Grundlagen, Kapitel 2 | Notizen `literature/notes/1_` bis `5_`, zugehörige PDFs |
| Schreiben allgemein | Kapitelgerüst in `writing/thesis/chapters/`, `Methodik/` (Vorgaben des Lehrstuhls) |

## Regeln für wissenschaftliche Aussagen

Grundlage sind die Lehrstuhlvorgaben (`Methodik/`) und die Erfahrungen aus dem
Abschlussabgleich, in dem Websuch-Zusammenfassungen unbelegte Aussagen enthielten.

- Keine Aussage über eine Quelle ohne Prüfung am Volltext. PDFs liegen in
  `literature/`; Text extrahieren mit `pdftotext -layout -enc UTF-8 <pdf> <txt>`
  (bei Umlauten im Pfad die Datei vorher in einen temporären Ordner kopieren).
- Jede Quellenaussage mit Fundstelle angeben (Seite, Abschnitt, Tabelle oder
  Abbildung), im Text als `\cite[Abschnitt 3.1]{schluessel}`.
- Keine Literaturangaben, Zahlen oder Zitate aus dem Gedächtnis oder aus
  Websuch-Zusammenfassungen übernehmen. Websuche dient nur der Kandidatenfindung.
  KI-Ausgaben sind keine Quelle.
- Ist etwas nicht geprüft, das ausdrücklich so kennzeichnen statt es plausibel
  zu formulieren. In der Konzeptmatrix bleibt `?` stehen, bis die Zelle am
  Volltext belegt ist; die Spalte „Status“ entsprechend fortschreiben.
- Gemessene Befunde und Interpretation trennen. Keine Neuheitsbehauptung, kein
  allgemeines Modellranking, keine Aussagen über Fehlmechanismen, die nicht
  untersucht wurden.
- Entwicklerberichte und unabhängige Studien getrennt einordnen;
  Rekonstruktionsgüte und Vorhersageleistung nicht vermischen.
- Der Nutzer ist für jeden Satz der Arbeit verantwortlich. Textvorschläge so
  liefern, dass er sie prüfen kann: mit Fundstellen und mit Hinweis auf
  unsichere Stellen. Änderungen an Forschungsfragen oder Versuchsdesign nur
  nach Rücksprache.

## Begriffe

Einheitlich verwenden: „fehlende Merkmalswerte“, „Fehlrate“, „Fehlmechanismus“
(MCAR, MAR, MNAR), „Behandlung“ (interne Verarbeitung, Median-Imputation,
Median-Imputation mit Missing-Indikatoren), „Modellansatz“,
„Verarbeitungsprinzip“, „Pipeline“, „Leistungsunterschied“ bzw.
„Leistungsabstand“. Modellnamen: TabPFN (v1), TabPFNv2, TabPFN-2.5, TabPFN-3.5.

## Schreiben und LaTeX

- Sprache der Arbeit: Deutsch, mit echten Umlauten und ß, UTF-8.
- Gemeinsame Bibliografie: `writing/references.bib`. Nur vorhandene Schlüssel
  verwenden; neue Einträge über DOI anlegen und am Original prüfen.
- Kapitel liegen einzeln in `writing/thesis/chapters/`; Labels nach dem Muster
  `sec:kapitel-thema`, `tab:…`, `fig:…`.
- Zitierstil: IEEE (`style=ieee` in `writing/thesis/main.tex`), Verzeichnis in
  Zitierreihenfolge.
- Lehrstuhlvorgaben: Quelle vor dem Satzpunkt, nicht eine Quelle für einen ganzen
  Absatz; Tabellenbeschriftung oben, keine senkrechten Linien; Abbildungen als
  PDF mit Beschriftung unten; jede Tabelle und Abbildung im Text erklären.
- `Methodik/` enthält die unveränderte Lehrstuhlvorlage und wird nicht bearbeitet.
- Build: `.\writing\thesis\build.ps1` (pdflatex, biber, zweimal pdflatex,
  `-shell-escape`). Einen laufenden Build nie abbrechen: MiKTeX installiert beim
  ersten Lauf fehlende Pakete nach, ein Abbruch kann die Paketdatenbank
  beschädigen.
- Build-Nebenprodukte sind ignoriert. `main.pdf`, `Expose.pdf` und
  `Gliederung.pdf` sind versioniert und werden nur bewusst mitcommittet.

## Experimente

- Rechenläufe des Hauptversuchs finden nur am PC statt. Der Laptop dient
  Recherche, Schreiben und kurzen Tests.
- Python 3.12 in `.venv`; Befehle aus dem Projekt-Hauptordner mit
  `.\.venv\Scripts\python.exe` ausführen.
- Kein Informationsabfluss: Splits vor Maskierung und Vorverarbeitung; Median
  und andere Statistiken nur aus beobachteten Trainingswerten; Testdaten nie für
  Abstimmung oder Konfigurationswahl; Labels werden nicht maskiert.
- Beide Modelle und alle Behandlungen erhalten innerhalb eines Durchlaufs
  dieselben Splits und Masken. Identische Merkmalsvektoren bleiben als Gruppe in
  einer Partition.
- Jede Zufallsquelle über dokumentierte Seeds steuern. Ergebnisse mit
  Konfiguration, Seeds, Paketversionen und realisierten Fehlanteilen speichern,
  nie nur auf der Konsole ausgeben.
- Zahlen in der Arbeit stammen ausschließlich aus gespeicherten Ergebnisdateien,
  nicht aus Chatverläufen. Der Pilot ist kein Ergebnis des Hauptversuchs.
- Während des Hauptversuchs keine Paket- oder Checkpointupdates.
- Zugangsdaten bleiben lokal (`~/.cache/tabpfn/auth_token`) und werden nie
  ausgegeben oder committet.

## Arbeitsweise

- Es wird an zwei Rechnern gearbeitet. Vor Beginn `git pull --ff-only`, danach
  committen und pushen. Kein Reset und kein Force-Push ohne ausdrückliche Bitte.
- Literatur-PDFs nur committen, wenn die Lizenz die Weitergabe erlaubt.
- Am Ende einer Sitzung, oder wenn der Nutzer „Sitzungsende“ schreibt,
  `PROJEKTSTAND.md` aktualisieren: neue Entscheidungen mit Datum, erledigte und
  neue offene Punkte, nächste Schritte, Eintrag im KI-Nutzungsprotokoll.
- Neue Dauerregeln gehören in diese Datei, nicht in den Chat.

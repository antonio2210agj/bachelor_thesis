# Projektstand

Fortlaufend gepflegter Stand der Bachelorarbeit. Dauerhafte Arbeitsregeln stehen
in [.github/copilot-instructions.md](.github/copilot-instructions.md).

Zuletzt aktualisiert: 25. November 2026 (PC). Erstfassung am Laptop aus dem
Inhalt des Repositorys erstellt; danach um den Stand aus dem PC-Chat ergänzt.

## Eckdaten

| Punkt | Stand |
|---|---|
| Abgabedatum laut `writing/thesis/main.tex` | 16. Februar 2027 |
| Erstgutachter | Prof. Dr. Stefan Schönig |
| Betreuer | Maximilian Metzner |
| Letzter Stand beim Betreuer | Exposé abgegeben, Bachelorarbeit angemeldet (Angabe des Nutzers vom 21.11.2026) |
| Nächster Betreuertermin | Freitag, 27. November 2026 (laut Nutzer vom 25.11.) |
| Seitenbudget laut Kapitelgerüst | ca. 40 Seiten ohne Anhang (4, 7, 6, 6, 9, 6, 2); „40 oder so“ ist eine Angabe des Nutzers vom 19.11.2026, keine belegte Lehrstuhlvorgabe |
| Phase | Literaturanalyse (FF1) beginnt; Kapitel sind Gerüste ohne Text |

## Entscheidungen

| Datum | Entscheidung | Quelle |
|---|---|---|
| 06.11.2026 | Fokus auf fehlende Merkmalswerte; Fehlraten 0, 10, 30, 50 %; Training, Validierung und Test separat und unabhängig mit derselben Zielfehlrate maskiert | Abschlussabgleich |
| 06.11.2026 | Kern: interne Verarbeitung gegen Median-Imputation; Median mit Missing-Indikatoren als Zusatzanalyse | Abschlussabgleich |
| 09.11.2026 | Technischer Pilot auf WDBC abgeschlossen; Checkpoint `tabpfn-v3.5-20260909.safetensors` mit SHA256 dokumentiert | Pilotprotokoll |
| 13.11.2026 | Nach Betreuergespräch: Titel und Forschungsfragen auf Ebene der Modellansätze formuliert; TabPFN-3.5 und LightGBM sind austauschbare Vertreter | Commits `be17761`, `24e045e` |
| 13.11.2026 | Fehlmechanismus ist Versuchsfaktor; MCAR als Referenz, MAR und MNAR vorgesehen, Umfang wird nach der Literaturanalyse festgelegt | Exposé |
| 19.11.2026 | MCAR, MAR und MNAR gehen alle in den Hauptversuch ein („auf jeden Fall“); offen ist nur noch der Umfang je Mechanismus, der sich nach dem Arbeitsaufwand richtet. Die Variante „nur MCAR“ ist damit verworfen | Nutzer, PC |
| 19.11.2026 | FF1 und FF2 bleiben im Wortlaut unverändert. Dass FF2 den Fehlmechanismus nicht nennt, ist gewollt (Spielraum); auch der Titel nennt keinen Mechanismus | Nutzer, PC |
| 19.11.2026 | Statistische Tests nur, wenn der Betreuer sie verlangt; sonst deskriptive Auswertung | Nutzer, PC |
| 19.11.2026 | Ältere Begleitdokumente (`notizen.md`, Exposé-Evaluationen, Verbesserungstipps, Cooper-Notiz, Gesprächscheckliste) bewusst gelöscht; sie gelten nicht mehr | Nutzer, PC |
| 23.11.2026 | Neue Literaturrecherche von Grund auf dokumentieren; vorhandene Literatur bleibt Bestand und wird nach denselben Kriterien geprüft oder mit getrennt dokumentiertem Fundweg ergänzt. Abschnitt 2 des Suchprotokolls beschreibt noch den früheren Plan und ist vor der Recherche anzupassen | Nutzer, PC |
| 20.11.2026 | Zitierstil IEEE nach den Lehrstuhlfolien; `main.tex` von `style=lncs` auf `style=ieee` umgestellt (Abweichung von der Lehrstuhlvorlage, vom Nutzer entschieden) | Nutzer, Laptop |
| 20.11.2026 | Rechenläufe des Hauptversuchs nur am PC; Laptop für Recherche, Schreiben und kurze Tests | Nutzer, Laptop |
| 20.11.2026 | Literaturanalyse: zuerst alle relevanten Arbeiten breit sammeln und jede Suche protokollieren, dann anhand der Ein- und Ausschlusskriterien reduzieren; die Konzeptmatrix bleibt, weil das Exposé sie zusagt | Nutzer, Laptop |
| Exposé | Primäre Metrik Balanced Accuracy, ergänzend Log-Loss; Zielgröße ist die Veränderung des gepaarten Abstands Δ − Δ₀ gegenüber der vollständigen Referenz | Exposé |
| Exposé | LightGBM wird nur auf der vollständigen Referenz abgestimmt und bleibt konstant; Sensitivitätsanalyse mit erneuter Abstimmung bei 50 %; TabPFN-3.5 mit Standardkonfiguration | Exposé |
| Exposé | Identische Merkmalsvektoren bleiben als Gruppe in einer Partition; nur binäre Klassifikation; vier numerische Hauptkandidaten, Credit-G als Reserve | Exposé |

## Offene Entscheidungen

Laut Exposé vor dem Hauptversuch festzulegen:

- endgültige Datensatzauswahl
- konkrete MAR- und MNAR-Regeln und ihr Umfang im Hauptversuch
- Splitanteile und Zahl der Wiederholungen (Splits und Maskierungsdurchläufe)
- Suchraum, Optimierungsmetrik und Budget der LightGBM-Abstimmung
- Aggregation der gepaarten Differenzen
- Regel für vollständig maskierte Trainingsspalten
- Fixierung von Paketversionen, Modellkonfiguration, Checkpoint und Seeds

Vom Nutzer zu entscheiden (Vorschläge vom 19.11.2026, PC, noch unbeantwortet):

- Kapitel 2 straffen: 2.2 und 2.3 zusammenlegen, 2.7 (Metriken) nach 4.7
  verschieben; sieben Unterkapitel auf rund sieben Seiten sind kleinteilig.
- Indikator-Behandlung einheitlich als Zusatzanalyse führen. Die Gliederung
  nennt sie so, die Abgrenzungstabelle im Exposé zählt sie als dritte volle
  Behandlung.
- Der Absatz zur Bedeutung von „Eignung“ (Leistung und Robustheit, nicht Kosten
  oder Laufzeit) steht nur noch in `Gliederung.tex`, nicht mehr im Exposé; für
  Kapitel 1.3 vormerken.
- Exposé als abgeschlossen behandeln und nur noch Gliederung und Kapitel pflegen.

Mit dem Betreuer zu klären:

- Datenbanken: Das Exposé nennt Google Scholar, arXiv und Zitationssuche; das
  Suchprotokoll zusätzlich Scopus, IEEE Xplore und ACM Digital Library. Die
  Folien nennen außerdem AISeL. Eine Fassung festlegen und beide Dokumente
  angleichen.

## Stand der Arbeitspakete

### Literaturanalyse (FF1)

- Suchprotokoll: Vorgehen, Suchstrings S1 bis S4 und Kriterien stehen als
  Vorschlag. Such-Log, Rückwärts- und Vorwärtssuche, Auswahlzahlen und
  Ausschlussliste sind leer; es ist noch keine Datenbanksuche protokolliert.
  Vorhanden sind sowohl Grundlagen als auch thematisch einschlägige Arbeiten.
  Laut Nutzer wurde bis zum 25.11.2026 nicht weiter recherchiert.
- Konzeptmatrix: 9 Arbeiten, alle mit Status „vorbefüllt, am Volltext prüfen“,
  21 Zellen mit `?`. In der Matrix fehlen aus der Startmenge der
  TabPFN-2.5-Bericht und Ke et al. (2017).
- Lokal fehlt TabImpute in der Fassung arXiv v6; für Ke et al. (2017) und Rubin
  (1976) liegt kein PDF vor.
- Perez-Lebel et al. (arXiv 2202.10580v1, Author Accepted Manuscript) liegt nur
  am PC unter `literature/07_Missing_Data_und_Imputation/` und ist in
  `.gitignore` ausgenommen, weil arXiv dafür keine Weitergabelizenz ausweist.
  Am Laptop bei Bedarf selbst herunterladen.
- Die frühere Kandidatenliste wurde am 23.11.2026 (PC) aus dem Suchprotokoll
  entfernt: Die dort genannten eigenständigen Arbeiten waren weder lokal
  vorhanden noch im Exposé oder auf dem sichtbaren Zotero-Screenshot enthalten.
  Neue Kandidaten werden bei der Recherche dokumentiert.
- In `references.bib` vorhanden, aber nirgends zitiert:
  `cooper_organizing_1988`, `page_prisma_2021` (vermutlich für Kapitel 3.1),
  `hu_noise_2026`, `liu_repeated_2026`, `zhao_alignment_2026` (früherer Zuschnitt).

### Experiment (FF2)

- Vorhanden sind der Pilot `experiments/pilot_tabpfn_wdbc.py`, der Ladetest
  und die Laufzeitskripte `laufzeit_spambase.py` und `laufzeit_diagnose.py`
  (mit Gruppensplit und allen drei Behandlungen, aber nur MCAR und ein Split).
  Code für den Hauptversuch (Splits mit Gruppen, Maskierung je
  Fehlmechanismus, Pipelines, Abstimmung, Ergebnisablage) existiert noch nicht.
- Rechenzeit: Im Pilot brauchte TabPFN-3.5 auf der CPU 68 bis 114 Sekunden je
  Bedingung bei 569 Fällen. Der PC hat eine GPU (RTX 5070 Ti, 16 GB); dort
  braucht derselbe Pilot etwa 0,3 Sekunden je Bedingung nach dem Laden des
  Modells, bei identischen Metriken und identischem Checkpoint (Pilotprotokoll,
  Abschnitt „Wiederholung am PC mit GPU“). Auf WDBC ist Rechenzeit damit kein
  Engpass. Spambase (4 601 Fälle) am 23.11.2026 gemessen (Pilotprotokoll,
  Abschnitt „Laufzeittest auf Spambase“): 15 bis 46 Sekunden je
  TabPFN-Bedingung, hochgerechnet etwa 13 Minuten je Wiederholung mit drei
  Fehlmechanismen, also rund 4,3 Stunden für 20 Wiederholungen. Diese grobe
  Hochrechnung betrifft nur Spambase und setzt voraus, dass MAR und MNAR
  ähnlich lange wie MCAR dauern; Tuning und andere Datensätze fehlen.
  Im Test half `memory_saving_mode=True`; bei `auto` waren zwei Läufe mit
  hoher GPU-Speicherauslastung sehr langsam und wurden abgebrochen. Die
  vollständige Hauptversuchspipeline und MAR/MNAR sind noch nicht getestet.
- `requirements.txt` enthält Versionsbereiche und kein `torch`; eine exakte
  Sperre fehlt noch. PC und Laptop haben verschiedene torch-Versionen (siehe
  Umgebung). Für den Hauptversuch zählt die PC-Umgebung.
- Hinweise aus der Exposé-Evaluation vom 15.11.2026 für das Design. Die Datei
  ist gelöscht; die Punkte wurden am PC aus ihr gelesen und sind nicht erneut
  nachgeprüft. Die Zahlen stammen aus einem Kurzcheck nur mit LightGBM und sind
  keine Ergebnisse:
  - Kein Kriterium, ab wann eine Veränderung des Abstands zählt. Die Streuung
    zwischen Splits wurde auf 0,01 bis 0,03 Balanced Accuracy geschätzt;
    vorgeschlagen war eine vorab festgelegte kleinste relevante Veränderung
    (z. B. 0,01) mit Intervallen über die Wiederholungen.
  - Unter MCAR unterschieden sich interne Verarbeitung und Median bei LightGBM
    kaum; unter einer informativen Maskenregel entstand ein Effekt, je
    Datensatz sehr unterschiedlich.
  - Auf Spambase und QSAR ist ein großer Teil der Zellen gleich dem
    Spaltenmedian; nominell gleiche Fehlraten bedeuten dann je Datensatz
    unterschiedlich viel Informationsverlust unter Median-Imputation.
  - Ionosphere, WDBC und QSAR kommen laut der Evaluation in der
    TabPFN-Originalarbeit vor (Tabellen 7 und 8); vor Verwendung am Volltext
    prüfen, gehört in die Limitationen.
  - Offen: Rolle der Validierungsdaten für TabPFN, verschachtelte statt
    unabhängiger Masken je Fehlrate, zweites Gradient-Boosting-Verfahren, bei
    MAR und MNAR keine direkte Abhängigkeit der Maske vom Klassenlabel.

### Schreiben

- `writing/thesis/chapters/` enthält Überschriften und Seitenbudgets, keinen
  Fließtext.
- Mit dem Schreiben wurde noch nicht begonnen; das ist so geplant.
- Deckblattangaben in `main.tex` sind vollständig (PLZ, Ort, Betreuer).

## Bis zum Betreuertermin am 27. November 2026

Der Termin wurde laut Nutzer am 25.11. verschoben. Die Recherche wurde noch
nicht begonnen. Ziel ist ein nachvollziehbarer erster Zwischenstand, keine
abgeschlossene Literaturanalyse.

Vorbereitung:

1. Suchprotokoll an den neuen Suchbeginn anpassen und eine erste Google-Scholar-
   Suche samt tatsächlichem Sichtungsbereich und Trefferzahlen protokollieren.
2. Titel und Abstracts sichten und bei einer passenden Arbeit exemplarisch
   eine Matrixzeile anhand des Volltexts prüfen.
3. Die Fragen unten und den vorläufigen Zeitplan für das Gespräch vorbereiten;
   Ergebnisse des Treffens anschließend festhalten.

Bis dahin kein Kapiteltext.

## Vorläufiger Zeitplan bis zur Abgabe

Planungsvorschlag vom 25.11.2026 (PC), abhängig von verfügbarer Arbeitszeit,
Feiertagen und Rückmeldung der Betreuung; Fristen sind interne Meilensteine.

| Zeitraum | Ziel |
|---|---|
| 25.–27.11. | Rechercheablauf und erste Suche vorbereiten; Betreuungsgespräch |
| 28.11.–11.12. | Suchläufe, Screening, Zitationssuche und Volltextprüfung; Konzeptmatrix aufbauen |
| 12.–18.12. | Literatursynthese und erste Rohfassung Kapitel 3; Experimentdetails vorläufig ableiten |
| 19.12.–03.01. | Experimentpipeline und Tests implementieren; Design, Seeds und Umgebung vor Hauptversuch festlegen; Grundlagen/Methodik beginnen |
| 04.–10.01. | End-to-End-Generalprobe und Hauptversuch am PC; Ergebnisse sichern |
| 11.–17.01. | Auswertung, Abbildungen, Ergebniskapitel und Methodikrohfassung |
| 18.–24.01. | Grundlagen und Diskussion; FF1 und FF2 anhand der Befunde bearbeiten |
| 25.01.–01.02. | Einleitung, Fazit, Abstract; vollständige Rohfassung |
| 02.–15.02. | Zwei Wochen Überarbeitung, Quellen- und Formprüfung, Abgabevorbereitung und Puffer |
| 16.02. | Abgabe |

Fragen an den Betreuer:

- Datenbanken: nur Google Scholar und arXiv wie im Exposé oder auch Scopus,
  IEEE Xplore, ACM Digital Library (und AISeL)?
- Zitierstil IEEE laut Folien, obwohl die Vorlage auf LNCS steht?
- Umfang von MAR und MNAR (Varianten aus Punkt 3)?
- Reichen vier Datensätze, wie viele Wiederholungen sind angemessen?
- Sind statistische Tests verlangt, oder reicht eine deskriptive Auswertung mit
  vorab festgelegter Schwelle?
- Erwartetes Verhältnis von Literatur- zu Praxisteil und verbindlicher Umfang?
- Form der Angabe der KI-Nutzung im Anhang?

## Nächste Schritte

1. Datenbanken festlegen und Exposé und Suchprotokoll angleichen.
2. Datenbanksuche S1 bis S4 durchführen und jede Suche am selben Tag ins
   Such-Log eintragen.
3. Die neun Matrixzeilen am Volltext prüfen, `?` auflösen, Status fortschreiben;
   TabPFN-2.5-Bericht und Ke et al. ergänzen.
4. Rückwärts- und Vorwärtssuche zu den Kernarbeiten, Kandidaten prüfen.
5. Aus der Synthese MAR- und MNAR-Regeln ableiten und die offenen
   Designentscheidungen festlegen.
6. Parallel zur Recherche das Gerüst des Hauptversuchs planen; der
   Spambase-Laufzeittest ist erledigt, der vollständige Versuch bleibt offen.

## Umgebung

| Rechner | Stand |
|---|---|
| Laptop | Python 3.12 mit `.venv` wie im Pilot (tabpfn 9.2.0, lightgbm 4.7.0, torch 2.15.0 nur CPU); Checkpoint und Zugang vorhanden; MiKTeX 25.12, Pakete der Lehrstuhlvorlage am 20.11.2026 nachinstalliert, `build.ps1` läuft durch (12 Seiten) |
| PC | GPU: NVIDIA GeForce RTX 5070 Ti, 16 GB, Treiber 610.88. Python 3.12.10 mit `.venv`: torch 2.11.0+cu128 (CUDA 12.8, GPU wird erkannt), tabpfn 9.2.0, lightgbm 4.7.0, numpy 2.5.3, pandas 3.0.6, scikit-learn 1.9.1, scipy 1.18.1. TabPFN wählt das Gerät automatisch (`device='auto'`). Checkpoint `tabpfn-v3.5-20260909.safetensors` unter `%APPDATA%\tabpfn\` mit derselben SHA256 wie im Pilotprotokoll; Zugang eingerichtet. MiKTeX 25.12, `biblatex-ieee` vorhanden, `build.ps1` läuft durch (12 Seiten, geprüft am 23.11.2026). `latexmk` funktioniert nicht (kein Perl), deshalb `build.ps1`. Repository liegt in einem OneDrive-Ordner |

Hinweise zur Umgebung:

- Der Browser-Login von `tabpfn` bricht unter Windows ab (`WinError 10038`).
  Der Token wurde am 19.11.2026 von Hand in `~/.cache/tabpfn/auth_token`
  abgelegt. Er stand dabei im Klartext im Chat; im Prior-Labs-Konto erneuern,
  falls noch nicht geschehen.
- Am PC wurde torch über den CUDA-Index installiert (siehe README), am Laptop
  von PyPI. Die Versionen unterscheiden sich deshalb (2.11.0+cu128 gegenüber
  2.15.0). Solange nur am PC gerechnet wird, ist das unkritisch; für den
  Hauptversuch die PC-Versionen exakt festhalten.

## KI-Nutzung (für den Anhang)

Der Lehrstuhl verlangt, die Nutzung von KI-Tools im Anhang anzugeben.

| Datum | Werkzeug | Wofür |
|---|---|---|
| 19.11.2026 | GitHub Copilot in VS Code (PC) | Bestandsaufnahme des Repositorys und Startplan; Thesis-Gerüst aus der Lehrstuhlvorlage mit Kapiteldateien und `build.ps1`; Vorlagen für Suchprotokoll und Konzeptmatrix (Matrixzeilen aus Exposé und Abschlussabgleich vorbefüllt, nicht am Volltext geprüft); Einrichtung der GPU-Umgebung und des TabPFN-Zugangs; Download der arXiv-Fassung von Perez-Lebel et al.; kein Text der Arbeit erzeugt |
| 20.11.2026 | GitHub Copilot in VS Code (PC) | Commit und Push des Stands |
| 20.11.2026 | GitHub Copilot in VS Code | Durchsicht des Repositorys, Einrichtung von Arbeitsanweisungen und Projektstand, Reparatur der LaTeX-Umgebung am Laptop, Umstellung des Zitierstils auf IEEE; kein Text der Arbeit erzeugt |
| 21.11.2026 | GitHub Copilot in VS Code | Vorschlag für die Vorbereitung des Betreuertermins am 25.11.2026 (Prioritäten, Fragenliste) |

| 23.11.2026 | GitHub Copilot in VS Code (PC) | Durchsicht der Laptop-Änderungen, Ergänzung des Projektstands um den PC-Stand, Wiederholung des Piloten auf der GPU, Laufzeittest auf Spambase mit Skripten und Diagnose des Speicherproblems |

Frühere Nutzung (Recherche, Exposé, Pilotcode) bitte nachtragen.

## Weiterhin offen aus der Übergabe

Der PC-Chat vom 19. und 20.11.2026 ist oben eingearbeitet. Nicht darin
enthalten und nur vom Nutzer zu ergänzen:

- Entscheidungen und Begründungen aus dem Betreuergespräch (eingearbeitet mit
  den Commits vom 13.11.2026), die nicht im Exposé stehen. Die Ergebnisnotiz in
  `notizen.md` war leer, die Datei ist gelöscht.
- verbindliche Vorgaben zu Umfang und Abgabeform

# Projektstand

Fortlaufend gepflegter Stand der Bachelorarbeit. Dauerhafte Arbeitsregeln stehen
in [.github/copilot-instructions.md](.github/copilot-instructions.md).

Zuletzt aktualisiert: 23. November 2026 (Laptop). Erstfassung aus dem Inhalt des
Repositorys erstellt. Was nur im Chat am PC besprochen wurde und nicht im
Repository steht, fehlt hier und ist unter „Vom PC-Chat zu ergänzen“ nachzutragen.

## Eckdaten

| Punkt | Stand |
|---|---|
| Abgabedatum laut `writing/thesis/main.tex` | 16. Februar 2027 |
| Erstgutachter | Prof. Dr. Stefan Schönig |
| Betreuer | Maximilian Metzner |
| Letzter Stand beim Betreuer | Exposé abgegeben, Bachelorarbeit angemeldet (Angabe des Nutzers vom 21.11.2026) |
| Nächster Betreuertermin | Mittwoch, 25. November 2026 |
| Seitenbudget laut Kapitelgerüst | ca. 40 Seiten ohne Anhang (4, 7, 6, 6, 9, 6, 2) |
| Phase | Literaturanalyse (FF1) beginnt; Kapitel sind Gerüste ohne Text |

## Entscheidungen

| Datum | Entscheidung | Quelle |
|---|---|---|
| 06.11.2026 | Fokus auf fehlende Merkmalswerte; Fehlraten 0, 10, 30, 50 %; Training, Validierung und Test separat und unabhängig mit derselben Zielfehlrate maskiert | Abschlussabgleich |
| 06.11.2026 | Kern: interne Verarbeitung gegen Median-Imputation; Median mit Missing-Indikatoren als Zusatzanalyse | Abschlussabgleich |
| 09.11.2026 | Technischer Pilot auf WDBC abgeschlossen; Checkpoint `tabpfn-v3.5-20260909.safetensors` mit SHA256 dokumentiert | Pilotprotokoll |
| 13.11.2026 | Nach Betreuergespräch: Titel und Forschungsfragen auf Ebene der Modellansätze formuliert; TabPFN-3.5 und LightGBM sind austauschbare Vertreter | Commits `be17761`, `24e045e` |
| 13.11.2026 | Fehlmechanismus ist Versuchsfaktor; MCAR als Referenz, MAR und MNAR vorgesehen, Umfang wird nach der Literaturanalyse festgelegt | Exposé |
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
  Bisher liegen nur die Grundlagenpaper der Startmenge vor.
- Konzeptmatrix: 9 Arbeiten, alle mit Status „vorbefüllt, am Volltext prüfen“,
  21 Zellen mit `?`. In der Matrix fehlen aus der Startmenge der
  TabPFN-2.5-Bericht und Ke et al. (2017).
- Lokal fehlt TabImpute in der Fassung arXiv v6; für Ke et al. (2017) und Rubin
  (1976) liegt kein PDF vor.
- Acht ungeprüfte Kandidaten stehen im Suchprotokoll, Abschnitt 6.
- In `references.bib` vorhanden, aber nirgends zitiert:
  `cooper_organizing_1988`, `page_prisma_2021` (vermutlich für Kapitel 3.1),
  `hu_noise_2026`, `liu_repeated_2026`, `zhao_alignment_2026` (früherer Zuschnitt).

### Experiment (FF2)

- Vorhanden sind nur der Pilot `experiments/pilot_tabpfn_wdbc.py` und der
  Ladetest. Code für den Hauptversuch (Splits mit Gruppen, Maskierung je
  Fehlmechanismus, Pipelines, Abstimmung, Ergebnisablage) existiert noch nicht.
- Rechenzeit: Im Pilot brauchte TabPFN-3.5 auf der CPU 68 bis 114 Sekunden je
  Bedingung bei 569 Fällen. Mit drei Fehlmechanismen wächst die Zahl der
  Bedingungen gegenüber der Schätzung im Pilotprotokoll deutlich. Gerechnet wird
  nur am PC. Vor der Festlegung der Wiederholungszahl ist dort ein Laufzeittest
  auf Spambase nötig; ob der PC eine GPU hat, ist hier nicht bekannt.
- `requirements.txt` enthält Versionsbereiche; eine exakte Sperre fehlt noch.

### Schreiben

- `writing/thesis/chapters/` enthält Überschriften und Seitenbudgets, keinen
  Fließtext.
- Mit dem Schreiben wurde noch nicht begonnen; das ist so geplant.
- Deckblattangaben in `main.tex` sind vollständig (PLZ, Ort, Betreuer).

## Bis zum Betreuertermin am 25. November 2026

Vorschlag vom 21.11.2026 (Laptop); am 23.11.2026 war davon laut Repository noch
nichts begonnen.

Pflicht:

1. Erste Suchrunde mit S1 und S2 in Google Scholar, arXiv und Scopus, jede
   Suche sofort im Such-Log eintragen (macht der Nutzer selbst, Uni-Zugang).
2. Konzeptmatrix am Volltext prüfen, zuerst Zaimoğlu (trägt die Abgrenzung im
   Exposé); TabPFN-2.5-Bericht, Ke et al. und neue Treffer ergänzen.
3. Ein bis zwei Varianten für den Umfang von MAR und MNAR mit Zahl der
   Rechenläufe (z. B. alle Mechanismen voll oder MCAR voll und MAR/MNAR nur bei
   einer Fehlrate).

Wenn Zeit bleibt:

4. Laufzeittest auf Spambase am PC als Grundlage für Punkt 3.
5. Zeitplan rückwärts vom 16. Februar 2027 mit zwei Wochen Überarbeitung.

Bis dahin kein Kapiteltext.

Fragen an den Betreuer:

- Datenbanken: nur Google Scholar und arXiv wie im Exposé oder auch Scopus,
  IEEE Xplore, ACM Digital Library (und AISeL)?
- Zitierstil IEEE laut Folien, obwohl die Vorlage auf LNCS steht?
- Umfang von MAR und MNAR (Varianten aus Punkt 3)?
- Reichen vier Datensätze, wie viele Wiederholungen sind angemessen?
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
6. Parallel: Laufzeittest auf Spambase und Gerüst des Hauptversuchs.

## Umgebung

| Rechner | Stand |
|---|---|
| Laptop | Python 3.12 mit `.venv` wie im Pilot (tabpfn 9.2.0, lightgbm 4.7.0, torch 2.15.0 nur CPU); Checkpoint und Zugang vorhanden; MiKTeX 25.12, Pakete der Lehrstuhlvorlage am 20.11.2026 nachinstalliert, `build.ps1` läuft durch (12 Seiten) |
| PC | hier nicht bekannt, bitte ergänzen (GPU, Paketversionen) |

## KI-Nutzung (für den Anhang)

Der Lehrstuhl verlangt, die Nutzung von KI-Tools im Anhang anzugeben.

| Datum | Werkzeug | Wofür |
|---|---|---|
| 20.11.2026 | GitHub Copilot in VS Code | Durchsicht des Repositorys, Einrichtung von Arbeitsanweisungen und Projektstand, Reparatur der LaTeX-Umgebung am Laptop, Umstellung des Zitierstils auf IEEE; kein Text der Arbeit erzeugt |
| 21.11.2026 | GitHub Copilot in VS Code | Vorschlag für die Vorbereitung des Betreuertermins am 25.11.2026 (Prioritäten, Fragenliste) |

Frühere Nutzung (Recherche, Exposé, Pilotcode) bitte nachtragen.

## Vom PC-Chat zu ergänzen

- Entscheidungen und Begründungen aus dem Betreuergespräch (eingearbeitet mit
  den Commits vom 13.11.2026), die nicht im Exposé stehen
- Anmeldestatus und verbindliche Termine
- geplante, aber noch nicht umgesetzte Schritte und verworfene Alternativen

# Suchprotokoll zur Literaturanalyse (FF1)

Arbeitsdokument für Kapitel 3.1 und Anhang A. Jede Suche wird am selben Tag
eingetragen, auch wenn sie nichts Neues bringt. Die ausgewerteten Arbeiten
stehen in der [Konzeptmatrix](./Konzeptmatrix.csv).

## 1. Ziel und Reviewtyp

FF1: Welche Befunde und Grenzen berichtet die aktuelle Literatur zur
Klassifikation auf tabellarischen Daten mit fehlenden Merkmalswerten bei
Tabular Foundation Models und Gradient Boosting, und welcher empirische
Untersuchungsbedarf ergibt sich daraus?

Einordnung nach Cooper (Vorschlag, im Methodenteil begründen):

| Merkmal | Ausprägung |
|---|---|
| Fokus | Forschungsergebnisse und Evaluationsmethoden |
| Ziel | Integration der Befunde, Identifikation des offenen Untersuchungsbedarfs |
| Perspektive | neutral |
| Abdeckung | repräsentativ und auf zentrale Arbeiten gerichtet, nicht erschöpfend |
| Organisation | konzeptuell (Konzeptmatrix nach Webster und Watson) |
| Zielgruppe | Fachpublikum |

## 2. Vorgehen

Die Literaturrecherche wird neu durchgeführt und ab dem ersten Suchlauf
dokumentiert. Der bereits vorhandene Bestand aus Themenfindung und Exposé
(Abschnitt 6) bleibt erhalten, ist aber kein Ergebnis dieser Suche. Er wird
nicht automatisch in die Synthese aufgenommen.

Es gibt zwei miteinander verbundene Wege:

- **FF1-Suche:** Arbeiten zu fehlenden Merkmalswerten bei den Modellansätzen
  suchen, sichten und für die Literaturanalyse auswählen. Suchläufe und
  Auswahl werden in den Abschnitten 7 bis 10 dokumentiert.
- **Grundlagen und Kontext:** Quellen für die Erklärung von Begriffen,
  Modellansätzen und Verfahren gezielt nutzen oder suchen, auch wenn sie
  fehlende Werte nicht untersuchen. Solche Quellen sind nicht automatisch
  FF1-Studien; ihren Fundweg und Zweck getrennt in Abschnitt 8a festhalten.
  Sie können auch für FF1 relevant sein, wenn sie die dortigen Kriterien
  erfüllen.

Die vorhandenen Modell- und Grundlagenarbeiten dürfen für den Hintergrund
genutzt werden: Ihre ursprüngliche Auswahl muss nicht nachträglich als
Datenbanksuche ausgegeben werden. Für konkrete Aussagen sind die passenden
Volltextstellen zu prüfen. Wird eine dieser Arbeiten bei einem neuen Suchlauf
erneut gefunden, wird dieser tatsächliche Fund zusätzlich dokumentiert.

1. **Datenbanksuche:** Suchstrings aus Abschnitt 3 an die jeweilige Datenbank
   anpassen; Datum, genaue Eingabe, Filter, Treffer und gesichteten Bereich
   in Abschnitt 7 festhalten.
2. **Auswahl:** Treffer erfassen, Dubletten prüfen und Titel und Abstracts
   anhand der Auswahlkriterien sichten; relevante oder unklare Volltexte prüfen.
3. **Zitationssuche:** Literaturverzeichnisse einschlägiger Arbeiten
   rückwärts und zitierende Arbeiten vorwärts durchsuchen; Ausgangsarbeit,
   gesichteten Bereich und neue Kandidaten in Abschnitt 8 dokumentieren.
4. **Bestand abgleichen:** Bereits vorhandene Arbeiten nach denselben Kriterien
   prüfen. Werden sie bei einer Suche oder Zitationssuche gefunden, den
   tatsächlichen Fundweg festhalten. Gezielt ergänzte Arbeiten getrennt als
   solche dokumentieren; Grundlagen und Kontext separat einordnen.
5. **Synthese:** Ausgewählte Arbeiten anhand der Volltexte und Fundstellen in
   die Konzeptmatrix eintragen. Vorbefüllte Angaben bleiben ungeprüft, bis sie
   am Volltext bestätigt wurden.
6. **Abbruch:** Nach den vereinbarten Suchläufen und einer weiteren
   dokumentierten Zitationsrunde ohne neue relevante Arbeiten kann die Suche
   vorläufig abgeschlossen werden. Das ist kein Vollständigkeitsnachweis.

## 3. Suchbegriffe und konkrete Suchläufe

### 3.1 Start in Google Scholar

Jede Zeile ist eine **eigene Suchanfrage**, kein einzelner Begriff und keine
Anweisung, alle Anfragen auf einmal einzugeben. Die Liste ist ein Arbeitsplan,
kein Nachweis bereits durchgeführter Suchen. Je nach Treffern später weitere
Varianten ergänzen und genau so protokollieren, wie sie tatsächlich eingegeben
wurden.

| ID | Eingabe in Google Scholar | Zweck |
|---|---|---|
| S1a | `"TabPFN" "missing values"` | Einstieg: TabPFN und fehlende Werte |
| S1b | `"tabular foundation models" "missing data"` | Breiterer Ansatz über TabPFN hinaus |
| S1c | `"TabPFN" imputation` | Weitere Arbeiten zur Behandlung fehlender Werte |
| S2a | `"TabPFN" "gradient boosting" "missing values"` | Mögliche direkte Vergleiche |
| S3a | `"gradient boosting" "missing values"` | Fehlende Werte bei Gradient Boosting |
| S3b | `"LightGBM" "missing values"` | Explorativ durchgeführt am 25.11.2026; laut Nutzer keine passende Arbeit zur Aufnahme identifiziert, keine weitere Suche vorgesehen (Details in Abschnitt 7) |
| S4a | `"missing data" imputation classification benchmark` | Vergleichsstudien zu Behandlungen |

**Erster Schritt:** S1a eingeben, angezeigte ungefähre Trefferzahl und
Sortierung notieren und Titel und – soweit verfügbar – Abstracts der
gesichteten Treffer prüfen. Für S1a unter `01 Suchtreffer` in Zotero eine
Untersammlung anlegen und die dort tatsächlich aufgenommenen Treffer
zuordnen. Eine Untersammlung ist für einen Suchlauf, nicht für jedes PDF.
RIS-Export und Suchangaben wie in Abschnitt 7 dokumentieren. Treffer können
für mehrere Suchläufe relevant sein und mehreren Sammlungen zugeordnet werden.

Die erste Anfrage liefert nur einen **Einstieg**, keinen vollständigen
Grundbestand. Weder müssen alle angezeigten Treffer gespeichert werden noch
ist jeder gespeicherte Treffer bereits für FF1 ausgewählt. Suchergebnisse
und tatsächlichen Sichtungsbereich getrennt festhalten. Bei wenigen Treffern
die nächste Variante ausprobieren; bei vielen Treffern den tatsächlich
gesichteten Bereich dokumentieren.

### 3.2 Suchbausteine für weitere Datenbanken

Die folgenden Bausteine helfen beim Erweitern der Suche. Sie sind keine
Eingabe, die unverändert in Google Scholar übernommen werden muss;
Schreibweise und Operatoren sind an die jeweilige Datenbank anzupassen.

| Block | Begriffe |
|---|---|
| A Modell (TFM) | "TabPFN" OR "tabular foundation model*" OR "prior-data fitted network*" OR "TabICL" |
| B Modell (GB) | "gradient boosting" OR "LightGBM" OR "XGBoost" OR "CatBoost" OR "gradient boosted trees" |
| C Fehlende Werte | "missing values" OR "missing data" OR "missingness" OR "imputation" OR "missing indicator*" OR "MCAR" OR "MAR" OR "MNAR" |
| D Aufgabe | "classification" OR "prediction" OR "supervised learning" |

| ID | Kombination | Zweck |
|---|---|---|
| S1 | A AND C | Fehlende Werte bei Tabular Foundation Models (Kern); S1a–c sind erste Varianten |
| S2 | A AND B AND C | Direkter Vergleich beider Modellansätze |
| S3 | B AND C AND D | Fehlende Werte bei Gradient Boosting; bei vielen Treffern gezielt eingrenzen und Eingrenzung begründen |
| S4 | C AND D AND ("benchmark" OR "comparison") AND ("tabular") | Vergleichsstudien zu Behandlungen |

Eine Jahresbegrenzung ab 2018 war für S3 vorgeschlagen, ist aber keine
automatische Voraussetzung: Sie kann ältere Grundlagen und relevante Arbeiten
ausschließen und muss vor Anwendung begründet und protokolliert werden.

### 3.3 Grundlagen gezielt ergänzen

Für Kapitel 2 werden Quellen zu den jeweils zu erklärenden Themen benötigt,
nicht zwingend eine einzelne umfassende Datenbanksuche. Zuerst den vorhandenen
Bestand und das Exposé prüfen, dann Lücken gezielt suchen:

| Thema | Ausgangspunkt beziehungsweise Beispiel für eine gezielte Suche |
|---|---|
| PFN und TabPFN | PFN-Grundlage und TabPFN-Originalarbeit aus dem Exposé; bei Bedarf `"prior data fitted networks"` |
| TabPFN-Versionen | vorhandene Nature-Arbeit und Modellberichte; die jeweils relevante Version prüfen |
| Gradient Boosting und LightGBM | vorhandener LightGBM-Eintrag; bei Bedarf `"gradient boosting" classification` und `"LightGBM"` |
| Fehlende Werte, MCAR/MAR/MNAR und Behandlungen | vorhandener Rubin-Eintrag; bei Bedarf `"missing data" MCAR MAR MNAR` und `"missing values" imputation classification` |

Das sind Such- und Lesestartpunkte, keine bereits geprüften Aussagen und keine
automatische Auswahl für FF1. Treffer aus einer gezielten Grundlagensuche
können in Zotero unter `04 Grundlagen` gesammelt werden; bei FF1-Relevanz
zusätzlich entsprechend zuordnen. Die tatsächlich verwendeten Quellen und
Fundwege in Abschnitt 8a festhalten. Aussagen später am Volltext mit
Fundstellen belegen.

## 4. Datenbanken

Scopus, IEEE Xplore, ACM Digital Library, Google Scholar und arXiv. Bei
Google Scholar werden nur die ersten 50 Treffer je Suche gesichtet. Preprints
werden nur aufgenommen, wenn keine publizierte Fassung existiert.

## 5. Ein- und Ausschlusskriterien (Vorschlag)

Einschluss:

- E1: Überwachtes Lernen auf tabellarischen Daten mit fehlenden Merkmalswerten.
- E2: Mindestens ein Tabular Foundation Model oder ein Gradient-Boosting-Verfahren.
- E3: Bewertet wird die Vorhersageleistung, oder die Arbeit beschreibt, wie das
  Modell fehlende Werte verarbeitet.
- E4: Deutsch oder Englisch, Volltext zugänglich.

Ausschluss:

- A1: Nur Rekonstruktionsgüte der Imputation ohne nachgelagerte Vorhersage
  (wird als Kontext genannt, nicht in die Synthese aufgenommen).
- A2: Fehlende Zielwerte statt fehlender Merkmalswerte.
- A3: Zeitreihen, Bilder oder Text ohne tabellarischen Vorhersageteil.
- A4: Keine nachvollziehbare Methodenbeschreibung.

## 6. Vorhandener Bestand

Die folgende Liste dokumentiert bereits vorhandene beziehungsweise im Exposé
verwendete Arbeiten. Sie gilt weder als Ergebnis der neuen Recherche noch als
Liste automatisch eingeschlossener Studien.

| Arbeit | BibTeX-Schlüssel | PDF lokal | In Matrix |
|---|---|---|---|
| Zaimoğlu (2026) | zaimoglu_tabpfn_2026 | ja | vorbefüllt |
| Perez-Lebel et al. (2022) | perez_benchmarking_2022 | ja (arXiv-Fassung) | vorbefüllt |
| Luo et al. (2025), TIME | luo_time_2025 | ja | vorbefüllt |
| Feitelberg et al. (2026), TabImpute | feitelberg_pipeline_2026 | nur ältere Fassung, v6 fehlt | vorbefüllt |
| Tran und Byeon (2024) | tran_predicting_2024 | ja | vorbefüllt |
| Hollmann et al. (2025), Nature | hollmann_accurate_2025 | ja | vorbefüllt |
| Hollmann et al. (2023), TabPFN | hollmann_tabpfn_2023 | ja | vorbefüllt |
| TabPFN-2.5-Bericht | grinsztajn_tabpfn-25_2026 | ja | offen |
| TabPFN-3.5-Bericht | jager_tabpfn-35_2026 | ja | vorbefüllt |
| Grinsztajn et al. (2022) | grinsztajn_why_2022 | ja | vorbefüllt |
| Ke et al. (2017), LightGBM | ke2017lightgbm | nein | offen |
| Rubin (1976) | rubin_inference_1976 | nein | Grundlage, nicht in Matrix |

## 7. Such-Log

Pro Suchlauf eine Zeile führen. Bei Google Scholar die angezeigte Trefferzahl
als Schätzung kennzeichnen und den tatsächlich gesichteten Bereich eintragen.
Die Zahl im RIS-Export ist nicht automatisch die Zahl der gesichteten oder
nach Titel-/Abstractprüfung behaltenen Arbeiten. Überschneidungen zwischen
Suchläufen getrennt erfassen und erst beim Abgleich bereinigen.

Zotero-RIS-Dateien können unter
[`literature/recherche/exporte/`](../recherche/exporte/README.md) für den
Abgleich abgelegt werden. Eine Anleitung liegt dort; die RIS-Dateien bleiben
lokal und werden nicht mit Git übertragen. Fehlende Angaben im Log offen
lassen und nicht aus einem Export erraten.

| Datum | Datenbank | Suchstring (ID und genaue Eingabe) | Felder, Filter und Sortierung | Angezeigte Treffer | Gesichtet (Bereich/Anzahl) | RIS-Datei und enthaltene Auswahl | Nach Titel/Abstract behalten | Neu gegenüber Bestand |
|---|---|---|---|---|---|---|---|---|
| 25.11.2026 | Google Scholar | S1a: `"TabPFN" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 1 310 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1a--TabPFN- -missing values-.ris`, 16 Einträge; nur die als passend oder unklar gespeicherten Treffer | 16 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 9 (siehe 7.1) |
| 25.11.2026 | Google Scholar | S1b: `"tabular foundation models" "missing data"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 236 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1b--tabular foundation models- -missing data-.ris`, 8 Einträge; nur die als passend oder unklar gespeicherten Treffer | 8 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 5 neu gegenüber Bestand und S1a (siehe 7.1); 2 Überschneidungen mit S1a |
| 25.11.2026 | Google Scholar | S1c: `"TabPFN" imputation` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 1 350 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1c--TabPFN- imputation.ris`, 16 Einträge; nur die als passend oder unklar gespeicherten Treffer | 16 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 5 Titel neu gegenüber S1a/S1b (siehe 7.1); 11 Überschneidungen |
| 25.11.2026 | Google Scholar | S2a: `"TabPFN" "gradient boosting" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 771 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S2a--TabPFN- -gradient boosting- -missing values-.ris`, 9 Einträge; nur die als passend oder unklar gespeicherten Treffer | 9 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 3 Titel neu gegenüber S1a–S1c (siehe 7.1); 6 Überschneidungen |
| 25.11.2026 | Google Scholar | S3a: `"gradient boosting" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 62 900 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S3a--gradient boosting- -missing values-.ris`, 18 RIS-Einträge; eine Arbeit doppelt exportiert (17 unterschiedliche Titel) | 18 gespeichert; Titel-/Abstractscreening noch offen | Perez-Lebel et al. ist bereits im Bestand; übrige Treffer mit früheren Exporten abgleichen (siehe 7.1) |
| 25.11.2026 | Google Scholar | S3b: `"LightGBM" "missing values"` | Sortierung und Filter nicht dokumentiert | nicht dokumentiert | Sichtungsbereich nicht dokumentiert | Kein RIS-Export im Exportordner | Laut Nutzer keine passende Arbeit zur Aufnahme identifiziert; Umfang des Screenings nicht dokumentiert | nicht quantifiziert |

### 7.1 Gespeicherte Treffer je Suchlauf

Angaben aus den Metadaten des RIS-Exports, nicht am Volltext geprüft. „Bestand“
heißt: Die Arbeit lag schon vor dem Neustart vor (Abschnitt 6 oder Zotero-Sammlung
„00 Vorhandener Bestand“) und stand laut Nutzer zusätzlich in der Trefferliste
dieser Suche.

**S1a (25.11.2026)**

| Nr. | Arbeit laut Export | Ort laut Export | Bestand oder neu |
|---|---|---|---|
| 1 | Hollmann et al. (2025), Accurate predictions on small data with a tabular foundation model | Nature | Bestand |
| 2 | Tran und Byeon (2024), Predicting dementia in Parkinson's disease … hybrid LightGBM–TabPFN and SHAP | im Export ohne Autor-, Jahres- und Ortsfeld | Bestand |
| 3 | Luo et al. (2025), TIME: TabPFN-Integrated Multimodal Engine … | arXiv | Bestand |
| 4 | Luo et al. (2026), TIMF: TabPFN-integrated multimodal framework for robust tabular-image learning | Neurocomputing | neu; vermutlich publizierte Fassung von Nr. 3, zu prüfen |
| 5 | Zhou et al. (2026), Prediction of cognitive impairment in Parkinson’s disease using TabPFN … | Frontiers in Aging Neuroscience | neu |
| 6 | Sepin (2026), Multiple Imputation of a Continuous Outcome with Fully Observed Predictors Using TabPFN | Stats | Bestand |
| 7 | Hollmann et al. (2023), TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second | arXiv | Bestand |
| 8 | van Leeuwen (2025), Conformal Prediction for Tabular Prior-Data Fitted Networks with Missing data | EurIPS 2025 Workshop: AI for Tabular Data | neu |
| 9 | Zaimoğlu (2026), Evaluation of TabPFN’s Performance Consistency Under Controlled MCAR Conditions … | IDAP 2026 | Bestand |
| 10 | Sepin (2026), Multiple Imputation Using Pretrained Foundation Models: A TabPFN-Based Approach | Preprints | neu; Verhältnis zu Nr. 6 zu prüfen |
| 11 | Bi et al. (2026), Missing-Aware Imbalanced Learning Pathways for Manufacturing Process Quality Assessment | METMS 2026 | neu |
| 12 | Neunhoeffer, Learning from Small Data: Tabular Foundation Models for Political Science | im Export ohne Jahr und Ort | neu |
| 13 | Rawat et al. (2025), A Fast and Reliable Transformer-Based TabPFN Model for Liver Disease Diagnosis | Cureus Journal of Computer Science | neu |
| 14 | Zhou et al. (2027 laut Export), Predicting fatal helicopter accidents with missing data … | Reliability Engineering & System Safety | neu |
| 15 | Grinsztajn et al. (2026), TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models | arXiv | Bestand |
| 16 | Grinsztajn et al. (2026), TabPFN-3: Technical Report | arXiv | neu; nicht identisch mit dem TabPFN-3.5-Bericht im Bestand |

Offen zu S1a: unvollständige Metadaten bei
Nr. 2 und Nr. 12 in Zotero ergänzen; Entscheidung je Treffer nach Titel und
Abstract.

**S1b (25.11.2026)**

| Nr. | Arbeit laut Export | Ort laut Export | Bestand oder neu |
|---|---|---|---|
| 1 | Yang et al. (2024), UniTabE: A Universal Pretraining Protocol for Tabular Foundation Model in Data Science | International Conference on Learning Representations | neu |
| 2 | Ren et al. (2025), Deep Learning within Tabular Data: Foundations, Challenges, Advances and Future Directions | arXiv | neu |
| 3 | Jha et al. (2026), A Survey of Large Language Models for Tabular Data Imputation: Tuning Paradigms and Challenges | Springer Nature Switzerland (Konferenzband, Titel fehlt im Export) | neu |
| 4 | Feitelberg et al. (2026), One Pipeline, Many Transformers: Pattern-Specific Imputation Specialists for Tabular Missing Data | arXiv | Bestand |
| 5 | Hollmann et al. (2025), Accurate predictions on small data with a tabular foundation model | Nature | Bestand; auch in S1a |
| 6 | Jiang et al. (2026), Representation Learning for Tabular Data: A Comprehensive Survey | IEEE Transactions on Pattern Analysis and Machine Intelligence | neu |
| 7 | Delouee et al. (2026), A Comparative Framework for Evaluating Foundation Models on Tabular Data: A Case Study in Healthcare | arXiv | neu |
| 8 | Grinsztajn et al. (2026), TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models | arXiv | Bestand; auch in S1a |

Anmerkung des Nutzers zu S1b: viele Treffer ohne Bezug zu fehlenden Werten,
deshalb wenige gespeichert. Offen: Entscheidung je Treffer nach Titel und
Abstract; Übersichtsarbeiten (Nr. 2, 3, 6) eher Kontext als FF1-Studie, zu
prüfen.

**S1c (25.11.2026)**

| Nr. | Arbeit laut Export | Ort laut Export | Status gegenüber früheren Exporten/Bestand |
|---|---|---|---|
| 1 | Sepin (2026), Multiple Imputation of a Continuous Outcome with Fully Observed Predictors Using TabPFN | Stats | Überschneidung mit S1a |
| 2 | Feitelberg et al. (2026), One Pipeline, Many Transformers: Pattern-Specific Imputation Specialists for Tabular Missing Data | arXiv | Überschneidung mit S1b; Bestand |
| 3 | Feitelberg et al. (2025), TabImpute: Accurate and Fast Zero-Shot Missing-Data Imputation with a Pre-Trained Transformer | im Export ohne Erscheinungsort | Neuer Titel im Export; möglicher Zusammenhang mit TabImpute/Einreichung 7944 im Bestand prüfen |
| 4 | Hollmann et al. (2025), Accurate predictions on small data with a tabular foundation model | Nature | Überschneidung mit S1a und S1b |
| 5 | Zhang et al. (2026), TabPFN: One Model to Rule Them All? | arXiv | Neuer Titel im Export |
| 6 | Zaimoğlu (2026), Evaluation of TabPFN’s Performance Consistency Under Controlled MCAR Conditions … | IDAP 2026 | Überschneidung mit S1a |
| 7 | Luo et al. (2026), TIMF: TabPFN-integrated multimodal framework for robust tabular-image learning | Neurocomputing | Überschneidung mit S1a |
| 8 | Ye et al. (2026), Evaluating TabPFN for Mild Cognitive Impairment to Alzheimer's Disease Conversion in Data Limited Settings | arXiv | Neuer Titel im Export |
| 9 | Hollmann et al. (2025), Accurate predictions on small data with a tabular foundation model | Nature | Duplikat von Nr. 4 und Überschneidung mit S1a/S1b |
| 10 | Liu et al. (2026), Causal Pre-training Under the Fairness Lens: An Empirical Study of TabPFN | ACM | Neuer Titel im Export |
| 11 | Luo et al. (2025), TIME: TabPFN-Integrated Multimodal Engine … | arXiv | Überschneidung mit S1a |
| 12 | Hollmann et al. (2023), TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second | arXiv | Überschneidung mit S1a |
| 13 | Tran und Byeon (2024), Predicting dementia in Parkinson's disease … hybrid LightGBM–TabPFN and SHAP | im Export ohne Autor-, Jahres- und Ortsfeld | Überschneidung mit S1a |
| 14 | Rametta et al. (2026), Are Random Forests Still ‘Good Enough’? Tabular Prior-Data Fitted Networks for Predictive and Causal Tasks | SocArXiv | Neuer Titel im Export |
| 15 | Grinsztajn et al. (2026), TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models | arXiv | Überschneidung mit S1a und S1b |
| 16 | Grinsztajn et al. (2026), TabPFN-3: Technical Report | arXiv | Überschneidung mit S1a |

Die Markierung „neuer Titel“ bedeutet nur, dass der Eintrag in S1a/S1b nicht
vorkam; sie ist keine Aussage zur Relevanz oder dazu, ob dieselbe Arbeit schon
im übrigen Bestand liegt. Offen: Screening der 16 Einträge nach Titel/Abstract,
Prüfung der möglichen TabImpute-Fassung und tatsächliche Auswahl.

**S2a (25.11.2026)**

| Nr. | Arbeit laut Export | Ort laut Export | Status gegenüber S1a–S1c |
|---|---|---|---|
| 1 | Hollmann et al. (2025), Accurate predictions on small data with a tabular foundation model | Nature | Überschneidung |
| 2 | Zaimoğlu (2026), Evaluation of TabPFN’s Performance Consistency Under Controlled MCAR Conditions … | IDAP 2026 | Überschneidung |
| 3 | Tran und Byeon (2024), Predicting dementia in Parkinson's disease … hybrid LightGBM–TabPFN and SHAP | im Export ohne Autor-, Jahres- und Ortsfeld | Überschneidung |
| 4 | Hollmann et al. (2023), TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second | arXiv | Überschneidung |
| 5 | Sepin (2026), Multiple Imputation Using Pretrained Foundation Models: A TabPFN-Based Approach | Preprints | Überschneidung |
| 6 | Grinsztajn et al. (2026), TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models | arXiv | Überschneidung |
| 7 | Ye et al. (2025), A Closer Look at Deep Learning Methods on Tabular Datasets | arXiv | Neuer Titel |
| 8 | Milosheski et al. (2026), Comparative Analysis of Neural Network Based Algorithms Against Tree Ensemble Algorithms on Tabular Data | ETAI International Conference | Neuer Titel |
| 9 | Zabërgja et al. (2025), Tabular Data: Is Deep Learning all you need? | arXiv | Neuer Titel |

Die Markierung „neuer Titel“ bedeutet nur, dass der Eintrag in den früheren
S1-Exporten nicht vorkam; sie ist keine Aussage zur Relevanz oder zum
Vorhandensein im übrigen Bestand. Screening nach Titel/Abstract steht aus.

**S3a (25.11.2026)**

RIS-Metadaten; Titel und Erscheinungsorte sind noch nicht am Volltext geprüft.
Der Export enthält eine doppelte Zotero-Aufnahme von Aydin und Öztürk.

| Nr. | Arbeit laut Export | Ort laut Export | Hinweis |
|---|---|---|---|
| 1 | Zhang et al. (2020), Predicting Missing Values in Medical Data Via XGBoost Regression | Journal of Healthcare Informatics Research | Imputation, trotz XGBoost im Titel keine Klassifikation aus dem Export ableitbar |
| 2 | Perez-Lebel et al. (2022), Benchmarking missing-values approaches for predictive models on health databases | GigaScience | Bereits im Bestand (Abschnitt 6); jetzt tatsächlich über S3a gefunden |
| 3 | Samad et al. (2022), Missing value estimation using clustering and deep learning within multiple imputation framework | Knowledge-Based Systems | — |
| 4 | Rusdah und Murfi (2020), XGBoost in handling missing values for life insurance risk prediction | SN Applied Sciences | — |
| 5 | Madhu et al. (2019), A Novel Algorithm for Missing Data Imputation on Machine Learning | ICSSIT | — |
| 6 | Batra et al. (2022), A Pragmatic Ensemble Strategy for Missing Values Imputation in Health Records | Entropy | — |
| 7 | Kurniadi et al. (2023), Local mean imputation for handling missing value to provide more accurate facies classification | Procedia Computer Science | — |
| 8 | Gorshenin et al. (2019), Application of Machine Learning Algorithms to Handle Missing Values in Precipitation Data | Springer conference volume | — |
| 9 | Kurucz et al., Methods for large scale SVD with missing values | Im Export ohne Erscheinungsort | — |
| 10 | Josse et al. (2024), On the consistency of supervised learning with missing values | Statistical Papers | — |
| 11 | Aydin und Öztürk, Performance Analysis of XGBoost Classifier with Missing Data | Im Export ohne Erscheinungsort | Doppelt im RIS-Export (Nr. 12); PDF liegt in Downloads |
| 12 | Aydin und Öztürk, Performance Analysis of XGBoost Classifier with Missing Data | Im Export ohne Erscheinungsort | Doppelt im RIS-Export (Nr. 11) |
| 13 | Ramosaj et al. (2019), Predicting missing values: a comparative study on non-parametric approaches for imputation | Computational Statistics | — |
| 14 | Rios et al. (2022), Handling missing values in machine learning to predict patient-specific risk of adverse cardiac events | Computers in Biology and Medicine | — |
| 15 | Chen et al. (2024), Missing values handling for machine learning portfolios | Journal of Financial Economics | — |
| 16 | Kuchen (2026), MIBoost: A gradient boosting algorithm for variable selection after multiple imputation | arXiv | — |
| 17 | Alabadla et al. (2022), Systematic Review of Using Machine Learning in Imputing Missing Values | IEEE Access | Review |
| 18 | Rabit, Handling Missing Values and Prediction of Waste Pile Data Based on Machine Learning | Im Export ohne vollständige Metadaten | — |

Der Nutzer hatte die Arbeiten von Aydin und Öztürk sowie Perez-Lebel zusätzlich
als Abstract beziehungsweise Volltext vorgelegt. Diese Sichtung wird separat
protokolliert und ersetzt nicht das spätere systematische Titel-/Abstractscreening
aller S3a-Treffer.

## 8. Rückwärts- und Vorwärtssuche

| Datum | Ausgangsarbeit | Richtung | Geprüft | Neue Kandidaten |
|---|---|---|---|---|
| | | | | |

## 8a. Grundlagen und gezielte Ergänzungen

Getrennt von den FF1-Suchläufen festhalten, wofür eine Quelle benötigt wird
und wie sie tatsächlich verfügbar wurde. Für Bestand aus der Zeit vor dem
Neustart genügt etwa „vorhandener Bestand/Exposé; ursprünglicher Fundweg
nicht dokumentiert“. Bei neuer Suche Datenbank und genaue Eingabe angeben,
bei Zitationssuche die Ausgangsarbeit und Richtung. Keine nachträglichen
Suchdaten erfinden. Für eine Aufnahme in die FF1-Synthese gelten zusätzlich
die Kriterien aus Abschnitt 5; die entsprechenden Auswahlzahlen stehen in
Abschnitt 9.

| Datum der Zuordnung | Quelle | Thema/Zweck | Tatsächlicher Fundweg oder Bestand | Volltext/Fundstelle geprüft? | FF1-relevant? |
|---|---|---|---|---|---|
| | | | | | |

## 9. Auswahlzahlen

| Stufe | Anzahl |
|---|---|
| Treffer aus Datenbanken | |
| Zusätzlich aus Rückwärts- und Vorwärtssuche | |
| Zusätzlich gezielt aus vorhandenem Bestand ergänzt | |
| Nach Entfernen von Dubletten | |
| Nach Titel- und Abstractscreening | |
| Nach Volltextprüfung in der Synthese | |

## 10. Ausgeschlossene Volltexte

| Arbeit | Kriterium | Begründung |
|---|---|---|
| | | |

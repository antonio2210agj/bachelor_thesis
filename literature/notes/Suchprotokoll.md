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

Die **FF1-Suche** und die gezielte Ergänzung von **Grundlagen und Kontext**
werden getrennt dokumentiert (Abschnitte 7–10 bzw. 8a). Grundlagenquellen
können auch für FF1 relevant sein, wenn sie die Kriterien erfüllen. Vorhandene
Arbeiten dürfen für den Hintergrund genutzt werden; ihren früheren Fundweg
nicht als neue Datenbanksuche ausgeben. Konkrete Aussagen am Volltext prüfen.

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

Jede Zeile ist eine eigene Suchanfrage. Die Beispiele mit Anführungszeichen
sind nicht zwingend identisch mit bereits durchgeführten Anfragen; maßgeblich
für die tatsächlichen Eingaben ist das Such-Log in Abschnitt 7.

| ID | Beispiel für Google Scholar | Zweck |
|---|---|---|
| S1a | `"TabPFN" "missing values"` | Einstieg: TabPFN und fehlende Werte |
| S1b | `"tabular foundation models" "missing data"` | Breiterer Ansatz über TabPFN hinaus |
| S1c | `"TabPFN" "imputation"` | Weitere Arbeiten zur Behandlung fehlender Werte |
| S2a | `"TabPFN" "gradient boosting" "missing values"` | Mögliche direkte Vergleiche |
| S3a | `"gradient boosting" "missing values"` | Fehlende Werte bei Gradient Boosting |
| S4a | `"missing data" "imputation" "classification" "benchmark"` | Vergleichsstudien zu Behandlungen |

S3b wurde explorativ ausprobiert, aber aus dem weiteren Suchplan entfernt;
der Versuch bleibt in Abschnitt 7 dokumentiert. S4a wurde ohne `tabular`
durchgeführt; eine zweite Variante ist ohne konkreten Bedarf nicht vorgesehen.

Für jeden Suchlauf eine Zotero-Untersammlung anlegen und tatsächlich
aufgenommene Treffer zuordnen; ein Eintrag kann mehreren Sammlungen angehören.
Die [RIS-Anleitung](../recherche/exporte/README.md) beschreibt den Export.
Gesichteter Bereich, gespeicherte Treffer und spätere Auswahl sind getrennt
zu erfassen; keine einzelne Anfrage liefert einen vollständigen Grundbestand.

### 3.1a Suchanfragen für IEEE Xplore

Kopiervorlagen für einzelne Suchläufe. Die Suchfelder und Einstellungen sowie
die tatsächlich eingegebene Anfrage je Lauf in Abschnitt 7 festhalten; die
Liste allein belegt keine durchgeführte Suche. Viele AND-Bedingungen können
passende Treffer ausschließen.

**S1a** (bereits durchgeführt)

```text
"TabPFN" AND "missing values"
```

**S1b** (bereits durchgeführt; keine Treffer)

```text
"tabular foundation models" AND "missing data"
```

**S1c** (bereits durchgeführt)

```text
"TabPFN" AND "imputation"
```

**S2a** (RIS-Export vorhanden; genaue Eingabe noch zu bestätigen)

```text
"TabPFN" AND "gradient boosting" AND "missing values"
```

**S3a** (bereits durchgeführt)

```text
"gradient boosting" AND "missing values"
```

**S4a** (RIS-Export vorhanden; genaue Eingabe noch zu bestätigen)

```text
"missing data" AND "imputation" AND "classification" AND "benchmark"
```

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

Google Scholar, arXiv und IEEE Xplore werden genutzt; ACM Digital Library
bleibt als mögliche Ergänzung offen. Scopus war trotz VPN nur als Preview
zugänglich; das [DBIS der Uni Regensburg](https://dbis.ur.de/UBR/resources/3636)
meldet derzeit keinen Zugriff. Die endgültige Auswahl mit dem Betreuer klären.
Bei Google Scholar werden nur die ersten 50 Treffer je Suche gesichtet.
Preprints werden nur aufgenommen, wenn keine publizierte Fassung existiert.

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
lassen und nicht aus einem Export erraten. Die unten aufgeführten RIS-Dateien
der Google-Scholar-Suchläufe liegen im Unterordner `exporte/Google Scholar/`.

Für die arXiv-Suchen S1a und S1b und die folgenden Suchen werden laut Nutzer
dieselben Einstellungen verwendet: Suchfelder „All fields“, alle
Fachgebiete und Daten, Cross-Listings eingeschlossen, ältere Versionen nicht
eingeschlossen, 50 Ergebnisse pro Seite, Abstracts eingeblendet und
unveränderte Standardsortierung (konkrete Reihenfolge nicht dokumentiert).
Der Nutzer ändert die Suchbegriffe über „Refine query“. Falls Einstellungen
später verändert werden, wird die Abweichung beim jeweiligen Suchlauf notiert.
Suchbegriffe, Trefferzahl und Sichtungsbereich bleiben für jeden Lauf separat
zu dokumentieren.

| Datum | Datenbank | Suchstring (ID und genaue Eingabe) | Felder, Filter und Sortierung | Angezeigte Treffer | Gesichtet (Bereich/Anzahl) | RIS-Datei und enthaltene Auswahl | Nach Titel/Abstract behalten | Neu gegenüber Bestand |
|---|---|---|---|---|---|---|---|---|
| 25.11.2026 | Google Scholar | S1a: `"TabPFN" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 1 310 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1a--TabPFN- -missing values-.ris`, 16 Einträge; nur die als passend oder unklar gespeicherten Treffer | 16 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 9 (siehe 7.1) |
| 25.11.2026 | Google Scholar | S1b: `"tabular foundation models" "missing data"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 236 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1b--tabular foundation models- -missing data-.ris`, 8 Einträge; nur die als passend oder unklar gespeicherten Treffer | 8 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 5 neu gegenüber Bestand und S1a (siehe 7.1); 2 Überschneidungen mit S1a |
| 25.11.2026 | Google Scholar | S1c: `"TabPFN" imputation` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 1 350 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S1c--TabPFN- imputation.ris`, 16 Einträge; nur die als passend oder unklar gespeicherten Treffer | 16 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 5 Titel neu gegenüber S1a/S1b (siehe 7.1); 11 Überschneidungen |
| 25.11.2026 | Google Scholar | S2a: `"TabPFN" "gradient boosting" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 771 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S2a--TabPFN- -gradient boosting- -missing values-.ris`, 9 Einträge; nur die als passend oder unklar gespeicherten Treffer | 9 als passend oder unklar gespeichert; Titel-/Abstractscreening noch offen | 3 Titel neu gegenüber S1a–S1c (siehe 7.1); 6 Überschneidungen |
| 25.11.2026 | Google Scholar | S3a: `"gradient boosting" "missing values"` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 62 900 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S3a--gradient boosting- -missing values-.ris`, 18 RIS-Einträge; eine Arbeit doppelt exportiert (17 unterschiedliche Titel) | 18 gespeichert; Titel-/Abstractscreening noch offen | Perez-Lebel et al. ist bereits im Bestand; übrige Treffer mit früheren Exporten abgleichen (siehe 7.1) |
| 25.11.2026 | Google Scholar | S3b: `"LightGBM" "missing values"` | Sortierung und Filter nicht dokumentiert | nicht dokumentiert | Sichtungsbereich nicht dokumentiert | Kein RIS-Export im Exportordner | Laut Nutzer keine passende Arbeit zur Aufnahme identifiziert; Umfang des Screenings nicht dokumentiert | nicht quantifiziert |
| 25.11.2026 | Google Scholar | S4a: `"missing data" imputation classification benchmark` | Standardsuche, keine Filter, Sortierung nach Relevanz | ungefähr 45 000 (Schätzung von Google Scholar) | Ergebnisseiten 1 bis 5 mit je 10 Treffern, also Treffer 1 bis 50 | `S4a--missing data- imputation classification benchmark.ris`, 22 Einträge; enthält mögliche Dubletten und Versionsüberschneidungen (siehe 7.1) | 22 als passend oder unklar gespeichert; systematisches Titel-/Abstractscreening noch offen | Perez-Lebel et al. bereits in S3a und im Bestand; weitere Überschneidungen prüfen (siehe 7.1) |
| 25.11.2026 | arXiv | S1a: `TabPFN` AND `"missing values"` | Beide Suchfelder: All fields; alle Fachgebiete und Daten, Cross-Listings eingeschlossen; ältere Versionen nicht eingeschlossen; Sortierung: Standardeinstellung | 7 | Nicht angegeben | `Arxiv/S1a--TabPFN- -missing values-.ris`, 3 als passend oder unklar gespeicherte Einträge | Endgültige Auswahl offen | Zwei Einträge bereits in Scholar-Exporten; Seldon bisher nicht darin (siehe 7.1) |
| 25.11.2026 | arXiv | S1b: `"tabular foundation models"` AND `"missing data"` | Beide Suchfelder: All fields; alle Fachgebiete und Daten, Cross-Listings eingeschlossen; ältere Versionen nicht eingeschlossen; Sortierung: Standardeinstellung, konkrete Reihenfolge nicht dokumentiert | 3 | Alle 3 Treffer | `Arxiv/S1b--tabular foundation models- -missing data-.ris`, 1 als passend oder unklar gespeicherter Eintrag | Endgültige Auswahl offen | Xia et al. im bisherigen Exportabgleich nicht nachgewiesen (siehe 7.1) |
| 25.11.2026 | arXiv | S1c: `TabPFN` AND `imputation` | Beide Suchfelder: All fields; gemeinsame arXiv-Einstellungen wie oben | 10 | Alle 10 Treffer | `Arxiv/S1c--TabPFN- imputation.ris`, 2 RIS-Einträge mit identischem Titel und identischer DOI; eine Arbeit | Endgültige Auswahl offen | TabPFGen in S1a/S1b und bisherigen Scholar-Exporten nicht nachgewiesen; übrigen Bestand prüfen |
| 25.11.2026 | arXiv | S2a: Felder `"TabPFN"`, `"gradient boosting"`, AND `"missing values"`; Verknüpfung des zweiten Feldes auf Screenshot nicht ersichtlich | Drei Suchfelder: All fields; gemeinsame arXiv-Einstellungen wie oben | 0 laut Nutzer | 0 | Kein RIS-Export (keine Treffer) | 0 | 0 |
| 25.11.2026 | arXiv | S3a: `"gradient boosting"` AND `"missing values"` | Beide Suchfelder: All fields; gemeinsame arXiv-Einstellungen wie oben | 34 | Alle 34 Treffer | `Arxiv/S3a--gradient boosting- -missing values-.ris`, 1 als passend oder unklar gespeicherter Eintrag | Endgültige Auswahl offen | Vo et al. im bisherigen Exportabgleich nicht nachgewiesen; übrigen Bestand prüfen |
| 25.11.2026 | arXiv | S4a: `"missing data"` AND `imputation` AND `classification` AND `benchmark` | Suchfelder: All fields; gemeinsame arXiv-Einstellungen wie oben | 0 laut Nutzer | 0 | Kein RIS-Export (keine Treffer) | 0 | 0 |
| 25.11.2026 | arXiv | S5a: `"missing data"` AND `classification` AND `benchmark` | Suchfelder: All fields; gemeinsame arXiv-Einstellungen wie oben | 24 | Alle 24 Treffer laut Nutzer | Kein RIS-Export im Exportordner; Zotero-Auswahl nicht bestätigt | Laut Nutzer keine passenden Treffer gefunden; endgültige Auswahl offen | Nicht quantifiziert |
| 25.11.2026 | IEEE Xplore | S1a: `"TabPFN"` AND `"missing values"` | Suchfeld nicht angegeben; „All Results“, Sortierung „Relevance“; Jahresanzeige 2026–2026 (aktive Einschränkung nicht geklärt) | 4 | Alle 4 Treffer | `IEEE Xplore/S1a--TabPFN- -missing values-.ris`, 3 als passend oder unklar gespeicherte Einträge | Endgültige Auswahl offen | Zwei Einträge bereits in Scholar-S1a; Jang et al. im bisherigen Exportabgleich nicht nachgewiesen (siehe 7.1) |
| 25.11.2026 | IEEE Xplore | S1b: `("All Metadata":"tabular foundation models") AND ("All Metadata":"missing data")` | Beide Suchfelder: All Metadata; Filter und Sortierung nicht angegeben | 0 laut Nutzer | 0 | Kein Treffer zum Exportieren | 0 | 0 |
| 25.11.2026 | IEEE Xplore | S1b-erweitert: `("TabPFN" OR "tabular foundation model" OR "tabular foundation models") AND ("missing data" OR "missing values")` laut Nutzer | Suchfelder, Filter und Sortierung nicht angegeben | Gesamtzahl nicht sichtbar; Screenshot zeigt 6 Treffer | Sichtungsbereich nicht angegeben | Nicht angegeben | Offen | Vier sichtbare Titel bereits in IEEE S1a oder S1c; zwei weitere nicht in bisherigen RIS-Exporten nachgewiesen |
| 25.11.2026 | IEEE Xplore | S1c: `"TabPFN" AND "imputation"` laut Nutzer | Keine Filter laut Nutzer; Suchfelder und Sortierung nicht angegeben | 6 laut Nutzer | Nicht angegeben | `IEEE Xplore/S1c--TabPFN- imputation.ris`, 4 Einträge | Endgültige Auswahl offen | Drei Einträge bereits in IEEE S1a; Shakir in bisherigen RIS-Exporten nicht nachgewiesen (siehe 7.1) |
| Nicht bestätigt; Export vom 25.11.2026 | IEEE Xplore | S2a: geplante Vorlage `"TabPFN" AND "gradient boosting" AND "missing values"`; tatsächliche Eingabe nicht bestätigt | Suchfelder, Filter und Sortierung nicht angegeben | 36 laut Nutzer | Alle 36 laut Nutzer | `IEEE Xplore/S2a--TabPFN- -gradient boosting- -missing values-.ris`, 2 Einträge | Endgültige Auswahl offen | Beide bereits in IEEE S1a (siehe 7.1) |
| 25.11.2026 | IEEE Xplore | S3a: `"gradient boosting" AND "missing values"` laut Nutzer | Suchfelder, Filter und Sortierung nicht angegeben | 1 142 laut Nutzer | Erste 50 laut Nutzer | Nicht angegeben | Laut Nutzer keine interessanten Arbeiten gefunden | Nicht quantifiziert |
| 25.11.2026 | IEEE Xplore | S4a: geplante Vorlage `"missing data" AND "imputation" AND "classification" AND "benchmark"`; tatsächliche Eingabe nicht bestätigt | Suchfelder, Filter und Sortierung nicht angegeben | 36 laut Nutzer | Alle 36 laut Nutzer | `IEEE Xplore/S4a--missing data- imputation classification benchmark.ris`, 1 Eintrag | Endgültige Auswahl offen | Shakir bereits in IEEE S1c (siehe 7.1) |

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

**S4a (25.11.2026)**

RIS-Metadaten; Relevanz und Volltexte noch nicht systematisch geprüft.

| Nr. | Arbeit laut Export | Ort laut Export | Hinweis |
|---|---|---|---|
| 1 | Jäger et al. (2021), A Benchmark for Data Imputation Methods | Frontiers in Big Data | Review/Benchmark; Aufgaben und Modellfamilien prüfen |
| 2 | Bertsimas et al. (2018), From Predictive Methods to Missing Data Imputation: An Optimization Approach | Journal of Machine Learning Research | — |
| 3 | Poulos und Valle (2018), Missing Data Imputation for Supervised Learning | Applied Artificial Intelligence | — |
| 4 | Woźnica et al. (2020), Does imputation matter? Benchmark for predictive models | arXiv | Vermutlich gleiche Arbeit wie Nr. 10; Fassung prüfen |
| 5 | Shadbahr et al. (2023), The impact of imputation quality on machine learning classifiers for datasets with missing values | Communications Medicine | Gleiche DOI wie Nr. 9; vermutlich Dublette |
| 6 | Perez-Lebel et al. (2022), Benchmarking missing-values approaches for predictive models on health databases | GigaScience | Bestand; auch in S3a |
| 7 | Farhangfar et al. (2008), Impact of imputation of missing values on classification error for discrete data | Pattern Recognition | — |
| 8 | Sun et al. (2025), Benchmarking Missing Data Imputation Methods in Socioeconomic Surveys | Transactions on Machine Learning Research | Aufgaben/Modelle prüfen |
| 9 | Shadbahr et al. (2023), Classification of datasets with imputed missing values: does imputation quality matter? | Communications Medicine | Gleiche DOI wie Nr. 5; vermutlich Dublette |
| 10 | Woźnica et al. (2020), Does imputation matter? Benchmark for real-life classification problems | ICML Workshop on the Art of Learning with Missing Values | Vermutlich gleiche Arbeit wie Nr. 4; Fassung prüfen |
| 11 | Lee et al. (2024), Evaluating missing data handling methods for developing building energy benchmarking models | Energy | — |
| 12 | Gendre, Benchmarking imputation methods for categorical biological data | Wiley Online Library | Metadaten im Export unvollständig |
| 13 | Gabr et al. (2023), Effect of Missing Data Types and Imputation Methods on Supervised Classifiers: An Evaluation Study | Big Data and Cognitive Computing | — |
| 14 | Pereira et al. (2024), Imputation of data Missing Not at Random: Artificial generation and benchmark analysis | Expert Systems with Applications | — |
| 15 | Ishaq et al. (2024), Machine Learning Based Missing Data Imputation in Categorical Datasets | IEEE Access | Klassifikationsbezug und Modelle prüfen |
| 16 | de Souto et al. (2015), Impact of missing data imputation methods on gene expression clustering and classification | BMC Bioinformatics | — |
| 17 | Garciarena et al. (2017), An extensive analysis of the interaction between missing data types, imputation methods, and supervised classifiers | Expert Systems with Applications | — |
| 18 | Gama et al. (2025), Imputation in well log data: A benchmark for machine learning methods | Computers & Geosciences | — |
| 19 | Liang et al. (2026), Nearly Optimal Bayesian Inference for Structural Missingness | arXiv | Aufgabenbezug prüfen |
| 20 | Seu, An Intelligent Missing Data Imputation Techniques: A Review | JOIV | Unvollständige Metadaten; vermutlich Dublette von Nr. 21 |
| 21 | Seu et al. (2022), An Intelligent Missing Data Imputation Techniques: A Review | JOIV | Vermutlich Dublette von Nr. 20 |
| 22 | Pereira Barata et al. (2019), Imputation Methods Outperform Missing-Indicator for Data Missing Completely at Random | ICDM Workshops | — |

**arXiv S1a (25.11.2026)**

Die drei RIS-Einträge stammen laut Nutzer aus der tatsächlichen Suche und
sind zunächst Kandidaten; die Auswahl ist nicht durch den Export belegt.

| Arbeit laut Export | Abgleich mit bisherigen Scholar-Exporten |
|---|---|
| Angebault et al. (2026), Seldon TFM family: Seldon-Mini, Seldon and Seldon+ | Nicht in den bisherigen Scholar-Exporten; übrigen Bestand und Relevanz noch prüfen |
| Luo et al. (2025), TIME: TabPFN-Integrated Multimodal Engine for Robust Tabular-Image Learning | Bereits in S1a und S1c |
| Hollmann et al. (2023), TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second | Bereits in S1a, S1c und S2a |

Offen ist der tatsächlich gesichtete Bereich. Drei gespeicherte Einträge
bedeuten nicht automatisch, dass alle sieben Treffer gesichtet wurden.

**arXiv S1b (25.11.2026)**

Der RIS-Export enthält Xia et al. (2026), *Tabular Foundation Models for
Weighted Regression and Classification* (arXiv:2611.29789). Relevanz für FF1
und ein möglicher Abgleich mit dem übrigen Bestand sind noch offen.
Der Screenshot zeigt 50 Ergebnisse pro Seite und eingeblendete Abstracts. Der
Nutzer hat die Sortierung nicht verändert; die konkrete Standardsortierung ist
nicht dokumentiert. „Submission date (most recent)“ bezeichnet die
Datumsfilterung, nicht nachweislich die Sortierung.

**arXiv S1c (25.11.2026)**

Der RIS-Export enthält zweimal Ma et al. (2024), *TabPFGen — Tabular Data
Generation with TabPFN* (arXiv:2406.05216). Titel und DOI sind identisch;
die Zotero-Einträge sind auf eine mögliche Dublette zu prüfen. Nach dem im
Chat vorgelegten Abstract zunächst eher Kontext zu generativer Imputation;
eine nachgelagerte Klassifikation und die endgültige FF1-Einordnung sind am
Volltext zu prüfen.

**arXiv S2a (25.11.2026)**

Laut Nutzer ergab die Anfrage keine Treffer. Der Screenshot zeigt vor dem
dritten Feld `AND`, aber keine sichtbare Operatorauswahl vor dem zweiten Feld;
dessen Verknüpfung wird daher nicht ergänzt oder erraten. Keine Treffer für
diese Eingabe belegen nicht, dass keine einschlägigen Arbeiten existieren.

**arXiv S3a (25.11.2026)**

Der RIS-Export enthält Vo et al. (2025), *Explainability of Machine Learning
Models under Missing Data* (arXiv:2407.00411). Der vorgelegte Abstract setzt
den Schwerpunkt auf SHAP und Erklärbarkeit; ein Bezug zur Klassifikationsleistung
bei fehlenden Merkmalswerten ist noch am Volltext zu prüfen. Der Export hieß
anfangs S2a und wurde vom Nutzer auf S3a korrigiert.

**arXiv S5a (25.11.2026)**

Laut Nutzer wurden alle 24 Treffer gesichtet und keine passenden Arbeiten
gefunden. Der Exportordner enthält keinen RIS-Export für diesen Lauf; ob
Einträge in Zotero gespeichert wurden, ist nicht bestätigt. Der Nutzer möchte
die arXiv-Suche vorläufig abschließen und den Ablauf mit dem Betreuer
besprechen. Das ist kein Nachweis einer vollständigen Abdeckung.

**IEEE Xplore S1a (25.11.2026)**

| Arbeit laut RIS-Export | Abgleich mit bisherigen Exporten |
|---|---|
| Zaimoğlu (2026), *Evaluation of TabPFN’s Performance Consistency Under Controlled MCAR Conditions* | Bereits in Google Scholar S1a |
| Bi et al. (2026), *Missing-Aware Imbalanced Learning Pathways for Manufacturing Process Quality Assessment* | Bereits in Google Scholar S1a |
| Jang et al. (2026), *When Does Train-Time Masking Help? A Leakage-Controlled Robustness Audit of Tabular Classifiers Under Feature Missingness* | In bisherigen Such-Exporten noch nicht nachgewiesen; übrigen Bestand und Volltext prüfen |

Der Screenshot zeigt „All Results“, Sortierung nach „Relevance“ und den
Jahresbereich 2026–2026. Der Nutzer berichtet, dass der Jahresbereich nach
einer Änderung automatisch zurückspringt. Ob dies die Jahre der Treffer
widerspiegelt oder eine aktive Einschränkung darstellt, ist noch ungeklärt;
aus der Anzeige allein wird keine Jahresfilterung abgeleitet.

**IEEE Xplore S1c (25.11.2026)**

| Arbeit laut RIS-Export | Abgleich mit bisherigen Exporten |
|---|---|
| Zaimoğlu (2026), *Evaluation of TabPFN’s Performance Consistency Under Controlled MCAR Conditions* | Bereits in IEEE S1a |
| Bi et al. (2026), *Missing-Aware Imbalanced Learning Pathways for Manufacturing Process Quality Assessment* | Bereits in IEEE S1a |
| Jang et al. (2026), *When Does Train-Time Masking Help? A Leakage-Controlled Robustness Audit of Tabular Classifiers Under Feature Missingness* | Bereits in IEEE S1a |
| Shakir (2024), *Benchmarking TabLM: Evaluating the Performance of Language Models Against Traditional Machine Learning in Structured Data Tasks* | In bisherigen RIS-Exporten nicht nachgewiesen; übrigen Bestand und FF1-Relevanz prüfen |

**IEEE Xplore S2a und S4a**

S2a enthält Zaimoğlu und Jang, beide bereits in IEEE S1a. S4a enthält Shakir,
bereits in IEEE S1c. Die Angaben beruhen auf RIS-Metadaten; die FF1-Relevanz
und die tatsächlichen Suchanfragen bleiben zu prüfen.

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

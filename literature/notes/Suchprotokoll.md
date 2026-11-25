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
| S3b | `"LightGBM" "missing values"` | Arbeiten zum konkreten Modell |
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
| | | | | | | | | |

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

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

## 3. Suchstrings

Bausteine, je Datenbank an deren Syntax anpassen:

| Block | Begriffe |
|---|---|
| A Modell (TFM) | "TabPFN" OR "tabular foundation model*" OR "prior-data fitted network*" OR "TabICL" |
| B Modell (GB) | "gradient boosting" OR "LightGBM" OR "XGBoost" OR "CatBoost" OR "gradient boosted trees" |
| C Fehlende Werte | "missing values" OR "missing data" OR "missingness" OR "imputation" OR "missing indicator*" OR "MCAR" OR "MAR" OR "MNAR" |
| D Aufgabe | "classification" OR "prediction" OR "supervised learning" |

| ID | Kombination | Zweck |
|---|---|---|
| S1 | A AND C | Fehlende Werte bei Tabular Foundation Models (Kern) |
| S2 | A AND B AND C | Direkter Vergleich beider Modellansätze |
| S3 | B AND C AND D | Fehlende Werte bei Gradient Boosting; viele Treffer, auf Titel/Abstract und ab 2018 begrenzen |
| S4 | C AND D AND ("benchmark" OR "comparison") AND ("tabular") | Vergleichsstudien zu Behandlungen |

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

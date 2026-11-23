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

Die Suche beginnt nicht bei null. Die Startmenge aus dem Exposé ist der
Ausgangspunkt, die Datenbanksuche prüft, ob daneben etwas fehlt.

1. **Startmenge festhalten** (Abschnitt 6) und in die Konzeptmatrix eintragen.
2. **Datenbanksuche** mit den Suchstrings aus Abschnitt 3 in den Datenbanken
   aus Abschnitt 4. Treffer nach Titel und Abstract sichten.
3. **Rückwärtssuche** in den Literaturverzeichnissen der Kernarbeiten und
   **Vorwärtssuche** über „Zitiert von" (Abschnitt 8).
4. **Volltextprüfung** der verbliebenen Arbeiten, Eintrag in die Konzeptmatrix.
5. **Abbruch**, wenn eine weitere Runde aus Rückwärts- und Vorwärtssuche keine
   neue relevante Arbeit mehr liefert.

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

## 6. Startmenge

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

| Datum | Datenbank | Suchstring (ID und genaue Eingabe) | Filter | Treffer | Nach Titel/Abstract behalten | Neu gegenüber Startmenge |
|---|---|---|---|---|---|---|
| | | | | | | |

## 8. Rückwärts- und Vorwärtssuche

| Datum | Ausgangsarbeit | Richtung | Geprüft | Neue Kandidaten |
|---|---|---|---|---|
| | | | | |

## 9. Auswahlzahlen

| Stufe | Anzahl |
|---|---|
| Treffer aus Datenbanken | |
| Zusätzlich aus Startmenge sowie Rückwärts- und Vorwärtssuche | |
| Nach Entfernen von Dubletten | |
| Nach Titel- und Abstractscreening | |
| Nach Volltextprüfung in der Synthese | |

## 10. Ausgeschlossene Volltexte

| Arbeit | Kriterium | Begründung |
|---|---|---|
| | | |

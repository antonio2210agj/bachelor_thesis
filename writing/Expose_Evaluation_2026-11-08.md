# Evaluation: Exposé, Titel & Forschungsfragen

> **Aktueller Stand:** Die Bewertung unten dokumentiert die erste Einschätzung
> vom 8. November und wurde durch die kritische Neubewertung vom 9. November
> ersetzt. Insbesondere die damalige Notenprognose und die Beschreibung des
> Beitrags als „exzellent“ gelten nicht als aktuelle Schlussfolgerungen.
> Siehe [Expose_Evaluation_2026-11-09_Neubewertung.md](./Expose_Evaluation_2026-11-09_Neubewertung.md).

Stand: 8. November 2026. **Aktualisiert am 9. November 2026** nach
Volltextprüfung der beiden neuen Quellen — Details im Folgedokument
[Expose_Evaluation_2026-11-09_Volltextabgleich.md](./Expose_Evaluation_2026-11-09_Volltextabgleich.md).
Die Pflichtpunkte 1 und 3 (unten) sind erledigt; Titel, FF2 und Exposé
wurden am 9. November entsprechend angepasst.

Bewertungsgrundlage: [Expose.tex](./Expose.tex),
[Gliederung.tex](./Gliederung.tex),
[Missing_Data_Abschlussabgleich.md](../literature/notes/Missing_Data_Abschlussabgleich.md)
sowie ein externer Web-Literaturabgleich am 8. November 2026.

## Gesamturteil

**Das Exposé ist anmeldefähig — mit einer Pflichtaufgabe vorher.** Titel und
Forschungsfragen sind sauber konstruiert, der rote Faden trägt, die methodische
Sorgfalt liegt über typischem BA-Niveau. Der externe Literaturabgleich hat
**eine neue, direkt benachbarte Publikation gefunden, die vor der Anmeldung
geprüft und abgegrenzt werden muss** (siehe Abschnitt 3). Eine 1,0 ist mit
diesem Design realistisch erreichbar — sie hängt nicht mehr am Konzept,
sondern an der Ausführung.

---

## 1. Bewertung des Titels

> „TabPFN bei unvollständigen tabellarischen Daten: Kritische Literaturanalyse
> und experimenteller Vergleich von Missing-Data-Behandlungen mit LightGBM"

**Stärken (sehr gut):**

- Nennt Gegenstand (TabPFN), Bedingung (unvollständige Daten), beide Methoden
  (Literaturanalyse + Experiment) und die Baseline (LightGBM). Ein Prüfer weiß
  nach einem Satz exakt, was die Arbeit leistet.
- „Kritische Literaturanalyse" signalisiert Eigenleistung über reines
  Referieren hinaus und deckt FF1 ab.
- Keine Übertreibung („Robustheit", „Benchmark", „State of the Art" werden
  vermieden) — konsistent mit der defensiven Beitragsformulierung.

**Schwächen (klein):**

- Grammatikalische Mehrdeutigkeit: „Vergleich von Missing-Data-Behandlungen
  **mit LightGBM**" kann gelesen werden als „Behandlungen werden mit LightGBM
  verglichen" statt „Vergleich [von TabPFN] mit LightGBM unter verschiedenen
  Behandlungen". Präziser: *„…experimenteller Vergleich mit LightGBM unter
  verschiedenen Missing-Data-Behandlungen"*.
- Leichte Redundanz „unvollständige Daten" / „Missing-Data" — verschmerzbar.
- Der Titel verschweigt die Einschränkung auf binäre Klassifikation und MCAR —
  für einen Titel okay, da das Exposé es sofort klärt.

**Titel-Note: 1,3. Mit der Umstellung oben: 1,0.**

---

## 2. Bewertung der Forschungsfragen

### Übergeordnete FF: „Möglichkeiten und Grenzen von TabPFN …"

- **Funktion erfüllt:** bewusst breite Klammer, vollständig durch FF1+FF2
  operationalisiert. Legitim und üblich.
- **Risiko:** „Möglichkeiten und Grenzen" ist eine klassische Catch-all-Formel.
  Das Exposé fängt das ab, weil beide Unterfragen präzise sind und die
  Diskussion (Kap. 6.3) die Zusammenführung explizit vorsieht.
  **Durchgängig, keine Änderung nötig.**

### FF1 (Literaturanalyse)

- **Stark:** „wie belastbar sind ihre Aussagen" macht aus einer deskriptiven
  eine **evaluative** Frage — das rechtfertigt „kritisch" im Titel. Die
  Bewertungskriterien (Modellversion, Daten, Vergleichsverfahren,
  Evaluationsdesign) sind im Vorgehen benannt; Konzeptmatrix nach
  Webster & Watson ist die richtige Methodenwahl; Trennung Entwicklerberichte
  vs. unabhängige Untersuchungen ist ein echtes Qualitätsmerkmal.
- **Schwäche:** „ausgewählte aktuelle Arbeiten" — Auswahlkriterien (Zeitraum,
  Ein-/Ausschluss, Zielzahl) stehen nur implizit im Vorgehen. Für die Anmeldung
  ausreichend; in der Arbeit in Kap. 3.1 hart dokumentieren.
- **Umfangsrisiko:** FF1 ist breit (Ansätze **und** Einsatzmöglichkeiten
  **und** Belastbarkeit). Breite konkurriert mit der Tiefe von FF2 — der
  realistischste Notenkiller: 15 Paper referieren, aber nur 3 kritisch
  sezieren → 2,0 statt 1,0. Lösung: wenige Arbeiten tief, Rest in der
  Konzeptmatrix.

### FF2 (Empirie) — das Herzstück

- **Exzellent konstruiert.** Nicht „Wie robust ist TabPFN?" (bereits beforscht),
  sondern: **Verändert die Behandlung den gepaarten Modellvergleich?** —
  Behandlung als Moderator. Die Frage ist:
  - messbar (Balanced Accuracy, Log-Loss, gepaarte Differenzen),
  - falsifizierbar (Rangfolge/Abstand ändert sich oder nicht),
  - fair (identische Splits und Masken),
  - ehrlich abgegrenzt (deskriptiv, kein Äquivalenznachweis, kein Kausalanspruch).
- **Methodische Glanzpunkte:** gruppengetrennte Splits wegen Duplikaten
  (Spambase-Audit), Imputationsstatistiken nur aus Trainingsdaten,
  vorregistrierte Tuning-Sensitivität bei 50 %, Checkpoint-Fixierung mit
  Prüfsumme, Klarstellung, dass TabPFNs interne Verarbeitung *nicht*
  „ohne Imputation" ist.
- **Schwächen:**
  1. „über mehrere Datensätze" = faktisch 4 (plus Reserve). Prüferfrage
     „warum nicht 8–10?" einplanen (Antwort: Rechenbudget, Tiefe statt Breite,
     gepaartes Design braucht Kontrolle).
  2. Rein deskriptive Auswertung: vertretbar, aber minimal inferenzielle
     Absicherung (z. B. gepaarte Konfidenzintervalle über Wiederholungen)
     wäre eine kleine, lohnende Ergänzung.
  3. **Größtes praktisches Risiko:** Der technische Pilot (TabPFN-3.5-Zugang,
     Lizenz, Ausführbarkeit) ist noch nicht gelaufen. Ohne lauffähigen
     Checkpoint kollabiert FF2. **Pilot vor der Anmeldung durchführen.**

**Forschungsfragen-Note: 1,0–1,3.**

---

## 3. Literaturabgleich (externer Abgleich vom 8. November 2026)

Der interne Abschlussabgleich ist methodisch sauber (Primärtextprüfung,
Misstrauen gegenüber Such-Zusammenfassungen, Versionstrennung bei TabImpute).
Der externe Abgleich bestätigt den Bestand weitgehend, ergab aber zwei
Fundstellen, die dort fehlen:

### ⚠️ Fund 1 — prüfpflichtig vor Anmeldung
**[ERLEDIGT 09.11.2026: Volltext geprüft — FF2 bleibt offen, Abgrenzung
ins Exposé eingearbeitet. Siehe Folgedokument.]**

**„Evaluation of TabPFN's Performance Consistency Under Controlled MCAR
Conditions: A Tabular Classification Analysis"** (IEEE-Konferenzpublikation,
<https://ieeexplore.ieee.org/abstract/document/11727906>). Titel direkt auf
IEEE Xplore verifiziert; laut Suchzusammenfassung (**unverifiziert**) MCAR bei
0/10/20/40 % auf mehreren Datensätzen mit Baum-Baselines.

**Einordnung:** Engste bekannte Nachbararbeit zu FF2 — thematisch näher als
TIME. **Sie zerstört die Frage nicht**, denn das Alleinstellungsmerkmal ist
nicht „TabPFN unter MCAR", sondern der **Pipelinevergleich** (intern vs.
Median vs. Indikatoren) unter **identischen Masken** mit **gepaartem**
TabPFN-3.5-vs-LightGBM-Vergleich und Maskierung aller drei Partitionen.

Konsequenz:

- Volltext beschaffen (Hochschulzugang zu IEEE Xplore), Methoden prüfen:
  Welche TabPFN-Version? Welche Behandlungen? Gepaart? LightGBM dabei?
- Im Exposé/Kap. 3.6 als direkteste Vorarbeit zitieren und abgrenzen —
  stärkt FF1 sogar (Belastbarkeit einer Konferenzstudie kritisch bewerten).

### Fund 2 — Kontextpflicht, keine Bedrohung
**[ERLEDIGT 09.11.2026: Volltext geprüft — LightGBM dient dort als
iterativer Imputer, TabPFN als Klassifikator; keine FF2-Überschneidung.
Im Exposé als Abgrenzung zitiert.]**

**Tran & Byeon (2024), Digital Health:** Hybrid LightGBM–TabPFN für
Demenzprognose bei Parkinson
(<https://pmc.ncbi.nlm.nih.gov/articles/PMC11833816/>). Andere Frage
(Hybridleistung, kein Behandlungsvergleich), aber publizierte
TabPFN+LightGBM-Kombination → gehört in die Konzeptmatrix.

### Bestätigt (keine Lücken gefunden)

- **Perez-Lebel et al. 2022** bleibt die korrekte methodische Hauptvorlage;
  Abgrenzung (kein TabPFN, natürliche Missingness ≠ MCAR) hält.
- **TabImpute** (Rekonstruktion ≠ Downstream-Klassifikation) und **TIME**
  (multimodal, Fusionsvarianten) — Abgrenzungen halten.
- **Noise Immunity** (arXiv 2604.04868) liegt bereits lokal vor — prüfen, ob
  dessen Missingness-Teil in Kap. 3.6 gewürdigt wird.
- OpenReview „Assessing the Robustness of Tabular Prior-Data Fitted Networks"
  war hinter Captcha nicht verifizierbar — als Prüfkandidat notieren, nicht
  als bestätigte Studie führen.

**Fazit:** Die Kernaussage — *Pipelinevergleich TabPFN-3.5 vs. LightGBM unter
identischen MCAR-Masken mit mehreren Behandlungen und Downstream-Bewertung
wurde im geprüften Bestand nicht gefunden* — hält auch nach diesem Abgleich,
**vorbehaltlich der IEEE-Volltextprüfung**.

---

## 4. Roter Faden: trägt er eine ganze BA?

**Ja, ungewöhnlich gut.** Die Kette *LLMs/In-Context Learning → Tabular
Foundation Models → TabPFN-Evidenz (FF1) → fehlende Werte als Prüfgegenstand →
kontrolliertes Experiment (FF2) → gemeinsame Einordnung* hat drei
Eigenschaften, die Gutachter als „roten Faden" belohnen:

1. **Jedes Kapitel ist Voraussetzung des nächsten** — nichts ist Füllmaterial.
   Der dokumentierte Verzicht (keine Versionshistorie, kein XAI, kein
   Laufzeitbenchmark) ist selbst ein Qualitätssignal.
2. **FF1 und FF2 sind verschränkt:** Kap. 3.6 ist das Scharnier, Kap. 6.3
   schließt die Klammer zur übergeordneten Frage.
3. **Erzählbare Hypothesenlogik:** TabPFN kodiert Missingness intern
   (Indikator + Mittelwert), LightGBM nutzt Default-Richtungen — externe
   Median-Imputation zerstört für beide die Missingness-Information,
   möglicherweise unterschiedlich stark. Daraus schreibt man eine
   1,0-Diskussion.

---

## 5. Anmeldung und Notenprognose

### Anmeldung: Ja — nach drei Pflichtpunkten

| # | Vor der Anmeldung | Aufwand | Status |
|---|---|---|---|
| 1 | **IEEE-MCAR-Paper im Volltext prüfen** und im Exposé (1 Satz) abgrenzen | 2–3 h | ✅ erledigt 09.11.2026 |
| 2 | **Technischer Pilot TabPFN-3.5:** Checkpoint laden, Lizenz klären, Mini-Lauf auf WDBC | 0,5–1 Tag | ✅ erledigt 09.11.2026 — siehe [Pilotprotokoll](../experiments/Pilotprotokoll.md) |
| 3 | Titel-Mehrdeutigkeit beheben: „…Vergleich mit LightGBM unter verschiedenen Missing-Data-Behandlungen" | 10 min | ✅ erledigt 09.11.2026 (Exposé + Gliederung) |

### 1,0-Prognose: realistisch, mit diesen Erfolgsbedingungen

**Bereits auf 1,0-Niveau:** Fragenarchitektur, Fairness des Versuchsdesigns
(gepaarte Masken, Split-Hygiene, Duplikat-Gruppen, Train-only-Statistiken),
Vorregistrierungs-Mentalität, ehrliche Beitrags- und Grenzenformulierung.

**Woran sich 1,0 vs. 1,7 entscheidet:**

1. **Tiefe der FF1-Kritik** — Evaluationsdesigns wirklich sezieren, nicht
   referieren (z. B. die IEEE-Studie selbst kritisch bewerten).
2. **Qualität der Diskussion** — die Mechanismus-Erzählung muss die
   Ergebnisse erklären, nicht nur beschreiben.
3. **Disziplin halten** — kein Scope Creep; das Exposé ist der Vertrag mit
   sich selbst.
4. **Keine technischen Überraschungen** — Pilot vor Anmeldung.

**Realistische Notenspanne bei sauberer Ausführung: 1,0–1,3.**
Das Konzept limitiert nicht mehr.

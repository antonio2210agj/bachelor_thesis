# Re-Evaluation nach Volltextprüfung: Ist FF2 schon beantwortet?

Stand: 9. November 2026. Geprüfte Volltexte (beide jetzt lokal in
[07_Missing_Data_und_Imputation](../literature/07_Missing_Data_und_Imputation)):

1. **Zaimoğlu (IDAP'26, IEEE):** „Evaluation of TabPFN's Performance Consistency
   Under Controlled MCAR Conditions: A Tabular Classification Analysis",
   DOI 10.1109/IDAP71869.2026.11727906
2. **Tran & Byeon (2024, Digital Health):** „Predicting dementia in Parkinson's
   disease on a small tabular dataset using hybrid LightGBM–TabPFN and SHAP",
   DOI 10.1177/20552076241272585

---

## Kurzantwort

**Zaimoğlu ist die engste Vorarbeit, beantwortet aber nicht dieselbe
Vergleichsfrage.** Die Arbeit untersucht TabPFN v2 unter MCAR mit mehreren
Behandlungen, kreuzt diese jedoch nicht vollständig über alle Modelle und
enthält kein LightGBM. Das begründet eine begrenzte Anschlussuntersuchung,
keinen Nachweis einer umfassenden Forschungslücke. Tran & Byeon adressieren
eine andere Frage und dienen vor allem als Anwendungskontext.

---

## 1. Was Zaimoğlu tatsächlich macht (verifiziert am Volltext)

- **Modell:** TabPFN **v2** (offizielle Bibliothek), nicht 3.5.
- **Design:** 7 Datensätze — 4 reale (breast_cancer, digits, iris, wine) und
  3 synthetische (make_classification); binär **und** Mehrklassen gemischt.
- **MCAR:** 0/10/20/40 % nur auf Eingabemerkmale; NumPy mit festem Seed.
- **Split:** 70/30 stratifiziert, **keine Validierung**; die Reihenfolge
  Maskierung↔Split ist im Text nicht eindeutig spezifiziert.
- **Behandlungen:** TabPFN bekommt alle drei (raw, Median, Median+Indikator);
  die Baselines bekommen **je genau eine**: HistGB_raw, RF_median,
  LogReg_indicator. **Kein LightGBM.**
- **Tuning:** keines — alle Modelle mit scikit-learn-Defaults.
- **Metriken:** Macro-F1, Balanced Accuracy; 3 Seeds; Friedman/Nemenyi über
  28 Blöcke (7 Datensätze × 4 Fehlraten).
- **Hauptbefund:** TabPFN_raw hat den geringsten relativen Macro-F1-Verlust
  bei 40 % (8,81 %); TabPFN_median (14,30 %) und TabPFN_indicator (15,23 %)
  verlieren *mehr* als HistGB_raw (13,35 %). TabPFN_raw signifikant besser
  als alle Baselines (Nemenyi, α=0,05).

## 2. Überschneidungsmatrix mit deiner FF2

| Dimension | Zaimoğlu (IDAP'26) | Deine BA |
|---|---|---|
| TabPFN-Version | v2 | **3.5** (interner Indikator + Mittelwert, Abschn. 3.1) |
| GBDT-Baseline | HistGradientBoosting, nur raw | **LightGBM, alle drei Behandlungen** |
| Design Modelle×Behandlungen | nur TabPFN gekreuzt; Baselines je 1 Behandlung | **vollständig gekreuzt → Behandlung als Moderator prüfbar** |
| Fehlraten | 0/10/20/40 % | 0/10/30/**50** % |
| Partitionen | Train/Test, keine Validierung, Maskierungsreihenfolge unklar | Train/Val/Test separat maskiert, dokumentiert |
| Tuning | keins (Defaults) | LightGBM auf Referenz abgestimmt + Sensitivität bei 50 % |
| Masken gepaart über Modelle? | nicht berichtet | **ja, identische Splits und Masken** |
| Metriken | Macro-F1, BA | BA + Log-Loss |
| Datenbasis | inkl. iris (n=150), wine, synthetisch, Mehrklassen | 4 reale binäre, Duplikat-Gruppen-Splits |
| Seeds/Wiederholungen | 3 | mehrere, vorab fixiert |

**Was Zaimoğlu beantwortet:** Welche Behandlung ist für TabPFN v2 unter MCAR
am besten? (raw) — und: Ist TabPFN_raw robuster als *ungetunte*
sklearn-Baselines? (ja).

**Was offen bleibt (= der engere Anschluss deiner FF2):** Verändert sich der
gepaarte Leistungsabstand zwischen TabPFN-3.5 und LightGBM, wenn beide
Modelle dieselben Behandlungen und Masken erhalten? Zaimoğlus
Vergleichsdesign beantwortet diese Differenzfrage nicht, weil die
Behandlungen nicht vollständig über die Baselines gekreuzt werden. Die
geplante Abstimmung von LightGBM auf vollständigen Daten verbessert die
Vergleichbarkeit, belegt aber keine optimale Konfiguration unter jeder
Fehlrate oder Pipeline.

**Vorsicht bei Zahlenvergleichen:** Tabelle II berichtet aggregierte
Ergebnisse unterschiedlicher Modell-Behandlungs-Kombinationen. Der Abstand
von 0,035 bei 40 % vergleicht TabPFN_median mit HistGB_raw und ist kein
gepaarter Behandlungseffekt. Er kann höchstens illustrieren, warum ein
gekreuzter Vergleich interessant ist; nicht als Beleg für die Größe oder
Richtung einer Moderation verwenden.

## 3. Kritikpunkte an Zaimoğlu (Material für FF1!)

Diese Studie ist ein Geschenk für deine „Belastbarkeits"-Frage — sie hat
genau die Schwächen, deren Vermeidung dein Design auszeichnet:

1. **Nicht gekreuztes Design:** Baselines bekommen je eine Behandlung →
   Modell- und Behandlungseffekt konfundiert.
2. **Kein Tuning:** Der 0 %-Abstand (0,965 vs. 0,914) kann teilweise
   Tuning-Artefakt sein; TabPFN ist als Default-stark bekannt, GBDTs
   profitieren stark von Abstimmung. Das schwächt die Signifikanzaussage.
3. **TabPFN-Komfortzone:** iris (n=150), wine (n=178) — winzige Datensätze,
   auf die TabPFN zugeschnitten ist.
4. **Maskierungsprozedur unterspezifiziert:** betroffene Partitionen und
   Reihenfolge Split↔Maskierung nicht eindeutig; exakte Replikation unmöglich.
5. **Nur 3 Seeds**, keine Validierungspartition.
6. **„Relative Decline" vermengt** Ausgangsniveau und Robustheit (wer höher
   startet, kann relativ mehr verlieren).
7. **Friedman über 28 Blöcke** behandelt Datensatz×Fehlrate-Paare als
   unabhängig — vier Fehlraten desselben Datensatzes sind es nicht.
8. Einzelautorin, Konferenzpaper; kein Code-/Daten-Release erkennbar.

## 4. Tran & Byeon: endgültig eingeordnet

Verifiziert am Volltext: „Hybrid LightGBM–TabPFN" bedeutet **LightGBM als
iterativer Imputer** (spaltenweise Regression/Klassifikation auf beobachteten
Werten, Tabelle 4) **und danach TabPFN als Klassifikator** auf den imputierten
Daten. Ein einzelner Parkinson-Datensatz mit natürlicher Missingness (bis
~49 % je Spalte), Vergleich gegen KNN- und andere Imputer sowie sieben
Klassifikatoren, SHAP zur Interpretation.

→ **Keine Überschneidung mit FF2** (kein Behandlungs-×-Modell-Vergleich,
kein kontrolliertes MCAR, keine Fehlratenkurven). Gehört in die
Konzeptmatrix unter „Kombinationen/Anwendungen" und belegt die praktische
Relevanz der Modellkombination. Interessante Querverbindung: Dort *hilft*
Imputation vor TabPFN (natürliche, informative Missingness, v1-Ära),
bei Zaimoğlu *schadet* sie (MCAR, v2) — dieser scheinbare Widerspruch ist
ein hervorragender Diskussionsaufhänger.

## 5. Konsequenzen für Exposé und Anmeldung

**Die empirische Anschlussfrage ist weiterhin vertretbar, aber enger und
bescheidener zu formulieren.** Erforderliche Konsequenzen:

1. **Zielgröße explizit festlegen:** Der zentrale Endpunkt ist die
   Veränderung der gepaarten Balanced-Accuracy-Differenz gegenüber der
   vollständigen Referenz, nicht ein allgemeines Modellranking.
2. **Beitragsformulierung begrenzen:** Das gekreuzte Design ist eine
   kontrolliertere Anschlussuntersuchung; es beweist weder generelle
   Überlegenheit noch eine weltweit erstmalige Lücke.
3. **Erwartungen offen halten:** Die Vorarbeit liefert Befunde, aber keine
   belastbare Vorhersage für TabPFN-3.5 gegen abgestimmtes LightGBM unter
   denselben Pipelines.
4. **FF1 nutzen:** Zaimoğlu ist ein zentraler Fall für die kritische
   Bewertung von Design, Baselines, Maskierung und statistischer Einheit.
5. **Neue Screening-Kandidaten aus Zaimoğlus Literaturverzeichnis:**
   Samad et al. 2026 (Imputation-free Learning of Tabular Data with Missing
   Values, Applied Soft Computing) und TabArena (arXiv 2506.16791) — kurz
   auf FF2-Relevanz prüfen, vermutlich nur Kontext.

Eine belastbare Notenprognose lässt sich aus dieser Literaturabgrenzung nicht
ableiten. Die Vorarbeit stärkt die Motivation, setzt aber zugleich enge
Grenzen für Neuheits- und Generalisierungsbehauptungen.

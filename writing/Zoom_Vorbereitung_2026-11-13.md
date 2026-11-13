# Vorbereitung Zoom-Call mit Maximilian

Freitag, 13. November 2026, 13 Uhr. Grundlage: [Expose.tex](./Expose.tex),
[Missing_Data_Abschlussabgleich.md](../literature/notes/Missing_Data_Abschlussabgleich.md)
und [Pilotprotokoll.md](../experiments/Pilotprotokoll.md).

Die Antworten sind so formuliert, dass du sie frei sprechen kannst.

## Aktueller Stand

**Titel:** Tabular Foundation Models bei fehlenden Merkmalswerten: Ein
literaturgestützter empirischer Vergleich mit Gradient Boosting unter
MCAR-Bedingungen

**Forschungsfrage:** Wie beeinflussen fehlende Merkmalswerte den
Leistungsvergleich zwischen Tabular Foundation Models und Gradient
Boosting in der tabellarischen Klassifikation?

**FF1:** Welche Befunde liefert die aktuelle Literatur zur Klassifikation
mit fehlenden Merkmalswerten bei Tabular Foundation Models und Gradient
Boosting, und welcher Untersuchungsbedarf ergibt sich daraus für den
Vergleich beider Ansätze?

**FF2:** Wie verändert sich der Leistungsunterschied zwischen einem
Tabular Foundation Model und einem Gradient-Boosting-Verfahren bei
steigenden Anteilen MCAR-fehlender Merkmalswerte und unterschiedlichen
Behandlungen dieser Werte?

## Die Arbeit in zwei Sätzen

Ich untersuche, ob sich der Leistungsabstand zwischen einem Tabular
Foundation Model und Gradient Boosting verändert, wenn Merkmalswerte
fehlen und unterschiedlich behandelt werden. Die Literaturanalyse zeigt,
was dazu bekannt ist und was offen bleibt; das Experiment prüft die
offene Frage unter kontrollierten Bedingungen.

## Teil 1: Die fünf Punkte aus seiner Mail

### 1. Warum stehen keine Modellversionen mehr im Titel?

Titel und Fragen nennen jetzt die Konzepte: Tabular Foundation Models
und Gradient Boosting. TabPFN-3.5 und LightGBM sind die Vertreter in der
Methodik. Kommt eine neue Version, tausche ich das Modell aus, und das
Versuchsdesign bleibt gleich.

### 2. Ist die Hauptfrage übergeordnet, oder nur FF1 „und" FF2?

Die Hauptfrage fragt nach einer Sache: dem Einfluss fehlender Werte auf
den Leistungsvergleich. FF1 und FF2 sind zwei Schritte zur Antwort.
Beantwortet wird die Hauptfrage in der Diskussion, wo Literaturbefunde
und eigene Ergebnisse zusammengeführt werden.

### 3. Wie baut FF2 auf FF1 auf?

- FF1 ordnet die Arbeiten in einer Konzeptmatrix: Modell und Version,
  Fehlmechanismus, Fehlrate, betroffene Partitionen, Behandlung,
  Vergleichsverfahren und deren Abstimmung, Metrik, Grenzen.
- Daraus ergibt sich, welche Vergleichsfrage offen ist.
- Aus derselben Matrix leite ich das Design von FF2 ab: Fehlmechanismus,
  Fehlraten, Behandlungen und Auswertung.

Ohne FF1 wäre das Experiment nicht begründet, ohne FF2 bliebe die
Literaturanalyse bei der Feststellung einer offenen Frage stehen.

### 4. Warum der Fokus auf fehlende Werte?

- Der allgemeine Vergleich liegt schon vor, vor allem in den
  Modellberichten selbst (Nature-Arbeit, TabPFN-2.5-Bericht).
- Fehlende Werte werden dort nicht kontrolliert untersucht:
  Grinsztajn et al. entfernen sie ausdrücklich (Abschnitt 3.2), die
  Nature-Arbeit wertet Datensätze mit und ohne fehlende Werte nur als
  Teilgruppe aus (Abb. 5b).
- Fehlende Werte sind in realen Tabellen häufig (Perez-Lebel et al.).
- Beide Modellansätze können fehlende Werte selbst verarbeiten. Damit
  stellt sich eine praktische Frage: intern verarbeiten oder vorher
  imputieren?

### 5. Was ist MCAR, und warum MCAR?

**Definition:** Missing Completely At Random. Ob ein Wert fehlt, hängt
weder von beobachteten noch von unbeobachteten Werten ab.

**Abgrenzung:**

- MAR (Missing At Random): Das Fehlen hängt von anderen, beobachteten
  Werten ab.
- MNAR (Missing Not At Random): Das Fehlen hängt vom fehlenden Wert
  selbst oder von unbeobachteten Größen ab.

**Was ich konkret mache:** In vollständigen Datensätzen wird jede Zelle
mit derselben Wahrscheinlichkeit als fehlend markiert (0, 10, 30, 50 %),
unabhängig von Merkmalswerten und Klasse. Die Klassenlabels bleiben
vollständig.

**Warum das passt:**

1. Ich kann den Anteil fehlender Werte exakt steuern.
2. Die vollständigen Daten dienen als Referenz.
3. Das Fehlen trägt keine Information über die Klasse. Unterschiede
   zwischen den Behandlungen gehen also nicht auf informative Fehlmuster
   zurück.
4. Außer dem Anteil muss ich nichts festlegen. Bei MAR oder MNAR müsste
   ich wählen, wovon das Fehlen abhängt und wie stark, und jede Wahl
   wäre angreifbar.
5. Die nächstliegende Vorarbeit (Zaimoğlu 2026) nutzt ebenfalls
   kontrolliertes MCAR, was den Vergleich erleichtert.

**Grenze:** In echten Daten fehlen Werte selten rein zufällig. Aussagen
über MAR oder MNAR treffe ich nicht; das steht in Grenzen und Ausblick.
Deshalb steht MCAR auch im Titel.

## Teil 2: Wahrscheinliche Nachfragen

### Beitrag und Abgrenzung

**Was ist dein eigener Beitrag?**
Eine kontrollierte Anschlussuntersuchung. Ich wende dieselben
Behandlungen auf beide Modelle an, mit denselben Splits und Masken, und
messe, wie sich der Abstand zwischen den Modellen verändert. Ich
beanspruche keine neue Methode, keine erstmalige Untersuchung fehlender
Werte und kein allgemeines Modellranking.

**Was macht Zaimoğlu, und was machst du anders?**

| | Zaimoğlu (2026) | Meine Arbeit |
|---|---|---|
| Modell | TabPFN v2 | TabPFN-3.5 |
| Vergleich | HistGradientBoosting, Random Forest, logistische Regression | LightGBM |
| Behandlungen | drei bei TabPFN, je eine pro Vergleichsmodell | dieselben drei bei beiden Modellen |
| Tuning | keines, Standardwerte | LightGBM abgestimmt, dann fixiert |
| Fehlraten | 0, 10, 20, 40 % | 0, 10, 30, 50 % |
| Daten | 7 Datensätze (4 real, 3 synthetisch), 3 Seeds, 70/30-Split | 4 reale numerische Datensätze |
| Zielgröße | Leistung je Modell (Macro-F1, Balanced Accuracy) | Veränderung des Abstands zwischen den Modellen |

Weil die Vergleichsmodelle bei ihr nur je eine Behandlung bekommen,
lässt sich nicht ablesen, ob die Behandlung den Abstand verändert.

**Ist die Antwort nicht schon klar?**
Wer besser ist, wahrscheinlich ja: TabPFN liegt bei Zaimoğlu und im
Pilot vorn. Ob sich der Abstand verschiebt, je nachdem wie man fehlende
Werte behandelt, ist nicht klar. Zaimoğlus eigene Zahlen (Macro-F1,
Mittel über sieben Datensätze) gehen je nach Behandlung in verschiedene
Richtungen:

| | 0 % | 40 % | Vorsprung vor HistGB |
|---|---|---|---|
| TabPFN intern | 0,965 | 0,880 | wächst von 0,051 auf 0,088 |
| TabPFN mit Median | 0,965 | 0,827 | schrumpft von 0,051 auf 0,035 |
| HistGradientBoosting intern | 0,914 | 0,792 | |

Das Baumverfahren bekommt dort nur eine Behandlung. Was passiert, wenn
beide Seiten gleich behandelt werden, ist offen. Die Zahlen taugen nur
als Motivation, nicht als Beleg: Mittelwerte über Datensätze, kein
Tuning, TabPFN v2, kein LightGBM.

Offen sind drei Dinge:

- Hilft oder schadet Median-Imputation bei LightGBM unter MCAR?
- Gilt Zaimoğlus Befund auch für TabPFN-3.5, das fehlende Werte anders
  verarbeitet als v2?
- Verschiebt sich der Abstand mit Fehlrate und Behandlung, wenn beide
  Modelle dieselben Behandlungen bekommen?

**Ist die Frage spannend genug?**
Es ist eine solide Anschlussfrage, keine spektakuläre. Der
Neuigkeitswert ist begrenzt: neu sind die Kreuzung beider Modelle, die
neuere Version, LightGBM und das Tuning. Auch „der Abstand ändert sich
kaum" wäre ein gültiges Ergebnis. Praktisch relevant ist sie, weil jeder,
der eines der Modelle mit unvollständigen Daten einsetzt, entscheiden
muss: intern verarbeiten oder vorher imputieren.

**Der Titel sagt „Tabular Foundation Models", du testest aber nur
TabPFN-3.5.**
Die Ergebnisse gelten für die untersuchten Vertreter, Datensätze und
Bedingungen. Das steht als Grenze im Exposé. Die Konzepte im Titel
beschreiben die Fragestellung; welche Vertreter ich prüfe, legt die
Methodik fest.

**Warum genau TabPFN und LightGBM?**
Beide verarbeiten fehlende Werte modellintern. Erst das macht den
Vergleich „intern gegen Imputation" für beide Seiten möglich. TabPFN ist
das am besten dokumentierte Tabular Foundation Model, LightGBM ein
verbreitetes Gradient-Boosting-Verfahren, das bei Zaimoğlu fehlt.

**Welche anderen Arbeiten gibt es, und warum beantworten sie die Frage
nicht?**

- Perez-Lebel et al. (2022): vergleichen Behandlungen bei Baumverfahren
  auf Gesundheitsdaten mit natürlich fehlenden Werten. Kein TabPFN.
- TIME (Luo et al. 2025): TabPFN v2 als Baustein eines
  Bild-Tabellen-Modells. Anderes Setting.
- TabImpute (Feitelberg et al. 2026): bewertet, wie gut fehlende Werte
  rekonstruiert werden, nicht die Klassifikation danach.
- Tran und Byeon (2024): LightGBM als Imputer, TabPFN als Klassifikator
  auf einem medizinischen Datensatz. Kein Vergleich über Modelle hinweg.

### Experiment

**Wie verarbeiten die Modelle fehlende Werte intern?**

- TabPFN-3.5 merkt sich pro Zelle, dass der Wert fehlt, und ersetzt ihn
  dann durch den Mittelwert der Trainingsspalte (Bericht, Abschnitt 3.1,
  Abb. 8).
- LightGBM behandelt NaN standardmäßig als fehlenden Wert
  (offizielle Dokumentation).

**Welche Behandlungen vergleichst du?**

1. Modellinterne Verarbeitung der fehlenden Werte.
2. Median-Imputation, berechnet nur aus beobachteten Trainingswerten.
3. Als Zusatzanalyse: Median-Imputation plus Missing-Indikatoren.

**Warum Median und nicht aufwendigere Imputation?**
Median ist die einfache Standardbehandlung und wird auch bei Zaimoğlu
und TIME verwendet. Mehr Imputer würden die Zahl der Bedingungen
vervielfachen. Perez-Lebel et al. zeigen außerdem, dass aufwendige
Imputation nicht durchgängig besser ist als einfache.

**Wozu Missing-Indikatoren, wenn das Fehlen unter MCAR nichts über die
Klasse verrät?**
Der Indikator sagt dem Modell trotzdem, welche Werte echt und welche
eingesetzt sind. Ob das unter MCAR etwas bringt, ist offen. Deshalb ist
es nur eine Zusatzanalyse; der Kern ist intern gegen Median.

**Warum 0, 10, 30 und 50 Prozent?**
Das ist eine Arbeitsfestlegung von niedrig bis sehr hoch mit der
vollständigen Referenz bei 0 %. Die Literatur schreibt keine bestimmten
Schwellen vor.

**Was genau misst du?**

- Primär Balanced Accuracy, ergänzend Log-Loss.
- Pro Bedingung die Differenz beider Modelle:
  Δ = BA(TabPFN) − BA(LightGBM).
- Zielgröße ist die Veränderung gegenüber den vollständigen Daten:
  Δ − Δ₀.

**Was heißt „gepaart"?**
Beide Modelle und alle Behandlungen bekommen dieselben Splits, dieselben
Testfälle und innerhalb einer Fehlrate dieselben Masken. Unterschiede
liegen dann an Modell und Behandlung, nicht an der zufälligen
Aufteilung.

**Werden auch Trainingsdaten maskiert?**
Ja. Training, Validierung und Test werden getrennt, aber mit derselben
Wahrscheinlichkeit maskiert. So entsteht kein Unterschied im Fehlanteil
zwischen Training und Einsatz.

**Wie stimmst du die Modelle ab?**
TabPFN läuft mit dokumentierter Standardkonfiguration. LightGBM wird
einmal auf den vollständigen Daten abgestimmt und bleibt dann über alle
Bedingungen fest. Als Sensitivitätsanalyse wird LightGBM bei 50 % noch
einmal neu abgestimmt, um zu prüfen, ob das die Schlussfolgerung ändert.

**Welche Datensätze?**

| Datensatz | Fälle | Merkmale |
|---|---|---|
| Breast Cancer Wisconsin Diagnostic | 569 | 30 |
| Ionosphere | 351 | 34 |
| Spambase | 4 601 | 57 |
| QSAR Biodegradation | 1 055 | 41 |
| Credit-G (Reserve) | 1 000 | 20 |

Alle sind binäre Klassifikationsaufgaben und enthalten keine fehlenden
Werte (lokal geprüft). Credit-G ist nur Reserve, weil 13 der 20 Merkmale
kategorial sind.

**Reichen vier Datensätze?**
Für eine Bachelorarbeit ja, aber sie sind keine repräsentative
Stichprobe. Ich stelle die Ergebnisse pro Datensatz dar und leite keinen
allgemeinen Effekt ab. Wiederholungen zählen nicht als zusätzliche
Datensätze.

**Statistische Tests?**
Geplant ist eine beschreibende Auswertung mit Einzelwerten und Streuung
pro Datensatz. Bei vier Datensätzen tragen Signifikanztests wenig. Das
ist eine der Fragen an ihn.

**Was erwartest du als Ergebnis?**
Ich habe keine Richtungshypothese. Auch ein stabiler Abstand wäre ein
Ergebnis.

### Literaturanalyse

**Wie systematisch ist sie?**
Eine fokussierte, dokumentierte Recherche mit konzeptzentrierter
Synthese nach Webster und Watson. Kein vollständiges systematisches
Review. Gesucht wird in Google Scholar, arXiv und über Vorwärts- und
Rückwärtszitationen; Suchanfragen, Auswahl und Ausschlüsse werden
dokumentiert.

**Wie viel Literatur liegt schon vor?**
Die Kernquellen sind gesichtet und in Notizen aufbereitet. Die
vollständige Konzeptmatrix entsteht in der Arbeit.

### Machbarkeit

**Läuft das technisch?**
Ja. Der Pilot vom 9. November lief auf Breast Cancer vollständig durch:
Modellzugang, Lizenz, fehlende Werte als Eingabe, Median-Pipeline und
Metriken.

- TabPFN braucht auf CPU etwa ein bis zwei Minuten pro Bedingung,
  LightGBM ein bis zwei Sekunden.
- Der Hauptversuch ist damit machbar, dauert aber mehrere Stunden.
- Spambase ist deutlich größer und muss noch einmal getestet werden.

**Zeigt der Pilot schon etwas?**
Nur die Machbarkeit. Es war ein einzelner Split mit einer Fehlrate; die
Zahlen sind nicht belastbar.

**Was ist noch offen?**
Endgültige Datensatzauswahl, Splitanteile, Zahl der Wiederholungen,
Tuningbudget, Aggregation der Differenzen und die Regel für vollständig
maskierte Trainingsspalten. Das lege ich vor dem Hauptversuch fest.

## Was du nicht sagen solltest

- „Erstmals" oder „Forschungslücke". Besser: „im geprüften
  Quellenbestand nicht gefunden".
- „TabPFN ist robuster". Es gibt noch keine Ergebnisse.
- Die Pilotzahlen als Ergebnis.
- „MCAR ist realistisch". Es ist ein kontrollierter Referenzfall.

## Fragen an ihn

1. Passen Titel und Forschungsfragen jetzt?
2. Wann melden wir an, und was braucht er dafür von mir?
3. Reicht die beschreibende Auswertung, oder erwartet er statistische
   Tests?
4. Wie soll das Verhältnis von Literatur- zu Praxisteil ungefähr sein?
5. Reichen vier Datensätze?

## Ergebnis des Gesprächs

- Titel und Forschungsfragen:
- Gewünschte Änderungen:
- Anmeldung:
- Nächster Schritt und Termin:

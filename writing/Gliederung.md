# Arbeitstitel

## **TabPFN for Tabular Data: Development and Empirical Comparison with Tree-Based Models**

**Deutsche Arbeitsübersetzung:** *TabPFN für tabellarische Daten: Entwicklung und empirischer Vergleich mit baumbasierten Modellen*

Der Titel ist ein vorläufiger Vorschlag für das Gespräch mit dem Betreuer. Er bildet sowohl den Literaturteil zur Entwicklung von TabPFN als auch den geplanten experimentellen Vergleich ab. Falls der Praxisteil oder die Vergleichsmodelle anders festgelegt werden, sollte der Titel entsprechend angepasst werden.

## Vorläufige Forschungsfrage

> **Wie wurde TabPFN weiterentwickelt, um Herausforderungen tabellarischer Daten zu adressieren, und wie schneidet eine ausgewählte TabPFN-Version im Vergleich zu baumbasierten Verfahren bei einer konkreten tabellarischen Vorhersageaufgabe ab?**

### Unterfragen

1. Welche Eigenschaften tabellarischer Daten erschweren den Einsatz von Deep Learning, und warum sind baumbasierte Verfahren auf solchen Daten starke Vergleichsmodelle?
2. Welche methodischen Änderungen zeigen sich zwischen dem ursprünglichen TabPFN-Paper, TabPFN-2.5 und TabPFN-3.5, insbesondere bei Architektur, Eingaberepräsentation und synthetischem Vortraining?
3. Wie unterscheiden sich TabPFN und ausgewählte baumbasierte Modelle auf einem festgelegten Datensatz hinsichtlich Vorhersageleistung und Rechenaufwand?
4. Welche Einschränkungen folgen aus Datensatzwahl, Evaluation, Modellversion, Hardware und Lizenzierung?

## Einordnung der betrachteten Arbeiten

Die drei zentralen TabPFN-Arbeiten entsprechen **nicht exakt drei aufeinanderfolgenden Hauptversionen „TabPFN 1, 2 und 3“**:

- Das ursprüngliche Paper beschreibt TabPFN (die frühe Version, häufig als TabPFN v1 bezeichnet).
- Das zweite ausgewählte Paper behandelt **TabPFN-2.5**.
- Das dritte ausgewählte Paper behandelt **TabPFN-3.5**.

Es handelt sich damit um drei wichtige Entwicklungsschritte, aber nicht um eine vollständige Darstellung aller Versionen oder Veröffentlichungen. Insbesondere sollten TabPFN-2.5 und TabPFN-3.5 nicht in „Version 2“ und „Version 3“ umbenannt werden. Im Literaturteil werden die ausgewählten Arbeiten als Meilensteine verglichen. Mit dem Betreuer ist abzuklären, ob für eine vollständige Versionsgeschichte zusätzliche Berichte, etwa zu TabPFN-v2 oder TabPFN-3, aufgenommen werden sollen.

Die zwei weiteren bisher gelesenen Arbeiten erfüllen eine andere Funktion:

- *Transformers Can Do Bayesian Inference* liefert den theoretischen Hintergrund zu PFNs.
- *Why do tree-based models still outperform deep learning on typical tabular data?* motiviert die Herausforderungen tabellarischer Daten und die starke Rolle baumbasierter Verfahren.

## Vorgeschlagene Gliederung

### 1. Einleitung

1.1 Motivation: Bedeutung tabellarischer Daten in praktischen Anwendungen  
1.2 Problemstellung: Herausforderungen für Deep Learning auf Tabellendaten  
1.3 Ziel und Abgrenzung der Arbeit  
1.4 Forschungsfrage und Unterfragen  
1.5 Aufbau der Arbeit

### 2. Hintergrund

2.1 Tabellarische Daten: Struktur, Merkmale und typische Herausforderungen  
2.2 Deep Learning auf Tabellendaten und Unterschiede zu Bild- und Sprachdaten  
2.3 Baumbasierte Verfahren als wichtige Baselines  
2.4 Tabular Foundation Models und In-Context Learning  
2.5 Prior-Data Fitted Networks und bayessche Interpretation  

**Ziel des Kapitels:** Erklären, warum TabPFN interessant ist und gegen welche Art von Problem beziehungsweise etablierter Methode es entwickelt wurde. Die Benchmark-Arbeit zu baumbasierten Modellen und *Transformers Can Do Bayesian Inference* gehören vor allem hierher.

### 3. Vorgehen der Literaturübersicht

3.1 Ziel und Umfang der Literaturauswahl  
3.2 Verwendete Suchquellen und Suchbegriffe  
3.3 Kriterien für Ein- und Ausschluss von Arbeiten  
3.4 Vorgehen beim strukturierten Vergleich der ausgewählten Arbeiten  

**Hinweis:** Umfang und Formalisierung dieses Kapitels mit dem Betreuer absprechen. Falls keine systematische Literaturübersicht verlangt wird, das Vorgehen dennoch transparent und angemessen knapp beschreiben.

### 4. Entwicklung von TabPFN

4.1 Ursprüngliches TabPFN: Grundidee und erste Umsetzung  
4.2 TabPFN-2.5: Erweiterungen und adressierte Grenzen  
4.3 TabPFN-3.5: weitere Änderungen und neue Fähigkeiten  
4.4 Vergleich über gemeinsame Aspekte  

| Vergleichsaspekt | Ursprüngliches TabPFN | TabPFN-2.5 | TabPFN-3.5 |
|---|---|---|---|
| Aufgaben und Datensatzgrößen |  |  |  |
| Architektur und Eingabekodierung |  |  |  |
| Synthetischer Prior / Trainingsaufgaben |  |  |  |
| Vorverarbeitung und Inferenz |  |  |  |
| Benchmarks und Vergleichsmodelle |  |  |  |
| Einschränkungen und Verfügbarkeit |  |  |  |

4.5 Zwischenfazit: Welche Probleme wurden adressiert, welche bleiben offen?

**Ziel des Kapitels:** Nicht nur drei Papers nacheinander zusammenfassen, sondern die Versionen anhand derselben Fragen vergleichen. Herstellerberichte und von den Autoren berichtete Resultate als solche kennzeichnen.

### 5. Experimenteller Vergleich

5.1 Ziel des Experiments und Bezug zur Forschungsfrage  
5.2 Datensatz und Vorhersageaufgabe  
5.3 Datenbereinigung und Vorverarbeitung  
5.4 Verglichene Modelle: ausgewählte TabPFN-Version und baumbasierte Baselines  
5.5 Versuchsaufbau: Splits, Validierung und Umgang mit Zufälligkeit  
5.6 Metriken für Vorhersageleistung  
5.7 Messung von Laufzeit und gegebenenfalls Ressourcenverbrauch  
5.8 Implementierung und Reproduzierbarkeit

**Derzeit offen:** Datensatz, konkrete Aufgabe (Klassifikation oder Regression), TabPFN-Version, Zahl und Art der Baselines, Metriken sowie Hardware. Diese Punkte nach dem Gespräch mit dem Betreuer und abhängig von den Daten festlegen. Als mögliche Baselines kommen beispielsweise XGBoost und Random Forest infrage; die endgültige Auswahl muss zum Umfang und zur verfügbaren Implementierung passen.

### 6. Ergebnisse

6.1 Ergebnisse zur Vorhersageleistung  
6.2 Ergebnisse zu Laufzeit und Ressourcen  
6.3 Vergleich der Modelle und Beobachtungen  

### 7. Diskussion

7.1 Beantwortung der Forschungsfrage anhand von Literatur und Experiment  
7.2 Einordnung der eigenen Ergebnisse im Vergleich zur Literatur  
7.3 Einfluss von Datensatz, Metrik, Split und Modellkonfiguration  
7.4 Grenzen der Untersuchung und mögliche Verzerrungen  
7.5 Praktische Aspekte: Skalierung, Verfügbarkeit und Lizenzierung

### 8. Fazit und Ausblick

8.1 Zusammenfassung der wichtigsten Erkenntnisse  
8.2 Abschließende Beantwortung der Forschungsfrage  
8.3 Ausblick auf weiterführende Untersuchungen

## Geplanter roter Faden

> **Herausforderung:** Warum sind typische tabellarische Daten für Deep Learning schwierig und baumbasierte Modelle starke Baselines?  
> **Ansatz:** Wie nutzt TabPFN synthetisches Vortraining und In-Context Learning, um tabellarische Vorhersage anders anzugehen?  
> **Entwicklung:** Wie verändern sich ausgewählte TabPFN-Meilensteine in Architektur, Prior, Skalierung und Anwendungsbreite?  
> **Überprüfung:** Wie schneidet eine festgelegte TabPFN-Version auf einer konkreten Aufgabe gegenüber baumbasierten Baselines ab?  
> **Einordnung:** Was lässt sich aus Literatur und Experiment folgern – und was bleibt aufgrund von Umfang und Versuchsbedingungen offen?

## Mit dem Betreuer zu klärende Punkte

1. Ist die geplante Kombination aus Literaturübersicht und eigenem empirischem Vergleich für die Bachelorarbeit passend?
2. Gibt es einen vom Betreuer empfohlenen Datensatz oder eine konkrete Anwendungsaufgabe? Falls nicht: Welche Anforderungen soll ein selbst ausgewählter öffentlicher Datensatz erfüllen?
3. Soll die experimentelle Aufgabe Klassifikation oder Regression sein?
4. Welche TabPFN-Version ist für die Implementierung und den vorgesehenen Einsatzzweck verfügbar und lizenzrechtlich geeignet?
5. Sind XGBoost und Random Forest als Vergleich ausreichend, oder wird eine weitere Baseline erwartet?
6. Soll die Versionsgeschichte über die drei ausgewählten Meilensteine hinaus erweitert werden, insbesondere um TabPFN-v2 und TabPFN-3?
7. Welche Anforderungen gelten an Suchstrategie, Umfang und Formalisierung der Literaturübersicht?
8. Welche Metriken, Hardware- und Laufzeitanalysen werden für den Praxisteil erwartet?

## Arbeitsstand und bewusste Abgrenzung

Diese Gliederung ist ein Gesprächs- und Planungsvorschlag, kein endgültig festgelegtes Studiendesign. Insbesondere Datensatz und experimentelle Konfiguration werden erst nach Rücksprache mit dem Betreuer bestimmt. Der Fokus liegt auf der Entwicklung von TabPFN; andere Tabular Foundation Models werden nur so weit behandelt, wie sie für Kontext oder Vergleich notwendig sind.
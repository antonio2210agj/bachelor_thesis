# 1_Benchmark – ausführliche Literaturnotiz

## Quelle und Zitierhinweis

**Grinsztajn, Leo; Oyallon, Edouard; Varoquaux, Gaël (2022):** *Why do tree-based models still outperform deep learning on typical tabular data?* NeurIPS 2022, Track on Datasets and Benchmarks.

- **PDF:** `literature/1_Benchmark.pdf`
- **Thema:** Systematischer Vergleich von baumbasierten Verfahren und Deep-Learning-Architekturen auf mittelgroßen Tabellendatensätzen sowie empirische Untersuchung, welche Eigenschaften der Daten den Leistungsunterschied erklären.
- **Hinweis zur Fundstellengenauigkeit:** Das Paper druckt keine Zeilennummern. Die Zeilenangaben in dieser Notiz zählen deshalb die aus der jeweiligen PDF-Seite extrahierten Textzeilen (in Leserichtung). Abbildungen, Bildunterschriften und mehrspaltige Elemente können die Extraktion unterbrechen. Für die Gegenprüfung zuerst die angegebene PDF-Seite und den Abschnitt aufsuchen und dann die Zeilenangabe als Orientierung verwenden.
- **Seitenzählung:** Gemeint sind die Seiten des PDFs; die Seitenzahlen im Paper stimmen ab Seite 2 mit den PDF-Seiten überein.

## 1. Kernproblem

### Ausgangslage

Deep Learning hat bei Text-, Bild- und Audiodaten große Fortschritte erzielt. Bei gewöhnlichen Tabellendaten war dagegen nicht überzeugend geklärt, ob neuronale Netze baumbasierte Ensembles tatsächlich übertreffen. In der Praxis wurden insbesondere XGBoost und andere Entscheidungsbaum-Ensembles häufig bevorzugt. Die Autoren führen die bisher widersprüchlichen Ergebnisse unter anderem darauf zurück, dass frühere Arbeiten oft nur wenige Datensätze verwendeten, Benchmarks uneinheitlich waren und der Aufwand zur Hyperparameteroptimierung nicht fair berücksichtigt wurde. **Fundstelle:** PDF S. 1, Z. 27–47; zum Vergleich mit früheren Benchmarks auch S. 2, Z. 38–50.

### Forschungsfragen

1. Bleiben baumbasierte Modelle gegenüber modernen Deep-Learning-Verfahren leistungsfähiger, wenn mehrere repräsentative Tabellendatensätze und ein umfangreiches Hyperparameter-Tuning verwendet werden?
2. Bleibt der Unterschied bestehen, wenn neuronale Netze sorgfältig abgestimmt werden und ausschließlich numerische Merkmale verwendet werden?
3. Welche Eigenschaften der Tabellendaten bzw. welche induktiven Vorannahmen der Lernverfahren könnten den Leistungsunterschied erklären?

Die Autoren beantworten die erste und zweite Frage mit einem Benchmark und untersuchen die dritte über gezielte Veränderungen der Daten. **Fundstelle:** PDF S. 1, Z. 15–26; S. 2, Z. 5–20; S. 6, Z. 19–37.

### Warum ist das wichtig?

Ohne einen gemeinsamen Benchmark kann ein Modell aufgrund günstiger Datensatzauswahl, anderer Vorverarbeitung oder intensiverer Abstimmung besser erscheinen, ohne tatsächlich allgemein überlegen zu sein. Die Studie will daher sowohl einen reproduzierbaren Vergleich als auch wiederverwendbare Benchmarkdaten bereitstellen. **Fundstelle:** PDF S. 1, Z. 39–47; S. 2, Z. 11–20.

## 2. Methodischer Ansatz / Architektur

### Datengrundlage und Auswahl

- Die Autoren stellen einen Benchmark aus **45 Tabellendatensätzen** aus verschiedenen Anwendungsdomänen zusammen; die Daten stammen hauptsächlich aus OpenML.
- Aufgenommen werden sollen Datensätze mit heterogenen, semantisch unterschiedlichen Spalten. Ausgeschlossen werden unter anderem Bild-/Signal- und Zeitreihendaten, hochdimensionale Datensätze (Merkmalszahl \(d < 500\) und Verhältnis \(d/n < 0{,}1\)), zu kleine Datensätze (weniger als 4 Merkmale oder 3.000 Stichproben), zu einfache Aufgaben sowie Ziele, die deterministisch aus den Eingaben folgen.
- Die Autoren schließen manche simulierten Datensätze nicht grundsätzlich aus: Sie behalten solche bei, die praktische Relevanz haben, und unterscheiden sie von rein künstlichen Spielzeugproblemen.
- Der Schwerpunkt liegt auf **mittelgroßen Trainingsdatensätzen**: Größere Trainingsmengen werden für den Hauptvergleich auf 10.000 Stichproben gekürzt. Ein zusätzlicher Vergleich mit 50.000 Stichproben wird im Anhang betrachtet, wobei dort weniger passende Datensätze verfügbar sind.

**Fundstelle:** PDF S. 3, Z. 17–49. Der Vergleich mit bestehenden allgemeinen Benchmark-Sammlungen, darunter OpenML CC-18/CC-100 und AutoML Benchmark, steht auf S. 3, Z. 3–9.

### Datenbereinigung und Aufgabenvereinheitlichung

Um Aufgaben möglichst vergleichbar zu halten, werden mehrere reale Problemstellungen im Hauptbenchmark bewusst ausgeklammert bzw. vereinheitlicht:

- Fehlende Werte werden entfernt: zunächst Spalten mit vielen fehlenden Einträgen, anschließend Zeilen mit mindestens einem fehlenden Wert.
- Bei Klassifikation mit mehr als zwei Klassen wird das Ziel auf die zwei häufigsten Klassen reduziert; außerdem wird eine ausgeglichene Klassenverteilung hergestellt.
- Kategoriale Merkmale mit mehr als 20 Ausprägungen werden entfernt.
- Die Autoren schreiben, dass numerische Merkmale mit weniger als 10 eindeutigen Werten entfernt und numerische Merkmale mit genau 2 Werten in kategoriale Merkmale umgewandelt werden. Diese Regeln überschneiden sich; das Paper löst nicht auf, ob die binären Merkmale von der Entfernung ausgenommen sind. Bei einer Reproduktion sollte diese Stelle daher nicht ohne zusätzliche Prüfung als eindeutige Regel umgesetzt werden.

Das ist methodisch wichtig, bedeutet aber auch, dass die Ergebnisse nicht ohne Weiteres auf fehlende Werte, hochkardinale kategoriale Merkmale oder echte Mehrklassenprobleme übertragbar sind. **Fundstelle:** PDF S. 3, Z. 44–51; S. 4, Z. 1–7.

### Verglichene Modelle

**Baumbasierte Modelle**

- Random Forest aus scikit-learn
- Gradient-Boosting-Bäume (GBT), bei kategorialen Merkmalen auch HistGradientBoostingTrees
- XGBoost

**Neuronale Netze / Deep Learning**

- **MLP:** klassisches Multi-Layer Perceptron; als zusätzliche Verbesserung wird ein Reduce-on-Plateau-Lernratenplaner eingesetzt.
- **ResNet:** MLP-nahe Architektur mit Dropout, Batch-/Layer-Normalisierung und Skip Connections.
- **FT-Transformer:** Transformer mit Feature-Tokenizer/Embeddings für numerische und kategoriale Merkmale. Die Autoren wählen ihn als besonders starke bzw. „best case“-Deep-Learning-Referenz für Tabellendaten.
- **SAINT:** Transformer mit Embedding-Modul und Attention zwischen Datenzeilen (inter-sample/row attention); aufgenommen, weil er in vorheriger Arbeit ein starkes Deep Model war und die Rolle dieser Attention geprüft werden sollte.

**Fundstelle:** PDF S. 5, Z. 1–13; SAINT-Beschreibung auf S. 6, Z. 1–4.

**Einordnung der Modellfamilien:** Das Paper testet klassische MLP-/ResNet-Modelle und ausgewählte tabellenspezifische Transformer. Es testet in diesem Benchmark **nicht** TabPFN, AutoGluon oder jedes heute verfügbare Tabular-Foundation-Modell. Die Ergebnisse sind daher kein vollständiger Vergleich aller AutoML- oder Foundation-Modelle.

### Trainingsdaten, synthetische Priors und SCMs

- Es handelt sich **nicht** um ein PFN-/Foundation-Modell, das auf synthetischen Priors oder strukturellen kausalen Modellen (SCMs) vortrainiert wird.
- Die Modelle werden auf den ausgewählten tabellarischen Benchmarks trainiert und anhand von Validierungsdaten abgestimmt.
- Die Studie verändert Daten für zusätzliche Diagnoseexperimente (z. B. Glättung der Zielstruktur, Entfernen/Hinzufügen irrelevanter Merkmale, zufällige Rotation). Diese Experimente sind keine synthetische Vortrainingsprior des Modells.

**Fundstelle:** Datenauswahl S. 3, Z. 17–29; Tuning-Verfahren S. 4, Z. 8–27; diagnostische Transformationen S. 6, Z. 32–37; S. 7–9.

### Hyperparameteroptimierung und Auswertung

- Die Autoren verwenden Random Search. Die Suchräume stammen, soweit verfügbar, aus Hyperopt-Sklearn, dem jeweiligen Originalpaper oder früheren Arbeiten.
- Pro Datensatz werden ungefähr 400 Konfigurationen untersucht; Baummodelle laufen auf CPUs und neuronale Netze auf GPUs.
- Die Standardkonfiguration jedes Modells ist stets der erste Suchpunkt.
- Für jede Anzahl von Suchläufen wird die auf dem Validierungssatz beste Konfiguration ausgewählt und auf dem Testsatz bewertet. Die Reihenfolge der Suchläufe wird 15-mal neu gemischt, um die Auswirkungen eines begrenzten Tuningbudgets sichtbar zu machen.
- Die Autoren berichten, dass Bayesian Optimization statt Random Search ihre Schlussfolgerungen nicht wesentlich änderte.
- Für Klassifikation wird Accuracy, für Regression \(R^2\) verwendet. Da Aufgaben unterschiedlich schwer sind, normalisieren sie die Ergebnisse pro Datensatz auf eine Skala zwischen 0 und 1 und aggregieren diese Kennzahl über Datensätze. Bei Regression werden negative normalisierte Werte auf 0 begrenzt.

**Fundstelle:** PDF S. 4, Z. 8–37. Die Beschreibung der 15 Suchreihenfolgen und der Kurven in Abbildung 1 findet sich zusätzlich in der Bildunterschrift auf S. 5, Z. 83–87.

## 3. Wichtigste Ergebnisse

### Gesamtergebnis

Die baumbasierten Modelle schneiden im untersuchten mittelgroßen Tabellendaten-Regime über die untersuchten Budgets der Hyperparameter-Suche hinweg besser ab als die neuronalen Netze. Der Abstand bleibt auch nach umfangreicherem Tuning bestehen. Die Hauptabbildung vergleicht Suchbudgets nach der Anzahl der Iterationen, nicht nach einem für alle Modelle identischen Zeitbudget. Da ein Suchlauf für neuronale Netze im Allgemeinen langsamer ist, bildet dieser Vergleich den zusätzlichen Laufzeitvorteil der Bäume nicht vollständig ab; das Paper nennt im Haupttext aber keinen pauschalen Laufzeitfaktor. **Fundstelle:** PDF S. 6, Z. 5–13.

Die zentrale Schlussfolgerung der Autoren lautet nicht, dass neuronale Netze grundsätzlich ungeeignet sind, sondern dass Baum-Ensembles für diese typische Datenlage leichter gute Vorhersagen mit geringerem Rechenaufwand liefern. **Fundstelle:** PDF S. 9, Z. 26–35.

### Kategorien sind nicht die ganze Erklärung

Der Abstand zwischen Bäumen und neuronalen Netzen wird kleiner, wenn nur numerische Merkmale betrachtet werden. Er verschwindet aber nicht: Auch bei numerischen Merkmalen bleibt der Großteil des Leistungsabstands bestehen. Kategoriale Daten allein erklären die Überlegenheit der Bäume demnach nicht. **Fundstelle:** PDF S. 6, Z. 14–18.

### Empirische Erklärung 1: unregelmäßige Zielzusammenhänge

Die Autoren glätten die Zielwerte des Trainingsdatensatzes mit einem Gaußschen Kernel und variieren die Glättungsstärke. Bei geringer Glättung sinkt die Genauigkeit der Baummodelle deutlich, während die neuronalen Netze weniger stark beeinflusst werden. Daraus leiten sie ab, dass die ursprünglichen Zielzusammenhänge häufig unregelmäßig sind und neuronale Netze Schwierigkeiten haben können, solche hochfrequenten bzw. nicht glatten Muster zu lernen. Entscheidungsbäume repräsentieren stückweise konstante Funktionen und zeigen diese spezielle Glättungstendenz nach Interpretation der Autoren weniger stark.

Die Autoren relativieren ausdrücklich: Das widerspricht nicht der Forschung zu Regularisierung. Geeignete Regularisierung und sorgfältige Optimierung könnten neuronalen Netzen helfen, auch unregelmäßige Muster zu lernen. **Fundstelle:** PDF S. 6, Z. 38–49; S. 7, Z. 16–24.

### Empirische Erklärung 2: irrelevante Merkmale

- In den Datensätzen finden die Autoren viele Merkmale, die wenig Information für das Ziel enthalten.
- Ein Gradient-Boosting-Baum bleibt relativ robust, wenn bis zur Hälfte der Merkmale entfernt wird. Modelle, die nur mit den als unwichtig eingestuften Merkmalen trainiert werden, schneiden entsprechend schwach ab.
- Das Entfernen irrelevanter Merkmale verringert den Abstand zwischen ResNet/MLP und den anderen Modellen; das Hinzufügen unkorrelierter, irrelevanter Merkmale vergrößert ihn.
- Daraus folgern die Autoren, dass MLP-nahe Modelle weniger robust gegenüber irrelevanten Merkmalen sind. Das ist angesichts ihrer Häufigkeit in Tabellendaten eine mögliche Teilerklärung des Benchmark-Ergebnisses.

**Fundstelle:** PDF S. 7, Z. 25–41. Abbildung 4 erläutert, dass hinzugefügte Störmerkmale aus unabhängigen Standardnormalverteilungen gezogen wurden: PDF S. 8, Z. 59–63.

### Empirische Erklärung 3: Bedeutung der ursprünglichen Merkmalsorientierung

Die Autoren beschreiben MLPs als rotationsinvariant: Die Lernprozedur verändert sich nicht, wenn die Eingabemerkmale gemeinsam rotiert werden. Bäume berücksichtigen dagegen einzelne Merkmale separat und sind nicht rotationsinvariant; auch der FT-Tokenizer führt eine merkmalsweise Operation aus. In Tabellendaten besitzen Spalten oft eine eigene Bedeutung (z. B. Alter oder Gewicht), sodass die ursprüngliche Merkmalsbasis wichtig sein kann.

Bei zufälliger Rotation der Daten kehrt sich die Rangfolge teilweise um: Neuronale Netze liegen dann vor den baumbasierten Modellen, und ResNets vor FT-Transformern. Das stützt die Interpretation, dass Rotationsinvarianz bei gewöhnlichen Tabellendaten nicht immer hilfreich ist. Die Befunde hängen mit irrelevanten Merkmalen zusammen, weil eine rotationsinvariante Methode die ursprüngliche Orientierung erst rekonstruieren müsste, bevor sie irrelevante Dimensionen gezielt aussortieren kann.

**Fundstelle:** PDF S. 7, Z. 43–49; S. 8, Z. 64–80; Ergänzung zur Rolle merkmalsweiser Embeddings S. 9, Z. 7–10.

### Benchmarks und Baselines: wichtige Präzisierung

- Die Studie vergleicht **nicht** nur gegen XGBoost: Sie enthält außerdem Random Forest und Gradient-Boosting-Varianten.
- Die Deep-Learning-Gegner sind MLP, ResNet, FT-Transformer und SAINT.
- Der Benchmark ist eine eigene kuratierte Sammlung aus 45 Datensätzen, **nicht OpenML-CC18**. CC-18/CC-100 und AutoML Benchmark werden im Related-Work-Teil als bestehende Sammlungen erwähnt, nicht als die zentrale Evaluationsbasis dieser Arbeit. **Fundstelle:** PDF S. 3, Z. 3–9, 17–20.
- In Abbildung 1 werden Ergebnisse für numerische Features (Klassifikation: 16 Datensätze; Regression: 19) und für numerische plus kategoriale Features (Klassifikation: 7; Regression: 17) getrennt dargestellt. Die Teilmengen können sich überschneiden; diese Zahlen sind daher nicht zu einer neuen Gesamtzahl zu addieren. **Fundstelle:** PDF S. 5, Z. 27–31, 44–48, 62–66, 79–87.
- Das Paper liefert an den hier ausgewerteten Textstellen **keinen einzelnen prozentualen Gewinn** wie „XGBoost ist um Y Prozent genauer“ und keinen pauschalen Laufzeitfaktor. Die Diagramme zeigen normalisierte Testwerte über Suchbudgets; der Text formuliert die Resultate überwiegend qualitativ. Daher keine präzise Prozentdifferenz oder „x-mal schneller“-Zahl aus dieser Arbeit zitieren.

## 4. Konkrete Limitierungen (besonders relevant für die Diskussion)

### Von den Autoren explizit genannte offene Punkte

Die Autoren nennen als mögliche Erweiterungen:

- weitere Größenregime, insbesondere kleine und sehr große Datensätze;
- Mehrklassenklassifikation;
- andere Metriken, besonders die Qualität probabilistischer Vorhersagen;
- systematische Untersuchung fehlender Daten und hochkardinaler kategorialer Merkmale;
- bessere Erklärung weiterer induktiver Vorannahmen baumbasierter Modelle und Untersuchung des Nutzens gelernter Embeddings für nachgelagerte Aufgaben.

**Fundstelle:** PDF S. 9, Z. 11–25.

### Einschränkungen durch Auswahl und Vorverarbeitung

- **Kein Missing-Data-Benchmark:** Fehlende Werte werden entfernt. Das Paper untersucht daher nicht, welches Modell fehlende Werte am besten behandelt. **Fundstelle:** S. 3, Z. 44–51; S. 4, Z. 1–2.
- **Kein echter Mehrklassenvergleich:** Mehrklassen-Ziele werden auf die zwei häufigsten Klassen reduziert und ausgeglichen. Das ist nicht gleichbedeutend mit der Leistung im ursprünglichen Mehrklassenproblem. **Fundstelle:** S. 4, Z. 3–4; als offene Erweiterung S. 9, Z. 16–17.
- **Hohe Kardinalitäten beschnitten:** Kategoriale Merkmale über 20 Ausprägungen werden entfernt; der Umgang mit ihnen wird als offene Forschungsfrage genannt. **Fundstelle:** S. 4, Z. 5; S. 9, Z. 20–22.
- **Begrenzter Datensatzbereich:** Es werden Datensätze mit weniger als 3.000 Stichproben bzw. weniger als 4 Merkmalen ausgeschlossen; der Hauptvergleich fokussiert auf höchstens 10.000 Trainingsbeispiele und moderate Dimensionalität. Zeitreihen, Streaming- und hochdimensionale Probleme liegen außerhalb des Geltungsbereichs. **Fundstelle:** S. 3, Z. 21–32, 44–49.
- **Kuratiertes Sample:** 45 ausgewählte Datensätze sind umfangreicher als viele frühere Vergleiche, repräsentieren aber nicht sämtliche Branchen, Datenverteilungen oder Aufgaben. Die Autoren weisen selbst auf Erweiterungen zu weiteren Datensatzgrößen hin. **Fundstelle:** S. 3, Z. 17–20; S. 9, Z. 12–17.

### Einschränkungen durch Vergleichsdesign und Interpretation

- **Keine identische Laufzeit pro Modell:** Die Zahl der Suchläufe wird verglichen, obwohl neuronale Netzläufe meist langsamer sind. Ein Vergleich bei identischem Zeitbudget könnte den Unterschied bei der Zahl der ausprobierten Konfigurationen und damit den Rechenaufwand deutlicher machen. Einen genauen Laufzeitfaktor liefert das Paper im Haupttext aber nicht. **Fundstelle:** S. 6, Z. 10–13; S. 9, Z. 29–30.
- **Unsicherheit der Tuningkurven:** Die 15 Kurvenvarianten entstehen durch Umordnen derselben Random-Search-Kandidaten. Die Autoren warnen, dass die resultierende Streuung bei vielen Suchläufen nicht unbedingt die tatsächliche Varianz nach diesem Suchbudget abbildet. **Fundstelle:** S. 6, Z. 6–9.
- **Begrenzte Modellabdeckung:** Der Vergleich ist für die untersuchten Verfahren und den Publikationsstand von 2022 aussagekräftig, umfasst aber keine späteren Methoden und nicht jede mögliche tabellenspezifische Architektur. Insbesondere darf daraus nicht abgeleitet werden, dass AutoGluon oder TabPFN getestet und geschlagen worden seien. Modellliste: S. 5, Z. 1–13; S. 6, Z. 1–4.
- **Mechanistische Befunde sind empirische Erklärungen, kein abschließender Beweis:** Glättung, Feature-Manipulation und Rotation zeigen, welche Veränderungen die Modellabstände verschieben. Die Studie bezeichnet weitere induktive Vorannahmen ausdrücklich als offene Frage. **Fundstelle:** S. 6, Z. 32–37; S. 9, Z. 12–14.
- **Metriken:** Accuracy und \(R^2\) decken nicht alle praktischen Ziele ab, insbesondere nicht probabilistische Klassifikationsgüte. Das nennen die Autoren selbst als Erweiterung. **Fundstelle:** S. 4, Z. 28–37; S. 9, Z. 18–19.

### Was man aus dem Paper nicht folgern sollte

1. Nicht: „Deep Learning ist für Tabellendaten immer schlechter.“ Die Evidenz gilt für den kuratierten Datensatzbereich, die getesteten Architekturen und das verwendete Evaluationsdesign.
2. Nicht: „Kategoriale Features erklären den gesamten Baumvorteil.“ Der Abstand bleibt laut Paper auch mit ausschließlich numerischen Merkmalen bestehen.
3. Nicht: „AutoGluon/TabPFN verliert gegen XGBoost.“ Diese Systeme sind keine Baselines des Experiments.
4. Nicht: „Die Bäume sind exakt X-mal schneller“ oder „um eine bestimmte Prozentzahl genauer.“ Für solche Zahlen gibt der Haupttext keinen pauschalen Wert an.
5. Nicht: „Neuronale Netze können keine irregulären Funktionen lernen.“ Die Autoren nennen Regularisierung und sorgfältige Optimierung ausdrücklich als mögliche Gegenmittel.

## 5. Relevanz für meine Bachelorarbeit

### Geeignete Verwendung

- **Kapitel „Stand der Technik / Tabellarisches Deep Learning“:** als systematische Gegenposition zur verbreiteten Annahme, dass modernere neuronale Architekturen klassische Baum-Ensembles automatisch übertreffen. Hier besonders die kontrollierte Benchmarkmethodik, Modellfamilien und Hauptergebnis heranziehen.
- **Kapitel „Benchmarking / Evaluation“:** als Begründung, warum Datensatzwahl, Hyperparameterbudget, Wiederholungen, Laufzeit und passende Metriken transparent berichtet werden müssen.
- **Kapitel „Skalierung und Grenzen“:** als Ausgangspunkt, um den Unterschied zwischen mittelgroßen Datensätzen (Hauptfokus bis 10.000 Trainingsbeispiele) und größeren Regimen zu diskutieren. Der 50.000-Stichproben-Vergleich steht im Anhang und hat laut Paper weniger passende Datensätze.
- **Diskussion / Limitationen:** fehlende Werte, Mehrklassenprobleme, hohe Kardinalitäten, probabilistische Metriken und die starke Modell-/Datensatzselektion sind unmittelbar brauchbare Einschränkungen.
- **Motivation für neuere Verfahren:** das Paper liefert einen wichtigen historischen Benchmark-Stand (NeurIPS 2022), aber keinen Vergleich gegen aktuelle Verfahren wie TabPFN oder moderne AutoML-Ensembles. Für eine Arbeit, die solche Modelle untersucht, eignet es sich als Baseline-/Motivationsquelle, nicht als abschließender Leistungsvergleich.

### Mögliche Formulierung für die Arbeit (indirektes Zitat)

> Grinsztajn et al. zeigen in einem Benchmark mit 45 kuratierten Tabellendatensätzen, dass baumbasierte Modelle die untersuchten neuronalen Verfahren im mittelgroßen Datensatzregime trotz umfangreicher Hyperparametersuche übertreffen. Als mögliche Erklärungen diskutieren sie die Robustheit gegenüber irrelevanten Merkmalen, die Eignung für unregelmäßige Zielzusammenhänge und die Bedeutung der ursprünglichen Merkmalsorientierung. (Grinsztajn et al., 2022, S. 1, 6–9)

Diese Paraphrase sollte an den tatsächlichen Fokus der Bachelorarbeit angepasst werden; insbesondere keine Aussage über ungetestete Modelle ergänzen.

## 6. Wörtliches Schlüsselzitat

> “Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations.”

**Fundstelle:** PDF S. 6, Z. 10–12, Abschnitt 4.2 („Results“).

**Arbeitsübersetzung:** „Baumbasierte Modelle sind bei jedem betrachteten Budget der Random Search überlegen, und der Leistungsabstand bleibt selbst nach einer großen Zahl von Random-Search-Durchläufen deutlich.“

Für ein direktes Zitat in der Bachelorarbeit das englische Original verwenden und die Zitierweise der Hochschule beachten. Für eine vorsichtigere wissenschaftliche Formulierung eignet sich ein indirektes Zitat mit dem Zusatz „im untersuchten Benchmark“.

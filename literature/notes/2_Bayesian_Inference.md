# Müller et al. (2022): *Transformers Can Do Bayesian Inference*

## Quelle und Zitierhinweis

**Samuel Müller, Noah Hollmann, Sebastian Pineda, Josif Grabocka und Frank Hutter (2022).** *Transformers Can Do Bayesian Inference.* International Conference on Learning Representations (ICLR 2022). Die PDF-Datei enthält die Konferenzfassung sowie Anhänge; auf der ersten PDF-Seite steht zusätzlich die arXiv-Kennung arXiv:2112.10510v7 (13. Aug. 2024).

- **PDF:** `literature/2_Bayesian_Inference.pdf`
- **Hauptbeitrag:** Prior-Fitted Networks (PFNs), eine Methode, die mit künstlich erzeugten Aufgaben aus einem spezifizierten Prior trainiert wird und anschließend die posterior-prädiktive Verteilung (PPD) mit einem einzigen Transformer-Forward-Pass approximiert.
- **Fundstellenformat:** Das Paper druckt keine Zeilennummern. Die Zeilenangaben dieser Notiz zählen den extrahierten PDF-Text der jeweiligen PDF-Seite und dienen als Suchhilfe; Abbildungen und Tabellen können die Extraktion unterbrechen. Zur Kontrolle zuerst die Seite und den Abschnitt aufrufen.
- **Seitenangabe:** „PDF S.“ bezeichnet die PDF-Seite (insgesamt 24 Seiten). Die ersten zehn Seiten sind der Haupttext; ab PDF S. 15 folgen Anhänge.

## 1. Kernproblem

### Ausgangslage

Bayessche Verfahren bieten eine explizite Möglichkeit, Vorwissen über die Datenerzeugung auszudrücken und Unsicherheit in Vorhersagen abzubilden. Ihr praktischer Nachteil: Die posterior-prädiktive Verteilung ist für viele Modelle nicht exakt berechenbar. Klassische Näherungsverfahren wie MCMC/NUTS können genau, aber langsam sein; Variational Inference (VI) ersetzt den Posterior durch eine handhabbare Näherung, die ebenfalls rechenintensiv sein kann. **Fundstelle:** PDF S. 1, Z. 7–25; S. 2, Z. 10–20; S. 3, Z. 23–31.

### Forschungsfrage

Können Transformer durch Lernen über viele aus einem Prior simulierte Datensätze die Bayes’sche Inferenz selbst approximieren, sodass für einen neuen Datensatz keine iterative Posterioroptimierung oder MCMC-Sampling-Schleife mehr notwendig ist? Die wesentliche Voraussetzung ist, dass man aus dem gewünschten Prior über Lernaufgaben bzw. Funktionen Daten generieren kann. **Fundstelle:** PDF S. 1, Z. 11–20; S. 2, Z. 21–34.

### Zielgröße

Das Ziel ist die **posterior-prädiktive Verteilung**:

\[
p(y \mid x,D)=\int p(y\mid x,\theta)\,p(\theta\mid D)\,d\theta,
\]

wobei \(D\) die beobachteten Trainingsbeispiele und \(x\) ein neuer Abfragepunkt ist. PFNs lernen diese Vorhersageverteilung direkt; sie müssen nicht erst explizit den Posterior über Modellparameter \(\theta\) schätzen. **Fundstelle:** PDF S. 3, Z. 12–25, Abschnitt 3; S. 4, Z. 31–40.

## 2. Methodischer Ansatz / Architektur

### PFN in einem Satz

Ein PFN ist ein Transformer, der während des Meta-Trainings viele synthetische Datensätze aus einem Aufgabenprior sieht. Für jeweils zurückgehaltene Labels lernt er, bedingt auf die übrigen gelabelten Beispiele eine prädiktive Verteilung vorherzusagen. Zur Inferenz erhält derselbe Transformer einen neuen Trainingsdatensatz und Abfragepunkte und gibt die approximierte PPD direkt aus. Das ist In-Context Learning über Beispieldatensätze, nicht ein erneutes Gradienten-Finetuning pro Testdatensatz. **Fundstelle:** PDF S. 1, Z. 13–20 und Bildunterschrift Abb. 1, Z. 60–62; S. 2, Z. 21–30.

### Trainingsverfahren und Zielfunktion

1. Der Anwender spezifiziert einen Prior \(p(D)\) über supervised Lernaufgaben bzw. die Funktionen, die Daten erzeugen.
2. Für jedes Meta-Trainingsbeispiel wird ein Datensatz aus diesem Prior gezogen.
3. Ein Label wird als Abfrage zurückgehalten; die übrigen Beispiele bilden den Kontext.
4. Der Transformer sagt eine Wahrscheinlichkeitsverteilung über das zurückgehaltene Label voraus.
5. Trainiert wird mit der **Prior-Data Negative Log-Likelihood (Prior-Data NLL)**, also der mittleren negativen Log-Wahrscheinlichkeit der gehaltenen Labels.

Die Autoren zeigen, dass diese Zielfunktion dem erwarteten Cross-Entropy zwischen echter und approximierter PPD entspricht und – bis auf eine additive Konstante – der erwarteten KL-Divergenz. Damit hat die supervised Trainingsloss eine direkte Interpretation als Gütemaß der Bayes’schen Vorhersageverteilung unter dem Trainingsprior. **Fundstelle:** PDF S. 2, Z. 23–30; S. 3, Z. 47–58; S. 4, Z. 24–40 und 56–61.

### Transformer-Architektur

- Verwendet wird ein Transformer-Encoder ohne Positionskodierungen, damit die Vorhersage nicht von der Reihenfolge der Beispiele im Datensatz abhängt.
- Eingabepaare \((x_i,y_i)\) und Abfragepunkte werden als Menge von Eingaben verarbeitet; die Autoren nutzen einfache lineare Projektionen zur Kodierung.
- Die Attention-Maske lässt Kontextbeispiele aufeinander und Abfragen auf die Kontextbeispiele zugreifen. Abfragepunkte attendieren nicht gegenseitig aufeinander, da ihre Vorhersagen unabhängig voneinander sein sollen, gegeben den Trainingsdatensatz.
- Die Gesamtsequenzlänge \(N=n+m\) aus \(n\) Kontextbeispielen und \(m\) Abfragen wird im Training festgelegt. Die Kontextgröße \(n\) wird variiert, damit das Modell unterschiedliche Datensatzgrößen verarbeiten kann.
- Für Klassifikation werden Sigmoid bzw. Softmax verwendet; für Regression schlagen die Autoren eine eigene Verteilungskodierung vor.

**Fundstelle:** PDF S. 5, Z. 21–30; detaillierte Architektur im Anhang PDF S. 18, Z. 4–20.

### Riemann-Verteilung für Regression

Für kontinuierliche Zielgrößen verwenden die Autoren keine einfache Normalverteilung als Ausgabekopf. Stattdessen modellieren sie die Dichte über diskrete Intervalle („Buckets“), die anhand des Prior-Datensatzes so gewählt werden, dass ungefähr gleich viel Prior-Wahrscheinlichkeit in jedem Bucket liegt. Die Dichte innerhalb eines Buckets ergibt sich aus der Bucket-Wahrscheinlichkeit und dessen Breite. Bei unbeschränktem Träger werden die äußeren Intervalle mit skalierten Halbnormalverteilungen ergänzt. So soll ein Transformer flexible, gegebenenfalls multimodale Vorhersageverteilungen darstellen können. **Fundstelle:** PDF S. 5, Z. 31–44; formale Definition im Anhang PDF S. 18, Z. 21–45.

### Welche Priors und synthetischen Daten?

PFNs sind **nicht an einen einzelnen Prior oder ausschließlich an SCMs gebunden**. Sie können prinzipiell jeden Prior nutzen, aus dem sich Aufgaben-Datensätze ziehen lassen. In diesem Paper werden insbesondere folgende Priors demonstriert:

- **Gaussian-Process-(GP)-Prior:** Eingaben werden aus dem Einheitswürfel gezogen, Funktionswerte anschließend aus einer multivariaten Normalverteilung mit der durch den Kernel definierten Kovarianzmatrix. Der feste GP-Prior liefert einen exakten Posterior als Ground Truth für den Vergleich. **Fundstelle:** PDF S. 6, Z. 26–48.
- **GP mit Hyperpriors:** Auch GP-Hyperparameter wie Länge/Glattheit, Rauschvarianz und Skalierung werden aus Verteilungen gezogen. Dadurch wird eine breitere Funktionsfamilie modelliert, deren PPD nicht mehr geschlossen berechenbar ist. **Fundstelle:** PDF S. 6, Z. 49–55; Fortsetzung und Baselines PDF S. 7, Z. 20–30.
- **Bayesian-Neural-Network-(BNN)-Prior:** Es werden Gewichte und – in einer Erweiterung – Netzwerkarchitekturen gezogen. Mit i.i.d. normalverteilten Eingabefeatures erzeugt das jeweilige Netzwerk die Zielwerte. Variiert werden u. a. Zahl der Schichten, Hidden Units, Sparsity, Aktivierungsfunktion und Rauschen. **Fundstelle:** PDF S. 7, Z. 31–44; S. 8, Z. 23–45; Anhang S. 20, Z. 43–46.
- **Omniglot-/Symbolprior:** Für Few-Shot-Lernen wird ein einfacher Prior aus zufälligen Linienmustern als handschriftähnliche Klassenprototypen konstruiert; in diesem Versuch wird das PFN anschließend zusätzlich auf Omniglot-Trainingsaufgaben feinabgestimmt. **Fundstelle:** PDF S. 9, Z. 20–39.

**SCM-Einordnung:** In der vorliegenden Arbeit werden GP-, BNN- und Linien-Priors beschrieben; ein SCM-Prior ist nicht der zentrale Ansatz und wird für die genannten Experimente nicht als Datengenerator berichtet.

### Prior-Wahl und Vortraining

Die Wahl des Priors ist zentral: Der PFN approximiert die Bayes’sche Vorhersage **unter dem verwendeten Prior**. Für die Tabular-Experimente werden die Hyperparameter des Priors auf einem separaten Satz von sechs Validierungsdatensätzen festgelegt; anschließend wird je Prior ein trainiertes Transformer-Modell über die Evaluationsdatensätze wiederverwendet. Die Autoren betonen, dass die PFN-Transformer nicht pro Evaluationsdatensatz neu abgestimmt werden, die Prior-Hyperparameter aber zuvor durchaus gewählt werden müssen. **Fundstelle:** PDF S. 8, Z. 46–63; Anhang S. 20, Z. 47–55.

Als Größenordnung für die vorgelagerte Kostenrechnung berichten die Autoren im Anhang 100 Epochen Vortraining: 2 h 44 min für den GP-Prior und 3 h 14 min für den BNN-Prior. Diese Modelle werden anschließend für viele Datensätze wiederverwendet. **Fundstelle:** PDF S. 20, Z. 59–61.

## 3. Wichtigste Ergebnisse

### A. Approximation von Gaussian Processes

Bei festen GP-Hyperparametern kommt die approximierte PPD den exakten GP-Vorhersagen sehr nahe. Die Qualität verbessert sich mit mehr Meta-Trainingsdatensätzen. Bei GP-Hyperpriors nähert sich der PFN der nicht exakt verfügbaren PPD besser an als die untersuchten MLE-II- und NUTS-Baselines und benötigt laut Paper deutlich weniger Inferenzzeit. **Fundstelle:** PDF S. 6, Z. 36–48; Abb. 4 und Bildunterschrift S. 6, Z. 20–25; Geschwindigkeitsangaben S. 7, Z. 20–30.

### B. Approximation von Bayesian Neural Networks

In den untersuchten BNN-Setups erreichen PFNs eine vergleichbare bzw. bessere Prior-Data-NLL als die verglichenen Inferenzverfahren bei wesentlich geringerer Inferenzzeit. Im Text werden für die konkret untersuchten Architekturen ungefähr **1.000×** gegenüber Bayes-by-Backprop-SVI und **10.000×** gegenüber NUTS genannt, um eine ähnliche Güte zu erreichen. Das sind Resultate der beschriebenen synthetischen BNN-Prior-Experimente, keine universellen Laufzeitgarantien. **Fundstelle:** PDF S. 7, Z. 31–44; Abb. 5 beschreibt die dort untersuchten kleinen BNN-Architekturen, Z. 15–19.

### C. Kleine tabellarische Klassifikationsaufgaben

**Evaluationsdesign**

- Die Datensätze stammen aus dem **OpenML AutoML Benchmark**, nicht aus OpenML-CC18.
- Es werden Datensätze mit mehr als 100 Merkmalen und Datensätze mit fehlenden Werten entfernt; daraus verbleiben 20 tabellarische Klassifikationsdatensätze mit numerischen und kategorialen Merkmalen.
- Jede Aufgabe wird zu balancierter binärer Klassifikation vereinfacht.
- Pro Datensatz werden 20 Teilmengen mit je 100 Beispielen gezogen. Für die Inferenz erhält das Modell die Labels der ersten 30; die übrigen 70 dienen der Evaluation.
- Zusätzlich werden sechs andere Datensätze verwendet, um allgemeine Hyperparameterbereiche der Prior-Modelle sowie der Baselines festzulegen.

**Fundstelle:** PDF S. 8, Z. 46–55; Liste der Evaluationsdatensätze im Anhang S. 22, Z. 2–24; Liste der sechs Hyperparameter-/Validierungsdatensätze S. 22, Z. 25–33.

**Verglichene Verfahren**

- PFN mit GP-Prior (PFN-GP)
- PFN mit BNN-Prior und Prior über Architekturen (PFN-BNN)
- Logistische Regression, Gaussian Process (RBF), K-Nearest Neighbors
- BNN mit Bayes-by-Backprop/SVI
- CatBoost und XGBoost

Die Baselines werden mit Grid Search und 5-facher Cross-Validation pro Datensatz abgestimmt. CatBoost erhält zusätzlich die Information, welche Features kategorial sind. **Fundstelle:** PDF S. 8, Z. 56–63.

**Leistung**

- PFN-BNN erreicht den besten mittleren Rang bei ROC-AUC: **2,786**. PFN-GP liegt bei **3,833**, XGBoost bei **3,357**, CatBoost bei **4,833**; kleinere mittlere Ränge sind besser. PFN-GP ist demnach nicht die beste Variante in dieser Tabelle; der stärkste PFN ist PFN-BNN.
- Der PFN-BNN zeigt in Tabelle 1 außerdem den niedrigsten Expected Calibration Error (ECE): **0,025**, gegenüber **0,066** bei XGBoost und **0,089** bei CatBoost. Die Autoren berichten somit sowohl gute Rangfolge bei ROC-AUC als auch besonders gute Kalibrierung.
- Die Tabelle enthält Loss/Tie/Win- und Wilcoxon-Angaben für PFN-BNN im Vergleich zu jeder Baseline. Die berichteten Wilcoxon-p-Werte sind klein; die Autoren interpretieren die Verbesserung auf den betrachteten Datensätzen als statistisch signifikant.

**Fundstelle:** PDF S. 9, Z. 2–9; Erläuterung der statistischen Tests PDF S. 8, Z. 64–71; Kalibrierung PDF S. 9, Z. 15–19.

### D. Laufzeit – was die Zahlen tatsächlich bedeuten

Für die **Tabellen-Auswertung** berichtet der Haupttext 13 Sekunden auf einer Nvidia Tesla V100 für die PFN-Inferenz auf allen 20 Evaluationsdatensätzen zusammen; XGBoost benötigte in der Tabelle ungefähr 20 Stunden. Das Paper formuliert daraus einen Faktor von über 5.000 gegenüber XGBoost. **Fundstelle:** PDF S. 9, Z. 10–14; Tabelle 1, Z. 7–9.

Diese Zahl ist als **amortisierte Inferenz nach PFN-Vortraining** zu lesen, nicht als Vergleich vollständiger End-to-End-Kosten ab null. Die einmaligen Kosten des PFN-Vortrainings und die Suche nach Prior-Hyperparametern auf Validierungsdatensätzen sind getrennt zu berücksichtigen. Im Anhang nennt das Paper für 100 Vortrainingsepochen 2:44 h (GP-Prior) bzw. 3:14 h (BNN-Prior); diese Modelle werden für alle Evaluationsdatensätze wiederverwendet. Baselines durchlaufen dagegen ihre Cross-Validation/Hyperparametersuche pro Datensatz. **Fundstelle:** PDF S. 8, Z. 52–63; S. 9, Z. 10–14; S. 20, Z. 47–61.

**Einordnung:** Der Vorteil ist besonders relevant, wenn derselbe gelernte Prior/Transformer für viele neue kleine Aufgaben eingesetzt wird. Bei nur einem einzelnen Datensatz oder häufig wechselnden Aufgabendomänen muss man Vortraining, Prioranpassung und Inferenz gemeinsam betrachten.

### E. Few-Shot-Lernen auf Omniglot

Mit einem künstlichen Linienprior und anschließendem Fine-Tuning auf Omniglot erreicht das PFN **0,865 ± 0,019** Genauigkeit im berichteten 5-shot-5-way-Setting. PACOH-NN liegt bei **0,885 ± 0,090**; die Autoren bezeichnen PFN als Ergebnis auf dem Niveau des damaligen State of the Art. Dieser Versuch unterscheidet sich vom tabellarischen Setup, weil hier explizit auf den Omniglot-Trainingsaufgaben feinabgestimmt wird. **Fundstelle:** PDF S. 9, Z. 20–45.

## 4. Konkrete Limitierungen (besonders wichtig für die Diskussion)

### Von den Autoren ausdrücklich genannte Zukunftsfragen

Im Schlussabschnitt nennen die Autoren als wichtige nächste Schritte:

1. neue Priors entwickeln, deren Approximation durch PFNs möglich wird;
2. Architekturen entwickeln, die besser für die Aufgabe geeignet sind, da hier nur eine leichte Anpassung bestehender Transformer verwendet wurde;
3. PFNs auf größere Realweltprobleme skalieren;
4. PFNs für amortisierte Simulation-Based Inference einsetzen.

**Fundstelle:** PDF S. 10, Z. 2–9.

### Geltungsbereich der Tabular-Ergebnisse

- **Nur kleine Aufgaben im zentralen Tabular-Benchmark:** Die Auswertung gibt den PFNs 30 gelabelte Beispiele zur Inferenz pro Teilaufgabe. Sie belegt deshalb nicht direkt die Leistung bei Tausenden gelabelten Beispielen oder sehr großen Datensätzen. **Fundstelle:** PDF S. 8, Z. 46–55; Tabelle 1 auf S. 9, Z. 7–9.
- **Binary statt ursprünglicher Mehrklassenaufgabe:** Die Datensätze werden zu balancierter binärer Klassifikation vereinfacht. Die Ergebnisse lassen sich nicht unverändert auf natürliche Mehrklassenprobleme übertragen. **Fundstelle:** PDF S. 8, Z. 48–51.
- **Fehlende Werte und sehr hohe Dimensionalität ausgeschlossen:** Es werden Datensätze mit Missing Values und mit mehr als 100 Features entfernt. Die Evaluation demonstriert damit nicht die Robustheit gegenüber NaNs oder extrem hochdimensionalen Eingaben. **Fundstelle:** PDF S. 8, Z. 46–49; Anhang S. 22, Z. 23–24.
- **Feste maximale Featurezahl im Tabular-PFN:** Die Eingabeprojektion hat eine feste Größe. Für die ausgewerteten Datensätze setzen die Autoren deshalb ein Maximum von 60 Features und füllen kleinere Featurevektoren mit Nullen auf. Das ist eine konkrete Architekturgrenze des Tabular-Experiments und nicht gleichbedeutend mit unbegrenzter Dimensionalität. **Fundstelle:** PDF S. 20, Z. 35–42.
- **Keine OpenML-CC18-Evaluation:** Der Benchmark stammt aus OpenML AutoML Benchmark, wurde gefiltert und weiter zu kleinen binären Teilaufgaben umgeformt. Resultate sind nicht direkt mit Ergebnissen auf CC18 oder dem Benchmark aus Grinsztajn et al. (2022) gleichzusetzen. **Fundstelle:** PDF S. 8, Z. 46–55.

### Abhängigkeit vom Prior und mögliche Prior-Mismatch-Probleme

- PFNs approximieren die PPD **des gewählten Priors**. Ein PFN mit GP-Prior ist nicht automatisch ein guter Inferenzalgorithmus für Daten, deren Struktur durch eine andere Generierungsfamilie beschrieben wird; analog ist ein BNN-Prior keine universelle Garantie.
- Die Voraussetzung „aus dem Prior sampeln können“ ist konzeptionell einfach, aber der Nutzen hängt davon ab, ob der Prior plausible Aufgaben für den späteren Einsatzbereich erzeugt.
- Die Hyperparameter des Priors müssen auf geeigneten Validierungsaufgaben gesetzt werden. Die Autoren tun das mit sechs separaten Validierungsdatensätzen, führen also nicht gar keine Modell-/Priorwahl durch.
- Beim PFN-BNN entsteht der synthetische Datensatz aus zufällig gewählten Netzarchitekturen und Gewichten sowie i.i.d. normalverteilten Eingaben. Das ist ein nützlicher kontrollierbarer Prior, aber nicht notwendigerweise eine realistische Beschreibung beliebiger tabellarischer Daten.

**Fundstelle:** Prior-Voraussetzung PDF S. 2, Z. 21–34; BNN-Datengenerierung S. 7, Z. 40–44 und S. 8, Z. 38–45; Validierungsdatensätze S. 8, Z. 52–55.

### Vortraining, Inferenz und Skalierung

- Die hohen Geschwindigkeitsfaktoren messen vor allem die schnelle **wiederverwendete** PFN-Inferenz gegenüber iterativen Verfahren oder pro-Datensatz abgestimmten Baselines. Die Vortrainingszeit und der Aufwand zur Auswahl des Priors sind getrennte Kosten, auch wenn das Vortrainingsmodell über viele Aufgaben amortisiert werden kann.
- Transformer werden mit einer festen Gesamtsequenzlänge \(N=n+m\) trainiert. Der Anhang beschreibt, wie verschiedene Kontext- und Abfragegrößen innerhalb dieses Budgets berücksichtigt werden; daraus folgt keine unbegrenzte Kontextlänge. **Fundstelle:** PDF S. 18, Z. 14–20.
- Größere Realweltprobleme werden von den Autoren ausdrücklich als offene Skalierungsrichtung bezeichnet. **Fundstelle:** PDF S. 10, Z. 5–9.
- Das Paper vergleicht einzelne Anwendungsfälle und Priors; die Geschwindigkeitsfaktoren (über 200×, 1.000×, 10.000×, über 5.000×) stammen aus unterschiedlichen Experimenten und Baselines. Sie dürfen nicht zu einer einzigen universellen Speedup-Aussage zusammengezogen werden.

### Vergleichs- und Interpretationsgrenzen

- **Vergleichsbudget nicht gleichartig:** Die PFN nutzt ein vortrainiertes Modell und bei Tabular-Daten einen einzigen Forward-Pass; klassische Baselines erhalten pro Evaluationsdatensatz Grid Search mit 5-fold CV. Das ist für den Anwendungsfall „viele Aufgaben mit gleichem Prior“ plausibel, aber kein Vergleich mit identischen Entwicklungs- und Rechenkosten. **Fundstelle:** PDF S. 8, Z. 56–63; S. 9, Z. 10–14.
- **Unterschiedliche Hardware-/Laufzeitbedingungen:** Die Tabellenzeiten nennen GPU-Zeiten für PFNs und baselinespezifische Aufwände, teils CPU-Zeiten in derselben Tabelle. Laufzeitfaktoren hängen daher vom konkreten Experiment und der Hardware ab und sind keine allgemeingültigen Benchmarks. **Fundstelle:** PDF S. 9, Z. 7–14.
- **Kleine Zahl an Evaluationseinheiten:** 20 Aufgaben, künstlich vereinfacht und pro Aufgabe 20 zufällige Teilmengen, sind informativ für den spezifischen Few-shot-Fall, aber keine vollständige Abdeckung realer Tabular-Domänen. **Fundstelle:** PDF S. 8, Z. 46–55.
- **Uneindeutige Zählung im Paper:** Der Methodentext nennt 20 Evaluationsdatensätze (S. 8, Z. 48–50; auch S. 9, Z. 13), während die Loss/Tie/Win-Zahlen in Tabelle 1 auf S. 9, Z. 4 jeweils zu 21 Fällen summieren und S. 8, Z. 68–69 von „21 evaluation datasets“ spricht. Die konkrete Zahl der unabhängigen Vergleichseinheiten ist im Haupttext somit nicht durchgehend konsistent. In dieser Notiz wird die explizite Datensatzliste (20 Einträge, Anhang S. 22, Z. 2–24) wiedergegeben und die Abweichung offengelegt.
- **Unsicherheitsmetriken nicht identisch mit Vorhersagegüte:** Niedriger ECE bedeutet bessere Kalibrierung in der verwendeten Metrik (100 Bins), nicht automatisch die beste Diskriminierung, beste Entscheidungsqualität oder universell korrekte Unsicherheit für Daten außerhalb des Priors. **Fundstelle:** PDF S. 9, Z. 15–19.

### Was man aus dem Paper nicht folgern sollte

1. Nicht: „PFN ist generell über 5.000-mal schneller als jedes Modell.“ Der Faktor bezieht sich auf das spezielle Tabular-Setup, auf vorausgesetztes PFN-Vortraining und auf die dort verglichenen Kosten.
2. Nicht: „PFN schlägt XGBoost auf großen Tabellendatensätzen.“ Die zentrale Tabular-Evaluation nutzt kleine binäre Teilaufgaben mit nur 30 gelabelten Beispielen zur Inferenz.
3. Nicht: „PFN braucht keinerlei Hyperparameterwahl.“ Die Evaluationsdatensätze brauchen keine eigene PFN-Optimierung, aber die Prior-Hyperparameter werden zuvor auf separaten Validierungsdatensätzen festgelegt.
4. Nicht: „Das Modell kann beliebige Daten ohne passende Vorannahmen korrekt bayessch behandeln.“ Das PFN approximiert die Posteriorvorhersage unter dem spezifizierten Trainingsprior; Prior-Mismatch bleibt relevant.
5. Nicht: „Die Arbeit verwendet SCMs als PFN-Prior.“ Die hier berichteten zentralen Priors sind GP-, BNN-Architektur-/Gewichts- und Linien-Priors.

## 5. Relevanz für meine Bachelorarbeit

### Wo die Quelle besonders nützlich ist

- **Kapitel 2 – Stand der Technik / TabPFN-Grundlagen:** zentrale Primärquelle zum ursprünglichen PFN-Prinzip und zur posterior-prädiktiven Inferenz im Forward-Pass.
- **Kapitel 3 – Methodik / synthetisches Vortraining:** erklärt, wie ein Prior über Aufgaben als synthetischer Datengenerator dient, wie Labels maskiert werden und wie die Prior-Data-NLL die Lernaufgabe bildet.
- **Kapitel 4 – Skalierungsansätze:** liefert eine frühe Demonstration der amortisierten Inferenz und einen sinnvollen Kontrast zwischen einmaligen Vortrainingskosten und sehr niedrigen Kosten pro neuer Aufgabe. Die explizite offene Skalierung auf größere Realweltprobleme ist für die Diskussion relevant.
- **Kapitel 5 – Evaluation und Limitationen:** nutzbar für den kleinen Few-shot-Tabular-Einsatz, Vergleiche mit XGBoost/CatBoost und Kalibrierung. Dabei stets die 30 Trainingslabels, binäre Aufgaben, Filter auf fehlende Werte/Featurezahl und die gewählte Priorfamilie nennen.
- **Diskussion zu Bayesian Learning:** zeigt, dass die Stärke der Methode nicht allein im Transformer liegt; die Kombination aus Priorwahl, synthetischer Task-Generierung, Set-Architektur und posterior-prädiktivem Ziel ist entscheidend.

### Mögliche Formulierung für die Bachelorarbeit (indirektes Zitat)

> Müller et al. schlagen Prior-Fitted Networks vor, die auf synthetischen Datensätzen aus einem spezifizierten Aufgabenprior trainiert werden und bei einer neuen Aufgabe deren posterior-prädiktive Verteilung in einem Forward-Pass approximieren. In ihrer Tabular-Evaluation erzielt die BNN-priorbasierte Variante auf kleinen, zu binärer Klassifikation vereinfachten OpenML-AutoML-Aufgaben starke ROC-AUC- und Kalibrierungsergebnisse; die Aussage ist jedoch an den verwendeten Prior und das Few-shot-Setting mit 30 gelabelten Beispielen gebunden. (Müller et al., 2022, S. 1–2, 8–9)

## 6. Wörtliches Schlüsselzitat

> “Presented with a set of samples from a new supervised learning task as input, PFNs make probabilistic predictions for arbitrary other data points in a single forward propagation, having learned to approximate Bayesian inference.”

**Fundstelle des wortgetreuen Zitats:** PDF S. 1, Z. 17–20, Abstract.

**Arbeitsübersetzung:** „Erhält ein PFN Beispiele aus einer neuen überwachten Lernaufgabe als Eingabe, erstellt es in einem einzigen Forward-Pass probabilistische Vorhersagen für beliebige weitere Datenpunkte und hat dabei gelernt, Bayes’sche Inferenz zu approximieren.“

Für ein direktes Zitat die englische Originalfassung verwenden und die Zitierweise der Hochschule beachten.

# Hollmann et al. (2023): *TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second*

## Quelle und Zitierhinweis

**Noah Hollmann, Samuel Müller, Katharina Eggensperger und Frank Hutter (2023).** *TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second.* ICLR 2023. Noah Hollmann und Samuel Müller sind als gleich beitragende Autoren gekennzeichnet. Die PDF enthält die Konferenzfassung sowie Anhang; die erste Seite zeigt zusätzlich arXiv:2207.01848v6 (16. September 2023).

- **PDF:** `literature/3_TabPFN_A.pdf`
- **Kernaussage:** Ein vortrainierter Transformer approximiert Bayes’sche Vorhersagen unter einem synthetischen Prior für Tabellendaten. Statt pro neuem Datensatz ein Modell zu trainieren und hyperzuoptimieren, verarbeitet TabPFN Trainingsbeispiele und Testpunkte gemeinsam in einem Forward-Pass.
- **Fundstellenformat:** Das Paper druckt keine Zeilennummern. Die Zeilenangaben hier zählen daher die aus der jeweiligen PDF-Seite extrahierten Textzeilen und sind Suchhilfen. Tabellen- und Abbildungszeilen können vom visuellen Layout abweichen; zur Kontrolle zuerst die angegebene PDF-Seite und den genannten Abschnitt aufsuchen.
- **Seitenangabe:** „PDF S.“ meint die physische PDF-Seite, insgesamt 37 Seiten. Haupttext: PDF S. 1–10; Anhang beginnt auf PDF S. 16.

## 1. Kernproblem

### Ausgangslage

Bei kleinen tabellarischen Klassifikationsproblemen dominieren häufig Gradient-Boosted Decision Trees (GBDTs). Deep-Learning-Verfahren sind trotz ihrer Stärke auf anderen Datentypen oft langsamer, erfordern Modelltraining und Hyperparameteroptimierung und liefern auf kleinen Datensätzen nicht zuverlässig bessere Ergebnisse. Die Autoren wollen die übliche pro-Datensatz-Modellierung durch ein bereits trainiertes Modell ersetzen, das direkt aus Beispielen Vorhersagen erzeugt. **Fundstelle:** PDF S. 1, Z. 29–44.

### Forschungsfrage

Kann ein Transformer, der offline auf synthetischen Tabellendatensätzen aus einem breit angelegten Aufgabenprior trainiert wurde, auf einem neuen kleinen Datensatz ohne erneutes Gradienten-Training oder datensatzspezifische Hyperparametersuche konkurrenzfähige Klassifikation liefern? **Fundstelle:** PDF S. 1, Z. 9–27, Abstract; PDF S. 2, Z. 8–23.

### Was wird vorhergesagt?

TabPFN approximiert die **posterior-prädiktive Verteilung** über Klassenlabels, bedingt auf die beobachteten Trainingsbeispiele. Das Verfahren integriert damit implizit über mögliche Daten-Generierungsmechanismen, gewichtet durch Prior und Likelihood, anstatt im Inferenzschritt eine einzelne optimale Hypothese oder einen einzelnen Klassifikator auszuwählen. **Fundstelle:** PDF S. 2, Z. 2–7 und Z. 29–43.

## 2. Methodischer Ansatz / Architektur

### PFN / In-Context Learning

TabPFN baut auf Prior-Data Fitted Networks (PFNs) auf:

1. Ein Prior beschreibt, wie plausible supervised Lernaufgaben bzw. tabellarische Datensätze generiert werden.
2. Offline werden viele synthetische Datensätze aus diesem Prior gezogen.
3. Der Transformer lernt, für zurückgehaltene Labels eine prädiktive Wahrscheinlichkeitsverteilung zu liefern, wenn er die übrigen beschrifteten Beispiele als Kontext sieht.
4. Online werden ein realer Trainingsdatensatz und dessen Testpunkte gemeinsam an den trainierten Transformer übergeben; der PFN gibt die Klassenverteilungen in einem Forward-Pass aus.

Der Inferenzschritt aktualisiert die Transformer-Parameter nicht per Gradient. Das Paper bezeichnet das als In-Context Learning. Das synthetische Prior-Fitting wird während der Algorithmenentwicklung einmalig durchgeführt und für die späteren Evaluationsdatensätze wiederverwendet. **Fundstelle:** PDF S. 1, Z. 34–44; PDF S. 3, Z. 17–30 und Z. 47–58.

### Architektur

- Der Transformer verarbeitet Featurevektoren und Labels als Tokens bzw. als Menge von Beispielen. Das Set-Design soll Invarianz gegenüber der Reihenfolge der Trainingsbeispiele ermöglichen.
- Trainingsbeispiele können aufeinander attendieren; Testbeispiele attendieren auf Trainingsbeispiele, nicht gegenseitig auf die anderen Testpunkte. Dadurch kann der Transformer für mehrere Testpunkte in einer gemeinsamen Auswertung Vorhersagen berechnen.
- Gegenüber dem PFN von Müller et al. (2022) werden Attention-Masken angepasst, um die Inferenz zu beschleunigen; unterschiedliche Featureanzahlen werden durch Zero-Padding behandelt.
- Die publizierte Version verwendet einen **12-Schichten-Transformer**.

**Fundstelle:** PDF S. 3, Z. 17–46 und Z. 47–53; Abb. 1 auf S. 3, Z. 17–20.

### Vortraining und Rechenaufwand

Das Modell wurde mit **18.000 Batches à 512 synthetisch generierten Datensätzen** trainiert. Das Vortraining dauerte laut Paper insgesamt **20 Stunden auf einer Maschine mit 8 Nvidia RTX 2080 Ti GPUs**. Dieses Modell wurde in allen Experimenten wiederverwendet; es ist also ein einmaliger Offline-Aufwand und nicht Teil der einzelnen TabPFN-Inferenzzeiten in derselben Weise wie das Training der Baselines. **Fundstelle:** PDF S. 3, Z. 47–53.

### Synthetischer Prior: SCMs, BNNs und Einfachheit

Der zentrale methodische Beitrag gegenüber den früheren PFNs ist ein eigens für Tabellendaten entworfener Prior, der zwei Generierungsfamilien mischt:

- **Structural Causal Models (SCMs):** Ein zufälliger gerichteter azyklischer Graph legt Abhängigkeiten zwischen latenten Knoten fest. Beobachtete Knoten werden als Features und Ziel ausgewählt. Geräuschvariablen werden gezogen, durch das Graphmodell propagiert und erzeugen korrelierte Features und Targets. Die Autoren verwenden eine breite Familie nichtlinearer Mechanismen und Rauschverteilungen.
- **Bayesian Neural Networks (BNNs):** Netzwerkarchitektur und Gewichte werden zufällig aus Prior-Verteilungen gezogen; damit erzeugen BNNs alternative synthetische Datenmechanismen.
- Während des PFN-Trainings werden SCM- und BNN-Datensätze mit gleicher Wahrscheinlichkeit ausgewählt.
- In beiden Familien wird **Einfachheit** bevorzugt: Graphen mit weniger Knoten bzw. BNNs mit weniger Parametern haben höheres Prior-Gewicht. Fast alle Hyperparameter werden als Verteilungen und nicht als einzelne feste Werte modelliert. Dadurch approximiert die PPD implizit eine Mischung über mögliche Mechanismen, Architekturen und Gewichte.

**Fundstelle:** PDF S. 1, Z. 45–48; S. 2, Z. 2–7; S. 4, Z. 30–59; SCM-Definition und Sampling S. 5, Z. 2–13 sowie Z. 33–48; Mischung mit BNN-Prior S. 5, Z. 49–52.

### Wichtige Abgrenzung: keine kausale Identifikation

Obwohl der Prior SCMs enthält und die Vorhersagen eine Präferenz für einfache kausale Erklärungen zeigen, rekonstruiert TabPFN im Inferenzschritt keinen kausalen Graphen und führt keine Interventionen oder Counterfactual-Inferenz durch. Es verwendet einen SCM-inspirierten Prior, um **assoziative Vorhersagen** auf Beobachtungsdaten zu erzeugen. Die Autoren ordnen dies als eine Art „rung 1.5“ ihrer Kausationsleiter ein, nicht als kausale Inferenz. **Fundstelle:** PDF S. 5, Z. 14–32.

### Mehrklassen- und Tabellendaten-Prior

Die SCM- und BNN-Generatoren erzeugen zunächst skalare Zielwerte für Regression. Für Klassifikation werden zufällige Klassengrenzen in diesen Zielwerten gewählt und die Abschnitte auf diskrete Klassen abgebildet. Danach werden Klassenlabels permutiert, damit keine künstliche Ordnung der Klassennummern bestehen bleibt. Das Modell kann so binäre und Mehrklassenprobleme sowie unterschiedliche Klassenungleichgewichte sehen. **Fundstelle:** PDF S. 4, Z. 34–39; PDF S. 6, Z. 25–36.

Der Anhang beschreibt weitere Anpassungen des Priors für korrelierte und kategoriale Features, exponentiell skalierte Daten und fehlende Werte. Dass solche Eigenschaften im synthetischen Prior prinzipiell vorkommen, bedeutet jedoch nicht, dass sie in den Hauptbenchmarks gleich gut abgedeckt oder gelöst sind. **Fundstelle:** PDF S. 4, Z. 36–39; Einschränkungen und reale Ergebnisse S. 9, Z. 4–15; S. 16, Z. 8–15.

### Testzeit-Ensembling

Die Autoren berichten sowohl einen einzelnen Forward-Pass als auch eine Ensemble-Variante mit **32 Forward-Pässen**. Für das Ensemble werden Trainingsdatensätze unterschiedlich permutiert bzw. transformiert; im beschriebenen Verfahren werden auch Feature-Spalten und Klassenlabels rotiert/permutiert. Das Ensemble kann genauer sein, benötigt aber mehr Inferenzzeit. Deshalb nicht alle berichteten Laufzeiten dem 32-Pass-Ensemble zuschreiben: Die besonders niedrigen Zeiten in der Haupttabelle beziehen sich auf „TabPFN n.e.“ (ohne dieses Ensembling). **Fundstelle:** PDF S. 3, Z. 54–58; PDF S. 4, Z. 28–29; Tabelle 1 und Bildunterschrift PDF S. 8, Z. 2–14.

## 3. Wichtigste Ergebnisse

### Hauptbenchmark: OpenML-CC18, numerische Features

- Die zentrale Hauptauswertung umfasst **18 kleine OpenML-CC18-Datensätze** mit ausschließlich numerischen Features und ohne fehlende Werte.
- Die Problemgröße ist auf höchstens **1.000 Trainingsbeispiele**, **100 numerische Features** und **10 Klassen** ausgelegt.
- Pro Datensatz und Verfahren werden fünf Wiederholungen mit unterschiedlichen Seeds und gemeinsamen Train-/Test-Splits (50 %/50 %) durchgeführt.
- Berichtet werden ROC-AUC One-vs-One (OVO), Accuracy und Cross-Entropy, jeweils aggregiert über Datensätze und Zeitbudgets. Die Baselines erhalten Budgets von 30, 60, 300, 900 oder 3.600 Sekunden; TabPFN wird auch ohne Testzeit-Ensembling ausgewertet.

**Fundstelle:** Abstract PDF S. 1, Z. 20–25; Evaluationsprotokoll PDF S. 8, Z. 30–36; Haupttabelle PDF S. 8, Z. 2–14.

### Baselines

Verglichen wird nicht nur mit einzelnen GBDTs, sondern auch mit AutoML-Systemen:

- **GBDTs:** LightGBM, CatBoost und XGBoost.
- **AutoML:** Auto-sklearn 2.0 und AutoGluon.
- **Weitere Verfahren:** logistische Regression, KNN, Gaussian Process, SAINT und Regularization Cocktails.
- Die Baselines erhalten unterschiedliche Laufzeitbudgets für Tuning, Training und Vorhersage. Auto-sklearn 2.0 nutzt Bayesian Optimization und kombiniert Modelle zu einem gewichteten Ensemble; AutoGluon kombiniert mehrere Modelltypen zu einem gestapelten Ensemble. Für die ausgewerteten Splits wählen die Autoren jeweils die nach ROC-AUC OVO beste Hyperparameterkonfiguration und fitten diese auf dem vollständigen Trainingssplit neu.

**Fundstelle:** PDF S. 8, Z. 15–29 (Baselinebeschreibung); Evaluationsprotokoll S. 8, Z. 30–36.

### Resultate auf den 18 numerischen CC18-Datensätzen

Bei 60 Minuten angefordertem Budget pro Split zeigt Tabelle 1 folgende über Datensätze gemittelte Werte:

| Verfahren | Mittlerer ROC-AUC-OVO | Mittlere Accuracy | Mittlere Cross-Entropy |
|---|---:|---:|---:|
| AutoGluon | 0,930 ± 0,0091 | 0,881 ± 0,010 | 0,714 ± 0,014 |
| TabPFN ohne Testzeit-Ensembling („n.e.“) | 0,932 ± 0,0088 | 0,873 ± 0,0095 | 0,727 ± 0,021 |
| TabPFN (Ensemble) | 0,934 ± 0,0086 | 0,879 ± 0,0089 | 0,716 ± 0,019 |
| TabPFN + AutoGluon | 0,934 ± 0,0084 | 0,886 ± 0,0094 | 0,711 ± 0,014 |

Die einzelnen Werte sind über Datensätze aggregiert; daraus folgt nicht, dass TabPFN jeden einzelnen Datensatz gewinnt. Der kombinierte TabPFN+AutoGluon-Eintrag ist ein Vorhersageensemble und erzielt in dieser Tabelle die besten Mittelwerte in Accuracy und Cross-Entropy; beim mittleren ROC-AUC liegt er praktisch gleichauf mit TabPFN allein. **Fundstelle:** Tabelle 1 PDF S. 8, Z. 2–14.

Die Autoren fassen zusammen: TabPFN liefert mit sehr kleinem Zeitbudget Resultate, die mit den stärksten AutoML-Verfahren bei wesentlich längerer Laufzeit konkurrieren, und übertrifft die getunten GBDT-Verfahren in der aggregierten Auswertung. **Fundstelle:** PDF S. 8, Z. 37–47; Abstract S. 1, Z. 20–25.

### Laufzeit: Speedup nur mit korrektem Kontext zitieren

- Für TabPFN ohne Testzeit-Ensembling nennt Tabelle 1 im Mittel etwa **1,30 s pro Datensatz auf CPU** bzw. **0,0519 s auf GPU**. Für die Variante mit Testzeit-Ensembling sind es etwa **37,59 s auf CPU** bzw. **0,6172 s auf GPU**. Das setzt voraus, dass das trainierte Modell bereits im GPU-Speicher liegt; das Laden benötigt laut Fußnote weitere etwa 0,2 s.
- Die Autoren berichten einen **230× CPU-** und **5.700× GPU-Speedup** gegenüber den stärksten Baselines bei fünf Minuten Laufzeitbudget, bei vergleichbarer Leistung. Diese Faktoren sind an genau diesen Vergleich und die verwendete Hardware gebunden.
- Die Laufzeiten der Baselines umfassen je nach Verfahren Tuning, Training und Vorhersage; TabPFN erledigt Inferenz in einem Forward-Pass und hat kein datensatzspezifisches Hyperparameter-Tuning.
- Im Fazit vergleichen die Autoren TabPFN-Vorhersagen von ungefähr 0,4 s mit AutoML-Laufzeiten von 5 bis 60 Minuten. Die genauen Zeiten unterscheiden sich nach Setup, Daten und Modellvariante; sie sind keine universellen Latenzgarantien.

**Fundstelle:** Tabelle 1 PDF S. 8, Z. 9–14; Geschwindigkeitsvergleich S. 8, Z. 45–55 und S. 9, Z. 2–3; Fazit S. 9, Z. 48–53.

### Zusätzliche Tests und offene Generalisierung

- Im Anhang werden auch **30 kleine OpenML-CC18-Datensätze** einschließlich kategorialer Merkmale und/oder fehlender Werte ausgewertet. TabPFN schneidet dort im Aggregat schwächer ab als im rein numerischen Teilbenchmark; die Leistung verbessert sich häufig mit der TabPFN+AutoGluon-Kombination. Die Tabelle enthält pro Datensatz sowohl Gewinne als auch Fälle, in denen TabPFN hinter Baselines liegt. **Fundstelle:** PDF S. 9, Z. 4–15; Anhang S. 16, Z. 44–53 und Tabelle 2 S. 18.
- Eine zusätzliche Prüfung testet bis zu **5.000 Trainingsbeispiele**, obwohl das Modell im synthetischen Vortraining nur Datensätze bis 1.024 Beispiele sah. Auf den untersuchten 18 Datensätzen zeigt TabPFN eine gewisse Generalisierung über die Trainingsgröße hinaus. Das ist ein ergänzender Test, ändert aber nicht die primäre Evaluationsgrenze von 1.000 Trainingsbeispielen und widerlegt nicht die quadratische Skalierung. **Fundstelle:** PDF S. 9, Z. 40–47.
- Im OpenML-AutoML-Benchmark berichten die Autoren für kleine Aufgaben im Mittel 4,4 Sekunden pro Datensatz auf einer CPU und bessere Mittelwerte als die dort verfügbaren Baselines mit 60-Minuten-Budget. **Fundstelle:** PDF S. 9, Z. 16–22.

### Weitere empirische Befunde

- **Nicht jeder Datensatz wird gewonnen:** TabPFN kann auch von einfachen Default-Baselines übertroffen werden. Die Leistung ist im Allgemeinen stärker bei rein numerischen Daten.
- **Ergänzung durch Ensembling:** TabPFN-Fehler sind weniger stark mit Fehlern der starken Baselines korreliert als deren Fehler untereinander. Ein Ensemble mit AutoGluon verbessert daher die aggregierten Resultate.
- **Robustheit gegenüber irrelevanten Merkmalen:** In den Zusatzexperimenten sind TabPFN und MLPs weniger robust gegenüber hinzugefügten uninformative Features als LightGBM. Die Autoren schlagen vor, solche Störmerkmale stärker im synthetischen Prior abzubilden.
- **Kategoriale Werte/Missingness:** Die Ergebnisse sind besser, wenn keine kategorialen Merkmale oder fehlenden Werte vorliegen; bei Binär- und Mehrklassenaufgaben scheint die relative Leistung vergleichbarer zu sein.

**Fundstelle:** PDF S. 9, Z. 4–15 und Z. 23–39; Anhang S. 16, Z. 44–49; Anhang S. 18, Z. 58–68.

## 4. Konkrete Limitierungen (besonders wichtig für die Diskussion)

### Von den Autoren explizit genannte Grenzen

- **Quadratische Skalierung:** Laufzeit und Speicher des verwendeten Transformer-PFN wachsen quadratisch mit der Zahl der Eingaben/Trainingsbeispiele. Sequenzen über 100.000 Eingaben sind auf damaligen Consumer-GPUs schwierig.
- **Begrenzte Feature- und Klassenanzahl:** Das konkret trainierte Modell ist auf höchstens 100 Features und 10 Klassen beschränkt; darüber kann genau diese TabPFN-Version nicht eingesetzt werden.
- **Kategoriale Daten und Missing Values:** Die Entwicklung konzentriert sich auf numerische Daten ohne fehlende Werte. Zwar können die Verfahren auf Daten mit Kategorien oder fehlenden Einträgen angewendet werden, die Leistung ist dort aber generell schwächer.
- **Uninformative Features:** Der synthetische Prior bildet viele irrelevante Features nicht hinreichend ab; das Hinzufügen solcher Features verschlechtert die Leistung.
- **Inferenzzeit ist nicht immer die schnellste reine Vorhersagezeit:** Baselines, die Training und Vorhersage trennen, können bei reiner Inferenz schneller sein. TabPFN führt Training und Vorhersage in einem gemeinsamen Schritt aus; sein Vorteil betrifft vor allem den Gesamtprozess inklusive Tuning/Training der Baselines.

**Fundstelle:** Anhang „Limitations“, PDF S. 16, Z. 2–18.

### Grenzen des Hauptbenchmarks

- Der Hauptbenchmark umfasst kleine Klassifikationsaufgaben: bis 1.000 Trainingsbeispiele, 100 numerische Features, höchstens 10 Klassen; der zentrale 18-Datensatz-Vergleich enthält keine Missing Values und nur numerische Features. **Fundstelle:** PDF S. 1, Z. 20–25; S. 10, Z. 2–7.
- Er evaluiert **Klassifikation**, nicht Regression. Regression und größere Aufgaben nennen die Autoren als zukünftige Erweiterungen. **Fundstelle:** PDF S. 10, Z. 8–10.
- Die primäre CC18-Auswertung wird nach Merkmalstyp gefiltert; sie ist daher nicht als uneingeschränkter Sieg auf der vollständigen OpenML-CC18-Suite zu beschreiben. Im Anhang werden weitere 30 kleine CC18-Datensätze samt Kategorien/Missingness separat betrachtet. **Fundstelle:** PDF S. 1, Z. 20–25; S. 9, Z. 7–10; Anhang S. 16, Z. 50–53.
- Die Laufzeitangaben berücksichtigen keine vollständigen Entwicklungs- bzw. Modellierungskosten. Die Autoren sagen ausdrücklich, dass sie Entwicklungskosten der einzelnen Methoden aus dem Vergleich ausklammern. **Fundstelle:** PDF S. 9, Z. 2–3.
- Der Vergleich der Gesamtpipeline begünstigt die amortisierte PFN-Inferenz, wenn das gleiche vortrainierte Modell auf viele neue Datensätze angewendet wird. Für eine einzelne neue Domäne muss der Offline-Aufwand – 20 Stunden auf 8 GPUs – ebenfalls berichtet werden. **Fundstelle:** PDF S. 3, Z. 47–53.

### Zusätzliche Vorsicht bei der Interpretation

- **Speedup bezieht sich auf ein bestimmtes Messsetup:** „230×“ bzw. „5.700×“ ist ein Vergleich mit den stärksten Baselines bei einem fünfminütigen Budget, nicht die Aussage, TabPFN sei für jede Hardware, jedes Datenvolumen oder jede Vorhersagephase pauschal so viel schneller.
- **Kein Sieg auf jedem Datensatz:** Die Autoren betonen dies ausdrücklich und nennen sogar Datensätze, auf denen Default-Baselines TabPFN übertreffen. Aggregierte Mittelwerte und Ränge verstecken diese Heterogenität. **Fundstelle:** PDF S. 9, Z. 4–15.
- **Prior-Mismatch bleibt zentral:** Das Modell approximiert Bayes’sche Vorhersagen unter dem synthetischen Prior. Wenn die reale Datengenerierung stark von den SCM-/BNN-Priorannahmen abweicht, ist aus der PFN-Idee allein keine gute Leistung garantiert. Die Autoren beschreiben die Priorwahl selbst als entscheidend. **Fundstelle:** PDF S. 4, Z. 30–39.
- **„Kausal“ bedeutet hier keine Intervention:** Die SCMs kodieren einen Bias des Priors, nicht die Identifikation wahrer Kausalgraphen aus Beobachtungsdaten. Für Aussagen über Interventionen oder Kausalbeziehungen reicht dieses Paper nicht. **Fundstelle:** PDF S. 5, Z. 14–32; mögliche künftige Interventions-/Counterfactual-Arbeit S. 10, Z. 15–16.
- **Bestimmte Anzahl zusätzlicher OpenML-Datensätze ist im Paper nicht konsistent berichtet:** Der Abstract erwähnt 67 zusätzliche kleine numerische OpenML-Datensätze, während der Haupttext 149 zusätzliche Validierungsdatensätze plus 30 Testdatensätze (179 insgesamt) nennt. Diese Angaben sollte man nicht ohne Erläuterung zu einer einzigen Zahl zusammenziehen. **Fundstelle:** Abstract PDF S. 1, Z. 24–26; PDF S. 9, Z. 9–12.
- **Kontextlänge / Generalisierung:** Der Transformer kann laut Architektur variable Inputlängen akzeptieren, wurde im synthetischen Prior-Fitting jedoch auf höchstens 1.024 Beispiele trainiert. Der Test bis 5.000 ist ein positives, begrenztes Generalisierungsergebnis, nicht der Nachweis, dass beliebige Größen effizient oder stabil funktionieren. **Fundstelle:** PDF S. 9, Z. 40–47.

### Was man aus dem Paper nicht folgern sollte

1. Nicht: „TabPFN schlägt alle AutoML-Verfahren auf allen tabellarischen Datensätzen.“ Der Befund ist aggregiert und gilt für kleine Aufgaben mit spezifischen Feature-/Klassenlimits; es gibt individuelle Verluste.
2. Nicht: „TabPFN wurde uneingeschränkt auf OpenML-CC18 getestet und gewinnt dort.“ Die Hauptauswertung nutzt 18 gefilterte rein numerische CC18-Datensätze; weitere 30 kleine CC18-Datensätze inklusive Kategorien/Missing Values sind eine separate Anhangsauswertung.
3. Nicht: „TabPFN ist 5.700-mal schneller, egal welche Kosten man betrachtet.“ Das ist ein spezifischer Speedup gegenüber Baselines im gegebenen Zeitbudget, bei bereits vortrainiertem Modell und bestimmter GPU-Hardware.
4. Nicht: „Das Modell erkennt Kausalität.“ Es nutzt SCMs als Prior und liefert beobachtungsbasierte Vorhersagen, nicht kausale Identifikation.
5. Nicht: „Es gibt keinerlei Hyperparameter- oder Entwicklungsaufwand.“ Pro Evaluationsdatensatz wird kein PFN-Tuning gemacht, aber die Priorfamilie, das Offline-Training und die Modellkonfiguration müssen zuvor entwickelt und trainiert werden.

## 5. Relevanz für meine Bachelorarbeit

### Geeignete Kapitel

- **Kapitel 2 – Stand der Technik:** Primärquelle zur ersten TabPFN-Version und zur Übertragung des PFN-Prinzips auf kleine tabellarische Klassifikation.
- **Kapitel 3 – Methodik / synthetische Priors:** besonders relevant für SCM-/BNN-Prior, Einfachheitsbias, synthetische Aufgaben und probabilistische In-Context-Vorhersage.
- **Kapitel 4 – Skalierungsansätze:** geeignet als Ausgangspunkt für den Geschwindigkeitsvorteil durch amortisierte Inferenz sowie als klares Beispiel der quadratischen Attention-/Speichergrenze.
- **Kapitel 5 – Evaluation / Vergleich:** die 18 OpenML-CC18-Datensätze, Zeitbudgets und Baselines können als Vergleichsrahmen dienen; die Einschränkungen (numerisch, klein, ohne Missing Values) müssen aber im Text mitgenannt werden.
- **Diskussion:** besonders wertvoll für Limitierungen durch uninformative Features, kategoriale Merkmale, fehlende Werte, Klassen-/Feature-Limits und Prior-Mismatch.
- **Abgrenzung zu späteren TabPFN-Versionen:** Diese Arbeit beschreibt den Stand von ICLR 2023. Nicht auf spätere TabPFN-Versionen übertragene Verbesserungen oder deren Skalierungsgrenzen dieser ursprünglichen Arbeit zuschreiben.

### Mögliche Formulierung für die Bachelorarbeit (indirektes Zitat)

> Hollmann et al. trainieren TabPFN offline auf synthetischen Klassifikationsaufgaben aus einer Mischung von SCM- und BNN-Priors und approximieren die posterior-prädiktive Verteilung eines neuen Datensatzes anschließend ohne datensatzspezifisches Gradienten-Training. Auf kleinen, rein numerischen OpenML-CC18-Aufgaben erreicht das Verfahren konkurrenzfähige Resultate gegenüber GBDT- und AutoML-Baselines bei deutlich geringerer Inferenz- und Tuningzeit. Die Aussage ist durch den kleinen Aufgabenbereich, die Abhängigkeit vom verwendeten Prior und die quadratische Skalierung des Transformers begrenzt. (Hollmann et al., 2023, S. 1–3, 8–10, 16)

## 6. Wörtliches Schlüsselzitat

> “TabPFN performs in-context learning (ICL), it learns to make predictions using sequences of labeled examples (x, f(x)) given in the input, without requiring further parameter updates.”

**Fundstelle:** PDF S. 1, Z. 11–14, Abstract.

**Arbeitsübersetzung:** „TabPFN führt In-Context Learning aus: Es lernt, Vorhersagen anhand von Sequenzen gelabelter Beispiele \((x,f(x))\) in der Eingabe zu erstellen, ohne weitere Parameteraktualisierungen zu benötigen.“

Für ein direktes Zitat die englische Originalfassung übernehmen und den Zitierstil der Hochschule beachten. Für die Einordnung im Fließtext ergänzen, dass dies den Inferenzschritt nach dem Offline-Vortraining beschreibt.

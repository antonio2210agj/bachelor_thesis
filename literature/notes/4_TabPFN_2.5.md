# Prior Labs Team (2025/2026): *TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models*

## Quelle und Zitierhinweis

**Prior Labs Team.** *TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models.* Technischer Report. Das Deckblatt datiert den Report auf **6. November 2025**; in der PDF-Kopfzeile steht **arXiv:2511.08667v2 vom 5. Februar 2026**. Die Quelle nennt „Prior Labs Team“ als Autor und verweist für die vollständige Beitragsliste auf den Anhang.

- **PDF:** `literature/4_TabPFN_2.5.pdf`
- **Thema:** nächste TabPFN-Generation für größere tabellarische Aufgaben; Ausbau der Modellarchitektur, neue bzw. breitere synthetische Priors, Skalierung, Distillation zu MLP-/Baum-Ensembles und Evaluation auf öffentlichen sowie internen Benchmarks.
- **Fundstellenformat:** Das Dokument druckt keine Zeilennummern. Die Zeilenangaben in dieser Notiz zählen den extrahierten PDF-Text und sind Suchhilfen. Für Tabellen und Abbildungen zusätzlich Titel und Seite beachten, weil Extraktion und visuelle Anordnung auseinanderfallen können.
- **Seitenzählung:** „PDF S.“ bezeichnet die physische PDF-Seite (35 Seiten). Der Haupttext liegt auf S. 1–11; der Anhang beginnt danach.
- **Quellenkritischer Hinweis:** Es handelt sich um einen vom Entwicklerteam verfassten technischen Bericht und nicht um eine unabhängige externe Evaluation. Ergebnisse aus internen/proprietären Benchmarks sind nicht vollständig nachprüfbar, solange die zugrunde liegenden Daten und Auswertungen nicht öffentlich verfügbar sind.

## 1. Kernproblem

### Ausgangslage

TabPFN v1 zeigte, dass ein auf synthetischen Aufgaben vortrainierter Transformer kleine Klassifikationsprobleme in einem Forward-Pass lösen kann; TabPFNv2 erweiterte das in Richtung realweltlicher, heterogener Daten. TabPFN-2.5 adressiert die verbleibenden Grenzen: begrenzte Daten- und Featuregrößen, Inferenzlatenz sowie den Bedarf nach breiterer Leistung über Klassifikation und Regression hinweg. Die Autoren wollen die amortisierte In-Context-Inferenz auf Datensätze bis zur Größenordnung von 50.000 Zeilen und 2.000 Features ausdehnen. **Fundstelle:** PDF S. 1, Z. 5–19; S. 2, Z. 13–29.

### Forschungsfragen / Beiträge

1. Lässt sich die Leistungsfähigkeit von TabPFN auf wesentlich größere Datensätze und mehr Features ausweiten?
2. Wie schneidet TabPFN-2.5 auf einem aktuellen, breiten öffentlichen Tabellendatenbenchmark gegen GBDTs, tabellenspezifische Deep-Learning-Verfahren und andere Tabular Foundation Models ab?
3. Kann man die Inferenz weiter beschleunigen, indem TabPFN-2.5 seine Vorhersagen in ein klassisches MLP oder ein Baum-Ensemble destilliert?
4. Verbessert das stärkere Basismodell auch Anwendungen der kausalen Inferenz, insbesondere die Schätzung heterogener Behandlungseffekte?

**Fundstelle:** PDF S. 2, Z. 18–34; experimentelle Übersicht S. 6, Z. 1–5.

### Was ist die zentrale Idee?

TabPFN-2.5 bleibt ein PFN-/Tabular-Foundation-Modell: Es wird vorab auf synthetischen tabellarischen Aufgaben trainiert und verwendet anschließend In-Context Learning, statt für jeden Anwendungsdatensatz ein klassisches Modell per Gradientenabstieg neu zu fitten. Der Rechenaufwand wird dadurch nicht eliminiert, sondern teilweise in ein wiederverwendbares Vortraining und einen bei der Inferenz weiterhin erheblichen Transformer-Forward-Pass verlagert. **Fundstelle:** PDF S. 2, Z. 8–12; S. 3, Z. 17–30.

## 2. Methodischer Ansatz / Architektur

### Synthetisches Vortraining und Real-TabPFN-2.5

- Das Standardmodell TabPFN-2.5 wird laut Report **ausschließlich auf synthetisch erzeugten Daten** trainiert. Diese Daten werden aus einem tabellarischen Prior gezogen, dessen Verteilungen gegenüber früheren Versionen verbreitert und für größere Aufgaben ausgelegt wurden.
- Zusätzlich stellen die Autoren **Real-TabPFN-2.5** vor: eine separat auf realen Daten feinabgestimmte Variante.
- Für dieses Fine-Tuning wurde ein kuratierter Korpus aus **43 realen Datensätzen** von OpenML und Kaggle verwendet. Die Daten wurden gegen interne Benchmarks und TabArena dedupliziert, um Überschneidungen oder Ableitungen der Evaluationstests zu vermeiden.
- Real-TabPFN-2.5 ist somit nicht mit dem rein synthetisch trainierten Standard-TabPFN gleichzusetzen; Resultate der beiden Varianten müssen getrennt benannt werden.

**Fundstelle:** PDF S. 4, Z. 8–17; Deduplizierung näher beschrieben im Anhang S. 28, Z. 23–28.

### Prior / synthetische Aufgabengenerierung

Das Paper baut auf den tabellarischen Priorideen der vorherigen TabPFN-Arbeiten auf. Für TabPFNv2 wird in diesem Report ausdrücklich ein synthetischer Prior mit **Structural Causal Models (SCMs)** und **Bayesian Neural Networks (BNNs)** als Generatorfamilien genannt. TabPFN-2.5 verbreitert die synthetischen Verteilungen und skaliert die Aufgaben. Bei den meisten Hyperparametern werden Verteilungen statt fester Punktwerte verwendet; unterschiedliche Graph-/Netzwerkstrukturen und Mechanismen tragen zur Vielfalt des Priors bei.

Die SCM-Komponente kodiert eine Präferenz für einfache, kausal interpretierbare Mechanismen. Das heißt nicht, dass TabPFN-2.5 im normalen Vorhersageschritt einen wahren Kausalgraphen identifiziert oder aus Beobachtungsdaten Interventionseffekte ableitet. Die Autoren behandeln kausale Schätzung als separate Anwendung und nennen explizite Interventions-/Strukturmodellierung als Zukunftsrichtung.

**Fundstelle:** PDF S. 2, Z. 13–17; S. 4, Z. 11–17; Hintergrund zur Priorwahl in den referenzierten Vorarbeiten. Die Abgrenzung für die vorliegende kausale Auswertung steht auf S. 9, Z. 53–58.

### Architekturänderungen gegenüber TabPFNv2

- TabPFN-2.5 behält die **alternierende Attention über Datenzeilen und Features** aus TabPFNv2 bei.
- Klassifikationsmodell: **24 Schichten**; Regressionsmodell: **18 Schichten** (gegenüber 12 Schichten bei TabPFNv2).
- Die Feature-Gruppengröße wird von 2 auf **3 Features** erhöht; laut Autoren beschleunigt das Training und Inferenz.
- Für Regression ersetzt ein zweischichtiges MLP den linearen Feature-Encoder.
- TabPFN-2.5 erhält **64 gelernte „thinking rows“** als zusätzliche Eingaben, die Rechenkapazität bereitstellen und als Attention Sinks dienen können.
- Weitere Komponenten aus TabPFNv2 bleiben erhalten, darunter Dual-Attention, Trennung/Caching des Trainings- und Testkontexts sowie Positions-Embeddings für Features.

**Fundstelle:** PDF S. 4, Z. 18–32; Modellübersicht in Tabelle 1 auf S. 5, Z. 34–41.

### Preprocessing und Robustheit

Vorhersagen werden über mehrere Permutationen der Daten und Feature-Transformationen aggregiert. Gegenüber früher werden robuste Skalierung und Soft-Clipping mit Quantil- und Standardisierungstransformationen kombiniert. Bei einem Teil der Estimatoren werden SVD-Komponenten als zusätzliche Merkmale ergänzt, um globale Varianzrichtungen einzubringen. Ziel ist, Ausreißer und unterschiedliche Featureverteilungen robuster zu behandeln sowie Vielfalt im Ensemble zu schaffen. **Fundstelle:** PDF S. 4, Z. 33–40.

### Modell- und Hyperparameterwahl

Die Autoren stimmen TabPFN-2.5 unter anderem mit einem „TabPFN tunes TabPFN“-Ansatz ab:

1. Zunächst werden 100 Modellkonfigurationen auf einer breiten, aber dünnen Auswahl plausibler Hyperparameterkombinationen trainiert und auf einem kuratierten internen Validierungssatz bewertet.
2. Da ungefähr 50 Hyperparameter mit nur 100 Beobachtungen nicht zuverlässig direkt interpolierbar sind, wird TabPFNv2 als Surrogatmodell verwendet.
3. Dieses Surrogat sagt die Leistung für ein dichteres Raster aus 10.000 Konfigurationen voraus, aus denen vielversprechende Kandidaten für teure vollständige Trainingsläufe ausgewählt werden.

Für benutzerdefinierte Metriken kann ein Entscheidungsschwellenwert für Kennzahlen wie F1 abgestimmt werden; für Mehrklassenklassifikation ist Temperature Scaling der Softmax-Ausgaben möglich. Die berichteten Standardwerte sind, sofern nicht anders vermerkt, **ohne** Schwellenwert-Tuning und **ohne** Temperature Scaling. **Fundstelle:** PDF S. 5, Z. 1–19.

### Distillation zu MLP oder Baum-Ensemble

Der proprietäre Distillation-Engine erhält einen Trainingsdatensatz und erzeugt ein datensatzspezifisches Modell:

- **TabPFN-2.5-as-MLP** oder
- **TabPFN-2.5-as-TreeEns**.

Diese Modelle sollen nahe an der TabPFN-Leistung bleiben, bei der Vorhersage aber niedrigere Latenz und geringeren Speicherbedarf haben. Im Gegensatz zum allgemeinen TabPFN führen sie beim Einsatz kein In-Context Learning durch: Sie sind an den jeweiligen Datensatz angepasst und nehmen einzelne Datenpunkte als Eingabe. Das Verfahren ist eine Distillation/Kompression für Deployment, keine gleichartige Foundation-Model-Inferenz. **Fundstelle:** PDF S. 5, Z. 25–33; Evaluierung auf S. 7, Z. 58–65.

## 3. Wichtigste Ergebnisse

### Öffentlicher Benchmark: TabArena-Lite

- TabArena basiert laut Report auf einer Auswahl von **51 Datensätzen aus 1.053 Kandidaten**.
- Verwendet wird „TabArena-Lite“, eine günstigere, als repräsentativ bezeichnete Version mit **einem Test-Fold**.
- Das Paper betrachtet einen kleinen/mittelgroßen Teilbereich bis **10.000 Trainingszeilen und 500 Features** sowie eine breitere Auswertung bis **100.000 Zeilen und 2.000 Features**.
- Baselines umfassen GBDTs (CatBoost, LightGBM, XGBoost), weitere tabellenspezifische Verfahren (u. a. RealMLP, TabM, ModernNCA, xRFM) und Foundation-Modelle (u. a. TabICL, TabDPT, LimiX, Mitra, TabPFNv2).

**Fundstelle:** PDF S. 6, Z. 6–16; kleine TabArena-Lite-Auswertung S. 6, Z. 17–24 und Bildunterschrift S. 7, Z. 43–46; größere Auswertung S. 6, Z. 25–36 und Bildunterschrift S. 8, Z. 44–49.

### Ergebnisse auf TabArena

- **Bis 10k Zeilen / 500 Features:** Die Autoren berichten, dass TabPFN-2.5 im Forward-Pass eine starke Leistung über die verglichenen Methoden erreicht. Bei Klassifikation übertrifft die Standardvariante laut Bericht AutoGluon 1.4 im „extreme mode“, das vier Stunden abgestimmt wurde und Modelle einschließlich TabPFNv2 ensembelt.
- **Regression reagiert stärker auf Tuning:** Das Regressionsmodell profitiert laut Autoren stärker von zusätzlicher Abstimmung und übertrifft AutoGluon 1.4 nach 60 TabPFN-Konfigurationen.
- **Bis 100k Zeilen / 2k Features:** TabPFN-2.5 wird als bester Default in der aggregierten TabArena-Auswertung berichtet. Getunt übertrifft es AutoGluon 1.4 bei Regression und nähert sich ihm bei Klassifikation. Für Real-TabPFN-2.5 berichten die Autoren besonders starke Klassifikationsresultate, auch im Forward-Pass.
- **Gegen TabPFNv2:** Die Default-Leistung von TabPFN-2.5 sei auf fast allen kompatiblen TabArena-Datensätzen besser und nur selten deutlich schlechter.

**Fundstelle:** PDF S. 6, Z. 17–36; Abb. 2 auf S. 5, Z. 54–61; Abb. 3 auf S. 7, Z. 43–48; Abb. 4 auf S. 8, Z. 44–49.

**Wichtige Einordnung:** Diese Resultate sind in den Abbildungen primär als Elo-/Rang- und paarweise Gewinnraten dargestellt. Der Bericht gibt an diesen Stellen keine allgemein gültige absolute Prozentverbesserung der Accuracy oder des ROC-AUC gegenüber jedem Konkurrenten an. Die Worte „outperforms“ und „leading“ beziehen sich auf die jeweilige aggregierte Benchmark-Auswertung.

### Angaben zu XGBoost-Gewinnraten

Das Deckblatt nennt für TabPFN-2.5 im Default-Modus:

- **100 % Win Rate** gegenüber Default-XGBoost auf kleinen bis mittelgroßen Klassifikationsaufgaben (bis 10.000 Datenpunkte und 500 Features);
- **87 %** auf größeren Datensätzen bis 100.000 Samples und 2.000 Features;
- **85 %** für Regression in der größeren Größenklasse.

Das sind vom Autorenteam berichtete Benchmark-Win-Rates; sie bedeuten nicht, dass TabPFN jeden Datensatz gewinnt oder in der angegebenen Prozenthöhe bessere Scores erzielt. Ein „Win“ beschreibt die Zahl der Benchmarkvergleiche mit besserem Resultat, nicht eine relative Zunahme der Metrik um diesen Prozentsatz. **Fundstelle:** PDF S. 1, Z. 8–19.

### Interne Benchmarks (nicht öffentlich)

- Das interne Framework enthält **mehr als 100 Anwendungsfälle** aus Healthcare, Finance, Insurance, Retail und Manufacturing.
- Verglichen werden XGBoost, CatBoost und LightGBM in Default- und getunter Version; die GBDT-Baselines erhalten jeweils eine Stunde Random Search.
- TabPFN wird über das interne AutoTabPFN-System abgestimmt und als getuntes Ensemble berichtet.
- Abbildung 5/6 beschreibt Klassifikations- und Regressionsdatensätze bis 50.000 Zeilen und **500 Features**; der Text unmittelbar davor spricht zugleich von bis zu 50.000 Samples und **2.000 Features**. Der Report nennt außerdem in der Zusammenfassung interne Ergebnisse bis 50k × 2k.

**Fundstelle:** PDF S. 6, Z. 37–49; der Featurebereich der Abbildungen ist aus den Diagrammbeschriftungen auf S. 8 ersichtlich. Die voneinander abweichenden Obergrenzen werden daher nicht stillschweigend vereinheitlicht.

Da diese Daten proprietär sind, sollten die internen Resultate getrennt von TabArena und mit dem Hinweis „interner, nicht öffentlich prüfbarer Benchmark“ berichtet werden. **Fundstelle:** PDF S. 6, Z. 38–45.

### Inferenzgeschwindigkeit und Skalierung

- Gegenüber TabPFNv2 sei TabPFN-2.5 trotz größerer Architektur je nach Setup **1× bis 2,3× schneller**, was die Autoren optimiertem Preprocessing und größeren Featuregruppen zuschreiben. **Fundstelle:** PDF S. 5, Z. 20–24.
- Die gemessene Zeit umfasst bei den Skalierungsexperimenten sowohl die Verarbeitung der Trainingszeilen (entspricht näherungsweise dem Modell-Fit klassischer Verfahren) als auch die Vorhersage auf Testzeilen. Es handelt sich also um die vollständige In-Context-Latenz, nicht nur um einen isolierten `predict`-Aufruf nach vorherigem Fit. **Fundstelle:** PDF S. 7, Z. 49–57.
- Bei \(r\) Zeilen und \(c\) Features gibt der Bericht die erwartete Skalierung als
  \[
  O\!\left(r^2\min(c,500)+r\min(c,500)^2\right)
  \]
  an. Die zweite Dimension ist pro Estimator durch Feature-Subsampling auf 500 begrenzt. Das vermindert den Featurekostenanteil, beseitigt aber die quadratische Abhängigkeit von der Zeilenzahl nicht. **Fundstelle:** PDF S. 7, Z. 50–57.
- Auf dem internen H100-Skalierungstest werden Latenzen für 1 bzw. 4 GPUs bis 50.000 Zeilen gezeigt; die Abbildung misst die Laufzeit einschließlich Fit/Inference bei 500 Testzeilen. **Fundstelle:** PDF S. 9, Z. 21–48.
- Für große Aufgaben empfehlen die Autoren dedizierte GPUs (NVIDIA H100/A100) und mehrere GPUs. CPU, integrierte GPUs und Apple MPS werden zwar unterstützt, aber nur für kleine Datensätze empfohlen. **Fundstelle:** PDF S. 9, Z. 59–68.

**Keine pauschale Beschleunigungszahl gegenüber AutoGluon/XGBoost:** Der Report berichtet keine universelle Speedup-Zahl, die für alle Datensatzgrößen und Geräte gilt. Die klar quantifizierte 1–2,3×-Aussage bezieht sich auf TabPFNv2, nicht auf GBDT oder AutoML. Die Vergleiche mit AutoGluon stellen primär Performance unter unterschiedlichen Budgets gegenüber.

### Distillation-Ergebnisse

Auf internen/open-source Datensätzen bis 10k Datenpunkten berichten die Autoren, dass TabPFN-2.5-as-MLP und TabPFN-2.5-as-TreeEns konkurrenzfähige Genauigkeit gegenüber TabPFN und getunten LightGBM-, XGBoost- und CatBoost-Modellen bei geringerer Vorhersagekosten bieten. Die konkrete Distillation-Engine ist proprietär; der Bericht liefert keine umfassende unabhängige Reproduzierbarkeit der erzeugten Modelle. **Fundstelle:** PDF S. 7, Z. 58–65; Abb. 7 auf S. 9, Z. 17–20.

### Kausale Inferenz

Die Autoren evaluieren PFN-basierte CATE-Schätzer auf **RealCause**, einem semi-synthetischen Benchmark, der reale RCT-Daten nutzt und beobachtbare Confounding-Effekte synthetisch erzeugt. Metrik ist PEHE (Root Mean Squared Error zwischen geschätztem und Ground-Truth-CATE). Der Bericht sagt, PFN-basierte Schätzer belegten die ersten sieben Plätze; TabPFN-2.5 als T-Learner erreicht laut Text die stärkste Gesamtleistung. Der Bericht weist selbst darauf hin, dass die Wahl von Propensity- und Outcome-Modell wichtig ist und dass latente Confounder in realen Anwendungen eine offene Schwierigkeit sind. **Fundstelle:** PDF S. 7, Z. 66–75; S. 9, Z. 49–58; Datensatzbeschreibung S. 30, Z. 1–5.

## 4. Konkrete Limitierungen (besonders wichtig für die Diskussion)

### Skalierung, Speicher und Laufzeit

- **Quadratische Zeilenskalierung bleibt bestehen:** Die Architektur ist im Zeilenumfang weiterhin quadratisch; größere Datensätze erhöhen Laufzeit und Speicher stark. Die Autoren nennen Millionen Zeilen als nächsten Skalierungsschritt und erklären, dafür noch neue Ansätze entwickeln zu müssen. **Fundstelle:** PDF S. 7, Z. 49–57; Fazit S. 11, Z. 14–17.
- **Empfohlene Obergrenze ist nicht gleich validierte Maximalgröße:** 50.000 × 2.000 ist der vorgesehene Bereich; der Report zeigt Benchmarks bis 100.000 × 2.000. Explorative Läufe bis etwa 160k × 500 für Klassifikation und 85k × 500 für Regression passen laut Fußnote auf eine H100 mit 80 GB und FP16/FlashAttention-3, sind aber ausdrücklich außerhalb des validierten Bereichs und nicht Teil der berichteten Benchmarks. **Fundstelle:** PDF S. 2, Z. 47–49; S. 5, Z. 34–41; S. 11, Z. 14–17.
- **GPU-Abhängigkeit bei größeren Daten:** Für größere Aufgaben empfiehlt das Team H100/A100 und parallele Inferenz auf mehreren GPUs. CPU und kleinere Geräte eignen sich laut Report primär für kleine Datensätze. **Fundstelle:** PDF S. 9, Z. 59–68.
- **Fitted-model cache ist speicherintensiv:** Der experimentelle Cache verwendet für Klassifikation ca. 6,1 KB GPU-Speicher und 48,8 KB CPU-Speicher pro Zelle im Trainingsdatensatz (Regression laut Report ca. 25 % weniger). Er ist daher derzeit nur für kleine Trainingsdatensätze geeignet. **Fundstelle:** PDF S. 10, Z. 17–23.
- **Batch-Inferenz nötig, wenn Speicher knapp ist:** Ohne Cache wird beim erneuten `predict()` laut Anleitung erneut fit-/verarbeitungsähnliche Arbeit ausgeführt. Testpunkte sollten möglichst in einem Aufruf oder bei Speicherproblemen in Batches von 1.000–10.000 verarbeitet werden. **Fundstelle:** PDF S. 10, Z. 11–14.

### Benchmark- und Generalisierungsgrenzen

- **Öffentlicher Benchmark mit nur einem Test-Fold:** TabArena-Lite reduziert die Kosten, verwendet aber nur einen Test-Fold. Das macht den Vergleich günstiger, erfasst jedoch nicht dieselbe Split-Variabilität wie eine Evaluation mit vielen Splits. **Fundstelle:** PDF S. 6, Z. 13–16.
- **Einschränkungen bei TabArena-Kompatibilität:** Vergleiche mit TabICL, LimiX und anderen Foundation Models werden jeweils auf die Datensätze beschränkt, mit denen die betreffenden Modelle kompatibel sind. Die jeweiligen Ranglisten haben deshalb nicht immer dieselbe Datensatzbasis. **Fundstelle:** PDF S. 6, Z. 30–36; Anhang S. 30, Z. 18–26.
- **Unterschiedliche Tuningbudgets:** TabPFN-2.5 wird in den TabArena-Abbildungen mit 60 zufälligen Konfigurationen getunt, Baselines mit bis zu 200; außerdem haben Baselines teils ein Vier-Stunden-Budget. Beim Vergleich „Default“ und „tuned+ensembled“ sind dies daher nicht identische Suchkosten. **Fundstelle:** PDF S. 7, Z. 43–46; S. 8, Z. 44–49.
- **Interne Daten nicht unabhängig verifizierbar:** Die über 100 internen Anwendungsfälle sind proprietär. Ihre Abdeckung klingt breit, aber externe Forschende können den Benchmark und die Resultate aus dem PDF allein nicht vollständig reproduzieren. **Fundstelle:** PDF S. 6, Z. 38–45.
- **Bericht des Entwicklerteams:** Die Ergebnisse stammen vom Modellanbieter. Die im PDF genannten Top-Ränge und Win Rates sollten deshalb als Autorenergebnisse, nicht als unabhängige Bestätigung, gekennzeichnet werden.
- **Keine universelle Dominanz:** Die Auswertung ist aggregiert, und die Begriffe „best“ oder „outperforms“ beziehen sich auf die jeweilige Auswahl, Metrik und Konfiguration. Die Deckblatt-Win-Rates bedeuten nicht, dass TabPFN-2.5 alle Aufgaben oder jede einzelne Split-Auswertung gewinnt. **Fundstelle:** PDF S. 1, Z. 14–16; öffentliche aggregierte Ergebnisse S. 6–8.

### Grenzen der Real-TabPFN-Variante

- Real-TabPFN-2.5 wird auf 43 realen Datensätzen feinabgestimmt. Deduplizierung gegen TabArena und interne Tests wird beschrieben, was wichtig ist, aber nicht alle möglichen Formen von Verteilungsnähe oder Informationsleckage ausschließt.
- Die bessere Performance dieser Variante darf nicht als Ergebnis des rein synthetischen Standardmodells dargestellt werden.
- Die Datenquellen OpenML und Kaggle sowie Deduplizierungsprozedur werden berichtet; Details und Korpus sind im Anhang nicht identisch mit einem frei verfügbaren, vollständig reproduzierbaren Trainingsset.

**Fundstelle:** PDF S. 4, Z. 11–17; Anhang S. 28, Z. 23–28.

### Proprietäre Distillation und Lizenz

- Der Distillation-Engine ist proprietär; der Report gibt keine vollständige technische Beschreibung der Optimierung/Generierung und macht eine unabhängige Reproduktion der Distillation schwerer. **Fundstelle:** PDF S. 5, Z. 25–33.
- Die Open-Source-Modelllizenz erlaubt laut Bericht Forschung, interne Evaluation und internes Benchmarking, aber **keine kommerzielle oder produktive Nutzung** des Modells, seiner Derivate oder Outputs. Für Produktion wird eine Enterprise-Lizenz angeboten. Die genaue Lizenz sollte vor einer Nutzung geprüft werden. **Fundstelle:** PDF S. 10, Z. 30–41.

### Grenzen der Kausalaussagen

- RealCause ist semi-synthetisch und die Resultate beruhen auf den dortigen Datensätzen und CATE-Metriken; daraus folgt nicht automatisch Leistung bei beliebigen realen kausalen Fragestellungen.
- Der Bericht sagt ausdrücklich, dass reale Kausalanalyse häufig latente Confounder und unvollkommene Daten enthält. Die gezeigten Experimente belegen keine Lösung des allgemeinen Kausalidentifikationsproblems.
- TabPFN-2.5 als gutes Outcome-/Propensity-Modell ist nicht dasselbe wie ein Modell, das kausale Strukturen oder Interventionseffekte unmittelbar aus Beobachtungsdaten identifiziert.

**Fundstelle:** PDF S. 7, Z. 66–75; S. 9, Z. 49–58; Appendix D, S. 29, Z. 30–45.

### Zahlenabweichung im Report

Beim internen Benchmark nennt der Text an einer Stelle Ergebnisse bis 50.000 Zeilen und 2.000 Features, während die Beschreibung der internen Klassifikations-/Regressionsergebnisse sowie die Diagramme bis 50.000 Zeilen und 500 Features reichen. Das Deckblatt und die generelle Produktbeschreibung beziehen sich auf bis zu 50.000 × 2.000; der interne Figure-5/6-Benchmark scheint aber teilweise nur bis 500 Features zu gehen. Für eine belastbare Aussage deshalb die Datendomäne und Abbildungsspezifikation mitzitieren statt beide Angaben gleichzusetzen. **Fundstelle:** PDF S. 6, Z. 46–49; internes Benchmarkdetail S. 8 (Diagrammachsen); allgemeine Modellgrenze S. 5, Z. 34–41.

### Was man aus dem Report nicht folgern sollte

1. Nicht: „TabPFN-2.5 ist 2,3-mal schneller als XGBoost/AutoGluon.“ Die 1–2,3×-Angabe betrifft TabPFNv2 und bezieht sich auf Inferenz; gegenüber GBDT/AutoML nennt der Bericht keine einheitliche Speedup-Zahl.
2. Nicht: „Die Modellleistung ist in allen Ergebnissen rein zero-shot.“ Der Standard-TabPFN wird ohne Datensatztraining eingesetzt, aber TabPFN-Konfigurationen werden mit einem Surrogat abgestimmt; außerdem existiert die separat realdaten-feinabgestimmte Real-TabPFN-2.5-Variante.
3. Nicht: „TabPFN-2.5 ist unabhängig und öffentlich auf über 100 realen Einsatzfällen validiert.“ Die über 100 Anwendungsfälle sind Teil eines internen proprietären Benchmarks.
4. Nicht: „Die Modellgrenze liegt gesichert bei 100k × 2k, ohne Einschränkungen.“ Das sind Benchmarkresultate im TabArena-Report; empfohlenes Designziel ist 50k × 2k, während Millionen Zeilen explizit zukünftige Arbeit sind.
5. Nicht: „TabPFN löst kausale Inferenz allgemein.“ Die gezeigten Resultate betreffen CATE auf semi-synthetischem RealCause und ausgewählte Meta-Learner.
6. Nicht: „Die 100-%-Win-Rate heißt 100 % höhere Genauigkeit.“ Sie bezeichnet den Anteil gewonnener Vergleiche, nicht die relative Metriksteigerung.

## 5. Relevanz für meine Bachelorarbeit

### Geeignete Verwendung

- **Kapitel 2 – Stand der Technik / Entwicklung von TabPFN:** als neuere Modellgeneration nach TabPFN v1 und v2, mit Erweiterung von kleinen numerischen Aufgaben auf gemischte Daten und größere Zeilen-/Featurezahlen.
- **Kapitel 3 – Architektur und Prior:** für Dual-Attention, zusätzliche Thinking Rows, breitere synthetische Priors, robuste Vorverarbeitung und die klare Trennung zwischen synthetischem TabPFN-2.5 und Real-TabPFN-2.5.
- **Kapitel 4 – Skalierungsansätze:** besonders relevant durch 18/24 Schichten, Featuregruppen, FlashAttention-3, Multi-GPU-Inferenz, die angegebene Komplexitätsformel und die Distillation zu MLP/TreeEns.
- **Kapitel 5 – Evaluation:** TabArena-Lite als öffentlicher Benchmark; Resultate auf 51 ausgewählten Datensätzen aus 1.053 Kandidaten. Berichte nach Aufgabenbereich trennen: bis 10k × 500 und bis 100k × 2k.
- **Diskussion / Limitationen:** sehr gut geeignet, um fortbestehende quadratische Zeilenskalierung, GPU-/Speicherbedarf, nur einen Test-Fold, abweichende Tuningbudgets und proprietäre interne Ergebnisse zu thematisieren.
- **Kausale Inferenz:** als empirischer Transfer zu CATE/RealCause anführen, aber nicht als Nachweis allgemeiner kausaler Identifikation.
- **Praktische Reproduzierbarkeit und Deployment:** Lizenzbedingungen sowie proprietären Distillation-Engine beachten; eine kommerzielle Nutzung ist laut Report unter der genannten nichtkommerziellen Modelllizenz nicht erlaubt.

### Mögliche Formulierung für die Bachelorarbeit (indirektes Zitat)

> Der Prior Labs Team Report zu TabPFN-2.5 beschreibt eine skalierte PFN-Variante mit breiterem synthetischem Prior und dualer Attention über Zeilen und Features. Auf TabArena-Lite berichten die Autoren konkurrenzfähige bzw. führende aggregierte Ergebnisse bis zu 100.000 Zeilen und 2.000 Features; zugleich bleibt die Inferenzkomplexität quadratisch in der Zahl der Zeilen, und für große Aufgaben werden dedizierte GPUs benötigt. Die Resultate sollten als Entwicklerbericht eingeordnet werden, insbesondere weil ein Teil der Evidenz aus proprietären internen Benchmarks stammt. (Prior Labs Team, 2025/2026, S. 4–8, 10–11)

## 6. Wörtliches Schlüsselzitat

> “The runtime and memory usage of TabPFN-2.5 scale quadratically with the number of rows.”

**Fundstelle:** Die Aussage ist im Report auf PDF S. 7, Z. 50–57 durch die Komplexitätsformel erläutert; diese Formulierung ist eine knappe Zusammenfassung und sollte **nicht** als wörtliches Direktzitat verwendet werden.

Für ein tatsächlich wörtliches Zitat eignet sich der Satz aus dem Fazit:

> “The next step is scaling to datasets with millions of rows.”

**Fundstelle:** PDF S. 11, Z. 14–17.

**Arbeitsübersetzung:** „Der nächste Schritt ist die Skalierung auf Datensätze mit Millionen Zeilen.“

Beim Direktzitat die englische Originalfassung, den technischen Report als Quelle und das PDF-Seitenformat angeben. Für die Interpretation ergänzen: Der Satz kennzeichnet Millionen Zeilen als zukünftiges Skalierungsziel, nicht als bereits validiertes Ergebnis.

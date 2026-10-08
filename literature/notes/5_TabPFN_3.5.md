# Prior Labs Team (2026): *TabPFN-3.5: Technical Report*

## Quelle und Zitierhinweis

**Prior Labs Team.** *TabPFN-3.5: Technical Report.* Technischer Bericht, datiert auf den 14. September 2026; die PDF-Kopfzeile nennt arXiv:2609.17895v2 vom 22. September 2026. Die Autorzeile verweist für die namentliche Liste der Beitragenden auf Appendix A.

- **PDF:** `literature/5_TabPFN_3.5.pdf`
- **Gegenstand:** TabPFN-3.5, ein Tabular Foundation Model (TFM) für Klassifikation und Regression, plus die Varianten Fast, Plus und Thinking. Der Bericht behandelt Benchmarkresultate, Architektur und Vorverarbeitung, Inferenz, synthetischen Prior und Lizenzierung.
- **Fundstellenformat:** Das Paper enthält keine gedruckten Zeilennummern. „Z.“ bezeichnet deshalb die Zeile des mit `pypdf` extrahierten Texts und dient nur als Suchhilfe. Bei Tabellen, Abbildungen und zweispaltigem Layout kann die Extraktionsreihenfolge von der visuellen Anordnung abweichen; bitte zusätzlich Seite, Abschnitt und ggf. Abbildungs-/Tabellentitel prüfen.
- **Seitenzählung:** „PDF S.“ meint die physische Seite der 33-seitigen PDF. Der Haupttext steht auf PDF S. 1–12; der Anhang beginnt auf S. 13.
- **Quellenkritik:** Dies ist ein Bericht des Modellherstellers. Die Autoren berichten eigene Evaluationen und teils eigene Harnesses; eine unabhängige Replikation wird in der Quelle nicht vorgelegt. Interne oder proprietäre Varianten und Optimierungen sind nur eingeschränkt von außen nachvollziehbar. Alle Rang- und Win-Rate-Angaben unten sind daher als berichtete Resultate dieses Reports zu lesen, nicht als unabhängiger Nachweis allgemeiner Überlegenheit.

## 1. Kernproblem

### Ausgangslage

TabPFN-3 und andere Tabular Foundation Models sind auf üblichen, kleinen IID-Benchmarks stark. Laut Einleitung bleiben jedoch praktische Fälle schwierig: gruppierte oder zeitliche Splits, sehr große oder breite Tabellen, Text- und hochkardinale Kategorien. Zugleich werden die leistungsstärksten Foundation Models größer und langsamer, was den Einsatz erschwert. TabPFN-3.5 soll diese Lücken verkleinern und dabei die für TabPFN typische In-Context-Inferenz auf bis zu eine Million Trainingszeilen sowie heterogene Tabellen ausweiten. **Fundstelle:** PDF S. 3, Z. 15–20 und 21–32.

### Forschungsfragen / Beiträge

1. Verbessert eine neue TabPFN-Version die Ergebnisse auf dem Standardbenchmark TabArena sowie auf erweiterten Benchmarks für zeitliche/gruppierte Daten, Strings, Text/Bilder und prädiktive Verteilungen?
2. Lässt sich ein gemeinsamer Modell-Checkpoint für Klassifikation und Regression trainieren, ohne dass die Architektur auf getrennte Modelle angewiesen ist?
3. Welche Änderungen an Zellkodierung und synthetischem Prior helfen besonders bei hochkardinalen, breiten und gruppierten Daten?
4. Kann eine Fast-Variante die Latenz senken, und wie verhalten sich die neuen Modelle bei großen Trainingskontexten und gecachter Online-Inferenz?

**Fundstelle:** PDF S. 1, Z. 3–16; S. 3, Z. 21–40; S. 8, Z. 51–55.

### Zentrale Aussage in angemessener Reichweite

Der Report beansprucht Spitzenplätze auf den untersuchten Benchmarks und bessere Ergebnisse als TabPFN-3 in den dargestellten Aufgaben. Das ist nicht gleichbedeutend damit, dass TabPFN-3.5 jedes Datenset oder jeden Split gewinnt: Im Text werden verbleibende Schwächen etwa bei großen, gruppierten und zeitlichen Datensätzen ausdrücklich erwähnt. **Fundstelle:** PDF S. 5, Z. 31–44.

## 2. Methodischer Ansatz / Architektur

### PFN-Ansatz und Trainingsprior

TabPFN-3.5 bleibt ein Tabular Foundation Model: Es erhält beim Einsatz die beschrifteten Trainingsbeispiele als Kontext und sagt Labels für Testbeispiele voraus, anstatt für jede Aufgabe ein klassisches Modell per Gradientenabstieg neu zu trainieren. Das Vortraining erfolgt auf synthetisch generierten tabellarischen Aufgaben. Der Bericht sagt, die Pipeline folge eng TabPFN-3, sei aber in Diversität und Skalierbarkeit verbessert und an den TabICLv2-Prior angelehnt. Besonders sollen die synthetischen Aufgaben realistischere hochkardinale Kategorien, mehr Features und gruppierte Situationen abbilden, in denen Testdaten aus einer anderen Gruppe kommen als Trainingsdaten. **Fundstelle:** PDF S. 3, Z. 27–32; S. 11, Z. 8–15.

Wichtig für die Interpretation: Das beschreibt, welche Muster der synthetische Prior stärker repräsentieren soll. Es belegt nicht, dass das Modell in jeder realen Domäne entsprechend gut generalisiert. Die empirische Generalisierung wird separat auf den Benchmarks untersucht.

### Architektur und Zellkodierung

- **Übernommene Grundstruktur:** Die Gesamtarchitektur bleibt nahe an TabPFN-3, wird aber bei Zellrepräsentation, gemeinsamer Aufgabenverarbeitung und Modellbreite verändert. **Fundstelle:** PDF S. 9, Z. 31–35; S. 8, Z. 51–55.
- **Drei Eingabesignale:** Neben fehlenden/unendlichen Werten und standardisierten Zellwerten kommen Fourier-Merkmale und eine In-Context-ECDF-Kodierung hinzu. Der ECDF-Rang jedes Werts wird gegen die Trainingswerte derselben Spalte gebildet. So erhält das Modell neben der absoluten skalierten Größe einen Hinweis auf die Position innerhalb der jeweiligen Spaltenverteilung. **Fundstelle:** PDF S. 9, Z. 34–48.
- **Fourier-Encoding:** Standardisierte Werte werden mit gelernten Frequenzen in Sinus-/Kosinusmerkmale abgebildet. Die Autoren motivieren dies unter anderem mit feinen Unterschieden zwischen ordinal kodierten Kategorien hoher Kardinalität. **Fundstelle:** PDF S. 9, Z. 36–40; S. 10, Z. 16–19 und Z. 29–38.
- **ECDF-Encoding:** Werte werden in Midranks innerhalb der Trainingsspalte umgerechnet und mit niederfrequenten Sinus-/Kosinustermen kodiert. Eine streng monotone Transformation einer Spalte ändert diese Ränge nicht. Gleichzeitig wird der standardisierte Wert weitergegeben, damit auch absolute Größeninformation erhalten bleibt. **Fundstelle:** PDF S. 9, Z. 40–48; S. 10, Z. 11–12 und Z. 31–38.
- **Gemeinsamer Klassifikations-/Regressionscheckpoint:** Das Modell wird gemeinsam auf beiden Aufgabenarten trainiert; der Aufgabentyp ist eine Eingabe. Zellkodierer, Spaltenverteilungs-Embedder, Feature-Aggregator und In-Context-Transformer sind geteilt, während Label-Encoding und Output-Head aufgabenspezifisch sind. Klassifikation nutzt Attention über die One-hot-Trainingslabels; Regression gibt eine Verteilung über feste Bins aus. **Fundstelle:** PDF S. 9, Z. 49–57.
- **Modellbreite:** Die Breite des In-Context-Transformers steigt laut Report von 512 auf 1024 Dimensionen. Die Parameterübersicht nennt 220 Mio. Parameter für TabPFN-3.5 und 84 Mio. für TabPFN-3.5-Fast. **Fundstelle:** PDF S. 9, Z. 58 ff.; S. 4, Tabelle „Overview of TabPFN releases“, Z. 1–12.

### Vorverarbeitung und Ensemble

Anders als frühere Versionen setzt TabPFN-3.5 laut Abschnitt 3.2 nicht zusätzlich auf Quantiltransformationen, robustes Scaling oder SVD-Komponenten. Die Autoren führen die größere Ausdruckskraft auf die verbesserten Zellkodierungen zurück. Für die finale Vorhersage aggregiert die Standardkonfiguration acht Estimatoren auf verschiedenen Permutationen des Datensatzes; Fast aggregiert vier. **Fundstelle:** PDF S. 11, Z. 1–7.

### Varianten und Zugänglichkeit

- **TabPFN-3.5:** Kernmodell; verfügbar als Open-Source-Paket für Evaluation und nicht-kommerzielle Nutzung.
- **TabPFN-3.5-Fast:** kleinerer Alpha-Checkpoint für Latenz-sensible Nutzung; der Report beschreibt geringe Leistungseinbußen gegenüber dem Kernmodell.
- **TabPFN-3.5-Plus:** API-/Enterprise-Variante mit weiterentwickelter Text- und Datumsverarbeitung sowie proprietären Inferenzoptimierungen, darunter FP8-Attention.
- **TabPFN-3.5-Thinking:** zusätzliche Inferenzzeitberechnung auf Basis von Plus. Der Bericht betont, dass hierfür keine LLMs, realen Daten oder Internetsuche eingesetzt würden; Implementierungsdetails sind proprietär.

Plus und Thinking sind laut Report nicht Teil des Open-Source-Releases. **Fundstelle:** PDF S. 3, Z. 33–41; S. 11, Z. 16–36.

## 3. Wichtigste Ergebnisse

### Benchmark-Überblick im Abstract

Tabelle 1 meldet für die jeweils beste Variante der TabPFN-3.5-Familie Rang 1 auf allen sieben aufgeführten Benchmarks. Die dortige mittlere Win-Rate beträgt 78 % gegen den stärksten anderen TFM und 89 % gegen den stärksten Nicht-TFM. Das sind **Anteile gewonnener benchmarkinterner Splits**, keine Prozentpunkte Accuracy-Verbesserung und keine relative Fehlerratenreduktion. Die beste Variante ist nicht überall dieselbe: Thinking wird für die ersten vier Benchmarks herangezogen, TabPFN-Rel (3.5) für RelArena, TabPFN-3.5 für TALENT und ScoringBench. **Fundstelle:** PDF S. 1, Tabelle 1, Z. 20–35; Definition der Win-Rate und Datensatzgewichtung: PDF S. 33, Z. 1–6.

| Benchmark | Berichteter Rang / Win-Rate gegen bestes Modell | Einordnung im Report |
|---|---|---|
| TabArena | 1/89; 57 % gegen bestes anderes TFM, 96 % gegen bestes Nicht-TFM | Standardbenchmark für tabellarische Vorhersage; 51 Datensätze. |
| BeyondArena | 1/29; 83 % / 79 % | IID- und Nicht-IID-Aufgaben, darunter gruppierte/zeitliche Splits sowie unterschiedliche Größen und Featuretypen. |
| STRABLE | 1/197; 98 % / 98 % | Tabellen mit String-Spalten; 108 Datensätze und 3 Folds je Datensatz. |
| MulTaBench | 1/14; 90 % / 95 % | Tabellarische Daten in Kombination mit Text und Bildern; 40 Datensätze und 5 Folds. |
| RelArena-? | 1/12; 57 % / 71 % | Relationale Aufgaben über TabPFN-Rel mit TabPFN-3.5-Plus; hier also nicht nur das Kernmodell. |
| TALENT | 1/37; 80 % / 91 % | Große Sammlung tabellarischer Datensätze; im Benchmarküberblick wird die beste Familievariante gewertet. |
| ScoringBench | 1/52; 78 % / 91 % | Bewertet prädiktive Verteilungen von Regressionsmodellen, nicht nur Punktvorhersagen. |

**Fundstelle:** PDF S. 1, Tabelle 1, Z. 20–35; Benchmarkgrößen und Win-Rate-Berechnung S. 33, Z. 1–6. „1/89“ etc. ist der im Report angegebene Platz unter den Benchmarkmethoden, nicht die Zahl getesteter Datensätze.

### TabArena

TabPFN-3.5, Fast und Thinking bilden laut Bericht gemeinsam die Elo-gegen-Laufzeit-Paretofront: Für jedes betrachtete Zeitbudget erreicht mindestens eine dieser Varianten den höchsten Elo-Wert. TabPFN-3.5 liegt laut Einleitung um etwa 150 Elo-Punkte über TabPFN-3 auf TabArena; gegenüber TabFM nennt der Report an anderer Stelle 84 Elo-Punkte bei einem Zehntel der Gesamtzeit je Sample. Außerdem wird ein Vergleich mit AutoGluon 1.6 extreme berichtet: 130 Elo-Punkte mehr bei einem Fünftel der Zeit. Die Zeitachse in Abbildung 2 addiert Fit- und Vorhersagezeit je 1.000 Trainings- bzw. Testzeilen und verwendet den Median über 51 Datensätze. Diese Vergleiche hängen somit an der gewählten Hardware-, Mess- und Konfigurationseinstellung. **Fundstelle:** PDF S. 3, Z. 56–64; S. 4, Z. 51–64; S. 5, Abbildung 2, Z. 18–22.

### BeyondArena: schwierigere Splits und Größen

BeyondArena umfasst unter anderem IID-, Gruppen- und Zeitsplits, kleine bis sehr große Datensätze, niedrige/hohe Dimensionalität, Text und hochkardinale Features. TabPFN-3.5 belegt insgesamt Rang 1 im „core“-Ergebnis und verbessert sich gegenüber TabPFN-3 in allen dargestellten Teilgruppen. Die Autoren berichten aber ausdrücklich, dass getunte/ensemblierte MLPs bei gruppierten, zeitlichen und großen Datensätzen weiterhin die höchsten Werte erreichen. Für die Teilmenge bis 100.000 Zeilen entspreche TabPFN-3.5 den besten Baselines auf gruppierten und zeitlichen Aufgaben. Kleine Teilgruppen haben breite Konfidenzintervalle; außerdem ist die zeitliche (und teilweise gruppierte) Kategorie mit Datensatzgröße konfundiert. **Fundstelle:** PDF S. 5, Z. 23–44.

Der Gruppen-Evaluationsablauf unterscheidet sich laut Text teilweise vom aktuellen BeyondArena-Verfahren (Verweis auf Appendix C.2.3). Das ist für direkte Vergleiche und Reproduzierbarkeit relevant. **Fundstelle:** PDF S. 5, Z. 36–41.

### STRABLE und MulTaBench

Auf STRABLE werden String-Spalten mit unter anderem Namen, Adressen und Freitextnotizen getestet. Die Abbildung enthält 108 Datensätze mit je drei Folds. Auf MulTaBench werden tabellarische Spalten mit Text-/Bildfeldern kombiniert; die Abbildung umfasst 40 Datensätze mit je fünf Folds. Bei den veröffentlichten Benchmarkbaselines ohne native Textunterstützung werden eingefrorene `e5-small-v2`-Embeddings und ohne native Bildunterstützung eingefrorene `DINOv3-small`-Embeddings verwendet; beide werden auf 30 PCA-Komponenten reduziert. TabPFN-3.5 und Fast nutzen für den Vergleich dieselbe Vorverarbeitung. Plus und Thinking verarbeiten die Rohtextspalten direkt, verwenden für Bilder aber weiter die Embeddings. Der Bericht zeigt die Familie deutlich vor den veröffentlichten Baselines; diese konkrete Vergleichsaussage sollte wegen des vom Hersteller durchgeführten Runs als berichtetes Benchmarkresultat gekennzeichnet werden. **Fundstelle:** PDF S. 7, Abbildung 5 und Z. 37–84.

### Relationale Aufgaben und Inferenzgeschwindigkeit

Für RelArena nutzt der Bericht TabPFN-Rel mit TabPFN-3.5-Plus; diese Kombination liegt laut Report auf Rang 1 der Modell- und Modell+System-Leaderboards. Der Text sagt, TabPFN-3.5-Plus verbessere den vorherigen TabPFN-3-Plus-Stand um nahezu 90 Elo-Punkte. Ein zusätzlich dargestellter, interner und gemeinsam mit dem Basismodell entwickelter TabPFN-Rel-Harness bringt weitere 36 Elo-Punkte, ist aber nicht als vollständig freigegebene Modellversion zu behandeln. **Fundstelle:** PDF S. 7, Z. 85–99; S. 8, Abbildung 6, Z. 25–30.

In einem Inferenztest auf einer NVIDIA RTX PRO 6000 Blackwell mit 96 GB ist TabPFN-3.5 bei großen Trainingskontexten laut Bericht bis zu zweimal langsamer als TabPFN-3. Fast wird als bis zu dreimal schneller als TabPFN-3 beschrieben. Der Plus-Pfad nutzt FP8-Attention und wird mit 1,25-facher Latenz von TabPFN-3 angegeben; derselbe Abschnitt nennt außerdem eine Viertelung der Laufzeit für den optimierten Plus-Pfad, ohne diese Aussage dort eindeutig einer konkreten Plus-/Fast-Kombination oder Messbedingung zuzuordnen. Ab 128.000 Trainingszeilen skalieren die Varianten in diesem Test quadratisch mit der Anzahl der Trainingszeilen. Bei gecachter Vorhersage einzelner Testzeilen liegt TabPFN-3.5 laut Abbildung ungefähr auf dem Niveau von TabPFN-3; die teuren Berechnungen auf den Trainingsdaten können wiederverwendet werden. **Fundstelle:** PDF S. 7, Z. 100–104; S. 8, Z. 31–50; S. 9, Abbildung 7, Z. 27–30.

**Wichtig zur Einordnung:** Das sind modellseitige Forward-Time-Messungen und ein bestimmtes GPU-Setup, keine universellen Ende-zu-Ende-Laufzeiten für jede Umgebung. API-, Plus- und Thinking-Resultate können zudem proprietäre Infrastruktur bzw. Inferenzimplementierungen einbeziehen.

## 4. Konkrete Limitierungen und kritische Einordnung

### Vom Report ausdrücklich genannte Grenzen

1. **Gruppiert, zeitlich und sehr groß:** Auf der vollständigen BeyondArena-Auswertung behalten getunte/ensemblierte MLPs die besten Resultate in den gruppierten, zeitlichen und großen Teilgruppen. TabPFN-3.5 verkleinert die Lücke; nur nach Beschränkung auf nicht-große Datensätze bis 100.000 Zeilen wird Gleichstand mit den besten Baselines für Gruppen-/Zeitsplits berichtet. **Fundstelle:** PDF S. 5, Z. 31–39.
2. **Unsicherheit bei kleinen Slices:** Bei kleinen Benchmarkteilgruppen sind die Konfidenzintervalle breit; die genaue Rangfolge soll vorsichtig interpretiert werden. **Fundstelle:** PDF S. 5, Z. 32–34.
3. **Latenz des großen Modells:** Das Kernmodell kann bei großen Trainingsmengen bis zu zweimal langsamer sein als TabPFN-3. Die Fast-Variante tauscht Geschwindigkeit gegen einen kleinen Genauigkeits-/Elo-Verlust; auf BeyondArena wird Fast als dreimal schneller und 40 Elo-Punkte niedriger als TabPFN-3.5 beschrieben. **Fundstelle:** PDF S. 4, Z. 51–55; S. 5, Z. 42–44; S. 8, Z. 31–36.
4. **Quadratische Skalierung:** Für mehr als 128.000 Trainingszeilen wird quadratische Skalierung mit der Zeilenzahl angegeben. Die Unterstützung von bis zu einer Million Zeilen bedeutet folglich nicht, dass die Inferenz bei dieser Größe günstig ist. **Fundstelle:** PDF S. 8, Z. 31–36; Größenübersicht S. 4, Tabelle, Z. 1–12.
5. **Proprietäre Bestandteile:** Plus- und Thinking-Optimierungen werden nicht technisch offengelegt; Varianten und interne Harnesses sind somit nicht in gleicher Weise reproduzierbar wie das beschriebene Kernmodell. **Fundstelle:** PDF S. 11, Z. 16–36.
6. **Lizenzbeschränkung der Gewichte:** Der Code steht unter Apache 2.0, die Gewichte jedoch unter der separaten TABPFN-3.5 License v1.0. Der Bericht erlaubt nach eigener Darstellung Forschung/Evaluation, untersagt aber die kommerzielle oder produktive Nutzung von Modellen, Derivaten und Outputs ohne kommerzielle Enterprise-Lizenz. Das ist eine praktische Einsatzgrenze, obwohl der Quellcode offen bereitgestellt wird. **Fundstelle:** PDF S. 1, Z. 17–18; S. 11, Z. 38–43; S. 12, Z. 1–18.

### Was die Limitationsdiskussion nicht belegt

Im Haupttext ist kein systematischer Katalog etwaiger Fehlerfälle zu fehlenden Werten, Klassenungleichgewicht oder einzelnen Domänen enthalten. Fehlende/unendliche Werte werden in der Zellkodierung behandelt; daraus folgt aber kein Nachweis, dass das Modell bei beliebigen Missingness-Mustern robust ist. Ebenso sollten die hohen Maximalgrößen (eine Million Zeilen, 6.000 Features) als empfohlene Eingabegrößen des Reports verstanden werden, nicht als pauschale Leistungsgarantie für jede Kombination aus Zeilen und Features. **Fundstelle:** PDF S. 4, Tabelle und Bildunterschrift, Z. 1–12; Kodierung S. 10, Z. 29–38.

### Quellen- und Benchmarkgrenzen

- Der Report stammt vom Entwicklerteam, das die neuen Modelle entwickelt und evaluiert. Rang 1 in der Ergebnistabelle ist daher eine wichtige Herstellerangabe, aber kein Ersatz für eine unabhängige Replikation.
- Win-Rate bedeutet: Split für Split wird mit einem Vergleichsmodell verglichen, Gleichstand zählt als halber Sieg; Resultate werden erst innerhalb eines Datensatzes und dann über Datensätze gemittelt, sodass jeder Datensatz gleich gewichtet wird. Es handelt sich ausdrücklich nicht um Prozent Accuracy-Verbesserung. **Fundstelle:** PDF S. 33, Z. 1–6.
- Die in Tabelle 1 verglichenen Varianten wechseln zwischen Benchmarks (Thinking, Plus/Rel-Harness oder Kernmodell). Man darf die sieben Rang-1-Einträge nicht als sieben unabhängige Tests desselben unveränderten Open-Source-Checkpoints zusammenfassen. **Fundstelle:** PDF S. 1, Z. 31–35.
- Der interne TabPFN-Rel-Harness wird im Bericht als Vorschau ausgewiesen; die Ergebnisse mit Open-Source-Checkpoints und Thinking seien noch in Arbeit. **Fundstelle:** PDF S. 7, Z. 95–99.
- Der Bericht kündigt für Benchmarkwettbewerbe teilweise eigene Evaluationen und abweichende Abläufe an (z. B. Gruppenbewertung); bei Vergleichen muss daher auf Protokoll, Daten-Slices und Baselinekonfiguration geachtet werden. **Fundstelle:** PDF S. 5, Z. 36–41; S. 7, Z. 74–84.

## 5. Relevanz für meine Bachelorarbeit

Diese Quelle eignet sich für **Kapitel 2 (Stand der Technik)** als aktueller Entwicklungsstand von TabPFN: Sie zeigt, wie sich PFN-basierte Tabellenvorhersage von kleinen IID-Aufgaben in Richtung große, breite und heterogene Tabellen entwickelt. Für den Vergleich mit den früheren Arbeiten sind besonders die neuen Zellrepräsentationen (Fourier- und ECDF-Merkmale), der gemeinsame Klassifikations-/Regressionscheckpoint und die Anpassung des synthetischen Priors an hochkardinale und gruppierte Daten nützlich.

Für **Kapitel 4 (Skalierung und praktische Einsatzgrenzen)** ist die Quelle relevant, weil sie Modellgröße, empfohlene Zeilen-/Featurezahlen, Fast-Variante, gecachte Inferenz und Hardwaremessungen benennt. Die Skalierung ist ambivalent: ein größeres Modell und ein breiterer Inputbereich gehen mit möglicher höherer Latenz und quadratischem Verhalten bei großen Kontexten einher. Daher die Aussage „bis zu 1M Zeilen / 6k Features“ immer zusammen mit den Laufzeitmessungen und dem konkreten Benchmarkprotokoll zitieren.

Für die **Diskussion** bietet BeyondArena eine wichtige Einschränkung: Auf den vollständigen gruppierten, zeitlichen und großen Teilmengen liegen getunte MLP-Ensembles weiterhin vorn; die behauptete Gleichstellung gilt in der genannten Auswertung für die bis 100.000 Zeilen beschränkte Teilmenge. Zusätzlich sind Herstellerperspektive, proprietäre Varianten und Lizenz der Gewichte zu diskutieren. Der Bericht eignet sich somit sowohl als Leistungsbeleg als auch für eine differenzierte Einordnung von Reproduzierbarkeit und praktischer Nutzbarkeit.

## 6. Wörtliches Schlüsselzitat

> “TabPFN-3.5 raises the recommended feature limit and can simultaneously handle 1M data points and 6k features.”

**Fundstelle:** PDF S. 4, Bildunterschrift zu Abbildung 1, Z. 34–37. Direktes Zitat im englischen Original; im Fließtext kann es sinngemäß übersetzt werden. Dabei „recommended feature limit“ nicht als Garantie für gleichbleibende Leistung auf beliebigen Datensätzen interpretieren.

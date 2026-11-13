# Kritische Neubewertung von Exposé, Forschungsfragen und Beitrag

Stand: 9. November 2026. Diese Bewertung ersetzt die frühere
Notenprognose im Dokument
[Expose_Evaluation_2026-11-08.md](./Expose_Evaluation_2026-11-08.md).
Geprüft wurden Exposé, Gliederung, Literaturabgleich, die Volltexte von
Zaimoğlu (2026) und Tran & Byeon (2024), Pilotprotokoll und Projektdateien.

## Kurzurteil

**Das Vorhaben ist für eine Bachelorarbeit geeignet und der empirische
Vergleich kann einen ausreichenden, klar begrenzten Beitrag leisten.**
Sein Wert liegt nicht in einem allgemeinen Ranking „TabPFN gegen
LightGBM“, sondern in der Frage, ob und wie sich der Leistungsabstand
zweier konkreter Pipelines unter verschiedenen Missing-Data-Behandlungen
verändert. Das ist eine nachvollziehbare Anschlussuntersuchung zur
Vorarbeit von Zaimoğlu.

Die Arbeit sollte dennoch keine große oder allgemeine Forschungslücke
behaupten. TabPFN unter MCAR, Median-Imputation und Missing-Indikatoren
wurden bereits untersucht. Der Eigenanteil liegt in der auf beide Modelle
angewandten Behandlung, dem gepaarten Vergleich mit denselben Splits und
Masken sowie dem Fokus auf TabPFN-3.5 und LightGBM. Dieser Beitrag ist für
eine BA plausibel, wenn die Ausführung methodisch sauber und die
Schlussfolgerung eng begrenzt bleibt.

## 1. Relevanz des Modellvergleichs

Ein Modellvergleich ist für sich genommen keine ausreichende Begründung.
Ein einzelner Vergleich von TabPFN-3.5 mit LightGBM auf wenigen Datensätzen
würde weder eine Rangfolge der Modellfamilien noch eine allgemeine Aussage
über Robustheit tragen. LightGBM ist eine konkrete, gut begründbare
Baum-Baseline, aber kein Stellvertreter für sämtliche Baumverfahren.

Der Vergleich wird relevant, weil die Missing-Data-Behandlung eine
praktische Pipelineentscheidung ist. Wer TabPFN oder LightGBM mit
unvollständigen Eingaben einsetzen will, muss entscheiden, ob NaNs
modellintern verarbeitet oder zuvor imputiert werden. Die Untersuchung
fragt daher, ob diese Entscheidung den Leistungsabstand zwischen den
beiden konkreten Pipelines verändert.

Die Einheit der Schlussfolgerung muss lauten: „In den untersuchten
Datensätzen und Konfigurationen veränderte sich der gepaarte
Balanced-Accuracy-Abstand wie folgt.“ Nicht zulässig wäre: „TabPFN ist
robuster als Baumverfahren“ oder „LightGBM ist bei fehlenden Daten
schlechter.“

## 2. Literatur und Abgrenzung

### Zaimoğlu (2026)

Die IEEE-Arbeit ist die engste Vorarbeit. Sie verwendet TabPFN v2,
kontrollierte MCAR-Raten von 0, 10, 20 und 40 Prozent sowie interne
Verarbeitung, Median-Imputation und Median-Imputation mit Indikatoren.
Die klassischen Baselines erhalten nicht dieselben Behandlungen; die
Studie enthält kein LightGBM und verwendet Standardkonfigurationen.
Daher beantwortet sie nicht die gepaarte Differenzfrage der vorliegenden
Arbeit.

Die im Volltextabgleich erwähnte Differenz von 0,035 bei 40 Prozent ist
kein gepaarter Behandlungseffekt: Sie vergleicht TabPFN mit
Median-Imputation und HistGradientBoosting ohne externe Imputation.
Sie darf höchstens die Motivation eines gekreuzten Vergleichs illustrieren.
Die Studie belegt weder die Größe noch die Richtung des Effekts für
TabPFN-3.5 gegen LightGBM.

Zaimoğlu ist außerdem kritisch zu würdigen: Es gibt nur drei Seeds,
keine Validierungspartition und keine Hyperparameterabstimmung. Die
Friedman-Auswertung verwendet Datensatz-Fehlraten-Paare als Blöcke,
obwohl mehrere Fehlraten desselben Datensatzes voneinander abhängig sind.
Das sollte bei der Diskussion von Signifikanz und Verallgemeinerbarkeit
berücksichtigt werden.

### Tran & Byeon (2024)

Tran & Byeon verwenden LightGBM zur iterativen Imputation und TabPFN
anschließend als Klassifikator auf einem kleinen medizinischen Datensatz.
Das ist eine andere Forschungsfrage als ein gekreuzter Modell- und
Pipelinevergleich unter künstlich kontrolliertem MCAR. Die Arbeit gehört
als Anwendungsbeispiel in die Literaturanalyse, aber ihre Ergebnisse
belegen keine allgemeine Leistungsfähigkeit der Kombination. Die
Berichterstattung zur Bereinigung und Imputation fehlender Fälle sollte
kritisch eingeordnet werden.

### Weitere Missing-Data-Literatur

TIME untersucht TabPFNv2 als Teil eines multimodalen Bild-Tabellen-Systems;
TabImpute zielt primär auf Rekonstruktionsgüte. Sepin untersucht eine
andere Imputationsaufgabe mit fehlendem kontinuierlichem Zielwert bei
vollständig beobachteten Prädiktoren. Diese Quellen erweitern den Kontext,
beantworten FF2 aber nicht. Die Literaturanalyse sollte Vorhersagegüte,
Rekonstruktionsgüte und inferenzstatistische Imputationsergebnisse nicht
als dieselbe Zielgröße behandeln.

Der externe Suchabgleich ist gezielt, aber nicht systematisch vollständig.
Die Arbeit sollte daher nur behaupten, dass eine entsprechende Studie im
geprüften Quellenbestand nicht gefunden wurde. Eine absolute
Neuheitsbehauptung ist nicht belegt.

## 3. Forschungsfragen

Die übergeordnete Frage verbindet die Literaturbefunde zu Möglichkeiten
und Grenzen von TabPFN mit dem zusätzlichen Erkenntnisbeitrag der eigenen
Untersuchung. Sie nennt den Einfluss fehlender Werte, ohne Fehlerraten,
Pipelines und Metrik aus FF2 zu wiederholen.

**FF1** ist fachlich sinnvoll, aber weiterhin breit: Methoden,
Einsatzmöglichkeiten, Leistungsfähigkeit und Grenzen. Sie braucht
Auswahlkriterien für Literatur, einen klaren Zeitrahmen und eine
Konzeptmatrix. Die Missing-Data-Befunde sollten die Brücke zu FF2 bilden,
nicht den gesamten Literaturteil verdrängen.

**FF2** ist der Kern der empirischen Eigenleistung. Die Frage selbst
benennt knapp den Leistungsunterschied, die MCAR-Fehlerraten, die
Behandlungen und die untersuchten numerischen Datensätze. Die technische
Operationalisierung – gepaarter Vergleich und Balanced Accuracy als
primärer Endpunkt – steht im Methodikteil statt in der Frage. Die
ergänzende Log-Loss-Auswertung sollte als sekundär gekennzeichnet bleiben.

Das Wort „gepaart“ bedeutet gleiche Testfälle, Splits und innerhalb einer
Fehlrate gleiche Masken für Modelle und Pipelines. Es impliziert keinen
Signifikanznachweis. Die Wiederholungen auf wenigen Datensätzen dürfen
nicht als viele unabhängige Datensätze behandelt werden.

## 4. Methodische Stärken und offene Punkte

### Stärken

- identische Datenaufteilungen und Masken für die Pipelinevergleiche;
- separate MCAR-Maskierung von Training, Validierung und Test;
- Imputationsstatistiken ausschließlich aus beobachteten Trainingswerten;
- gruppengetrennte Splits bei identischen ursprünglichen Eingabevektoren;
- klarer Hinweis, dass externe Median-Imputation kein isolierter
  Mittelwert-vs.-Median-Vergleich ist;
- keine Verwendung des Testsets zur Hyperparameterwahl;
- sinnvolle Begrenzung auf binäre Klassifikation und numerische Daten.

### Vor dem Hauptversuch festlegen

1. **Datensätze:** Auswahl und Ausschlussregeln verbindlich dokumentieren.
   Vier Datensätze können für eine BA ausreichen, sind aber keine
   repräsentative Stichprobe tabellarischer Aufgaben.
2. **Splits und Wiederholungen:** Splitanteile, Zahl der Splits,
   Maskierungsreplikate und Seed-Logik festlegen. Masken sind zwischen
   Fehlerraten unabhängig; gleiche Splits erlauben nur eine Paarung auf
   Split-Ebene.
3. **Zielgröße und Aggregation:** Pro Datensatz und Bedingung zuerst
   \(\Delta=\mathrm{BA}_{TabPFN}-\mathrm{BA}_{LightGBM}\) bilden, danach
   die Änderung gegenüber der vollständigen Referenz auswerten. Datensätze
   getrennt darstellen und keine Wiederholungen als unabhängige Datensätze
   zählen.
4. **0-Prozent-Bedingung:** Indikatoren weglassen, weil keine fehlenden
   Werte vorliegen und ausschließlich konstante Indikatorspalten sonst
   die Eingabedimension künstlich verändern.
5. **Vollständig maskierte Trainingsspalten:** Vorab definieren, wie diese
   behandelt werden. Jede datenabhängige Entscheidung muss ohne Testdaten
   getroffen werden.
6. **Tuning:** Suchraum, Metrik, Versuchszahl und die Aufteilung von
   Tuning und Wiederholungen dokumentieren. Eine auf vollständigen Daten
   abgestimmte und dann eingefrorene LightGBM-Konfiguration untersucht
   den Behandlungseffekt bei fixer Konfiguration – nicht das beste
   Modell je Bedingung. Die 50-Prozent-Sensitivität bleibt eine begrenzte
   Ergänzung.
7. **Reproduzierbarkeit:** Die aktuelle `requirements.txt` enthält
   Versionsbereiche, keine vollständige Sperre. Das Pilotskript sucht
   Checkpointdateien und gibt Hashes aus, erzwingt jedoch nicht sichtbar,
   dass beim Modelllauf genau der dokumentierte Checkpoint geladen wurde.
   Umgebung und tatsächliche Checkpointidentität müssen für den Hauptlauf
   nachweisbar fixiert werden.

Der Pilot auf WDBC ist ein Machbarkeitsnachweis laut Protokoll, kein
Leistungsnachweis. Die lokal vorhandene virtuelle Umgebung ließ sich bei
der Prüfung nicht mit TabPFN importieren. Das widerspricht nicht
notwendigerweise dem protokollierten Pilotlauf, zeigt aber, dass die
Umgebung aktuell nicht aus sich heraus reproduzierbar ist.

## 5. Exposé und Gliederung

Der rote Faden trägt: Tabular Foundation Models und TabPFN-Evidenz führen
zu fehlenden Eingabewerten und dann zur konkreten Pipelinefrage. Die
Gliederung vermeidet ein eigenständiges Versionsgeschichtskapitel und
einen unnötigen XAI- oder Laufzeitbenchmark.

Der Titel benennt TabPFN-3.5, fehlende Merkmalswerte, die Literaturanalyse,
den gepaarten Vergleich mit LightGBM und den MCAR-Rahmen. Die Formulierung
vermeidet den unnötig technischen Ausdruck „MCAR-Pipelinevergleich“.

Die Exposé-Formulierungen begrenzen nun den Anspruch auf die konkreten
Pipelines, Datensätze und MCAR-Bedingungen. Die Projektbeschreibung im
README wurde dem vorhandenen Pilotcode angepasst. Eine vollständige
Präregistrierung ist noch nicht erfolgt; offene Versuchsdetails müssen
vor dem Hauptlauf dokumentiert und fixiert werden.

## Gesamtbewertung

**Geeignet für eine Bachelorarbeit: ja.** Der Modellvergleich allein
wäre ein schwacher Beitrag; als kontrollierte Untersuchung, ob sich der
gepaarte Leistungsabstand durch die Missing-Data-Behandlung verändert,
ist er hinreichend fokussiert und eigenständig genug für eine BA.

Die Qualität wird sich an sauberem Design, transparenter Literaturauswahl,
reproduzierbarer Umgebung und disziplinierter Interpretation entscheiden.
Aus dem Exposé lässt sich keine seriöse Note prognostizieren. Die größten
Risiken bleiben die kleine und nicht repräsentative Datensatzbasis, offene
Versuchsdetails und eine mögliche Überdehnung der Neuheits- oder
Generalisierungsbehauptung.

## Aktueller Bearbeitungsstand: 6. November 2026

### Beschlossener Missing-Data-Schwerpunkt

Nach dem [Literaturabschlussabgleich](../literature/notes/Missing_Data_Abschlussabgleich.md)
wurde der Zusatzmerkmalversuch durch einen Missing-Data-Pipelinevergleich
ersetzt. [Exposé](./Expose.tex) und [Gliederung](./Gliederung.tex) wurden
mit identischem Titel und identischen Forschungsfragen darauf ausgerichtet.
Die bisherigen Zusatzmerkmal-Planungsnotizen weiter unten sind historisch.

**Vom Nutzer festgelegt:**

Nach Abgleich mit den ursprünglichen Fragen wurde die breite Klammer
wiederhergestellt:

- **Übergeordnet:** „Welche Möglichkeiten und Grenzen von TabPFN für
  tabellarische Vorhersageaufgaben lassen sich aus der aktuellen Forschung
  und einer eigenen Untersuchung bei unvollständigen Eingaben ableiten?“
- **FF1:** „Welche methodischen Ansätze und Einsatzmöglichkeiten von
  TabPFN beschreiben ausgewählte aktuelle Arbeiten, und wie belastbar
  sind ihre Aussagen zur Leistungsfähigkeit und zu den Grenzen des Modells?“
- **FF2:** „Wie verändert die Behandlung fehlender Merkmalswerte den
  Leistungsvergleich zwischen TabPFN-3.5 und LightGBM bei steigenden
  Fehlraten über mehrere Datensätze?“

Die Versuchsdetails bleiben in der Methodik. Der breitere Literaturfokus
bleibt erhalten; die Synthese zur Behandlung fehlender Werte bildet die
Brücke zu FF2. Der LightGBM-Vergleich betrifft nur den empirischen
Schwerpunkt, nicht alle Einsatzmöglichkeiten beider Modelle. Die Bewertung von
Modellversionen, Daten, Vergleichsverfahren und Evaluationsdesigns
ist im Literaturvorgehen explizit beschrieben.

- MCAR-Maskierung in Training, Validierung und Test, separat und unabhängig,
  jeweils mit derselben Wahrscheinlichkeit;
- 0 %, 10 %, 30 % und 50 %; tatsächliche Fehlanteile dokumentieren;
- interne Verarbeitung versus Trainingsmedian-Imputation als Hauptvergleich;
- Median plus Missing-Indikatoren als kleine ergänzende Analyse;
- Klassenlabels bleiben vollständig; gleiche Splits und Masken für alle Pipelines.

Der Beitrag liegt in der kritischen Synthese und im kontrollierten Vergleich
von Modell, Behandlung und Fehlrate, nicht in einer neuen Imputationsmethode.
Interne TabPFN-Verarbeitung ist nicht „ohne Imputation“: Sie bewahrt
Missing-Indikatoren und ersetzt Werte durch Trainingsmittelwerte.
Der Versuch ist ein Pipelinevergleich, keine isolierte Median-Ablation.
Die LightGBM-Konfiguration wird auf der vollständigen Referenz abgestimmt
und für die folgenden Bedingungen eingefroren.

**Zusätzlich vom Nutzer beschlossen:** Identische ursprüngliche Eingaben
ohne ID/Ziel werden vor Maskierung und datenabhängiger Vorverarbeitung
als Gruppen gebildet und nicht über Training, Validierung und Test
verteilt. Widersprüchliche Labels bleiben erhalten; Klassenanteile und
erreichte Splitgrößen werden dokumentiert.

Der feste Hauptversuch wird um eine vorab definierte Tuning-Sensitivität
bei 50 % Fehlrate ergänzt: LightGBM für interne Verarbeitung und Median
separat neu abstimmen, mit gleichem Suchraum, gleicher Optimierungsmetrik
und gleichem Versuchszahlbudget wie auf der vollständigen Referenz.
Gleiche Splits und Masken für feste und neu abgestimmte Konfiguration;
keine Auswahl anhand der Testergebnisse. Kein Nachweis optimaler
Konfigurationen für alle Bedingungen.

Paketversionen, konkreten Checkpoint samt Prüfsumme, Konfigurationen und
Seeds vor dem Hauptversuch fixieren; keine unkontrollierten Updates.
Dies ist eine beschlossene Absicherung, noch keine ausgeführte
technische Prüfung.

**Weiterhin offen vor dem Hauptversuch:** endgültige Datenwahl,
Splitanteile, Wiederholungen, Tuningbudget,
Regel für vollständig maskierte Trainingsspalten sowie Modellzugang,
Nutzungsbedingungen und technischer Pilot. Keine Modelle ausgeführt.

Die nachfolgenden Datenaudits bleiben gültig; ältere Statustabellen
beziehen sich teilweise auf die frühere Zusatzmerkmalfassung.

### Vertiefte Dateneignungsprüfung

Lokale Dateien mit Python 3.12.10 und Standardbibliothek vollständig
eingelesen; numerische Werte für den Duplikatvergleich als Zahlen
normalisiert. WDBC ohne ID/Ziel, übrige Daten ohne Zielvariable geprüft.
Keine Modelle ausgeführt, keine Rohdaten verändert.

| Datensatz | Fehlende Werte / nichtendliche numerische Werte | Konstante Eingabespalten | Verschiedene Merkmalsvektoren | Zusätzliche Zeilen bei identischem X | Gruppen mit identischem X und widersprüchlichem Ziel |
|---|---|---|---:|---:|---:|
| WDBC | 0 / 0 | keine | 569 von 569 | 0 | 0 |
| Ionosphere | 0 / 0 | Spalte 2 | 350 von 351 | 1 | 0 |
| Spambase | 0 / 0 | keine | 4.207 von 4.601 | 394 | 3 (6 Zeilen) |
| QSAR | 0 / 0 | keine | 1.052 von 1.055 | 3 | 0 |
| Credit-G | 0 / 0 in den numerischen Spalten | keine | 1.000 von 1.000 | 0 | 0 |

„Zusätzliche Zeilen“ bedeutet n minus Anzahl verschiedener
Merkmalsvektoren, nicht Anzahl aller betroffenen Zeilen.
Bei Spambase gehören 577 Zeilen zu wiederholten X-Gruppen;
die größte Gruppe umfasst 69 Zeilen. 391 Zeilen sind zusätzliche
exakte (X,y)-Wiederholungen. Identisches X belegt keine identische
ursprüngliche E-Mail, weil die Merkmale komprimierte Beschreibungen sind.
Auch widersprüchliche Ziele bei identischem X sind nicht automatisch
Fehlbeschriftungen. Sie dürfen nicht anhand günstiger Modellresultate
bereinigt werden.

**Vorläufige Empfehlungen:**

- **WDBC:** stärkster unproblematischer Startkandidat der geprüften
  Dateien. 569 eindeutige IDs; ID ausschließen. Die Beschreibung
  [wdbc.names](../experiments/data/breast+cancer+wisconsin+diagnostic/wdbc.names)
  bezeichnet die Daten als mit allen Merkmalen linear separierbar.
  Hohe Ausgangsleistung ist deshalb plausibel, aber für die hier
  geplanten Modelle und Splits noch nicht gemessen. Keine Garantie
  unabhängiger Patienten allein aus eindeutigen IDs ableiten.
- **Ionosphere:** mit dokumentierter Behandlung des einen identischen
  (X,y)-Paars brauchbar. Spalte 2 nach Trainingsregel entfernen.
  [ionosphere.names](../experiments/data/ionosphere/ionosphere.names)
  beschreibt Radarerfassung und Autokorrelationsmerkmale. Zeitbezug
  innerhalb einer Merkmalsbeschreibung ist nicht automatisch ein
  Zeitreihen-Splitproblem zwischen Zeilen; Metadaten zur Unabhängigkeit
  der Beobachtungen reichen aber nicht für einen Beweis aus.
- **QSAR:** mit dokumentierter Behandlung der drei zusätzlichen
  identischen (X,y)-Zeilen brauchbar. Laut
  [UCI](https://archive.ics.uci.edu/dataset/254/qsar+biodegradation)
  handelt es sich um molekulare Deskriptoren von Chemikalien.
  Die lokale Datei liefert keine Molekülkennungen/Strukturen für eine
  Prüfung chemischer Familien. Aussagen auf neue chemische
  Strukturklassen sind damit nicht abgesichert.
- **Spambase:** nur bedingt als Hauptkandidat; zuerst Umgang mit vielen
  identischen X und drei widersprüchlichen Gruppen entscheiden.
  [spambase.DOCUMENTATION](../experiments/data/spambase/spambase.DOCUMENTATION)
  beschreibt zusätzlich personenspezifische Nicht-Spam-Indikatoren.
  Kein Nachweis eines allgemeinen Spamfilters auf unabhängigen
  Absendern oder künftigen Nachrichten.
- **Credit-G:** Daten strukturell unauffällig, aber 13 kategoriale
  Spalten. Bleibt Reserve außerhalb der rein numerischen Hauptauswahl.

**Mögliche spätere Vorgehensweisen, noch nicht beschlossen:**
Entweder identische Eingaben als zusammenbleibende Gruppen splitten
(dadurch Anpassung des stratifizierten Splitplans) oder eine
vorab begründete Bereinigungsregel festlegen. Bei Spambase ist bloßes
Entfernen gleicher (X,y)-Zeilen nicht ausreichend, um alle identischen
X über Splits zu vermeiden. Keine Bereinigung in diesem Durchgang.
Nahe Duplikate, versteckte Patienten-/Erfassungsgruppen und
Vortrainingsüberschneidungen wurden nicht geprüft.

**Versandfassung für das Betreuergespräch:** Das Exposé wurde von neun
auf sechs Seiten einschließlich Literatur gekürzt. Alle fünf lokalen
Datensätze sind mit Fall- und Merkmalszahlen genannt; die vier numerischen
Datensätze sind Hauptkandidaten, Credit-G bleibt wegen seiner 13
kategorialen Merkmale Reserve. Die Tabelle verlinkt auf die UCI-Quellen;
die Zahlen beruhen auf der lokalen Strukturprüfung.
Detailformeln, genaue Aggregationsregeln, Seed-Organisation und der
ausführliche technische Arbeitsplan wurden aus dem Exposé entfernt;
die bisherigen Planungsnotizen unten bleiben erhalten.
Forschungsfragen, Quellenbezüge und zentrale Schutzmaßnahmen gegen
Datenlecks wurden beibehalten. Zugang, Nutzungsbedingungen und Pilot
sind ausdrücklich nach dem Betreuergespräch vorgesehen.
Die folgende Checkliste dokumentiert teilweise den ausführlicheren
Planungsstand, nicht den Wortlaut der gekürzten Versandfassung.

[Exposé](./Expose.tex) und [Gliederung](./Gliederung.tex) verbinden eine
breitere kritische Literaturanalyse mit einer empirischen
Anschlussuntersuchung. Dieser Status ersetzt die teilweise überholten
Empfehlungen in den historischen Notizen weiter unten.
**Erledigt bedeutet hier: im Entwurf konkretisiert und abgeglichen,
nicht: Experiment bereits durchgeführt.**

### Durchgang durch die offenen Kritikpunkte

| Prüfpunkt aus der früheren Bewertung | Status | Umsetzung bzw. verbleibende Aufgabe |
|---|---|---|
| Motivation konkret belegen, Benchmarkumfang und Übertragbarkeit begrenzen | Im Text erledigt | KI/LLM-Einstieg bleibt auf Wunsch erhalten; Überleitung zu Tabellen und TabPFN mit Nature belegt. Benchmarkbefund nicht auf spätere TFMs verallgemeinert. |
| TabPFN-Funktionsweise und ursprünglichen Robustheitsbefund korrekt beschreiben | Im Text erledigt | Synthetisches Vortraining, Kontextnutzung und richtige Quelle B.3.2/Abb. 9 bleiben erhalten. Historische Benchmarkdetails werden im Exposé nicht unnötig wiederholt. |
| Neue Literatur berücksichtigen statt eine Forschungslücke vorauszusetzen | Kernabgleich erledigt; Synthese offen | Nature, Hu/Ghelichi, Zhao et al. und Liu et al. berücksichtigt; keine Erstmaligkeitsbehauptung. Vergleich unten dokumentiert; vollständige Konzeptmatrix und Rechercheprotokoll stehen noch aus. |
| Entwicklerbericht, Publikationsstatus und Unabhängigkeit unterscheiden | Im Text erledigt | Quellenstatus und Unabhängigkeit als getrennte Kriterien; Methode und Benchmark nicht als kausaler Mechanismusnachweis behandelt. |
| Erkenntnisgewinn deutlicher benennen | Im Text erledigt | Literatursynthese plus Quantifizierung der Leistungsänderungen und ihrer datensatzübergreifenden Konsistenz statt bloßem Modellranking. Umfang noch mit Betreuer abzustimmen. |
| FF1 abgrenzen und mit FF2 verbinden | Im Text erledigt | Methoden, Einsatzmöglichkeiten und Aussagekraft der Evaluationen; breiter Literaturteil bleibt bewusst erhalten. FF1 in beiden Dokumenten gleichlautend geschärft. Frühere Empfehlung zur ausschließlichen Robustheitsfokussierung wird nicht übernommen. |
| Robustheit operationalisieren | Im Text erledigt | Leistungsänderung unter genau der festgelegten Intervention; keine allgemeine Sicherheits- oder Robustheitsgarantie. |
| Optionalen Laufzeitbenchmark entfernen | Erledigt | Laufzeit und Speicher nur Teil der Machbarkeitsprüfung. |
| Recherche nachvollziehbar eingrenzen | Plan konkretisiert; Durchführung offen | Vorwärts-/Rückwärtssuche, Volltextzugang, Sprachen, auswertbarer Methoden-/Anwendungsbezug, Versionsbehandlung und Suchschluss beschrieben. Tatsächliche Suchläufe und Ausschlüsse müssen dokumentiert werden. |
| Verschiedene Arten von Rauschen unterscheiden | Im Text erledigt | Zusatzmerkmale, Messrauschen, fehlende Werte und Label-Rauschen getrennt; Spaltenreihenfolge nicht mit Wertepermutation verwechselt. |
| PFN-Grundlage einbeziehen | Erledigt | Vorhandene PFN-Primärquelle zitiert und im Literaturvorgehen berücksichtigt. |
| Datensatztabelle mit etwa vier Kandidaten | Offen | IDs/Versionen, Umfang, Klassen, Missing Values, Lizenz und Beobachtungsstruktur tatsächlich prüfen. Keine unbestätigten Kandidaten als fest ausgewählt ausgeben. |
| Zeit-/Gruppenabhängigkeiten bei zufälligen Splits | Auswahlregel festgelegt; Prüfung offen | Bekannte zeitliche/gruppierte Daten und wiederholte Einheiten ausgeschlossen; Dokumentation je Kandidat prüfen. Ungeklärte Abhängigkeit ist keine bestätigte Unabhängigkeit. |
| Vorverarbeitung für Missing Values und Konstanten | Im Text festgelegt | Nur anhand von Training: leere/konstante Spalten entfernen, verbleibende Missing Values mit Trainingsmedian ersetzen; vor Zusatzmerkmal-Erzeugung. |
| Splitanteile und Klassengrößen | Offen | Im Pilot prüfen und vor Hauptversuch festschreiben; keine willkürlichen Anteile als geprüft darstellen. |
| Verhältnis statt Anteil definieren, Rundung und Nesting klären | Im Text erledigt | Zusatzspalten/Originalspalten, Aufrundung und realisiertes Verhältnis; höhere Stufen enthalten niedrigere. |
| Spaltenreihenfolge als zusätzliche Zufallsquelle kontrollieren | Im Text konkretisiert | Pro Konstruktion eine Reihenfolge aller maximalen Spalten; kleinere Stufen verwenden die eingeschränkte Reihenfolge. Keine neue unabhängige Umsortierung pro Stufe. |
| Split-, Konstruktions- und Modellzufall trennen | Im Text konkretisiert; Anzahlen offen | Getrennte Seeds; Modell-Seed je gepaartem Stufenvergleich konstant; Wiederholungszahlen nach Pilot. |
| LightGBM je Stufe neu trainieren, Konfiguration einfrieren | Im Text erledigt | Neu trainieren mit erweiterter Matrix; Tuning nur auf unverändertem Training/Validierung. Kein Testzugriff für Tuning. |
| LightGBM-Suchraum, Budget und konkreter TabPFN-Checkpoint | Offen | Paket/API, Hardware und Machbarkeit prüfen, anschließend vor Hauptversuch festlegen. |
| Balanced Accuracy begründen, Log-Loss korrekt einordnen | Im Text erledigt | Gleichgewichtung der Klassen; keine automatische Vergleichbarkeit der Datensätze. Log-Loss bewertet Wahrscheinlichkeitsausgaben, nicht ausschließlich Kalibrierung. |
| Gepaarte Änderungen und deren Richtung definieren | Im Text erledigt | Referenzdifferenzen für beide Metriken und Modellkontrast definiert; Prozentpunkte statt relativer Prozentänderung bei Balanced Accuracy. |
| Streuung und Unsicherheit methodisch festlegen | Deskriptiver Plan festgelegt | Konstruktionen innerhalb Split, dann Splitmittel; Einzelwerte, Standardabweichung und Spannweite getrennt zeigen. Keine Konfidenzintervalle oder Signifikanztests versprechen. Wiederholungen nicht als neue Datensätze zählen. |
| „Vergleichbar robust“ ohne Toleranz vermeiden | Im Text erledigt | Keine Gleichwertigkeitsbehauptung; kleine Differenzen numerisch berichten. Richtung und Größe je Datensatz statt nur Gesamtmittelwert. |
| Grenzen und Kausalität kenntlich machen | Im Text erledigt | Keine Architektur-/Priorattribution, keine allgemeine Modellfamilienrangfolge und kein Versionsfortschrittsnachweis ohne entsprechende Vergleiche. |
| Arbeits- und Zeitplan ergänzen | Phasenplan ergänzt; Termine offen | Arbeitsschritte und Abhängigkeiten beschrieben. Kalendarische Planung braucht tatsächlichen Bearbeitungszeitraum/Abgabetermin. |
| Autor und Datum | Teilweise offen | Datum vorhanden; Autorname und mögliche formale Lehrstuhlvorgaben nicht mit geratenen Angaben ergänzt. |
| Technischen Pilot durchführen | Offen, ausdrücklich nächster Schritt | In diesem Durchgang keine Installation, Modellfreigabe, Datenübertragung oder Modellläufe. Vorbereitung siehe unten. |
| Wiederholungen und Gliederung abgleichen | Im Text erledigt | FF1 synchronisiert, FF2 erhalten; Grenzen dort erläutert, wo sie zur Interpretation nötig sind. Kein Kapitel zur Versionschronik oder zusätzlicher XAI-Benchmark. |

Die Methodenfestlegungen zu Vorverarbeitung und deskriptiver Auswertung
wurden vom Nutzer in diesem Durchgang bestätigt. Sie sind
**eigene Designentscheidungen**, keine behaupteten Ergebnisse der Papers.

### Geprüfter Kernvergleich für den experimentellen Bezug

Die folgenden Angaben beruhen auf den relevanten Methoden- und
Ergebnispassagen, nicht auf einer behaupteten vollständigen
Literaturabdeckung.

| Primärquelle / Fundstelle | Modell und Aufgabe | Eingriff und berichteter Befund | Abgrenzung zur BA |
|---|---|---|---|
| [Ursprüngliches TabPFN](../literature/02_TabPFN_Kernmodelle/3_TabPFN_A.pdf), Anhang B.3.2, Abb. 9 | Damaliges TabPFN und u. a. LightGBM; eingeschränkte Auswahl binärer Klassifikationsaufgaben | Permutierte Spaltenkopien; ROC-AUC sinkt bei TabPFN, LightGBM bleibt relativ stabil | Historischer Anschluss, kein identischer Versionsvergleich im geplanten BA-Experiment |
| [Nature / TabPFNv2](../literature/02_TabPFN_Kernmodelle/13_Accurate%20predictions%20on%20small%20data%20with%20a%20tabular%20foundation%20model.pdf), Abb. 5a und zugehöriger Text | TabPFNv2 und Baselines; Klassifikation/Regression | Durchmischte Zusatzmerkmale; aggregierte normalisierte ROC-AUC/negative RMSE; berichtet vergleichsweise robuste Leistung | Reale Daten und Zusatzmerkmale bereits untersucht; kein Erstmaligkeitsanspruch |
| [Hu und Ghelichi](../literature/04_Merkmalszahl_und_Selektion/8_Noise%20Immunity.pdf), Abschnitt 3.2.1, Anhang A | Spezieller TabPFNv2-Checkpoint; synthetische binäre Klassifikation | 2 informative Merkmale, insgesamt 4 bis 512 Spalten durch Zufallsmerkmale; stabile ROC-AUC; 1 Merkmal pro Gruppe, 1 Schätzer, kein Feature-Shuffling | Synthetische Daten und spezielle Konfiguration, nicht ungeprüft auf Standardensemble oder v3.5 übertragen |
| [Zhao et al.](../literature/04_Merkmalszahl_und_Selektion/Architecture_Alignment_with_Sparse_Priors_2609.36883v1.pdf), Abschnitt 2, Anhang C.1 | Unter anderem TabPFNv2/v3; 42 reale OpenML-Regressionsdatensätze | Verhältnis 0 bis 7; ganze Kopien gemeinsam nach Zeilen permutiert, getrennt für Kontext/Query; 5 Konstruktionen bei festem Split; u. a. geringe R²-Verluste für TabPFN | Engste methodische Referenz; BA mit Klassifikation/v3.5/LightGBM und einzeln permutierten Kopien. Das lokal namenlose PDF wurde über Titel und Autoren identifiziert. |
| [Liu et al.](../literature/05_Weitere_Robustheit/10_Repeated%20Measurement.pdf), Abschnitt 3.2, Tabelle 16 | Unter anderem TabPFN-v3.5; Regression mit wiederholten Messungen | Zusätzliche unabhängige Koordinaten verstärken bei v3.5 den Wiederholungsmessungs-Nachteil in diesem Setup nicht entsprechend | Verhältnis Expanded/Single, kein direkter Nachweis allgemeiner Robustheit gegenüber Zusatzmerkmalen |

### Priorität bis zum Betreuergespräch

Auf Nutzerwunsch werden Modellzugang, Checkpoint-/Lizenzprüfung,
technischer Pilot und endgültige Laufkonfiguration **bis nach dem
Betreuergespräch zurückgestellt**. Zuerst wird geklärt, ob Fragestellung
und Umfang so vereinbart werden können. Diese Prüfungen sind keine
Voraussetzung für dieses Gespräch, bleiben aber vor der Durchführung
erforderlich. Es werden bis dahin keine Modelle installiert oder geladen.

### Lokaler Datenbestand: erste Strukturprüfung

Die fünf vorhandenen Datensätze wurden anhand der lokalen Dateien auf
Zeilen, Spalten und Klassenhäufigkeiten geprüft; das ist noch keine
vollständige Eignungs-, Lizenz- oder Abhängigkeitsprüfung.

| Datensatz | Beobachtungen | Merkmale ohne Ziel/ID | Klassenhäufigkeiten | Vorläufige Einordnung |
|---|---:|---:|---|---|
| [Breast Cancer Diagnostic](../experiments/data/breast+cancer+wisconsin+diagnostic/wdbc.data) | 569 | 30 | B: 357, M: 212 | Numerischer Kandidat; erste Spalte ist ID und muss ausgeschlossen werden. |
| [Ionosphere](../experiments/data/ionosphere/ionosphere.data) | 351 | 34 | g: 225, b: 126 | Numerischer Kandidat; zweite Eingabespalte ist in der gesamten Datei konstant. Entfernen weiterhin nach Trainingsregel. |
| [Spambase](../experiments/data/spambase/spambase.data) | 4.601 | 57 | 0: 2.788, 1: 1.813 | Numerischer Kandidat; mögliche Duplikate/Abhängigkeiten noch prüfen. |
| [QSAR Biodegradation](../experiments/data/biodeg.csv) | 1.055 | 41 | NRB: 699, RB: 356 | Numerischer Kandidat; semikolongetrennt, keine Kopfzeile. |
| [Credit-G](../experiments/data/credit_g.arff) | 1.000 | 20 | good: 700, bad: 300 | 7 numerische und 13 kategoriale Eingabespalten; passt nicht ohne zusätzliche Kodierungsentscheidung zum derzeit rein numerischen Design. Als Reserve behalten. |

Die vier numerischen Dateien haben konsistente Feldzahlen und in der
einfachen Textprüfung keine leeren Felder oder Marker `?`, `NA`, `NaN`.
Das ersetzt keine spätere vollständige Validierung.
Alle fünf Aufgaben sind binär. Vier numerische Hauptkandidaten plus
Credit-G als Reserve erfordern keine Erweiterung des bisherigen
Versuchsdesigns; ein endgültiger Beschluss ist damit nicht vorweggenommen.

### Nach dem Betreuergespräch: Pilot vorbereiten, nicht den Hauptversuch starten

1. Verwendete Python-Umgebung, verfügbare Hardware und Paketkompatibilität
   erfassen; anschließend offiziellen TabPFN-3.5-Zugang, Checkpoint und
   Lizenz anhand aktueller Anbieterunterlagen prüfen.
2. Einen numerischen Pilotdatensatz anhand derselben Auswahlkriterien wie
   später dokumentieren. Der vorhandene Datenlader allein ist keine
   Implementierung des geplanten Experiments.
3. Erst danach passende TabPFN-/LightGBM-Abhängigkeiten festlegen und in
   [requirements.txt](../requirements.txt) ergänzen. Dort stehen aktuell
   nur Datenverarbeitungs- und scikit-learn-Abhängigkeiten.
4. Beide Modelle bei unveränderter Eingabe und höchster geplanter Stufe
   laufen lassen; Datenformate, Wahrscheinlichkeiten, Klassenreihenfolge,
   Laufzeit und Speicherbedarf prüfen. Training/Test und
   Zusatzmerkmal-Erzeugung auf Trennung und Reproduzierbarkeit prüfen.
5. Aus gemessenen Laufzeiten den geplanten Umfang mit Datensätzen,
   Splits, Konstruktionen und Stufen kalkulieren. Erst dann endgültige
   Wiederholungszahlen und Tuningbudget abstimmen.

**Noch kein vollständiger Freigabestand:** Datensatztabelle,
Quellen-/Suchprotokoll, Pilot, endgültige Laufkonfiguration und
Betreuerabstimmung fehlen weiterhin. Sie lassen sich nicht durch
sprachliche Überarbeitung erledigen.

### Prüfung dieses Durchgangs

- Relevante Passagen aus Nature, Hu/Ghelichi, Zhao et al. und Liu et al.
  erneut in den lokalen Primär-PDFs gelesen.
- FF1 zwischen Exposé und Gliederung auf identischen Wortlaut geprüft.
- Beide PDFs erfolgreich neu kompiliert: Exposé 9 Seiten einschließlich
  Literatur, Gliederung 2 Seiten. Keine undefinierten Zitate oder
  überbreiten Textzeilen gemeldet; Stichproben der PDF-Seiten visuell
  geprüft.
- Die zunächst gesperrte Gliederungs-PDF ließ sich nach Schließen des
  Viewers aktualisieren.
- Keine Modellläufe durchgeführt, keine Machbarkeit behauptet.

---

## Historische Bewertung und frühere Satzüberarbeitungen

Die folgenden Passagen bleiben als Verlauf erhalten. Ihre Empfehlungen
und Statusangaben beziehen sich teilweise auf frühere Fassungen;
maßgeblich ist die aktuelle Übersicht oben.

**Ja, die Bachelorarbeit ergibt in dieser Ausrichtung Sinn. Aber nein: Das Exposé ist noch nicht vollständig fundiert und noch kein abschließend festgelegter Versuchsplan.** Als Gesprächsentwurf ist es brauchbar; vor dem Versand als verbindliches Forschungsvorhaben würde ich einige Punkte konkretisieren.

Ich habe [Expose.tex](./Expose.tex) vollständig gelesen, mit [Gliederung.tex](./Gliederung.tex) abgeglichen und zentrale Aussagen erneut in den Original-Papers geprüft. **Ich habe bei dieser Bewertung nichts verändert.**

## 1. Gesamturteil anhand der vier zentralen Kriterien

| Kriterium | Urteil |
|---|---|
| **Faktenbasis** | Der zentrale Ausgangspunkt ist belegt. Einige Aussagen sind noch zu allgemein; genaue Quellenstellen fehlen. |
| **Roter Faden und Forschungsfragen** | Grundsätzlich schlüssig. FF1 ist noch breiter als der praktische Schwerpunkt. |
| **Eigenleistung** | Eine nachvollziehbare empirische Erweiterung ist möglich. Eine bislang unbeantwortete Forschungslücke ist noch nicht nachgewiesen. |
| **Methodik und Machbarkeit** | Gute Grundidee, aber Datensätze, Wiederholungen, Vorverarbeitung und Auswertung sind noch nicht ausreichend festgelegt. Ein Modell-Pilot fehlt. |

**Die nächste Aufgabe ist nicht, wieder ein anderes Thema zu suchen. Sie ist, dieses Thema belastbar zu konkretisieren.**

---

## 2. Satzprüfung: Was trägt, was muss verbessert werden?

Nicht jeder Satz braucht eine Quelle: **Literaturbefunde brauchen Belege; deine geplanten Untersuchungsentscheidungen brauchen eine Begründung und eindeutige Definition.** Ich unterscheide deshalb zwischen belegten Tatsachen, eigenen Schlussfolgerungen und Planungsentscheidungen.

### A. Problemstellung und Motivation

**„Tabellarische Klassifikationsaufgaben unterscheiden sich in Umfang, Merkmalstypen, Klassenverteilung und Datenqualität.“**

**Bearbeitet: Der erste Satz wurde im Exposé ersetzt.**

Neue Formulierung:

> Grinsztajn et al. zeigen in kontrollierten Experimenten mit tabellarischen Klassifikationsdaten, dass das Hinzufügen uninformativer Merkmale den Leistungsabstand zwischen den untersuchten MLP-nahen Modellen und den übrigen Vergleichsverfahren vergrößert.

**Beleg:** Grinsztajn et al. (2022), Abschnitt 5.3. Der Quellenverweis steht unmittelbar hinter dem Satz im Exposé.

**Was wurde geändert und warum?** Der allgemeine Einstieg über Unterschiede zwischen Datensätzen wurde durch einen konkreten Literaturbefund ersetzt. Damit beginnt die Motivation direkt bei dem Datenfaktor, den die Arbeit untersuchen soll: zusätzlichen uninformativen Merkmalen. Die Formulierung benennt die untersuchte Modellgruppe ausdrücklich als „MLP-nahe Modelle“ und überträgt den Befund nicht pauschal auf alle neuronalen Modelle oder auf TabPFN-3.5.

**Welches Problem ist damit gelöst?** Der erste Satz ist jetzt themenspezifisch und unmittelbar belegt statt nur allgemein plausibel. Die spätere Wiederholung dieses Befunds wurde im Schritt zum Benchmark-Satz ebenfalls entfernt.

**„Für solche Aufgaben werden häufig baumbasierte Verfahren eingesetzt.“**

**Bearbeitet: Der Satz wurde gestrichen.**

**Was wurde geändert und warum?** Die allgemeine Aussage zur häufigen Nutzung baumbasierter Verfahren wurde entfernt. Sie beschreibt die Verbreitung dieser Verfahren, obwohl die Motivation der Arbeit deren Robustheit betrifft. Der anschließende Satz benennt bereits einen konkreten Benchmark mit baumbasierten und neuronalen Verfahren und übernimmt damit die nötige Einordnung.

**Welches Problem ist damit gelöst?** Die unbelegte Verbreitungsaussage entfällt, ohne dass für die Forschungsfrage notwendige Information verloren geht. Statt einen zusätzlichen Beleg für eine entbehrliche Aussage einzufügen, wird der Einstieg auf den relevanten Literaturbefund konzentriert.

**Die Aussagen zum Benchmark mit 45 Datensätzen und zum Hinzufügen irrelevanter Merkmale:**

**Bearbeitet: Der Benchmark-Satz wurde eingeordnet und der wiederholte Robustheitsbefund gestrichen.**

Neue Formulierung:

> Die Studie umfasst neben diesen Experimenten einen Benchmark baumbasierter und neuronaler Verfahren auf 45 kuratierten tabellarischen Datensätzen.

**Beleg:** Grinsztajn et al. (2022). Der Quellenverweis steht unmittelbar hinter dem Satz im Exposé.

**Was wurde geändert und warum?** Der Satz ordnet den zuvor genannten Robustheitsbefund in die Studie ein, ohne den ersten Satz erneut mit „Grinsztajn et al.“ zu beginnen. Die Zahl 45 bezeichnet den Benchmarkumfang; die Formulierung behauptet nicht, dass das Robustheitsexperiment auf sämtlichen 45 Datensätzen durchgeführt wurde. Der anschließende Satz über das Hinzufügen irrelevanter Merkmale wurde entfernt, weil der neue Einstieg diesen Befund bereits präziser beschreibt.

**Welches Problem ist damit gelöst?** Der Absatz wiederholt den Robustheitsbefund nicht mehr und enthält nicht mehr die zu breite Formulierung „die untersuchten neuronalen Modelle“. Abschnitt 5.3 des [Benchmark-Papers](../literature/03_Benchmarks_Baumverfahren/1_Benchmark.pdf) unterscheidet insbesondere MLP-nahe Modelle von FT-Transformern und Baumverfahren; diese Reichweite bleibt im ersten Satz erhalten. Der nächste Satz begrenzt weiterhin die Übertragbarkeit des Befunds.

**„Der Befund gilt für die getesteten Modelle und Versuchsbedingungen …“**

**Bearbeitet: Die Einschränkung wurde konkret auf TabPFN-3.5 bezogen.**

Neue Formulierung:

> Eine entsprechende Empfindlichkeit von TabPFN-3.5 gegenüber uninformativen Merkmalen lässt sich aus diesen Ergebnissen allein nicht ableiten.

**Was wurde geändert und warum?** Der bisherige Satz begrenzte den Befund allgemein auf die untersuchten Modelle und Versuchsbedingungen. Die neue Formulierung benennt stattdessen genau die Übertragung, die für diese Arbeit relevant ist: von den Ergebnissen der Benchmark-Studie auf TabPFN-3.5. Sie formuliert eine Grenze der Schlussfolgerung, keinen zusätzlichen empirischen Befund.

**Welches Problem ist damit gelöst?** Die Einschränkung bleibt erhalten, wird aber konkreter und stellt den Bezug zur eigenen Forschungsfrage her. Der Satz behauptet weder, dass TabPFN-3.5 dieselbe Schwäche besitzt, noch, dass es dagegen robust ist. Das muss anhand der einschlägigen Literatur und des geplanten Experiments untersucht werden.

**Die Beschreibung von TabPFN als vortrainiertem Transformer mit Trainingsbeispielen als Kontext:**

**Bearbeitet: Vortraining und Einsatz auf einem neuen Datensatz wurden ausdrücklich getrennt.**

Neue Formulierung:

> TabPFN wird vorab auf synthetisch erzeugten Klassifikationsaufgaben trainiert und nutzt bei der Vorhersage für einen neuen Datensatz dessen beschriftete Trainingsbeispiele als Kontext, ohne seine Modellparameter dabei durch Gradienten-Updates anzupassen.

**Beleg:** Hollmann et al. (2023), Abschnitte 2 und 3, insbesondere „Real-World Inference“ auf Seite 3. Der Quellenverweis steht unmittelbar hinter dem Satz im Exposé.

**Was wurde geändert und warum?** Der allgemein formulierte Gegensatz zu einem neu trainierten neuronalen Netz wurde durch die konkrete Funktionsweise ersetzt. Der Satz unterscheidet das Vortraining auf synthetischen Aufgaben vom Einsatz auf einem neuen Datensatz. Dabei wird ausdrücklich festgehalten, dass die beschrifteten Trainingsbeispiele genutzt werden, ohne die Modellparameter durch Gradienten-Updates anzupassen.

**Welches Problem ist damit gelöst?** Der Unterschied zwischen datensatzspezifischem Gradienten-Training und In-Context Learning wird verständlicher. Der Satz vermeidet die irreführende Verkürzung „TabPFN braucht keine Trainingsdaten“ oder „TabPFN wird nie trainiert“ und hat jetzt einen unmittelbar zugeordneten Primärbeleg. Er beschreibt den hier betrachteten Inferenzmodus, nicht mögliche zusätzliche Fine-Tuning-Verfahren.

**Die Aussagen zum ursprünglichen TabPFN-Paper und uninformativen Merkmalen:**

**Bearbeitet: Evaluationsumfang und Robustheitsvergleich wurden anhand des Originalpapers geprüft und konkretisiert.**

Neue Formulierung:

> Der Hauptbenchmark des ursprünglichen TabPFN-Papers umfasst 18 OpenML-CC18-Klassifikationsdatensätze mit höchstens 1 000 Trainingsbeispielen, 100 numerischen Merkmalen ohne fehlende Werte und zehn Klassen; ergänzend untersuchen die Autoren die Robustheit gegenüber uninformativen Merkmalen.

**Belege:** Hollmann et al. (2023), Abstract und Abschnitt 5 für den Hauptbenchmark; Anhang B.3.2 für die zusätzliche Robustheitsuntersuchung. Der zuvor eingetragene Verweis B.3.3 war falsch: Dieser Abschnitt behandelt Feature-Rotationen.

**Was wurde geändert und warum?** Die unbestimmte Beschreibung „vor allem auf kleinen Klassifikationsdatensätzen“ wurde durch den konkreten Umfang und die Auswahlbedingungen des Hauptbenchmarks ersetzt. Die ergänzende Robustheitsuntersuchung wird davon getrennt und erhält einen eigenen Abschnittsverweis.

**Welches Problem ist damit gelöst?** Der Leser kann die Reichweite der damaligen Evaluation nachvollziehen. Die Formulierung behauptet weder, dass das gesamte Paper nur diese 18 Datensätze untersucht, noch, dass die Ergebnisse uneingeschränkt für OpenML-CC18 oder TabPFN-3.5 gelten.

**Geprüfter Robustheitsvergleich:**

> Die Autoren erzeugen diese Zusatzmerkmale durch Kopieren vorhandener Spalten und zufälliges Permutieren ihrer Werte zwischen den Beobachtungen; dabei sinkt die Vorhersageleistung der damaligen TabPFN-Version, während die von LightGBM vergleichsweise konstant bleibt.

**Beleg:** Hollmann et al. (2023), Anhang B.3.2 auf den Seiten 18–19 und Abbildung 9 auf Seite 20. Die Abbildung zeigt ROC-AUC. Für diese Analyse schließen die Autoren Mehrklassenaufgaben und Datensätze mit mehr als 50 Merkmalen aus.

**Was wurde geändert und warum?** Der pauschale Vergleich „geringere Robustheit als LightGBM“ wurde durch den tatsächlich berichteten Leistungsverlauf und die Erzeugungsmethode der Zusatzmerkmale ersetzt. Außerdem wurde der falsche Abschnittsverweis korrigiert. Das Ergebnis ist auf dieses Experiment und die damalige TabPFN-Version beschränkt.

**Welches Problem ist damit gelöst?** Der zentrale Ausgangsbefund ist jetzt mit der richtigen Quelle und dem konkreten Eingriff nachvollziehbar beschrieben.

**Entscheidung umgesetzt:** Der Hauptversuch verwendet nun zufällig permutierte Kopien vorhandener numerischer Spalten statt standardnormalverteilter Zusatzmerkmale. Forschungsfragen, Zielsetzung, Abgrenzung und Versuchsplan wurden entsprechend angepasst. Die Permutation erhält die Werteverteilungen der kopierten Spalten, garantiert aber keine vollständige statistische Unabhängigkeit.

**Begründung und Durchführung:** Die Erzeugungsmethode schließt direkt an Hollmann et al. (Anhang B.3.2) an. Trainings-, Validierungs- und Testdaten werden getrennt permutiert; Zielwerte werden nicht zur Auswahl der Zusatzspalten verwendet. Die Quellspalten werden in zufälligen Durchläufen ausgewählt, jede Kopie erhält eine eigene Permutation und höhere Störmerkmal-Stufen enthalten die Kopien der niedrigeren Stufen. Beide Modelle erhalten dieselben Eingabedaten.

**Grenze des Beitrags:** Es handelt sich um eine an die Vorarbeit angelehnte empirische Erweiterung, nicht um eine exakte Replikation. Ohne identischen Vergleich mit der ursprünglichen TabPFN-Version kann keine Verbesserung von TabPFN-3.5 gegenüber dieser Version nachgewiesen werden. Eine zusätzliche Analyse mit normalverteilten Merkmalen ist derzeit nicht Bestandteil des Hauptversuchs.

**Die Aussagen zu TabPFN-3.5 und größeren Merkmalszahlen:**

**Bearbeitet: Methodische Änderung und Evaluation wurden getrennt formuliert und einzeln belegt.**

Neue Formulierung:

> Der technische Bericht zu TabPFN-3.5 beschreibt eine Anpassung des synthetischen Priors, durch die realistischere Trainingsaufgaben mit großen Merkmalszahlen erzeugt werden sollen.
>
> In der hochdimensionalen Teilgruppe des Benchmarks BeyondArena berichten die Autoren bessere Ergebnisse als für TabPFN-3.
>
> Aus diesem Benchmarkvergleich allein lässt sich jedoch nicht ableiten, welchen Anteil die Prioränderung an der berichteten Verbesserung hat.

**Belege:** Abschnitt 3.3 des [TabPFN-3.5-Berichts](../literature/02_TabPFN_Kernmodelle/5_TabPFN_3.5.pdf) für die Prioränderung; Abschnitt 2.2 für den Vergleich in der hochdimensionalen Teilgruppe von BeyondArena. Beide Stellen wurden im Original-PDF geprüft.

**Was wurde geändert und warum?** Die zuvor zusammengefassten Aussagen wurden in eine beschriebene methodische Änderung und ein berichtetes Evaluationsergebnis aufgeteilt. Die Zielsetzung „realistischere Trainingsaufgaben“ ist als Absicht der Entwickler formuliert, nicht als unabhängig nachgewiesene Eigenschaft. Das Evaluationsergebnis benennt Benchmark, Teilgruppe und Vergleichsmodell.

**Welches Problem ist damit gelöst?** Jede Tatsachenaussage hat jetzt einen konkreten Quellenverweis. Außerdem wird nicht suggeriert, dass der Benchmarkvergleich allein die Prioränderung als Ursache der Verbesserung nachweist. Die Einschränkung bezieht sich auf diesen Vergleich und behauptet nicht, der Bericht enthalte grundsätzlich keine Ablationsanalysen.

**Die Einordnung als Entwicklerbericht:**

Richtig. Daraus folgt nicht, dass die Ergebnisse unbrauchbar sind; sie müssen lediglich entsprechend eingeordnet werden.

**„Eine größere unterstützte Merkmalszahl beantwortet … nicht, wie empfindlich TabPFN-3.5 … reagiert.“**

Das ist eine sinnvolle eigene Schlussfolgerung: **Hohe Dimensionalität ist nicht gleichbedeutend mit kontrolliert hinzugefügter Irrelevanz.** Genau hier liegt deine fachliche Motivation.

**„Im geprüften Bericht wird kein isoliertes Experiment … berichtet.“**

**An die beschlossene Methode angepasst:** Im Exposé wird jetzt ausdrücklich ein Experiment zur schrittweisen Zugabe zufällig permutierter Kopien vorhandener Merkmale genannt, nicht mehr ein Experiment mit „unabhängigen Störmerkmalen“.

Als auf diesen Bericht beschränkte Aussage vertretbar. Sie darf aber nicht in „Das wurde noch nie untersucht“ umgewandelt werden. Der ergänzende Literaturabgleich außerhalb dieses Berichts ist weiterhin offen.

**„Ob neuere Studien diese Frage bereits untersuchen, wird … nachgeprüft.“**

Ehrlich, aber für eine abschließende Exposé-Fassung noch eine offene Aufgabe. Die Recherche sollte vor dem verbindlichen Versand zumindest gezielt durchgeführt sein.

**Die abschließenden Sätze zur praktischen Frage und zum Verzicht auf einen allgemeinen Modellsieger:**

Schlüssig. Allerdings wiederholen sie teilweise die späteren Abschnitte. Das Exposé kann hier kürzer werden.

### B. Zielsetzung und Eigenleistung

Die Sätze zur Literaturanalyse, zum kontrollierten Experiment und zur Veränderung gegenüber der Ausgangsbedingung passen zusammen.

**„Der praktische Beitrag besteht in einer reproduzierbaren Untersuchung …“**

Als Ziel richtig. Aber **Reproduzierbarkeit und mehrere Datensätze allein machen noch keine unterscheidbare Forschungsleistung**. Deutlicher sollte werden, welcher Erkenntnisgewinn daraus entsteht:

> Die Untersuchung quantifiziert, wie sich die Leistung einer aktuellen TabPFN-Version unter einer kontrollierten Erhöhung irrelevanter Eingabedimensionen verändert und wie sich diese Veränderung von LightGBM unterscheidet.

Die Sätze „kein neuer Algorithmus“, „keine Aussagen über alle Baumverfahren“ und „Forschungslücke noch zu prüfen“ sind wissenschaftlich sauber. Sie werden im Dokument allerdings mehrfach wiederholt. **Einmal präzise abgrenzen reicht.**

### C. Forschungsfragen

**Übergeordnete Frage:** Sie funktioniert, ist aber lang und überschneidet sich stark mit FF2. Das ist kein Ausschlusskriterium.

**FF1:** Inhaltlich sinnvoll, derzeit aber noch sehr weit:

> „Welche relevanten methodischen Änderungen und adressierten Herausforderungen …“

Was gilt als „relevant“? Der Literaturteil könnte sonst wieder Architektur, Multimodalität, Regression und sämtliche Versionsänderungen sammeln.

Ich würde ihn auf **Modellverständnis, Merkmalsverarbeitung, Prior und relevante Evaluationen** beschränken. FF1 ist der begründende Literaturteil, keine zweite umfassende Forschungsarbeit.

**FF2:** Das ist die stärkste Frage im Exposé. Sie ist konkret und empirisch beantwortbar.

Allerdings muss „Robustheit“ operationalisiert werden: Hier meinst du **die Veränderung der Vorhersageleistung nach dem kontrollierten Eingriff**, nicht allgemeine Sicherheit, adversariale Robustheit oder Robustheit gegen jeden Datenfehler.

Du brauchst dafür keine künstlichen Hypothesen oder beliebigen Schwellen. Wenn du später „vergleichbar robust“ behaupten willst, musst du aber festlegen, welche Unterschiede praktisch relevant wären.

### D. Abgrenzung und roter Faden

Die Ausschlüsse von XAI, Regression, umfassendem Modellbenchmark und vollständiger Versionsgeschichte sind passend.

**„Die genaue Version … von TabPFN-3.5 wird geprüft.“**

Unglücklich formuliert: Die Modellgeneration ist bereits gewählt. Offen sind **Checkpoint, Paketversion, Zugang, Lizenz und technische Ausführbarkeit**, nicht erneut die grundsätzliche Wahl der Modellversion.

**Optionale Laufzeitmessung:**

Für diesen Fokus entbehrlich. Ich würde sie vorerst aus dem geplanten Ergebnisumfang herauslassen. Laufzeit und Speicherbedarf musst du ohnehin im Pilot prüfen, aber daraus muss keine zusätzliche Forschungsfrage entstehen.

**Der rote Faden:**

Er ist logisch. Eine Grenze muss ausdrücklich bleiben:

> Das Experiment untersucht das Verhalten von TabPFN-3.5. Es kann nicht nachweisen, welche einzelne Architektur- oder Prioränderung dieses Verhalten verursacht.

Dafür wären kontrollierte Ablationen oder zusätzliche Versionsvergleiche nötig. Die Literaturanalyse erklärt den Hintergrund; sie ersetzt diese Nachweise nicht.

### E. Literaturanalyse

Die fokussierte Recherche statt eines vollständigen systematischen Reviews passt zur empirischen Bachelorarbeit.

Die genannten Suchbegriffe sind brauchbar. Es fehlen noch:

- Vorwärts- und Rückwärtssuche anhand der zentralen Papers;
- klare Kriterien für relevante Treffer;
- eine dokumentierte Unterscheidung zwischen **hinzugefügtem Feature-Rauschen**, Messrauschen und Label-Rauschen;
- PFN-Grundlagenliteratur für den theoretischen Teil.

Du hast das [PFN-Grundlagenpaper](../literature/01_Grundlagen_KI_PFN/2_Bayesian_Inference.pdf) bereits. Es sollte im Literaturvorgehen berücksichtigt werden, wenn Bayesianische Priors und PFNs in der Gliederung stehen.

### F. Experimenteller Vergleich

Hier liegen die größten offenen Punkte.

| Aussage im Entwurf | Bewertung und nötige Präzisierung |
|---|---|
| Etwa vier numerische Datensätze | Plausibler BA-Umfang. Vier ist aber eine Umfangsentscheidung, keine wissenschaftlich magische Mindestzahl. Konkrete Kandidaten fehlen. |
| Numerische Eingaben zur Vermeidung unterschiedlicher Kategorie-Kodierungen | Sinnvolle Eingrenzung. Umgang mit fehlenden Werten und konstanten Spalten bleibt offen. |
| Identische stratifizierte Splits | Richtig für passende Aufgaben. Zeit- und gruppenabhängige Datensätze nicht einfach zufällig aufteilen. |
| Zufällig permutierte Kopien vorhandener Merkmale | Erzeugungsmethode beschlossen und an das ursprüngliche TabPFN-Paper angelehnt. Werteverteilungen bleiben erhalten; vollständige Unabhängigkeit ist nicht garantiert. |
| Stufen 0, 0,5, 1 und 2 pro ursprünglicher Spalte | Gut messbar, aber das ist ein **Verhältnis zur ursprünglichen Spaltenzahl**, nicht der Anteil am Gesamtdatensatz. Bei Verhältnis 2 sind zwei Drittel aller Spalten Zusatzmerkmale. |
| Gleiche Merkmale, Seeds und Splits für beide Modelle | Wichtig und richtig. Zusätzlich sollten höhere Stufen möglichst dieselben Rauschspalten der niedrigeren Stufen enthalten. |
| „Mehrere wiederholte Seeds“ | Zu unbestimmt. Datensplit, Rauscherzeugung und Modellzufall sind unterschiedliche Zufallsquellen. |
| Konfigurationen einfrieren | Sinnvoll für die Frage nach Empfindlichkeit einer festen Konfiguration. **LightGBM muss trotzdem auf jeder veränderten Trainingsmatrix neu trainiert werden.** |
| LightGBM-Tuning auf unveränderten Trainingsdaten | Vertretbar, aber die Frage betrifft dann feste Konfigurationen, nicht die jeweils optimal abstimmbare Leistung jeder Stufe. Validierung und Test müssen strikt getrennt bleiben. |
| Balanced Accuracy als primäre Kennzahl | Vertretbar. Sie macht verschieden schwierige Datensätze aber nicht automatisch vergleichbar. Veränderungen innerhalb eines Datensatzes bleiben zentral. |
| Log-Loss nur bei „vergleichbaren“ Wahrscheinlichkeiten | Zu vage. Unterschiedliche Kalibrierung ist nicht automatisch ein Hindernis für den Vergleich; die Kennzahl bewertet gerade die Wahrscheinlichkeitsvorhersagen. |
| Streuung und Unsicherheit berichten | Richtig, aber das Verfahren fehlt. Wiederholte Splits desselben Datensatzes sind keine unabhängigen neuen Datensätze. |
| Endliche Stichproben können zufällige Korrelationen enthalten | Sehr guter und wichtiger Einschränkungssatz. |
| Keine Verallgemeinerung auf alle Domänen und Baumverfahren | Richtig. |

Die Kapitelstruktur passt. **Ein einfacher Zeit- und Arbeitsplan sowie Angaben zu Autor und Datum fehlen noch** – je nach Exposé-Vorgaben des Lehrstuhls.

---

## 3. Wo genau entsteht der Wert deiner BA?

Der stärkste Beitrag wäre:

> **Eine an frühere Robustheitsexperimente angelehnte empirische Untersuchung, die Leistungsänderungen von TabPFN-3.5 durch hinzugefügte, zufällig permutierte Kopien vorhandener Merkmale auf mehreren Datensätzen im Vergleich zu LightGBM quantifiziert.**

Das ist mehr als ein allgemeines Modellranking, weil du einen Eingabefaktor gezielt veränderst.

**Aber:** „Neue Modellversion getestet“ allein wäre eine dünne Begründung. Der Wert entsteht aus der Verbindung von relevantem Vorbefund, sauberem Design und aussagekräftiger Auswertung. Auch das Ergebnis „kaum Verschlechterung“ kann wertvoll sein – sofern die Unsicherheit klein genug ist. **Kein signifikanter Unterschied ist nicht automatisch ein Nachweis gleicher Robustheit.**

---

## 4. Deine nächsten Schritte vor dem Versand

### 1. Die konkrete Literaturüberschneidung prüfen

Erstelle eine kleine Übersicht zu den direkt relevanten Arbeiten:

**Modellversion – Art der Zusatzmerkmale – Versuchsbedingungen – Leistungsmetrik – Ergebnis.**

Ziel: Nicht beweisen, dass niemand etwas Ähnliches gemacht hat, sondern deinen Beitrag gegenüber vorhandenen Studien sauber abgrenzen.

### 2. Einen technischen Pilot durchführen

Aktuell enthält [experiments](../experiments) einen Datenlader; TabPFN und LightGBM sind in [requirements.txt](../requirements.txt) noch nicht enthalten.

Der Pilot sollte zeigen:

- konkreter TabPFN-3.5-Checkpoint verfügbar und nutzbar;
- beide Modelle liefern Vorhersagen;
- Ausgangsbedingung und höchste Rauschstufe laufen;
- Zeit und Speicherbedarf sind tragbar.

**Noch keinen großen Benchmark starten.**

### 3. Eine Datensatztabelle festlegen

Für etwa vier Kandidaten: Datenquelle/ID, Beobachtungen, Merkmale, Klassen, Missing Values, Lizenz und Ausschluss möglicher Zeit-/Gruppenstruktur.

### 4. Den Versuchsplan auf einer Seite konkretisieren

Festlegen:

- Splitverfahren und Wiederholungszahlen;
- getrennte Seeds für Splits und Rauschmerkmale;
- Vorverarbeitung ausschließlich anhand der Trainingsdaten;
- Modellkonfiguration und eventuelles Validierungsbudget;
- primäre Metrik;
- Leistungsänderung je Modell und deren gepaarter Vergleich;
- Verfahren zur Darstellung von Streuung und Unsicherheit.

### 5. Erst danach den Text finalisieren

Die überbreite Benchmark-Aussage präzisieren, zentrale Seiten-/Abschnittsbelege ergänzen, Wiederholungen kürzen und Gliederung sowie Zeitplan abstimmen.

## Meine Empfehlung zum Versand

**Als Diskussionsentwurf kannst du es deinem Professor bereits schicken**, wenn du klar sagst, dass du die Richtung abstimmen möchtest und Datensätze sowie Pilot noch offen sind.

**Als weitgehend festgelegtes Exposé würde ich es erst nach Literaturabgleich und kleinem Pilot versenden.** Du brauchst davor keine fertigen Ergebnisse. Du solltest aber zeigen können: *Die Frage ist sinnvoll abgegrenzt, das Modell ist tatsächlich nutzbar und der geplante Umfang ist realistisch.*

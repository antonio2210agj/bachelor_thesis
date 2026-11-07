# Abschlussabgleich: Missing Data und der Modellvergleich

Stand: 6. November 2026.

## Ergebnis und Reichweite

Die vorhandene Literatur und der gezielte externe Abschlussabgleich tragen eine
Bachelorarbeit zum Einfluss der Missing-Data-Behandlung auf den Leistungsvergleich
zwischen TabPFN-3.5 und LightGBM. Eine weitere breite Suchrunde ist vor der
Formulierung der Arbeitsfrage nicht erforderlich.

Der Beitrag ist eine kontrollierte empirische Anschlussuntersuchung, keine neue
Imputationsmethode und kein nachgewiesener weltweit erstmaliger Versuch.
Steigende Fehlraten, interne Verarbeitung versus externe Imputation und
Missing-Indikatoren sind bereits etablierte Untersuchungsbausteine.

In den geprueften Primaerquellen wurde der kombinierte Vergleich von
TabPFN-3.5 und LightGBM unter gleichen MCAR-Masken, mehreren Fehlraten und
unterschiedlichen Behandlungen mit nachgelagerter Klassifikationsbewertung
nicht gefunden. Das ist eine Aussage ueber den geprueften Quellenbestand,
kein Vollstaendigkeits- oder Neuheitsbeweis.

Expose, Titel und Gliederung wurden durch diesen Abgleich nicht umgestellt.
Im anschliessenden Umsetzungsschritt wurden sie auf den Missing-Data-Fokus
ausgerichtet; die folgenden Empfehlungen dokumentieren den Abgleichstand.
Der technische Zugang zu TabPFN-3.5 und die Ausfuehrbarkeit des Versuchs
sind noch nicht durch einen Modellpilot nachgewiesen.

## Vorgehen und Quellenstatus

- Titel und Abstracts der aktuell 15 lokalen PDFs wurden im vorausgehenden
  Screening gelesen; fuer relevante Arbeiten wurden Methoden, Ergebnisse
  und Anhaenge gezielt geprueft.
- Im Abschlussabgleich wurden die Volltexte von Perez-Lebel et al.,
  Ye et al. und der aktuellen TabImpute-Fassung heruntergeladen und
  lokal gezielt gelesen. Die Pruefkopien waren keine neu in das
  Repository aufgenommenen PDFs.
- Fuer die beiden arXiv-PDFs TIME und TabImpute wurde keine explizite
  Weiterverteilungslizenz festgestellt. Daher werden sie hier ueber
  ihre arXiv-Quellen verlinkt, nicht als PDFs mitcommittet. Das gilt
  auch fuer die lokale anonyme Review-Fassung von TabImpute.
- Direkte Websuchen dienten der Kandidatenfindung, nicht als Beleg.
  Teilweise enthielten die generierten Suchzusammenfassungen Aussagen
  ueber LightGBM-Vergleiche, die die geprueften Primaertexte nicht
  bestaetigen. Diese Aussagen wurden nicht uebernommen.
- Die Verlagsseite von Perez-Lebel war nicht direkt zugaenglich;
  geprueft wurde das als Author Accepted Manuscript gekennzeichnete
  arXiv-PDF. OpenReview-Treffer mit Zugriffshuerden wurden nicht als
  bestaetigte weitere Studien verwendet.
- Dies ist ein begrenzter Abschlussabgleich, keine systematische
  Literaturuebersicht mit vollstaendigem Datenbankexport. Google Scholar
  wurde dabei nicht direkt bedient.

## Wichtigste Vorarbeiten und konkrete Abgrenzung

### 1. Perez-Lebel et al.: methodische Hauptquelle

**Benchmarking missing-values approaches for predictive models on health
databases** (2022).

- [Publikations-DOI](https://doi.org/10.1093/gigascience/giac013)
- [Geprueftes Author Accepted Manuscript, arXiv v1](https://arxiv.org/pdf/2202.10580v1)
- Stellen: S. 2-3, Single Imputation, Adding the mask, MIA und Tabelle 1;
  S. 4-6, Results und Discussion.

Das Paper untersucht 13 Vorhersageaufgaben (10 Klassifikation, 3 Regression)
aus vier Gesundheitsdatenbanken mit natuerlich vorhandenen Fehlwerten.
Verglichen werden unter anderem Mittelwert- und Median-Imputation,
KNN und iterative Imputation, jeweils teilweise mit Missing-Indikatoren,
sowie interne Baumverarbeitung (MIA). Bagging bildet einen weiteren Faktor.
Trainingsteilgroessen sind 2.500, 10.000, 25.000 und 100.000 Faelle.
Imputationsstatistiken werden auf dem Training gelernt und auf Testdaten angewandt.

Die MIA-Implementierung stammt aus scikit-learns Histogram-Gradient-Boosting;
das Paper ist kein TabPFN- oder direkter LightGBM-Vergleich.
Die Methodenbeschriftung nennt HistGradientBoostingRegressor. Daraus
keine konkrete LightGBM-Konfiguration ableiten.

Wichtige Befunde:

- Missing-Indikatoren verbessern die Vorhersage in den untersuchten
  Gesundheitsdaten gegenueber den entsprechenden Imputationen ohne Indikator.
- Aufwendige bedingte Imputation ist nicht durchgaengig besser als
  konstante Imputation.
- Interne Verarbeitung bietet einen guenstigen Leistungs-Kosten-Kompromiss.
  Bagged iterative Imputation mit Indikatoren erzielt den besten gesamten
  durchschnittlichen Rang; deshalb nicht behaupten, interne Verarbeitung
  gewinne ausnahmslos gegen jede Imputationspipeline.

**Bedeutung fuer die BA:** Der Vergleich von Behandlungsstrategien ist bereits
etabliert. Die Quelle begruendet das Design und die Beruecksichtigung von
Missing-Indikatoren. Die Ergebnisse zu natuerlicher, informativer Missingness
lassen sich nicht als Garantie auf kuenstliches MCAR uebertragen.

### 2. TIME: naechste TabPFN-Vorhersagevorarbeit

[TIME: TabPFN-Integrated Multimodal Engine for Robust Tabular-Image Learning](https://arxiv.org/abs/2506.00813v1).

- [arXiv v1](https://arxiv.org/abs/2506.00813v1)
- Stellen: Abschnitte 3.1, 4.1, 4.3 und 4.4; Tabellen 1-2, Abbildungen 4-6.

TabPFNv2 dient als eingefrorener Tabellenencoder innerhalb eines
Bild-Tabellen-Modells. Drei medizinische Datensaetze werden mit ihren
natuerlichen Fehlwerten sowie nach Median-Imputation ausgewertet.
Zusaetzlich wird auf dem Adoption-Datensatz zufaellig mit Fehlraten
von 10, 20, 30, 40 und 50 Prozent maskiert.

Die Fehlratenanalyse wertet TIME-Fusionsvarianten aus, nicht entsprechende
vollstaendige Fehlratenkurven aller Baselines. Die gelesene Beschreibung
legt die betroffenen Partitionen der kuenstlichen Maskierung nicht eindeutig
genug fuer eine exakte Replikation fest. Die Bildmodalitaet liefert
zusaetzliche Information und kann Tabellenverlust kompensieren.

**Bedeutung fuer die BA:** Weder kuenstliche Fehlraten noch der Vergleich
mit Median-Imputation sind bei TabPFN grundsaetzlich neu. Der reine
TabPFN-3.5-versus-LightGBM-Pipelinevergleich ist eine andere Untersuchung.

### 3. TabImpute: aktuelle Fassung statt Versionsvermischung

- Eine lokal gepruefte anonyme Review-Fassung trug den Titel
  *TabImpute: Accurate and Fast Zero-Shot Missing-Data Imputation with a
  Pre-Trained Transformer* und berichtete 42 Datensaetze sowie 13 Muster,
  davon 11 MNAR. Ihre Angaben und Auswertung sind nicht mit der aktuellen
  Fassung gleichzusetzen; eine Weiterverteilungslizenz wurde nicht
  festgestellt, deshalb wird die lokale PDF nicht mitcommittet.
  Abschnitt 4 der Fassung misst min-max-normalisierte Rekonstruktions-RMSE.
- [Gepruefte aktuelle Fassung, arXiv v6 vom 28. August 2026](https://arxiv.org/pdf/2510.02625v6):
  *One Pipeline, Many Transformers: Pattern-Specific Imputation Specialists
  for Tabular Missing Data*, Feitelberg et al.
  Stellen: Abstract, Abschnitt 3.1.2, Abschnitt 4, Anhang A.2.

Die aktuelle Fassung untersucht 42 numerische OpenML-Datensaetze mit
11 Mustern (MCAR, MAR, 9 MNAR). Sie bewertet die Rekonstruktion fehlender
Eintraege anhand spaltenstandardisierter RMSE und R2, inklusive
fehlratenspezifischer und musterspezifischer Ergebnisse.

Im geprueften Experimentteil findet sich kein entsprechender
TabPFN-3.5-versus-LightGBM-Downstream-Klassifikationsvergleich.
Rekonstruktionsguete ist nicht gleich Klassifikationsguete.
Die Ergebnisse und Musterzahlen beider Fassungen nicht zusammenfuehren.

**Bedeutung fuer die BA:** Pflichtkontext fuer Imputation mit Foundation
Models, aber kein Anlass, TabImpute zwingend selbst zu implementieren.

### 4. Ye et al.: keine weitere direkte Missingness-Studie

**A Closer Look at TabPFN v2: Understanding Its Strengths and Extending
Its Capabilities**.

- [Geprueftes arXiv v2 vom 11. Juni 2025](https://arxiv.org/pdf/2502.17361v2)
- Stellen: Abstract, Abschnitt 4, Abschnitte 5-7, Anhang D.

Untersucht werden breitere Benchmarks, Attributtokens, Feature-Extraktion,
Skalierung sowie Divide-and-Conquer-Erweiterungen. Anhang D behandelt
unter anderem Fingerprint-/Polynomial-Features und Ensembling.

Die Volltextsuche und Pruefung der Evaluation ergeben keinen kontrollierten
Missingness-Behandlungsversuch, der die BA-Frage beantwortet.
Die Vorabvermutung, hier koennte eine direkte Missing-Data-Ueberschneidung
liegen, hat sich fuer diese Fassung nicht bestaetigt.

**Bedeutung fuer die BA:** Hintergrundliteratur, nicht weiterer Pflichtkern
fuer FF2.

### 5. Kernberichte und weitere lokale Imputationsarbeiten

- [Nature/TabPFNv2](../02_TabPFN_Kernmodelle/13_Accurate%20predictions%20on%20small%20data%20with%20a%20tabular%20foundation%20model.pdf):
  Missingness im synthetischen Vortraining; Missing-Indikator in der
  Zellverarbeitung. Abbildung 5b ist eine Subgruppenanalyse nach vorhandenen
  Fehlwerten, kein isolierter Fehlraten-Behandlungsversuch.
- [TabPFN-3.5](../02_TabPFN_Kernmodelle/5_TabPFN_3.5.pdf):
  Abschnitt 3.1 und Abbildung 8 bewahren den NaN/Inf-Indikator vor der
  Ersetzung durch den Trainingsspaltenmittelwert.
- [Sepin, Multiple Imputation](../07_Missing_Data_und_Imputation/stats-09-00038.pdf):
  Abschnitte 2.2 und 3 behandeln fehlendes kontinuierliches Y bei
  vollstaendigem X, MCAR/MAR, ungefaehr 50 Prozent Fehlwerte.
  Ziel ist Mittelwertschaetzung mit Bias, Standardfehler und Coverage;
  kein fehlendes-X-Klassifikationsvergleich mit LightGBM.
- [Effective Handling](../07_Missing_Data_und_Imputation/information-14-00092.pdf):
  Abschnitte 3-4 verbinden SVM-Imputation, zweite Klassifikationsstufe
  und Merkmalsauswahl auf PIMA. Eine Leistungsverbesserung ist dadurch
  nicht isoliert der Imputation zuzuordnen. Das fold-interne Lernen aller
  Verarbeitungsschritte ist in der Beschreibung nicht eindeutig dokumentiert.
  Ergaenzende Quelle, keine tragende Methodenvorlage.

## Offizielle LightGBM-Dokumentation

[Advanced Topics: Missing Value Handle](https://lightgbm.readthedocs.io/en/latest/Advanced-Topics.html#missing-value-handle),
abgerufen am 6. November 2026:

- Missing-Value-Verarbeitung ist standardmaessig aktiviert (`use_missing`).
- NaN repraesentiert standardmaessig fehlende Werte.
- `zero_as_missing=false` ist der Standard: Nullwerte werden nicht
  pauschal als fehlend behandelt.

Damit ist eine LightGBM-Pipeline mit NaN-Eingaben dokumentarisch begruendet.
Es handelt sich nicht um dieselbe interne Behandlung wie bei TabPFN-3.5.
Fuer den Versuch Version und Einstellungen festhalten und dense NaN-Masken
verwenden, ohne echte Nullwerte umzudeuten. Ein Laufzeittest steht noch aus.

## Beitrag und moegliche Arbeitsfrage

Arbeitsfrage:

> Wie beeinflusst die Behandlung fehlender Merkmalswerte den Leistungsvergleich
> zwischen TabPFN-3.5 und LightGBM auf ausgewaehlten numerischen Datensaetzen?

Moegliche empirische Konkretisierung, noch nicht beschlossen:

> Wie veraendern sich die Klassifikationsleistung und der Leistungsabstand
> zwischen TabPFN-3.5 und LightGBM bei steigenden Anteilen MCAR-fehlender
> Merkmalswerte unter modellinterner Verarbeitung und vorgeschalteter
> Median-Imputation?

Moeglicher Beitragsabsatz:

> Die Arbeit uebertraegt etablierte Vergleiche von Missing-Data-Behandlungen
> auf einen kontrollierten Vergleich von TabPFN-3.5 und LightGBM.
> Auf ausgewaehlten numerischen Datensaetzen werden identische Splits
> und Missingness-Masken verwendet, um Leistungsveraenderungen und die
> Abhaengigkeit des Modellvergleichs von der Behandlung fehlender
> Eingabewerte zu untersuchen. Die Ergebnisse werden als empirische
> Anschlussuntersuchung innerhalb des gewaehlten Designs eingeordnet,
> nicht als Entwicklung einer neuen Imputationsmethode oder allgemeiner
> Nachweis der Ueberlegenheit eines Modells.

## Methodische Entscheidungen vor der endgueltigen Formulierung

**Anschliessend am 6. November 2026 vom Nutzer beschlossen:** separate
Maskierung von Training, Validierung und Test mit derselben Wahrscheinlichkeit;
0/10/30/50 Prozent; interne Verarbeitung versus Median als Kern,
Median plus Indikatoren als kleine Zusatzanalyse. Diese Entscheidungen
sind nun im Expose und in der Gliederung aufgenommen. Weitere technische
Details und ein Modellpilot bleiben offen.

Keine neue breite Recherche, sondern vier Designentscheidungen:

1. **Partitionen:** Welche Werte werden maskiert? Empfehlung fuer einen
   einfachen Hauptversuch: Training, Validierung und Test unter derselben
   Fehlrate, separat und unabhaengig maskiert. Kein unbeabsichtigter
   Missingness-Shift. Das ist eine Empfehlung, keine bereits getroffene Wahl.
2. **Behandlungen:** Interne Verarbeitung und Median-Imputation als Kern.
   Median plus Missing-Indikatoren als kleine, fachlich begruendete
   Sensitivitaetsanalyse erwaegen. Nicht viele weitere Imputer aufnehmen.
3. **Fehlraten und Wiederholungen:** Vollstaendige Referenz, wenige vorab
   definierte Fehlraten, mehrere gepaarte Masken/Splits. Beispielsweise
   0/10/30/50 Prozent als Arbeitsvorschlag, nicht als literaturbedingt
   zwingende Schwellen.
4. **Auswertung:** Balanced Accuracy und Log-Loss, pro Datensatz absolute
   Werte, Veraenderung gegenueber der vollstaendigen Referenz und
   Leistungsabstand beider Modelle. Keine Gleichwertigkeit aus fehlender
   Signifikanz ableiten; Ergebnisse nicht als allgemeines Modellranking
   auf alle Tabellen ausdehnen.

Wichtig: Externe Median-Imputation entfernt die NaN-Information fuer
die interne TabPFN-Verarbeitung. Der Vergleich ist deshalb ein
Pipelinevergleich, keine isolierte Mittelwert-versus-Median-Ablation.
Zusaetzliche Indikatorspalten sind ebenfalls nicht identisch mit TabPFNs
internem Zellindikator. Unter MCAR ist die Maskierung unabhaengig von
Werten und Ziel; Verbesserungen durch Indikatoren nicht automatisch
mit der informativen Missingness realer Gesundheitsdaten begruenden.

Median und andere gelernte Statistiken nur aus beobachteten Trainingswerten
bestimmen. Labels nicht maskieren und nicht fuer die Imputation der
Vorhersageeingaben verwenden. Bei leeren Trainingsspalten eine explizite
Regel festlegen. Bekannte identische Eingaben beim Splitting beruecksichtigen.
Die vorhandenen vollstaendigen numerischen Daten sind als kontrollierte
Ausgangsbasis geeignet; MCAR repraesentiert nicht jede reale Unvollstaendigkeit.

## Literaturstruktur

Die bestehende Ablage ist passend:

- 01: KI/ICL/PFN-Grundlagen;
- 02: TabPFN-Kernmodelle, auch wenn sie Missingness behandeln;
- 03: Baum-/Benchmarkkontext;
- 04: Zusatzmerkmale und Selektion als Hintergrund zum alten Schwerpunkt;
- 07: Missing Data und Imputation;
- notes: zentrale Notizen und dieser Abschlussabgleich.

Keine neuen leeren Themenordner und keine doppelten PDFs erforderlich.
Ordner 07 ist inzwischen befuellt. Die nicht mehr vorhandenen Ordner 05/06
werden nicht neu erstellt; die verbliebenen Nummern bleiben fuer stabile Links.
Perez-Lebel waere bei einem spaeteren rechtlich zulaessigen PDF-Import
in Ordner 07 einzuordnen, Ye et al. in Ordner 02. Dieser Bericht enthaelt
bereits stabile externe Quellenlinks; ein PDF-Import ist kein Voraussetzung
fuer die Frageformulierung.

## Suchbegriffe nur fuer spaeter auftretende Detailfragen

Eine weitere Literaturbeschaffung ist aktuell keine Voraussetzung.
Falls bei Ausarbeitung oder Betreuerfeedback eine konkrete Luecke entsteht:

```text
"TabPFN" "missing values" "LightGBM"
"TabPFN" "missingness" "classification"
"TabPFN" "median imputation"
"missing value handling" prediction "missing indicators"
"MCAR" classification "native" imputation
"missingness shift" prediction
```

Nicht vorsorglich MAR/MNAR, XAI, weitere Modelle oder viele Imputer
in den Hauptversuch aufnehmen. Nach Festlegung der Frage folgt ein kleiner
technischer Pilot; gezielte Nachrecherche bleibt bei neuen Befunden erlaubt.
"Letzter Abgleich" bedeutet Ende der offenen Themenfindung, nicht ein
Verbot, spaeter notwendige Quellen fuer die Arbeit nachzutragen.

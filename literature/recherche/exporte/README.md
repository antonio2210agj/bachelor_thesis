# Zotero-Austausch für die Literaturrecherche

Zotero bleibt die Hauptbibliothek. Dieser Ordner dient dazu, Metadaten einer
konkreten Suche als RIS-Datei für den Abgleich mit dem Suchprotokoll bereitzustellen.

1. In Zotero unter „01 Suchtreffer“ die Datenbank und darunter für jede Suche
   eine eigene Untersammlung anlegen, zum Beispiel
   `Google Scholar` → `S1a TabPFN missing values`. Die zu dieser Suche
   tatsächlich erfassten Einträge zuordnen. Ein vorhandener Eintrag kann
   mehreren Sammlungen angehören.
2. Die Untersammlung per Rechtsklick exportieren und das Format **RIS** wählen.
   Falls Zotero entsprechende Optionen anbietet: Dateien und Notizen nicht
   mit exportieren. Keine Zugangsdaten oder privaten Notizen einfügen.
3. Die Datei im passenden Datenbank-Unterordner speichern, für Google Scholar
   unter `Google Scholar/`, zum Beispiel
   `Google Scholar/2026-11-25_S1a_Scholar_TabPFN_missing-values.ris`. Für
   jede Suche eine eigene Datei verwenden. Für arXiv oder Scopus bei Bedarf
   jeweils einen eigenen Unterordner anlegen.
4. Im Chat Datum, Datenbank, exakte Suchanfrage, Sortierung und Filter,
   angezeigte Trefferzahl, tatsächlich gesichteten Bereich sowie den Namen
   der RIS-Datei mitteilen. Google-Scholar-Trefferzahlen als ungefähre Angaben
   kennzeichnen. Zusätzlich mitteilen, ob die Datei alle gesichteten Treffer
   oder nur eine Auswahl enthält.
5. Nach der Titel-/Abstractsichtung die tatsächlichen Entscheidungen und
   Zahlen mitteilen. Der RIS-Export allein zeigt weder sicher, was gesichtet
   wurde, noch die Gründe einer Auswahl. Die Assistenz ergänzt das
   [Suchprotokoll](../../notes/Suchprotokoll.md) nur anhand belegter Angaben;
   ungeklärte Angaben bleiben offen.

RIS-Dateien in diesem Ordner und seinen Unterordnern werden durch `.gitignore`
**nicht mit Git synchronisiert**. Sie können private Pfade oder Notizen
enthalten und sind nur auf dem Rechner verfügbar, auf dem sie gespeichert
wurden. Das Suchprotokoll selbst wird wie gewohnt mit Git synchronisiert.

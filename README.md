# Bernhard Topp: *Ganne Nettels* / *Otto Veihwann* (1884)

Erste digitale Ausgabe eines ostfälischen Buches: Bernhard Topp, *Otto Veihwann, en
Tiedtmäreken*, mit der Vorgeschichte *Ganne Nettels*, Osterwieck am Harz: A. W. Zickfeldt,
1884. Diplomatische Transkription aller 109 Textseiten, neu aus der Fraktur erkannt und Seite
für Seite von Hand gegen die Scans geprüft, dazu ein Satz in [Typst](https://typst.app).

*English: the first digital edition of an 1884 book in Eastphalian Low German. A diplomatic
transcription of all 109 text pages, re-OCRed from the Fraktur and checked by hand against the
scans page by page, with a Typst setting in two forms: a reading text and a line-for-line
diplomatic one.*

Bernhard Topp (1815–1904) war Arzt und Kreisphysikus in Hornburg. Der Band enthält eine
Werbungs- und Erbgeschichte um einen Grenzstein zwischen zwei Höfen und, ab dem Zwischentitel
auf S. 73, ein „Tiedtmäreken“, ein Zeitmärchen: Reichsgründungspolitik im Fabelbild.

## Die Sprache

Das Buch ist Ostfälisch, Niederdeutsch aus dem Harzvorland, **keine Schreibvariante des
Hochdeutschen**. `hei`, `ſek`, `dat`, `ok`, `wärren`, `Mäken` stehen so im Druck und bleiben so
stehen. Eine Rechtschreibprüfung oder ein Sprachmodell, das auf Hochdeutsch trainiert ist, macht
daraus `bei`, `sich`, `Mädchen` und zerstört den Text. Eine feste Rechtschreibung hatte das
Ostfälische nicht; das Buch schreibt dasselbe Wort mitunter auf zwei Arten, und auch das bleibt.

## Was hier liegt

| | |
|---|---|
| `transcription/pNNN.txt` | **Die Edition.** Eine Datei je Druckseite, Zeilen und Trennstriche wie gedruckt, langes `ſ` wie gedruckt. `front_0000.txt` ist der Umschlag, `p114.txt` der Rückdeckel; leere Druckseiten sind leere Dateien. |
| `transcription/anmerkungen.tsv` | Die Anmerkungen zu einzelnen Stellen: Druckschäden, zweifelhafte Buchstaben und wie sie entschieden wurden, Berichtigungen, Formen, die nur einmal vorkommen. |
| `editionsrichtlinien.md` | Was die Transkription vom Druck unterscheidet und warum. Jede Abweichung vom Druck steht dort, sonst ist sie ein Fehler. |
| `struktur.tsv` | Titel, Kapitel und Impressum: welche Zeile welcher Seite eine Überschrift ist. |
| `lesetext.py` | Leitet aus den Seiten die beiden Zwischendateien ab. Nur Python-Standardbibliothek. |
| `lesetext/absaetze.tsv` | Der Text in Absätzen, Trennstriche aufgelöst, für den Lesesatz. |
| `lesetext/zeilen.tsv` | Der Text Zeile für Zeile, für den diplomatischen Satz. |
| `lesetext/lesetext.txt` | Der ganze Text in Absätzen, als reiner Text zum Lesen. |
| `book.typ` | Der Satz in Typst. |

Die Dateien in `lesetext/` sind erzeugt, liegen aber bei, damit zum Setzen Typst allein
genügt und zum Lesen gar nichts. Wer an `transcription/` etwas ändert, erzeugt sie mit `python3 lesetext.py` neu.

## Setzen

Mit Typst 0.15.1 (auf diese Version ist der Satz abgestimmt):

```sh
typst compile --root . book.typ                                       # Lesefassung
typst compile --root . --input satz=diplomatisch book.typ topp-diplomatisch.pdf
```

Weitere Schalter, beliebig kombinierbar:

- `--input s=rund` setzt `ſ` als `s`.
- `--input schrift=fraktur` setzt in UnifrakturMaguntia statt Libertinus Serif. Die Schrift ist
  frei (SIL Open Font License, bei Google Fonts) und muss installiert sein oder mit
  `--font-path` angegeben werden.

Der diplomatische Satz setzt jede Druckseite auf eine Seite, jede Druckzeile auf eine Zeile, mit
der Seitenzahl des Drucks im Kopf. Läuft eine Seite über, bricht er mit einer Meldung ab.

## Die Vorlage

Die Scans liegen im Internet Archive: <https://archive.org/details/otto-veihwann>
(JPEG 2000, 300 dpi). Druckseite *p* ist im JP2-Archiv das Bild mit dem Index *p* + 1, also
S. 10 = `…_0011.jp2`. Jede Stelle lässt sich so am Bild nachprüfen.

Erkannt wurde mit Tesseract und dem Fraktur-Modell `frak2021`, **alle Wörterbücher
abgeschaltet**, damit die Erkennung nichts ins Hochdeutsche „verbessert“. Das Ergebnis war ein
Entwurf; jede Seite ist danach von Hand gegen den Scan gelesen und in einem zweiten, unabhängigen
Durchgang Buchstabe für Buchstabe kontrolliert worden. Zweifelhafte Buchstaben wurden am Bild
gemessen, nicht geraten. Nichts im Text ist automatisch korrigiert.

## Lizenz

Der Text von 1884 ist gemeinfrei. Die Transkription, die Anmerkungen, die Editionsrichtlinien und
der Satz (`book.typ`, `lesetext.py`) stehen unter
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de), siehe `LICENSE`.

Zitiervorschlag:

> Bernhard Topp: Ganne Nettels / Otto Veihwann. Osterwieck 1884. Diplomatische Transkription,
> just-a-book-archivist, 2026. <https://github.com/just-a-book-archivist/1884-topp-otto-veihwann>

## Zu diesem Repository

Dies ist die abgeschlossene Fassung einer Edition, kein gepflegtes Softwareprojekt. Werkzeugstände
sind absichtlich festgehalten, das Ziel ist Reproduzierbarkeit, nicht Aktualität. Meldungen über
„veraltete“ Versionen werden kommentarlos geschlossen. Jede Änderung am Text muss gegen den Scan
geprüft sein; wer eine Stelle für falsch hält, nenne Druckseite, Zeile und was im Scan steht.

Mehr zum Projekt: <https://buchmigrationen.neocities.org/html/1884-topp-otto-veihwann.html>

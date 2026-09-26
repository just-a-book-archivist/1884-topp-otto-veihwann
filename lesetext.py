#!/usr/bin/env python3
"""Lesetext: aus den Seitendateien einen Text in Absaetzen machen.

transcription/pNNN.txt ist diplomatisch: Zeilen, Seiten und Trennstriche wie
gedruckt. Das bleibt die Quelle. Dieses Skript leitet daraus einen Lesetext ab,
Absatz fuer Absatz, und ist damit die Stufe zwischen der Transkription und
einem spaeteren Satz in Typst -- regenerierbar wie ocr-out/, nie von Hand
bearbeitet. Korrigiert wird weiter in transcription/.

    python3 lesetext.py            # -> lesetext/absaetze.tsv, lesetext.txt, pruefen.txt
    python3 lesetext.py --s        # lang-s als s
    python3 lesetext.py --seiten   # Seitenwechsel als [N] in den Text

Was es liest, steht schon in den Seiten (editionsrichtlinien.md):

- vier Leerzeichen Einzug: ein Absatz beginnt
- sechs: Zeile eines eingerueckten Einschubs (Brief), zehn: Absatz darin
- acht: Verszeile oder abgesetzte Zeile; Leerzeile trennt Strophen;
  zwoelf: eingerueckte Verszeile, der Mehreinzug bleibt erhalten
- Zeile ohne Einzug: der laufende Absatz geht weiter, auch ueber die Seite

Ueberschriften, Titel und Impressum kann es nicht erkennen, sie stehen ohne
Einzug wie Text. Die sagt ihm struktur.tsv, von Hand gepflegt: Seite, Art und
der Wortlaut der Zeile, der genau so in der Seite stehen muss.

Trennstriche am Zeilenende:

- geht es klein weiter, wird zusammengezogen (Beſchimpunge-/n -> ...);
- geht es gross weiter, bleibt der Bindestrich (Peiter-/Fiſcher);
- steht das Wort mit Bindestrich mitten in einer Zeile irgendwo im Buch,
  bleibt er ebenfalls, und die Stelle kommt nach pruefen.txt;
- folgt ein alleinstehendes „un“/„oder“ (Laſt- un Luſt-Pere), bleibt der
  Strich mit Leerzeichen danach.

lesetext/absaetze.tsv hat je Block eine Zeile mit Art und Fundstelle
(Seite:Zeile von/bis) -- das ist die Form, die Typst mit csv(delimiter: "\\t")
liest. lesetext.txt ist dasselbe zum Lesen.

lesetext/zeilen.tsv ist die diplomatische Seite davon: jede gedruckte Zeile
eine Zeile, mit Seite, Zeilennummer, Art, Einzug in Leerzeichen und der Spalte
„voll“ -- ja, wenn der Absatz in der naechsten Zeile weitergeht, die Zeile im
Druck also bis zum rechten Rand reicht und im Satz auf Breite gebracht wird.
Leerzeilen stehen mit drin, Trennstriche bleiben. Reines stdlib.
"""

import argparse
import csv
import re
from pathlib import Path

TRANS = Path("transcription")
STRUKTUR = Path("struktur.tsv")
OUT = Path("lesetext")
FIRST, LAST = 3, 112           # Druckseiten mit Erzaehltext
WORD = r"[A-Za-zÄÖÜäöüßſ]+"
CONJ = {"un", "und", "oder", "as"}


def fold(word: str) -> str:
    return word.lower().replace("ſ", "s")


def load_struktur() -> dict[tuple[str, str], str]:
    with STRUKTUR.open(encoding="utf-8") as handle:
        return {(row["seite"], row["text"]): row["art"]
                for row in csv.DictReader(handle, delimiter="\t")}


def pages() -> list[tuple[str, list[str]]]:
    result = []
    for number in range(FIRST, LAST + 1):
        path = TRANS / f"p{number:03d}.txt"
        lines = path.read_text(encoding="utf-8").split("\n")
        if any(line.strip() for line in lines):
            result.append((path.stem, lines))
    return result


def hyphenated_midline(all_pages) -> set[str]:
    """Woerter, die irgendwo mitten in einer Zeile mit Bindestrich stehen."""
    found = set()
    for _, lines in all_pages:
        for line in lines:
            for match in re.finditer(rf"({WORD})-({WORD})", line):
                if match.end() < len(line.rstrip()):
                    found.add(fold(match.group(0)))
    return found


def classify(line: str) -> str:
    if not line.strip():
        return "leer"
    indent = len(line) - len(line.lstrip(" "))
    if indent == 10:
        return "brief-absatz"
    if indent >= 8:  # auch zwoelf: eingerueckte Verszeile (p054, p055)
        return "vers"
    if indent >= 6:
        return "brief"
    if indent >= 4:
        return "absatz"
    return "weiter"


class Block:
    def __init__(self, art, page, number, fortsetzung=False):
        self.art, self.start, self.end = art, (page, number), (page, number)
        self.fortsetzung = fortsetzung
        self.lines: list[tuple[str, int, str]] = []

    def add(self, page, number, text):
        self.lines.append((page, number, text))
        self.end = (page, number)


def join(block, attested, notes, seiten) -> str:
    """Zeilen eines Blocks zu einem Text, Trennstriche aufgeloest."""
    if block.art == "vers":
        return "\n".join(text for _, _, text in block.lines)
    out, previous_page = "", block.lines[0][0]
    for index, (page, number, text) in enumerate(block.lines):
        marker = f"[{int(page[1:])}] " if seiten and page != previous_page else ""
        previous_page = page
        if not out:
            out = text
            continue
        head = re.search(rf"({WORD})-$", out)
        tail = re.match(rf"({WORD})", text)
        if head and tail:
            first, second = head.group(1), tail.group(1)
            where = f"{page}:{number}"
            if fold(second) in CONJ:
                out += " " + marker + text
            elif second[0].isupper():
                out += marker + text
            elif fold(f"{first}-{second}") in attested:
                notes.append(f"{where}\tBindestrich behalten\t{first}-{second} "
                             f"steht so auch mitten in einer Zeile")
                out += marker + text
            else:
                out = out[:-1] + marker + text
        else:
            out += " " + marker + text
    return out


def write_zeilen(all_pages, struktur, long_s: bool) -> int:
    """lesetext/zeilen.tsv: die Seiten Zeile fuer Zeile, fuer den diplomatischen Satz."""
    flat = []  # (seite, zeile, art, einzug, text)
    for page, lines in all_pages:
        while lines and not lines[-1].strip():
            lines = lines[:-1]
        for number, line in enumerate(lines, 1):
            art = struktur.get((page, line.strip())) or classify(line)
            einzug = len(line) - len(line.lstrip(" ")) if line.strip() else 0
            text = line.strip()
            if long_s:
                text = text.replace("ſ", "s")
            flat.append([int(page[1:]), number, art, einzug, text])

    # voll: der Absatz laeuft in der naechsten Zeile weiter, auch ueber die Seite
    goes_on = {"absatz": {"weiter"}, "weiter": {"weiter"},
               "brief": {"brief"}, "brief-absatz": {"brief"}}
    rows = []
    for index, (seite, zeile, art, einzug, text) in enumerate(flat):
        following = flat[index + 1][2] if index + 1 < len(flat) else None
        voll = "ja" if following in goes_on.get(art, ()) else ""
        rows.append((seite, zeile, art, einzug, voll, text))

    OUT.mkdir(exist_ok=True)
    with (OUT / "zeilen.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["seite", "zeile", "art", "einzug", "voll", "text"])
        writer.writerows(rows)
    return len(rows)


def build(seiten: bool, long_s: bool) -> None:
    struktur = load_struktur()
    all_pages = pages()
    attested = hyphenated_midline(all_pages)
    blocks: list[Block] = []
    notes: list[str] = []
    seen_struktur = set()
    current = None

    for page, lines in all_pages:
        for number, line in enumerate(lines, 1):
            art = struktur.get((page, line.strip()))
            if art:
                seen_struktur.add((page, line.strip()))
                current = Block(art, page, number)
                current.add(page, number, line.strip())
                blocks.append(current)
                current = None
                continue
            kind = classify(line)
            # im Vers bleibt ein Einzug ueber acht Leerzeichen hinaus stehen
            text = line.rstrip()[8:] if kind == "vers" else line.strip()
            if kind == "leer":
                # Leerzeile schliesst Vers und Einschub; ein Absatz laeuft
                # weiter, bis ein Einzug den naechsten anfaengt
                if current and current.art in ("vers", "brief"):
                    current = None
                continue
            if kind == "vers":
                if not (current and current.art == "vers"):
                    current = Block("vers", page, number)
                    blocks.append(current)
            elif kind in ("absatz", "brief-absatz"):
                current = Block("brief" if kind == "brief-absatz" else "absatz",
                                page, number)
                blocks.append(current)
            elif kind == "brief":
                if not (current and current.art == "brief"):
                    current = Block("brief", page, number)
                    blocks.append(current)
            else:  # weiter
                if not current or current.art == "vers":
                    # nach einem Vers oder einer Ueberschrift ohne Einzug:
                    # der Satz laeuft weiter, der Druck zieht nicht ein
                    current = Block("absatz", page, number, fortsetzung=True)
                    blocks.append(current)
                    if not blocks[-2:-1] or blocks[-2].art != "vers":
                        notes.append(f"{page}:{number}\tAbsatz ohne Einzug\t{text[:50]}")
            current.add(page, number, text)

    for key in struktur:
        if key not in seen_struktur:
            notes.append(f"{key[0]}\tstruktur.tsv nicht gefunden\t{key[1]}")

    OUT.mkdir(exist_ok=True)
    rows = []
    for index, block in enumerate(blocks, 1):
        text = join(block, attested, notes, seiten)
        if long_s:
            text = text.replace("ſ", "s")
        rows.append((index, block.art, "ja" if block.fortsetzung else "",
                     f"{block.start[0]}:{block.start[1]}",
                     f"{block.end[0]}:{block.end[1]}", text))

    with (OUT / "absaetze.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["nr", "art", "fortsetzung", "von", "bis", "text"])
        for row in rows:
            writer.writerow(row[:5] + (row[5].replace("\n", " / "),))

    with (OUT / "lesetext.txt").open("w", encoding="utf-8") as handle:
        for _, art, fortsetzung, _, _, text in rows:
            if art in ("titel", "kapitel"):
                handle.write(f"\n\n{text}\n\n")
            elif art in ("untertitel", "unterkapitel"):
                handle.write(f"{text}\n\n")
            elif art == "vers":
                handle.write("".join(f"        {line}\n" for line in text.split("\n")) + "\n")
            elif art == "brief":
                handle.write(f"      {text}\n\n")
            elif art == "impressum":
                handle.write(f"\n\n{text}\n")
            else:
                handle.write(("" if fortsetzung else "    ") + text + "\n\n")

    (OUT / "pruefen.txt").write_text("\n".join(notes) + "\n", encoding="utf-8")
    zeilen = write_zeilen(all_pages, struktur, long_s)
    counts = {}
    for row in rows:
        counts[row[1]] = counts.get(row[1], 0) + 1
    print(f"{len(all_pages)} Seiten -> {len(rows)} Bloecke "
          f"({', '.join(f'{k} {v}' for k, v in sorted(counts.items()))}); "
          f"{len(notes)} Stellen in {OUT}/pruefen.txt; {zeilen} Zeilen in {OUT}/zeilen.tsv")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--s", action="store_true", help="lang-s als s ausgeben")
    parser.add_argument("--seiten", action="store_true",
                        help="Seitenwechsel als [N] in den Text setzen")
    args = parser.parse_args()
    build(args.seiten, args.s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

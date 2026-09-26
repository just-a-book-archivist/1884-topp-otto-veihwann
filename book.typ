// Bernhard Topp, Ganne Nettels / Otto Veihwann (Osterwieck 1884) — Satz.
//
// Der Text kommt nicht aus diesem Dokument, sondern aus lesetext/absaetze.tsv
// und lesetext/zeilen.tsv, die lesetext.py aus transcription/ erzeugt;
// korrigiert wird dort, nie hier. Dieses Dokument entscheidet nur über das
// Aussehen: Seite, Schrift, Absätze, Verse, Überschriften.
//
// Schalter, als --input an typst compile (im Arbeitsrepo über make build ARGS="…"):
//   s        lang (Standard) — ſ wie gedruckt;  rund — ſ als s
//   schrift  antiqua (Standard, Libertinus Serif);  fraktur — UnifrakturMaguntia
//   satz     lese (Standard) — Absätze aus lesetext/absaetze.tsv, neu umbrochen;
//            diplomatisch — aus lesetext/zeilen.tsv: jede Druckzeile eine Zeile,
//            jede Druckseite eine Seite, mit der Seitenzahl des Drucks

#let s-rund = sys.inputs.at("s", default: "lang") == "rund"
#let fraktur = sys.inputs.at("schrift", default: "antiqua") == "fraktur"
#let diplomatisch = sys.inputs.at("satz", default: "lese") == "diplomatisch"

#let zeilen = csv("/lesetext/absaetze.tsv", delimiter: "\t").slice(1)
#let text-von(roh) = if s-rund { roh.replace("ſ", "s") } else { roh }

#set document(title: "Ganne Nettels · Otto Veihwann", author: "Bernhard Topp")
#set page(
  paper: "a5",
  margin: (inside: 22mm, outside: 16mm, top: 20mm, bottom: 22mm),
  numbering: "— 1 —",
  number-align: center + top,
)
// Kein Wörterbuch für Ostfälisch: keine Silbentrennung, statt sie mit
// hochdeutschen Mustern falsch zu machen.
#set text(
  font: if fraktur { "UnifrakturMaguntia" } else { "Libertinus Serif" },
  size: 10.5pt,
  lang: "nds",
  hyphenate: false,
)
#set par(justify: true, leading: 0.62em, spacing: 0.62em,
         first-line-indent: 1.2em)

#let titel(t) = {
  pagebreak(weak: true)
  v(22%)
  align(center, text(size: 20pt, weight: "bold", t))
}
#let untertitel(t) = align(center, text(size: 12pt, style: "italic", t))
#let kapitel(t) = {
  v(1.6em, weak: true)
  align(center, text(size: 12pt, weight: "bold", t))
  v(0.8em)
}
#let unterkapitel(t) = { align(center, text(style: "italic", t)); v(0.8em) }

// Verse: eine Zeile je Druckzeile; ein Mehreinzug aus der Transkription
// (zwölf statt acht Leerzeichen) wird zu einem Einzug im Satz.
#let vers(t) = {
  v(0.5em)
  pad(left: 2.5em, for zeile in t.split(" / ") {
    let rest = zeile.trim(at: start)
    if rest.len() < zeile.len() { h(1.5em) }
    rest
    linebreak()
  })
  v(0.5em)
}

#let brief(t) = pad(left: 1.5em, right: 1.5em, text(size: 9.5pt, t))

// Diplomatischer Satz: die Druckseite ist die Einheit. Ein Einzug in
// Leerzeichen wird zu einem Einzug in em, eine Zeile, deren Absatz im Druck
// weitergeht („voll“), wird auf Breite gebracht, wie im Druck; Trennstriche
// stehen, wie sie stehen. Seitenhöhe und Zeilenabstand sind so gewählt, dass
// die vollste Seite (p026, 47 Zeilen samt Leerzeilen) auch in Fraktur passt;
// läuft eine über, bricht der Satz am Ende mit einer Meldung ab.
#let diplomatische-seiten() = {
  let zeilen = csv("/lesetext/zeilen.tsv", delimiter: "\t").slice(1)
  let seiten = (:)
  for z in zeilen {
    let s = z.at(0)
    if s not in seiten { seiten.insert(s, ()) }
    seiten.at(s).push(z)
  }
  set page(
    width: 148mm, height: 230mm,
    margin: (x: 12mm, top: 20mm, bottom: 14mm),
    // Kopf: die Druckseitenzahl, die auf dieser Seite als Metadatum steht.
    // counter(page) taugt dafür nicht: ein Update wirkt erst ab der nächsten
    // Seite, nach einer leeren Druckseite hinkte der Kopf eins hinterher.
    header: context {
      let hier = query(<druckseite>).filter(m => m.location().page() == here().page())
      if hier.len() > 0 { align(center, [— #hier.first().value —]) }
    },
  )
  set text(size: 10.5pt)
  set par(justify: false, leading: 0.7em, spacing: 0.7em, first-line-indent: 0pt)
  for (i, (seite, zs)) in seiten.pairs().enumerate() {
    if i > 0 { pagebreak() }
    [#metadata(int(seite)) <druckseite>]
    // zusammenhängende Zeilen eines Absatzes stehen in einem par, damit
    // linebreak(justify: true) die vollen Zeilen auf Breite bringen kann
    let laufend = ()
    for z in zs {
      let (_, _, art, einzug, voll, roh) = z
      let t = text-von(roh)
      if art in ("titel", "untertitel", "kapitel", "unterkapitel", "impressum") {
        align(center, if art in ("titel", "kapitel") { text(weight: "bold", t) }
                      else if art == "impressum" { text(size: 8pt, t) }
                      else { t })
      } else if art == "leer" {
        // Leerzeilen trennen in der Transkription Absätze und Verse
        // (editionsrichtlinien.md); gedruckt ist dort kein Abstand.
      } else {
        // Verse stehen im Druck etwa ein Viertel der Zeile weit eingerückt;
        // ein Mehreinzug (zwölf statt acht Leerzeichen) kommt dazu.
        let einzug = if art == "vers" { 27% + (int(einzug) - 8) * 0.3em }
                     else { int(einzug) * 0.3em }
        laufend.push(h(einzug) + t
                     + if voll == "ja" { linebreak(justify: true) })
        if voll != "ja" {
          par(laufend.join())
          laufend = ()
        }
      }
    }
    if laufend.len() > 0 { par(laufend.join()) }
  }
  // Eine Druckseite, eine Seite: bricht Typst irgendwo um, stimmt die Zahl
  // nicht mehr, und der Satz bricht hier ab, statt es still hinzunehmen.
  context {
    let gesetzt = counter(page).final().first()
    assert(gesetzt == seiten.len(),
      message: str(seiten.len()) + " Druckseiten, aber " + str(gesetzt)
        + " Seiten gesetzt: eine Seite läuft über.")
  }
}

#if diplomatisch { diplomatische-seiten() } else {
  for z in zeilen {
    let (nr, art, fortsetzung, von, bis, roh) = z
    let t = text-von(roh)
    if art == "titel" { titel(t) }
    else if art == "untertitel" { untertitel(t) }
    else if art == "kapitel" { kapitel(t) }
    else if art == "unterkapitel" { unterkapitel(t) }
    else if art == "vers" { vers(t) }
    else if art == "brief" { brief(t) }
    else if art == "impressum" {
      v(1fr)
      align(center, text(size: 8pt, t))
    }
    else if fortsetzung == "ja" { par(first-line-indent: 0pt, t) }
    else { par(t) }
  }
}

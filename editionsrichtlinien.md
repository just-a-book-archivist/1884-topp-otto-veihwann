# Editionsrichtlinien

Was in `transcription/pNNN.txt` steht und was nicht. Die Seitendateien sind das Ergebnis, diese
Datei ist die Begründung — jede Abweichung vom Druck muss hier stehen, sonst ist sie ein Fehler.

Grundsatz: **der Scan ist die Autorität.** Normalisiert wird nur, was hier einzeln aufgeführt und
am Scan geprüft ist. Ostfälisch wird nie in Richtung Hochdeutsch geglättet.

## Was ohnehin gilt

| Sache | Regelung | seit |
|---|---|---|
| Langes ſ | bleibt stehen. `ſ`→`s` macht der Generator, nicht die Transkription. | Anfang |
| Zeilenumbrüche | bleiben wie im Druck. Trennstrich am Zeilenende bleibt; auflösen macht der Generator. | Anfang |
| Doppelschräger Bindestrich `⸗` | wird als einfacher `-` geschrieben. Eigenschaft der Fraktur-Type, nicht des Textes; das Buch hat keinen anderen Bindestrich, die Abbildung ist total und umkehrbar. | 31.08.2026 |
| Laufkopf `— N —` | wird **nicht** übernommen. Die Seitenzahl steht im Dateinamen. | ab p003 in der Praxis, hier festgeschrieben 04.09.2026 |
| Bogensignatur (Ziffer am Fuß) | wird **nicht** übernommen, sondern in `anmerkungen.tsv` vermerkt. Druckersignatur zum Falzen der Bogen, kein Text. Erster Fund p049 („4“). | 19.09.2026, p049 |
| Spatium vor `!` `?` `;` `:` | Der Druck setzt nach Frakturbrauch ein Spatium davor (p058 `Welt !`, `beſtahn ?`, `ſegt :`). Es wird **nicht** übernommen, die Transkription schreibt eng. Eigenschaft des Satzes, nicht des Textes — dieselbe Klasse wie `⸗`. Seit p003 in der Praxis, hier nachgetragen. | 20.09.2026, p058 |
| Absatz | vier Leerzeichen Einzug, davor eine Leerzeile. | ab p003 |
| Verse | jede Verszeile auf eigener Zeile, acht Leerzeichen Einzug, davor und danach eine Leerzeile. So bleibt der Vers Zeile für Zeile wie gedruckt und ist für den Generator vom Absatz unterscheidbar. Strophen, die im Druck durch größeren Abstand getrennt sind, bekommen eine Leerzeile dazwischen; ist die erste Zeile einer Strophe im Druck eingerückt, bekommt sie zwölf statt acht Leerzeichen (p054, 19.09.2026). Zentrierte Verse werden nicht nachgebildet: Wirkt eine kürzere Zeile im Druck weiter eingerückt, liegt das an der Zentrierung, nicht an einem eigenen Einzug (p052). `../werkzeuge/pruefen.py` kann neben Versen einen Absatz fälschlich als „im Scan nicht eingerückt“ melden, weil die Verszeilen die Randschätzung verschieben. | 18.09.2026, p026 |
| Eingerückte Einschübe (Briefe) | Jede Zeile des Blocks bekommt **sechs** Leerzeichen Einzug, davor und danach eine Leerzeile; ein Absatzanfang innerhalb des Blocks bekommt vier weitere, also zehn. So bleibt der Block vom Absatz (vier) und vom Vers (acht) unterscheidbar, und der Generator kann ihn als Einschub setzen. Zentrierte oder rechts gesetzte Zeilen des Blocks — Anrede, Unterschrift — werden **nicht** nachgebildet, sie bekommen die sechs Leerzeichen wie der Rest; ihre Stellung im Druck steht in `anmerkungen.tsv`. `../werkzeuge/pruefen.py` meldet jede Blockzeile als „im Text eingerückt, im Scan nicht“, weil es den Rand lokal aus den Blockzeilen selbst schätzt — dieselbe Fehlmeldung wie bei Versen. | 22.09.2026, p067 |
| Zierlinien, Vignetten | werden **nicht** übernommen und in `transcription/anmerkungen.tsv` vermerkt (art `satz`). Ob der spätere Satz sie wieder setzt, entscheidet der Generator. `../werkzeuge/pruefen.py` meldet ihren Streifen als „ohne Text“. | 17.09.2026, p017; p003 angeglichen |
| Fehlender Satzend-Punkt, fehlendes schließendes Anführungszeichen | wird ergänzt: der Punkt, wenn der nächste Satz groß anhebt und am Scan kein Punkt steht; das „““, wenn eine geöffnete Rede nie geschlossen wird. Jede Stelle in der Liste „Berichtigt“. Fehlende Kommas bleiben, wie gedruckt. | 18.09.2026, p034; p008 angeglichen; Anführungszeichen 19.09.2026, p043 |
| Druckschäden, Bleistiftspuren, Setzerfehler | bleiben im Text wie gedruckt und werden in `transcription/anmerkungen.tsv` vermerkt. **Ausnahme:** ein Setzfehler, der kein Wort ergibt, wird berichtigt, wenn die gemeinte Form eindeutig ist — jede Stelle einzeln in der Liste „Berichtigt“ unten. | Anfang; Ausnahme seit 17.09.2026 |

## Normalisiert — die Positivliste

Nur diese Formen werden stillschweigend vereinheitlicht. Die Liste wächst **wortweise**, nie
klassenweise (siehe unten, warum).

| Gedruckt | In der Transkription | Beleg im Buch | Begründung |
|---|---|---|---|
| `und` | `un` | `un` 2169× gegen `und` 109× | Gleiches Wort, gleiche Funktion, keine grammatische Unterscheidung. Die Minderheitsform steht im Buch ohne System, teils in derselben Zeile wie `un` (p010: `kommen und Jonas` neben `un denn härre`). |
| `Sonn-` | `Sönn-` | `Sönn-` 6× gegen `Sonn-` 4× | Dasselbe Wort, auf p010 einundzwanzig Zeilen auseinander einmal mit und einmal ohne Punkte — Setzervariante ohne Bedeutungsunterschied. Die Regel gilt dem Wort, also auch der Zusammensetzung: `Sonndagsſtaate` → `Sönndagsſtaate`. **Dünne Beleglage** — 6:4 statt der zunächst gezählten 5:2, weil die Zusammensetzungen (`Sonndagsſtaate`, `Sonndaesſtaate`) beim ersten Zählen durch das Wortgrenzen-Muster fielen. Bei dieser Verteilung ist auch freie Variation denkbar; die Regel steht zur Rücknahme. |
| `Hochtiedt` | `Hochtied` | `Hochtied` 7× gegen `Hochtiedt` 2× | Dasselbe Wort; das auslautende t ist stumm und trägt keine Bedeutung. **Dünne Beleglage** — beide `Hochtiedt` stehen auf noch nicht geprüften Seiten und können OCR-Rauschen sein; bei der Korrektur dieser Seiten zu prüfen, sonst ist die Regel zurückzunehmen. |
| `Merſte` | `Mehrſte` | `Mehrſte(n)` 16× auf 14 Seiten gegen `Merſte` 1× (p013) | Dasselbe Wort; das h ist Dehnungszeichen und trägt keine Bedeutung. p013 setzt `vor't Merſte` in genau der Wendung, die sonst 8× `vor't Mehrſte` lautet. Einzelfall des Setzers. |

**Nur für Topps Plattdeutsch.** Die Positivliste gilt nicht für fremde Rede, die der Autor bewusst anders
setzt — auf p045 spricht ein Student verspottetes Sächsisch (`tu`, `tenn`, `Peweis`, `teitſch`), und dessen
`und` bleibt stehen. Dort wäre die Normalisierung eine Verfälschung. (Festgelegt 19.09.2026.)

**Angewandt auf:** p005 (3×), p006 (1×), p008 (1×), p009 (1×), p010 (2× `und`, 1× `Sonndaes`),
p011 (`Sonndaes`, `Sonndagsſtaate`), p012 (2× `und`, `Sonndaesſtaate`), p013 (`und`, `Merſte`), p019 (2× `und`, `Hochtiedt`), p020 (2× `und`), p022 (3× `und`), p023 (3× `und`), p026 (`und`), p027 (2× `und`), p030 (`und`), p031 (`und`), p032 (`und`), p036 (2× `und`), p040 (`und`), p041 (`und`), p042 (`und`), p044 (`und`), p046 (`und`), p055 (2× `und`), p064 (`und`), p065 (`und`), p066 (2× `und`), p068 (`und`), p077 (`und`), p078 (`und`), p079 (`und`), p083 (`und`), p084 (`und`), p085 (3× `und`), p086 (5× `und`), p087 (5× `und`), p088 (3× `und`), p089 (`und`), p090 (2× `und`), p091 (7× `und`), p092 (3× `und`), p093 (4× `und`), p094 (`und`), p096 (2× `und`), p099 (`und`), p102 (`und`), p105 (`und`), p106 (2× `und`).
Auf den noch nicht am Scan geprüften Seiten in `transcription/` wird nichts angewandt — dort ist
`und` womöglich gar keine Lesung, sondern Maschinenrauschen. Die Regel greift, wenn die Seite
korrigiert wird.

## Berichtigt — Setzfehler, die kein Wort ergeben

Anders als die Positivliste gilt hier nichts für ein Wort oder eine Klasse, sondern jede Zeile für
genau eine Stelle. Berichtigt wird nur, wenn die gedruckte Form kein Wort ist (Ostfälisches
Wörterbuch, Belege im Buch) und die gemeinte Form eindeutig. Ein seltenes, aber mögliches Wort ist
kein Setzfehler und bleibt stehen — `anzant` auf p012 sah auch wie ein Fehler aus.

| Seite | Gedruckt | In der Transkription | Begründung |
|---|---|---|---|
| p007 | `prußig` | `prutzig` | `hebbe ſau en ſlank, prutzig Fruenzen`: die Ligatur ist tz, nicht ß. Gemessen beim Lesen von p062, wo dasselbe Wort als `Prutzigkeit` wiederkehrt — jede Type auf 40x40 gerastert und pixelweise verglichen, Verfahren wie `Krabaten` (p030). Die drei Kandidaten treffen tz mit 0,819/0,787/0,784/0,684/0,677, ß nur mit 0,576–0,642; Maßstab: ß gegen ß 0,916 und 0,802, verschiedene Typen 0,558–0,664. p007 entscheidet es allein, weil die Seite beide Ligaturen elf Zeilen auseinander setzt: `Burßen` mit ß, `prutzig` mit tz. `prußig` ist kein Wort, `prutzig` (stolz, hochmütig) passt zur Stelle. |
| p008 | `prußig` | `prutzig` | `ſied nich ſau prutzig tien mek as up Stunds`: dieselbe Type wie p007, hier zusätzlich in der Höhe getrennt — die tz-Ligatur misst 22x51 px Tinte, das ß von `Burßen` derselben Seite 27x88 px. |
| p107 | `hren` | `ehren` | `de flietigen Immen mit ehren Honnigdronen`: das e am Zeilenanfang ist nicht gedruckt. Die Zeile beginnt bei x=245 gegen 231-234 der Nachbarzeilen (auch gegen `harren`, das ebenfalls mit h anhebt) — ausgefallene Type. `hren` ist kein Wort. |
| p102 | `bevormuuden` | `bevormunden` | `dat ober beie teſamme ſe bevormunden`: u statt n, vertauschte Type wie `iu` auf p084. Bei der Kontrolle am 26.09.2026 so bestimmt; die erste Lesung hatte das Wort schon als „bevormunden“ geschrieben, die Frage aber offen gelassen. Kein Wort. |
| p101 | `Balutdruppe` | `Blautdruppe` | `manche rohe Blautdruppe up ehre witte Winterkled follt`: vertauschte Typen (al statt la), wie `Gurndbeſitz` auf p084. Kein Wort; `Blaut` (Blut) ist im Buch belegt. |
| p100 | `nn` | `un` | `un begüſeke ehne un föddere kleineke`: n statt u, vertauschte Type wie `iu` auf p084, nur in der Gegenrichtung. Bei der Kontrolle am 26.09.2026 bemerkt; die OCR und die erste Lesung hatten stillschweigend „un“. `nn` ist kein Wort. |
| p099 | `Twilliugen` | `Twillingen` | `ſtorf … de Vormund von en beien Twillingen`: der vorletzte Stamm-Buchstabe ist gemessen ein u — sein Verbindungsbogen sitzt nur unten (0,81-0,94 der Glyphenhöhe), das n von `en` in derselben Zeile trägt ihn oben (0,12-0,24). Vertauschte Type wie `eue` auf p078. `Twillinge` steht auf derselben Seite zweimal. |
| p095 | `heiduiſchen` | `heidniſchen` | `mit groten Nummern un velen bunten, heidniſchen Blaumen`: u statt n, vertauschte Type wie `iu` auf p084. Bei der Kontrolle am 26.09.2026 vom Nutzer bestätigt, dass u gedruckt ist; die erste Lesung hatte das Wort als nur hier belegte Form wie gedruckt stehen lassen. Kein Wort; `heidniſchen` steht auf p044. |
| p094 | `der na. as` | `der na, as` | `denn licket ſe neggen Dae der na, / as wärr' et ile Honnig`: Punkt am Zeilenende mitten im Satz, der klein weitergeht. Falsche Type des Setzers, wie auf p035 zum Komma berichtigt; bei der Kontrolle am 26.09.2026 so entschieden. |
| p094 | `Ottte` | `Otte` | `De Upſeiher ſäe tau Otte`: ein t zu viel. Kein Wort; der Name steht im Buch hundertfach. |
| p094 | `ok'` | `ok` | `vel hätt dei ok nich under en Häuen`: verirrter Apostroph ohne Funktion, wie auf p042 und p089. |
| p093 | `utmaken` | `utmaken.` | `weil des, dat ſe en grötteſten Hupen utmaken.`: Absatzende ohne Punkt, der nächste Absatz hebt groß an; am Scan nach dem Wort nichts. |
| p089 | `ok'` | `ok` | `Mit en Gewarbe ſtund dat ok ſau hen`: verirrter Apostroph ohne Funktion, wie `ok'` auf p042. |
| p089 | `ſchonen.` | `ſchonen.“` | Vers „Den Sönndag frie …“: das öffnende „„“ steht, das schließende fehlt; am Scan nach dem Punkt nichts. |
| p085 | `mank'` | `mank` | `Name mank de Perſonen enennt word`: verirrter Apostroph ohne Funktion, dasselbe Wort wie auf p077. |
| p084 | `iu` | `in` | `un ſe leien den Grafen von All bi Enne in en Ohren`: der zweite Buchstabe ist ein u, wo ein n stehen muss — vertauschte Type wie `eue` auf p078 und `Twilliugen` auf p099. Bei der Kontrolle am 25.09.2026 so bestimmt; die erste Lesung hatte ihn auf dem 40x40-Raster als n gemessen (0,859 gegen 0,794), der Raster trennt u und n aber schlecht (vgl. p087). `iu` ist kein Wort. |
| p084 | `Gurndbeſitz` | `Grundbeſitz` | `wie wol hei en olen befeſtigten Grundbeſitz`: vertauschte Typen (ur statt ru), wie `Slkavendeinſt` auf p057. Kein Wort; `Grundbeſitz` steht auf p027. |
| p078 | `eue` | `ene` | `un de Immen umſwaren ene un dreuen Honnig in`: der mittlere Buchstabe ist am Scan ein u — der Verbindungsbogen sitzt unten (y=308), während das `n` von `un` zwei Wörter weiter ihn oben trägt; die beiden `e` links und rechts tragen ihren Querstrich. `eue` ist kein Wort, `ene` (ihn) steht allein auf p003-p059 einundneunzigmal. Bei der Kontrolle am 24.09.2026 als kopfstehendes n bestimmt — die Type um 180° gedreht, wie das k auf p044; vgl. `Krabateu` (p030) und `Naſinuen` (p042). |
| p077 | `mank'` | `mank` | `denn wat leip ek mank en Wullewaens rum`: verirrter Apostroph ohne Funktion, wie p039 `ſek'`, p042 `ok'` und p049 `hat'`. `mank` ist eine Präposition, es ist nichts elidiert; dieselbe Seite setzt in Zeile 36 `wedder mank en` ohne Apostroph. |
| p070 | `Deconom` | `Oeconom` | `un von er andern en olt Oeconom mit en ſpaniſchen Rohre`: der Anfangsbuchstabe ist am Scan ein D, kein O. Gemessen gegen beide: das `D` von `Dat` (Z. 23) misst 51 x 51 px Tinte und hat dieselbe Form, das `O` von `Otte` (Z. 9) misst 36 x 39 px und eine andere; der Kandidat misst 46 x 54 px. `Deconom` ist kein Wort, `Oeconom` schon — im Buch auch auf p086 als `econome`. D und O liegen im Setzkasten nebeneinander. |
| p069 | `eeubet` | `eubet` | `un Kiekebuſch ward hier ok nich eubet!`: das `e` ist doppelt gesetzt. Zuerst in neunfacher Vergrößerung als `ecubet` gemessen — der zweite runde Buchstabe schien den Querstrich nicht zu tragen —, bei der Kontrolle am 24.09.2026 in starker Vergrößerung eindeutig als zweites `e` gelesen: der Querstrich des zweiten ist vage, aber da, erst weit über neunfach zu sehen. Eine verdoppelte Type ist ein Setzfehler, `eeubet` kein Wort. Die gemeinte Form ist `eubet` (üben, Partizip mit der Vorsilbe `e-`, hd. *ge-*, wie auf derselben Seite `uneſchicket`, `umeſchertet`, `taueſtoppet`), im Buch belegt als zweiter Teil von `uteeubet` (p044, geprüft) und `inneeubet` (p079); Wörter mit `ee-` am Anfang gibt es im Buch nicht außer `eene`. **Die unsicherste Berichtigung bisher**, weil sie eine Type streicht statt eine zu ersetzen. |
| p068 | `Dör` | `Dör.` | `De Regierungsrath dreie de Hand umme un wieſe na er Dör`: Satzende ohne Punkt, der nächste Absatz hebt groß mit `No, dachte Otte` an. Anders als p034, p047 und p061 ist rechts **kein** freier Raum — die Zeile läuft mit Tintenende 2276 px voll an den Satzspiegel (2266-2276 der übrigen Zeilen), der Punkt hatte also keinen Platz, wie bei p065. Kein Geisterbild: dunkelster Grauwert im Rand hinter `Dör` 245 gegen 239, 240 und 241 auf drei Kontrollzeilen derselben Seite (Papier 253). |
| p066 | `eiper` | `deiper` | `de Vergißmeinichſteren word immer deiper un grötter`: dem Wort fehlt das anlautende d. `eiper` ist kein Wort, `deiper` steht auf derselben Seite zweimal (`deipen Japp`, `deipe in dat grote Oe`). Die Zeile beginnt bündig am Satzspiegel (Tinte ab x=348 gegen x=349 der Folgezeile), ist also nicht beschnitten, und vor dem `e` steht kein Geisterbild: dunkelster Grauwert im Rand 242 gegen 235 und 241 auf zwei regulär beginnenden Kontrollzeilen (Papier 253). Die Type stand nicht im Satz. Wie p039 `u` → `un` und p061 `m Stammbaume`. Nachgetragen am 22.09.2026, nachdem die Stelle beim Gegenlesen auffiel — die erste Lesung hatte das `d` stillschweigend ergänzt. |
| p066 | `gerac` | `gerae` | `Alles na gerac in dat Wiee verſwinnt.`: der letzte Buchstabe ist am Scan ein c, und `gerac` ist kein Wort; `na gerae` steht auf p051, `nagerae` auf p050. Falsche Type. Der Pixelvergleich taugt hier nicht — c und e unterscheiden sich nur durch den Querstrich im Auge, und auf dem 40x40-Raster trifft der Kandidat c mit 0,868 und e mit 0,873/0,861, während e gegen c selbst 0,881 und 0,853 misst. Entschieden am Buchstaben in zwölffacher Vergrößerung: die beiden e derselben Zeile tragen den Querstrich deutlich, der Kandidat hat keinen und gleicht dem c von `Tact` eine Zeile höher. |
| p065 | `ſe` / `ek` | `ſe-` / `ek` | Zeilenumbruch mitten in `ſek` ohne Trennstrich: `vornut, wenn ſe` / `ek en ander leiw hätt`. Die Wendung steht im Buch sonst zusammen — `ſek en ander leiw` (p053), `ſek en ander tau` (p005), `ſek en ander de Hänne` (p056). Beide Hälften sind für sich Wörter, und genau darum setzte der Generator ohne Trennstrich zwei. Anders als p031 und p061 läuft die Zeile hier voll bis an den Satzspiegel (Tintenende x=2119 gegen das Maß 2116 der übrigen Zeilen), der Trennstrich ist also nicht weggelassen, sondern hatte keinen Platz mehr. |
| p061 | `m Stammbaume` | `im Stammbaume` | `m` allein ist kein Wort; der Satz verlangt `im`. Die Zeile beginnt bündig am Satzspiegel (x=254 gegen 236–261 der übrigen Zeilen), ist also nicht beschnitten, und vor dem `m` steht kein Geisterbild eines `i`: dunkelster Grauwert im Rand links der Zeile 207 gegen 213/213/219 auf drei Kontrollzeilen derselben Seite (Papier 255; die Schattenspalte des Blattrands bei x=187–189 ist ausgenommen). Das `i` stand nicht im Satz. Wie p039 `u` → `un`. |
| p061 | `auf` / `gebracht` | `auf-` / `gebracht` | Zeilenumbruch mitten in `aufgebracht` ohne Trennstrich; rechts freier Raum bis zum Blattrand. Ohne ihn setzte der Generator zwei Wörter. Wie p031 `Vaddern` / `gabe`. |
| p061 | `Heme` | `Heme.` | Satzende ohne Punkt, der nächste Absatz beginnt groß mit `Von Heme?`; rechts freier Raum bis zum Blattrand. |
| p061 | `dürfen` | `dürfen.` | Satzende ohne Punkt, der nächste Absatz beginnt groß mit `Das mag ſein`; rechts freier Raum bis zum Blattrand. |
| p061 | `nehmen` | `nehmen.` | Satzende ohne Punkt, der nächste Satz beginnt groß mit `Was ich will`; rechts freier Raum bis zum Blattrand. Eine Zeile tiefer steht `mein Herr.` mit Punkt, der Setzer lässt sie also nicht durchweg weg. Für alle drei Punkte gemessen: hinter den Wörtern dunkelster Grauwert 238/241/247, hinter `mein Herr.` und `gung af.` mit Punkt 245/246 — kein Geisterbild, also nicht gedruckt, sondern nicht gesetzt. |
| p008 | `ſachte` | `ſachte.` | Satzende ohne Punkt, der nächste Satz beginnt mit `Wenn`; rechts freier Raum bis zum Blattrand. Zunächst wie gedruckt belassen, am 18.09.2026 nach der Regel angeglichen. |
| p057 | `Slkavendeinſt` | `Sklavendeinſt` | Vertauschte Typen (lk statt kl); zwei Zeilen höher steht „Sklaven“ richtig. |
| p051 | `verſeuken.` | `verſeuken,` | Punkt mitten im Satz, der klein mit `ok dine Stelten` weitergeht. |
| p051 | `nich!` | `nich!“` | Rede `„Vergütt dat Beſte nich!` im Druck nicht geschlossen. |
| p049 | `Liw gurt` | `Liwgurt` | Wortlücke im Kompositum, Unsauberkeit beim Setzen. |
| p049 | `hat'` | `hat` | Apostroph ohne Funktion, wie p039, p042. |
| p048 | `Gere.` | `Gere,` | `bi ſiner Gere, / de hei ſau herzlich leiw harre`: Punkt vor dem Relativsatz, der klein weitergeht. |
| p047 | `velfältigſten.` | `velfältigſten,` | Punkt zwischen zwei Adjektiven, `dat de velfältigſten, ſwärreſten Rechtsſprüche`. Schlechter Druck, zum Komma berichtigt. |
| p047 | `utebuet` | `utebuet.` | Satzende ohne Punkt, der nächste Absatz beginnt groß mit `Diſſen`. |
| p045 | `Gott.` | `Gott.“` | Vers „Fri in er Noth …“: das öffnende „„“ steht, das schließende fehlt. |
| p044 | `ʞein` (kopfstehendes k) | `kein` | `wenn ſe grade kein Gegenpart`: die k-Type steht auf dem Kopf und sieht aus wie ein J mit Unterlänge (OCR: `zein`). Um 180° gedreht eindeutig ein Fraktur-k — erster sicherer Beleg einer kopfstehenden Type im Buch. |
| p043 | `min;` | `min` | `un Gere was min; / Sweſter`: Semikolon mitten in „meine Schwester“. Falsche Type. |
| p043 | `kree.` | `kree.“` | Die Rede `„da will ek mek …` wird geöffnet, aber nie geschlossen; zwei Absätze höher ist das „““ gesetzt. |
| p042 | `Naſinuen` | `Naſinnen` | `bi en bettchen Naſinuen`: n und u vertauscht wie bei `Krabateu` (p030). Kein Wort; `Naſinnen` (Nachsinnen) steht auf p020. |
| p042 | `ok'` | `ok` | `un ok' de Weihdae`: verirrter Apostroph wie `ſek'` auf p039. |
| p040 | `ſind.` | `ſind,` | `ſeer mine Eldern dodt ſind, / finne ek neine Rauhe nich`: Punkt mitten im Satz, der klein weitergeht. Wie p035 zum Komma. |
| p039 | `u` | `un` | `bi Brauer u Sweſter`: `n` fehlt. Kein Wort. |
| p039 | `ſek'` | `ſek` | `bigegnen ſek' Otte`: verirrter Apostroph ohne Funktion. |
| p035 | `meinen. ſau lange` | `meinen, ſau lange` | Punkt mitten im Satz, der klein weitergeht (`dei meinen, ſau lange, wie ſei leben, wolle ſek dat wol hentrecken`). Falsche Type des Setzers, zum Komma berichtigt. |
| p034 | `deilen` | `deilen.` | Satzende ohne Punkt, der nächste Satz beginnt groß mit `Sau`. Punkt ergänzt. Zwei Zeilen tiefer steht nach `un dat ſe` ein Punkt, wo der Satz auf p035 weiterläuft — womöglich derselbe, verrutscht; dort nicht übernommen. |
| p031 | `Vaddern` / `gabe` | `Vaddern-` / `gabe` | Zeilenumbruch mitten im Kompositum ohne Trennstrich. Ohne ihn setzte der Generator zwei Wörter; `Vadderngabe` steht im Buch sonst immer zusammen. |
| p030 | `Krabateu` | `Krabaten` | Letzter Buchstabe am Scan ein u (Pixelvergleich gegen u und n derselben Zeile: 0,912 gegen 0,833/0,876, Grundähnlichkeit 0,876). „Krabateu“ ist kein Wort, „Krabaten“ (Kinder) steht auf p025. Falsche oder kopfstehende Type. |
| p021 | `up e legt` | `upelegt` | Volle Wortlücke im Partizip; `e` ist für sich kein Wort. |
| p021 | `ſin er` | `ſiner` | Volle Wortlücke. Beide Teile sind für sich Wörter, aber `an ſin er leiwen Frue` ergibt keinen Satz. |
| p020 | `uu` | `un` | `Ganne lache ſchämeleren, uu Veihwann`. Kein Wort; „un“ steht in derselben Zeile mehrfach. |
| p020 | `nn` | `un` | `up er Wieſche, nn en ſtillen Free`. Kein Wort, und der Satz verlangt „un“. Die OCR machte daraus „nu“, was den Sinn verkehrt. |
| p020 | `Gan ne` | `Ganne` | Volle Wortlücke mitten im Namen. Anders als `e ne` (p004, p010, p016), wo beide Teile für sich stehen könnten: `Gan` ist großgeschrieben und sonst nichts, also der Name. |
| p015 | `Shnieer` | `Schnieer` | Am Scan eindeutig `Sh` ohne c. „Shnieer“ ist kein Wort; gemeint ist der Schneider, in der Aufzählung Schmed, Stellmaker, Schnieer. |
| p017 | `Nettehowwe` | `Nettelhowwe` | Am Scan eindeutig ohne l. „Nettehowwe“ ist kein Wort; im Buch sonst 8× `Nettelhowwe`, der Hof der Nettels. |
| p015 | `emährt` | `ernährt` | Am Scan eindeutig m, nicht rn — ein Setzfehler, keine Verlesung. „emährt“ steht nicht im Ostfälischen Wörterbuch, „ernährt“ gibt es. |

**Die Wortlücken — entschieden 18.09.2026.** `e ne` bleibt als Lücke stehen, wie auf p004, p010, p016
und p025: Es ist kein Einzelfehler, sondern kehrt im Buch auf rund sechzehn Seiten wieder, also eine
Gewohnheit des Setzers, die zur Überlieferung gehört. Geschlossen werden nur einzelne Lücken, die sonst
nicht vorkommen und ohne Schließen keinen Sinn ergeben: `Gan ne` (p020), `up e legt` und `ſin er`
(p021). Dasselbe gilt für `e ner`, das ebenso wiederkehrt: Auf p022 war es zunächst
zu `ener` geschlossen und ist am 18.09.2026 auf die Lücke zurückgesetzt worden.

## Nicht normalisiert — die Verwechslungsliste

**Der Umlaut ist hier die Grammatik.** Diese Paare unterscheiden sich nur durch den Umlaut und sind
trotzdem verschiedene Wörter. Wer sie vereinheitlicht, löscht den Konjunktiv aus dem ganzen Buch:

| Paar | Buch | ist | Beleg |
|---|---|---|---|
| `harre` / `härre` | 184 / 72 | **hatte / hätte** | `Se harre ehren Korf ſtellt` — `Hei härre geren utegluſtert` |
| `harren` / `härren` | 101 / 25 | hatten / hätten | `Striet ehat harren` — `as härren ſe wat verloren` |
| `moßte` / `mößte` | 17 / 33 | **musste / müsste** | `up den en ſtien moßte` — `et mößte ene wol gelingen` |
| `wußte` / `wüßte` | 10 / 1 | **wusste / wüsste** | `Nettels wußte as e ne gue Dochter` — `ſau wüßte ek nich` |
| `Mäken` / `maken` | 17 / 43 | Mädchen / machen | |
| `Schon` / `ſchön` | | schon / schön | |
| `Buſche` / `Büſche` | | Singular / Plural | |
| `Koppe` / `Köppe` | | Singular / Plural | |
| `Andern` / `ändern` | | andern / ändern | |
| `Lüe` / `lue` | | Leute / laut (`da juchheißen ſe lue up`) | |

## Warum wortweise und nicht klassenweise — gemessen 04.09.2026

Die naheliegende Regel wäre „Umlautvarianten vereinheitlichen“. Sie wurde an den acht geprüften
Seiten p003–p010 gemessen: dort gibt es **zwölf Formpaare, die sich nur im Umlaut unterscheiden,
und zehn davon sind verschiedene Wörter** — Konjunktive, Plurale, Homographen. Die Trefferquote
einer Klassenregel läge bei 2 von 12.

Auch die Mehrheit taugt nicht als Kriterium. Bei `un`/`und` zeigt sie richtig (2169:109), bei
`moßte`/`mößte` zeigt sie mit 33:17 auf den **Konjunktiv** und würde den Indikativ ersetzen.

Das ist derselbe Befund wie bei `ocr-out/suspects.tsv`, nur an anderer Stelle: **ostfälische
Flexion lebt auf Editierdistanz 1.** Jede mechanische Regel, die auf einem Zeichen Unterschied
aufsetzt, kann Morphologie nicht von Variante trennen. Was bleibt, ist die Einzelprüfung — und die
Positivliste oben ist ihr Ergebnis, nicht ihre Abkürzung.

## Offen — bewusst noch nicht entschieden

- **`ſüß` / `ſüſſ` / `Süß` / `Süſſ`.** Dasselbe Wort, auf p009 vier Zeilen auseinander einmal mit
  ß-Ligatur, einmal mit zwei langen s (in `anmerkungen.tsv` vermerkt, wie gedruckt übernommen).
  Für eine Normalisierung spräche dasselbe Argument wie bei `⸗`: die Wahl zwischen `ß` und `ſſ` ist
  eine Setzerentscheidung an der Type. Dagegen spricht, dass sie im Fraktursatz nicht durchweg
  bedeutungslos ist. Ungeprüft, wie oft das Paar im Buch überhaupt vorkommt. **p065 liefert den bisher dichtesten Beleg:** dasselbe Wort dreimal auf einer Seite, `Kuſſe` (Z. 14) und `Küſſe` (Z. 17) mit zwei langen s, `Kuß` (Z. 28) mit der ß-Ligatur — am Scan geprüft, alle drei wie gedruckt. Der Unterschied folgt hier der Silbe, nicht der Laune: `Kuſſe`/`Küſſe` sind zweisilbig mit s zwischen Vokalen, `Kuß` einsilbig im Auslaut. Das spricht gegen eine Normalisierung.
- **`kummet` / `kümmet`** (27 / 3). Beide belegt als 3. Person Singular — `wie dat ſau kümmet`
  gegen `et kummet nich wieer`. Anders als `harre`/`härre` ist hier kein Modusunterschied zu sehen,
  aber auch kein Beweis für freie Variation. Bleibt vorerst wie gedruckt.
- **`he` / `hei`** (15 / 311). Dasselbe Wort, dieselbe Funktion — nach dem Muster von `und`/`un`
  ein Kandidat für die Positivliste. Dagegen spricht, dass `he` die unbetonte Form sein könnte
  (p011: `dat he de kranke Mudder nich ſtört`, satzintern und unbetont). Ungeprüft, ob die
  15 Belege alle in dieser Stellung stehen; solange das nicht ausgezählt ist, bleibt es wie
  gedruckt.
- **Abgetrennte Vorsilben: `e ne` für `ene`, `ober e hat` für `ehat`.** Der Druck setzt eine volle
  Wortlücke (p003, p004, p010, p022, p025 …). Auf p004 als „wie gedruckt übernommen“ entschieden.
  Eine Zusammenziehung wäre eine Normalisierung des Wortabstands, nicht der Orthographie — eigene
  Klasse, eigene Entscheidung.

## Die Spalte `art` in `anmerkungen.tsv`

Sieben Werte, scharf getrennt gehalten. Wer einen siebten braucht, führt ihn hier ein, statt einen
bestehenden zu dehnen.

| Wert | wofür |
|---|---|
| `scan` | Schaden am Bild oder an der Aufnahme: Bundschatten, Verzerrung, zerlegte und umgestellte Zeilen. Der Druck ist in Ordnung, die Vorlage nicht. |
| `druckschaden` | Schadhafte Type: der Druck selbst ist beschädigt, das Blatt gibt nichts anderes her. |
| `satz` | Entscheidung des Setzers: Wortlücken, fehlende Satzzeichen, dasselbe Wort verschieden gesetzt. Kein Schaden, sondern so gewollt oder so passiert. |
| `verlesung` | Der Druck ist klar lesbar, die OCR las etwas anderes — und das Falsche ist ein plausibles Wort. Der gefährlichste Fall, darum eigener Wert. |
| `marginalie` | Spätere Hand im Buch. Nie in den Text übernommen. |
| `normalisiert` | Eine Regel aus der Positivliste oben wurde angewandt; die gedruckte Form steht in der Anmerkung. |
| `berichtigt` | Ein Setzfehler aus der Liste „Berichtigt“ oben wurde behoben; die gedruckte Form steht in der Anmerkung. Eingeführt 17.09.2026. |

## Eine Regel hinzufügen

1. Beide Formen am Scan lesen, nicht in der OCR. Die OCR verwechselt genau diese Zeichen.
2. Im ganzen Buch zählen (`grep -how` über `ocr-out/text/`), und die Trefferstellen ansehen —
   Zählen allein hätte bei `moßte`/`mößte` in die Irre geführt.
3. Prüfen, ob der Unterschied Bedeutung trägt: Indikativ/Konjunktiv, Singular/Plural, Person.
   Im Zweifel nicht normalisieren; `anmerkungen.tsv` kostet nichts, ein stiller Eingriff ist
   unumkehrbar.
4. Zeile in die Positivliste, mit Beleg und Begründung. Dann anwenden — auf die geprüften Seiten
   sofort, auf die übrigen beim Korrekturgang.

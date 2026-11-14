#!/usr/bin/env python3
"""Detaillering van het kantoor in de loods: plattegrond 1:50 met de kasten, de plank onder het raam en de plek van het bureau.
Schrijft detaillering-kantoor.html; daarna de PDF maken (zie CLAUDE.md).
Maten in mm, zelfde assen als CV/loods_plattegrond.py. x: van de achterwand (0) naar de wand van de slaapkamer.
y: van het sandwichpaneel van de rechtergevel (0, boven) naar de binnenwand (4150)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t

B = 4150                    # sandwichpaneel tot binnenwand
L = 6550                    # kantoor lang: voorstel, wand naar de slaapkamer 1,60 m opgeschoven (loodsplattegrond: 6450)
VZ = 225                    # isolatie en voorzetwand langs de rechtergevel
KD = 600                    # diepte van de kasten en de plank
RAAM = (1600, 2600)         # raam: 160 cm uit de achterwand, 1 m breed
DEUR = (3400, 4300)         # deur naar de loods (plek van de loodsplattegrond, draairichting aangenomen)
NIS = 800                   # diepte van de nis van de kachel
AB = 2100                   # achterwand tot hier langs de accuruimte; daarna de nis

STIJL = '''<style>
.kp text{font-family:Inter,Arial,sans-serif}
.kp .dim{fill:none;stroke:#1d1d1b;stroke-width:8px}.kp .ext{fill:none;stroke:#777;stroke-width:6px}
.kp .dimt{font-size:125px;fill:#1d1d1b;text-anchor:middle}
.kp .nm{font-size:150px;font-weight:700;fill:#1d1d1b;text-anchor:middle}.kp .gr{font-size:230px;font-weight:700;fill:#1d1d1b;text-anchor:middle}
.kp .tx{font-size:128px;fill:#1d1d1b;text-anchor:middle}.kp .tl{font-size:128px;fill:#1d1d1b}.kp .ti{font-size:128px;fill:#333;font-style:italic;text-anchor:middle}
.kp .iso{fill:#6f6a62;stroke:#1d1d1b;stroke-width:6px}.kp .kaal{fill:#fff;stroke:#1d1d1b;stroke-width:9px}.kp .gat{fill:#fff;stroke:none}
.kp .raam{fill:#fff;stroke:#1d1d1b;stroke-width:7px}
.kp .plank{fill:#fff;stroke:#1d1d1b;stroke-width:10px}.kp .kast{fill:#e1ded7;stroke:#1d1d1b;stroke-width:10px}
.kp .schuif{fill:none;stroke:#1d1d1b;stroke-width:6px}
.kp .bur{fill:#fff;stroke:#1d1d1b;stroke-width:24px;stroke-linejoin:round}
.kp .alt{fill:none;stroke:#1d1d1b;stroke-width:12px;stroke-dasharray:95 60}
.kp .aan{fill:none;stroke:#555;stroke-width:8px;stroke-dasharray:60 45}
.kp .app{fill:#fff;stroke:#1d1d1b;stroke-width:12px}
.kp .blad{fill:none;stroke:#1d1d1b;stroke-width:10px}.kp .zw{fill:none;stroke:#555;stroke-width:6px;stroke-dasharray:45 35}
.kp .pijl{fill:none;stroke:#1d1d1b;stroke-width:14px;marker-end:url(#kpkop)}
</style><defs><marker id="kpkop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#1d1d1b"/></marker></defs>'''

def r(x, y, w, h, c): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def tx(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}">{s}</text>'
def lvorm(x0, y0, x1, y1, hx0, hy0, hx1, hy1, c):
    """Bureau met hoekstuk als één omtrek: hoofdblad (x0,y0)-(x1,y1), hoekstuk (hx0,hy0)-(hx1,hy1), ze raken elkaar."""
    return r(x0, y0, x1 - x0, y1 - y0, c) + r(hx0, hy0, hx1 - hx0, hy1 - hy0, c)

def plattegrond():
    o = [STIJL]
    # ---- rechtergevel: sandwichpaneel, isolatie en voorzetwand; het raam blijft zichtbaar
    o.append(r(-1000, -90, L + 1200, 90, "iso") + r(0, 0, L, VZ, "iso"))
    o.append(r(RAAM[0], -90, 1000, VZ + 90, "raam") + f'<path class="schuif" d="M{RAAM[0]} -45 H{RAAM[1]}"/>')
    # ---- achterwand (accuruimte), nis, binnenwand, wand naar de slaapkamer
    o.append(r(-160, 0, 160, AB, "iso") + r(-NIS - 100, AB - 100, NIS + 100, 100, "kaal"))
    o.append(r(-NIS - 100, AB, 100, B - AB, "kaal") + r(-NIS - 100, B, NIS + 100, 100, "kaal"))
    o.append(r(0, B, L + 100, 160, "iso") + r(L, 0, 100, B, "iso"))
    o.append(r(DEUR[0], B - 8, 900, 180, "gat"))
    o.append(f'<path class="blad" d="M{DEUR[0]} {B} v-900"/><path class="zw" d="M{DEUR[0]} {B-900} A900 900 0 0 1 {DEUR[1]} {B}"/>')
    # ---- kachel in de nis, met de vrije ruimte ervoor
    o.append(r(-740, 2875, 540, 500, "app") + tx(-470, 3175, "K1", "nm") + tx(-400, 2420, "nis"))
    o.append(r(-200, 2775, 800, 700, "aan") + tx(660, 3170, "80 vrij", "tl"))
    # ---- airco en afzuiging op de achterwand (plek aangenomen)
    o.append(r(20, 1050, 210, 800, "aan") + tx(300, 1400, "airco,", "tl") + tx(300, 1570, "afzuiging", "tl"))
    o.append(tx(-560, 1050, "accu-") + tx(-560, 1220, "ruimte"))
    # ---- langs de gevel: plank met schuifdeuren eronder tot het raam, daarna hoge kasten
    o.append(r(0, VZ, RAAM[1], KD, "plank") + f'<path class="schuif" d="M0 {VZ+KD-40} H{RAAM[1]}"/>')
    o.append(tx(RAAM[1]/2, VZ + 270, "plank op 71 hoog, 60 diep") + tx(RAAM[1]/2, VZ + 450, "schuifdeuren eronder"))
    o.append(r(RAAM[1], VZ, L - RAAM[1], KD, "kast") + f'<path class="schuif" d="M{RAAM[1]} {VZ+KD-40} H{L}"/>')
    o.append(tx((RAAM[1] + L)/2, VZ + 270, "hoge kasten, 60 diep, met schuifdeuren") + tx((RAAM[1] + L)/2, VZ + 450, "hoogte en indeling nog te bepalen"))
    # ---- bureau A (advies): rug naar de wand van de slaapkamer, hoekstuk in de hoek tegen de binnenwand
    ax0 = DEUR[1] + 50
    o.append(lvorm(ax0, B - 2000, ax0 + 1000, B, ax0 + 1000, B - 600, L, B, "bur"))
    o.append(f'<path d="M{ax0+1000} {B-588} V{B-12}" stroke="#fff" stroke-width="30"/>')          # naad tussen blad en hoekstuk weg
    o.append(tx(ax0 + 500, 2950, "A", "gr") + tx(ax0 + 500, 3150, "bureau") + tx(ax0 + 500, 3320, "200 × 100"))
    o.append(tx((ax0 + 1000 + L)/2, B - 250, "hoekstuk 120 × 60"))
    o.append(f'<circle class="app" cx="{L-600}" cy="2780" r="230"/><path class="pijl" d="M{L-850} 2780 H{ax0+1060}"/>')
    t.TK = 45
    o.append(t.chain_h([ax0 + 1000, L], 3330, ["1200"]))
    o.append(t.chain_v([VZ + KD, B - 2000], ax0 + 500, ["1325"]))
    # ---- bureau B (alternatief): bij het raam, zicht op het raam
    o.append(lvorm(1300, 1925, 3300, 2925, 1300, 2925, 1900, 4125, "alt"))
    o.append(tx(2300, 2400, "B", "gr") + tx(2300, 2600, "alternatief: bij het raam"))
    o.append('<circle class="aan" cx="2600" cy="3400" r="230"/>')
    # ---- namen
    o.append(tx(3700, 1260, "Kantoor", "nm") + tx(3700, 1440, "655 × 392 netto"))
    o.append(tx(1700, B + 420, "loods", "ti"))
    o.append(f'<text class="ti" x="{L+330}" y="2300" transform="rotate(-90 {L+330} 2300)">slaapkamer</text>')
    o.append(tx(0, -700, "rechtergevel · het raam van 1 m blijft zichtbaar, de plank loopt eronder door", "tl"))
    # ---- maten
    t.TK = 55
    o.append(t.chain_h([0, RAAM[0], RAAM[1], L], -420, ["1600", "1000", "3950"], frm=-140))
    o.append(t.chain_h([0, DEUR[0], DEUR[1], L], B + 800, ["3400", "900 · deur", "2250"], frm=B + 230))
    o.append(t.chain_h([0, L], B + 1130, ["6550 · wand naar de slaapkamer 1,60 m opgeschoven"], frm=B + 860))
    o.append(t.chain_v([0, AB, B], -1400, ["2100", "2050 · nis"], frm=-960))
    o.append(t.chain_v([0, VZ, VZ + KD, B], L + 650, ["", "600", "3325"], frm=L + 160) + tx(L + 400, 160, "225"))
    t.TK = 26
    return t.svg(f"-1650 -880 {L+2500} 6240", 50, "".join(o), cls="kp")

PAGINA = '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Detaillering kantoor loods · Gasthuisstraat 6-a</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
/* A4 liggend, leesbaar in zwart-wit: lopende tekst >= 9 pt, tekst in tekeningen >= 7 pt. */
@page{size:297mm 210mm;margin:0}
:root{--ink:#1b1b1b;--muted:#444;--rule:#bdb9b0;--card:#f6f4ef;--cardrule:#8f8b82}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:Inter,"Helvetica Neue",Arial,sans-serif;color:var(--ink);font-size:9.4pt;line-height:1.38;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.sheet{width:297mm;height:210mm;padding:8mm 10mm 0;position:relative;page-break-after:always;overflow:hidden}
.sheet:last-child{page-break-after:auto}
.eyebrow{font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 1.5mm}
h2{font-size:15pt;line-height:1.15;font-weight:700;margin:0 0 1mm}
h3{font-size:10.4pt;font-weight:700;margin:0 0 1.6mm}
p{margin:0 0 2mm}
.sub{color:var(--muted);font-size:8.8pt;margin:0}
.card{background:var(--card);border:.3mm solid var(--cardrule);border-radius:1.4mm;padding:2.8mm 3.6mm}
ul.chk{list-style:none;margin:0;padding:0}
ul.chk li{position:relative;padding-left:5.4mm;margin-bottom:1.2mm}
ul.chk li:last-child{margin-bottom:0}
ul.chk li::before{content:"";position:absolute;left:0;top:.7mm;width:3mm;height:3mm;border:.35mm solid var(--ink);background:#fff}
ul.punt{margin:0;padding-left:4.4mm}ul.punt li{margin-bottom:1.1mm}ul.punt li:last-child{margin-bottom:0}
.foot{position:absolute;left:10mm;right:10mm;bottom:5.5mm;border-top:.35mm solid var(--ink);display:grid;grid-template-columns:3.1fr 2.5fr 1.2fr 1.7fr .8fr;font-size:8pt}
.foot div{padding:1.3mm 2.5mm 0 2.5mm;border-left:.2mm solid var(--rule);min-height:8.5mm}
.foot div:first-child{border-left:0;padding-left:0}
.foot span{display:block;font-size:6.6pt;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:.3mm}
.foot b{font-weight:600}
svg{display:block}
</style>
</head>
<body>
<section class="sheet">
  <p class="eyebrow">Eigen werk · kantoor in de loods · 14-11-2026</p>
  <h2>Kantoor loods · plattegrond 1:50 · plek van het bureau</h2>
  <p class="sub">Maten in mm, volgens de plattegrond van de loods. Dikke lijn = bureau op plek A (advies); streeplijn = alternatief B of aangenomen.</p>
  <div style="display:grid;grid-template-columns:181mm 1fr;gap:5mm;margin-top:2mm;align-items:start">
    <div>
%(plan)s
      <div class="card" style="margin-top:2mm"><h3>Nog opmeten voor de aanzichten van de kastenwand</h3>
        <ul class="chk" style="columns:2;column-gap:7mm">
          <li>Raam: onderkant en bovenkant boven de vloer.</li>
          <li>Plafondhoogte bij de gevel en bij de binnenwand.</li>
          <li>Hoge kasten: tot het plafond? Hoeveel deuren?</li>
          <li>Hoogte van het bureaublad (de plank ligt op 71).</li>
        </ul></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card"><h3>A · advies: achterin, rug naar de slaapkamerwand</h3>
        <ul class="punt">
          <li>Het verst van kachel, airco en afzuiging (± 6 m): geen geluid, warmte of tocht.</li>
          <li>Deur, kachel en de hele ruimte in beeld; niemand kijkt van achteren op de schermen.</li>
          <li>Raam schuin rechts voor: licht van opzij, geen spiegeling.</li>
          <li>Kasten en plank blijven bereikbaar: 1,3 m loopruimte.</li>
          <li>Nadeel: weinig daglicht op het blad (raam op bijna 5 m).</li>
          <li>Vraagt 2,2 m tussen deurpost en wand; er is 2,15 m. Daarom staat de wand hier 10 cm verder: 1,60 m opgeschoven in plaats van 1,50 m (slaapkamer 335 lang).</li>
        </ul></div>
      <div class="card"><h3>B · alternatief: bij het raam</h3>
        <ul class="punt">
          <li>Uitzicht en daglicht recht voor je; past zonder de wand te verschuiven.</li>
          <li>De kachel staat dan op ± 3 m links, en de deur zit schuin achter je.</li>
        </ul></div>
      <div class="card"><h3>Aangenomen, graag nalopen</h3>
        <ul class="chk">
          <li>Hoekstuk: haaks aan de zitkant, links van de stoel.</li>
          <li>Deur: scharnier aan de kant van de kachel.</li>
          <li>Kasten en plank: 60 diep vanaf de voorzetwand.</li>
          <li>Plek van airco en afzuiging.</li>
        </ul></div>
    </div>
  </div>
  <div class="foot">
    <div><span>Project</span><b>Kantoor loods · Gasthuisstraat 6-a, Langenboom</b></div>
    <div><span>Blad</span><b>Plattegrond 1:50 · plek van het bureau</b></div>
    <div><span>Voor</span><b>Julian</b></div>
    <div><span>Datum · status</span><b>14-11-2026 · concept</b></div>
    <div><span>Blad</span><b>1 / 1</b></div>
  </div>
</section>
</body>
</html>
'''

if __name__ == "__main__":
    pad = os.path.join(HERE, "detaillering-kantoor.html")
    open(pad, "w", encoding="utf-8").write(PAGINA % {"plan": plattegrond()})
    print("geschreven:", os.path.relpath(pad, HERE))

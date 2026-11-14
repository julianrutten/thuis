#!/usr/bin/env python3
"""Detaillering van het kantoor in de loods: plattegrond 1:50, aanzicht van de kastenwand 1:25 en doorsnede 1:25.
Schrijft detaillering-kantoor.html; daarna de PDF maken (zie CLAUDE.md).
Maten in mm, zelfde assen als CV/loods_plattegrond.py. x: van de achterwand (0) naar de wand van de slaapkamer.
y: van het sandwichpaneel van de rechtergevel (0) naar de binnenwand (4150). z: hoogte boven de vloer.
Wat met ± is aangegeven, is aangenomen en moet nog worden opgemeten."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t

B = 4150                    # sandwichpaneel tot binnenwand
L = 6550                    # kantoor lang: wand naar de slaapkamer 1,60 m opgeschoven (Julian koos plek A, 14-11-2026)
VZ = 225                    # isolatie en voorzetwand langs de rechtergevel
KD = 600                    # diepte van de kasten en de plank
RAAM = (1600, 2600)         # raam: 160 cm uit de achterwand, 1 m breed
DEUR = (3400, 4300)         # deur naar de loods (plek van de loodsplattegrond, draairichting aangenomen)
NIS = 800                   # diepte van de nis van de kachel
AB = 2100                   # achterwand tot hier langs de accuruimte; daarna de nis
AX = DEUR[1] + 50           # voorkant van het bureau
# ---- hoogtes
PT, PD, PL = 710, 30, 80    # plank: bovenkant (Julian), dikte en plint (aangenomen)
H0 = 1900                   # plafond bij de voorzetwand (aangenomen; wandhoogte van de loods)
HK = 1900                   # hoge kasten: recht onder het laagste punt van het plafond (aangenomen)
RZ0, RZ1 = 950, 1700        # raam: onderkant en bovenkant (aangenomen)
BH = 750                    # bureaublad (aangenomen)
TAN = math.tan(math.radians(16))
YV = B - 800                # vanaf hier is het plafond vlak: de driehoek van 80 cm langs de binnenwand
def dak(y): return H0 + (y - VZ)*TAN                 # onderkant van het dakpakket
def plafond(y): return dak(min(y, YV))

def stijl(k, f):
    p = f".kp.s{k}"
    return (f"{p} .dim{{stroke-width:{8*f}px}}{p} .ext{{stroke-width:{6*f}px}}{p} .dimt{{font-size:{125*f}px}}"
            f"{p} .nm{{font-size:{150*f}px}}{p} .gr{{font-size:{230*f}px}}{p} .tx,{p} .tl,{p} .tr,{p} .ti{{font-size:{128*f}px}}"
            f"{p} .iso,{p} .dak{{stroke-width:{6*f}px}}{p} .kaal{{stroke-width:{9*f}px}}{p} .raam,{p} .raamaan{{stroke-width:{7*f}px}}"
            f"{p} .plank,{p} .kast,{p} .snede{{stroke-width:{10*f}px}}{p} .zicht,{p} .plint,{p} .top{{stroke-width:{6*f}px}}{p} .schuif{{stroke-width:{6*f}px}}"
            f"{p} .bur{{stroke-width:{24*f}px}}"
            f"{p} .aan,{p} .raamaan{{stroke-dasharray:{60*f} {45*f}}}{p} .aan{{stroke-width:{8*f}px}}{p} .app{{stroke-width:{12*f}px}}"
            f"{p} .blad{{stroke-width:{10*f}px}}{p} .zw{{stroke-width:{6*f}px;stroke-dasharray:{45*f} {35*f}}}"
            f"{p} .snl{{stroke-width:{10*f}px;stroke-dasharray:{160*f} {50*f} {20*f} {50*f}}}"
            f"{p} .pijl,{p} .pijl2{{stroke-width:{14*f}px}}{p} .vloer{{stroke-width:{16*f}px}}{p} .plaf{{stroke-width:{12*f}px}}")

STIJL = '''<style>
.kp text{font-family:Inter,Arial,sans-serif}
.kp .dim{fill:none;stroke:#1d1d1b}.kp .ext{fill:none;stroke:#777}.kp .dimt{fill:#1d1d1b;text-anchor:middle}
.kp .nm{font-weight:700;fill:#1d1d1b;text-anchor:middle}.kp .gr{font-weight:700;fill:#1d1d1b;text-anchor:middle}
.kp .tx{fill:#1d1d1b;text-anchor:middle}.kp .tl{fill:#1d1d1b}.kp .tr{fill:#1d1d1b;text-anchor:end}.kp .ti{fill:#333;font-style:italic;text-anchor:middle}
.kp .iso,.kp .dak{fill:#6f6a62;stroke:#1d1d1b}.kp .kaal{fill:#fff;stroke:#1d1d1b}.kp .gat{fill:#fff;stroke:none}
.kp .raam,.kp .raamaan{fill:#fff;stroke:#1d1d1b}
.kp .plank,.kp .snede{fill:#fff;stroke:#1d1d1b}.kp .kast{fill:#e1ded7;stroke:#1d1d1b}
.kp .zicht{fill:#eeece7;stroke:#555}.kp .plint{fill:#cfcbc3;stroke:#555}.kp .top{fill:#55514b;stroke:#1d1d1b}
.kp .schuif{fill:none;stroke:#1d1d1b}
.kp .bur{fill:#fff;stroke:#1d1d1b;stroke-linejoin:round}
.kp .aan{fill:none;stroke:#555}.kp .app{fill:#fff;stroke:#1d1d1b}
.kp .blad{fill:none;stroke:#1d1d1b}.kp .zw{fill:none;stroke:#555}.kp .snl{fill:none;stroke:#1d1d1b}
.kp .pijl{fill:none;stroke:#1d1d1b;marker-end:url(#kpkop)}.kp .pijl2{fill:none;stroke:#1d1d1b;marker-end:url(#kpkop);marker-start:url(#kpkop)}
.kp .vloer{fill:none;stroke:#1d1d1b}.kp .plaf{fill:none;stroke:#1d1d1b}
''' + stijl(50, 1) + stijl(25, .5) + '''
</style>'''
KOP = '<defs><marker id="kpkop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#1d1d1b"/></marker></defs>'

def r(x, y, w, h, c): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def R(x, z, w, h, c): return r(x, -(z + h), w, h, c)                    # in aanzicht en doorsnede: z = onderkant
def tx(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}">{s}</text>'
def txr(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}" transform="rotate(-90 {x} {y})">{s}</text>'
def poly(pts, c): return f'<polygon class="{c}" points="' + " ".join(f"{a:.0f},{-b:.0f}" for a, b in pts) + '"/>'

def plattegrond():
    o = [STIJL, KOP]
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
    o.append(tx(RAAM[1]/2 - 300, VZ + 270, "plank op 71 hoog, 60 diep") + tx(RAAM[1]/2 - 300, VZ + 450, "schuifdeuren eronder"))
    o.append(r(RAAM[1], VZ, L - RAAM[1], KD, "kast") + f'<path class="schuif" d="M{RAAM[1]} {VZ+KD-40} H{L}"/>')
    o.append(tx((RAAM[1] + L)/2, VZ + 270, "hoge kasten, 60 diep, met schuifdeuren") + tx((RAAM[1] + L)/2, VZ + 450, "aanzicht op blad 2"))
    # ---- bureau: rug naar de wand van de slaapkamer, hoekstuk in de hoek tegen de binnenwand
    o.append(r(AX, B - 2000, 1000, 2000, "bur") + r(AX + 1000, B - 600, L - AX - 1000, 600, "bur"))
    o.append(f'<path d="M{AX+1000} {B-588} V{B-12}" stroke="#fff" stroke-width="30"/>')          # naad tussen blad en hoekstuk weg
    o.append(tx(AX + 500, 3050, "bureau", "nm") + tx(AX + 500, 3240, "200 × 100"))
    o.append(tx((AX + 1000 + L)/2, B - 250, "hoekstuk 120 × 60"))
    o.append(f'<circle class="app" cx="{L-600}" cy="2780" r="230"/><path class="pijl" d="M{L-850} 2780 H{AX+1060}"/>')
    t.TK = 45
    o.append(t.chain_h([AX + 1000, L], 3330, ["1200"]))
    o.append(t.chain_v([VZ + KD, B - 2000], AX + 500, ["1325"]))
    o.append(t.chain_h([DEUR[1], AX], B - 2150, [""]) + tx(AX - 25, B - 2210, "50", "tr"))
    # ---- doorsnede C (blad 3): over het raam, gezien naar de slaapkamer
    o.append(f'<path class="snl" d="M2250 -300 V{B+380}"/>' + tx(2140, B + 380, "C", "nm") + tx(2140, -180, "C", "nm"))
    o.append(f'<path class="pijl" d="M2250 {B+330} h300"/><path class="pijl" d="M2250 -235 h300"/>')
    # ---- namen
    o.append(tx(3500, 1500, "Kantoor", "nm") + tx(3500, 1680, "655 × 392 netto"))
    o.append(tx(1200, B + 420, "loods", "ti"))
    o.append(txr(L + 330, 2300, "slaapkamer", "ti"))
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

def aanzicht():
    """Kastenwand langs de rechtergevel, gezien vanuit het kantoor. Horizontaal x, verticaal z."""
    o = []
    o.append(R(0, 0, L, H0, "kaal"))                                                        # wandvlak tot het plafond
    o.append(R(RAAM[0], RZ0, 1000, RZ1 - RZ0, "raamaan") + tx(2100, -1370, "raam", "nm") + tx(2100, -1270, "hoogte opmeten"))
    # ---- plank met de lage kast eronder
    o.append(R(0, 0, RAAM[1], PL, "plint") + R(0, PL, RAAM[1], PT - PD - PL, "plank") + R(0, PT - PD, RAAM[1], PD, "top"))
    o.append(f'<path class="schuif" d="M1300 {-PL} V{-(PT-PD)}"/>')
    for x in (650, 1950):
        o.append(tx(x, -420, "schuifdeur") + f'<path class="pijl2" d="M{x-170} -330 h340"/>')
    o.append(tx(60, -(PT + 55), "plank 60 diep, bovenkant op 71", "tl"))
    o.append(txr(120, -1350, "achterwand (accuruimte)", "ti"))
    # ---- hoge kasten met vier schuifdeuren
    n = 4; bw = (L - RAAM[1])/n
    o.append(R(RAAM[1], 0, L - RAAM[1], PL, "plint") + R(RAAM[1], PL, L - RAAM[1], HK - PL, "kast"))
    for i in range(n):
        x = RAAM[1] + bw*(i + .5)
        if i: o.append(f'<path class="schuif" d="M{RAAM[1]+bw*i:.0f} {-PL} V{-HK}"/>')
        o.append(tx(x, -1080, "schuifdeur ± 99") + f'<path class="pijl2" d="M{x-170:.0f} -990 h340"/>')
    o.append(tx(0, -(H0 + 70), "plafond bij de gevel ± 190 (opmeten); de hoge kasten komen daar recht onder, met een passtrook tegen het schuine plafond", "tl"))
    o.append(f'<path class="vloer" d="M-330 0 H{L+60}"/>')
    # ---- maten
    t.TK = 28
    o.append(t.chain_h([0, RAAM[0], RAAM[1], L], 240, ["1600", "1000 · raam", "3950"], frm=30))
    o.append(t.chain_h([0, 1300, RAAM[1], L], 440, ["1300", "1300", "3950 · hoge kasten tot de wand van de slaapkamer"], frm=270))
    o.append(t.chain_v([-H0, -PT, 0], -200, ["± 1190", "710"], frm=-30))
    t.TK = 26
    return t.svg(f"-330 {-(H0+190)} {L+390} {H0+190+520}", 25, "".join(o), cls="kp")

def doorsnede():
    """Doorsnede C over het raam en de plank, gezien naar de slaapkamer. Horizontaal y (gevel links), verticaal z."""
    o = []
    # ---- dak met isolatie, binnenwand, gevel
    o.append(poly([(-90, dak(-90)), (B + 160, dak(B + 160)), (B + 160, dak(B + 160) + 192), (-90, dak(-90) + 192)], "dak"))
    o.append(poly([(B, 0), (B + 160, 0), (B + 160, dak(B + 160)), (B, dak(B))], "iso"))
    o.append(R(-90, 0, 90, RZ0, "iso") + poly([(-90, RZ1), (0, RZ1), (0, dak(0)), (-90, dak(-90))], "iso"))        # sandwichpaneel
    o.append(R(0, 0, VZ, RZ0, "iso") + poly([(0, RZ1), (VZ, RZ1), (VZ, dak(VZ)), (0, dak(0))], "iso"))            # isolatie en voorzetwand
    o.append(R(-60, RZ0, 30, RZ1 - RZ0, "raamaan"))
    # ---- plafond: volgt het dak, de laatste 80 cm vlak; daarboven de leiding naar het huis
    o.append(f'<path class="plaf" d="M{YV} {-plafond(YV):.0f} H{B}"/>')
    o.append(f'<circle class="app" cx="{B-340}" cy="{-(plafond(YV)+45):.0f}" r="22"/><circle class="app" cx="{B-200}" cy="{-(plafond(YV)+45):.0f}" r="22"/>')
    o.append(tx(B - 60, -2630, "vlak plafond, 80 breed;", "tr") + tx(B - 60, -2540, "erboven de leiding naar het huis", "tr"))
    o.append(tx(2050, -2130, "plafond volgt het dak, 16°"))
    # ---- hoge kasten erachter, lage kast met plank in de snede
    o.append(R(VZ, 0, KD, HK, "zicht") + txr(VZ + 330, -1320, "hoge kasten, erachter", "ti"))
    o.append(R(VZ, 0, KD - 50, PL, "plint") + R(VZ, PL, KD, PT - PD - PL, "snede") + R(VZ, PT - PD, KD, PD, "top"))
    o.append(f'<path class="schuif" d="M{VZ+KD-45} {-PL} V{-(PT-PD)} M{VZ+KD-22} {-PL} V{-(PT-PD)}"/>')
    o.append(tx(VZ + KD/2 - 30, -420, "lage kast") + tx(VZ + KD/2 - 30, -330, "schuifdeuren"))
    # ---- bureau erachter
    o.append(R(B - 2000, BH - 30, 2000, 30, "top") + R(B - 1960, 0, 40, BH - 30, "zicht") + R(B - 60, 0, 40, BH - 30, "zicht"))
    o.append(tx(B - 1000, -(BH + 60), "bureau, erachter"))
    o.append(f'<path class="vloer" d="M-650 0 H{B+500}"/>')
    o.append(tx(2400, -1500, "Kantoor", "nm") + txr(B + 330, -1300, "loods", "ti"))
    # ---- maten
    t.TK = 28
    o.append(t.chain_h([0, VZ, VZ + KD, B - 2000, B], 250, ["225", "600", "1325", "2000 · bureau"], frm=30))
    o.append(t.chain_h([0, B], 450, ["4150 · sandwichpaneel tot binnenwand"], frm=280))
    o.append(t.chain_v([-RZ1, -RZ0, 0], -330, ["± 750 · raam", "± 950"], frm=-110))
    o.append(t.chain_v([-H0, 0], -540, ["± 1900 · plafond bij de gevel"], frm=-360))
    o.append(t.chain_v([-PT, 0], 1080, ["710"], frm=VZ + KD + 20))
    o.append(t.chain_v([-HK, 0], 1330, ["± 1900 · hoge kasten"], frm=VZ + KD + 20))
    o.append(t.chain_v([-BH, 0], B - 2130, ["± 750"]))
    o.append(t.chain_v([-plafond(B), 0], B + 620, [f"± {round(plafond(B), -1):.0f}"], frm=B + 190))
    t.TK = 26
    return t.svg(f"-700 -3330 {B+1450} 3880", 25, "".join(o), cls="kp")

def voet(blad, nr):
    return f'''  <div class="foot">
    <div><span>Project</span><b>Kantoor loods · Gasthuisstraat 6-a, Langenboom</b></div>
    <div><span>Blad</span><b>{blad}</b></div>
    <div><span>Voor</span><b>Julian</b></div>
    <div><span>Datum · status</span><b>14-11-2026 · concept</b></div>
    <div><span>Blad</span><b>{nr} / 3</b></div>
  </div>'''

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
<!-- ============================================================ BLAD 1 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · kantoor in de loods · 14-11-2026</p>
  <h2>Kantoor loods · plattegrond 1:50</h2>
  <p class="sub">Maten in mm, volgens de plattegrond van de loods. Streeplijn = aangenomen. C = doorsnede op blad 3; de kastenwand staat op blad 2.</p>
  <div style="display:grid;grid-template-columns:181mm 1fr;gap:5mm;margin-top:2mm;align-items:start">
    <div>
%(plan)s
      <div class="card" style="margin-top:2mm"><h3>Nog opmeten (op blad 2 en 3 aangenomen, met ±)</h3>
        <ul class="chk" style="columns:2;column-gap:7mm">
          <li>Raam: onderkant en bovenkant boven de vloer.</li>
          <li>Plafondhoogte bij de gevel en bij de binnenwand.</li>
          <li>Hoge kasten: tot het plafond? Hoeveel deuren?</li>
          <li>Hoogte van het bureaublad (de plank ligt op 71).</li>
        </ul></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card"><h3>Bureau</h3>
        <ul class="punt">
          <li>Blad 200 × 100 met hoekstuk 120 × 60, achterin het kantoor: rug naar de wand van de slaapkamer, hoekstuk in de hoek tegen de binnenwand.</li>
          <li>Voorkant van het blad 5 cm naast de deurpost; achter het blad 120 voor de stoel.</li>
          <li>Tussen de kasten en het bureau 1,3 m loopruimte.</li>
        </ul></div>
      <div class="card"><h3>Wand naar de slaapkamer</h3>
        <ul class="punt">
          <li>1,60 m opgeschoven (was 1,50 m): bureau 100 + hoekstuk 120 vragen 2,2 m tussen deurpost en wand.</li>
          <li>Kantoor 655 lang, slaapkamer 335 lang.</li>
        </ul></div>
      <div class="card"><h3>Kastenwand langs de rechtergevel</h3>
        <ul class="punt">
          <li>Van de achterwand tot voorbij het raam: plank op 71 hoog, 60 diep, met schuifdeuren eronder.</li>
          <li>Daarna tot de wand van de slaapkamer: hoge kasten van 60 diep met schuifdeuren.</li>
          <li>Het raam blijft zichtbaar.</li>
        </ul></div>
      <div class="card"><h3>Aangenomen, graag nalopen</h3>
        <ul class="chk">
          <li>Hoekstuk: haaks aan de zitkant, links van de stoel.</li>
          <li>Deur: 3,40 m uit de achterwand, scharnier aan de kant van de kachel.</li>
          <li>Plek van airco en afzuiging.</li>
        </ul></div>
    </div>
  </div>
%(voet1)s
</section>
<!-- ============================================================ BLAD 2 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · kantoor in de loods · 14-11-2026</p>
  <h2>Kastenwand langs de rechtergevel · aanzicht 1:25</h2>
  <p class="sub">Gezien vanuit het kantoor. Maten in mm; ± = aangenomen, nog opmeten. Streeplijn = hoogte van het raam aangenomen.</p>
  <div style="margin-top:2mm">
%(aanzicht)s
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;margin-top:2.5mm;align-items:start">
    <div class="card"><h3>Plank en lage kast</h3>
      <ul class="punt">
        <li>Plank 60 diep met de bovenkant op 71, van de achterwand tot voorbij het raam: 2600 lang.</li>
        <li>Eronder een lage kast met twee schuifdeuren van 130, zoals nu.</li>
        <li>Het raam blijft vrij; de voorzetwand krijgt daar een opening met dagkanten.</li>
      </ul></div>
    <div class="card"><h3>Hoge kasten</h3>
      <ul class="punt">
        <li>Van het raam tot de wand van de slaapkamer: 3950 lang, 60 diep.</li>
        <li>Vier schuifdeuren van ± 99 op twee rails.</li>
        <li>± 190 hoog, recht onder het laagste punt van het plafond; de wig erboven (0 tot ± 17 cm) dicht met een passtrook.</li>
      </ul></div>
    <div class="card"><h3>Aangenomen (±), nog opmeten</h3>
      <ul class="chk">
        <li>Plafond bij de gevel: 190.</li>
        <li>Raam: onderkant 95, bovenkant 170.</li>
        <li>Plint 8, plank 3 dik.</li>
        <li>Aantal en breedte van de schuifdeuren.</li>
      </ul></div>
  </div>
%(voet2)s
</section>
<!-- ============================================================ BLAD 3 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · kantoor in de loods · 14-11-2026</p>
  <h2>Doorsnede C over het raam · 1:25</h2>
  <p class="sub">Gezien naar de slaapkamer; de plek van de snede staat op blad 1. Maten in mm; ± = aangenomen, nog opmeten.</p>
  <div style="display:grid;grid-template-columns:224mm 1fr;gap:4mm;margin-top:2mm;align-items:start">
    <div>
%(doorsnede)s
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card"><h3>Op de doorsnede</h3>
        <ul class="punt">
          <li>Links de rechtergevel met het raam, rechts de binnenwand naar de loods.</li>
          <li>In de snede: de plank op 71 met de lage kast.</li>
          <li>Erachter: de zijkant van de hoge kasten en het bureau.</li>
          <li>Tussen kasten en bureau 1,3 m loopruimte.</li>
          <li>Boven het bureau is het plafond ± 2,45 tot 2,80 m.</li>
        </ul></div>
      <div class="card"><h3>Aangenomen (±)</h3>
        <ul class="chk">
          <li>Plafond 190 bij de gevel, stijgt 16°.</li>
          <li>Vlak op ± 280 in de laatste 80 cm.</li>
          <li>Bureaublad op 75.</li>
          <li>Raam van 95 tot 170.</li>
        </ul></div>
    </div>
  </div>
%(voet3)s
</section>
</body>
</html>
'''

if __name__ == "__main__":
    pad = os.path.join(HERE, "detaillering-kantoor.html")
    open(pad, "w", encoding="utf-8").write(PAGINA % {
        "plan": plattegrond(), "aanzicht": aanzicht(), "doorsnede": doorsnede(),
        "voet1": voet("Plattegrond 1:50", 1),
        "voet2": voet("Aanzicht kastenwand 1:25", 2), "voet3": voet("Doorsnede C 1:25", 3)})
    print("geschreven:", os.path.relpath(pad, HERE))

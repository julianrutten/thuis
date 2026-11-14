#!/usr/bin/env python3
"""Inrichting van het kantoor in de loods: plattegrond 1:50, aanzicht van de kastenwand 1:25 en doorsnede 1:25.
Zet blad 7, 8 en 9 in "Zelf regelen CV-installatie loods" (zelf-regelen/zelf-regelen-loods.html); daarna de PDF opnieuw maken.
Maten in mm, zelfde assen als CV/loods_plattegrond.py. x: van de achterwand (0) naar de wand van de slaapkamer.
y: van het sandwichpaneel van de rechtergevel (0) naar de binnenwand (4150). z: hoogte boven de vloer.
Wat met ± is aangegeven, is aangenomen en moet nog worden opgemeten."""
import math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t

B = 4150                    # sandwichpaneel tot binnenwand
OUD = 4950                  # de oude wand tussen kantoor en berging
L = 6550                    # kantoor lang: wand naar de slaapkamer 1,60 m opgeschoven
VZ = 225                    # isolatie en voorzetwand langs de rechtergevel
KD = 600                    # diepte van de hoge kasten
RG = 155                    # regelwerk met glaswol tussen de spanten; de hoge kasten staan daar direct tegenaan (geen voorzetwand)
FR = RG + KD                # voorkant van de kastenwand: 755, dus 53 cm vóór de voorzetwand
PDP = FR - VZ               # diepte van de plank en de lage kast: 530
RAAM = (1600, 2600)         # raam: 160 cm uit de achterwand, 1 m breed
DEUR_OUD = (OUD - 120 - 900, OUD - 120)   # bestaande deur naar de loods: 12 cm van de oude wand (Julian); wordt dichtgezet
DEUR = (800, 1700)          # nieuwe deur: 80 cm uit de nis van de kachel (Julian), draait naar buiten; breedte 90 aangenomen
KX = RAAM[1] + 200          # de hoge kasten beginnen 20 cm rechts van het raam (Julian)
NIS = 800                   # diepte van de nis van de kachel
AB = 2100                   # achterwand tot hier langs de accuruimte; daarna de nis
ST = 1200                   # ruimte voor de stoel, tussen het blad en de wand van de slaapkamer (= lengte van het hoekstuk)
AX = L - ST - 1000          # voorkant van het bureau
# ---- hoogtes
PT, PD, PL = 710, 30, 80    # plank: bovenkant (Julian), dikte en plint (aangenomen)
H0 = 1900                   # plafond bij de voorzetwand (aangenomen; wandhoogte van de loods)
HK = 1880                   # hoge kasten: recht onder het laagste punt van het plafond, achter in de wand (aangenomen)
RZ0, RZ1 = 710, 1710        # raam: onderkant op 71, 100 hoog (Julian); de plank ligt dus gelijk met de onderkant
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
.kp .dim{fill:none;stroke:#1d1d1b}.kp .ext{fill:none;stroke:#777}.kp .dimt{fill:#1d1d1b;text-anchor:middle;letter-spacing:0}
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
''' + stijl(50, 1) + stijl(25, .5) + stijl(100, 2) + '''
</style>'''
KOP = '<defs><marker id="kpkop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#1d1d1b"/></marker></defs>'

def r(x, y, w, h, c): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def R(x, z, w, h, c): return r(x, -(z + h), w, h, c)                    # in aanzicht en doorsnede: z = onderkant
def tx(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}">{s}</text>'
def txr(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}" transform="rotate(-90 {x} {y})">{s}</text>'
def poly(pts, c): return f'<polygon class="{c}" points="' + " ".join(f"{a:.0f},{-b:.0f}" for a, b in pts) + '"/>'

def kamer():
    """Wanden, raam, deur, kachel en kastenwand, zonder tekst."""
    o = []
    # ---- rechtergevel: sandwichpaneel, isolatie en voorzetwand; het raam blijft zichtbaar
    o.append(r(-1000, -90, L + 1200, 90, "iso") + r(0, 0, L, RG, "iso") + r(0, RG - 5, KX, VZ - RG + 5, "iso"))   # voorzetwand alleen tot de hoge kasten
    o.append(r(RAAM[0], -90, 1000, VZ + 90, "raam") + f'<path class="schuif" d="M{RAAM[0]} -45 H{RAAM[1]}"/>')
    # ---- achterwand (accuruimte), nis, binnenwand, wand naar de slaapkamer
    o.append(r(-160, 0, 160, AB, "iso") + r(-NIS - 100, AB - 100, NIS + 100, 100, "kaal"))
    o.append(r(-NIS - 100, AB, 100, B - AB, "kaal") + r(-NIS - 100, B, NIS + 100, 100, "kaal"))
    o.append(r(0, B, L + 100, 160, "iso") + r(L, 0, 100, B, "iso"))
    o.append(r(DEUR[0], B - 8, 900, 180, "gat"))
    o.append(f'<path class="blad" d="M{DEUR[0]} {B+160} v900"/><path class="zw" d="M{DEUR[0]} {B+1060} A900 900 0 0 0 {DEUR[1]} {B+160}"/>')
    # ---- kachel in de nis
    o.append(r(-740, 2875, 540, 500, "app"))
    # ---- langs de gevel: plank met schuifdeuren eronder tot het raam, daarna hoge kasten
    o.append(r(0, VZ, KX, PDP, "plank") + f'<path class="schuif" d="M0 {FR-40} H{KX}"/>')
    o.append(r(KX, RG, L - KX, KD, "kast") + f'<path class="schuif" d="M{KX} {FR-40} H{L}"/>')
    return o

def plattegrond():
    o = [STIJL, KOP] + kamer()
    o.append(tx(-470, 3175, "K1", "nm") + tx(-400, 2420, "nis"))
    o.append(r(-200, 2775, 800, 700, "aan") + tx(660, 3170, "80 vrij", "tl"))
    # ---- airco en afzuiging op de achterwand (plek aangenomen)
    o.append(r(20, 1050, 210, 800, "aan") + tx(300, 1400, "airco,", "tl") + tx(300, 1570, "afzuiging", "tl"))
    o.append(tx(-560, 1050, "accu-") + tx(-560, 1220, "ruimte"))
    o.append(tx(1000, VZ + 230, "plank op 71 hoog, 53 diep") + tx(1000, VZ + 400, "schuifdeuren eronder"))
    o.append(tx((KX + L)/2, RG + 270, "hoge kasten, 60 diep, 7 cm in de wand") + tx((KX + L)/2, RG + 450, "schuifdeuren · aanzicht op blad 8"))
    # ---- bureau: rug naar de wand van de slaapkamer, hoekstuk in de hoek tegen de binnenwand
    o.append(r(AX, B - 2000, 1000, 2000, "bur") + r(AX + 1000, B - 600, ST, 600, "bur"))
    o.append(f'<path d="M{AX+1000} {B-588} V{B-12}" stroke="#fff" stroke-width="30"/>')          # naad tussen blad en hoekstuk weg
    o.append(tx(AX + 500, 3050, "bureau", "nm") + tx(AX + 500, 3240, "200 × 100"))
    o.append(tx(AX + 1000 + ST/2, B - 250, "hoekstuk 120 × 60"))
    o.append(f'<circle class="app" cx="{L-600}" cy="2780" r="230"/><path class="pijl" d="M{L-850} 2780 H{AX+1060}"/>')
    t.TK = 45
    o.append(t.chain_h([AX + 1000, L], 3330, ["1200"]))
    o.append(t.chain_v([FR, B - 2000], AX + 500, [str(B - 2000 - FR)]))
    # ---- oude deur: dichtzetten
    o.append(f'<path d="M{DEUR_OUD[0]} {B} v160 M{DEUR_OUD[1]} {B} v160" stroke="#fff" stroke-width="14"/>')
    o.append(tx(sum(DEUR_OUD)/2, B + 420, "oude deur: dichtzetten", "ti"))
    # ---- doorsnede C (blad 9): over het raam, gezien naar de slaapkamer
    o.append(f'<path class="snl" d="M2250 -300 V{B+380}"/>' + tx(2140, B + 380, "C", "nm") + tx(2140, -180, "C", "nm"))
    o.append(f'<path class="pijl" d="M2250 {B+330} h300"/><path class="pijl" d="M2250 -235 h300"/>')
    # ---- namen
    o.append(tx(3000, 1700, "Kantoor", "nm") + tx(3000, 1880, "655 × 392 netto"))
    o.append(tx(3050, B + 420, "loods", "ti"))
    o.append(txr(L + 330, 2300, "slaapkamer", "ti"))
    o.append(tx(0, -700, "rechtergevel · het raam van 1 m blijft zichtbaar, de plank loopt eronder door", "tl"))
    # ---- maten
    t.TK = 55
    o.append(t.chain_h([0, RAAM[0], RAAM[1], KX, L], -420, ["1600", "1000", "", "3750"], frm=-140) + tx((RAAM[1] + KX)/2 + 40, -500, "200", "tl"))
    o.append(t.chain_h([0, DEUR[0], DEUR[1], L], B + 1380, [str(DEUR[0]), "900 · deur", str(L - DEUR[1])], frm=B + 1130))
    o.append(t.chain_h([0, OUD, L], B + 1710, ["4950 · tot de oude wand", "1600 opgeschoven"], frm=B + 1440))
    o.append(tx(DEUR[1] + 130, B + 760, "nieuwe deur,", "tl") + tx(DEUR[1] + 130, B + 930, "draait naar buiten", "tl"))
    o.append(t.chain_v([0, AB, B], -1400, ["2100", "2050 · nis"], frm=-960))
    o.append(t.chain_v([0, RG, FR, B], L + 650, ["", "600", "3395"], frm=L + 160) + tx(L + 400, 125, "155"))
    t.TK = 26
    return t.svg(f"-1650 -880 {L+2500} 6820", 50, "".join(o), cls="kp")

def aanzicht():
    """Kastenwand langs de rechtergevel, gezien vanuit het kantoor. Horizontaal x, verticaal z."""
    o = []
    o.append(R(0, 0, L, H0, "kaal"))                                                        # wandvlak tot het plafond
    o.append(R(RAAM[0], RZ0, 1000, RZ1 - RZ0, "raam") + tx(2100, -1260, "raam", "nm") + tx(2100, -1160, "100 × 100, onderkant op 71"))
    # ---- plank met de lage kast eronder
    o.append(R(0, 0, KX, PL, "plint") + R(0, PL, KX, PT - PD - PL, "plank") + R(0, PT - PD, KX, PD, "top"))
    o.append(f'<path class="schuif" d="M{KX//2} {-PL} V{-(PT-PD)}"/>')
    for x in (KX//4, 3*KX//4):
        o.append(tx(x, -420, "schuifdeur") + f'<path class="pijl2" d="M{x-170} -330 h340"/>')
    o.append(tx(60, -(PT + 55), "plank 53 diep, bovenkant op 71", "tl"))
    o.append(txr(120, -1350, "achterwand (accuruimte)", "ti"))
    # ---- hoge kasten met vier schuifdeuren
    n = 4; bw = (L - KX)/n
    o.append(R(KX, 0, L - KX, PL, "plint") + R(KX, PL, L - KX, HK - PL, "kast"))
    for i in range(n):
        x = KX + bw*(i + .5)
        if i: o.append(f'<path class="schuif" d="M{KX+bw*i:.0f} {-PL} V{-HK}"/>')
        o.append(tx(x, -1080, "schuifdeur ± 94") + f'<path class="pijl2" d="M{x-170:.0f} -990 h340"/>')
    o.append(tx(0, -(H0 + 70), "plafond bij de gevel ± 190 (opmeten); de hoge kasten komen daar recht onder, met een passtrook tegen het schuine plafond", "tl"))
    o.append(f'<path class="vloer" d="M-330 0 H{L+60}"/>')
    # ---- maten
    t.TK = 28
    o.append(t.chain_h([0, RAAM[0], RAAM[1], KX, L], 240, ["1600", "1000 · raam", "200", "3750"], frm=30))
    o.append(t.chain_h([0, KX//2, KX, L], 440, ["1400", "1400", "3750 · hoge kasten tot de wand van de slaapkamer"], frm=270))
    o.append(t.chain_v([-H0, -RZ1, -PT, 0], -200, ["± 190", "1000 · raam", "710"], frm=-30))
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
    o.append(R(-60, RZ0, 30, RZ1 - RZ0, "raam"))
    # ---- plafond: volgt het dak, de laatste 80 cm vlak; daarboven de leiding naar het huis
    o.append(f'<path class="plaf" d="M{YV} {-plafond(YV):.0f} H{B}"/>')
    o.append(f'<circle class="app" cx="{B-340}" cy="{-(plafond(YV)+45):.0f}" r="22"/><circle class="app" cx="{B-200}" cy="{-(plafond(YV)+45):.0f}" r="22"/>')
    o.append(tx(B - 60, -2630, "vlak plafond, 80 breed;", "tr") + tx(B - 60, -2540, "erboven de leiding naar het huis", "tr"))
    o.append(tx(2050, -2130, "plafond volgt het dak, 16°"))
    # ---- hoge kasten erachter, lage kast met plank in de snede
    o.append(R(VZ, 0, PDP, HK, "zicht") + txr(VZ + 300, -1320, "hoge kasten, erachter", "ti"))
    o.append(R(VZ, 0, PDP - 50, PL, "plint") + R(VZ, PL, PDP, PT - PD - PL, "snede") + R(VZ, PT - PD, PDP, PD, "top"))
    o.append(f'<path class="schuif" d="M{FR-45} {-PL} V{-(PT-PD)} M{FR-22} {-PL} V{-(PT-PD)}"/>')
    o.append(tx(VZ + PDP/2 - 30, -420, "lage kast") + tx(VZ + PDP/2 - 30, -330, "schuifdeuren"))
    # ---- bureau erachter
    o.append(R(B - 2000, BH - 30, 2000, 30, "top") + R(B - 1960, 0, 40, BH - 30, "zicht") + R(B - 60, 0, 40, BH - 30, "zicht"))
    o.append(tx(B - 1000, -(BH + 60), "bureau, erachter"))
    o.append(f'<path class="vloer" d="M-650 0 H{B+500}"/>')
    o.append(tx(2700, -1500, "Kantoor", "nm") + txr(B + 330, -1300, "loods", "ti"))
    # ---- maten
    t.TK = 28
    o.append(t.chain_h([0, VZ, FR, B - 2000, B], 250, ["225", "530", str(B - 2000 - FR), "2000 · bureau"], frm=30))
    o.append(t.chain_h([0, B], 450, ["4150 · sandwichpaneel tot binnenwand"], frm=280))
    o.append(t.chain_v([-RZ1, -RZ0, 0], -330, ["1000 · raam", "710"], frm=-110))
    o.append(t.chain_v([-H0, 0], -540, ["± 1900 · plafond bij de gevel"], frm=-360))
    o.append(t.chain_v([-PT, 0], 960, ["710"], frm=FR + 20))
    o.append(t.chain_v([-HK, 0], 1160, ["± 1880 · hoge kasten"], frm=FR + 20))
    o.append(t.chain_v([-BH, 0], B - 2130, ["± 750"]))
    o.append(t.chain_v([-plafond(B), 0], B + 620, [f"± {round(plafond(B), -1):.0f}"], frm=B + 190))
    t.TK = 26
    return t.svg(f"-700 -3330 {B+1450} 3880", 25, "".join(o), cls="kp")

def voet(blad, nr):
    return f"""  <div class="foot">
    <div><span>Project</span><b>CV-installatie loods · Gasthuisstraat 6-a, Langenboom</b></div>
    <div><span>Blad</span><b>{blad}</b></div>
    <div><span>Voor</span><b>Julian</b></div>
    <div><span>Datum · status</span><b>14-11-2026 · concept</b></div>
    <div><span>Blad</span><b>{nr} / 9</b></div>
  </div>"""

BLADEN = """<!-- ============================================================ BLAD 7 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · inrichting van het kantoor · 14-11-2026</p>
  <h2>Kantoor · plattegrond 1:50</h2>
  <p class="sub">Maten in mm, volgens de plattegrond op blad 2. Streeplijn = aangenomen. C = doorsnede op blad 9; de kastenwand staat op blad 8.</p>
  <div style="display:grid;grid-template-columns:181mm 1fr;gap:5mm;margin-top:2mm;align-items:start">
    <div>
%(plan)s
      <div class="card klein" style="margin-top:2mm"><h3>Nog opmeten of kiezen (op blad 8 en 9 aangenomen, met ±)</h3>
        <ul class="chk" style="columns:2;column-gap:7mm;padding-left:0">
          <li>Plafondhoogte bij de gevel en bij de binnenwand.</li>
          <li>Hoge kasten: tot het plafond? Hoeveel deuren?</li>
          <li>Hoogte van het bureaublad (de plank ligt op 71).</li>
          <li>Wand naar de slaapkamer: 1,60 m opgeschoven; voor het bureau hoeft dat niet meer, 1,50 m kan ook.</li>
        </ul></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card klein"><h3>Bureau</h3>
        <ul>
          <li>Blad 200 × 100 met hoekstuk 120 × 60 achterin het kantoor: rug naar de wand van de slaapkamer, hoekstuk in de hoek tegen de binnenwand.</li>
          <li>Achter het blad 1,2 m voor de stoel; tussen de kasten en het bureau 1,4 m.</li>
          <li>Het raam zit schuin rechts voor je; de deur en de kachel zijn in beeld.</li>
        </ul></div>
      <div class="card klein"><h3>Deur verplaatsen</h3>
        <ul>
          <li>Nieuwe deur 80 cm uit de nis van de kachel: 0,80 tot 1,70 m uit de achterwand. Draait naar buiten.</li>
          <li>De oude opening (3,93 tot 4,83 m) dichtzetten, met 100 mm glaswol zoals de rest van die wand.</li>
          <li>Rechts van de deur is het kantoor één doorlopende ruimte van 4,85 m.</li>
          <li>Je komt binnen op ± 1 m van de voorkant van de kachel.</li>
        </ul></div>
      <div class="card klein"><h3>Aangenomen, graag nalopen</h3>
        <ul class="chk" style="padding-left:0">
          <li>Deur: 90 breed, scharnier aan de kant van de kachel.</li>
          <li>Hoekstuk: haaks aan de zitkant, links van de stoel.</li>
          <li>Spanten: ± 1,5 cm vóór het regelwerk; kasten daar uitsparen.</li>
        </ul></div>
    </div>
  </div>
%(voet7)s
</section>
<!-- ============================================================ BLAD 8 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · inrichting van het kantoor · 14-11-2026</p>
  <h2>Kantoor · kastenwand langs de rechtergevel · aanzicht 1:25</h2>
  <p class="sub">Gezien vanuit het kantoor. Maten in mm; ± = aangenomen, nog opmeten.</p>
  <div style="margin-top:2mm">
%(aanzicht)s
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;margin-top:2.5mm;align-items:start">
    <div class="card klein"><h3>Plank en lage kast</h3>
      <ul>
        <li>Plank 53 diep met de bovenkant op 71, van de achterwand tot 20 cm voorbij het raam: 2800 lang.</li>
        <li>Eronder een lage kast met twee schuifdeuren van 140, zoals nu.</li>
        <li>Het raam (100 × 100) begint op 71: de plank ligt gelijk met de onderkant. De voorzetwand krijgt daar een opening met dagkanten.</li>
      </ul></div>
    <div class="card klein"><h3>Hoge kasten</h3>
      <ul>
        <li>Vanaf 20 cm rechts van het raam tot de wand van de slaapkamer: 3750 lang, 60 diep, waarvan 7 cm in de wand (geen voorzetwand erachter; glaswol afdekken met folie).</li>
        <li>Vier schuifdeuren van ± 94 op twee rails. Voor kleding op hangers: de deuren nemen ± 8 cm, binnen blijft ± 52 cm vrij.</li>
        <li>± 188 hoog, recht onder het laagste punt van het plafond; de wig erboven (0 tot ± 17 cm) dicht met een passtrook.</li>
      </ul></div>
    <div class="card klein"><h3>Aangenomen (±), nog opmeten</h3>
      <ul class="chk" style="padding-left:0">
        <li>Plafond bij de gevel: 190.</li>
        <li>Plint 8, plank 3 dik.</li>
        <li>Aantal en breedte van de schuifdeuren.</li>
      </ul></div>
  </div>
%(voet8)s
</section>
<!-- ============================================================ BLAD 9 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · inrichting van het kantoor · 14-11-2026</p>
  <h2>Kantoor · doorsnede C over het raam · 1:25</h2>
  <p class="sub">Gezien naar de slaapkamer; de plek van de snede staat op blad 7. Maten in mm; ± = aangenomen, nog opmeten.</p>
  <div style="display:grid;grid-template-columns:224mm 1fr;gap:4mm;margin-top:2mm;align-items:start">
    <div>
%(doorsnede)s
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card klein"><h3>Op de doorsnede</h3>
        <ul>
          <li>Links de rechtergevel met het raam, rechts de binnenwand naar de loods.</li>
          <li>In de snede: de plank op 71 met de lage kast, 53 diep; het raam begint op dezelfde hoogte.</li>
          <li>Erachter: de hoge kasten (7 cm dieper, in de wand) en het bureau.</li>
          <li>Tussen kasten en bureau 1,4 m loopruimte.</li>
          <li>Boven het bureau is het plafond ± 2,45 tot 2,80 m.</li>
        </ul></div>
      <div class="card klein"><h3>Aangenomen (±)</h3>
        <ul class="chk" style="padding-left:0">
          <li>Plafond 190 bij de gevel, stijgt 16°.</li>
          <li>Vlak op ± 280 in de laatste 80 cm.</li>
          <li>Bureaublad op 75.</li>
        </ul></div>
    </div>
  </div>
%(voet9)s
</section>"""

def vul(pad, naam, inhoud_):
    html = open(pad, encoding="utf-8").read()
    pat = re.compile(r"(<!-- BK:%s -->).*?(<!-- /BK:%s -->)" % (naam, naam), re.S)
    html, n = pat.subn(lambda m: m.group(1) + "\n" + inhoud_ + "\n" + m.group(2), html)
    assert n == 1, (pad, naam)
    open(pad, "w", encoding="utf-8").write(html)
    print("bijgewerkt:", os.path.relpath(pad, HERE), "·", naam)

if __name__ == "__main__":
    vul(os.path.join(HERE, "zelf-regelen", "zelf-regelen-loods.html"), "kantoor", BLADEN % {
        "plan": plattegrond(), "aanzicht": aanzicht(), "doorsnede": doorsnede(),
        "voet7": voet("Kantoor: plattegrond 1:50", 7),
        "voet8": voet("Kantoor: aanzicht kastenwand 1:25", 8), "voet9": voet("Kantoor: doorsnede C 1:25", 9)})

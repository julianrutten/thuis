#!/usr/bin/env python3
"""Plattegrond 1:100 van de ruimtes in de loods, voor blad 2 van "Zelf regelen CV-installatie loods".
Maten van Julian (13-11-2026); wat gestreept is, is aangenomen. Draaien na een wijziging, daarna de PDF opnieuw maken.
Maten in mm. x: van achter (links) naar de straatkant (rechts). y: van de buitenwand (0, boven) naar de binnenwand (4150)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t

B = 4150
K0, K1x = 0, 4950
G0, G1 = 5050, 10000
V0, V1 = 10100, 17980
H0, H1 = 18080, 20050
HB = 2450
T0, T1 = 2550, 3970
TX1 = H0 + 1170

STIJL = '''<style>
.lp .dim{stroke-width:12px}.lp .ext{stroke-width:9px}.lp .dimt{font-size:250px;fill:#1d1d1b;letter-spacing:0}
.lp .nm{font-size:285px;font-weight:700;fill:#1d1d1b;text-anchor:middle}.lp .tx{font-size:250px;fill:#1d1d1b;text-anchor:middle}
.lp .tl{font-size:250px;fill:#1d1d1b}.lp .tr{font-size:250px;fill:#1d1d1b;text-anchor:end}.lp .ti{font-size:250px;fill:#333;font-style:italic}
.lp .iso{fill:#6f6a62;stroke:#1d1d1b;stroke-width:10px}.lp .kaal{fill:#fff;stroke:#1d1d1b;stroke-width:14px}
.lp .gat{fill:#fff;stroke:none}.lp .blad{fill:none;stroke:#1d1d1b;stroke-width:14px}
.lp .zw{fill:none;stroke:#555;stroke-width:9px;stroke-dasharray:70 50}
.lp .aan{fill:none;stroke:#1d1d1b;stroke-width:12px;stroke-dasharray:110 70}
.lp .app{fill:#fff;stroke:#1d1d1b;stroke-width:18px}.lp .rad{fill:#1d1d1b}.lp .raam{fill:#fff;stroke:#1d1d1b;stroke-width:10px}
.lp .pijl{fill:none;stroke:#1d1d1b;stroke-width:22px;marker-end:url(#lpkop)}.lp .ld{stroke:#1d1d1b;stroke-width:8px;fill:none}
</style><defs><marker id="lpkop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#1d1d1b"/></marker></defs>'''

def r(x, y, w, h, c): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def tx(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}">{s}</text>'
def blok(x, y, regels):
    return tx(x, y, regels[0], "nm") + "".join(tx(x, y + 330*(i+1), s) for i, s in enumerate(regels[1:]))
def deur_h(x, y, w, omlaag=True):
    s = 1 if omlaag else -1
    return f'<path class="blad" d="M{x} {y} v{s*w}"/><path class="zw" d="M{x} {y+s*w} A{w} {w} 0 0 {0 if omlaag else 1} {x+w} {y}"/>'
def deur_v(x, y, w, rechts=True):
    s = 1 if rechts else -1
    return f'<path class="blad" d="M{x} {y} h{s*w}"/><path class="zw" d="M{x+s*w} {y} A{w} {w} 0 0 {1 if rechts else 0} {x} {y+w}"/>'

def tekening():
    o = [STIJL]
    o.append(r(-3600, -200, H1 + 100 + 3600, 200, "iso"))
    o.append(r(-160, 0, 160, 900, "iso") + r(-160, 1900, 160, B - 1900 + 160, "iso"))
    o.append(r(-900, 800, 900, 100, "iso") + r(-900, 1900, 900, 100, "iso") + r(-900, 800, 100, 1200, "iso"))
    o.append(r(-160, B, K1x + 260, 100, "kaal"))          # wand naar de loods: al dicht, zonder isolatie
    o.append(r(K1x, 0, 100, B, "iso"))
    o.append(r(G0, B, H1 + 100 - G0, 100, "kaal"))
    o.append(r(G1, 0, 100, B, "kaal") + r(V1, 0, 100, HB + 100, "kaal") + r(H1, 0, 100, B + 100, "kaal"))
    o.append(r(V1, T0, 100, B - T0, "kaal"))
    o.append(r(H0, HB, TX1 + 100 - H0, 100, "kaal") + r(TX1, HB, 100, T1 - HB, "kaal") + r(H0, T1, TX1 + 100 - H0, B - T1, "kaal"))
    for x in (3400, 5600):
        o.append(r(x, B - 10, 900, 190, "gat") + deur_h(x, B, 900, omlaag=False))
    o.append(r(G1 - 10, 2900, 120, 900, "gat") + deur_v(G1, 2900, 900, rechts=False))
    o.append(r(V1 - 10, 800, 120, 900, "gat") + deur_v(V1 + 100, 800, 900, rechts=True))
    o.append(r(18950, -210, 950, 220, "gat") + deur_h(18950, 0, 950, omlaag=True))
    o.append(r(18300, HB - 10, 750, 120, "gat") + f'<path class="blad" d="M18250 {HB+130} h800"/>')
    # kantoor
    o.append(r(2500, -200, 1500, 200, "raam") + '<path class="ld" d="M2500 -100 h1500"/>')
    o.append(r(2500, 40, 1500, 110, "rad") + tx(3250, 480, "R3 · ± 1,3 kW"))
    o.append(r(-740, 1150, 540, 500, "app") + tx(-470, 1500, "K1", "nm"))
    o.append(blok(2700, 1500, ["Kantoor", "415 × 495 · 20,5 m²", "21–22 °C · wand naar de loods kaal", "± 1,3 kW bij −10 °C"]))
    o.append('<path class="ld" d="M-470 1150 V620 H150"/>' + tx(200, 700, "kachel in een nis van 80 cm", "tl"))
    o.append(r(-910, 1000, 120, 800, "gat") + '<path class="pijl" d="M-250 1000 H-1150"/>' + tx(200, 1010, "warmte naar achteren (voorstel)", "tl"))
    o.append('<path class="pijl" d="M500 3500 H-700"/>' + tx(650, 3590, "bestaande afzuiging", "tl"))
    # achter het kantoor
    o.append(f'<rect class="aan" x="-3500" y="0" width="3340" height="2350"/><rect class="aan" x="-3500" y="2500" width="3340" height="{B-2500}"/>')
    o.append('<circle class="app" cx="-1650" cy="1350" r="495"/>' + tx(-1650, 1450, "B1", "nm"))
    o.append('<circle class="app" cx="-2850" cy="650" r="300"/>' + tx(-2850, 750, "X1", "nm"))
    o.append(tx(-2400, 2200, "technische ruimte") + tx(-1830, 3250, "accuruimte", "nm") + tx(-1830, 3580, "niet gemeten"))
    # buiten
    o.append(r(-2500, -1050, 1300, 450, "app") + tx(-1850, -720, "WP1", "nm"))
    o.append('<rect class="aan" x="-950" y="-1000" width="800" height="350"/>')
    o.append(tx(-3500, -1300, "buiten: warmtepomp WP1 naast de buitenunit van de airco (blijft)", "tl"))
    o.append(tx(4300, -480, "buitenwand en dak: sandwichpaneel met 100 of 150 mm steenwol erbij", "tl"))
    # berging, voorkamer, hal, toilet
    o.append(r(6800, 40, 1500, 110, "rad") + tx(7550, 480, "R6 · ± 1 kW"))
    o.append(blok(7525, 1500, ["Berging", "415 × 495 · 20,5 m²", "wordt slaapkamer en deel kantoor", "18 °C · ± 1 kW bij −10 °C"]))
    o.append(r(12000, 40, 2400, 110, "rad") + tx(13200, 480, "R2 · plek aangenomen"))
    o.append(blok(14040, 1600, ["Voorkamer", "415 × 788 · 32,7 m²", "15–16 °C · ± 50 uur per seizoen in gebruik", "± 1,4 kW bij −10 °C · ± 1,8 kW in gebruik"]))
    o.append(f'<rect class="aan" x="{V1-650}" y="2750" width="600" height="1300"/>' + tx(V1 - 760, 3480, "keukenblok", "tr"))
    o.append(blok(19250, 1150, ["Hal", "245 × 197"]))
    o.append(blok((H0 + TX1)/2 + 20, 3050, ["Toilet", "117 × 142"]) + r(H0 + 60, T1 - 150, 700, 90, "rad"))
    o.append(tx(18650, B + 1050, "R4 toilet: 18–19 °C · ± 0,3 kW"))
    o.append(tx(19430, -480, "buitendeur", "tx"))
    # loods en maten
    o.append(tx(9300, B + 1050, "loods · de airco houdt 10–12 °C aan", "ti"))
    t.TK = 100
    o.append(t.chain_h([K0, K1x, G0, G1, V0, V1, H0, H1], B + 2000, ["4950", "", "4950", "", "7880", "", "1970"], frm=B + 1450))
    o.append(t.chain_v([0, B], H1 + 750, ["4150"], frm=H1 + 120))
    t.TK = 26
    return t.svg("-3700 -1650 24800 8050", 100, "".join(o), cls="lp")

if __name__ == "__main__":
    pad = os.path.join(HERE, "zelf-regelen", "zelf-regelen-loods.html")
    html = open(pad, encoding="utf-8").read()
    pat = re.compile(r"(<!-- BK:loodsplan -->).*?(<!-- /BK:loodsplan -->)", re.S)
    html, n = pat.subn(lambda m: m.group(1) + "\n" + tekening() + "\n" + m.group(2), html)
    assert n == 1, "markering BK:loodsplan niet gevonden"
    open(pad, "w", encoding="utf-8").write(html)
    print("bijgewerkt: zelf-regelen/zelf-regelen-loods.html · loodsplan")

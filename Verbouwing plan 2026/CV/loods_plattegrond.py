#!/usr/bin/env python3
"""Plattegrond van de ruimtes in de loods, met de kachel in de nis, de schuine technische ruimte erachter en de accuruimte.
Maten van Julian (13- en 14-11-2026); wat gestreept is, is aangenomen of nog te bepalen.
Zet de tekening op blad 2 van "Zelf regelen CV-installatie loods" (1:100) en op blad CV-02 van de tekenset (uitsnede).
Draaien na een wijziging; daarna de PDF opnieuw maken en de tekenset opnieuw publiceren.
Maten in mm. x: van achter (links) naar de voorgevel (rechts). y: van de rechtergevel (0, boven) naar de binnenwand (4150)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t

B = 4150                                   # binnenmaat van de rechtergevel tot de binnenwand
K0, K1x = 0, 4950                          # kantoor
G0, G1 = 5050, 10000                       # berging (wordt slaapkamer en deel kantoor)
V0, V1 = 10100, 17980                      # voorkamer
H0, H1 = 18080, 20050                      # hal en toilet (197 diep), tegen de voorgevel
HB = 2450                                  # hal breed
T0, T1 = 2550, 3970                        # toilet: 142 dwars op de strook
TX0 = H1 - 1170                            # toilet: 117 langs de strook, tegen de voorgevel
AB, AL = 2000, 4000                        # accuruimte: ± 2 m breed, 4 m lang, tegen de rechtergevel achter het kantoor
NIS = 800                                  # diepte van de nis van de kachel

STIJL = '''<style>
.lp .dim{stroke-width:12px}.lp .ext{stroke-width:9px}.lp .dimt{font-size:250px;fill:#1d1d1b;letter-spacing:0}
.lp .nm{font-size:285px;font-weight:700;fill:#1d1d1b;text-anchor:middle}.lp .tx{font-size:250px;fill:#1d1d1b;text-anchor:middle}
.lp .tl{font-size:250px;fill:#1d1d1b}.lp .tr{font-size:250px;fill:#1d1d1b;text-anchor:end}.lp .ti{font-size:250px;fill:#333;font-style:italic}
.lp .iso{fill:#6f6a62;stroke:#1d1d1b;stroke-width:10px}.lp .kaal{fill:#fff;stroke:#1d1d1b;stroke-width:14px}
.lp .gat{fill:#fff;stroke:none}.lp .blad{fill:none;stroke:#1d1d1b;stroke-width:14px}
.lp .zw{fill:none;stroke:#555;stroke-width:9px;stroke-dasharray:70 50}
.lp .aan{fill:none;stroke:#1d1d1b;stroke-width:12px;stroke-dasharray:110 70}
.lp .schuin{fill:none;stroke:#1d1d1b;stroke-width:60px;stroke-dasharray:260 90}
.lp .duo{fill:none;stroke:#1d1d1b;stroke-width:34px;stroke-dasharray:320 90 50 90}
.lp .app{fill:#fff;stroke:#1d1d1b;stroke-width:18px}.lp .rad{fill:#1d1d1b}.lp .raam{fill:#fff;stroke:#1d1d1b;stroke-width:10px}
.lp .pijl{fill:none;stroke:#1d1d1b;stroke-width:22px;marker-end:url(#lpkop)}.lp .ld{stroke:#1d1d1b;stroke-width:8px;fill:none}
</style><defs><marker id="lpkop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#1d1d1b"/></marker></defs>'''

def r(x, y, w, h, c): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def tx(x, y, s, c="tx"): return f'<text class="{c}" x="{x}" y="{y}">{s}</text>'
def blok(x, y, regels):
    return tx(x, y, regels[0], "nm") + "".join(tx(x, y + 330*(i+1), s) for i, s in enumerate(regels[1:]))
def deur_h(x, y, w, omlaag=True):
    """Deur in een wand langs de strook: opening x..x+w, blad draait naar boven of naar beneden."""
    s = 1 if omlaag else -1
    return f'<path class="blad" d="M{x} {y} v{s*w}"/><path class="zw" d="M{x} {y+s*w} A{w} {w} 0 0 {0 if omlaag else 1} {x+w} {y}"/>'
def deur_v(x, y, w, rechts=True):
    """Deur in een dwarswand: opening y..y+w, blad draait naar rechts of naar links."""
    s = 1 if rechts else -1
    return f'<path class="blad" d="M{x} {y} h{s*w}"/><path class="zw" d="M{x+s*w} {y} A{w} {w} 0 0 {1 if rechts else 0} {x} {y+w}"/>'

def inhoud():
    o = [STIJL]
    # ---- buitenwanden: rechtergevel (boven) en voorgevel (rechts)
    o.append(r(-AL - 100, -200, H1 + 300 + AL, 200, "iso") + r(H1, -200, 200, B + 300, "iso"))
    # ---- kantoor: achterwand naar de accuruimte, wand naar de slaapkamer; de wand naar de loods is kaal
    o.append(r(-160, 0, 160, AB + 100, "iso") + r(K1x, 0, 100, B, "iso"))
    o.append(r(-NIS - 100, B, K1x + NIS + 200, 100, "kaal"))                       # binnenwand kantoor, loopt door langs de nis
    o.append(r(-NIS - 100, AB + 100, 100, B - AB - 100, "kaal"))                    # achterwand van de nis
    o.append(r(G0, B, H1 - G0, 100, "kaal"))                                        # binnenwand berging en voorkamer
    o.append(r(G1, 0, 100, B, "kaal") + r(V1, 0, 100, HB + 100, "kaal"))            # dwarswanden
    # ---- accuruimte tegen de rechtergevel, achter het kantoor
    o.append(r(-AL - 100, AB, AL - 60, 100, "kaal") + r(-AL - 100, 0, 100, AB + 100, "kaal"))
    o.append(tx(-AL/2 - 100, 850, "accuruimte", "nm") + tx(-AL/2 - 100, 1180, "± 2 × 4 m"))
    # ---- schuine technische ruimte achter de nis: van 2 m naar 0, ± 3 m lang
    o.append(f'<path class="schuin" d="M{-NIS-50} {B+50} L{-AL-50} {AB+50}"/>')
    o.append('<circle class="app" cx="-1500" cy="2740" r="495"/>' + tx(-1500, 2840, "B1", "nm"))
    o.append('<circle class="app" cx="-2700" cy="2460" r="300"/>' + tx(-2700, 2560, "X1", "nm"))
    o.append(tx(-2500, B + 700, "technische ruimte, schuin:", "tx") + tx(-2500, B + 1030, "± 3 m lang, van 2 m naar 0", "tx"))
    # ---- nis met de kachel: 80 cm diep, 2 m breed, opening naar achteren
    o.append(r(-740, 2875, 540, 500, "app") + tx(-470, 3225, "K1", "nm"))
    o.append(r(-NIS - 110, 3500, 120, 500, "gat") + f'<path class="pijl" d="M-250 3750 H-1250"/>')
    o.append(tx(200, 3050, "kachel K1 in een nis:", "tl") + tx(200, 3380, "80 cm diep, 2 m breed", "tl"))
    # ---- hal, toilet en keukentje tegen de voorgevel
    o.append(r(H0, HB, H1 - H0, 100, "kaal"))                                       # hal | toilet en keukentje
    o.append(r(TX0 - 100, T0, 100, B - T0, "kaal"))                                 # keukentje | toilet
    o.append(r(TX0, T1, H1 - TX0, B - T1, "kaal"))                                  # rest tot de binnenwand
    # ---- deuren
    o.append(r(3400, B - 10, 900, 120, "gat") + deur_h(3400, B, 900, omlaag=False))             # kantoor - loods
    o.append(r(G1 - 1100, B - 10, 900, 120, "gat") + deur_h(G1 - 1100, B, 900, omlaag=False))   # berging - loods, 20 cm uit de hoek
    o.append(r(G1 - 10, 1625, 120, 900, "gat") + deur_v(G1, 1625, 900, rechts=False))           # berging - voorkamer, in het midden
    o.append(r(V1 - 10, 800, 120, 900, "gat") + deur_v(V1, 800, 900, rechts=False))             # voorkamer - hal
    o.append(r(H1 - 10, 1050, 220, 900, "gat") + deur_v(H1, 1050, 900, rechts=False))           # buitendeur in de voorgevel
    o.append(r(TX0 + 200, HB - 10, 750, 120, "gat") + f'<path class="blad" d="M{TX0+150} {HB+130} h800"/>')   # schuifdeur toilet
    # ---- kantoor
    o.append(r(2500, -200, 1500, 200, "raam") + '<path class="ld" d="M2500 -100 h1500"/>')
    o.append(r(2500, 40, 1500, 110, "rad") + tx(3250, 480, "R3 · ± 1,3 kW"))
    o.append(blok(2700, 1100, ["Kantoor", "415 × 495 · 20,5 m²", "21–22 °C · wand naar de loods kaal", "± 1,3 kW bij −10 °C"]))
    o.append('<path class="pijl" d="M500 500 H-700"/>' + tx(250, 760, "bestaande afzuiging", "tl"))
    # ---- buiten
    o.append(r(-2500, -1050, 1300, 450, "app") + tx(-1850, -720, "WP1", "nm"))
    o.append('<rect class="aan" x="-950" y="-1000" width="800" height="350"/>')
    o.append(tx(-AL - 100, -1300, "buiten: warmtepomp WP1 naast de buitenunit van de airco (blijft)", "tl"))
    o.append(tx(4300, -480, "sandwichpaneel met glaswol erbij: dak 150 mm, rechtergevel 100 mm", "tl"))
    # ---- berging, voorkamer, hal, toilet
    o.append(r(6800, 40, 1500, 110, "rad") + tx(7550, 480, "R6 · ± 1 kW"))
    o.append(blok(7400, 1100, ["Berging", "415 × 495 · 20,5 m²", "wordt slaapkamer en", "deel kantoor · 18 °C", "± 1 kW bij −10 °C"]))
    o.append(r(12000, 40, 2400, 110, "rad") + tx(13200, 480, "R2 · plek aangenomen"))
    o.append(blok(14040, 1600, ["Voorkamer", "415 × 788 · 32,7 m²", "15–16 °C · ± 50 uur per seizoen in gebruik", "± 1,4 kW bij −10 °C · ± 1,8 kW in gebruik"]))
    # ---- duoleiding: boven het vlakke plafond langs de binnenwand naar voren, bij de hal dwars naar de rechtergevel en omlaag (A)
    o.append(f'<path class="duo" d="M{-NIS-100} 3950 H{V1-100} V260"/><circle cx="{V1-100}" cy="260" r="110" fill="#1d1d1b"/>')
    o.append(tx(11400, 3800, "duoleiding boven het plafond, langs de binnenwand", "ti"))
    o.append(tx(V1 - 300, 800, "A · omlaag in een koof,", "tr") + tx(V1 - 300, 1130, "onder de fundering door naar het huis", "tr"))
    o.append(tx(V1 - 420, 3500, "keukentje", "tr") + f'<rect class="aan" x="{H0+60}" y="{T0+60}" width="{TX0-100-H0-120}" height="{B-T0-120}"/>')
    o.append(blok(18800, 420, ["Hal", "245 × 197"]))
    o.append(blok((TX0 + H1)/2, 3150, ["Toilet", "117 × 142"]) + r(TX0 + 60, T1 - 150, 700, 90, "rad"))
    o.append(tx(18200, B + 1050, "R4 toilet: 18–19 °C · ± 0,3 kW"))
    o.append(tx(H1 + 350, 1000, "buitendeur", "tl") + tx(H1 + 350, 1330, "voorgevel", "tl"))
    # ---- loods en maten
    o.append(tx(9300, B + 1050, "loods · de airco houdt 10–12 °C aan", "ti"))
    t.TK = 100
    o.append(t.chain_h([-AL, K0, K1x, G0, G1, V0, V1, H0, H1], B + 2000, ["± 4000", "4950", "", "4950", "", "7880", "", "1970"], frm=B + 1450))
    o.append(t.chain_v([0, B], H1 + 2300, ["4150"], frm=H1 + 320))
    t.TK = 26
    return "".join(o)

def tekening():
    """Hele strook, 1:100, voor de PDF."""
    return t.svg("-4500 -1650 27100 8050", 100, inhoud(), cls="lp")

def detail():
    """Uitsnede kantoor, nis, technische ruimte en accuruimte, voor blad CV-02 van de tekenset (schaalt mee op het scherm)."""
    s = t.svg("-4500 -1650 9800 8050", 50, inhoud(), cls="lp")
    return re.sub(r'style="width:[^"]*"', 'style="max-width:760px;margin:0 auto"', s, count=1)

def vul(pad, naam, inhoud_):
    html = open(pad, encoding="utf-8").read()
    pat = re.compile(r"(<!-- BK:%s -->).*?(<!-- /BK:%s -->)" % (naam, naam), re.S)
    html, n = pat.subn(lambda m: m.group(1) + "\n" + inhoud_ + "\n" + m.group(2), html)
    assert n == 1, (pad, naam)
    open(pad, "w", encoding="utf-8").write(html)
    print("bijgewerkt:", os.path.relpath(pad, HERE), "·", naam)

if __name__ == "__main__":
    vul(os.path.join(HERE, "zelf-regelen", "zelf-regelen-loods.html"), "loodsplan", tekening())
    vul(os.path.join(HERE, "index.html"), "cv02-plan", detail())

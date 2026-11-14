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
import loods_kantoor as k          # de inrichting van het kantoor (blad 7) komt hier op 1:100 terug
import loods_keuken as kk          # de keuken van de voorkamer (blad 10)

B = 4150                                   # binnenmaat van de rechtergevel tot de binnenwand
K0, K1x = 0, 6550                          # kantoor: wand naar de slaapkamer 1,60 m opgeschoven (was 4950), voor het bureau
G0, G1 = 6650, 10000                       # slaapkamer (was berging), 3350 lang
V0, V1 = 10100, 17980                      # voorkamer
H0, H1 = 18080, 20050                      # hal en toilet (197 diep), tegen de voorgevel
HB = 2450                                  # hal breed
T0, T1 = 2550, 3970                        # toilet: 142 dwars op de strook
TX0 = H1 - 1170                            # toilet: 117 langs de strook, tegen de voorgevel
AB, AL = 2000, 4000                        # accuruimte: ± 2 m breed, 4 m lang, tegen de rechtergevel achter het kantoor
NIS = 800                                  # schouw van de kachel: 80 cm in de wand, 24 cm ervoor (zie loods_kantoor.py)
VZ = 225                                   # rechtergevel: 155 mm regelwerk met glaswol + 70 mm voorzetwand, gemeten vanaf het sandwichpaneel

STIJL = '''<style>
.lp .dim{stroke-width:12px}.lp .ext{stroke-width:9px}.lp .dimt{font-size:250px;fill:#1d1d1b;letter-spacing:0}
.lp .nm{font-size:285px;font-weight:700;fill:#1d1d1b;text-anchor:middle}.lp .tx{font-size:250px;fill:#1d1d1b;text-anchor:middle}
.lp .tl{font-size:250px;fill:#1d1d1b}.lp .tr{font-size:250px;fill:#1d1d1b;text-anchor:end}.lp .ti{font-size:250px;fill:#333;font-style:italic}
.lp .iso{fill:#6f6a62;stroke:#1d1d1b;stroke-width:10px}.lp .kaal{fill:#fff;stroke:#1d1d1b;stroke-width:14px}
.lp .gat{fill:#fff;stroke:none}.lp .blad{fill:none;stroke:#1d1d1b;stroke-width:14px}
.lp .zw{fill:none;stroke:#555;stroke-width:9px;stroke-dasharray:70 50}
.lp .aan{fill:none;stroke:#1d1d1b;stroke-width:12px;stroke-dasharray:110 70}
.lp .meub{fill:#fff;stroke:#1d1d1b;stroke-width:10px}
.lp .schuin{fill:none;stroke:#1d1d1b;stroke-width:60px;stroke-dasharray:260 90}
.lp .duo{fill:none;stroke:#1d1d1b;stroke-width:34px;stroke-dasharray:320 90 50 90}
.lp .app{fill:#fff;stroke:#1d1d1b;stroke-width:18px}.lp .rad{fill:#1d1d1b}.lp .raam{fill:#fff;stroke:#1d1d1b;stroke-width:10px}
.lp .pijl{fill:none;stroke:#1d1d1b;stroke-width:22px;marker-end:url(#lpkop)}.lp .ld{stroke:#1d1d1b;stroke-width:8px;fill:none}
.lp .kast{fill:#e1ded7;stroke:#1d1d1b;stroke-width:10px}.lp .bur{fill:#fff;stroke:#1d1d1b;stroke-width:22px}
.lp .gord{fill:none;stroke:#1d1d1b;stroke-width:16px;stroke-dasharray:70 45}
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
    o.append(r(-AL - 100, -90, H1 + 190 + AL, 90, "iso") + r(H1, -90, 90, B + 190, "iso"))      # sandwichpanelen
    o.append(r(0, 0, k.KX, VZ, "iso") + r(k.KX - 5, 0, K1x - k.KX + 5, k.RG, "iso") + r(G0, 0, G1 - G0, VZ, "iso") + r(V0, 0, V1 - V0, VZ, "iso"))   # isolatie en voorzetwand, niet in de hal
    # ---- kantoor: achterwand naar de accuruimte, wand naar de slaapkamer; de wand naar de loods is kaal
    o.append(r(-160, 0, 160, AB + 100, "iso") + r(K1x, 0, 100, B, "iso"))
    o.append(r(-NIS - 100, B, NIS + 100, 100, "kaal") + r(0, B, K1x + 100, 160, "iso"))     # binnenwand: langs de nis kaal, langs het kantoor 100 mm glaswol
    o.append(r(-NIS - 100, AB + 100, 100, B - AB - 100, "kaal"))                    # achterwand van de nis
    o.append(r(G0, B, H1 - G0, 160, "iso"))                                         # binnenwand: slaapkamer, voorkamer, keukentje en toilet van binnenuit 100 mm glaswol (Julian, 14-11-2026)
    o.append(r(G1, 0, 100, B, "iso") + r(V1, 0, 100, HB + 100, "kaal"))             # dwarswanden: slaapkamer-voorkamer 100 mm glaswol, voorkamer-hal kaal
    # ---- accuruimte tegen de rechtergevel, achter het kantoor
    o.append(r(-AL - 100, AB, AL - 60, 100, "kaal") + r(-AL - 100, 0, 100, AB + 100, "kaal"))
    o.append(tx(-AL/2 - 100, 1100, "accuruimte", "nm"))
    # ---- schuine technische ruimte achter de nis: van 2 m naar 0, ± 3 m lang
    o.append(f'<path class="schuin" d="M{-NIS-50} {B+50} L{-AL-50} {AB+50}"/>')
    o.append('<circle class="app" cx="-1650" cy="2700" r="495"/>' + tx(-1650, 2800, "B1", "nm"))
    o.append('<circle class="app" cx="-2700" cy="2460" r="300"/>' + tx(-2700, 2560, "X1", "nm"))
    o.append(tx(-2500, B + 700, "technische ruimte, schuin:", "tx") + tx(-2500, B + 1030, "± 3 m lang, van 2 m naar 0", "tx"))
    # ---- nis met de kachel: 80 cm diep, 2 m breed, opening naar achteren
    o.append(r(0, AB, 240, 100, "kaal") + r(0, B - 100, 240, 100, "kaal"))                              # wangen van de schouw, 24 cm vóór de wand
    o.append(r(-1090, 3035, 540, 80, "app") + '<circle class="app" cx="-1090" cy="3075" r="75"/>')      # rookgasafvoer: achteruit door de wand, in de technische ruimte omhoog door het dak
    o.append(r(-550, 2825, 540, 500, "app") + tx(-280, 3175, "K1", "nm"))                        # 25 cm van de achterwand, midden in de schouw
    o.append(r(-NIS - 110, 3500, 120, 500, "gat") + f'<path class="pijl" d="M-250 3750 H{-NIS-450}"/>')
    # ---- hal, toilet en keukentje tegen de voorgevel
    o.append(r(H0, HB, H1 - H0, 100, "kaal"))                                       # hal | toilet en keukentje
    o.append(r(TX0 - 100, T0, 100, B - T0, "kaal"))                                 # keukentje | toilet
    # het toilet loopt op de tekening door tot de binnenwand: één wand, net als bij de voorkamer (Julian, 14-11-2026)
    # ---- deuren
    o.append(r(3100, B - 10, 900, 190, "gat") + f'<path class="blad" d="M4000 {B} v-900"/><path class="zw" d="M4000 {B-900} A900 900 0 0 0 3100 {B}"/>')   # kantoor - loods: deur op 3,10-4,00 m (83 cm naar links geschoven), achter de bank van de zithoek, draait naar binnen naar de kant van het bureau (Julian); de oude deur (3930-4830) gaat dicht
    o.append(r(G1 - 1100, B - 10, 900, 190, "gat") + f'<path class="blad" d="M{G1-200} {B+160} v900"/><path class="zw" d="M{G1-200} {B+1060} A900 900 0 0 1 {G1-1100} {B+160}"/>')   # slaapkamer - loods, 20 cm uit de hoek: draait naar buiten, rechtsdraaiend: scharnier aan de kant van de voorkamer (Julian, 14-11-2026)
    o.append(r(G1 - 10, 1625, 120, 900, "gat") + deur_v(G1 + 100, 1625, 900, rechts=True))      # slaapkamer - voorkamer, in het midden: draait naar de voorkamer (Julian, 14-11-2026)
    o.append(r(V1 - 10, 1050, 120, 900, "gat") + deur_v(V1, 1050, 900, rechts=False))           # voorkamer - hal, in lijn met de buitendeur
    o.append(r(H1 - 10, 1050, 110, 900, "gat") + deur_v(H1, 1050, 900, rechts=False))           # buitendeur in de voorgevel
    o.append(r(TX0 + 200, HB - 10, 750, 120, "gat") + f'<path class="blad" d="M{TX0+150} {HB+130} h800"/>')   # schuifdeur toilet
    # ---- kantoor
    o.append(r(1600, -90, 1000, VZ + 90, "raam") + tx(2100, -180, "raam, 1 m", "tx"))           # 160 cm van de achterwand; blijft zichtbaar (opening in de voorzetwand)
    # inrichting van blad 7 (bron: loods_kantoor.py), zonder tekst: plank met lage kast, hoge kasten, airco, rooster van de afzuiging
    o.append(r(0, VZ, k.KX, k.PDP, "meub") + r(k.KX, k.RG, K1x - k.KX, k.KD, "kast"))
    o.append(r(60, VZ + 10, 800, 200, "aan") + r(-70, 1300, 70, 300, "raam"))
    (ax, ay, aw, ah), (zx, zy, zw, zh) = k.COCKPIT
    o.append(f'<path class="meub" d="M{ax} {ay} h{aw} v{zy-ay} h{zw} v{zh} h{-zw} v{ay+ah-zy-zh} h{-aw} Z"/>')
    bx, by, bh = k.BANK
    o.append(f'<rect class="meub" x="{bx-375}" y="{by-625}" width="750" height="1250" rx="90" transform="rotate({bh} {bx} {by})"/>')
    tx_, ty_, th = k.TAFEL
    o.append(f'<ellipse class="meub" cx="{tx_}" cy="{ty_}" rx="290" ry="475" transform="rotate({th} {tx_} {ty_})"/>')
    for sx, sy, sh in k.STOELEN:
        o.append(f'<rect class="meub" x="{sx-350}" y="{sy-350}" width="700" height="700" rx="110" transform="rotate({sh} {sx} {sy})"/>')
    o.append(r(k.AX, B - 2000, 1000, 2000, "bur") + r(k.AX + 1000, B - 600, k.ST, 600, "bur") + f'<path d="M{k.AX+1000} {B-586} V{B-14}" stroke="#fff" stroke-width="34"/>')
    o.append(tx(3550, 1500, "Kantoor", "nm"))
    # ---- buiten
    o.append(r(-2500, -1050, 1300, 450, "app") + tx(-1850, -720, "WP1", "nm"))
    o.append('<rect class="aan" x="-950" y="-1000" width="800" height="350"/>')
    o.append(tx(-AL - 100, -1300, "buiten: warmtepomp WP1 naast de buitenunit van de airco (blijft)", "tl"))
    o.append(tx(4300, -480, "rechtergevel: sandwichpaneel, 150 mm glaswol in het regelwerk en 70 mm voorzetwand = 225 mm", "tl"))
    # ---- berging, voorkamer, hal, toilet
    # slaapkamer: bed 2100 x 1800 met het hoofdeind tegen de wand van het kantoor, twee ledikanten 1400 x 700 langs de gevel
    o.append(r(G0, 1525, 2100, 1800, "meub") + f'<path class="ld" d="M{G0+450} 1525 v1800"/>')
    # ledikanten uit elkaar: één tegen de wand van het kantoor, één tegen die van de voorkamer; ertussen een gordijn (Julian, 14-11-2026)
    o.append(r(G0, VZ, 1400, 700, "meub") + r(G1 - 1400, VZ, 1400, 700, "meub"))
    o.append(f'<path class="gord" d="M{(G0+G1)/2} {VZ} v700"/>')
    t.TK = 70
    o.append(t.chain_h([G0 + 1400, G1 - 1400], VZ + 1050, [f"{G1 - G0 - 2800} · gordijn"]))
    o.append(tx(G0 + 1250, 2520, "Slaapkamer", "nm"))
    # vrije ruimte rond het bed: voeteneind tot de wand van de voorkamer, zijkant tot de binnenwand en tot de ledikanten
    o.append(t.chain_h([G0 + 2100, G1], 2900, [str(G1 - G0 - 2100)]))
    o.append(t.chain_v([3325, B], G0 + 1050, [str(B - 3325)]) + t.chain_v([VZ + 700, 1525], G0 + 400, [str(1525 - VZ - 700)]))
    o.append(r(kk.R2[0], VZ + 40, kk.R2[1], 110, "rad") + tx(kk.R2[0] + kk.R2[1]/2, VZ + 480, "R2"))
    # keuken (blad 10): hoekblad tegen de binnenwand met de spoelbak in de nis, aanrecht met kookplaat tegen de rechtergevel
    o.append(r(*kk.NIS_BLAD, "meub") + r(*kk.HOEK_BLAD, "meub") + f'<path d="M{kk.NIS_BLAD[0]} {kk.HOEK_BLAD[1]+12} V{B-12}" stroke="#fff" stroke-width="30"/>')
    o.append(r(*kk.SPOELBAK, "app") + r(*kk.AANRECHT, "meub") + r(*kk.KOOKPLAAT, "app"))
    o.append(tx(14040, 2150, "Voorkamer", "nm"))
    # ---- duoleiding: boven het vlakke plafond langs de binnenwand naar voren, bij de hal dwars naar de rechtergevel en omlaag (A)
    o.append(f'<path class="duo" d="M{-NIS-100} 3950 H{V1-100} V{VZ+130}"/><circle cx="{V1-100}" cy="{VZ+130}" r="110" fill="#1d1d1b"/>')
    o.append(tx(V1 - 340, 800, "A", "nm"))
    o.append(tx(18800, 620, "Hal", "nm"))
    o.append(tx((TX0 + H1)/2, 3250, "Toilet", "nm") + r(TX0 + 60, T1 - 150, 400, 90, "rad"))
    o.append(tx(18400, B + 1050, "R4 toilet: 18–19 °C · ± 0,3 kW"))
    o.append(tx(H1 + 350, 1000, "buitendeur", "tl") + tx(H1 + 350, 1330, "voorgevel", "tl"))
    # ---- loods en maten
    o.append(tx(10000, B + 1050, "loods · de airco houdt 10–12 °C aan", "ti"))
    t.TK = 100
    o.append(t.chain_h([-AL, K0, K1x, G0, G1, V0, V1, H0, H1], B + 2000, ["± 4000", "6550", "", "3350", "", "7880", "", "1970"], frm=B + 1450))
    o.append(t.chain_v([0, B], H1 + 2300, ["4150"], frm=H1 + 320))
    t.TK = 26
    return "".join(o)

def tekening():
    """Hele strook, 1:100, voor de PDF."""
    return t.svg("-4500 -1650 27100 8050", 100, inhoud(), cls="lp")

def detail():
    """Uitsnede kantoor, nis, technische ruimte en accuruimte, voor blad CV-02 van de tekenset (schaalt mee op het scherm)."""
    s = t.svg("-4500 -1650 11300 8050", 50, inhoud(), cls="lp")
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

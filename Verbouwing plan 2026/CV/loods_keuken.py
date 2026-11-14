#!/usr/bin/env python3
"""Keuken in de voorkamer van de loods: detailplattegrond 1:40.
Zet blad 10 in "Zelf regelen CV-installatie loods" (zelf-regelen/zelf-regelen-loods.html); daarna de PDF opnieuw maken.
De maten hieronder gebruikt loods_plattegrond.py ook voor de plattegrond 1:100 op blad 2.
Maten in mm, zelfde assen als loods_plattegrond.py. x: van achter naar de voorgevel. y: van de rechtergevel (0) naar de binnenwand (4150)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
sys.dont_write_bytecode = True
import tekening as t
import loods_kantoor as k          # stijl en hulpfuncties

B, VZ = 4150, 225
V1, H0 = 17980, 18080              # wand voorkamer-hal
HB = 2450                          # hal breed; daarna de wand naar de nis en het toilet (2450-2550)
TXW = 18780                        # wand tussen de nis en het toilet (18780-18880)
BD = 635                           # diepte van alle bladen
# ---- hoekkeuken tegen de binnenwand (Julian, 14-11-2026)
NIS_BLAD = (TXW - BD, B - 1425, BD, 1425)        # blad in de nis, 142,5 x 63,5: wordt vervangen; de spoelbak blijft aan de kant van de hal
HOEK_BLAD = (TXW - BD - 1900, B - BD, 1900, BD)  # nieuw hoekblad ertegenaan, 190 x 63,5, langs de binnenwand
SPOELBAK = (TXW - BD + 110, B - 1425 + 60, 420, 420)
VW = HOEK_BLAD[0]                                # vaatwasser: de kast het verst van de hoek (keuze Julian: "de meest rechtse nog beter")
# ---- aanrecht tegen de rechtergevel, tegenover het hoekblad: 200 x 63,5 met inductiekookplaat en afzuigkap
KOOF = 300                                       # hoek bij de hal: de koof met de leiding naar het huis (punt A)
AANRECHT = (V1 - KOOF - 2000, VZ, 2000, BD)
KOOKPLAAT = (AANRECHT[0] + 700, VZ + 60, 600, 520)
R2 = (13700, 1600)                               # radiator R2 schuift op: links van het aanrecht tegen de rechtergevel

r, tx, txr = k.r, k.tx, k.txr

def detail():
    o = ['<style>' + k.stijl(40, .8) + '.kp .rad{fill:#1d1d1b}</style>']
    X0, X1 = 13450, 19500
    # ---- wanden
    o.append(r(X0, -90, X1 - X0, 90, "iso") + r(X0, 0, V1 - X0, VZ, "iso"))                      # rechtergevel: paneel, isolatie en voorzetwand (niet in de hal)
    o.append(r(X0, B, X1 - X0, 160, "iso"))                                                      # binnenwand naar de loods, 100 mm glaswol
    o.append(r(V1, 0, 100, HB + 100, "kaal") + r(H0, HB, X1 - H0, 100, "kaal") + r(TXW, HB + 100, 100, B - HB - 100, "kaal"))
    o.append(r(V1 - 8, 1050, 116, 900, "gat") + f'<path class="blad" d="M{V1} 1050 h-900"/><path class="zw" d="M{V1-900} 1050 A900 900 0 0 0 {V1} 1950"/>')
    # ---- hoekkeuken: blad in de nis en het hoekblad langs de binnenwand
    nx, ny, nw, nh = NIS_BLAD
    hx, hy, hw, hh = HOEK_BLAD
    o.append(r(nx, HB + 100, nw, ny - HB - 100, "aan") + txr(nx + 340, HB + 190, "?", "nm"))
    o.append(r(nx, ny, nw, nh, "plank") + r(hx, hy, hw, hh, "plank"))
    o.append(f'<path d="M{nx} {hy+10} V{B-10}" stroke="#fff" stroke-width="26"/>')                # naad in de hoek weg
    sx, sy, sw, sh = SPOELBAK
    o.append(f'<rect class="app" x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="50"/><circle class="app" cx="{sx+sw/2}" cy="{sy+sh+70}" r="28"/>')
    o.append(txr(nx + 380, ny + 1000, "142,5 × 63,5") + tx(sx + sw/2, sy + sh/2 + 35, "bak"))
    for i in range(1, 4):
        o.append(f'<path class="aan" d="M{hx+600*i} {hy+15} V{B-15}"/>')
    o.append(tx(hx + 300, hy + 300, "vaatwasser") + tx(hx + 300, hy + 440, "60") + tx(hx + 900, hy + 370, "kast 60") + tx(hx + 1500, hy + 370, "kast 60"))
    o.append(tx(hx + 950, hy - 90, "hoekblad 190 × 63,5"))
    # ---- aanrecht tegen de rechtergevel met kookplaat en afzuigkap
    ax, ay, aw, ah = AANRECHT
    o.append(r(ax, ay, aw, ah, "plank"))
    for xx in (ax + 100, ax + 700, ax + 1300, ax + 1900):
        o.append(f'<path class="aan" d="M{xx} {ay+15} V{ay+ah-15}"/>')
    kx, ky, kw, kh = KOOKPLAAT
    o.append(r(kx, ky, kw, kh, "app") + "".join(f'<circle class="schuif" cx="{kx+cx}" cy="{ky+cy}" r="95"/>' for cx in (160, 440) for cy in (140, 380)))
    o.append(f'<path class="pijl" d="M{kx+kw/2} {ky-10} V-640"/>' + tx(kx + kw/2 + 70, -560, "afzuigkap: recht door de gevel", "tl"))
    o.append(tx(ax + 400, ay + 370, "kast 60") + tx(ax + 1600, ay + 370, "kast 60") + tx(ax + 1000, ay + ah + 140, "aanrecht 200 × 63,5 · inductie, 4 zones"))
    o.append(r(ax + aw, VZ, KOOF, KOOF, "aan") + tx(ax + aw + KOOF/2, VZ + 190, "A", "nm"))
    # ---- radiator R2, opgeschoven
    o.append(r(R2[0], VZ + 40, R2[1], 110, "rad") + tx(R2[0] + R2[1]/2, VZ + 290, "R2 · 600 × 1600"))
    # ---- namen
    o.append(tx(16300, 2300, "Voorkamer", "nm") + tx(18800, 1300, "Hal", "nm") + tx(19230, 2950, "Toilet", "nm"))
    o.append(tx(15000, B + 400, "loods", "ti") + tx(14300, -560, "rechtergevel (buiten)", "ti"))
    # ---- maten
    t.TK = 45
    o.append(t.chain_h([R2[0], R2[0] + R2[1], ax, ax + aw, V1], -330, ["1600", str(ax - R2[0] - R2[1]), "2000", str(KOOF)], frm=-110))
    o.append(t.chain_h([hx, nx, TXW], B + 560, ["1900", "635"], frm=B + 200))
    o.append(t.chain_v([VZ, VZ + BD, hy, B], 15250, ["635", str(hy - VZ - BD), "635"], frm=15450))
    o.append(t.chain_v([ny, B], TXW + 300, ["1425"], frm=TXW + 120))
    t.TK = 26
    return t.svg(f"{X0} -800 {X1-X0} {B+1500}", 40, "".join(o), cls="kp")

def voet(blad, nr, van):
    return f"""  <div class="foot">
    <div><span>Project</span><b>CV-installatie loods · Gasthuisstraat 6-a, Langenboom</b></div>
    <div><span>Blad</span><b>{blad}</b></div>
    <div><span>Voor</span><b>Julian</b></div>
    <div><span>Datum · status</span><b>14-11-2026 · concept</b></div>
    <div><span>Blad</span><b>{nr} / {van}</b></div>
  </div>"""

BLAD = """<!-- ============================================================ BLAD 10 -->
<section class="sheet">
  <p class="eyebrow">Eigen werk · keuken in de voorkamer · 14-11-2026</p>
  <h2>Voorkamer · keuken · plattegrond 1:40</h2>
  <p class="sub">Maten in mm. Streeplijn = kastindeling onder het blad of nog te bepalen. De hele voorkamer staat op blad 2.</p>
  <div style="display:grid;grid-template-columns:152mm 1fr;gap:5mm;margin-top:2mm;align-items:start">
    <div>
%(detail)s
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm">
      <div class="card klein"><h3>Hoekkeuken tegen de binnenwand</h3>
        <ul>
          <li>Het blad in de nis (142,5 × 63,5) wordt vervangen; de spoelbak blijft op zijn plek tegen de wand van de hal, op de sanibroyeur.</li>
          <li>Ertegenaan een nieuw hoekblad van 190 × 63,5 langs de binnenwand: drie kasten van 60 en een passtuk van 10 in de hoek.</li>
          <li>Vaatwasser in de kast het verst van de hoek; de afvoer loopt dan ± 2 m onder het blad door naar de spoelbak.</li>
          <li>Warm water vanaf de verswatermodule in de technische ruimte: ± 24 m leiding van 16 mm boven het plafond, ± 30 s wachten. Koud water en afvoer zijn er.</li>
        </ul></div>
      <div class="card klein"><h3>Aanrecht tegen de rechtergevel</h3>
        <ul>
          <li>Blad 200 × 63,5 tegenover het hoekblad, 30 cm uit de wand van de hal: in die hoek komt de koof met de leiding naar het huis (A).</li>
          <li>Inductiekookplaat met vier zones in het midden (krachtstroom is er), kasten van 60 links en rechts, passtukken van 10 aan de uiteinden.</li>
          <li>Afzuigkap erboven, recht door de gevel naar buiten. De wand is daar ± 190 hoog: een vlakke kap of onderbouwkap, met de uitblaas op ± 170.</li>
          <li>Radiator R2 schuift op naar links van het aanrecht.</li>
        </ul></div>
      <div class="card klein"><h3>Nalopen</h3>
        <ul class="chk" style="padding-left:0">
          <li>Kan de sanibroyeur het hete afvalwater van een vaatwasser aan? Een toiletvermaler is daar vaak niet voor gemaakt; een keukenpomp wel.</li>
          <li>De nis: hal 245 + wand + blad 142,5 is ± 397, de strook is 415. Het verschil (± 17 cm, bij "?") nameten.</li>
          <li>Kastmaten: gerekend met drie kasten van 60 per blad.</li>
          <li>Tussen de twee bladen is 2,65 m vrij; de deur van de hal draait daarin open.</li>
        </ul></div>
    </div>
  </div>
%(voet)s
</section>"""

def vul(pad, naam, inhoud_):
    html = open(pad, encoding="utf-8").read()
    pat = re.compile(r"(<!-- BK:%s -->).*?(<!-- /BK:%s -->)" % (naam, naam), re.S)
    html, n = pat.subn(lambda m: m.group(1) + "\n" + inhoud_ + "\n" + m.group(2), html)
    assert n == 1, (pad, naam)
    open(pad, "w", encoding="utf-8").write(html)
    print("bijgewerkt:", os.path.relpath(pad, HERE), "·", naam)

if __name__ == "__main__":
    vul(os.path.join(HERE, "zelf-regelen", "zelf-regelen-loods.html"), "keuken",
        BLAD % {"detail": detail(), "voet": voet("Voorkamer: keuken 1:40", 10, 10)})

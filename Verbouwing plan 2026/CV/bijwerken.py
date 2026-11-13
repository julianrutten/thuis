#!/usr/bin/env python3
"""Zet de bijkeuken-tekeningen uit ../Bijkeuken/tekening.py in de CV-stukken, tussen de BK-markeringen:
  - index.html (tekenset, blad CV-03)
  - detaillering-woning/detaillering.html (bijkeuken op het leidingplan, en blad techniekkast)
Zo tekenen de detaillering bijkeuken, de detaillering CV-installatie en de tekenset dezelfde indeling in dezelfde stijl.
Draaien na elke wijziging van tekening.py. Daarna de PDF's opnieuw maken en de tekenset opnieuw publiceren (zie README.md)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Bijkeuken"))
import tekening as t
sys.path.insert(0, HERE)
import vloerverwarming as vv   # groepenplan vloerverwarming: zones, buisafstand en lengtes

def vul(pad, blokken, css):
    html = open(pad, encoding="utf-8").read()
    for naam, inhoud in blokken.items():
        pat = re.compile(r"(<!-- BK:%s -->).*?(<!-- /BK:%s -->)" % (naam, naam), re.S)
        html, n = pat.subn(lambda m: m.group(1) + "\n" + inhoud + "\n" + m.group(2), html)
        assert n == 1, (pad, naam)
    pat = re.compile(r"(/\* BK-STIJL \*/).*?(/\* /BK-STIJL \*/)", re.S)
    html, n = pat.subn(lambda m: m.group(1) + "\n" + css + "\n" + m.group(2), html)
    assert n == 1, (pad, "stijl")
    open(pad, "w", encoding="utf-8").write(html)
    print("bijgewerkt:", os.path.relpath(pad, HERE), "·", ", ".join(blokken))

def scope(css, pre):
    """Zet elke regel achter een klasse, zodat de tekenstijl niet botst met de stijl van de tekenset."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    uit = []
    for regel in css.split("}"):
        if "{" not in regel: continue
        sel, body = regel.split("{", 1)
        uit.append(",".join(pre + " " + s.strip() for s in sel.split(",")) + "{" + body.strip() + "}")
    return "\n".join(uit)

def scherm(svg, maxb):
    """Voor de tekenset: geen vaste maat in mm, maar meeschalen met de kolom."""
    return re.sub(r'style="width:[^"]*"', f'style="max-width:{maxb}px;margin:0 auto"', svg, count=1)

WAND = t.svg("-420 -100 2020 2800", 20, t.TECHWAND, cls="cv")
ACHTER = t.svg("-200 -100 1120 2800", 20, t.TECHACHTER, cls="cv")
KAST = t.svg("-460 -330 2020 2090", 20, t.TECHPLAN_CV, cls="cv")

# detaillering voor aannemer en loodgieter (A4 liggend, PDF, leesbaar in zwart-wit)
vul(os.path.join(HERE, "detaillering-woning", "detaillering.html"), {
    # plattegrond in de punten van blad 9 van VO4: 1 mm = 0,028346 pt, binnenhoek linksvoor = (602, 568)
    "leidingplan": '<g id="bk" class="bkp" transform="translate(602 432.28) scale(0.028346)">' + t.PLAN_MEUBEL + "</g>",
    "techwand": WAND, "techachter": ACHTER, "techplan": KAST, "vvplan": vv.svg(), "vvtabel": vv.tabel(), "vvzones": "<li><b>Zones</b> (zwart blokje = plek van de thermostaat): " + vv.zones_tekst() + ".</li>",
}, t.CSS_TEKEN)

# tekenset (artifact)
vul(os.path.join(HERE, "index.html"), {
    "cv03-wand": scherm(WAND, 520), "cv03-achter": scherm(ACHTER, 300), "cv03-plan": scherm(KAST, 560),
}, scope(t.CSS_TEKEN, ".bkt") + "\n.bkt text{font-family:var(--f-body)}")

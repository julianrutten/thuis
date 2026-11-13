#!/usr/bin/env python3
"""Bouwt detaillering-bijkeuken.html (A3, negen bladen). Daarna met Chrome naar PDF: zie README.md.
Maten in mm. Plattegrond: x van linkerwand naar rechts, y van achter (0) naar de voorgevel (4788)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tekening import *
DATUM = "13-11-2026"

def foot(blad, schaal, n):
    return f'''<div class="foot"><div><span>Project</span><b>Bijkeuken · Gasthuisstraat 6-a, Langenboom</b></div><div><span>Blad</span><b>{blad}</b></div>
<div><span>Schaal (op A3)</span><b>{schaal}</b></div><div><span>Datum · status</span><b>{DATUM} · concept</b></div><div><span>Bladnummer</span><b>{n} / 9</b></div></div>'''

ELEMENTEN = [
 ("D1","Kapstok in de kastenwand","852 × 600 × 2600"),
 ("D2","Hoge kast, vrij in te delen","680 × 600 × 2600"),
 ("D3","Zitbank onder het raam + bovenkast boven het raam","800 × 500 × 450 / 800 × 600 × 480"),
 ("D4","Schoonmaakkast","444 × 600 × 2600"),
 ("D5","Binnenmuur met inbouwschuifdeur","2776 × 100, doorgang 850"),
 ("W1","Koel/vries-kolom: twee inbouwnissen 880","1280 × 650 × 2600"),
 ("W2","Kast voor wasmachine en droger, gestapeld","680 × 650 × 2600"),
 ("W3","Aanrecht recht, Belgisch hardsteen, met spoelbak","diepte 650–700, h 910"),
 ("W4","Afzuigkap 1400 in koof, kanaal Ø150 door dak","onderkant 1600"),
 ("W5","Open hoekplanken in de bocht boven het blad","3 × diepte 250"),
 ("W6","Bovenkasten boven de spoelbak","1208 × 350 × 1100"),
 ("W7","Pizzaoven Gastro-M GR213 in geventileerde nis","oven 1305 × 600 × 413"),
 ("W8","Hoge voorraadkast","1108 × 615 × 2600"),
]
def eltabel():
    r = "".join(f'<tr><td class="c">{c}</td><td>{e}</td><td class="n">{m}</td></tr>' for c, e, m in ELEMENTEN)
    return f'<table><thead><tr><th>Code</th><th>Element</th><th>Maat (b × d × h)</th></tr></thead><tbody>{r}</tbody></table>'

INSTTABEL = [
 ("KW1","Koud water spoelbak","± 500 (onder aanrecht)","–"),
 ("KW2","Kraan wasmachine (inbouw-aansluitbox in kast W2)","± 550","–"),
 ("WW1","Warm water spoelbak (vanuit de techniekkast in de speelkamer)","± 500","–"),
 ("A1","Afvoer spoelbak Ø40","± 450","–"),
 ("A2","Afvoer wasmachine + condens droger, sifon in inbouwbox","volgens machine","–"),
 ("E1","WCD wasmachine (in bovenkast W2)","± 2000","1"),
 ("E2","WCD droger (in bovenkast W2)","± 2000","2"),
 ("E3","WCD koelkast (achter in bovenkast W1)","± 1800","3"),
 ("E4","WCD vriezer (achter in bovenkast W1)","± 1800","3"),
 ("E5","WCD frituur op het blad, opzij onder de kap","± 1150","4"),
 ("E6","Dubbele WCD werkblad (hoek rechts)","± 1150","5"),
 ("E7","Dubbele WCD werkblad (naast spoelbak)","± 1150","5"),
 ("E8","Aansluiting afzuigkap (in koof)","± 2300","5"),
 ("E11","WCD laadpunt stofzuiger (in schoonmaakkast)","± 1200","6"),
 ("E12","Aansluiting pizzaoven 400 V 3-fase + werkschakelaar","± 250 (achter rooster)","8"),
 ("E13","Voeding 12 V ventilatoren + thermostaat + temperatuurbeveiliging","± 250","8"),
 ("L1","Plafondlicht doorloop","plafond","6"),
 ("L2","Plafondlicht werkruimte","plafond","6"),
 ("L3","LED onder de hoekplanken W5","± 1450","6"),
 ("V1","Afzuigpunt ventilatie werkruimte (plafond)","plafond","–"),
 ("V2","Luchttoevoer: spleet ≥ 10 mm of rooster in schuifdeur","onderkant deur","–"),
 ("V3","Kanaal afzuigkap Ø150 recht door het dak","plafond → dak","–"),
 ("S1","Schakelaar doorloop (bij buitendeur)","1050","6"),
 ("S2","Schakelaar doorloop (bij keukendeur)","1050","6"),
 ("S3","Schakelaar werkruimte (vast wanddeel naast schuifdeur)","1050","6"),
]

CSS = '''
@page{size:420mm 297mm;margin:0}
:root{--ink:#1b1b1b;--muted:#6f6a61;--rule:#d9d5cb;--card:#f8f6f1;--cardrule:#dedad0}
*{box-sizing:border-box} html,body{margin:0;padding:0}
body{font-family:Inter,"Helvetica Neue",Arial,sans-serif;color:var(--ink);font-size:8.3pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.sheet{width:420mm;height:297mm;padding:11mm 14mm 0;position:relative;page-break-after:always;overflow:hidden}
.sheet:last-child{page-break-after:auto}
.eyebrow{font-size:6.4pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 2mm}
h1{font-size:25pt;line-height:1.08;font-weight:700;margin:0 0 4mm;letter-spacing:-.01em}
h2{font-size:14pt;line-height:1.15;font-weight:700;margin:0 0 3mm}
h3{font-size:9.6pt;font-weight:700;margin:0 0 1.6mm}
p{margin:0 0 2mm} .lead{font-size:11.2pt;line-height:1.42;max-width:205mm;margin-bottom:6mm}
.sub{color:var(--muted);font-size:7.6pt;margin:0}
.card{background:var(--card);border:.25mm solid var(--cardrule);border-radius:1.6mm;padding:4mm 5mm}
.card ol,.card ul{margin:0;padding-left:4.4mm} .card li{margin-bottom:1.1mm} .card li:last-child{margin-bottom:0}
ol.n{margin:0;padding-left:4.4mm} ol.n li{margin-bottom:1.1mm}
table{border-collapse:collapse;width:100%;font-size:7.7pt}
th{font-size:5.9pt;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);font-weight:600;text-align:left;padding:0 2mm 1.3mm 0;border-bottom:.35mm solid var(--ink);white-space:nowrap}
td{padding:1.4mm 2mm 1.4mm 0;border-bottom:.2mm solid var(--rule);vertical-align:top} td.c{font-weight:700;white-space:nowrap} td.n{white-space:nowrap}
table.dicht td{padding:1.05mm 2mm 1.05mm 0}
.grid{display:grid;gap:8mm}
.foot{position:absolute;left:14mm;right:14mm;bottom:7.5mm;border-top:.3mm solid var(--ink);display:grid;grid-template-columns:2.6fr 3fr 1.7fr 1.9fr 1fr;font-size:7pt}
.foot div{padding:1.8mm 3mm 0 3mm;border-left:.2mm solid var(--rule);min-height:9mm} .foot div:first-child{border-left:0;padding-left:0}
.foot span{display:block;font-size:5.4pt;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:.6mm} .foot b{font-weight:600}
.key{display:flex;flex-wrap:wrap;gap:1.4mm 5mm;font-size:7.2pt;align-items:center}
.key i{display:inline-block;width:3.2mm;height:3.2mm;border-radius:50%;vertical-align:-.5mm;margin-right:1.4mm} .key i.v{border-radius:.5mm}
.sw{display:inline-block;width:3.6mm;height:3.6mm;vertical-align:-.7mm;margin-right:1.4mm;border:.3mm solid}
.checks{list-style:none;margin:0;padding:0} .checks li{position:relative;padding-left:5.2mm;margin-bottom:1.5mm}
.checks li::before{content:"";position:absolute;left:0;top:.55mm;width:2.6mm;height:2.6mm;border:.3mm solid var(--ink);border-radius:.3mm;background:#fff}
.cap{font-size:7.6pt;margin:1.5mm 0 3mm} .cap b{font-weight:700} .cap span{color:var(--muted)}
svg{display:block} svg text{font-family:Inter,Arial,sans-serif}
ol.n{font-size:7.6pt;color:#333}
''' + CSS_TEKEN
def blad(inhoud, naam, schaal, n):
    return f'<section class="sheet">{inhoud}{foot(naam, schaal, n)}</section>\n'

def kleurkey():
    k = [("kw","koud water",""),("ww","warm water",""),("af","afvoer",""),("el","elektra (WCD)","v"),("sch","schakelaar","v"),("li","licht",""),("ve","ventilatie","")]
    return '<div class="key">' + "".join(f'<span><i class="{c}" style="background:{KLEUR[s]}"></i>{t}</span>' for s, t, c in k) + '</div>'

LEGENDA = ('<div class="key" style="margin-top:4mm">'
  '<span><span class="sw" style="background:#efece5;border-color:#5c5a55"></span>kasten</span>'
  '<span><span class="sw" style="background:#e2e9f1;border-color:#3b5b7a"></span>apparaten</span>'
  '<span><span class="sw" style="background:#6f6a62;border-color:#6f6a62"></span>nieuwe wand</span>'
  '<span><span class="sw" style="background:#fff;border-color:#8a8174;border-style:dashed"></span>boven (kasten, planken, kap)</span></div>')

B = []
# ---------------- 1
B.append(blad(f'''
<div class="grid" style="grid-template-columns:1fr 104mm;gap:12mm;align-items:start">
<div>
<p class="eyebrow">Uitwerking bij ontwerp VO4 (Lenz) · {DATUM} · vervangt de eerdere versie van 13-11-2026</p>
<h1>Bijkeuken · detaillering indeling</h1>
<p class="lead">De berging van 12,6 m² wordt een <b>doorloop</b> met een maatwerk kastenwand langs de voorgevel, met kapstok, kast en zitbank. Daarachter, achter een <b>inbouwschuifdeur</b>, komt een afgesloten <b>werkruimte</b> met aanrecht, koelen en vriezen op hoogte en een kast met wasmachine en droger boven elkaar.</p>
<div class="grid" style="grid-template-columns:1.25fr 1fr;gap:6mm;margin-bottom:6mm;align-items:start">
<div class="card"><h3>Uitgangspunten</h3><ol>
<li>Maten afgelezen uit de PDF van VO4 (1:100): binnenmaat ± 2776 × 4788, plafond 2600, ronde wand R ± 1300. Afleesnauwkeurigheid ± 20–50 mm: <b>alles nameten op de bouw vóór productie.</b></li>
<li>Raamhoogtes (borstwering ± 1000, bovenkant ± 2100) geschat uit het gevelaanzicht: bevestigen bij Lenz.</li>
<li>Maten in mm, hoogtes vanaf de afgewerkte vloer.</li>
<li>Wijzigingen t.o.v. VO4: binnenmuur met inbouwschuifdeur, keukendeur draait andersom, kanaal afzuigkap door het dak.</li>
<li>Werkblad Belgisch hardsteen 30 mm, zelfde als de keuken. Pizzaoven Gastro-M GR213 ingebouwd onder het blad.</li>
<li>Installatiegegevens zijn indicatief. Installateur en elektricien bepalen de definitieve uitvoering.</li></ol></div>
<div style="display:grid;gap:6mm">
<div class="card"><h3>Gewijzigd na het gesprek van 13-11-2026</h3><ol>
<li>De techniekkast van de CV gaat de bijkeuken uit, naar een hoekkast in de speelkamer.</li>
<li>Wasmachine en droger komen terug in de werkruimte, boven elkaar, in kast W2 (680 × 650) tegen de rechterwand.</li>
<li>De voorraadkast W8 ernaast wordt 1108 breed.</li>
<li>Kast D2 in de kastenwand wordt een gewone hoge kast, 600 diep.</li>
<li>De grondleiding uit de loods komt niet meer door de bijkeuken: die komt binnen bij de buitendeur van de eetkamer.</li></ol></div>
<div class="card"><h3>Inhoud</h3><ol>
<li>Voorblad en overzicht</li><li>Plattegrond met maatvoering · 1:25</li><li>Installatieplan · 1:25</li>
<li>Wandaanzichten voorwand en linkerwand · 1:25</li><li>Wandaanzichten achterkant en rechterwand · 1:25</li>
<li>Details doorloop · 1:20</li><li>Details werkruimte · 1:20</li><li>Elementenlijst en elektragroepen</li><li>Aandachtspunten per partij en open vragen</li></ol></div>
</div></div>
{eltabel()}
</div>
<div>{plan("-560 -200 3660 5500", 40, badges=1.55, labels=False)}<p class="cap" style="text-align:center"><span>Overzicht · 1:40 · voorgevel (straat) onderaan</span></p></div>
</div>''', "Voorblad en overzicht", "1:40", 1))

# ---------------- 2
B.append(blad(f'''
<div class="grid" style="grid-template-columns:217mm 1fr;gap:9mm;align-items:start">
<div>{plan("-1830 -260 5430 6170", 25, maten=True)}</div>
<div><h2>Plattegrond met maatvoering</h2>
<p class="sub" style="margin-bottom:5mm">Binnenmaten in mm. Kettingmaten links langs de linkerwand, rechts langs de rechterwand.</p>
{eltabel()}
<div class="card" style="margin-top:6mm"><h3>Belangrijkste maten</h3><ol>
<li>Kastenwand voorgevel: 600 diep over de volle breedte. Loopruimte doorloop 1300.</li>
<li>Binnenmuur 100 dik, voorkant op 1900 uit de voorgevel, in lijn met het kozijn van de buitendeur.</li>
<li>Werkruimte: kolommen 650 diep, vrije loopbreedte 1476.</li>
<li>Werkblad recht: 700 diep langs de achterwand (oven + ventilatie), 650 langs de linkerwand; Belgisch hardsteen 30.</li>
<li>Pizzaoven 1305 breed met 85 ventilatieruimte aan beide kanten; afzuigkap 1400 erboven.</li>
<li>Kast W2 voor wasmachine en droger: 680 × 650, tegen de binnenmuur, deur naar de loopruimte.</li>
<li>Hoge voorraadkast W8 (1108, twee deuren) in het verlengde van W2.</li></ol></div>
{LEGENDA}
</div></div>''', "Plattegrond met maatvoering", "1:25", 2))

# ---------------- 3
rijen = "".join(f'<tr><td class="c">{c}</td><td>{o}</td><td class="n">{h}</td><td class="n">{g}</td></tr>' for c, o, h, g in INSTTABEL)
B.append(blad(f'''
<div class="grid" style="grid-template-columns:160mm 1fr;gap:12mm;align-items:start">
<div>{plan("-560 -200 4000 5500", 25, extra=INSTALL, badges=0, labels=False, cls="fade")}</div>
<div><h2>Installatieplan</h2>{kleurkey()}
<table class="dicht" style="margin-top:4mm"><thead><tr><th>Code</th><th>Omschrijving</th><th>Hoogte</th><th>Groep</th></tr></thead><tbody>{rijen}</tbody></table>
<p class="sub" style="margin-top:2mm">Posities indicatief; groepsnummers verwijzen naar de groepenlijst op blad 8. De techniekkast is een hoekkast in de speelkamer; het leidingplan van de woning staat in de detaillering CV-installatie woning. Geen vloerverwarmingslussen onder vaste kasten en kolommen.</p>
</div></div>''', "Installatieplan", "1:25", 3))

# ---------------- 4
B.append(blad(f'''
<div class="grid" style="grid-template-columns:147mm 1fr;gap:10mm;align-items:start">
<div>{svg("-480 -120 3676 3330", 25, VOORWAND)}
<p class="cap"><b>Voorwand · kastenwand in de doorloop</b> <span>— gezien vanuit de doorloop; links de kant van de keukendeur, rechts de ingang</span></p>
<div class="card"><h3>Voorwand</h3><ol>
<li>Kastenwand 600 diep van vloer tot plafond, fronten in één lijn; plint 100.</li>
<li>Raam: borstwering en bovenkant zijn geschat (±). Bovenkast boven het raam en zitbank eronder op de echte raammaten afstemmen.</li>
<li>Zitbank 450 hoog incl. kussen, 500 diep, twee lades.</li>
<li>Kast D2: hoge kast met twee deuren, vrij in te delen (jassen, schoenen, voorraad).</li></ol></div></div>
<div>{svg("-480 -120 5388 3330", 25, LINKERWAND)}
<p class="cap"><b>Linkerwand</b> <span>— van voorgevel (links) naar achterkant (rechts)</span></p>
<div class="card"><h3>Linkerwand</h3><ol>
<li>Binnenmuur in lijn met het kozijn van de buitendeur (± 12 mm speling).</li>
<li>Koel/vries-kolom W1: lades 100–800, nissen 800–1680, bovenkast 1700–2600. Roosters in plint en bovenin.</li>
<li>Aanrecht 910 hoog, hardsteen 30; spoelkast 500 breed (bak ± 340 × 400), daarnaast de blinde hoek.</li>
<li>Bovenkasten W6 350 diep, onderkant 1500.</li></ol></div></div>
</div>''', "Wandaanzichten voorwand en linkerwand", "1:25", 4))

# ---------------- 5
B.append(blad(f'''
<div class="grid" style="grid-template-columns:147mm 1fr;gap:10mm;align-items:start">
<div>{svg("-480 -120 3676 3330", 25, ACHTERKANT)}
<p class="cap"><b>Achterkant · aanrecht</b> <span>— gezien vanuit de werkruimte (doorsnede achter de kolommen)</span></p>
<div class="card"><h3>Achterkant</h3><ol>
<li>Afzuigkap 1400 in een koof over de volle breedte tot het plafond, onderkant 1600; kanaal recht omhoog door het dak.</li>
<li>Pizzaoven onder het blad tussen twee ventilatiewangen: aanzuigrooster met ventilatoren onderin, uitblaasrooster bovenin (zie blad 7).</li>
<li>Werkblad recht, onderkasten gewone rechte kasten. De hoek rechts achter W8 krijgt open hoekplanken (W5).</li></ol></div></div>
<div>{svg("-480 -120 4688 3330", 25, RECHTERWAND)}
<p class="cap"><b>Rechterwand</b> <span>— van de voorraadkast (links) naar de voorgevel (rechts)</span></p>
<div class="card"><h3>Rechterwand</h3><ol>
<li>Hoge voorraadkast W8 (1108, twee deuren) naast kast W2, achterkant volgt de bocht.</li>
<li>Kast W2 (680 × 650): wasmachine onder, droger boven, bovenkast erboven. Zie blad 7.</li>
<li>Keukendeur: scharnier aan de achterkant, zodat de deur openvalt tegen de binnenmuur.</li></ol></div></div>
</div>''', "Wandaanzichten achterkant en rechterwand", "1:25", 5))

# ---------------- 6
B.append(blad(f'''
<h2>Details doorloop</h2>
<div class="grid" style="grid-template-columns:78mm 1fr;gap:14mm;align-items:start">
<div>{crop(6, 36, 82, 221, 426)}
<p class="cap"><b>D1 · Kapstok</b> <span>— verticale doorsnede · breedte 852</span></p>
<ol class="n">
<li>Bovenkast 600 hoog, deuren tot het plafond (passtrook ± 20 mm).</li>
<li>Hoedenplank op 2000 = onderkant bovenkast.</li>
<li>Kledingroede op 1750, 250 onder de plank (ruimte voor de haken van hangers).</li>
<li>Open nis 450–2000, diepte 600: jassen op hangers. Achter- en zijwanden afgewerkt, bijvoorbeeld fineer.</li>
<li>Twee schoenenlades 100–450; het bovenblad op 450 is te gebruiken als zitje.</li>
<li>Plint 100 hoog, 50 terugliggend.</li>
</ol></div>
<div>{crop(6, 527, 60, 633, 268)}
<p class="cap"><b>D5 · Binnenmuur met inbouwschuifdeur</b> <span>— horizontale doorsnede</span></p>
<ol class="n">
<li>Metal-stud wand 100 mm (bijv. 75 + 2 × 12,5 gips) met isolatie, ook tegen het geluid van afzuigkap, oven en pompen.</li>
<li>Inbouwschuifdeurcassette voor een wand van 100 mm; het wanddeel van 1000 mm wordt de cassette.</li>
<li>Doorgang 850 × 2300, of plafondhoog (2600) voor een strak beeld. Dicht paneel of matglas: glas geeft de werkruimte wat daglicht.</li>
<li>In het cassettedeel geen kasten, haken, schakelaars of leidingen, aan beide kanten. De koel/vries-kolom W1 vrij van deze wand monteren.</li>
<li>Schakelaar werkruimte op het vaste wanddeel rechts van de deur.</li>
<li>Spleet ≥ 10 mm onder de deur of een rooster: luchttoevoer voor de afzuigkap en de ventilatie.</li>
<li>Kast W2 met wasmachine en droger staat tegen het vaste wanddeel rechts; de machines niet aan deze wand bevestigen (trillingen).</li>
</ol></div>
</div>''', "Details doorloop", "1:20", 6))

# ---------------- 7
B.append(blad(f'''
<h2>Details werkruimte</h2>
<div class="grid" style="grid-template-columns:88mm 72mm 1fr;gap:9mm;align-items:start">
<div>{crop(7, 340, 84, 250, 420)}
<p class="cap"><b>W1 · Koel/vries-kolom</b> <span>— verticale doorsnede</span></p>
<ol class="n">
<li>Inbouwkoelkast en inbouwvriezer voor een nis van 880 hoog (vaak 874–880), nisbreedte 560–570, diepte ≥ 550. Montagevoorschrift van het gekozen model volgen.</li>
<li>Nis op 800–1680: de deurgreep zit op ooghoogte, niet bukken.</li>
<li>Ventilatiekanaal ≥ 40–50 mm achter de nissen, van plint tot bovenkast.</li>
<li>Luchtinlaat via een rooster in de plint, uitlaat bovenin; doorsnede volgens voorschrift (vaak ≥ 200 cm²).</li>
<li>Twee lades 100–800 voor voorraad en flessen. Geen vloerverwarming onder deze kolom.</li>
<li>Bovenkast 1700–2600. WCD's (groep 3) achter in de bovenkast of volgens voorschrift.</li>
</ol></div>
<div>{svg("-470 -100 1400 2990", 20, WASKAST)}
<p class="cap"><b>W2 · Kast wasmachine en droger</b> <span>— vooraanzicht zonder deur</span></p>
<ol class="n">
<li>Bovenkast tot het plafond voor wasmiddel; deur over de volle hoogte of gedeeld op 1910.</li>
<li>Inbouw-aansluitbox (kraan + sifon) boven de machines, bereikbaar via de bovenkast. Condens van de droger naar dezelfde sifon.</li>
<li>Twee WCD's (eigen groepen 1 en 2) in de bovenkast.</li>
<li>Droger boven, maximaal 600 breed en 850 hoog.</li>
<li>Tussenplank 30 of stapelkit; machines borgen tegen wandelen.</li>
<li>Wasmachine onder, op een verstevigde bodem met trillingsdempers.</li>
<li>Plint 100 met rooster. De kast is 650 diep, gelijk aan de koel/vries-kolom.</li>
</ol></div>
<div>{crop(7, 622, 60, 540, 545)}</div>
</div>''', "Details werkruimte", "1:20", 7))

# ---------------- 8
EL8 = [
 ("D1","Kapstok","852","600","2600","Open nis 450–2000, roede 1750, hoedenplank 2000, bovenkast 2000–2600, 2 schoenenlades 100–450, plint 100."),
 ("D2","Hoge kast","680","600","2600","Twee deuren, vrij in te delen: legplanken of een roede."),
 ("D3","Zitbank + bovenkast raam","800","500 / 600","450 / 480","Bank met 2 lades en kussen; bovenkast van bovenkant raam tot plafond (op raammaat)."),
 ("D4","Schoonmaakkast","444","600","2600","Laadpunt steelstofzuiger, haken bezem/dweil, legplanken boven."),
 ("D5","Binnenmuur + schuifdeur","2776","100","2600","Metal stud geïsoleerd; cassette 1000; doorgang 850 × 2300 (of plafondhoog); dicht of matglas."),
 ("W1","Koel/vries-kolom","1280","650","2600","Lades 100–800, 2 nissen 880 (800–1680), bovenkast 1700–2600, ventilatiekanaal + roosters."),
 ("W2","Kast wasmachine + droger","680","650","2600","Machines gestapeld, aansluitbox en WCD's in de bovenkast, verstevigde bodem, rooster in de plint."),
 ("W3","Aanrecht recht","± 2000 (voorkant)","650–700","910","Belgisch hardsteen 30; plint 100, onderkasten 780; spoelkast 500, blinde hoeken links en rechts."),
 ("W4","Afzuigkap + koof","1400","600","kap op 1600","Koof volle breedte tot plafond, kanaal Ø150 + terugslagklep + dakdoorvoer."),
 ("W5","Open hoekplanken","in de bocht","250","1450 / 1800 / 2150","Rechts achter, naast de kap; LED eronder."),
 ("W6","Bovenkasten spoelbak","1208","350","1500–2600","Twee deuren."),
 ("W7","Pizzaoven-nis","1476","700","0–880","GR213 op stalen frame (347), ventilatoren + roosters, onbrandbare bekleding, hitteschild onder blad."),
 ("W8","Hoge voorraadkast","1108","± 615","2600","Twee deuren, legplanken; achterkant volgt de bocht."),
]
r8 = "".join(f'<tr><td class="c">{a}</td><td>{b}</td><td class="n">{c}</td><td class="n">{d}</td><td class="n">{e}</td><td>{f}</td></tr>' for a, b, c, d, e, f in EL8)
GR = [("1","Wasmachine","Eigen groep 16 A"),("2","Droger","Eigen groep 16 A"),("3","Koelkast + vriezer","Samen één groep 16 A"),
 ("4","Frituur","Eigen groep 16 A (frituur vaak 2–3 kW)"),("5","WCD's werkblad + afzuigkap","Groep 16 A"),
 ("6","Stofzuigerlaadpunt, verlichting","Groep 16 A (verlichting eventueel apart)"),
 ("7","Vrij","Was het element in het buffervat; dat zit nu in de techniekkast in de hal."),
 ("8","Pizzaoven GR213 6 kW + ventilatoren","Eigen 3-fase groep 400 V (bijv. 3 × 16 A), werkschakelaar; 12 V-voeding ventilatoren en temperatuurbeveiliging op dezelfde groep.")]
rg = "".join(f'<tr><td class="c">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in GR)
B.append(blad(f'''
<div class="grid" style="grid-template-columns:1.6fr 1fr;gap:12mm;align-items:start">
<div><h2>Elementenlijst</h2>
<table><thead><tr><th>Code</th><th>Element</th><th>Breedte</th><th>Diepte</th><th>Hoogte</th><th>Uitvoering</th></tr></thead><tbody>{r8}</tbody></table>
<p class="sub" style="margin-top:2mm">Alle kasten maatwerk, plaatdikte 18 mm, plint 100. Maten zijn buitenmaten van het element; definitieve maten na inmeten op de bouw.</p></div>
<div><h2>Elektragroepen (indicatief)</h2>
<table><thead><tr><th>Groep</th><th>Gebruiker</th><th>Advies</th></tr></thead><tbody>{rg}</tbody></table>
<div class="card" style="margin-top:6mm"><h3>Aansluitwaarde</h3><p style="margin:0">De woning heeft een batterijsysteem van 30 kVA / 100 kWh met power assist (circa 3 × 50 A). Oven (6 kW), droger, wasmachine en frituur samen passen daar ruim in. Laat de elektricien de groepenkast en de verdeling over de fasen wel narekenen.</p></div></div>
</div>''', "Elementenlijst en elektragroepen", "–", 8))

# ---------------- 9
def lijst(items): return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
B.append(blad(f'''
<h2 style="margin-bottom:5mm">Aandachtspunten per partij en open vragen</h2>
<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:6mm;align-items:start">
<div class="card"><h3>Lenz (ontwerp)</h3>{lijst([
 "Binnenmuur met inbouwschuifdeur in de tekening opnemen.",
 "Draairichting keukendeur omdraaien (scharnier aan de achterkant).",
 "Positie dakdoorvoer kanaal afzuigkap vastleggen (midden boven de oven).",
 "Raammaten voorgevel bevestigen: borstwering en bovenkant.",
 "De grondleiding van de CV komt niet door de bijkeuken, maar bij de buitendeur van de eetkamer naar binnen (zie de detaillering CV-installatie woning).",
 "Wat is de nis van ± 1000 × 300 achterin? Kan die als schacht voor leidingen of het kanaal dienen?",
 "Wat is het element van ± 400 × 1600 op de linkerwand in VO4? Dat vervalt in deze indeling."])}</div>
<div class="card"><h3>Installateur</h3>{lijst([
 "De techniekkast staat niet meer in de bijkeuken maar in een hoekkast in de speelkamer. Zie de detaillering CV-installatie woning.",
 "Wasmachine en droger in kast W2 in de werkruimte: koud water en afvoer daarheen, afvoerhoogte afstemmen op de machine.",
 "Warm water voor de spoelbak komt uit de techniekkast in de speelkamer: ± 12 m leiding, dus ± 15 seconden wachten op warm water.",
 "De afvoeren van spoelbak en wasmachine lopen in de vloer naar de standleiding in de techniekkast (zie het leidingplan in de detaillering CV-installatie woning).",
 "Ventilatie: afzuigpunt in de werkruimte en luchttoevoer voor de afzuigkap.",
 "Geen vloerverwarming onder vaste kasten en kolommen."])}</div>
<div class="card"><h3>Elektricien</h3>{lijst([
 "Aansluitwaarde woning en vrije groepen controleren.",
 "3-fase groep pizzaoven + ventilatoren, thermostaat en temperatuurbeveiliging.",
 "Eigen groepen wasmachine, droger en frituur.",
 "WCD's in de bovenkasten van W2 en W1 (bereikbaar).",
 "Geen dozen of leidingen in het cassettedeel van de binnenmuur.",
 "Verlichting werkruimte (geen daglicht) en LED onder de planken."])}</div>
<div class="card"><h3>Interieurbouwer</h3>{lijst([
 "Inmeten op de bouw na het stucwerk, vóór productie.",
 "Kast W2: verstevigde bodem met trillingsdempers, 650 diep, rooster in de plint.",
 "Kast D2: gewone hoge kast, 600 diep, in lijn met de rest van de kastenwand.",
 "Ventilatiekanaal en roosters koel/vries-kolom volgens voorschrift.",
 "Ovennis onbrandbaar bekleden, stalen frame, roosters en hitteschild onder het hardsteen.",
 "Koel/vries-kolom vrij van de cassettewand monteren.",
 "Koof afneembaar voor onderhoud."])}</div>
</div>
<div class="grid" style="grid-template-columns:1.2fr 1.2fr 1fr;gap:6mm;margin-top:6mm;align-items:start">
<div class="card"><h3>Keuzes die nog open staan</h3>{lijst([
 "Kast D2 in de kastenwand is vrijgekomen: jassen, schoenen of voorraad?",
 "Voorraadkast W8 is nu 1108 breed: twee brede deuren of drie smalle?",
 "Zitbank onder het raam, of lage kasten?",
 "Schuifdeur dicht of met matglas; 2300 hoog of plafondhoog?",
 "Pizzaoven: gewicht en akkoord fabrikant op inbouw opvragen.",
 "Ovenhoogte: zo hoog mogelijk onder het blad (mond ± 450–600) akkoord?"])}</div>
<div class="card"><h3>Apparaten kiezen op deze maten</h3>{lijst([
 "Koelkast en vriezer: inbouwmodellen voor een nis van 880 hoog.",
 "Wasmachine en droger: max. 600 breed, 850 hoog, ± 600 diep, stapelbaar; droger bij voorkeur warmtepomp.",
 "Afzuigkap: 1400 breed (horeca- of plafondmodel), inbouw in koof, ruime capaciteit, aansluiting Ø150.",
 "Spoelbak: onderbouw in het hardsteen, bak ± 340 × 400 in een kast van 500."])}</div>
<div class="card"><h3>Volgorde</h3><ol>
<li>Keuzes hiernaast maken en apparaten kiezen.</li><li>Lenz verwerkt binnenmuur, deur, dakdoorvoer en muurdoorvoer in de tekening.</li>
<li>Installateur en elektricien leggen aansluitpunten vast.</li><li>Ruwbouw en installaties; kanaal en leidingen vóór het stucwerk.</li>
<li>Interieurbouwer meet in na het stucwerk en produceert.</li></ol></div>
</div>''', "Aandachtspunten en open vragen", "–", 9))

html = f'''<!DOCTYPE html>
<html lang="nl"><head><meta charset="utf-8"><title>Bijkeuken · detaillering indeling · Gasthuisstraat 6-a</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>{CSS}</style></head><body>
{"".join(B)}</body></html>
'''
open(os.path.join(HERE, "detaillering-bijkeuken.html"), "w", encoding="utf-8").write(html)
print("geschreven", len(html))

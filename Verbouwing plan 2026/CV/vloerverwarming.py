# Groepenplan vloerverwarming: zones in de punten van blad 9 van VO4 (1 pt = 35,28 mm). Oppervlak en buislengte worden hier uitgerekend.
# Vloerafwerking (Julian, 13-11-2026): tegels, behalve slaapkamer, garderobe en zithoek: daar laminaat met een toplaag van echt hout.
# Wensen van Julian (13-11-2026): looproutes eerst; dicht waar je staat (badkamer, aanrecht, voor de bank tot onder de voorrand);
# een warme strook van 0,6 m langs de ruiten van eetkamer en woonkamer tegen stralingskou (niet in speelkamer en slaapkamer);
# 200 mm rond de haard en onder de bank; onder de trap 150 mm (Julian, 13-11-2026; eerst 200); slaapkamer blijft 200; toilet 100 mm (Julian); groep 1 moet de stoelen van de eettafel dekken; nergens stukken overslaan.
# Opzet na de beoordeling van Claude (zelfde dag, door Julian gevraagd om te laten zien): in eetkamer en woonkamer banen die vanaf de
# keukenkant naar de gevel lopen. Elke lus begint bij het glas (eerste 0,6 m op 100 mm). Geen ring van losse stukken meer, geen kruisingen.
# Looproute keuken (boven het kookeiland) op 150 mm: Julian, 13-11-2026: dat is een primaire looproute, 200 mm vond hij te wijd.
# Speelkamer: strook van 100 mm en ±0,9 m diep langs het raam, onder het bureau (Julian, 13-11-2026: comfort bij het zitten).
# Bijkeuken: de doorloop bij de buitendeur op 100 mm (Julian, 13-11-2026: "de binnenkomst moet gezellig warm zijn"); het bovenste deel blijft 150.
# Aanloopleidingen in mantelbuis waar ze door een andere thermostaatzone lopen (speelkamer, garderobe).
# Buisafstanden alleen in veelvouden van 50 mm (100, 150, 200): dat is het raster van de gangbare noppenplaat. Julian vroeg op 13-11-2026
# of de afstanden standaard waren; 75 en 125 mm (eerste versie van deze opzet) waren dat niet en zijn vervallen.
PT = 0.03528
# Een zone is een rechthoek (x, y, b, h, h.o.h., hout) of een veelhoek ("p", [(x, y), ...], h.o.h., hout).
DOORGANG = [(662,429),(703,429),(703,397),(705.2,397.2),(706.9,409.1),(711.4,420.2),(718.7,429.7),(728.2,437),(736,441),(736,442),
            (686,442),(686,470),(684,470),(683.3,462),(680,452.7),(675,444.5),(670,439.4),(665,435.6),(662,433.8)]
HOEK = [(709.5,383),(724,383),(724,395),(752,395),(752,438.6),(740.5,437.2),(730.5,433.1),(721.9,426.5),
        (715.3,417.9),(711.2,407.9),(709.8,397.2),(709.5,397)]
# groep: nr, naam, zones, aanloop enkel (m), bundel, plekken van het nummer [(x, y, h.o.h. die erbij staat)]
G = [
 (1, "Eetkamer links, vanaf de linkerruit", [(600,293,17,136,100,0),(617,293,28,17,100,0),(617,310,28,119,150,0)], 10.5, "N", [(631,370,150),(608.5,345,100)]),
 (2, "Eetkamer rechts, vanaf de bovenruit, en langs de haard", [(645,293,79,17,100,0),(645,310,40,119,150,0),(685,310,18,110,200,0),(703,310,21,7,200,0)], 9.5, "N", [(665,370,150),(675,301.5,100),(694,355,200)]),
 (3, "Woonkamer, vóór de bank · hout", [(752,310,35,132,150,1),(787,310,28,132,100,1)], 3.7, "N", [(767,400,150),(801,400,100)]),
 (4, "Woonkamer, in een U om de bank heen · hout", [(724,293,118,17,100,1),(815,310,27,132,200,1),(724,310,28,85,200,1),("p",HOEK,200,1)], 4.0, "N", [(790,301.5,100),(828.5,345,200),(738,352,200)]),
 (5, "Speelkamer, raamkant, met het bureau", [(850,293,87,25.5,100,0),(850,318.5,87,56.5,150,0)], 2.6, "–", [(893,305.75,100),(893,347,150)]),
 (6, "Speelkamer, kant kast", [(850,375,87,67.5,150,0),(850,442.5,68,23,150,0)], 1.0, "–", [(886,415,150)]),
 (7, "Slaapkamer · hout", [(946,293,103,116,200,1)], 2.6, "O", [(997,351,200)]),
 (8, "Garderobe en halletje · hout", [(946,410,25,21,150,1),(946,431,103,38,150,1),(946,469,25,42,150,1)], 1.0, "O", [(1010,450,150)]),
 (9, "Badkamer, kant deur en wc", [(946,514,57,77,100,0)], 2.5, "O", [(975,530,100)]),
 (10, "Badkamer, wastafels en douche", [(1003,514,46,27,100,0),(1017,541,32,50,100,0)], 4.5, "O", [(1033,563,100)]),
 (11, "Entree, onder de trap en toilet", [(845,487,92,28,150,0),(845,515,92,26,150,0),(845,541,44,26,150,0),(903,545,34,46,100,0)], 1.2, "Z", [(885,505,150),(920,566,100)]),
 (12, "Keuken: aanrecht en rechts van het eiland", [(686,518,156,29,100,0),(804,480,38,38,150,0)], 4.7, "Z", [(764,532.5,100),(818,499,150)]),
 (13, "Keuken: looproute en links van het eiland", [(686,442,156,38,150,0),(686,480,55,38,150,0),("p",DOORGANG,150,0)], 2.7, "N", [(764,465,150),(713.5,499,150)]),
 (14, "Bijkeuken: doorloop en werkruimte", [(621,461,40,49,150,0),(603,515,77,35,100,0)], 10.3, "Z", [(641,485,150),(641,532.5,100)]),
]
# Thermostaatzones (Julian, 13-11-2026): letter, naam, groepen, plek van de thermostaat op de plattegrond (binnenwand, niet bij raam, haard of buitendeur).
# De keuken hoort bij de eethoek (één open ruimte), de bijkeuken is een eigen zone; slaapkamer en garderobe samen.
ZONES = [
 ("A", "Eethoek en keuken", [1, 2, 12, 13], (681, 449)),
 ("B", "Zithoek", [3, 4], (840, 426)),
 ("C", "Kantoor", [5], (933, 352)),
 ("D", "Speelkamer", [6], (933, 400)),
 ("E", "Slaapkamer en garderobe", [7, 8], (951, 392)),
 ("F", "Badkamer", [9, 10], (951, 521)),
 ("G", "Hal", [11], (932, 524)),
 ("H", "Bijkeuken", [14], (676, 503)),
]
ZONE_VAN = {g: z[0] for z in ZONES for g in z[2]}
def zones_tekst(): return " · ".join(f"<b>{l}</b> {naam.lower()} ({', '.join(str(g) for g in gr)})" for l, naam, gr, _ in ZONES)
# aanloopbundels: (pad, in mantelbuis?)
BUNDELS = [("M918 455 L850 451", 1), ("M850 451 H716 L698 437", 0), ("M838 451 L829 441", 0), ("M838 451 L801 441", 0),
           ("M929 482.4 V531 H690", 0), ("M938.2 462 H958 V413", 0), ("M958 462 V511", 1)]
# waar een lus begint: de aanvoer loopt eerst hierlangs
BEGIN = ["M690 425 H609 V300", "M694 432 V302 H650", "M801 438 V318", "M829 438 V302 H735 V385"]
def opp(z):
    if z[0] == "p":
        P = z[1]; a = 0
        for i in range(len(P)):
            x1, y1 = P[i]; x2, y2 = P[(i + 1) % len(P)]; a += x1 * y2 - x2 * y1
        return abs(a) / 2 * PT * PT
    return z[2] * z[3] * PT * PT
def hoh(z): return z[2] if z[0] == "p" else z[4]
def hout(z): return z[3] if z[0] == "p" else z[5]
def punten(z):
    if z[0] == "p": return list(z[1])
    x, y, w, h = z[:4]; return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
def omtrek(zones, alle=None):
    """Buitenrand van aansluitende zones: randen die twee zones delen vallen weg. `alle`: zones waarvan de hoekpunten ook als knippunt gelden."""
    seg = []
    for z in zones:
        P = punten(z); seg += [(P[i], P[(i + 1) % len(P)]) for i in range(len(P))]
    pts = {q for z in (alle or zones) for q in punten(z)}
    def op(a, b, q):  # ligt q strikt tussen a en b op het lijnstuk?
        (ax, ay), (bx, by), (qx, qy) = a, b, q
        if abs((bx - ax) * (qy - ay) - (by - ay) * (qx - ax)) > 1e-6: return None
        L2 = (bx - ax) ** 2 + (by - ay) ** 2; t = ((qx - ax) * (bx - ax) + (qy - ay) * (by - ay)) / L2
        return t if 1e-9 < t < 1 - 1e-9 else None
    stuk = {}
    for a_, b_ in seg:
        ts = sorted(t for t in (op(a_, b_, q) for q in pts) if t is not None)
        ps = [a_] + [(round(a_[0] + t * (b_[0] - a_[0]), 3), round(a_[1] + t * (b_[1] - a_[1]), 3)) for t in ts] + [b_]
        for i in range(len(ps) - 1):
            k = tuple(sorted((ps[i], ps[i + 1]))); stuk[k] = stuk.get(k, 0) + 1
    return [k for k, n in stuk.items() if n == 1]
def rij(g):
    nr, naam, zones, aanloop, bundel, _ = g
    a = sum(opp(z) for z in zones)
    lus = sum(opp(z) * 1000 / hoh(z) for z in zones)
    hohs = " / ".join(str(v) for v in sorted({hoh(z) for z in zones}))
    return nr, naam, hohs, a, lus + 2 * aanloop, bundel
ROWS = [rij(g) for g in G]
N = len(G)
TOT_A = sum(r[3] for r in ROWS); TOT_L = sum(r[4] for r in ROWS)
LANGST = max(r[4] for r in ROWS); KORTST = min(r[4] for r in ROWS)
def nl(x, d=1): return f"{x:.{d}f}".replace(".", ",")
def svg():
    o = ['<svg viewBox="584 283 478 317" style="width:168.6mm;height:111.8mm" xmlns="http://www.w3.org/2000/svg">', '<defs>']
    for v in (100, 150, 200):
        h = v / 35.28
        o.append(f'<pattern id="h{v}" width="10" height="{h:.3f}" patternUnits="userSpaceOnUse"><rect width="10" height="{h:.3f}" fill="#fff" fill-opacity=".55"/><line x1="0" y1="{h/2:.2f}" x2="10" y2="{h/2:.2f}" stroke="#8f3608" stroke-width=".6"/></pattern>')
    o += ['<marker id="pijl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#1b1b1b"/></marker>',
          '<marker id="pijlk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 Z" fill="#1b1b1b"/></marker>',
          '</defs>',
          '<image href="grondplan-vo4.svg" x="0" y="0" width="1190.55" height="841.89"/>',
          '<rect x="584" y="283" width="478" height="317" fill="#fff" opacity=".6"/>']
    # vulling per zone; één doorlopende omtrek per groep (Julian, 13-11-2026: wat bij elkaar hoort loopt door, geen zwarte streep ertussen);
    # waar binnen een groep de buisafstand wisselt alleen een dunne stippellijn
    for nr, naam, zones, aanloop, bundel, plek in G:
        for z in zones:
            o.append(f'<path d="M{" L".join(f"{x} {y}" for x, y in punten(z))} Z" fill="url(#h{hoh(z)})"/>')
    for nr, naam, zones, aanloop, bundel, plek in G:
        rand = omtrek(zones)
        binnen = sorted({k for v in {hoh(z) for z in zones} for k in omtrek([z for z in zones if hoh(z) == v], zones)} - set(rand))
        pad = lambda L: " ".join(f"M{x1} {y1} L{x2} {y2}" for (x1, y1), (x2, y2) in L)
        if binnen: o.append(f'<path d="{pad(binnen)}" fill="none" stroke="#555" stroke-width=".4" stroke-dasharray="1.6 1.6"/>')
        o.append(f'<path d="{pad(rand)}" fill="none" stroke="#1b1b1b" stroke-width="{1.5 if hout(zones[0]) else .45}" stroke-linecap="square"/>')
    # kast met lades en techniekkast
    o.append('<rect x="847.8" y="465.7" width="70.6" height="16.7" fill="#efece6" stroke="#6f6a61" stroke-width=".5"/>')
    o.append('<rect x="918.4" y="442.7" width="19.8" height="39.7" fill="#f9e1cd" stroke="#7a4318" stroke-width=".9"/>')
    # waar een lus begint (dunne pijl)
    for p in BEGIN: o.append(f'<path d="{p}" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/>')
    for p in BEGIN: o.append(f'<path d="{p}" fill="none" stroke="#1b1b1b" stroke-width=".8" stroke-linejoin="round" marker-end="url(#pijlk)"/>')
    # aanloopleidingen: drie bundels; gestreept = in mantelbuis
    for p, m in BUNDELS: o.append(f'<path d="{p}" fill="none" stroke="#fff" stroke-width="4.2" stroke-linejoin="round"/>')
    for p, m in BUNDELS:
        dash = ' stroke-dasharray="3.2 2.2"' if m else ""
        o.append(f'<path d="{p}" fill="none" stroke="#1b1b1b" stroke-width="1.7" stroke-linejoin="round"{dash} marker-end="url(#pijl)"/>')
    T = 'font-family="Inter,Arial,sans-serif"'
    for x, y, t in [(886, 446.5, "N"), (935.5, 508, "Z"), (965, 458.5, "O")]:
        o.append(f'<text x="{x}" y="{y}" {T} font-size="7.4" font-weight="700" fill="#1b1b1b" paint-order="stroke" stroke="#fff" stroke-width="2.4" stroke-linejoin="round">{t}</text>')
    o.append(f'<text x="928.3" y="465.5" {T} font-size="6.4" font-weight="700" text-anchor="middle" fill="#1b1b1b">VD</text>')
    for nr, naam, zones, aanloop, bundel, plek in G:
        for x, y, hh in plek:
            o.append(f'<circle cx="{x}" cy="{y}" r="6.3" fill="#fff" stroke="#1b1b1b" stroke-width=".8"/>'
                     f'<text x="{x}" y="{y+2.5}" {T} font-size="7" font-weight="700" text-anchor="middle" fill="#1b1b1b">{nr}</text>'
                     f'<text x="{x+8.5}" y="{y+2.3}" {T} font-size="7" fill="#1b1b1b" paint-order="stroke" stroke="#fff" stroke-width="2.2" stroke-linejoin="round">{hh}</text>')
    for l, naam, gr, (x, y) in ZONES:
        o.append(f'<rect x="{x-4.6}" y="{y-4.6}" width="9.2" height="9.2" rx="1.2" fill="#1b1b1b" stroke="#fff" stroke-width=".8"/>'
                 f'<text x="{x}" y="{y+2.6}" {T} font-size="7.2" font-weight="700" text-anchor="middle" fill="#fff">{l}</text>')
    o.append('<rect x="590" y="594" width="141.73" height="1.9" fill="#fff" stroke="#1b1b1b" stroke-width=".3"/><rect x="590" y="594" width="28.35" height="1.9" fill="#1b1b1b"/><rect x="646.7" y="594" width="28.35" height="1.9" fill="#1b1b1b"/><rect x="703.4" y="594" width="28.35" height="1.9" fill="#1b1b1b"/>')
    o.append(f'<text x="735" y="596.4" {T} font-size="6.6" fill="#1b1b1b">5 m</text>')
    o.append('</svg>')
    return "\n".join(o)
def tabel():
    r = "".join(f'<tr><td class="c">{nr}</td><td>{naam}</td><td class="n">{hoh}</td><td class="n">{nl(a)}</td><td class="n">± {round(tot/5)*5:.0f} m</td><td class="n">{ZONE_VAN[nr]}</td></tr>' for nr, naam, hoh, a, tot, b in ROWS)
    return ('<table class="vv"><thead><tr><th>Nr</th><th>Ruimte</th><th>h.o.h.</th><th>m²</th><th>Buis</th><th>Zone</th></tr></thead><tbody>' + r +
            f'<tr class="tot"><td></td><td><b>Totaal</b></td><td></td><td class="n"><b>{nl(TOT_A, 0)}</b></td><td class="n"><b>± {round(TOT_L/10)*10:.0f} m</b></td><td></td></tr></tbody></table>')
if __name__ == "__main__":
    for r in ROWS: print(r[0], r[1][:44], r[2], nl(r[3]), round(r[4]), r[5])
    print("totaal", nl(TOT_A), round(TOT_L), "langste", round(LANGST), "kortste", round(KORTST))

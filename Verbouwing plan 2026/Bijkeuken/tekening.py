"""Gedeelde tekeningen van de bijkeuken, in de stijl van de detaillering van 29-10-2026.
Gebruikt door bouw.py (detaillering bijkeuken) en door CV/detaillering-woning/bijwerken.py (detaillering CV-installatie).
Maten in mm. Plattegrond: x van de linkerwand naar rechts, y van achter (0) naar de voorgevel (4788)."""
# ------------------------------------------------------------------ tekenhulpen (stijl van de detaillering van 29-10-2026)
TK = 26
def svg(vb, schaal, inner, cls=""):
    a, b, c, d = [float(v) for v in vb.split()]
    return (f'<svg class="s{schaal} {cls}" viewBox="{vb}" style="width:{c/schaal:.1f}mm;height:{d/schaal:.1f}mm" xmlns="http://www.w3.org/2000/svg">'
            '<defs><pattern id="hatchN" width="44" height="44" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect class="nbg" width="44" height="44"/><line class="nln" x1="0" y1="0" x2="0" y2="44"/></pattern>'
            '<pattern id="muur" width="26" height="26" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="26" height="26" fill="#d9d5cc"/><line x1="0" y1="0" x2="0" y2="26" stroke="#b9b4aa" stroke-width="7"/></pattern></defs>'
            + inner + '</svg>')
def badge(x, y, code, s=1.0):
    w = (150 if len(code) < 3 else 180)*s; h = 100*s
    return (f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="{22*s}" fill="#fff" stroke="#1d1d1b" stroke-width="{7*s}"/>'
            f'<text x="{x}" y="{y+2*s}" class="bdg" style="font-size:{62*s}px">{code}</text>')
def tick(x, y):
    return f'<line class="dim" x1="{x-TK}" y1="{y+TK}" x2="{x+TK}" y2="{y-TK}"/>'
def chain_h(xs, y, labels, frm=None):
    out = f'<line class="dim" x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}"/>'
    for x in xs:
        out += tick(x, y)
        if frm is not None: out += f'<line class="ext" x1="{x}" y1="{frm}" x2="{x}" y2="{y+(55 if y > frm else -55)}"/>'
    for a, b, t in zip(xs, xs[1:], labels):
        if t: out += f'<text class="dimt" x="{(a+b)/2}" y="{y-26}">{t}</text>'
    return out
def chain_v(ys, x, labels, frm=None):
    out = f'<line class="dim" x1="{x}" y1="{ys[0]}" x2="{x}" y2="{ys[-1]}"/>'
    for y in ys:
        out += tick(x, y)
        if frm is not None: out += f'<line class="ext" x1="{frm}" y1="{y}" x2="{x+(-55 if x < frm else 55)}" y2="{y}"/>'
    for a, b, t in zip(ys, ys[1:], labels):
        if t:
            lvl = 0
            if isinstance(t, tuple): t, lvl = t
            m = (a+b)/2; tx = x-26-75*lvl
            out += f'<text class="dimt" x="{tx}" y="{m}" transform="rotate(-90 {tx} {m})">{t}</text>'
    return out
def hdim(x1, x2, y, t, frm=None): return chain_h([x1, x2], y, [t], frm)
def vdim(y1, y2, x, t, frm=None): return chain_v([y1, y2], x, [t], frm)
def mark(x, y, n, r=37):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#1d1d1b"/><text x="{x}" y="{y+1}" class="dott" style="font-size:{r*1.12:.0f}px">{n}</text>'

# ------------------------------------------------------------------ plattegrond (x van links naar rechts, y van achter naar de voorgevel)
PLAN_VLOER = '''
<path class="floor" d="M 0 300 L 1100 300 L 1100 0 L 1478 0 A 1298 1298 0 0 1 2776 1299 L 2776 4788 L 0 4788 Z"/>
'''
PLAN_MEUBEL = '''
<path class="cab" d="M 0 1508 L 0 300 L 1100 300 L 1100 0 L 1478 0 A 1298 1298 0 0 1 2741 1000 L 650 1000 L 650 1508 Z"/>
<line class="hair" x1="650" y1="300" x2="650" y2="1000"/><line class="hair" x1="0" y1="1000" x2="650" y2="1000"/>
<line class="shelfline" x1="350" y1="300" x2="350" y2="1508"/>
<rect class="sink" x="125" y="1080" width="400" height="340" rx="50"/>
<rect class="oven" x="736" y="388" width="1305" height="600"/><rect class="mouth" x="820" y="900" width="1137" height="60"/>
<rect class="hood" x="688" y="400" width="1400" height="600"/><circle class="drum" cx="1388" cy="600" r="75"/>
<path class="shelfline" d="M 2088 447 A 1048 1048 0 0 1 2482 1000"/>
<rect class="cab" x="2126" y="1000" width="615" height="1108"/>
<rect class="cab" x="0" y="1508" width="650" height="1280"/>
<rect class="app" x="25" y="1538" width="600" height="600"/><rect class="app" x="25" y="2158" width="600" height="600"/>
<rect class="cab" x="2126" y="2108" width="650" height="680"/><rect class="app" x="2151" y="2148" width="600" height="600"/><circle class="drum" cx="2451" cy="2448" r="230"/>
<rect class="newwall" x="0" y="2788" width="1000" height="100"/><rect class="newwall" x="1850" y="2788" width="926" height="100"/>
<line class="pocket" x1="110" y1="2838" x2="1000" y2="2838"/>
<rect class="glass" x="1000" y="2826" width="850" height="24"/>
<rect class="cab" x="0" y="4188" width="852" height="600"/>
<line class="rail" x1="60" y1="4490" x2="792" y2="4490"/>
<line class="hanger" x1="150" y1="4330" x2="150" y2="4650"/><line class="hanger" x1="300" y1="4330" x2="300" y2="4650"/>
<line class="hanger" x1="552" y1="4330" x2="552" y2="4650"/><line class="hanger" x1="702" y1="4330" x2="702" y2="4650"/>
<rect class="cab" x="852" y="4188" width="680" height="600"/>
<rect class="cab" x="1532" y="4288" width="800" height="500"/><path class="shelfline" d="M1532 4188 H2332"/>
<rect class="cab" x="2332" y="4188" width="444" height="600"/>
'''
PLAN_WANDEN = '''
<rect class="wall" x="-400" y="-100" width="400" height="3000"/><rect class="wall" x="-400" y="3933" width="400" height="1255"/>
<rect class="wall" x="-400" y="4788" width="1932" height="400"/><rect class="wall" x="2332" y="4788" width="700" height="400"/>
<rect class="glass" x="1532" y="4788" width="800" height="400"/><line class="hair" x1="1532" y1="4988" x2="2332" y2="4988"/>
<rect class="wall" x="2776" y="1299" width="100" height="1690"/><rect class="wall" x="2776" y="3891" width="100" height="897"/>
<path class="arcwall" d="M 1478 -50 A 1348 1348 0 0 1 2826 1299"/>
<rect class="wall" x="1100" y="-100" width="378" height="100"/><rect class="niche" x="0" y="-100" width="1000" height="300"/>
<rect class="wall" x="1000" y="-100" width="100" height="400"/><rect class="wall" x="0" y="200" width="1000" height="100"/>
<line class="thin" x1="-1433" y1="3933" x2="-400" y2="3933"/>
<path class="swing" d="M -400 2900 A 1033 1033 0 0 0 -1433 3933"/>
<line class="thin" x1="2776" y1="2989" x2="1876" y2="2989"/><path class="swing" d="M 2776 3889 A 900 900 0 0 1 1876 2989"/>
'''
PLAN_BASIS = PLAN_VLOER + PLAN_MEUBEL + PLAN_WANDEN
PLAN_LABELS = '''
<text class="lbl" x="500" y="690">hoek</text><text class="lbl" x="325" y="1265">spoelbak</text>
<text class="lbl" x="1388" y="770">pizzaoven GR213</text><text class="lbl" x="2433" y="1640">voorraad</text>
<text class="lbl" x="325" y="1855">vriezer</text><text class="lbl" x="325" y="2475">koelkast</text>
<text class="lbl" x="2451" y="2560">was + droger</text>
<text class="lbl" x="1425" y="2760">schuifdeur</text>
<text class="lbl" x="1192" y="4560">kast</text>
<text class="lbl" x="426" y="4290">kapstok</text><text class="lbl" x="1932" y="4440">zitbank</text><text class="lbl" x="2554" y="4700">schoonmaak</text>
<text class="lbl it" x="1932" y="5110">raam</text><text class="lbl it" x="-900" y="3250">ingang</text>
<text class="lbl it" x="3020" y="3440" transform="rotate(90 3020 3440)">keuken</text>
'''
def plan_badges(s=1.0):
    P = [(426,4560,"D1"),(1192,4440,"D2"),(1932,4600,"D3"),(2554,4480,"D4"),(1425,3010,"D5"),
         (325,2148,"W1"),(2451,2440,"W2"),(480,870,"W3"),(1990,255,"W4"),(2390,830,"W5"),(170,470,"W6"),(990,640,"W7"),(2433,1510,"W8")]
    return "".join(badge(x, y, c, s) for x, y, c in P)
PLAN_MATEN = (
    chain_v([300,1000,1508,2788,2888,2900,3933,4188,4788], -1500, ["700","508","1280",("100",1),"","1033","255","600"], frm=-420) +
    vdim(300, 4788, -1740, "4488") +
    chain_v([1000,2108,2788,2888,2989,3891,4188,4788], 3260, ["1108","680",("100",1),"101","902","297","600"], frm=2900) +
    chain_v([0,1299,4788], 3520, ["1299","3489"]) +
    chain_h([0,852,1532,2332,2776], 5500, ["852","680","800","444"], frm=5210) +
    chain_h([-400,0,2776,2876], 5790, ["400","2776","100"], frm=5210) +
    hdim(650, 2126, 1950, "1476 loopruimte") +
    chain_h([650,736,2041,2126], 1110, ["86","1305 oven","85"]) +
    hdim(688, 2088, 1360, "1400 afzuigkap") +
    chain_h([0,1000,1850,2776], 3260, ["1000 cassette","850 doorgang","926"]) +
    vdim(2888, 4188, 720, "doorloop 1300") +
    '<text class="dimt" x="2890" y="330">R1298</text>')
def plan(vb, schaal, extra="", maten=False, badges=1.0, labels=True, cls=""):
    return svg(vb, schaal, PLAN_BASIS + (PLAN_LABELS if labels else "") + (PLAN_MATEN if maten else "")
               + (plan_badges(badges) if badges else "") + extra, cls)

# ------------------------------------------------------------------ installatieplan
KLEUR = {"kw":"#2c6fce","ww":"#c8372d","af":"#3f8f3f","cv":"#e0672b","el":"#c8900a","sch":"#8a6a1f","li":"#3a3a3a","ve":"#7b4fb0","gas":"#8b8b8b"}
def dot(x, y, code, soort):
    k = KLEUR[soort]
    s = (f'<rect x="{x-48}" y="{y-48}" width="96" height="96" rx="10" fill="{k}"/>' if soort in ("el", "sch")
         else f'<circle cx="{x}" cy="{y}" r="50" fill="{k}"/>')
    return s + f'<text x="{x}" y="{y+1}" class="dott" style="font-size:{34 if len(code) > 2 else 42}px">{code}</text>'
def sbadge(x, y, code):
    return (f'<rect x="{x-62}" y="{y-40}" width="124" height="80" rx="18" fill="#fff" stroke="#1d1d1b" stroke-width="5"/>'
            f'<text x="{x}" y="{y+1}" class="bdg" style="font-size:46px">{code}</text>')
INSTALL = "".join([
    sbadge(426,4640,"D1"), sbadge(1192,4463,"D2"), sbadge(1932,4600,"D3"), sbadge(2554,4600,"D4"),
    sbadge(325,2148,"W1"), sbadge(2451,2448,"W2"), sbadge(480,700,"W3"), sbadge(1388,1000,"W7"), sbadge(2433,1400,"W8"),
    dot(250,1190,"KW1","kw"), dot(400,1190,"WW1","ww"), dot(325,1335,"A1","af"), dot(85,1445,"E7","el"),
    dot(545,1620,"E4","el"), dot(545,2680,"E3","el"),
    dot(2215,2185,"KW2","kw"), dot(2350,2185,"A2","af"), dot(2550,2185,"E1","el"), dot(2685,2185,"E2","el"),
    dot(2547,4306,"E11","el"),
    dot(815,480,"E12","el"), dot(1690,480,"E8","el"), dot(1952,334,"E5","el"), dot(1108,861,"E13","el"), dot(2318,627,"E6","el"),
    dot(1388,600,"V3","ve"), dot(2420,715,"L3","li"),
    dot(1381,1705,"L2","li"), dot(1381,2354,"V1","ve"), dot(1415,2990,"V2","ve"), dot(1381,3700,"L1","li"),
    dot(73,3994,"S1","sch"), dot(2700,3050,"S2","sch"), dot(1937,2730,"S3","sch"),
])

# ------------------------------------------------------------------ wandaanzichten (y van plafond 0 naar vloer 2600)
VOORWAND = '''
<rect class="wallbg" x="0" y="0" width="2776" height="2600"/>
<rect class="cab" x="0" y="0" width="444" height="2500"/><rect class="plinth" x="0" y="2500" width="444" height="100"/><circle class="knob" cx="400" cy="1300" r="12"/>
<rect class="cab" x="444" y="0" width="800" height="480"/><rect class="glass" x="444" y="500" width="800" height="1100"/>
<text class="lbl" x="844" y="1080">raam (hoogtes ±)</text>
<rect class="cushion" x="464" y="2100" width="760" height="50"/><rect class="cab" x="444" y="2150" width="800" height="350"/><line class="line" x1="844" y1="2150" x2="844" y2="2500"/>
<rect class="plinth" x="444" y="2500" width="800" height="100"/>
<rect class="cab" x="1244" y="0" width="680" height="2500"/><rect class="plinth" x="1244" y="2500" width="680" height="100"/>
<line class="line" x1="1584" y1="0" x2="1584" y2="2500"/><circle class="knob" cx="1550" cy="1300" r="12"/><circle class="knob" cx="1618" cy="1300" r="12"/>
<rect class="cab" x="1924" y="0" width="852" height="2500"/><rect class="plinth" x="1924" y="2500" width="852" height="100"/>
<rect class="open" x="1944" y="630" width="812" height="1520"/><rect class="top" x="1944" y="600" width="812" height="30"/>
<line class="rail" x1="1964" y1="850" x2="2736" y2="850"/>
<rect class="coat" x="2010" y="870" width="140" height="800" rx="40"/><rect class="coat" x="2200" y="870" width="140" height="900" rx="40"/>
<rect class="coat" x="2390" y="870" width="140" height="760" rx="40"/><rect class="coat" x="2580" y="870" width="140" height="850" rx="40"/>
<line class="line" x1="1924" y1="2150" x2="2776" y2="2150"/><line class="line" x1="1924" y1="2325" x2="2776" y2="2325"/>
<line class="floorline" x1="-150" y1="2600" x2="2926" y2="2600"/>
''' + chain_h([0,444,1244,1924,2776], 2900, ["444","800","680","852"], frm=2640) + hdim(0,2776,3110,"2776", frm=2640) \
    + chain_v([0,500,1600,2150,2600], -300, ["500","1100 (±)","550 (±)","450"], frm=-20) \
    + chain_v([0,600,850,2150,2500,2600], 3080, ["600","250","1300","350","100"], frm=2796) \
    + badge(222,1100,"D4") + badge(844,1900,"D3") + badge(1584,350,"D2") + badge(2350,1960,"D1")

LINKERWAND = '''
<rect class="wallbg" x="0" y="0" width="4488" height="2600"/>
<rect class="cabhatch" x="0" y="0" width="600" height="2600"/><text class="lbl" x="300" y="1300" transform="rotate(-90 300 1300)">kastenwand</text>
<rect class="door" x="855" y="300" width="1033" height="2300"/><rect class="pane" x="955" y="400" width="833" height="2100"/><text class="lbl" x="1371" y="1500">buitendeur</text>
<rect class="newwall" x="1900" y="0" width="100" height="2600"/>
<rect class="cab" x="2000" y="0" width="1280" height="900"/><line class="line" x1="2640" y1="0" x2="2640" y2="900"/>
<rect class="cab" x="2000" y="900" width="1280" height="900"/>
<rect class="app" x="2040" y="920" width="580" height="880"/><text class="lbl" x="2330" y="1380">koelkast</text>
<rect class="app" x="2660" y="920" width="580" height="880"/><text class="lbl" x="2950" y="1380">vriezer</text>
<rect class="cab" x="2000" y="1800" width="1280" height="700"/><line class="line" x1="2640" y1="1800" x2="2640" y2="2500"/><line class="line" x1="2000" y1="2150" x2="3280" y2="2150"/>
<text class="lbl" x="2640" y="2010" style="fill:#777">lades</text>
<rect class="plinth" x="2000" y="2500" width="1280" height="100"/>
<rect class="cab" x="3280" y="0" width="1208" height="1100"/><line class="line" x1="3884" y1="0" x2="3884" y2="1100"/>
<rect class="splash" x="3280" y="1100" width="1208" height="590"/><rect class="panel" x="3528" y="1530" width="14" height="160"/>
<rect class="stone" x="3280" y="1690" width="1208" height="30"/><rect class="cab" x="3280" y="1720" width="1208" height="780"/>
<line class="line" x1="3788" y1="1720" x2="3788" y2="2500"/><text class="lbl" x="3534" y="2150">spoelkast</text><text class="lbl" x="4138" y="2150">hoek</text>
<rect class="plinth" x="3280" y="2500" width="1208" height="100"/>
<line class="floorline" x1="-150" y1="2600" x2="4638" y2="2600"/>
''' + chain_h([0,600,855,1888,1900,2000,3280,3788,4488], 2900, ["600","255","1033","","100","1280","508","700"], frm=2640) + hdim(0,4488,3110,"4488", frm=2640) \
    + chain_v([0,900,1800,2500,2600], -300, ["900","900","700","100"], frm=-20) \
    + chain_v([0,1100,1690,1720,2500,2600], 4792, ["1100","590",("30",1),"780","100"], frm=4508) \
    + badge(2640,450,"W1") + badge(3884,550,"W6") + badge(3884,2330,"W3") + badge(1950,1300,"D5")

ACHTERKANT = '''
<rect class="wallbg" x="0" y="0" width="2776" height="2600"/>
<rect class="splash" x="0" y="1000" width="2126" height="690"/>
<rect class="cab" x="0" y="0" width="350" height="1100"/>
<rect class="cab" x="688" y="0" width="1400" height="880"/><line class="duct" x1="1388" y1="0" x2="1388" y2="880"/>
<text class="lbl" x="1388" y="410">koof + kanaal Ø150</text>
<rect class="app" x="688" y="880" width="1400" height="120"/><text class="lbl" x="1388" y="1170">afzuigkap 1400</text>
<rect class="app" x="1550" y="1390" width="360" height="300" rx="30"/><text class="lbl" x="1730" y="1560">frituur</text>
<rect class="stone" x="0" y="1690" width="2126" height="30"/>
<rect class="cab" x="0" y="1720" width="650" height="780"/><text class="lbl" x="325" y="2150">hoek</text><rect class="plinth" x="0" y="2500" width="650" height="100"/>
<rect class="cab" x="650" y="1720" width="86" height="880"/><rect class="cab" x="2041" y="1720" width="85" height="880"/>
<rect class="shield" x="736" y="1720" width="1305" height="20"/><rect class="grill" x="736" y="1740" width="1305" height="100"/>
<rect class="oven" x="736" y="1840" width="1305" height="413"/><line class="line" x1="900" y1="1935" x2="1877" y2="1935"/><rect class="mouth" x="860" y="2000" width="1057" height="150"/>
<text class="lbl" x="1388" y="2215">pizzaoven GR213</text>
<rect class="panel" x="736" y="2253" width="1305" height="12"/><rect class="grill" x="736" y="2270" width="1305" height="230"/>
''' + "".join(f'<circle class="fan" cx="{820+142*i}" cy="2385" r="52"/>' for i in range(9)) + '''
<rect class="grill" x="736" y="2500" width="1305" height="100"/>
<rect class="cab" x="2126" y="0" width="615" height="2600"/><text class="lbl" x="2433" y="1400" transform="rotate(-90 2433 1400)">W8 zijkant</text>
<line class="floorline" x1="-150" y1="2600" x2="2926" y2="2600"/>
''' + chain_h([0,650,736,2041,2126,2741], 2900, ["650","86","1305","85","615"], frm=2640) + hdim(0,2741,3110,"2741", frm=2640) \
    + chain_v([0,1000,1690,1720,1840,2253,2500,2600], -300, ["1000","690",("30",1),"120","413","247","100"], frm=-20) \
    + badge(175,600,"W6") + badge(1388,220,"W4") + badge(325,1960,"W3") + badge(1388,2075,"W7")

RECHTERWAND = '''
<rect class="wallbg" x="0" y="0" width="3788" height="2600"/>
<rect class="cab" x="0" y="0" width="1108" height="2500"/><rect class="plinth" x="0" y="2500" width="1108" height="100"/>
<line class="line" x1="554" y1="0" x2="554" y2="2500"/><circle class="knob" cx="520" cy="1300" r="12"/><circle class="knob" cx="588" cy="1300" r="12"/>
<text class="lbl" x="277" y="1500" transform="rotate(-90 277 1500)">voorraad</text>
<rect class="cab" x="1108" y="0" width="680" height="2500"/><rect class="plinth" x="1108" y="2500" width="680" height="100"/>
<line class="line" x1="1108" y1="690" x2="1788" y2="690"/>
<rect class="app" x="1148" y="770" width="600" height="850"/><circle class="drum" cx="1448" cy="1240" r="225"/><text class="lbl" x="1448" y="910">droger</text>
<rect class="app" x="1148" y="1650" width="600" height="850"/><circle class="drum" cx="1448" cy="2120" r="225"/><text class="lbl" x="1448" y="1790">wasmachine</text>
<rect class="newwall" x="1788" y="0" width="100" height="2600"/>
<rect class="door" x="1989" y="300" width="902" height="2300"/><rect class="panel" x="2826" y="1440" width="14" height="140"/>
<text class="lbl" x="2440" y="1480">keukendeur</text><text class="lbl" x="2440" y="1560" style="fill:#777">(scharnier links)</text>
<rect class="cabhatch" x="3188" y="0" width="600" height="2600"/><text class="lbl" x="3488" y="1300" transform="rotate(-90 3488 1300)">kastenwand</text>
<line class="floorline" x1="-150" y1="2600" x2="3938" y2="2600"/>
''' + chain_h([0,1108,1788,1888,1989,2891,3188,3788], 2900, ["1108","680","100","101","902","297","600"], frm=2640) + hdim(0,3788,3110,"3788", frm=2640) \
    + vdim(0, 2600, -300, "2600", frm=-20) + chain_v([0,300,2600], 4092, ["300","2300"], frm=3808) \
    + badge(554,650,"W8") + badge(1448,350,"W2") + badge(1838,420,"D5")

# ------------------------------------------------------------------ details 1:20
WASKAST = '''
<rect class="cabhatch" x="-150" y="0" width="150" height="2600"/><rect class="newwall" x="680" y="0" width="100" height="2600"/>
<text class="lbl" x="-75" y="1300" transform="rotate(-90 -75 1300)">voorraadkast W8</text><text class="lbl" x="732" y="1300" transform="rotate(-90 732 1300)" style="fill:#fff">binnenmuur D5</text>
<rect class="cab" x="0" y="0" width="680" height="2500"/><rect class="plinth" x="0" y="2500" width="680" height="100"/>
<rect class="grill" x="120" y="2520" width="440" height="56"/>
<line class="line" x1="0" y1="690" x2="680" y2="690"/><rect class="top" x="18" y="690" width="644" height="30"/>
<rect class="app" x="40" y="770" width="600" height="850"/><circle class="drum" cx="340" cy="1240" r="230"/>
<rect class="top" x="40" y="1620" width="600" height="30"/>
<rect class="app" x="40" y="1650" width="600" height="850"/><circle class="drum" cx="340" cy="2120" r="230"/>
<rect class="elbox" x="80" y="430" width="70" height="70"/><rect class="elbox" x="180" y="430" width="70" height="70"/>
<rect class="wbox" x="430" y="380" width="180" height="200"/>
<line class="floorline" x1="-220" y1="2600" x2="900" y2="2600"/>
''' + chain_v([0,690,770,1620,1650,2500,2600], -330, ["690",("80",1),"850",("30",1),"850","100"], frm=-170) + hdim(0,680,2800,"680", frm=2640) \
    + mark(340,200,1)+mark(520,480,2)+mark(165,360,3)+mark(340,1240,4)+mark(600,1635,5)+mark(340,2120,6)+mark(610,2548,7)

# ------------------------------------------------------------------ techniekkast: hoekkast 600 x 1200 in de speelkamer, voor de CV-stukken
# De hoekkast staat in de hoek bij de trap (achterwand) en de garderobe (lange wand). De lange kast ernaast is een gewone kast met lades.
# De tekst is groter dan in de detaillering bijkeuken: de CV-detaillering moet leesbaar zijn op een A4 in zwart-wit.
def _duct(x, y0, y1, t=""):
    m = (y0 + y1) // 2
    return (f'<rect class="duct2" x="{x}" y="{y0}" width="125" height="{y1-y0}"/>'
            + (f'<text class="lbs" x="{x+80}" y="{m}" text-anchor="middle" transform="rotate(-90 {x+80} {m})">{t}</text>' if t else ""))

# aanzicht van de lange wand (kant garderobe), gezien vanaf de kant van de kast: links de deur aan de kopse kant, rechts de achterwand.
# Hoekkast 700 x 1400 (Julian, 13-11-2026: 600 x 1200 werd te krap met de leidingen). Leidingen staan erin met isolatie, op schaal:
# dichte band = aanvoer, open band = retour.
def _pijp(d, retour=False):
    s = f'<path d="{d}" fill="none" stroke="#7a4318" stroke-width="44" stroke-linejoin="round"/>'
    if retour: s += f'<path d="{d}" fill="none" stroke="#fff" stroke-width="28" stroke-linejoin="round"/>'
    return s

TECHWAND = '''
<rect x="1400" y="-40" width="120" height="2480" fill="url(#muur)" stroke="#1d1d1b" stroke-width="4"/>
<text class="lbl it" x="1478" y="1200" transform="rotate(-90 1478 1200)" style="fill:#1d1d1b">achterwand (kant trap)</text>
<rect class="tech" x="0" y="0" width="1400" height="2400"/>
<text class="lbl it" x="-45" y="1200" transform="rotate(-90 -45 1200)">deur aan de kopse kant</text>
''' + _duct(70, 0, 265) + _duct(208, 0, 265) + _duct(346, 0, 265) + _duct(484, 0, 265) + '''
<text class="lbs" x="670" y="132" text-anchor="middle" transform="rotate(-90 670 132)">4 × Ø 125</text>
<rect class="unit" x="60" y="265" width="560" height="635"/>
<text class="lbt b" x="340" y="545" text-anchor="middle" style="font-size:62px">WTW-unit</text><text class="lbs" x="340" y="610" text-anchor="middle">S&amp;P Energisava 260 R</text><text class="lbs" x="340" y="666" text-anchor="middle">560 × 635 × 260</text>
<path d="M590 900 V1000" fill="none" stroke="#1d1d1b" stroke-width="5" stroke-dasharray="14 12"/><text class="lbs" x="565" y="990" text-anchor="end">condens</text>
<rect class="unit" x="100" y="1030" width="280" height="295" rx="55"/><text class="lbt b" x="240" y="1172" text-anchor="middle">X2</text><text class="lbs" x="240" y="1234" text-anchor="middle">12 L</text>
<text class="lbs it" x="700" y="1190" text-anchor="middle">vrij: wand-</text><text class="lbs it" x="700" y="1246" text-anchor="middle">contactdozen</text>
<rect class="unit" x="440" y="1340" width="330" height="118"/><text class="lbs b" x="605" y="1415" text-anchor="middle" style="fill:#1d1d1b">ZR</text>
<text class="lbs" x="605" y="1516" text-anchor="middle">zoneregelaar</text><text class="lbs" x="605" y="1572" text-anchor="middle">330 × 118 × 57</text>
''' + _pijp("M990 580 H950 V1730 H885") + _pijp("M990 725 H896 V1650", True) + _pijp("M1075 1250 V1520") + _pijp("M1145 1250 V1520", True) + '''
<text class="lbs" x="870" y="1100" text-anchor="end">naar VD</text>
''' + "".join(f'<path d="M{95+50*i} 2050 V2400" fill="none" stroke="#9c3d0c" stroke-width="6"/>' for i in range(14)) + '''
<rect class="unit" x="60" y="1650" width="825" height="400"/><path d="M85 1725 H750" stroke="#9c3d0c" stroke-width="9"/><path d="M85 1980 H750" stroke="#9c3d0c" stroke-width="9" stroke-dasharray="30 18"/>
<rect x="770" y="1670" width="100" height="360" fill="#fff" stroke="#1d1d1b" stroke-width="4"/><circle cx="820" cy="1780" r="34" fill="#fff" stroke="#1d1d1b" stroke-width="4"/><path d="M803 1762 L839 1780 L803 1798 Z" fill="#1d1d1b"/><text class="lbs" x="820" y="1900" text-anchor="middle">P5</text><text class="lbs" x="820" y="1955" text-anchor="middle">V2</text>
<text class="lbt b" x="415" y="1825" text-anchor="middle">VD · verdeler met pomp</text><text class="lbs" x="415" y="1888" text-anchor="middle">14 groepen · 35 °C</text><text class="lbs" x="415" y="1942" text-anchor="middle">825 × 400 × 160</text>
<rect class="vat" x="990" y="130" width="395" height="1120" rx="60"/>
<text class="lbt b" x="1187" y="590" text-anchor="middle" style="font-size:66px">B2</text><text class="lbt" x="1187" y="662" text-anchor="middle">buffervat 80 L</text><text class="lbs" x="1187" y="722" text-anchor="middle">Ø 395 × 1120</text><text class="lbs" x="1187" y="778" text-anchor="middle">hangend</text>
<circle class="sens" cx="1065" cy="400" r="44"/><text class="lbt" x="1065" y="415" text-anchor="middle" style="font-size:42px">T5</text>
<circle class="sens" cx="1065" cy="1000" r="44"/><text class="lbt" x="1065" y="1015" text-anchor="middle" style="font-size:42px">T8</text>
<path class="sens" d="M1187 130 V100 M1159 100 H1215 L1187 52 Z"/><text class="lbs" x="1232" y="98">VV2</text>
<rect x="1232" y="930" width="30" height="320" fill="none" stroke="#1d1d1b" stroke-width="5" stroke-dasharray="14 10"/><rect x="1212" y="1250" width="70" height="80" fill="#fff" stroke="#1d1d1b" stroke-width="5"/>
<text class="lbt b" x="1302" y="1308">E2</text>
<rect class="unit" x="1010" y="1520" width="366" height="573"/>
<text class="lbt b" x="1193" y="1770" text-anchor="middle">FWM2</text><text class="lbs" x="1193" y="1832" text-anchor="middle">verswatermodule</text><text class="lbs" x="1193" y="1888" text-anchor="middle">366 × 573 × 160</text>
<line class="floorline" x1="-150" y1="2400" x2="1620" y2="2400"/>
''' + vdim(0,2400,-330,"≥ 2400", frm=-140) + hdim(0,1400,2620,"1400", frm=2440)

# aanzicht van de achterwand (kant trap), gezien vanaf de deur aan de kopse kant: links de lange wand, rechts de kast ernaast
TECHACHTER = '''
<rect x="-120" y="-40" width="120" height="2480" fill="url(#muur)" stroke="#1d1d1b" stroke-width="4"/>
<text class="lbl it" x="-42" y="1200" transform="rotate(-90 -42 1200)" style="fill:#1d1d1b">lange wand (kant garderobe)</text>
<rect class="cabhatch" x="700" y="0" width="110" height="2400"/><text class="lbl" x="772" y="1200" transform="rotate(-90 772 1200)">kast ernaast</text>
<rect class="tech" x="0" y="0" width="700" height="2400"/>
<rect x="590" y="0" width="110" height="2400" fill="#dcdcdc" stroke="#1d1d1b" stroke-width="4"/>
<text class="lbt b" x="645" y="90" text-anchor="middle">S</text>
''' + _pijp("M665 2400 V265 H545") + _pijp("M612 2400 V1060 H545", True) + _pijp("M150 265 H40 V1520") + _pijp("M150 1060 H100 V1520", True) + _pijp("M150 580 H95") + _pijp("M150 725 H95", True) + _pijp("M545 580 H590") + _pijp("M545 725 H590", True) + '''
<text class="lbs" x="140" y="652" text-anchor="middle" transform="rotate(-90 140 652)">VD</text><text class="lbs" x="585" y="652" text-anchor="middle" transform="rotate(-90 585 652)">V4</text>
<path d="M643 1352 L687 1388 V1352 L643 1388 Z" fill="#fff" stroke="#1d1d1b" stroke-width="4"/><path d="M590 1352 L634 1388 V1352 L590 1388 Z" fill="#fff" stroke="#1d1d1b" stroke-width="4"/><text class="lbs" x="575" y="1387" text-anchor="end">kranen</text>
<rect class="vat" x="150" y="130" width="395" height="1120" rx="60"/>
<text class="lbt b" x="347" y="700" text-anchor="middle" style="font-size:66px">B2</text><text class="lbt" x="347" y="772" text-anchor="middle">buffervat</text><text class="lbt" x="347" y="836" text-anchor="middle">80 L</text>
<path class="sens" d="M347 130 V100 M319 100 H375 L347 52 Z"/>
<rect x="332" y="930" width="30" height="320" fill="none" stroke="#1d1d1b" stroke-width="5" stroke-dasharray="14 10"/><rect x="312" y="1250" width="70" height="80" fill="#fff" stroke="#1d1d1b" stroke-width="5"/>
<text class="lbt b" x="347" y="1392" text-anchor="middle">E2</text><text class="lbs" x="347" y="1446" text-anchor="middle">in het vat</text>
<text class="lbs it" x="345" y="1760" text-anchor="middle">vrij onder</text><text class="lbs it" x="345" y="1816" text-anchor="middle">het vat</text>
<rect class="unit" x="0" y="1520" width="160" height="573"/><text class="lbs b" x="97" y="1806" text-anchor="middle" transform="rotate(-90 97 1806)" style="fill:#1d1d1b">FWM2</text>
<rect class="unit" x="530" y="1500" width="170" height="400"/><text class="lbs b" x="632" y="1700" text-anchor="middle" transform="rotate(-90 632 1700)" style="fill:#1d1d1b">V4 + P7</text>
<line class="floorline" x1="-200" y1="2400" x2="900" y2="2400"/>
''' + hdim(0,700,2620,"700", frm=2440)

# plattegrond van de hoekkast, deurkant onder: links de lange wand (garderobe), boven de achterwand (trap), rechts de kast ernaast
TECHPLAN_CV = '''
<rect x="-150" y="-150" width="1500" height="150" fill="url(#muur)" stroke="#1d1d1b" stroke-width="4"/>
<rect x="-150" y="0" width="150" height="1520" fill="url(#muur)" stroke="#1d1d1b" stroke-width="4"/>
<rect class="cab" x="700" y="0" width="650" height="600"/>
<rect class="duct2" x="700" y="14" width="650" height="125"/><text class="lbs" x="1025" y="94" text-anchor="middle">afzuiging keuken, bovenin</text>
<text class="lbl" x="1025" y="400">kast</text>
<rect class="tech" x="0" y="0" width="700" height="1400"/>
<rect class="unit" x="8" y="24" width="160" height="366"/><text class="lbs b" x="72" y="207" text-anchor="middle" transform="rotate(-90 72 207)" style="fill:#1d1d1b">FWM2</text>
<rect class="unit" x="8" y="515" width="160" height="825"/><text class="lbs b" x="105" y="1200" text-anchor="middle" transform="rotate(-90 105 1200)" style="fill:#1d1d1b">VD</text>
<rect class="ghost" x="8" y="780" width="260" height="560"/><text class="lbs b" x="215" y="1070" text-anchor="middle" style="fill:#1d1d1b">WTW</text><text class="lbs" x="215" y="1122" text-anchor="middle">boven</text>
<path d="M150 212 h-50 M545 212 h45" fill="none" stroke="#1d1d1b" stroke-width="14"/><circle class="vat" cx="347" cy="212" r="198"/><text class="lbt b" x="347" y="207" text-anchor="middle">B2</text><text class="lbs" x="347" y="265" text-anchor="middle">80 L</text>
<circle cx="645" cy="55" r="52" fill="#dcdcdc" stroke="#1d1d1b" stroke-width="4"/><text class="lbs b" x="645" y="72" text-anchor="middle" style="fill:#1d1d1b">S</text>
<circle cx="665" cy="165" r="22" fill="#fff" stroke="#7a4318" stroke-width="9"/><circle cx="665" cy="240" r="22" fill="#fff" stroke="#7a4318" stroke-width="9"/><text class="lbs" x="617" y="160" text-anchor="middle">GL</text>
<rect class="unit" x="530" y="300" width="162" height="265"/><text class="lbs b" x="628" y="432" text-anchor="middle" transform="rotate(-90 628 432)" style="fill:#1d1d1b">V4 + P7</text>
<path class="ghost" d="M0 1400 H700 V600"/>
<text class="lbl it" x="350" y="1462">deur</text><text class="lbl it" x="755" y="1000" transform="rotate(-90 755 1000)">deur</text>
<text class="lbs it" x="485" y="1000" text-anchor="middle">vloer vrij</text>
<text class="lbl it" x="600" y="-195">achterwand (trap)</text>
<text class="lbl it" x="-195" y="700" transform="rotate(-90 -195 700)">lange wand (garderobe)</text>
<text class="lbl it" x="1075" y="1000">Speelkamer / Studie</text>
''' + hdim(0,700,1670,"700", frm=1540) + vdim(0,1400,-390,"1400", frm=-260) + vdim(0,600,1460,"600", frm=1370)

# namen op de plattegrond 1:50 (leidingplan en 'plek in de bijkeuken')
PLAN_LABELS_50 = '''
<text class="lbl" x="426" y="4530">kapstok</text><text class="lbl" x="1932" y="4580">zitbank</text><text class="lbl" x="2554" y="4530">kast</text>
<text class="lbl" x="325" y="1870">vriezer</text><text class="lbl" x="325" y="2490">koelkast</text><text class="lbl" x="2433" y="1430">voorraad</text>
<text class="lbl" x="1388" y="730">oven</text>
<text class="lbl b" x="2451" y="2060" style="fill:#1d1d1b">TECHNIEK</text>
'''

def crop(blad, x, y, w, h):
    mm = 25.4/72
    return (f'<svg viewBox="{x} {y} {w} {h}" style="width:{w*mm:.1f}mm;height:{h*mm:.1f}mm" xmlns="http://www.w3.org/2000/svg">'
            f'<image href="origineel/blad{blad}.svg" x="0" y="0" width="1191.12" height="841.92"/></svg>')


CSS_TEKEN = '''/* tekenstijl: gelijk aan de detaillering van 29-10-2026 (dunne lijnen, kleine tekst) */
.wall{fill:#1d1d1b}.newwall{fill:#6f6a62}.floor{fill:#fff}
.cab{fill:#efece5;stroke:#5c5a55;stroke-width:4px}.app{fill:#e2e9f1;stroke:#3b5b7a;stroke-width:4px}.tech{fill:#f9e8d9;stroke:#a2602b;stroke-width:5px}
.oven{fill:#e9ddd2;stroke:#8a4a2a;stroke-width:5px}.mouth{fill:#5a3a2a}.niche{fill:url(#hatchN);stroke:#1d1d1b;stroke-width:4px}.nbg{fill:#fff}.nln{stroke:#a9a9a9;stroke-width:5px}
.glass{fill:#eef3f6;stroke:#1d1d1b;stroke-width:4px}.thin{fill:none;stroke:#1d1d1b;stroke-width:7px}.hair{fill:none;stroke:#5c5a55;stroke-width:3px}
.pocket{fill:none;stroke:#fff;stroke-width:5px;stroke-dasharray:30 22}.arcwall{fill:none;stroke:#1d1d1b;stroke-width:100px}
.swing{fill:none;stroke:#8a8a8a;stroke-width:4px;stroke-dasharray:26 20}.hood{fill:none;stroke:#3b5b7a;stroke-width:5px;stroke-dasharray:36 20}
.shelfline{fill:none;stroke:#8a8174;stroke-width:4px;stroke-dasharray:30 22}.drum{fill:#fff;stroke:#3b5b7a;stroke-width:4px}.vat{fill:#fff;stroke:#a2602b;stroke-width:5px}
.sink{fill:#fff;stroke:#5c5a55;stroke-width:4px}.hanger{stroke:#b3aca0;stroke-width:5px}.rail{stroke:#8a8174;stroke-width:8px}
.dim{fill:none;stroke:#3a3a3a;stroke-width:3px}.ext{fill:none;stroke:#8a8a8a;stroke-width:2.5px}
.dimt{fill:#333;font-size:56px;text-anchor:middle;letter-spacing:1.5px}
.lbl{fill:#333;font-size:50px;text-anchor:middle;letter-spacing:1px}.lbls{fill:#5a3a1c;font-size:46px;text-anchor:middle}.it{fill:#777;font-style:italic}
.bdg{font-weight:700;text-anchor:middle;dominant-baseline:central;fill:#1d1d1b}
.dott{fill:#fff;font-weight:700;text-anchor:middle;dominant-baseline:central}
.wallbg{fill:#fbfaf7;stroke:#1d1d1b;stroke-width:7px}.floorline{stroke:#1d1d1b;stroke-width:8px}
.cabhatch{fill:#e4dfd5;stroke:#5c5a55;stroke-width:4px}
.grill{fill:#f4f2ee;stroke:#5c5a55;stroke-width:3px;stroke-dasharray:10 8}.door{fill:#fff;stroke:#1d1d1b;stroke-width:8px}.pane{fill:#eef3f6;stroke:#8aa0b2;stroke-width:4px}
.ghost{fill:none;stroke:#a2602b;stroke-width:4px;stroke-dasharray:26 18}.top{fill:#cfc9bd;stroke:#5c5a55;stroke-width:3px}.plinth{fill:#d9d5cc;stroke:#5c5a55;stroke-width:3px}
.splash{fill:#f1efea}.open{fill:#f8f6f2;stroke:#5c5a55;stroke-width:3px}.cushion{fill:#c9bfae;stroke:#8a8174;stroke-width:3px}.coat{fill:#ddd7cb;stroke:#8a8174;stroke-width:3px}
.line{stroke:#5c5a55;stroke-width:3px}.panel{fill:#5c5a55}.knob{fill:#5c5a55}.stone{fill:#5d656c}
.duct{stroke:#3b5b7a;stroke-width:5px;stroke-dasharray:22 16}.shield{fill:#d9c9a8}.fan{fill:#fff;stroke:#3b5b7a;stroke-width:4px}
.elbox{fill:#e0a400;stroke:#8a6a1f;stroke-width:3px}.wbox{fill:#fff;stroke:#3f8f3f;stroke-width:5px}
.s75.bkp .lbl{font-size:135px}.s75.bkp .cab,.s75.bkp .app,.s75.bkp .sink,.s75.bkp .drum,.s75.bkp .oven{stroke-width:11px}
.s20 .dimt{font-size:46px}.s20 .lbl{font-size:42px}.s20 .lbls{font-size:40px}
.s40 .lbl{font-size:70px}
.fade .cab{fill:#f6f4f0;stroke:#bdb9b1}.fade .app{fill:#eef3f7;stroke:#a9b8c8}.fade .tech{fill:#fcf3ea;stroke:#d6b08c}.fade .oven{fill:#f3ede7;stroke:#cdb0a2}
.fade .mouth{fill:#b9aca4}.fade .newwall{fill:#bdb9b3}.fade .drum{stroke:#a9b8c8}.fade .vat{stroke:#d6b08c}.fade .sink{stroke:#bdb9b1}.fade .hood{stroke:#a9b8c8}
.b{font-weight:700}
.lbt{fill:#1d1d1b;font-size:54px}.lbs{fill:#333;font-size:48px}.ld2{stroke:#1d1d1b;stroke-width:3px}
.duct2{fill:#fff;stroke:#1d1d1b;stroke-width:4px;stroke-dasharray:22 12}
.s50.cv .lbt{font-size:128px}.s50.cv .lbl{font-size:112px}.s50.cv .dimt{font-size:118px}.s50.cv .unit,.s50.cv .vat{stroke-width:11px}.s50.cv .tech{stroke-width:12px}.s50.cv .dim{stroke-width:8px}.s50.cv .ext{stroke-width:6px}.s50.cv .ghost{stroke-width:12px;stroke-dasharray:60 40}
.cv .dimt{font-size:54px;fill:#1d1d1b}.cv .lbl{font-size:48px;fill:#1d1d1b}.cv .it{fill:#444}.cv .ghost{stroke:#7a4318;stroke-width:5px}.cv .tech{stroke:#7a4318}.cv .vat{stroke:#1d1d1b}
.unit{fill:#fff;stroke:#1d1d1b;stroke-width:4px}.sens{fill:#fff;stroke:#1d1d1b;stroke-width:4px}
.bkp .cab,.bkp .app,.bkp .sink,.bkp .drum,.bkp .oven{stroke-width:8px}.bkp .tech,.bkp .vat{stroke-width:12px}
.bkp .hair,.bkp .shelfline,.bkp .hood,.bkp .hanger{stroke-width:6px}.bkp .rail{stroke-width:10px}.bkp .pocket{stroke-width:9px}
.bkp .lbl{font-size:92px;letter-spacing:0;fill:#6f6a61}.bkp .swing{stroke-width:7px}.bkp .thin{stroke-width:10px}
'''

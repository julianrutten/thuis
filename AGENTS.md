# Thuis: verbouwing Gasthuisstraat 6-a

Werktaal is Nederlands.

## Waar staat wat

- `Verbouwing plan 2026/2620-20261002-V04.pdf`: ontwerp VO4 van Lenz (02-10-2026). Blad 9 is het grondplan 1:100 waar aannemer en loodgieter mee werken.
- `Verbouwing plan 2026/Detaillering bijkeuken Gasthuisstraat 6-a.pdf`: detaillering bijkeuken (13-11-2026, negen bladen). Dit is de stijl voor alles wat naar aannemer, loodgieter of Lenz gaat. Bron in `Verbouwing plan 2026/Bijkeuken/` (zie `README.md` daar). De versie van 29-10-2026 staat in `Verbouwing plan 2026/archief/`.
- `Verbouwing plan 2026/Detaillering CV-installatie woning Gasthuisstraat 6-a.pdf`: detaillering CV voor aannemer en loodgieter (vier bladen). Bron in `CV/detaillering-woning/`.
- `Verbouwing plan 2026/CV/`: CV-ontwerp loods en huis. `README.md` daar beschrijft het versiebeheer: `index.html` en `notities.html` zijn altijd de actuele revisie (nu rev. K), oude revisies staan in `archief/rev-x/`.
- `Verbouwing plan 2026/Gemeente/`: omgevingsdialoog.

## Werkwijze

- **Bij elke wijziging alle documenten bijwerken.** Verandert er iets aan het ontwerp, dan moeten in dezelfde beurt alle stukken waarin het voorkomt worden aangepast: de CV-tekenset en notities (`CV/`, nieuwe revisie, opnieuw publiceren), de detaillering CV-installatie woning, de detaillering bijkeuken en dit bestand. Geen "dat loopt nog achter" laten staan; anders raakt Julian het overzicht kwijt (zijn woorden, 13-11-2026). Kan een stuk niet meteen worden bijgewerkt, zeg dat dan vooraf en los het eerst op.
- **Eén bron voor de bijkeuken-tekeningen:** `Bijkeuken/tekening.py`. Daaruit tekenen de detaillering bijkeuken (`Bijkeuken/bouw.py`), de detaillering CV-installatie en blad CV-03 van de tekenset (beide via `CV/bijwerken.py`). Verandert de indeling: `tekening.py` aanpassen, beide scripts draaien, beide PDF's opnieuw maken, tekenset opnieuw publiceren.
- **Tekenstijl:** die van de detaillering bijkeuken: dunne lijnen, kleine tekst (±6 pt), maatkettingen met schuine streepjes en hulplijnen, kleine codeblokjes (D1, W2). Julian vond de eerste, grovere tekeningen in de CV-detaillering duidelijk minder net (13-11-2026). Nieuwe tekeningen dus met de hulpfuncties en klassen uit `tekening.py` maken.
- Documenten voor aannemer, loodgieter of Lenz: een nette PDF op A3 in de stijl van de detaillering bijkeuken, geen artifact. Leidingen en onderdelen staan leesbaar op de tekening zelf benoemd; een legenda mag erbij, maar alleen nummers met een legenda is niet genoeg.
- Houd zulke documenten eenvoudig, zeker voor een eerste gesprek: geen vragenlijsten per partij, geen uitputtende maten en instellingen. Een vakman vult de details zelf in. (Julian vond de eerste versie van de CV-detaillering "overdreven"; het voorblad was goed.)
- Eigen analyses en het CV-ontwerp: als artifact (zie `CV/README.md` voor de vaste link).
- Wie maakt wat: de loods en de grondleiding zijn eigen werk van Julian (hij heeft een graafmachine, Cat 301.8). De loodgieter maakt alleen het huis, vanaf de grondleiding.

## Besluiten woning (t/m 13-11-2026)

Alles hieronder is verwerkt in rev. K van de tekenset en in beide detailleringen.

- **Indeling bijkeuken** (besluit Julian 13-11-2026). Kastenwand voorgevel: D1 kapstok 852, D2 kast met wasmachine en droger gestapeld 680 × 650, D3 zitbank 800, D4 schoonmaakkast 444. Werkruimte: W1 koel/vries-kolom tegen de linkerwand (koelkast en vriezer worden veel gebruikt vanuit het keukentje, dus niet in de gang), W2 techniekkast CV tegen de rechterwand, W8 voorraadkast.
- **Techniekkast** (W2): 1000 breed, 650 diep, 2600 hoog; de voorraadkast W8 ernaast is 788 breed. Buffervat B2 van 100 L laag in de hoek bij de binnenmuur. Achterwand: verswatermodule boven het vat, de twee pompgroepen links ervan. Linker zijwand (650 diep): verdeler VD1 onderaan, daarboven elektra en expansievat. Vervallen: D2 in de kastenwand (632/832/1232, te krap) en 1300 × 650 met 200 L (rev. I en J: Julian vond dat "veel te groot"). De zijwand benutten en de verdeler daarheen was Julians idee: niet alles naast elkaar op de achterwand zetten.
- Vloerverwarming met twee verdelers: VD1 in de techniekkast (linkerhelft), VD2 in de kastenwand van de garderobe (rechterhelft). Julian is akkoord.
- De verdieping houdt haar bestaande radiatoren. De bestaande CV-installatie staat nu in de hoek van de bestaande woning, waar de tunnelhaard komt; daar lopen de leidingen naar boven. Vanuit de techniekkast gaat daar een eigen pompgroep met mengkraan heen (V4 + P7), plus warm en koud tapwater voor de kraan boven.
- Element E2 in het huisvat: 3 kW, onderin, met de hand geschakeld, thermostaat 75 °C (vervangt "tot 6 kW, bovenin, 52 °C automatisch"). Voeding 1 × 16 A. Expansievat X2 18 L (berekening Codex: 100 L, 75 °C, 2,5 bar).
- De grondleiding komt door de linkergevel binnen ter hoogte van de werkruimte en loopt recht naar de techniekkast; totaal ±18 m.
- Geen circulatieleiding, geen doorstromer, geen gasketel. Wel een afgedopte gasleiding van de meterkast naar de techniekkast.
- Tunnelhaard in de woonkamer: gewone Spartherm, niet op de CV.

## Kachel in de loods (besluiten t/m 12-11-2026)

### Keuze

- Er komt één kachel op de CV, in het kantoor van de loods. In huis komt een gewone Spartherm-tunnelhaard die niet op de CV zit.
- Gekozen kachel: **Walltherm Vajolet**, houtvergasser met ruit, ±€7.500.
- Afgevallen: Neptunus 30 kW van HGB Trading (€1.999, 22–23 kW naar water, 76 % rendement, 3 bar volgens de verkoper): te veel vermogen en laag rendement. Ook afgevallen: Spartherm Linear Tunnel H2O als CV-haard in huis (±€8.000–10.000 meerkosten, te ingewikkeld).

### Gegevens Walltherm Vajolet (handleiding V01, via eco2all.nl)

| | |
|---|---|
| Nominaal vermogen | 10 kW, bereik 8–15 kW |
| Verdeling | tot 80 % naar het water, 20 % straling |
| Rendement | > 90 % |
| Maximale bedrijfsdruk | 2,5 bar |
| Waterinhoud, gewicht | ±80 L, 300 kg leeg, ±380 kg gevuld |
| Rookgastemperatuur | 130–170 °C bij vergassing, tot 400 °C bij aansteken |
| Rookgasmassastroom | 8,8 g/s |
| Vereiste trek | 12 Pa, maximaal 20 Pa (elders in de handleiding: 12–15, max 25) |
| Rookaansluiting | Ø 150 mm inwendig |
| Hout | maximaal 35 cm lang, droog |
| Buitenlucht | kanaal Ø 125 mm, maximaal 4 m, niet vanaf het dak |
| Afstand rookpijp tot brandbaar materiaal | 50 cm |

De handleiding vraagt een geïsoleerde schoorsteen (minimaal 20 mm, anders "werkt hij waarschijnlijk niet"), 0,3–0,5 m verticaal vóór de eerste bocht, en noemt "ca. 6 m" als beste lengte. Een aanbieder noemt een buffer van 1.000 L of meer.

### Schoorsteen

- Loods: 12 × 50 m, wandhoogte 1,90 m, dak 16° van sandwichpanelen. Vrije hoogte op de plek van de kachel ±3,30 m, nok ±3,6–3,7 m.
- De kachel komt maximaal ±3 m de loods in, anders kunnen er geen auto's meer doorrijden.
- Besluit: recht omhoog vanaf de kachel, zonder bochten, dubbelwandig Ø 150/200, door het dak, **1 m boven het dak**. Een hoge schoorsteen is niet gewenst: er staat altijd stevige wind en het oost/zuid-dakvlak is voor zonnepanelen.
- Berekende natuurlijke trek (vereenvoudigde schatting, rookuitlaat op ±1,4 m, 5 °C buiten): ±1 m boven het dak 9–11 Pa, 2 m 13–16 Pa, 3 m 16–20 Pa. Wind over de mond geeft meestal extra trek, bij harde wind mogelijk te veel.
- Na de installatie de trek meten. Terugvalopties: een rookgasventilator bovenop (type Darco GCK Ø 150: 94 W, tot 42 Pa, rookgas tot 400 °C) met toerenregelaar, en een trekbegrenzer als de trek boven de 20 Pa komt. Geen lucht in de kachel blazen: dat zet hem onder overdruk.
- Kap: een gewone regenkap of windneutrale kap, geen trekkende kap.
- Onderdelen: HGB Trading heeft de hele reeks dubbelwandig Ø 150, waaronder dakplaat hellend 5–30° (€82,49), sectie 1000 mm (€89,95), schuifsectie 280–500 mm (€107,13), stormkraag, dakbevestigingsbeugel en tuibeugel 3-punts (€30,41). Nog na te vragen: afdichting op sandwichpanelen, afstand tot brandbaar materiaal, isolatiedikte, welk aansluitstuk.

### Gevolgen voor het CV-ontwerp (verwerkt in rev. K)

- Alle veiligheidsventielen 2,5 bar in plaats van 3 bar.
- **Twee buffervaten van 750 L in serie** (besluit Julian 13-11-2026). Expansievat X1 300 L, technische ruimte loods ±3300 × 2200.
- De laadunit moet de retour op minimaal 60 °C houden (eis handleiding).
- Tien uur stoken is ±100 kWh, waarvan ±80 kWh naar het water, en kost ±28 kg droog hout.
- **Nog open:** de warmtepomp alleen op de bovenste helft van het eerste vat, met een dagvenster (advies Codex, niet bevestigd). Het schema CV-01 toont de twee vaten als één symbool "2 × 750 L in serie"; de plattegrond CV-02 toont ze apart.

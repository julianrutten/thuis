# CV-systeem loods en huis

Ontwerp van het CV-systeem met warmtepomp, pelletkachel (Nordic Fire HRV Torsby) en buffervat in de loods, een duoleiding naar het huis en de installatie in de techniekkast: een hoekkast van 700 × 1400 in de speelkamer, in de hoek bij de trap.

**Actuele versie: rev. W, 13-11-2026.**

Open `index.html` in een browser. Er is geen build-stap nodig. Online staat dezelfde set op https://claude.ai/artifact/MGdHUn5eSu7e3egPYovpRu. Die link toont altijd de actuele revisie.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `index.html` | Tekenset CV-01 t/m CV-05 van de actuele revisie: wijzigingen, installatieschema, technische ruimte loods, techniekkast huis, regeling en elektra, leidingtracé, stuklijst, berekeningen en open punten |
| `notities.html` | Onderbouwing bij de actuele revisie: uitgangspunten, warmtebehoefte, douchen, warmtepomp, buffer, grondleiding, kachel en schoorsteen, tapwater en B2, gasketel, haard, wachttijd, techniekkast en inkoop |
| `img/situatie.jpg` | Onderlegger voor CV-05, uit de situatietekening VO4 (Lenz, 02-10-2026) |
| `loods_plattegrond.py` | Plattegrond 1:100 van de ruimtes in de loods (kantoor, berging, voorkamer, hal, toilet, met de kachel in de nis, het vat erachter en de warmtepomp buiten). Zet de tekening op blad 2 van "Zelf regelen CV-installatie loods" (1:100) en een uitsnede op blad CV-02 van de tekenset; daarna de PDF opnieuw maken en de tekenset publiceren |
| `detaillering-woning/` | Bron van de detaillering voor aannemer en loodgieter (A4 liggend, zeven bladen: voorblad, leidingplan 1:75 met CV, tapwater, afvoer en ventilatie, groepenplan vloerverwarming 1:100, techniekkast 1:20, principeschema met onderdelenlijst, twee bestellijsten met merk, type, aantal en winkellinks: per hoofdonderdeel met toebehoren, en klein materiaal apart). Leesbaar op een A4 in zwart-wit: lopende tekst minimaal 9 pt, tekst in tekeningen minimaal 7 pt, leidingen verschillen in lijnsoort en dikte en niet alleen in kleur. `detaillering.html` met `grondplan-vo4.svg` als onderlegger (blad 9 van VO4). De PDF staat een map hoger: `Detaillering CV-installatie woning Gasthuisstraat 6-a.pdf` |
| `zelf-regelen/` | Bron van de stukken "Zelf regelen" (A4 liggend; loods tien bladen met een plattegrond op blad 2, de inrichting van het kantoor op blad 7 tot en met 9 uit `loods_kantoor.py` en de keuken van de voorkamer op blad 10 uit `loods_keuken.py`; woning drie). `zelf-regelen-loods.html` → "Zelf regelen CV-installatie loods": eigen werk, beslissen, navragen, elektra en de bestellijsten van de loods (kachel, warmtepomp, vat, rookgasafvoer); maken met dezelfde opdracht en de bestandsnaam van de loods. `zelf-regelen.html` → "Zelf regelen CV-installatie woning": wat het project van Julian zelf vraagt, met de stroomvoorziening. De regeling zelf (motoren, thermostaten, regelaars) staat sinds 13-11-2026 met prijzen in de detaillering. Maken: `cd CV/zelf-regelen` en dan dezelfde Chrome-opdracht als hieronder met `--print-to-pdf="../../Zelf regelen CV-installatie woning Gasthuisstraat 6-a.pdf"` en `zelf-regelen.html` |
| `vloerverwarming.py` | Groepenplan vloerverwarming: de zones (in punten van blad 9 van VO4), de buisafstand en de aanlooplengte per groep. Rekent oppervlak en buislengte uit en tekent het plan en de tabel. Aanpassen hier, daarna `bijwerken.py` draaien |
| `bijwerken.py` | Zet de tekeningen uit `../Bijkeuken/tekening.py` in de tekenset (techniekkast op blad CV-03: `TECHWAND`, `TECHACHTER`, `TECHPLAN_CV`) en in de detaillering woning (bijkeuken op het leidingplan, en blad techniekkast). Zo tonen alle stukken dezelfde indeling in dezelfde tekenstijl |

## Versies

| Rev. | Datum | Belangrijkste wijzigingen | Plaats |
|---|---|---|---|
| **W** | 13-11-2026 | Loods vereenvoudigd (besluiten Julian). Julian zet de kachel zelf aan: geen vrijgave door de regelaar en geen buitenvoeler. Mengklep V3 naar het huis vervalt; de watertemperatuur wordt op de kachel ingesteld op hooguit ±75 °C (vat 55 → 75 °C, 17 kWh). Luchtverhitter LV1 met P6 vervalt (airco van 30 kW in de loods). Back-upelement E1 vervalt. Buffervat EnergyBy EBB-0B-750, pelletafvoer recht omhoog door het dak. Verswatermodule loods zelf samengesteld (platenwisselaar, mengventiel 60 °C, pomp, stromingsschakelaar). Huis ongewijzigd, behalve aanvoer uit de loods maximaal 75 °C | `index.html`, `notities.html` |
| V | 13-11-2026 | Loods opnieuw opgezet (eerste wijziging sinds rev. K). Kachel wordt een CV-pelletkachel Nordic Fire HRV Torsby (3,3–15 kW, 11,7 kW naar water) in plaats van de Walltherm. De warmtepomp is de hoofdbron en houdt het vat het hele jaar op 55 °C; de kachel springt bij onder ±0 °C en stookt het vat naar 80 °C. Eén buffervat van 750 L in plaats van twee, X1 200 L, technische ruimte 2600 × 2200. Laadunit, thermische afloopbeveiliging en het rookkanaal Ø 150 vervallen: retour via mengventiel 55 °C, pelletafvoer Ø 80. Overschotgroep met luchtverhitter alleen nog als optie | git-geschiedenis |
| U | 13-11-2026 | Techniekkast 700 × 1400 in plaats van 600 × 1200 (Julian: te krap met alle leidingen). Nieuwe indeling: vat op de achterwand met ±15 cm aan elke kant en vrije ruimte eronder; verswatermodule op de lange wand naast de verdeler; pompgroep radiatoren op de zijwand; expansievat onder de WTW-unit. Leidingen in de kast ingetekend met isolatie, op schaal. De kast ernaast wordt 10 cm korter | git-geschiedenis |
| T | 13-11-2026 | Hoofdonderdelen van de techniekkast gekozen en ingetekend. Verdeler vloerverwarming met ingebouwde pomp, mengventiel en maximaalthermostaat (VTE Composiet 14 groepen, 825 × 400 × 160): de losse pompgroep V2 + P5 vervalt. Pompgroep radiatoren met mengventiel tot 60 °C (was 70 °C). Verswatermodule Technische Alternative FRISTAR3 (366 × 573 × 160) onder het vat; vrije ruimte voor E2 ±40 cm. Expansievat 12 L Ø 280 × 295. Element E2: voorstel Inventum 3 kW 1½" × 14". WTW-unit in de rechter uitvoering, vier aansluitingen. Bestellijsten met winkellinks op blad 6 en 7 van de detaillering. Groepenplan van rev. S goedgekeurd en ongewijzigd | git-geschiedenis |
| S | 13-11-2026 | Groepenplan vloerverwarming opnieuw opgezet na een kritische beoordeling. Eetkamer en woonkamer in vier banen die bij het glas beginnen (1 eetkamer links, 2 eetkamer rechts met de strook langs de haard, 3 vóór de bank: 100 mm in de eerste meter en 150 mm naar de haard toe, 4 een U om de bank heen); groep 2 lag in rev. R als een gesloten ring om groep 3 en was niet te leggen zonder kruisingen. Geen groep langer dan ±90 m (was ±100 m). Doorgang keuken–eetkamer bij groep 13; looproute keuken 150 mm (hoofdroute; met de aanloopleidingen van groep 1 en 2 erbij ±105 mm); het stuk rechts van het kookeiland bij groep 12. Aanloop in mantelbuis door de speelkamer en door het halletje naar de badkamer. Alle buisafstanden in veelvouden van 50 mm (100, 150, 200), het raster van de gangbare noppenplaat. Voorstellen, niet besloten: handdoekradiator in de badkamer op V4 + P7, weersafhankelijke mengregeling voor de vloer | git-geschiedenis |
| R | 13-11-2026 | Groepenplan vloerverwarming: 14 groepen op één verdeler, ±124 m² en ±1000 m buis 16 × 2, langste groepen ±100 m. Buisafstand 100 mm in de badkamer, langs het aanrecht, vóór de bank en in een strook van 0,6 m langs de ruiten van eetkamer en woonkamer; 150 mm in de andere leefruimtes; 200 mm in de slaapkamer, rond de haard, onder de bank en onder de trap. Vloer: tegels, behalve hout in slaapkamer, garderobe en zithoek. Aanloopleidingen in drie bundels door de looproutes. Tekening op blad 3 van de detaillering, tabel in de notities | git-geschiedenis |
| Q | 13-11-2026 | De grondleiding komt binnen in de lijn van de buitendeur van de eetkamer (zo loopt het tracé naar de loods werkelijk) en loopt ±11,5 m in een rechte lijn door de vloer naar de techniekkast; niet meer onder de bijkeuken door. Totaal ±27 m | git-geschiedenis |
| P | 13-11-2026 | Buffervat B2 wordt een wandmodel van 80 L (Metalac 80-8 TPZ: Ø 395 × 1120, 6 bar, aansluitingen 5/4" links en rechts, mof 6/4" onderin voor E2). De hoekkast blijft 600 × 1200. E2: 80 L in ±2 uur, ±16 minuten douchen. Leidingen naar het stijgpunt bij de haard in een rechte lijn, ±8,5 m. Element E2 van onderaf in de mof van 6/4"; passend type nog te vinden | git-geschiedenis |
| O | 13-11-2026 | Techniekkast is alleen nog de hoekkast: 600 × 1200, minimaal 2400 hoog; de lange kast wordt een kast met lades (maximaal 450 diep, 150 vrij erachter voor het ventilatiekanaal naar de keuken). B2 100 L als wandmodel, hangend. Eén verdeler van ±14 groepen. X2 12 L. WTW-unit S&P Energisava 260 (560 × 635 × 260, Ø 125). Grondleiding ±28 m, waarvan ±12,5 m in huis. Open: 600 breed is krap, 900 breed is de ruime variant. Later op de dag bijgewerkt zonder nieuwe letter: de leidingen naar het stijgpunt bij de haard lopen in een rechte lijn (±8,5 m) | git-geschiedenis |
| N | 13-11-2026 | Ventilatie vereenvoudigd: de WTW-unit zuigt af in badkamer en keuken (kanaal bovenin de techniekkast, ventiel in de tussenmuur tussen kast en keuken). Afzuiging in de zithoek met een kanaal in de vloer vervalt. WTW niet op een warmeluchtkanaal van de haard. Verder gelijk aan rev. M | git-geschiedenis |
| M | 13-11-2026 | B2 weer 100 L (past in 600 diep bij Ø ≤ 540). WTW-unit in een diepere hoekkast (±900 × 900) aan de kant van de garderobe; het vat en de verswatermodule aan de kant van de woonkamer. Afvoeren ingetekend: standleiding in de techniekkast als verzamelpunt (badkamer boven en beneden, toilet, keuken, bijkeuken, condens, veiligheidsventiel). Leidingen in huis rechtstreeks: geen tappunt verder dan ±10 m, wachttijd ±10–15 s. Grondleiding ±25 m, waarvan ±10 m in huis | git-geschiedenis |
| L | 13-11-2026 | Besluiten uit het gesprek met de loodgieter. Techniekkast verhuist naar de kast tussen speelkamer en trap (±3200 × 600, deuren naar de speelkamer). B2 50–60 L. VD1 en VD2 allebei in de techniekkast. Gas vervalt: aansluiting wordt afgesloten, geen gasleiding en geen reserve-aansluitingen meer. WTW-unit ventilatie in de techniekkast: afzuiging zithoek (kanaal in de vloer) en badkamer, toevoer hal boven en slaapkamer/hal. Grondleiding ±29 m, waarvan ±14 m in de vloer van het huis. Wasmachine en droger terug naar de werkruimte van de bijkeuken (W2). Loods ongewijzigd | git-geschiedenis |
| K | 13-11-2026 | Loods: twee buffervaten van 750 L in serie, X1 300 L, technische ruimte 3300 × 2200. Huis: B2 100 L, techniekkast 1000 × 650 (was 1300), verdeler op de linker zijwand, verswatermodule boven het vat, X2 18 L. Open: warmtepomp op de bovenste helft van het eerste vat | git-geschiedenis |
| J | 13-11-2026 | Indeling techniekkast huis: verdeler en pompgroepen op de achterwand naast het vat, verswatermodule, expansievat en elektra op de linker zijwand. B2 blijft 200 L. Blad CV-03 heeft er een aanzicht van de zijwand bij | git-geschiedenis |
| I | 13-11-2026 | Kachel gekozen: Walltherm Vajolet (10 kW, tot 80 % naar water, max 2,5 bar); alle veiligheidsventielen 2,5 bar, X1 250 L, rookkanaal recht omhoog tot 1 m boven het dak. Techniekkast huis verhuisd naar de rechterwand van de werkruimte (1300 × 650), B2 200 L, E2 3 kW onderin en handgeschakeld op 75 °C, X2 25 L. Bestaande radiatoren boven op eigen pompgroep V4 + P7, met warm en koud water via het stijgpunt bij de haard. Grondleiding komt binnen ter hoogte van de werkruimte, ±18 m. Open: één of twee buffervaten | git-geschiedenis |
| H | 12-11-2026 | Besluiten vastgelegd, tekeningen gelijk aan rev. G. Haard in huis wordt een gewone Spartherm-tunnelhaard, niet op de CV; alleen de loodskachel zit op de CV. Grondleiding is eigen werk. Nieuw open punt: warmte van de haard verspreiden (warmeluchtkanalen; de WTW verplaatst weinig warmte) | git-geschiedenis |
| G | 12-11-2026 | Warmtepomp 12 kW (op het oog HouseHeating HH-C3-12). Loods: eigen verwarmingsgroep (P3) met radiatoren in voorkamer, kantoor en toilet, en eigen overschotgroep (P6) met luchtverhitter LV1 van 15–20 kW. Mengklep V3 houdt de grondleiding op maximaal 78 °C; B1 mag tot ±88 °C. Tabel "wie maakt wat": loods eigen werk, huis loodgieter. Haard in huis (wel of niet op de CV) als open punt, met advies in de notities | git-geschiedenis |
| F | 12-11-2026 | Circulatie tapwater vervalt, toevoer badkamer terug naar 16 × 2; de wachttijd van ±25–30 s wordt geaccepteerd. Expansievat X2 12 L. Afgedopte gasleiding van de meterkast naar D2 als voorbereiding | git-geschiedenis |
| E | 12-11-2026 | Doorstromer vervalt. Elektrisch element E2 (tot 6 kW) hoog in B2. B2 terug naar 100 L. Techniekkast D2 832 × 600 in de kastenwand van de bijkeuken, kapstok D1 700. Circulatie op aanvraag naar de badkamer (CP1), toevoer 20 × 2. Geen gasketel, wel twee reserve-aansluitingen op B2. Notities bijgewerkt | git-geschiedenis |
| D | 12-11-2026 | Warmtepomp 8 kW met winterstand 45 °C en zomerstand 55 °C. E1 alleen back-up. Duoleiding 40/160. Overschot op de onderste voeler. B2 150–200 L met twee voelers. Doorstromer 11 kW bij de badkamer. Verdelers VD1 en VD2, niets onder de trap. Eén regelaar | git-geschiedenis |
| C | 12-11-2026 | Uitgangspunt: warmtepomp 12 kW vast op 55 °C, B2 100 L, doorstromer 6 kW in D2, verdeler in de trapkast | git-geschiedenis |

## Werkwijze

1. `index.html` en `notities.html` zijn altijd de actuele revisie. De revisie en de datum staan in het tekeninghoofd rechtsboven.
2. Het versiebeheer staat sinds 13-11-2026 in git: elke ronde wijzigingen wordt een commit op `master`. Er zijn geen archiefmappen meer; de vervallen revisies C t/m V staan in de eerste commit (`ac255e1`).
3. De nieuwe revisie krijgt de volgende letter, een tabel "wat er verandert" bovenaan de tekenset en een regel in de tabel hierboven.
4. De tekenset bevat de open punten. De notities bevatten de onderbouwing. Staat iets op beide plekken, dan geldt de tekenset.
5. Verandert de indeling van de bijkeuken of de techniekkast, pas dan `../Bijkeuken/tekening.py` aan en draai `../Bijkeuken/bouw.py` en `bijwerken.py`. Maak daarna beide PDF's opnieuw en publiceer de tekenset opnieuw.

## Detaillering woning opnieuw maken

```
python3 CV/bijwerken.py
cd "CV/detaillering-woning"
google-chrome --headless=new --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="../../Detaillering CV-installatie woning Gasthuisstraat 6-a.pdf" "file://$PWD/detaillering.html"
```

De detaillering volgt de actuele revisie van de tekenset (nu rev. W). Coördinaten op het leidingplan zijn de punten van blad 9 van VO4 (1 m = 28,35 pt).

## Bronnen

- VO4 principeverzoek, Lenz, 02-10-2026 (`../2620-20261002-V04.pdf`)
- Detaillering bijkeuken, 13-11-2026 (`../Detaillering bijkeuken Gasthuisstraat 6-a.pdf`, bron in `../Bijkeuken/`). De versie van 29-10-2026 staat in de git-geschiedenis.
- Handleiding Walltherm Vajolet V01 (eco2all.nl)
- Prijzen grondleiding: benem.nl, 12-11-2026

## Status

Concept. Dit zijn ontwerpberekeningen en schattingen. De installateur bepaalt de definitieve uitvoering.

# Detaillering bijkeuken

Bron van `../Detaillering bijkeuken Gasthuisstraat 6-a.pdf` (A3, negen bladen).

**Actuele versie: 13-11-2026, na het gesprek met de loodgieter.** De versie van 29-10-2026 staat in `../archief/`.

| Bestand | Inhoud |
|---|---|
| `tekening.py` | Alle tekeningen van de bijkeuken (plattegrond, wandaanzichten, details) en de tekenstijl. Ook de tekeningen van de techniekkast (hoekkast in de speelkamer) staan hier (`TECHWAND`, `TECHACHTER`, `TECHPLAN_CV`). De detaillering CV-installatie woning en de tekenset tekenen hieruit, zodat alle stukken dezelfde indeling tonen |
| `bouw.py` | Teksten, tabellen en bladindeling. Schrijft `detaillering-bijkeuken.html` |
| `origineel/blad5–7.svg` | Bladen uit de versie van 29-10-2026. De details die niet zijn veranderd (kapstok D1, binnenmuur D5, koel/vries-kolom, pizzaoven-nis) worden hieruit overgenomen |

## Opnieuw maken

```
cd "Bijkeuken"
python3 bouw.py
google-chrome --headless=new --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="../Detaillering bijkeuken Gasthuisstraat 6-a.pdf" "file://$PWD/detaillering-bijkeuken.html"
python3 ../CV/bijwerken.py   # daarna ook de CV-detaillering opnieuw naar PDF en de tekenset opnieuw publiceren, zie ../CV/README.md
```

## Indeling (13-11-2026, na het gesprek met de loodgieter)

- Kastenwand voorgevel: D1 kapstok 852, D2 gewone hoge kast 680 × 600, D3 zitbank 800, D4 schoonmaakkast 444.
- D5 binnenmuur met inbouwschuifdeur.
- Werkruimte: W1 koel/vries-kolom tegen de linkerwand (1280 × 650), W2 kast met wasmachine en droger gestapeld tegen de rechterwand (680 × 650), W8 voorraadkast 1108 breed, aanrecht met pizzaoven langs de achterwand.
- De techniekkast van de CV staat niet meer in de bijkeuken, maar in een hoekkast in de speelkamer. De grondleiding uit de loods loopt niet door de bijkeuken: die komt binnen bij de buitendeur van de eetkamer.

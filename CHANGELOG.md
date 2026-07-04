# Changelog - Feestcafe De Dokter Website

## v15 - 2026-07-04
- `.nojekyll` toegevoegd: schakelt de legacy Jekyll-build van GitHub Pages uit (pure statische site); de Pages-build faalde herhaaldelijk op de favicon-commit met een generieke "Page build failed" (@herriaan)
- Favicon toegevoegd op basis van het logo: `favicon.ico` (16/32/48), `favicon-32.png`, `favicon-192.png` en een `apple-touch-icon.png` (180px, logo op donkere teal-achtergrond) met bijbehorende link-tags in de head (@herriaan)

## v14 - 2026-07-03
- Fotostrip: twee kaarten toegevoegd uit aangeleverd klantbeeld (mail 2 jul): "Beste DJ's" (DJ achter de decks) en "De krokodil" (het krokodil-shotspel aan de bar). Rondt issue #6 af (DJ-foto stond nog open) (@herriaan)

## v13 - 2026-07-03
- Het Rad: uitkomst klopt nu met waar de pijl wijst. De rad-afbeelding heeft 23 segmenten (niet 24); de oude prijzenlijst had een label te veel én verkeerde labels in de onderste helft, waardoor de uitkomst ~1 segment verschoof en verkeerde prijzen toonde. Alle 23 segmentgrenzen + prijzen zijn pixel-gemeten uit `assets/img/draairad.png` en visueel geverifieerd; pijl-naar-segment-berekening vereenvoudigd (`SEG_START` + `segmentAt`/`pointerImageAngle`). Calibratie-script toegevoegd: `scripts/rad-meten.py` (@herriaan)

## v12 - 2026-07-03
- Fotostrip: "Het team" en "Proost!" vervangen door nieuw aangeleverd beeldmateriaal (klant). De oude "Proost"-foto toonde een medewerkster die niet meer in dienst is; nu een proost/rocketshot-foto. Beide met De Dokter-logo, nieuwe bestandsnamen voor cache-busting; alt-tekst "Proost" aangescherpt (@herriaan)

## v11 - 2026-06-23
- Fotostrip: "Het team" nu een echte teamfoto (4 medewerkers in De Dokter-uniform) i.p.v. een interieurfoto; "Aan de bar" nu de bar met barman + publiek i.p.v. een poserende tray-foto. Beide uit aangeleverd beeldmateriaal (Drive), geoptimaliseerd naar max 1600px + betekenisvolle alt-teksten (issue #6) (@herriaan)
- Nog open binnen issue #6: een aparte DJ-foto. Geen authentieke DJ-foto in het aangeleverde materiaal; wacht op de klant (@herriaan)

## v10 - 2026-06-19
- Lettertypes naar Reetraa-huisstijl: body Open Sans, koppen Bangers (accent Permanent Marker en Caveat behouden) (@herriaan)
- "Rad van Fortuin" overal vervangen door "Rad" (hero, about, radsectie, alt-tekst) (@herriaan)
- Tekstcorrecties: Privéfeest, Confettiregen (@herriaan)
- Zin toegevoegd over de beste feestdj's van Nederland in de about-sectie (@herriaan)
- Footer: adres Havermarkt 27 en telefoon 06-23855950 ingevuld (@herriaan)

## v9 - 2026-03-12
- Design polish op basis van frontend-design review
- Donkere secties: hoger contrast (0.78 opacity) + backdrop-filter blur
- Medische SVG illustraties op donkere secties (bloedzak, spuit, pil, stethoscoop, hart, thermometer, infuus)
- Medische illustraties zichtbaarder (0.07 → 0.15 opacity)
- Gouden text-shadow op alle sectie-kopjes
- Foto galerij: Polaroid-stijl met rotaties, witte rand en handgeschreven bijschriften
- Gevarieerde scroll-reveal animaties (links, rechts, scale-up) ipv uniform fadeUp
- About foto: scheef met rand en schaduw (Polaroid-effect)
- Mascotte klikbaar: toont random dokters-quips in speech bubble
- Wheel mapping: SEGMENT_OFFSET 0 → 7.5 (half segment correctie)
- Footer: gouden social hover, speelse tagline, Spreekuur ipv Openingstijden
- Social link hover: goud ipv teal

## v5 - 2026-03-12
- Confetti nu multi-color (roze, geel, blauw, paars, oranje, groen, wit, rood) - 350 stuks
- Medische iconen in meerdere kleuren (teal, roze, goud, paars)
- Kopjes (h2) in Luckiest Guy font voor speelser effect
- RX symbool verwijderd uit receptblok en resultaatkaart
- Receptkaart verschijnt als overlay over het rad (niet eronder)
- Hartslagmonitor dunner en transparanter
- Logo in navigatie helderder/beter leesbaar
- Rad van Fortuin: physics-based drag-to-spin (muis en touch)
- Rad mapping formule gecorrigeerd (richting was omgekeerd)
- Segmentvolgorde geupdate om overeen te komen met het radbeeld

## v4 - 2026-03-12
- Achtergrond verschoven van puur zwart naar donker teal (#071a17)
- Canvas met ~200 confetti rectangles + ~30 medische iconen
- Mascotte fixed rechtsonder met float-animatie en druppel uit spuit
- Sectie-achtergronden met groene gradienten

## v3 - 2026-03-12
- Luckiest Guy font voor logo/hero titel
- Prescription-styled resultaatkaart met typewriter effect
- Glow orbs op 0.20 opacity met groene tint
- Sectie gradienten toegevoegd
- Git repo geinitialiseerd

## v2 - 2026-03-12
- Eerste versie met interactief rad, foto galerij, video hero
- Neon flicker animatie, scroll-reveal
- Glow orbs achtergrond (0.08 opacity)
- Drag-to-scroll foto strip

## v1 - 2026-03-12
- Initiele opzet: hero, about, wheel, photos, info, footer
- Dark theme met teal accenten

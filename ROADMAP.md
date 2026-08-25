# Roadmap - Feestcafe De Dokter Website

## Done

- [x] Initiele opzet: hero, about, wheel, photos, info, footer (v1)
- [x] Dark theme met teal accenten en CSS variabelen
- [x] Video hero met neon flicker animatie
- [x] Confetti achtergrond (afbeelding, canvas variant verwijderd vanwege Chrome flicker)
- [x] Mascotte fixed rechtsonder met float-animatie en klikbare quips (v4)
- [x] Luckiest Guy font voor headings/logo (v5)
- [x] Physics-based drag-to-spin Rad van Fortuin met receptkaart resultaat (v5)
- [x] Foto galerij: Polaroid-stijl met rotaties en handgeschreven bijschriften (v9)
- [x] Medische SVG illustraties op donkere secties (v9)
- [x] Scroll-reveal animaties (links, rechts, scale-up) (v9)
- [x] Gouden text-shadow op sectie-kopjes (v9)
- [x] Chrome glitch fixes: fixed bg div, geen backdrop-filter, geen canvas confetti
- [x] Debug overlay (`?debug`) voor rad-kalibratie
- [x] GitHub Pages deploy (auto bij push naar main)
- [x] README.md en ROADMAP.md toegevoegd
- [x] Rad mapping kalibratie - rad heeft 23 segmenten (niet 24); alle grenzen + prijzen pixel-gemeten uit draairad.png en geverifieerd, uitkomst klopt nu met de pijl (v13, 3 jul). Script: `scripts/rad-meten.py`
- [x] Fotoronde 2 jul verwerkt: team/proost vervangen, dj- en krokodilfoto toegevoegd; originelen in `assets/aanlevering-2026-07-02/` (v12/v14, 3 jul)
- [x] Favicon: mascotte-hoofd als tab-icoon + apple-touch-icon; `.nojekyll` toegevoegd na falende Pages-build (v15/v16, 4 jul)

## In Progress

- (niets)

## Next

- [x] Echte teamfoto + bar-foto in fotostrip (issue #6, 23 jun)
- [x] "Het team" + "Proost" foto's vervangen door klantbeeld (v12, 3 jul)
- [x] DJ-foto + krokodil in fotostrip (issue #6) - "Beste DJ's" + "De krokodil" geplaatst uit klantbeeld (v14, 3 jul)
- [x] Contact gegevens in footer vervanging door echte data (nu placeholders) — live site
  (feestcafededokter.nl, WordPress, niet deze GitHub Pages-repo) gecorrigeerd 25 aug 2026:
  mailadres info@cafededokter.nl → info@feestcafededokter.nl, telefoon 06-23855950 bevestigd
  correct door de klant (geen placeholder, geen wijziging nodig). Deze repo's eigen
  `index.html` bevat geen contactgegevens en is niet de live bron.
- [ ] Openingstijden verifieren met klant
- [ ] Glitch/flicker definitief verifieren met klant
- [ ] Custom domein koppelen (indien gewenst)
- [ ] Performance: lazy loading voor foto's en video
- [ ] SEO: Open Graph meta tags en structured data

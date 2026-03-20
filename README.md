# Feestcafe De Dokter - Website

One-page website voor Feestcafe De Dokter (Breda), een medisch/dokter-thema feestcafe. Klant via Reetra Horeca Beheer.

**Live**: https://herriaan.github.io/de-dokter-website/

## Tech Stack

- Single-file HTML/CSS/JS (`index.html`, geen framework, geen build step)
- Alle CSS inline in `<style>`, alle JS inline in `<script>`
- Google Fonts: Luckiest Guy, DM Sans, Caveat, Permanent Marker
- Hosting: GitHub Pages (auto-deploy bij push naar `main`)

## Features

- **Video hero** met neon flicker animatie en scroll-reveal
- **Interactief Rad van Fortuin** - physics-based drag-to-spin (muis + touch), receptkaart resultaat met typewriter effect
- **Foto galerij** - Polaroid-stijl met rotaties, drag-to-scroll strip, handgeschreven bijschriften (Caveat font)
- **Mascotte** - klikbare cartoon dokter (fixed rechtsonder) met random medische quips
- **Medische SVG illustraties** als subtiele achtergrond-decoratie op donkere secties
- **Confetti achtergrond** via vaste afbeelding (canvas variant verwijderd vanwege Chrome flicker)
- **Heartbeat divider** - geanimeerde hartslagmonitor SVG tussen secties
- **Responsive** met mobiel hamburger menu

## Secties

Hero | Over Ons | Rad van Fortuin | Foto's | Info (openingstijden, locatie) | Footer (contact, socials)

## Lokaal ontwikkelen

Geen build step nodig. Open `index.html` in een browser, of start een lokale server:

```bash
python3 -m http.server 8000
# of
npx serve .
```

Debug overlay voor rad-kalibratie: voeg `?debug` toe aan de URL.

## Assets

- `assets/img/` - logo, mascotte, achtergrond, draairad, foto's (9 stuks)
- `assets/video/hero-bg.mp4` - hero achtergrondvideo

## Repo

- GitHub: `Herriaan/de-dokter-website` (public)
- Deploy: automatisch via GitHub Pages bij push naar `main`

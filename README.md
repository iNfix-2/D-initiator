# Nsikan-Abasi Essiet — Personal Portfolio Website

A high-performance, dark-mode portfolio website engineered for **Nsikan-Abasi Essiet** (Senior Full-Stack & Web Developer). Faithfully replicated from the design architecture, typography pairing, micro-interactions, and editorial aesthetics of [cagd.as](https://cagd.as/?ref=darkmodedesign).

---

## 🎨 Design System & Aesthetics

- **Theme**: Pure Deep Black (`#000000`), Dark Gray card surfaces (`#080808`), and subtle micro-borders (`#0e0e0e`).
- **Typography**:
  - **Editorial Headings**: `Lyon Text` (Regular 400 & SemiBold 600) — High-contrast editorial serif.
  - **Body & UI**: `Söhne` (Light 300, Regular 400 & SemiBold 600) — Modernist Swiss grotesque.
  - **Local Fonts**: All font files are stored locally in `assets/fonts/` for instant zero-dependency rendering.
- **Accents**:
  - Role Highlight: Cobalt Blue (`#126ef5`)
  - Live Status Indicator: Pulse Emerald Green (`#22c55e`)
  - Subtle Borders & Hover states: `#1c1c1c` → `#2e2e2e`

---

## 🚀 Features & Architecture

1. **Editorial Hero Section**:
   - Live availability badge: `🟢 Accepting new projects`.
   - Real-time live West Africa Time (`WAT`) clock for Kaduna, Nigeria (UTC+1).
   - High-contrast studio portrait blending seamlessly into pure black with custom radial aura and bottom gradient mask.
2. **Asymmetrical Case Study Grids**:
   - Replicating the multi-image gallery composition of `cagd.as` (`work-img-hero`, `work_images-split-asym`, and `work_images-split-2`).
   - Interactive *"Read the details"* drawer accordion on every project.
3. **Featured Projects**:
   - **DigiNorth Ecosystem Platform** (13-module Northern Nigeria innovation platform)
   - **WorldSeed 3D Interactive Simulation** (Real-time procedural WebGL planet engine)
   - **DigiVolt Smart Electric Mobility** (EV transit dispatch & telematics)
   - **Everything Kaduna** (Regional business discovery directory)
   - **Nethawk Aviation Training Institute** (Aviation academy portal)
   - **Winepress Media & Elegante' Systems** (High-throughput publishing & retail systems)
4. **Endorsements / Testimonials**:
   - Quotes from Engr. Okojere John (CEO, Digi02), Engr. Elijah Danjuma (CEO, Leap Solutions), and Winepress Media leadership.
   - Grayscale executive avatars and custom SVG client logos.
5. **Services & Capabilities (4-Pillar Grid)**:
   - Full-Stack Web Engineering
   - 3D Web & Interactive Experiences
   - Real-Time Systems & IoT Mobility
   - Performance & Architecture Auditing
6. **Career Timeline**:
   - Detailed career history from 2020 to present, including educational background (B.Sc. Computer Science at AFIT).

---

## 📁 Directory Structure

```
/home/ini/Desktop/protfolio2/
├── index.html            # Semantic HTML5, accessibility ARIA, SEO meta
├── styles.css            # cagd.as tokens, layout grids, typography, animations
├── main.js               # WAT clock, smooth scroll, mobile overlay, drawers
├── README.md             # Documentation
└── assets/
    ├── fonts/            # LyonText and Sochne WOFF2 web fonts
    └── images/
        ├── hero/         # Dark mode studio portrait
        ├── logos/        # Partner & client SVG logos
        ├── projects/     # Multi-image case study galleries
        └── testimonials/ # Grayscale avatars for executive references
```

---

## 💻 Local Testing & Development

To test locally:
```bash
python3 -m http.server 8080 --directory /home/ini/Desktop/protfolio2
```
Then open `http://localhost:8080` in any web browser.

---

## 🚢 Deployment

The portfolio is static and zero-dependency, meaning it can be deployed instantly to:
- **GitHub Pages**: Push this directory to your `iNfix-2.github.io` repository.
- **Vercel / Netlify**: Connect the repository or run `npx vercel` / `netlify deploy`.
- **Cloudflare Pages**: Link repo and select static output.

---

## ⚡ Cloudflare Deployment & Live Links

### 1. Live Public Tunnel URL (Active)
Your portfolio is currently connected to the Cloudflare Edge network via a live Quick Tunnel:
- **Public URL**: `https://elliott-search-genealogy-shareware.trycloudflare.com`

### 2. Deploying Permanently to Cloudflare Pages
To deploy to a permanent `.pages.dev` subdomain (or custom domain with free SSL & DDoS protection):

#### Option A: Direct Deploy via Wrangler CLI
```bash
npx wrangler pages deploy /home/ini/Desktop/protfolio2 --project-name=nsikan-portfolio
```

#### Option B: Connect via GitHub
1. Push this repository to GitHub: `https://github.com/iNfix-2/portfolio`
2. Open the [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Select the repository and choose:
   - **Framework preset**: None
   - **Build output directory**: `/`
4. Click **Save and Deploy**. Your site will be live at `https://nsikan-portfolio.pages.dev`.

# Nsikan-Abasi Essiet — Developer Portfolio

A single-page developer portfolio that faithfully follows the visual structure and interaction system of [cagd.as](https://cagd.as/), adapted with Nsikan's own identity, projects, testimonials, contact details and imagery.

## Experience

- Black editorial interface with blue accents
- Lyon Text and Söhne font system
- Portrait-led hero
- Six animated project showcases
- Expandable case-study details
- Testimonial interlude
- Responsive desktop and mobile navigation
- Reduced-motion support
- Search and social metadata

## Development

The page is implemented in `index.html`, `styles.css` and `main.js`. Images and local font files live in `assets/`.

## Build and publish

Run `python3 scripts/build.py` and serve the generated `dist/` directory. For a local preview:

```bash
python3 scripts/build.py
python3 -m http.server 8080 --directory dist
```

On Cloudflare Pages, use `python3 scripts/build.py` as the build command and `dist` as the output directory. Set `SITE_URL` to the preferred public HTTPS address to generate the canonical URL, social preview metadata, sitemap and robots declaration. The build falls back to `CF_PAGES_URL`.

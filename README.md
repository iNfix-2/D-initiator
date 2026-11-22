# Nsikan-Abasi Essiet — Developer Portfolio

A static portfolio with six project case studies and an interactive, seeded terrain generator. The initial landscape and all portfolio content are visible without JavaScript.

## Development

Edit the page templates in `scripts/render.py` and project records in `scripts/projects.json`. Run `python3 scripts/render.py` from the repository root to update the checked-in HTML. The visual system is in `styles.css` and terrain rendering is in `assets/portfolio/terrain.js`.

## Build and publish

Run `python3 scripts/build.py` and serve the resulting `dist/` directory. For a local preview, run `python3 -m http.server 8080 --directory dist`.

On Cloudflare Pages use `python3 scripts/build.py` as the build command and `dist` as the output directory. Set `SITE_URL` to the preferred public HTTPS address to generate absolute canonical links, social preview images and the sitemap. The build uses `CF_PAGES_URL` when no custom origin is set. The static host must serve directory index files for the project URLs under `/work/`.

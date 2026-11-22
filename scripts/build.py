"""Package the exact single-page portfolio for production deployment."""
import os
import shutil
from html import escape
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree.ElementTree import Element, SubElement, ElementTree

root = Path(__file__).resolve().parents[1]
dist = root / "dist"
origin = (os.getenv("SITE_URL") or os.getenv("CF_PAGES_URL") or "").rstrip("/")

if origin:
    parts = urlsplit(origin)
    if parts.scheme not in {"http", "https"} or not parts.netloc or parts.query or parts.fragment:
        raise ValueError("SITE_URL must be an absolute web address")

if dist.exists():
    shutil.rmtree(dist)
dist.mkdir()

for item in ("index.html", "styles.css", "main.js", "_headers"):
    shutil.copy2(root / item, dist / item)

shutil.copytree(root / "assets", dist / "assets")

robots = "User-agent: *\nAllow: /\n"
if origin:
    index = dist / "index.html"
    social_image = origin + "/assets/images/hero/nsikan-hero.jpg"
    metadata = (
        f'<link rel="canonical" href="{escape(origin + "/")}">'
        f'<meta property="og:url" content="{escape(origin + "/")}">'
        f'<meta property="og:image" content="{escape(social_image)}">'
        f'<meta name="twitter:image" content="{escape(social_image)}">'
    )
    index.write_text(
        index.read_text(encoding="utf-8").replace("<!-- deployment-meta -->", metadata),
        encoding="utf-8",
    )

    sitemap = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    SubElement(SubElement(sitemap, "url"), "loc").text = origin + "/"
    ElementTree(sitemap).write(
        dist / "sitemap.xml", encoding="utf-8", xml_declaration=True
    )
    robots += f"Sitemap: {origin}/sitemap.xml\n"

(dist / "robots.txt").write_text(robots, encoding="utf-8")

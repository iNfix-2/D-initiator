"""Package the static portfolio and bind search metadata to its deployment origin."""
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
dist.mkdir(exist_ok=True)
for item in ("index.html", "styles.css", "main.js", "_headers"):
    shutil.copy2(root / item, dist / item)
for directory in ("work", "assets/portfolio"):
    shutil.copytree(root / directory, dist / directory, dirs_exist_ok=True)
fonts = dist / "assets/fonts"
fonts.mkdir(exist_ok=True)
for filename in ("Sochne-400-Regular.woff2", "Sochne-600-SemiBold.woff2", "69db63dc2e8675a7ac6108f9_LyonText-400-Regular-Italic.woff2"):
    shutil.copy2(root / "assets/fonts" / filename, fonts / filename)
sitemap = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
robots = "User-agent: *\nAllow: /\n"
if origin:
    for page in sorted(dist.rglob("index.html")):
        relative = page.parent.relative_to(dist).as_posix()
        url = origin + "/" + (relative + "/" if relative != "." else "")
        image = origin + "/assets/portfolio/" + (page.parent.name + "-home.webp" if relative != "." else "social.jpg")
        metadata = f'<link rel="canonical" href="{escape(url)}"><meta property="og:url" content="{escape(url)}"><meta property="og:image" content="{escape(image)}"><meta name="twitter:image" content="{escape(image)}">'
        page.write_text(page.read_text().replace("<!-- deployment-meta -->", metadata))
        SubElement(SubElement(sitemap, "url"), "loc").text = url
    ElementTree(sitemap).write(dist / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    robots += f"Sitemap: {origin}/sitemap.xml\n"
else:
    (dist / "sitemap.xml").unlink(missing_ok=True)
(dist / "robots.txt").write_text(robots)

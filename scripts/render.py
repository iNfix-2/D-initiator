from pathlib import Path
import json, html
from html import escape as e
projects=json.loads(Path('scripts/projects.json').read_text())
name="Nsikan-Abasi Essiet"
email="mfonessiet0@gmail.com"
gh="https://github.com/iNfix-2"
def head(title,desc,root,schema):
 return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#101210">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:site_name" content="Nsikan Essiet"><meta name="twitter:card" content="summary_large_image"><!-- deployment-meta -->
<link rel="icon" href="{root}assets/portfolio/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}styles.css">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body>'''
def header(root):
 home=root or './'
 return f'''<a href="#main" class="skip">Skip to content</a><header class="site-head wrap"><a class="brand" href="{home}" aria-label="Nsikan Essiet, home"><img src="{root}assets/portfolio/mark.svg" alt="" width="37" height="37">Nsikan Essiet<span class="brand-period">.</span></a><nav aria-label="Main"><a href="{root}#portfolio">Work</a><a href="{root}#about">About</a><a class="contact-nav" href="{root}#contact">Contact</a></nav></header>'''
def footer(root):
 return f'''<footer class="wrap footer"><a class="brand" href="{root or './'}"><img src="{root}assets/portfolio/mark.svg" width="30" height="30" alt="">Nsikan Essiet.</a><div><a href="{gh}">GitHub</a><a href="mailto:{email}">Email</a><a href="tel:+2348082697842">Phone</a></div></footer><script defer src="{root}main.js"></script></body></html>'''
def picture(p,root='',lazy=True):
 return f'''<div class="cover {p['tone']}"><div class="browser-frame"><div class="chrome" aria-hidden="true"><i></i><i></i><i></i></div><img src="{root}assets/portfolio/{p['slug']}-home.webp" width="1140" height="636" alt="{e(p['alt'])}" {'loading="lazy"' if lazy else ''}></div></div>'''
def card(p):
 return f'''<article class="project"><a class="card-link" href="work/{p['slug']}/">{picture(p)}<div class="card-meta mono">{p['type']}</div><h3>{p['name']}</h3><p>{p['summary']}</p></a></article>'''
description="Nsikan-Abasi Essiet is a senior full-stack developer in Kaduna, Nigeria. Explore work in WebGL, electric mobility, education and digital platforms."
person={'@type':'Person','name':name,'alternateName':'Nsikan Essiet','jobTitle':'Senior Full-Stack Developer','sameAs':[gh],'homeLocation':{'@type':'Place','name':'Kaduna, Nigeria'}}
s=head(f'{name} | Full-Stack Developer in Kaduna',description,'',{'@context':'https://schema.org','@type':'ProfilePage','mainEntity':person})+header('')
s+='''<main id="main" class="wrap">
<section class="hero" aria-labelledby="intro">
<div class="intro"><div class="smallcap availability"><span></span>Available for projects</div>
<h1 id="intro">Full-stack<br><em>developer.</em></h1>
<p>I’m Nsikan-Abasi Essiet. I build web platforms, real-time systems and interactive 3D experiences from Kaduna, Nigeria.</p>
<div class="hero-links"><a href="#portfolio" class="button accent">Explore my work</a><a class="inline-link" href="https://github.com/iNfix-2">GitHub</a></div></div>
<figure class="terrain-panel"><div class="panel-head"><span class="mono"><i class="cross" aria-hidden="true"></i>Terrain generator</span><span class="panel-lang mono">Procedural mesh</span></div><div class="plot"><i class="axis axis-y" aria-hidden="true">Y</i><div id="mesh" role="img" aria-label="An isometric green wireframe mountain landscape"><img src="assets/portfolio/terrain.webp" alt="" width="560" height="324"></div><i class="axis axis-x" aria-hidden="true">X</i></div><figcaption><span id="seed" aria-live="polite" class="mono">Seed 2408</span><button id="regenerate" type="button" hidden><span aria-hidden="true">⟳</span> New terrain</button></figcaption></figure></section>
<section id="portfolio" class="work"><div class="section-title"><div><div class="smallcap section-label">Portfolio</div><h2>Selected work<span>.</span></h2></div><span class="count mono">6 projects</span></div>
<div class="project-grid">'''+''.join(card(p) for p in projects)+'''</div></section>
<section id="about" class="about"><div class="portrait"><img src="assets/portfolio/nsikan.webp" alt="Nsikan-Abasi Essiet" width="500" height="500" loading="lazy"></div><div><div class="smallcap section-label">About me</div><h2>Nsikan-Abasi <em>Essiet.</em></h2><p>I’m a full-stack developer based in Kaduna. My work ranges from helping a dispatcher follow an electric fleet to putting a sculptable planet in someone’s browser.</p><p>I like working on both sides of the screen. What a visitor sees depends on decisions about data, rendering and how the system behaves when the connection slows down.</p><div class="location mono">Kaduna, Nigeria <span data-clock>WAT</span></div></div></section>
<section id="testimonials" class="quote"><div class="smallcap section-label">Working together</div><blockquote>“He doesn’t just work through requirements, but also checks them for reasonableness.”</blockquote><p>Engr. Okojere John <span>· Digi02</span></p><details class="more-quotes"><summary>More recommendations</summary><blockquote>“He is thorough, reliable, and possesses a rare combination of frontend finesse and backend rigor.”</blockquote><p>Engr. Elijah Danjuma <span>· Leap Solutions</span></p><blockquote>“Nsikan transformed our publishing and systems infrastructure.”</blockquote><p>Editorial Director <span>· Winepress Media</span></p></details></section>
<section id="contact" class="contact"><div><div class="smallcap section-label">Contact</div><h2>Have a project <em>in mind?</em></h2></div><a class="button accent" href="mailto:mfonessiet0@gmail.com">Email me</a><a class="email" href="mailto:mfonessiet0@gmail.com">mfonessiet0@gmail.com</a></section></main><script defer src="assets/portfolio/terrain.js"></script>'''+footer('')
Path('index.html').write_text(s)
for i,p in enumerate(projects):
 r='../../'; slug=p['slug']; nxt=projects[(i+1)%len(projects)]
 desc=p['name']+' — '+p['summary']+' A development case study by '+name+'.'
 schema={'@context':'https://schema.org','@type':'CreativeWork','name':p['name'],'description':p['summary'],'author':person}
 s=head(p['name']+' | '+name,desc,r,schema)+header(r)+f'''<main id="main" class="wrap case"><div class="crumb"><a href="../../#portfolio">Selected work</a><span>/</span>{p['name']}</div><div class="smallcap section-label">{p['type']}</div><h1>{p['name']}<em>.</em></h1><p class="case-intro">{p['summary']}</p>{picture(p,r,False)}<div class="case-copy"><aside><div class="smallcap">My role</div><p>{p['role']}</p><div class="smallcap">Tools &amp; approach</div><p>{p['tools']}</p>'''
 if slug == 'diginorth': s+='<a class="inline-link" href="https://diginorth.org">Project website</a>'
 if p.get('url'): s+=f'''<a class="inline-link" href="{p['url']}">{p['link']}</a>'''
 s+=f'''</aside><article><h2>The brief</h2><p>{p['brief']}</p><h2>The build</h2><p>{p['build']}</p><p>{p['detail']}</p></article></div><div class="case-gallery"><img loading="lazy" src="{r}assets/portfolio/{slug}-detail1.webp" alt="{p['name']} project detail, first view"><img loading="lazy" src="{r}assets/portfolio/{slug}-detail2.webp" alt="{p['name']} project detail, second view"></div><a class="next-case" href="../{nxt['slug']}/"><div class="smallcap section-label">Next project</div><h2>{nxt['name']}<span>.</span></h2></a></main>'''+footer(r)
 d=Path('work')/slug;d.mkdir(exist_ok=True);(d/'index.html').write_text(s)

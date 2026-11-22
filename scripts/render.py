"""Render the portfolio and its supporting pages as static HTML."""
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
NAME = "Nsikan-Abasi Essiet"
EMAIL = "mfonessiet0@gmail.com"
PHONE = "+2348082697842"
GITHUB = "https://github.com/iNfix-2"
DESCRIPTION = (
    "Nsikan-Abasi Essiet is a senior full-stack developer in Kaduna, Nigeria. "
    "Explore work in WebGL, electric mobility, education and digital platforms."
)
PERSON = {
    "@type": "Person",
    "name": NAME,
    "alternateName": "Nsikan Essiet",
    "jobTitle": "Senior Full-Stack Developer",
    "sameAs": [GITHUB],
    "homeLocation": {"@type": "Place", "name": "Kaduna, Nigeria"},
}

with (ROOT / "scripts/projects.json").open() as source:
    projects = json.load(source)
projects_by_slug = {project["slug"]: project for project in projects}
projects = [
    projects_by_slug[slug]
    for slug in ("diginorth", "worldseed", "digivolt", "everything-kaduna", "nati-aviation", "winepress")
]

NAVIGATION = [
    ("Work", "#portfolio"),
    ("Services", "services/"),
    ("Rates", "rates/"),
    ("Process", "process/"),
    ("Agencies", "agencies/"),
    ("Contact", "contact/"),
]
PROJECT_HEADINGS = {
    "diginorth": "brings Northern Nigeria’s innovation programmes into one platform.",
    "worldseed": "puts a planet you can sculpt straight in the browser.",
    "digivolt": "gives electric fleet operators a live dispatch workspace.",
    "everything-kaduna": "helps people discover businesses across Kaduna.",
    "nati-aviation": "brings course discovery and admissions online.",
    "winepress": "supports digital publishing and connected retail operations.",
}
TESTIMONIALS = [
    ("okojere-john", "Engr. Okojere John", "Digi02",
     "He doesn't just work through requirements, but also checks them for reasonableness. "
     "This makes a collaboration very enjoyable."),
    ("elijah-danjuma", "Engr. Elijah Danjuma", "Leap Solutions",
     "I would describe Nsikan as an exceptional problem-solver and engineer. "
     "He is thorough, reliable, and possesses a rare combination of frontend finesse and backend rigor."),
    ("winepress-director", "Editorial Director", "Winepress Media",
     "Nsikan transformed our publishing and systems infrastructure."),
]

SERVICES = [
    ("Full-stack platforms", "Web applications with clear workflows, reliable data models and access "
     "controls that reflect how your team works."),
    ("Real-time systems", "Operational interfaces for dispatch, fleet telemetry and tasks that depend "
     "on current information."),
    ("Interactive 3D", "Browser-based experiences built with WebGL, including procedural graphics and "
     "interactive tools."),
    ("Performance and architecture", "Review an existing application’s rendering, data flow and "
     "deployment setup to identify what makes it slow or difficult to maintain."),
]


def page(title, description, prefix, body, schema):
    document_title = escape(title)
    description = escape(description)
    home = prefix or "./"
    nav_links = "\n".join(
        f'      <a href="{prefix}{path}">{label}</a>' for label, path in NAVIGATION
    )
    schema = {"@context": "https://schema.org", **schema}
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{document_title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#11100f">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{document_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:site_name" content="Nsikan Essiet">
  <meta name="twitter:card" content="summary_large_image">
  <!-- deployment-meta -->
  <link rel="icon" href="{prefix}assets/portfolio/mark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}styles.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-head wrap">
    <a class="brand" href="{home}" aria-label="Nsikan Essiet, home">Nsikan<span>.</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" hidden>Menu</button>
    <nav id="main-nav" aria-label="Main">
{nav_links}
      <a class="mobile-call" href="{prefix}call/">Schedule a call</a>
    </nav>
    <a class="head-call underlined" href="{prefix}call/">Schedule a call</a>
  </header>
{body}
  <footer class="wrap footer">
    <a class="brand" href="{home}">Nsikan<span>.</span> <small>Full-stack developer</small></a>
    <div class="footer-links">
      <a href="{GITHUB}">GitHub</a>
      <a href="mailto:{EMAIL}">Email</a>
      <a href="tel:{PHONE}">Phone</a>
    </div>
    <p>© 2026 {NAME}</p>
  </footer>
  <script defer src="{prefix}main.js"></script>
</body>
</html>
'''


def image_link(project, variant, description, prefix="", hero=False):
    file = f'{prefix}assets/portfolio/{project["slug"]}-{variant}.webp'
    loading = 'fetchpriority="high"' if hero else 'loading="lazy"'
    return f'''<a class="gallery-image gallery-{variant}" href="{file}" data-gallery>
      <img src="{file}" alt="{escape(description)}" {loading} decoding="async">
    </a>'''


def gallery(project, prefix="", case_page=False):
    name = project["name"]
    images = [
        ("home", project["alt"]),
        ("mobile", f"{name} mobile interface"),
        ("detail1", f"{name} interface detail"),
        ("detail2", f"{name} secondary interface view"),
    ]
    links = "\n    ".join(
        image_link(project, variant, description, prefix, case_page and variant == "home")
        for variant, description in images
    )
    return f'<div class="gallery" role="group" aria-label="{escape(name)} gallery">\n    {links}\n  </div>'


def project_links(project, link_to_case=True):
    links = []
    if project["slug"] == "diginorth":
        links.append('<a class="underlined" href="https://diginorth.org">View the website</a>')
    if project.get("url"):
        url = escape(project["url"])
        links.append(f'<a class="underlined" href="{url}">View the code</a>')
    if link_to_case:
        links.append(f'<a class="underlined" href="work/{project["slug"]}/">Full case study</a>')
    return " ".join(links)


def project_facts(project):
    values = [
        ("Project", project["name"]),
        ("Type", project["type"]),
        ("Role", project["role"]),
        ("Stack", project["tools"]),
    ]
    return "\n".join(f"          <div><dt>{label}</dt><dd>{escape(value)}</dd></div>" for label, value in values)


def work_entry(project):
    slug = project["slug"]
    return f'''<article class="work-entry" id="{slug}" aria-labelledby="{slug}-title">
  <div class="work-copy">
    <h2 id="{slug}-title"><a href="work/{slug}/">{escape(project["name"])}</a> {PROJECT_HEADINGS[slug]}</h2>
    <p class="work-intro">{escape(project["brief"])}</p>
    <div class="text-links">{project_links(project)}</div>
    <details class="project-details" open>
      <summary>Read the details</summary>
      <div class="project-details-body">
        <dl class="facts">
{project_facts(project)}
        </dl>
        <h3>Details</h3>
        <p>{escape(project["build"])}</p>
        <p>{escape(project["detail"])}</p>
      </div>
    </details>
  </div>
  {gallery(project)}
</article>'''


def testimonials():
    cards = []
    for image, name, organisation, words in TESTIMONIALS:
        cards.append(f'''<figure class="testimonial">
          <blockquote>“{escape(words)}”</blockquote>
          <figcaption>
            <img src="assets/images/testimonials/{image}.jpg" width="48" height="48" alt="" loading="lazy">
            <span>{escape(name)}<small>{escape(organisation)}</small></span>
          </figcaption>
        </figure>''')
    return f'''<section id="testimonials" class="testimonials" aria-labelledby="testimonials-title">
      <h2 id="testimonials-title">Selected<br><em>testimonials</em></h2>
      <div class="quote-grid">{"".join(cards)}</div>
    </section>'''


def contact_prompt(prefix):
    return f'''<section class="contact-prompt wrap" aria-labelledby="contact-title">
      <h2 id="contact-title">Have a project in mind?<br><em>Let’s talk through it.</em></h2>
      <div class="text-links">
        <a class="underlined" href="{prefix}call/">Schedule a call</a>
        <span>or</span>
        <a class="underlined" href="{prefix}contact/">Send a message</a>
      </div>
    </section>'''


def gallery_dialog():
    return '''<dialog class="image-dialog" aria-labelledby="image-caption">
      <div class="image-dialog-bar">
        <p id="image-caption"></p>
        <form method="dialog"><button class="underlined" autofocus>Close</button></form>
      </div>
      <img alt="">
    </dialog>'''


def write_page(directory, document):
    folder = ROOT / directory
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(document, encoding="utf-8")


first_group = "\n".join(work_entry(project) for project in projects[:3])
second_group = "\n".join(work_entry(project) for project in projects[3:])
home_body = f'''<main id="main">
  <section class="hero" aria-labelledby="intro">
    <div class="hero-portrait">
      <img src="assets/portfolio/portrait.webp" alt="{NAME}" width="1024" height="1024" fetchpriority="high">
    </div>
    <div class="hero-content wrap">
      <h1 id="intro">I’m Nsikan Essiet.<br>A <em>full‑stack developer.</em></h1>
      <p>I build web platforms, real-time systems and interactive 3D experiences. I work across the interface, the data and the code that ties them together.</p>
      <div class="availability">
        <span class="status"><i aria-hidden="true"></i>Open for projects</span>
        <span>Kaduna, Nigeria <time data-clock>WAT</time></span>
      </div>
      <a class="underlined hero-link" href="#portfolio">View my portfolio</a>
    </div>
  </section>
  <section id="portfolio" class="wrap work" aria-label="Selected work">
    <div class="work-group">
{first_group}
    </div>
    {testimonials()}
    <div class="work-group">
{second_group}
    </div>
  </section>
  {contact_prompt("")}
</main>
{gallery_dialog()}'''
write_page("", page(f"{NAME} | Full-Stack Developer in Kaduna", DESCRIPTION, "", home_body,
                    {"@type": "ProfilePage", "mainEntity": PERSON}))

for index, project in enumerate(projects):
    slug = project["slug"]
    name = escape(project["name"])
    next_project = projects[(index + 1) % len(projects)]
    case_body = f'''<main id="main" class="wrap case">
      <a class="underlined back-link" href="../../#{slug}">Back to selected work</a>
      <article>
        <header class="case-heading">
          <p class="eyebrow">{escape(project["type"])}</p>
          <h1>{name}</h1>
          <p class="lead">{escape(project["summary"])}</p>
        </header>
        <div class="case-grid">
          <div>
            <dl class="facts">{project_facts(project)}</dl>
            <h2>The brief</h2>
            <p>{escape(project["brief"])}</p>
            <h2>The build</h2>
            <p>{escape(project["build"])}</p>
            <p>{escape(project["detail"])}</p>
            <div class="text-links">{project_links(project, link_to_case=False)}</div>
          </div>
          {gallery(project, "../../", case_page=True)}
        </div>
      </article>
      <a class="next-case" href="../{next_project["slug"]}/">
        <span class="eyebrow">Next project</span>
        <span>{escape(next_project["name"])}</span>
      </a>
    </main>
    {gallery_dialog()}'''
    write_page(
        "work/" + slug,
        page(f'{project["name"]} | {NAME}', f'{project["summary"]} A case study by {NAME}.', "../../",
             case_body, {"@type": "CreativeWork", "name": project["name"],
                         "description": project["summary"], "author": PERSON}),
    )


def feature_grid(features):
    return '<div class="feature-grid">' + "".join(
        f'<article><h2>{escape(title)}</h2><p>{escape(description)}</p></article>'
        for title, description in features
    ) + "</div>"


def enquiry(subject, body):
    return f"mailto:{EMAIL}?subject={quote(subject)}&amp;body={quote(body)}"


call_url = enquiry("Schedule a project call", "Hi Nsikan,\n\nI’d like to discuss:\n\nMy preferred times and time zone:\n")
contact_url = enquiry("Portfolio project enquiry", "Hi Nsikan,\n\nHere’s what I’m working on:\n\nTimeline:\n")
secondary_pages = {
    "services": (
        "Full-stack development services",
        "I build web platforms, operational tools and interactive experiences, and help teams improve the applications they already use.",
        feature_grid(SERVICES),
    ),
    "rates": (
        "Project rates",
        "Share what you need built, your timeline and what you already have. Those details make it possible to discuss a realistic estimate.",
        feature_grid([
            ("New builds", "Include the main features, any design files and the systems the application needs to connect to."),
            ("Existing applications", "Describe the problem, where it happens and what a successful change would look like."),
        ]) + '<a class="underlined body-action" href="../contact/">Request an estimate</a>',
    ),
    "process": (
        "How I work",
        "From the first brief to launch, decisions about scope, data and the interface stay visible to the people who will use and maintain the product.",
        feature_grid([
            ("Share the brief", "Identify the users, the workflows that matter and the constraints that shape the build."),
            ("Agree on the scope", "Define what needs to ship and agree on the first pieces to review."),
            ("Review the working build", "Try the main workflows as they take shape and flag anything that needs to change."),
            ("Prepare for launch", "Test the agreed workflows, package the release and document what the team needs to maintain."),
        ]),
    ),
    "agencies": (
        "Development for agencies",
        "I can join your team for a full-stack build, an interactive feature or technical work on an existing project.",
        feature_grid([
            ("From design to implementation", "Share your designs and requirements. I’ll identify what the build needs across the interface, data and integrations."),
            ("Work in your existing stack", "Share the repository, technical constraints and how your team handles review and handoff."),
        ]),
    ),
    "contact": (
        "Tell me about your project",
        "A short brief is enough to start. Include what you’re building, the timeline and any designs or links that are ready to share.",
        f'<div class="text-links"><a class="underlined" href="{contact_url}">Open email draft</a>'
        f'<a class="underlined" href="mailto:{EMAIL}">{EMAIL}</a></div>',
    ),
    "call": (
        "Schedule a call",
        "Send a short note about your project with two times that work for you and your time zone.",
        f'<div class="text-links"><a class="underlined" href="{call_url}">Request a time by email</a>'
        f'<a class="underlined" href="tel:{PHONE}">Call +234 808 269 7842</a></div>',
    ),
}

for slug, (title, description, content) in secondary_pages.items():
    closing = contact_prompt("../") if slug in {"services", "process", "agencies"} else ""
    body = f'''<main id="main">
      <section class="wrap secondary">
        <h1>{title}</h1>
        <p class="lead">{description}</p>
        {content}
      </section>
{closing}
    </main>'''
    write_page(slug, page(f"{title} | {NAME}", description, "../", body,
                          {"@type": "WebPage", "name": title, "author": PERSON}))

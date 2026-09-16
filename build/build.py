# -*- coding: utf-8 -*-
"""Static site generator for aspiro.me.  Run:  python3 build/build.py"""
import os, sys, re, datetime, html as H

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, NAV, STATS, CLIENT_LOGOS, ICONS, SERVICES, CASES, TEAM, INSIGHTS, WHITEPAPERS  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "21"
TODAY = datetime.date.today().isoformat()

PHOTOS = {"hero": (1024, 640), "smartops": (1200, 700)}  # portrait hero; every other photo is 1536x1024 landscape


def photo_dims(name):
    return PHOTOS.get(name, (1536, 900))


SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
CASE_BY_SLUG = {c["slug"]: c for c in CASES}
INSIGHT_BY_SLUG = {i["slug"]: i for i in INSIGHTS}
WP_BY_INSIGHT = {w["insight"]: w for w in WHITEPAPERS}


def picture(name, alt, sizes, cls="", pos=None, loading="lazy", priority=False):
    big, small = photo_dims(name)
    style = f' style="object-position:{pos}"' if pos else ""
    extra = ' fetchpriority="high"' if priority else f' loading="{loading}"'
    h_big = round(big * (1.5 if name == "hero" else 2 / 3))
    return f'''<picture class="{cls}">
  <source type="image/webp" srcset="/public/photos/{name}-{small}.webp {small}w, /public/photos/{name}.webp {big}w" sizes="{sizes}" />
  <img src="/public/photos/{name}.jpg" srcset="/public/photos/{name}-{small}.jpg {small}w, /public/photos/{name}.jpg {big}w" sizes="{sizes}" alt="{H.escape(alt)}" width="{big}" height="{h_big}"{extra}{style} />
</picture>'''


def topic_slug(cat):
    return re.sub(r'[^a-z0-9]+', '-', H.unescape(cat).lower()).strip('-')


def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


# ---------------------------------------------------------------------------
# LAYOUT
# ---------------------------------------------------------------------------
def head(title, desc, path, og_image="/public/og-image.jpg", jsonld="", noindex=False, body_class=""):
    url = SITE["domain"] + ("/" if path == "/index.html" else path)
    robots = '<meta name="robots" content="noindex, follow" />' if noindex else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{H.escape(title)}</title>
  <meta name="description" content="{H.escape(desc)}" />
  <link rel="canonical" href="{url}" />
  {robots}
  <meta name="theme-color" content="#2b0e48" />
  <meta name="color-scheme" content="light" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{SITE['name']}" />
  <meta property="og:title" content="{H.escape(title)}" />
  <meta property="og:description" content="{H.escape(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE['domain']}{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{H.escape(title)}" />
  <meta name="twitter:description" content="{H.escape(desc)}" />
  <meta name="twitter:image" content="{SITE['domain']}{og_image}" />
  <link rel="icon" type="image/png" sizes="64x64" href="/public/favicon.png" />
  <link rel="icon" type="image/png" sizes="512x512" href="/public/icon-512.png" />
  <link rel="apple-touch-icon" href="/public/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
  <link rel="preload" as="image" href="/public/LogoAspiro.png" />
  <link rel="stylesheet" href="/styles.css?v={V}" />
  {jsonld}
</head>
<body class="{body_class}">
  <a class="skip-link" href="#main">Skip to content</a>
'''


def header(active):
    links = "".join(
        f'<a href="{href}"{" class=\"active\"" if label == active else ""}>{label}</a>' for label, href in NAV)
    mlinks = "".join(
        f'<a href="{href}"><span class="menu-num">0{i + 1}</span>{label}</a>' for i, (label, href) in enumerate(NAV))
    mlinks += f'<a href="/contact.html"><span class="menu-num">0{len(NAV) + 1}</span>Contact</a>'
    addr = "<br>".join(SITE["address_lines"])
    return f'''
  <header class="site-header" role="banner" data-header>
    <div class="header-inner">
      <a href="/" class="logo" aria-label="Aspiro home">
        <img class="logo-img" src="/public/LogoAspiro.png" alt="Aspiro" width="464" height="120" />
      </a>
      <nav class="nav-desktop" aria-label="Primary">{links}</nav>
      <div class="header-right">
        <a href="/contact.html" class="btn btn-primary btn-sm header-cta">Talk to us</a>
        <button class="menu-btn" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="menu-overlay"><span></span><span></span></button>
      </div>
    </div>
  </header>
  <div class="menu-overlay" id="menu-overlay" role="dialog" aria-modal="true" aria-label="Navigation menu" hidden>
    <div class="menu-overlay-inner">
      <nav class="menu-primary" aria-label="Mobile navigation">{mlinks}</nav>
      <div class="menu-secondary">
        <a href="mailto:{SITE['email']}">{SITE['email']}</a>
        <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a>
        <p class="menu-address">{addr}</p>
      </div>
    </div>
  </div>
  <main id="main">
'''


def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}.html">{s["name"].replace("&", "&amp;")}</a></li>' for s in SERVICES)
    return f'''
  </main>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner footer-inner--4">
        <div class="footer-brand">
          <a href="/" class="logo" aria-label="Aspiro home"><img class="logo-img" src="/public/LogoAspiro.png" alt="Aspiro" width="464" height="120" /></a>
          <p>Independent management consultancy engineering transformation outcomes for GCC financial services since {SITE['founded']}. Practitioner-led. Investor-free.</p>
          <p class="footer-strap"><em>Leading with clarity.<br>Delivering the difference.</em></p>
        </div>
        <div class="footer-col"><h4>Services</h4><ul>{svc}</ul></div>
        <div class="footer-col"><h4>Company</h4><ul>
          <li><a href="/about.html">About</a></li><li><a href="/approach.html">Our approach</a></li><li><a href="/work.html">Our work</a></li>
          <li><a href="/people.html">Our people</a></li><li><a href="/insights.html">Insights</a></li><li><a href="/contact.html">Contact</a></li></ul></div>
        <div class="footer-col"><h4>Offices</h4><ul>
          <li>Dubai (HQ)</li><li>Riyadh</li><li>London</li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li><li><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></li>
          <li><a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
      </div>
      <div class="footer-bar">
        <p>© <span data-year>{datetime.date.today().year}</span> {SITE['name']}. All rights reserved.</p>
        <div class="footer-bar-links"><a href="/privacy-policy.html">Privacy policy</a><a href="#main">Back to top ↑</a></div>
      </div>
    </div>
  </footer>
  <script src="/main.js?v={V}" defer></script>
</body>
</html>
'''


def page(path, title, desc, active, body, **kw):
    out = head(title, desc, path, **kw) + header(active) + body + footer()
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)
    return path


# ---------------------------------------------------------------------------
# COMPONENTS
# ---------------------------------------------------------------------------
def label(text, light=False):
    return f'<p class="label{" label--teal" if light else ""}">{text}</p>'


def page_hero(eyebrow, title, intro="", photo=None, pos=None, dark=False, crumbs=None):
    cls = "page-hero" + (" page-hero--dark" if dark else "") + (" page-hero--media" if photo else "")
    crumb = ""
    if crumbs:
        items = " ".join(f'<a href="{h}">{t}</a><span aria-hidden="true">/</span>' for t, h in crumbs)
        crumb = f'<nav class="breadcrumb" aria-label="Breadcrumb">{items}<span aria-current="page">{eyebrow}</span></nav>'
    media = f'<figure class="page-hero-media reveal reveal-d1">{picture(photo, "", "(max-width: 900px) 100vw, 44vw", pos=pos, priority=True)}</figure>' if photo else ""
    intro_html = f'<p class="t-lead{" t-lead--light" if dark else ""} reveal reveal-d1">{intro}</p>' if intro else ""
    return f'''
<section class="{cls}">
  <div class="container page-hero-inner">
    <div class="page-hero-copy">
      {crumb}
      {label(eyebrow, dark)}
      <h1 class="t-display{" t-title--light" if dark else ""} reveal">{title}</h1>
      {intro_html}
    </div>
    {media}
  </div>
</section>'''


def cta_band(title="Ready to engineer your <em>next</em> transformation?",
             text="Tell us about the challenge on your desk. A partner will come back to you within one business day."):
    return f'''
<section class="cta-band">
  <div class="container cta-band-inner">
    <div>
      {label("Contact us", True)}
      <h2 class="t-title t-title--light reveal">{title}</h2>
      <p class="t-lead t-lead--light reveal reveal-d1">{text}</p>
    </div>
    <div class="cta-band-actions reveal reveal-d2">
      <a href="/contact.html" class="btn btn-teal btn-lg">Start a conversation</a>
      <a href="mailto:{SITE['email']}" class="cta-band-mail">{SITE['email']}</a>
    </div>
  </div>
</section>'''


def service_card(s, d=""):
    return f'''
<a class="svc-card reveal{d}" href="/services/{s['slug']}.html">
  <span class="svc-card-top"><span class="svc-icon" aria-hidden="true">{ICONS[s['icon']]}</span><span class="svc-num">{s['num']}</span></span>
  <h3>{s['short']}</h3>
  <p>{s['summary']}</p>
  <span class="link-arrow">Explore <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
</a>'''


def case_card(c, d="", link=True):
    tag = "a" if link else "article"
    href = f' href="/work.html#{c["slug"]}"' if link else ""
    return f'''
<{tag} class="case reveal{d}"{href}>
  <p class="case-cat">{c['cat']}</p>
  <p class="case-metric">{c['metric']}</p>
  <p class="case-metric-sub">{c['metric_sub']}</p>
  <h3 class="case-title">{c['title']}</h3>
  <p class="case-body">{c['summary']}</p>
</{tag}>'''


def insight_card(i, d="", featured=False):
    sizes = "(max-width: 900px) 100vw, 60vw" if featured else "(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
    return f'''
<a class="insight-card{' insight-card--featured' if featured else ''} reveal{d}" href="/insights/{i['slug']}.html" data-ins-item data-type="article" data-topic="{topic_slug(i['cat'])}" data-text="{H.escape((i['title'] + ' ' + i['dek']).lower())}">
  <figure class="insight-media">{picture(i['photo'], '', sizes, pos=i['pos'])}</figure>
  <div class="insight-body">
    <p class="insight-meta"><span class="insight-cat">{i['cat']}</span><span>{fmt_date(i['date'])}</span><span>{i['read']} min read</span></p>
    <h3>{i['title']}</h3>
    <p class="insight-dek">{i['dek']}</p>
    <span class="link-arrow">Read <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
  </div>
</a>'''


def wp_card(w, d="", compact=False):
    return f'''
<article class="wp-card{' wp-card--compact' if compact else ''} reveal{d}" id="{w['slug']}" data-ins-item data-type="whitepaper" data-topic="{topic_slug(w['cat'])}" data-text="{H.escape((w['plain'] + ' ' + w['dek'] + ' ' + w['audience']).lower())}">
  <figure class="wp-cover">{picture(w['photo'], '', '(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw', pos=w['pos'])}</figure>
  <div class="wp-body">
    <p class="insight-meta"><span class="insight-cat">{w['cat']}</span><span>{w['series']}</span></p>
    <h3>{w['title']}</h3>
    <p class="wp-audience">{w['audience']}</p>
    <p class="wp-dek">{w['dek']}</p>
    <div class="wp-foot">
      <button type="button" class="btn btn-primary" data-gate data-wp-slug="{w['slug']}" data-wp-title="{H.escape(w['plain'])}" data-wp-file="/public/whitepapers/{w['slug']}.pdf">Download PDF</button>
      <span class="wp-meta">PDF · {w['pages']} pages · {w['size']}</span>
    </div>
  </div>
</article>'''


def wp_slide(w, idx):
    return f'''
<li class="wp-slide" data-ins-item data-type="whitepaper" data-topic="{topic_slug(w['cat'])}" data-text="{H.escape((w['plain'] + ' ' + w['dek'] + ' ' + w['audience']).lower())}" id="{w['slug']}">
  <figure class="wp-slide-cover">{picture(w['photo'], '', '(max-width: 900px) 86vw, 460px', pos=w['pos'], priority=idx < 2)}</figure>
  <div class="wp-slide-body">
    <p class="insight-meta"><span class="insight-cat">{w['cat']}</span><span>{w['series']}</span><span>{w['pages']} pages</span></p>
    <h3>{w['title']}</h3>
    <p class="wp-audience">{w['audience']}</p>
    <p class="wp-dek">{w['dek']}</p>
    <div class="wp-foot">
      <button type="button" class="btn btn-primary" data-gate data-wp-slug="{w['slug']}" data-wp-title="{H.escape(w['plain'])}" data-wp-file="/public/whitepapers/{w['slug']}.pdf">Download PDF</button>
      <span class="wp-meta">PDF · {w['size']}</span>
    </div>
  </div>
</li>'''


GATE_DIALOG = f'''
<dialog class="bio-dialog gate-dialog" id="gate-dialog" aria-labelledby="gate-title">
  <div class="gate-inner">
    <button class="bio-close" type="button" aria-label="Close" data-gate-close><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <p class="label">Download the whitepaper</p>
    <h3 id="gate-title" data-gate-title>Whitepaper</h3>
    <p class="gate-note">Tell us who you are and the PDF will download straight away. We will only use your details to follow up on this paper.</p>
    <form class="gate-form" id="gate-form" novalidate data-endpoint="{SITE['gate_endpoint']}">
      <input type="hidden" name="whitepaper" data-gate-slug />
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true" />
      <div class="form-row">
        <div class="field"><label for="g-name">Name</label><input id="g-name" name="name" type="text" autocomplete="name" required /></div>
        <div class="field"><label for="g-company">Organisation</label><input id="g-company" name="company" type="text" autocomplete="organization" required /></div>
      </div>
      <div class="field"><label for="g-email">Work email</label><input id="g-email" name="email" type="email" autocomplete="email" required /></div>
      <div class="field"><label for="g-role">Role</label><input id="g-role" name="role" type="text" autocomplete="organization-title" /></div>
      <label class="gate-consent"><input type="checkbox" name="consent" required /> <span>I agree to Aspiro contacting me about this paper and related insights, per the <a href="/privacy-policy.html" target="_blank" rel="noopener">privacy policy</a>.</span></label>
      <div class="form-foot"><button type="submit" class="btn btn-primary btn-lg">Get the PDF</button></div>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</dialog>'''


def person_card(first, name, role, bio, d=""):
    return f'''
<article class="person reveal{d}">
  <button class="person-btn" type="button" data-person>
    <span class="person-photo"><picture><source srcset="/public/headshots/{first}.webp" type="image/webp" /><img src="/public/headshots/{first}.png" alt="{name}" loading="lazy" width="560" height="560" /></picture></span>
    <span class="person-name">{name}</span><span class="person-role">{role}</span><span class="person-more">Read bio</span>
  </button>
  <div class="person-bio" hidden><p>{bio}</p></div>
</article>'''


BIO_DIALOG = '''
<dialog class="bio-dialog" id="bio-dialog" aria-labelledby="bio-dialog-name">
  <div class="bio-dialog-inner">
    <button class="bio-close" type="button" aria-label="Close" data-bio-close><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <div class="bio-photo"><img src="" alt="" data-bio-photo width="560" height="560" /></div>
    <div class="bio-text"><p class="person-role" data-bio-role></p><h3 id="bio-dialog-name" data-bio-name></h3><div data-bio-body></div></div>
  </div>
</dialog>'''


def clients_section():
    imgs = "".join(f'<img class="client-logo" src="/public/bank-logos/{f}.webp" alt="{a}" loading="lazy" />' for f, a in CLIENT_LOGOS)
    imgs2 = "".join(f'<img class="client-logo" src="/public/bank-logos/{f}.webp" alt="" loading="lazy" />' for f, a in CLIENT_LOGOS)
    return f'''
<section class="clients" aria-label="Clients">
  <div class="container"><p class="clients-title">Trusted by leading financial institutions across the GCC and beyond</p></div>
  <div class="marquee" aria-hidden="true"><div class="marquee-track"><div class="marquee-group">{imgs}</div><div class="marquee-group" aria-hidden="true">{imgs2}</div></div></div>
</section>'''


def stats_row(cls="hero-stats"):
    return f'<div class="container {cls} reveal reveal-d3" role="list" aria-label="Key facts">' + "".join(
        f'<div class="h-stat" role="listitem"><div class="h-stat-num" data-count="{n.replace(",", "")}">{n}</div><div class="h-stat-label">{l}</div></div>'
        for n, l in STATS) + "</div>"


D = ["", " reveal-d1", " reveal-d2", " reveal-d3"]

# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------
def build_home():
    services = "".join(service_card(s, D[i % 3]) for i, s in enumerate(SERVICES))
    cases = "".join(case_card(CASE_BY_SLUG[k], D[i]) for i, k in enumerate(["saudi-capital-markets", "lean-optimisation", "digital-banking-launch"]))
    insights = "".join(insight_card(i, D[n]) for n, i in enumerate(INSIGHTS[:3]))
    steps = [("01", "Strategy", "The <em>what</em>", "Validating the business case before a single dollar is spent."),
             ("02", "Design", "The <em>how</em>", "Translating strategic intent into detailed operating models."),
             ("03", "Implementation", "The <em>now</em>", "Ensuring strategy survives contact with reality.")]
    steps_html = "".join(f'''<li class="step step--compact reveal{D[i]}"><div class="step-top"><span class="step-label">{lab}</span><span class="step-num">{n}</span></div><h3 class="step-name">{name}</h3><p class="step-quote">{q}</p></li>''' for i, (n, lab, name, q) in enumerate(steps))
    jsonld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"{SITE['name']}","alternateName":"Aspiro","url":"{SITE['domain']}/","logo":"{SITE['domain']}/public/icon-512.png","image":"{SITE['domain']}/public/og-image.jpg","foundingDate":"{SITE['founded']}","description":"Independent, practitioner-led management consultancy engineering transformation outcomes for GCC financial institutions.","email":"{SITE['email']}","telephone":"{SITE['phone_tel']}","address":{{"@type":"PostalAddress","streetAddress":"Office 102-031, Montana Building, Al Karama","addressLocality":"Dubai","addressCountry":"AE"}},"areaServed":["AE","SA","QA","GB"],"sameAs":["{SITE['linkedin']}"]}}</script>'''
    body = f'''
<section class="hero" id="home" aria-label="Introduction">
  <div class="container hero-inner">
    <div class="hero-copy">
      <h1 class="hero-headline reveal">We engineer <span class="word-slot" aria-hidden="true"><span class="word-slot-inner">clarity</span></span><span class="sr-only">clarity</span> for the most ambitious financial institutions.</h1>
      <p class="hero-tagline reveal reveal-d1">Independent. Practitioner-led. Investor-free. We move from strategy to execution fast, so outcomes land sooner rather than later.</p>
      <div class="hero-actions reveal reveal-d2">
        <a href="/contact.html" class="btn btn-primary btn-lg">Start a conversation</a>
        <a href="/work.html" class="btn btn-ghost btn-lg">See our work <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>
    </div>
    <figure class="hero-media reveal reveal-d1">{picture("hero", "Glass office tower at dusk in a Gulf financial district", "(max-width: 900px) 100vw, 42vw", priority=True)}</figure>
  </div>
  {stats_row()}
</section>
{clients_section()}

<section class="about">
  <div class="container">
    <div class="about-grid">
      <div class="about-left">
        {label("Who we are")}
        <h2 class="t-title reveal">We don't just advise.<br>We <em>engineer</em> outcomes.</h2>
        <p class="t-lead reveal reveal-d1">Aspiro is an independent management consultancy, founded in Dubai in {SITE['founded']}, that helps GCC financial institutions transform, grow and thrive.</p>
      </div>
      <div class="about-right">
        <div class="about-body">
          <p class="reveal">We reject the heavy-infrastructure model of the 20th century. We do not maintain passive global hubs. We deploy active practitioner teams wherever you are, coordinated by senior leadership deeply rooted in the GCC.</p>
          <p class="reveal reveal-d1">Born independent, with no external investors, we reject the "land and expand" model of traditional firms. Our advice serves your interests alone. We are practitioners who have sat in your seat.</p>
        </div>
        <a href="/about.html" class="link-arrow reveal reveal-d2">More about Aspiro <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>
    </div>
    <figure class="about-media reveal">{picture("about", "Financial district skyline at blue hour reflected in calm water", "(max-width: 1280px) 100vw, 1280px", pos="center 55%")}</figure>
  </div>
</section>

<section class="services services--home">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("What we do")}<h2 class="t-title">Six practices. One accountable team.</h2></div>
      <p class="section-note">End-to-end capability across the financial services value chain, every practice led by people who have held the roles they advise on.</p>
    </div>
    <div class="svc-cards">{services}</div>
    <p class="section-more reveal"><a href="/services.html" class="btn btn-ghost">All services</a></p>
  </div>
</section>

<section class="approach">
  <div class="section-bg" aria-hidden="true">{picture("approach", "", "100vw")}</div>
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Our approach", True)}<h2 class="t-title t-title--light">We define the path, blueprint the future, and stay to deliver the result.</h2></div>
      <p class="section-note section-note--light">Strategy survives contact with reality because we never leave the room.</p>
    </div>
    <ol class="steps">{steps_html}</ol>
    <p class="section-more reveal"><a href="/approach.html" class="btn btn-teal">How we work</a></p>
  </div>
</section>

<section class="cases">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Our work")}<h2 class="t-title">Outcomes delivered.<br>Results that <em>speak</em>.</h2></div>
      <p class="section-note">A selection of recent engagements across the region's largest banks, capital-markets institutions and insurers.</p>
    </div>
    <div class="cases-grid">{cases}</div>
    <p class="section-more reveal"><a href="/work.html" class="btn btn-ghost">All case studies</a></p>
  </div>
</section>

<section class="smartops">
  <span class="smartops-display" aria-hidden="true">M³</span>
  <div class="container">
    <div class="smartops-grid">
      <div class="smartops-left">
        {label("Smart Ops / MCubed", True)}
        <h2 class="t-title t-title--light reveal">Our proprietary approach to operations <em>excellence</em>.</h2>
        <p class="t-lead t-lead--light reveal reveal-d1">The M³ framework creates a digital twin of your bank's operations, applying Lean first to eliminate waste, then automating. We prevent the costly mistake of digitising the mess.</p>
        <p class="reveal reveal-d2"><a href="/approach.html#smartops" class="btn btn-teal">Explore Smart Ops</a></p>
      </div>
      <div class="smartops-right">
        <figure class="smartops-media reveal">{picture("smartops", "Layered precision-cut glass panels lit in violet and teal", "(max-width: 900px) 100vw, 45vw")}</figure>
        <div class="outcomes">
          <div class="outcome reveal"><p class="outcome-num">$25M</p><p class="outcome-desc">Cost savings realised in a single global bank engagement.</p></div>
          <div class="outcome reveal reveal-d1"><p class="outcome-num">$1.1bn</p><p class="outcome-desc">RWA reduction, releasing $150M of capital.</p></div>
          <div class="outcome reveal reveal-d2"><p class="outcome-num">70%</p><p class="outcome-desc">Reduction in manual processing time.</p></div>
          <div class="outcome reveal reveal-d3"><p class="outcome-num">Weeks</p><p class="outcome-desc">Time to first measurable ROI.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="insights-teaser">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Insights")}<h2 class="t-title">Perspectives from the <em>practitioners</em>.</h2></div>
      <p class="section-note">Points of view on the questions GCC financial services leaders are asking now.</p>
    </div>
    <div class="insights-grid">{insights}</div>
    <p class="section-more reveal"><a href="/insights.html" class="btn btn-ghost">All insights</a></p>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Whitepapers")}<h2 class="t-title">Points of view, in <em>depth</em>.</h2></div>
      <p class="section-note">Six short papers for the executive agenda: execution, automation, disclosure, efficiency, nationalisation and integration.</p>
    </div>
    <div class="wp-grid">{"".join(wp_card(w, D[i], compact=True) for i, w in enumerate(WHITEPAPERS[:3]))}</div>
    <p class="section-more reveal"><a href="/insights.html#whitepapers" class="btn btn-ghost">All whitepapers</a></p>
  </div>
</section>
{GATE_DIALOG}
{cta_band()}
'''
    return page("/index.html", "Aspiro — Management Consultancy for GCC Financial Services",
                "Aspiro is an independent, practitioner-led management consultancy engineering transformation outcomes for the GCC's most ambitious banks and financial institutions.",
                None, body, jsonld=jsonld)


def build_about():
    pillars = [("Independent", "No external investors, no alliance obligations, no referral fees. Our advice serves your interests alone."),
               ("Practitioner-led", "Every engagement is led by people who have run banks, not just advised them. Veterans with 20+ years, augmented by modern data science."),
               ("Outcome-based", "We are measured on results that land on the P&amp;L, the balance sheet and the regulator's desk, not on slides delivered.")]
    pillars_html = "".join(f'<article class="pillar-card reveal{D[i]}"><span class="adv-num">0{i + 1}</span><h3>{t}</h3><p>{p}</p></article>' for i, (t, p) in enumerate(pillars))
    leaders = "".join(person_card(*t[:3], t[4], D[i]) for i, t in enumerate(TEAM[:4]))
    offices = [("Dubai", "Headquarters", "Office 102-031, Montana Building<br>Al Karama, Dubai, UAE"),
               ("Riyadh", "Kingdom of Saudi Arabia", "Serving SAMA-regulated banks, capital-markets institutions and NBFIs across the Kingdom."),
               ("London", "United Kingdom", "Access to global best practice and our international specialist network.")]
    offices_html = "".join(f'<div class="office reveal{D[i]}"><h3>{c}</h3><p class="office-sub">{s}</p><p>{d}</p></div>' for i, (c, s, d) in enumerate(offices))
    body = page_hero("About Aspiro", "Independent by design.<br>Practitioner-led by <em>conviction</em>.",
                     "Founded in Dubai in 2015, Aspiro is a boutique management consultancy built by senior bankers for the financial institutions of the GCC.",
                     photo="about-hero", pos="center") + f'''
<section class="section">
  <div class="container">
    <div class="about-grid">
      <div class="about-left">
        {label("Our story")}
        <h2 class="t-title reveal">Built by people who have <em>sat in your seat</em>.</h2>
      </div>
      <div class="about-right about-body">
        <p class="reveal">Aspiro was founded in {SITE['founded']} by senior financial services executives who had spent their careers running businesses inside the region's largest banks. They had bought a great deal of consulting, and they had a clear view of what was wrong with it: junior teams, generic frameworks, and a commercial model that rewarded the length of the engagement rather than the outcome.</p>
        <p class="reveal reveal-d1">We built the firm we had wanted to hire. Small enough to be led by partners on every engagement. Independent enough to say what is right rather than what is welcome. Connected enough, through an elastic network of more than 8,000 specialists, to bring global best practice to a GCC boardroom without the overhead of a global firm.</p>
        <p class="reveal reveal-d2">A decade on, we have partnered with all of the major banks in the region and delivered more than 24 major transformation programmes. Our headquarters remain in Dubai, with a presence in Riyadh and London.</p>
      </div>
    </div>
    <dl class="facts reveal">
      <div><dt>Founded</dt><dd>{SITE['founded']}</dd></div>
      <div><dt>Headquarters</dt><dd>Dubai</dd></div>
      <div><dt>Offices</dt><dd>Dubai · Riyadh · London</dd></div>
      <div><dt>Ownership</dt><dd>Partner-owned, investor-free</dd></div>
      <div><dt>Network</dt><dd>8,000+ specialists</dd></div>
    </dl>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("What we stand for")}<h2 class="t-title">Three commitments on every engagement.</h2></div>
      <p class="section-note">We tell you what is right, not what you want to hear. Then we stay to deliver it.</p>
    </div>
    <div class="pillar-cards">{pillars_html}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("How we are different")}<h2 class="t-title">The networked model.</h2></div>
      <p class="section-note">A borderless talent ecosystem without the legacy real-estate overhead.</p>
    </div>
    <div class="adv-grid">
      <article class="adv-card reveal"><div class="adv-num">01</div><h3>Practitioner-led wisdom</h3><p>Veterans with 20+ years in banking, not fresh graduates, augmented by AI-driven market insight. The scars of experience combined with the precision of modern data science.</p></article>
      <article class="adv-card reveal reveal-d1"><div class="adv-num">02</div><h3>Asymmetric speed via Smart Ops</h3><p>Agentic AI workflows and our proprietary Smart Ops framework compress the strategy-to-execution cycle. We move from diagnosis to deployment while competitors are still drafting the RFP.</p></article>
      <article class="adv-card reveal reveal-d2"><div class="adv-num">03</div><h3>Global reach, local roots</h3><p>Green finance from London, payments architecture from Singapore, AI governance from Silicon Valley, delivered by a team whose senior leadership has spent decades in the GCC.</p></article>
    </div>
    <div class="partner-note reveal">
      <p><strong>Our technology partner.</strong> Where an engagement requires software build and technology execution, we work with ATS5E, our strategic technology partner, so advisory depth and technical delivery come from one accountable team.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="section-bg" aria-hidden="true">{picture("contact", "", "100vw", pos="center 70%")}</div>
  <div class="container">
    <div class="section-head reveal">{label("Where we are", True)}<h2 class="t-title t-title--light">Based in the GCC. Operating wherever you are.</h2></div>
    <div class="office-grid">{offices_html}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Leadership")}<h2 class="t-title">Senior practitioners.<br>Real <em>accountability</em>.</h2></div>
      <p class="section-note"><a href="/people.html" class="link-arrow">Meet the whole team <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></p>
    </div>
    <div class="team-grid">{leaders}</div>
  </div>
</section>
{BIO_DIALOG}
{cta_band()}
'''
    return page("/about.html", "About Aspiro — Independent GCC Financial Services Consultancy",
                "Founded in Dubai in 2015, Aspiro is an independent, partner-owned management consultancy built by senior bankers for GCC financial institutions.", "About", body)


def build_services():
    rows = "".join(f'''
<a class="svc-row-link reveal{D[i % 3]}" href="/services/{s['slug']}.html">
  <span class="svc-num">{s['num']}</span>
  <span class="svc-row-main"><span class="svc-name">{s['short']}</span><span class="svc-row-summary">{s['summary']}</span>
    <ul class="tags">{"".join(f"<li>{t}</li>" for t in s['tags'])}</ul></span>
  <span class="svc-icon" aria-hidden="true">{ICONS[s['icon']]}</span>
  <span class="svc-toggle svc-toggle--arrow" aria-hidden="true"></span>
</a>''' for i, s in enumerate(SERVICES))
    body = page_hero("What we do", "End-to-end capability, strategy through <em>delivery</em>.",
                     "Six practices spanning the financial services value chain. Every one led by people who have held the roles they advise on, and every one measured on outcomes.",
                     photo="hero", pos="center 60%") + f'''
<section class="section services-index">
  <div class="container"><div class="svc-list svc-list--links">{rows}</div></div>
</section>
<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("How an engagement runs")}<h2 class="t-title">Fast to start. Built for impact.</h2></div>
      <p class="section-note">A fixed-fee diagnostic first, so you see the value before you commit to the programme.</p>
    </div>
    {timeline()}
    <p class="section-more reveal"><a href="/approach.html" class="btn btn-ghost">Our approach in full</a></p>
  </div>
</section>
{cta_band()}
'''
    return page("/services.html", "Services — Aspiro Management Consultants",
                "Transformation, AI and digital, revenue and cost optimisation, risk and ESG, human capital and marketing for GCC financial institutions.", "Services", body)


def timeline():
    phases = [("01", "Diagnostic", "Weeks 1–2", ["Executive interviews and data request", "Process and control walkthroughs", "Baseline and value hypothesis", "Prioritised roadmap and business case"]),
              ("02", "Quick wins", "Weeks 3–6", ["Fixes deployed inside the first month", "Benefits tracked from day one", "Governance and cadence established", "Pods mobilised against value streams"]),
              ("03", "Build &amp; deploy", "Months 2–4", ["Operating model and process redesign", "Automation and platform delivery", "Change and capability building", "Weekly measurable outcomes"]),
              ("04", "Sustain", "Month 4+", ["Benefits banked to the P&amp;L", "Capability handed to your teams", "Gold-standard SOPs and controls", "Light-touch partner oversight"])]
    return '<ol class="timeline">' + "".join(f'''<li class="tl-phase reveal{D[i]}"><span class="tl-num">{n}</span><h3>{name}</h3><p class="tl-period">{period}</p><ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul></li>''' for i, (n, name, period, bullets) in enumerate(phases)) + "</ol>"


def build_service_pages():
    paths = []
    for idx, s in enumerate(SERVICES):
        sections = "".join(f'<h2>{h}</h2><p>{p}</p>' for h, p in s["body"])
        caps = "".join(f"<li>{c}</li>" for c in s["capabilities"])
        outs = "".join(f'<div class="stat reveal{D[i]}"><p class="stat-num">{n}</p><p class="stat-label">{l}</p></div>' for i, (n, l) in enumerate(s["outcomes"]))
        related_cases = "".join(case_card(CASE_BY_SLUG[k], D[i]) for i, k in enumerate(s["cases"]))
        others = "".join(f'<li><a href="/services/{o["slug"]}.html"><span class="svc-num">{o["num"]}</span>{o["name"].replace("&", "&amp;")}</a></li>' for o in SERVICES if o["slug"] != s["slug"])
        body = page_hero(s["name"].replace("&", "&amp;"), s["short"].replace("<br>", " "), s["intro"], photo=s["photo"], pos=s["photo_pos"],
                         crumbs=[("Home", "/"), ("Services", "/services.html")]) + f'''
<section class="section">
  <div class="container svc-detail">
    <div class="prose">{sections}</div>
    <aside class="svc-aside">
      <div class="svc-aside-card reveal">
        <h4>Capabilities</h4>
        <ul class="check-list">{caps}</ul>
      </div>
      <div class="svc-aside-card svc-aside-card--cta reveal reveal-d1">
        <h4>Talk to a partner</h4>
        <p>Every engagement starts with a conversation and a fixed-fee diagnostic.</p>
        <a href="/contact.html" class="btn btn-primary">Start a conversation</a>
      </div>
    </aside>
  </div>
</section>
<section class="stat-band"><div class="container stat-band-inner">{outs}</div></section>
<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Related work")}<h2 class="t-title">Proof, not promises.</h2></div>
      <p class="section-note"><a href="/work.html" class="link-arrow">All case studies <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></p>
    </div>
    <div class="cases-grid cases-grid--2">{related_cases}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    {label("Other practices")}
    <ul class="svc-links">{others}</ul>
  </div>
</section>
{cta_band()}
'''
        paths.append(page(f"/services/{s['slug']}.html", f"{s['name']} — Aspiro", H.unescape(s["summary"]).replace("<br>", " ")[:155], "Services", body))
    return paths


def build_approach():
    steps = [("01", "Strategy", "The <em>what</em>", "Validating the business case before a single dollar is spent.", ["M&amp;A due diligence", "Market entry strategy", "Synergy modelling", "ESG framework design"]),
             ("02", "Design", "The <em>how</em>", "Translating strategic intent into detailed operating models.", ["Target operating model", "Customer journey mapping", "Digital architecture", "HR harmonisation logic"]),
             ("03", "Implementation", "The <em>now</em>", "Ensuring strategy survives contact with reality.", ["PMO execution", "Post-merger integration", "Smart Ops process factory", "Automation deployment"])]
    steps_html = "".join(f'''<li class="step reveal{D[i]}"><div class="step-top"><span class="step-label">{lab}</span><span class="step-num">{n}</span></div><h3 class="step-name">{name}</h3><p class="step-quote">{q}</p><ul class="step-items">{"".join(f"<li>{x}</li>" for x in items)}</ul></li>''' for i, (n, lab, name, q, items) in enumerate(steps))
    start = [("A conversation", "Thirty minutes with a partner on the challenge as you see it. No deck, no proposal, no obligation."),
             ("A fixed-fee diagnostic", "Two weeks inside the business with your data and your people. You receive a baseline, a value hypothesis and a prioritised roadmap you can act on with or without us."),
             ("A mandate on evidence", "If the diagnostic shows value worth pursuing, we agree scope, milestones and a commercial structure linked to the outcome.")]
    start_html = "".join(f'<div class="principle-card reveal{D[i]}"><span class="adv-num">0{i + 1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(start))
    commercial = [("Fixed-fee diagnostic", "A defined price for a defined outcome, so the first decision is a small one."),
                  ("Transparent time and materials", "Where scope must flex, rates and effort are visible weekly, with no surprises at month end."),
                  ("Value-linked milestones", "Where outcomes can be measured, a portion of our fee is tied to them. We are comfortable being paid on results.")]
    commercial_html = "".join(f'<div class="principle-card reveal{D[i]}"><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(commercial))
    csuite = [("CEO", "Chief Executive Officer", "Growth strategy, legacy consolidation and M&amp;A execution at scale.", "<strong>M&amp;A integration and strategy execution.</strong> Led the integration of the Kingdom's largest lenders. Delivered a Vision 2027 strategy. Established the target operating model as the single source of truth, giving the CEO and Board full visibility of execution and risk."),
              ("COO / CIO", "Operations &amp; Technology", "Operational efficiency, digitalisation at scale and platform scalability.", "<strong>Digital transformation and Smart Ops.</strong> Implemented omnichannel banking with cloud-native architecture, WhatsApp banking and instant onboarding. Reduced manual processing by 70% through automation."),
              ("CRO", "Chief Risk Officer", "Regulatory compliance, operational resilience and risk governance frameworks.", "<strong>Operational resilience and risk governance.</strong> Basel III compliance. Third-party risk protocols. AML/KYC remediation across the GCC. 70% reduction in ESG processing time with full IFRS S1/S2 compliance."),
              ("CFO", "Chief Financial Officer", "Profitability improvement, cost control and synergy realisation.", "<strong>Cost optimisation and synergy tracking.</strong> $25M cost savings. SAR 4.75M annual HR synergies with a 6 to 12 month payback. $1.1bn RWA reduction releasing $150M of capital.")]
    csuite_html = "".join(f'''<div class="csuite-row reveal{D[i]}"><div class="csuite-role"><span class="csuite-role-title">{r}</span><span class="csuite-role-sub">{sub}</span></div><div class="csuite-col"><p class="csuite-col-label">Your challenge</p><p class="csuite-pain">{pain}</p></div><div class="csuite-col"><p class="csuite-col-label">How we help</p><p class="csuite-solution">{sol}</p></div></div>''' for i, (r, sub, pain, sol) in enumerate(csuite))
    pillars = [("The M³ framework", "A structured enterprise process management tool capturing flows, controls and risks, creating a living digital twin of your operations."),
               ("Lean, then automation", "Lean principles eliminate waste first, then we digitise. Every automation dollar delivers real ROI rather than encoding inefficiency at scale."),
               ("Pod-based delivery", "Cross-functional pods of process engineers, developers and change agents run rapid transformation sprints with measurable weekly outcomes."),
               ("Granular diagnostics", "Proprietary tooling identifies value-destructive activity at the process level, ensuring ROI on every transformation dollar and gold-standard SOPs for compliance.")]
    pillars_html = "".join(f'<div class="pillar reveal{D[i]}"><span class="pillar-n">0{i + 1}</span><div><h3>{t}</h3><p>{p}</p></div></div>' for i, (t, p) in enumerate(pillars))
    body = page_hero("Our approach", "We define the path, blueprint the future, and stay to deliver the <em>result</em>.",
                     "Strategy survives contact with reality because we never leave the room. Here is how an Aspiro engagement works, from the first conversation to benefits banked.",
                     photo="approach", pos="center") + f'''
<section class="section section--dark">
  <div class="section-bg" aria-hidden="true">{picture("approach", "", "100vw")}</div>
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Three phases", True)}<h2 class="t-title t-title--light">Strategy. Design. Implementation.</h2></div>
      <p class="section-note section-note--light">One team from the business case to the benefits ledger, so nothing is lost in the hand-off.</p>
    </div>
    <ol class="steps">{steps_html}</ol>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("How we start")}<h2 class="t-title">Earning the mandate before <em>commitment</em>.</h2></div>
      <p class="section-note">The first decision you take with us is a small one. The diagnostic pays for itself whether or not the programme follows.</p>
    </div>
    <div class="principle-cards">{start_html}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Engagement model")}<h2 class="t-title">Fast to start. Built for impact.</h2></div>
      <p class="section-note">Quick wins inside the first month, benefits tracked weekly, capability handed over at the end.</p>
    </div>
    {timeline()}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Commercial principles")}<h2 class="t-title">Transparent. Outcome-linked. No surprises.</h2></div>
      <p class="section-note">We present the structure up front and are comfortable being paid on results.</p>
    </div>
    <div class="principle-cards">{commercial_html}</div>
  </div>
</section>

<section class="smartops" id="smartops">
  <span class="smartops-display" aria-hidden="true">M³</span>
  <div class="container">
    <div class="smartops-grid">
      <div class="smartops-left">
        {label("Smart Ops / MCubed", True)}
        <h2 class="t-title t-title--light reveal">Our proprietary approach to operations <em>excellence</em>.</h2>
        <p class="t-lead t-lead--light reveal reveal-d1">The M³ framework creates a digital twin of your bank's operations, applying Lean first to eliminate waste, then automating. We prevent the costly mistake of digitising the mess.</p>
        <div class="pillars">{pillars_html}</div>
      </div>
      <div class="smartops-right">
        <figure class="smartops-media reveal">{picture("smartops", "Layered precision-cut glass panels lit in violet and teal", "(max-width: 900px) 100vw, 45vw")}</figure>
        <div class="outcomes">
          <div class="outcome reveal"><p class="outcome-num">$25M</p><p class="outcome-desc">Cost savings realised through efficiency gains and waste reduction in a single global bank engagement.</p></div>
          <div class="outcome reveal reveal-d1"><p class="outcome-num">$1.1bn</p><p class="outcome-desc">RWA reduction from redesigned credit processes, releasing $150M of capital.</p></div>
          <div class="outcome reveal reveal-d2"><p class="outcome-num">70%</p><p class="outcome-desc">Reduction in manual processing time through automation and intelligent workflow redesign.</p></div>
          <div class="outcome reveal reveal-d3"><p class="outcome-num">Weeks</p><p class="outcome-desc">Speed to value. ROI realised within weeks through quick-fix deployment.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="solutions">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Tailored for the C-suite")}<h2 class="t-title">Every engagement begins with your most pressing challenge.</h2></div>
      <p class="section-note">We map our capabilities directly to the executive agenda, delivering outcomes rather than activity.</p>
    </div>
    <div class="csuite-rows">{csuite_html}</div>
  </div>
</section>
{cta_band()}
'''
    return page("/approach.html", "Our Approach — How Aspiro Works",
                "Strategy, design and implementation by one team. A fixed-fee diagnostic, quick wins inside the first month, and the Smart Ops M³ framework.", "Approach", body)


def build_work():
    cards = "".join(case_card(c, D[i % 3]) for i, c in enumerate(CASES))
    details = "".join(f'''
<article class="case-detail reveal" id="{c['slug']}">
  <div class="case-detail-head">
    <p class="case-cat">{c['cat']}</p>
    <p class="case-metric">{c['metric']}</p>
    <p class="case-metric-sub">{c['metric_sub']}</p>
  </div>
  <div class="case-detail-body">
    <h3>{c['title']}</h3>
    <p class="case-client">{c['client']}</p>
    <div class="case-detail-cols">
      <div><h4>The challenge</h4><p>{c['challenge']}</p></div>
      <div><h4>What we did</h4><p>{c['did']}</p></div>
      <div><h4>The outcome</h4><p>{c['outcome']}</p></div>
    </div>
    <p class="case-services">Practices: {" · ".join(f'<a href="/services/{k}.html">{SERVICE_BY_SLUG[k]["name"].replace("&", "&amp;")}</a>' for k in c['services'])}</p>
  </div>
</article>''' for c in CASES)
    body = page_hero("Our work", "Outcomes delivered.<br>Results that <em>speak</em>.",
                     "A selection of engagements across the region's largest banks, capital-markets institutions and insurers. Client names are withheld; the numbers are real.",
                     photo="work-hero", pos="center") + f'''
<section class="section"><div class="container"><div class="cases-grid">{cards}</div></div></section>
<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">{label("In detail")}<h2 class="t-title">Challenge, approach, outcome.</h2></div>
    <div class="case-details">{details}</div>
  </div>
</section>
{cta_band()}
'''
    return page("/work.html", "Our Work — Case Studies — Aspiro",
                "Case studies from Aspiro engagements: digital banking launch, $25M Lean savings, Saudi capital-markets execution, zero-disruption integration, automated ESG reporting.", "Work", body)


def build_people():
    leaders = "".join(person_card(*t[:3], t[4], D[i % 4]) for i, t in enumerate(TEAM) if t[3] == "leadership")
    principals = "".join(person_card(*t[:3], t[4], D[i % 4]) for i, t in enumerate(TEAM) if t[3] == "principals")
    body = page_hero("Our people", "Senior practitioners.<br>Real <em>accountability</em>.",
                     "Every Aspiro engagement is led by people who have run banks, not just advised them. Select a profile to read more.") + f'''
<section class="section team">
  <div class="container">
    <h2 class="team-group-title reveal">Leadership</h2>
    <div class="team-grid">{leaders}</div>
    <h2 class="team-group-title reveal">Principals &amp; Associates</h2>
    <div class="team-grid team-grid--compact">{principals}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container about-grid">
    <div>{label("The network")}<h2 class="t-title reveal">8,000+ specialists, <em>one</em> standard.</h2></div>
    <div class="about-body"><p class="reveal">Behind the partners and principals sits an elastic associate network of more than 8,000 subject-matter experts across the world's financial centres. Every associate is selected for the engagement, led by an Aspiro partner and held to the same standard of accountability. You get the depth of a global firm and the attention of a boutique.</p></div>
  </div>
</section>
{BIO_DIALOG}
{cta_band("Work with people who have <em>sat in your seat</em>.", "Tell us about the challenge on your desk. A partner will come back to you within one business day.")}
'''
    return page("/people.html", "Our People — Aspiro Management Consultants",
                "Meet the partners and principals of Aspiro: senior practitioners from the GCC's largest banks and the world's leading consultancies.", "People", body)


def build_insights_index():
    topics = {}
    for w in WHITEPAPERS:
        topics.setdefault(topic_slug(w["cat"]), [w["cat"], 0])[1] += 1
    for i in INSIGHTS:
        topics.setdefault(topic_slug(i["cat"]), [i["cat"], 0])[1] += 1
    topic_opts = "".join(f'<option value="{k}">{v[0]}</option>' for k, v in sorted(topics.items(), key=lambda kv: H.unescape(kv[1][0])))
    slides = "".join(wp_slide(w, i) for i, w in enumerate(WHITEPAPERS))
    cards = "".join(insight_card(i, D[n % 3]) for n, i in enumerate(INSIGHTS))
    total = len(WHITEPAPERS) + len(INSIGHTS)
    body = page_hero("Insights", "Perspectives from the <em>practitioners</em>.",
                     f"{len(WHITEPAPERS)} whitepapers and {len(INSIGHTS)} articles on the questions GCC financial services leaders are asking now: execution, automation, regulation, cost and growth. Written by people who have done the work.") + f'''
<div class="ins-toolbar" data-ins-toolbar>
  <div class="container ins-toolbar-inner">
    <div class="ins-types" role="group" aria-label="Type">
      <button type="button" data-type="all" aria-pressed="true">All</button>
      <button type="button" data-type="whitepaper" aria-pressed="false">Whitepapers</button>
      <button type="button" data-type="article" aria-pressed="false">Articles</button>
    </div>
    <div class="ins-controls">
      <label class="ins-select">
        <select aria-label="Topic" data-ins-topic>
          <option value="all">All topics</option>{topic_opts}
        </select>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
      </label>
      <label class="ins-search">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input type="search" placeholder="Search" aria-label="Search insights" data-ins-search />
      </label>
    </div>
  </div>
  <div class="container ins-summary" aria-live="polite" data-ins-summary hidden><span data-ins-count>{total}</span> results<button type="button" class="ins-clear" data-ins-clear>Clear filters</button></div>
</div>

<section class="section ins-section" id="whitepapers" data-ins-section="whitepaper">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Whitepapers")}<h2 class="t-title">Points of view, in <em>depth</em>.</h2></div>
      <p class="section-note">Short papers with an argument, the evidence, a framework and four moves for Monday. Free to download.</p>
    </div>
  </div>
  <div class="wp-rail-wrap">
    <button type="button" class="rail-btn rail-btn--prev" data-rail-prev aria-label="Previous whitepaper"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></button>
    <ul class="wp-rail" data-rail tabindex="0" aria-label="Whitepapers">{slides}</ul>
    <button type="button" class="rail-btn rail-btn--next" data-rail-next aria-label="Next whitepaper"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
  </div>
  <div class="container"><div class="rail-dots" data-rail-dots aria-hidden="true"></div></div>
</section>

<section class="section section--tint ins-section" id="articles" data-ins-section="article">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Articles")}<h2 class="t-title">Shorter reads from the <em>practice</em>.</h2></div>
      <p class="section-note">Five to eight minutes each. Every one ends with what to do on Monday.</p>
    </div>
    <div class="insights-grid insights-grid--index">{cards}</div>
  </div>
</section>
<div class="container"><p class="ins-empty" data-ins-empty hidden>Nothing matches those filters. <button type="button" class="link-arrow" data-ins-clear>Clear filters</button></p></div>
{GATE_DIALOG}
{cta_band("Want a point of view on <em>your</em> agenda?", "A conversation with a partner costs nothing and usually saves a quarter.")}
'''
    return page("/insights.html", "Insights — Aspiro Management Consultants",
                "Practitioner perspectives and downloadable whitepapers on transformation, AI and automation, risk and ESG, cost and growth for GCC financial institutions.", "Insights", body)


def build_insight_pages():
    paths = []
    for n, i in enumerate(INSIGHTS):
        # insert pull quote after the second paragraph
        parts = i["body"].strip().split("</p>")
        if len(parts) > 2:
            parts.insert(2, f'<blockquote class="pullquote"><p>{i["quote"]}</p></blockquote>')
        body_html = "</p>".join(parts)
        related = "".join(insight_card(INSIGHT_BY_SLUG[r], D[k]) for k, r in enumerate(i["related"]) if r in INSIGHT_BY_SLUG)
        prev_i = INSIGHTS[n - 1] if n > 0 else None
        next_i = INSIGHTS[n + 1] if n + 1 < len(INSIGHTS) else None
        nav = '<nav class="article-nav" aria-label="More insights">'
        nav += f'<a class="article-nav-link" href="/insights/{prev_i["slug"]}.html"><span>Newer</span>{prev_i["title"]}</a>' if prev_i else "<span></span>"
        nav += f'<a class="article-nav-link article-nav-link--next" href="/insights/{next_i["slug"]}.html"><span>Older</span>{next_i["title"]}</a>' if next_i else "<span></span>"
        nav += "</nav>"
        url = f"{SITE['domain']}/insights/{i['slug']}.html"
        wp = WP_BY_INSIGHT.get(i["slug"])
        wp_aside = f'''<div class="aside-card aside-card--wp"><h4>Whitepaper</h4><p class="aside-wp-title">{wp['title']}</p><p>{wp['audience']}. {wp['pages']} pages.</p><button type="button" class="btn btn-primary btn-sm" data-gate data-wp-slug="{wp['slug']}" data-wp-title="{H.escape(wp['plain'])}" data-wp-file="/public/whitepapers/{wp['slug']}.pdf">Download PDF</button></div>''' if wp else ""
        share = f'''<div class="share"><h4>Share</h4>
          <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener">LinkedIn</a>
          <a href="mailto:?subject={H.escape(i['title'])}&amp;body={url}">Email</a>
          <button type="button" data-copy="{url}">Copy link</button></div>'''
        jsonld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{H.escape(i['title']).__repr__().replace("'", '"')},"datePublished":"{i['date']}","dateModified":"{i['date']}","author":{{"@type":"Organization","name":"{SITE['name']}"}},"publisher":{{"@type":"Organization","name":"{SITE['name']}","logo":{{"@type":"ImageObject","url":"{SITE['domain']}/public/icon-512.png"}}}},"image":"{SITE['domain']}/public/photos/{i['photo']}.jpg","mainEntityOfPage":"{url}"}}</script>'''
        body = f'''
<div class="read-progress" aria-hidden="true"><span data-read-progress></span></div>
<article class="article">
  <header class="article-head">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/insights.html">Insights</a><span aria-hidden="true">/</span><span aria-current="page">{i['cat']}</span></nav>
      <p class="insight-meta reveal"><span class="insight-cat">{i['cat']}</span><span>{fmt_date(i['date'])}</span><span>{i['read']} min read</span></p>
      <h1 class="t-display reveal reveal-d1">{i['title']}</h1>
      <p class="t-lead article-dek reveal reveal-d2">{i['dek']}</p>
    </div>
  </header>
  <div class="container"><figure class="article-hero reveal">{picture(i['photo'], '', '(max-width: 1280px) 100vw, 1280px', pos=i['pos'], priority=True)}</figure></div>
  <div class="container article-layout">
    <div class="article-body prose">{body_html}
      <p class="article-byline">By {SITE['name']}. Aspiro is an independent, practitioner-led consultancy for GCC financial institutions.</p>
    </div>
    <aside class="article-aside">
      {wp_aside}
      {share}
      <div class="aside-card"><h4>Talk to a partner</h4><p>If this is on your agenda, a thirty-minute conversation is the fastest way to test it.</p><a href="/contact.html" class="btn btn-primary btn-sm">Get in touch</a></div>
    </aside>
  </div>
  <div class="container">{nav}</div>
</article>
<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>{label("Related insights")}<h2 class="t-title">Keep reading.</h2></div>
      <p class="section-note"><a href="/insights.html" class="link-arrow">All insights <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></p>
    </div>
    <div class="insights-grid insights-grid--2">{related}</div>
  </div>
</section>
{GATE_DIALOG if wp else ""}
{cta_band()}
'''
        paths.append(page(f"/insights/{i['slug']}.html", f"{i['title']} — Aspiro Insights", i["dek"][:155], "Insights", body,
                          og_image=f"/public/photos/{i['photo']}.jpg", jsonld=jsonld))
    return paths


def build_whitepapers():
    cards = "".join(wp_card(w, D[i % 2]) for i, w in enumerate(WHITEPAPERS))
    body = page_hero("Whitepapers", "Points of view, in <em>depth</em>.",
                     "Six short papers on the questions GCC financial services leaders are asking now. Each one states an argument, shows the evidence, sets out a framework and closes with four moves you can make on Monday.") + f'''
<section class="section">
  <div class="container"><div class="wp-grid wp-grid--index">{cards}</div></div>
</section>
{GATE_DIALOG}
{cta_band("Want a point of view on <em>your</em> agenda?", "A conversation with a partner costs nothing and usually saves a quarter.")}
'''
    return page("/whitepapers.html", "Whitepapers — Aspiro Management Consultants",
                "Download Aspiro points of view on execution, automation, IFRS S1/S2 disclosure, cost-to-income, Saudization and post-merger integration.", "Whitepapers", body)


def build_contact():
    opts = "".join(f'<option value="{s["name"]}">{s["name"].replace("&", "&amp;")}</option>' for s in SERVICES) + '<option value="Something else">Something else</option>'
    addr = "<br>".join(SITE["address_lines"])
    body = f'''
<section class="contact contact--page">
  <div class="section-bg section-bg--contact" aria-hidden="true">{picture("contact", "", "100vw", priority=True)}</div>
  <div class="container">
    <div class="contact-grid">
      <div class="contact-left">
        {label("Contact us", True)}
        <h1 class="t-display t-title--light reveal">Ready to engineer your <em>next</em> transformation?</h1>
        <p class="t-lead t-lead--light reveal reveal-d1">Tell us about the challenge on your desk. A partner will come back to you within one business day.</p>
        <dl class="contact-details reveal reveal-d2">
          <div><dt>Email</dt><dd><a href="mailto:{SITE['email']}">{SITE['email']}</a></dd></div>
          <div><dt>Phone</dt><dd><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></dd></div>
          <div><dt>Head office</dt><dd>{addr}</dd></div>
          <div><dt>Also in</dt><dd>Riyadh · London</dd></div>
        </dl>
      </div>
      <form class="contact-form reveal reveal-d1" id="contact-form" novalidate data-endpoint="{SITE['form_endpoint']}">
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true" />
        <div class="form-row">
          <div class="field"><label for="cf-name">Name</label><input id="cf-name" name="name" type="text" autocomplete="name" required /></div>
          <div class="field"><label for="cf-company">Organisation</label><input id="cf-company" name="company" type="text" autocomplete="organization" /></div>
        </div>
        <div class="field"><label for="cf-email">Work email</label><input id="cf-email" name="email" type="email" autocomplete="email" required /></div>
        <div class="field"><label for="cf-topic">What can we help with?</label><select id="cf-topic" name="topic">{opts}</select></div>
        <div class="field"><label for="cf-message">Message</label><textarea id="cf-message" name="message" rows="5" required></textarea></div>
        <div class="form-foot"><button type="submit" class="btn btn-teal btn-lg">Send message</button><p class="form-note">By sending, you agree to our <a href="/privacy-policy.html">privacy policy</a>.</p></div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal">{label("Offices")}<h2 class="t-title">Dubai. Riyadh. London.</h2></div>
    <div class="office-grid office-grid--light">
      <div class="office reveal"><h3>Dubai</h3><p class="office-sub">Headquarters</p><p>{addr}</p><p><a class="link-arrow" href="https://maps.google.com/?q=Montana+Building,+Al+Karama,+Dubai" target="_blank" rel="noopener">Open in maps</a></p></div>
      <div class="office reveal reveal-d1"><h3>Riyadh</h3><p class="office-sub">Kingdom of Saudi Arabia</p><p>Serving SAMA-regulated banks, capital-markets institutions and NBFIs across the Kingdom.</p></div>
      <div class="office reveal reveal-d2"><h3>London</h3><p class="office-sub">United Kingdom</p><p>Access to global best practice and our international specialist network.</p></div>
    </div>
  </div>
</section>
'''
    return page("/contact.html", "Contact Aspiro — Dubai, Riyadh, London",
                "Talk to an Aspiro partner about your transformation, automation, risk, cost or growth agenda. Offices in Dubai, Riyadh and London.", None, body, body_class="header-on-dark")


def build_privacy():
    sections = [("Information we collect", "We may collect information you provide directly, including your name, email address, phone number, organisation and any message content submitted through our contact channels. We may also collect limited technical data such as IP address, browser type and device information through standard analytics or server logs."),
                ("How we use information", "We use personal information to respond to enquiries, deliver and improve our services, maintain website performance and security, comply with legal obligations, and communicate relevant business updates where permitted."),
                ("Legal basis", "Where applicable, we process personal information on the basis of legitimate interests, contractual necessity, consent or legal obligation."),
                ("Sharing and disclosure", "We do not sell personal information. We may share data with trusted service providers (for hosting, analytics and operations) and where required by law, regulation or a competent authority."),
                ("Data retention", "We retain personal information only for as long as necessary for the purposes outlined in this policy, including legal, regulatory and business requirements."),
                ("Your rights", "Depending on your jurisdiction, you may have rights to access, correct, delete, restrict or object to the processing of your personal information, and to request portability of your data."),
                ("Cookies and tracking", "This website may use cookies and similar technologies for essential functionality, analytics and performance. You can manage cookies through your browser settings."),
                ("International transfers", "Where information is transferred across borders, we apply reasonable safeguards and controls to protect personal information in accordance with applicable law."),
                ("Security", "We implement reasonable technical and organisational measures to protect personal data from unauthorised access, alteration, disclosure or destruction."),
                ("Contact", f'For privacy requests or questions, contact us at <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.')]
    body = f'''
<section class="legal">
  <div class="container"><div class="legal-inner">
    {label("Legal")}
    <h1 class="t-title">Privacy policy</h1>
    <p class="legal-updated">Last updated 20 February 2026</p>
    <p>This privacy policy explains how {SITE['name']} ("Aspiro", "we", "our", "us") collects, uses, discloses and protects personal information when you visit this website or contact us.</p>
    {"".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in sections)}
  </div></div>
</section>'''
    return page("/privacy-policy.html", "Privacy Policy — Aspiro Management Consultants",
                "How Aspiro Management Consultants collects, uses and protects personal information.", None, body, noindex=True)


def build_404():
    body = '''
<section class="nf"><div>
  <p class="nf-code">4<em>0</em>4</p>
  <p class="nf-text">The page you're looking for has moved or never existed. Let's get you back on track.</p>
  <a href="/" class="btn btn-primary btn-lg">Back to home</a>
</div></section>'''
    return page("/404.html", "Page not found — Aspiro", "Page not found.", None, body, noindex=True)


def build_sitemap(paths):
    urls = []
    for p in paths:
        if p.endswith("404.html"):
            continue
        loc = SITE["domain"] + ("/" if p == "/index.html" else p)
        pri = "1.0" if p == "/index.html" else ("0.2" if "privacy" in p else "0.7")
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pri}</priority></url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")


if __name__ == "__main__":
    paths = [build_home(), build_about(), build_services(), *build_service_pages(), build_approach(), build_work(),
             build_people(), build_insights_index(), *build_insight_pages(), build_contact(), build_privacy(), build_404()]
    build_sitemap(paths)
    print(f"built {len(paths)} pages")
    for p in paths:
        print("  ", p)

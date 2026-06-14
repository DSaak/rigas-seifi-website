#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static-site generator for Rīgas Seifi.

Reads content.py and writes a fully SEO-optimised, multi-page, trilingual
site into dist/:  dist/<lang>/<slug>.html  + sitemap.xml + robots.txt.

Run:  python3 build.py
"""
import os, shutil, html, json, datetime
import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "docs")
ASSETS_SRC = os.path.join(ROOT, "assets")
S = C.SITE


def esc(t):
    return html.escape(str(t), quote=True)


# ---------- URL helpers (relative links between generated files) ----------
def page_file(page):
    return f"{C.SLUGS[page]}.html"

def link(page):                     # same-language link (pages share a folder)
    return "index.html" if page == "index" else page_file(page)

def link_lang(lang, page):          # cross-language link
    return f"../{lang}/{link(page)}"

def canonical(lang, page):
    if page == "index":
        return f"{S['domain']}/{lang}/"
    return f"{S['domain']}/{lang}/{page_file(page)}"

ASSET = "../assets"


# ---------- small inline icon set ----------
ICONS = {
    "shield": '<path d="M12 2 4 5.5v5.1c0 5 3.4 9.6 8 10.9 4.6-1.3 8-5.9 8-10.9V5.5L12 2z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m8.7 12 2.3 2.3 4.3-4.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="15.5" r="1.7" fill="currentColor"/>',
    "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    "box": '<path d="M3 8 12 3l9 5v8l-9 5-9-5V8z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M3 8l9 5 9-5M12 13v8" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    "deal": '<path d="M5 12 9 8l4 3 6-6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 5h5v5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 19h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    "truck": '<rect x="2" y="7" width="11" height="9" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13 10h4l4 4v2h-8z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="7" cy="18" r="1.8" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="17" cy="18" r="1.8" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    "room": '<rect x="3" y="4" width="18" height="14" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3 9h18M8 18v2M16 18v2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS.get(name, ICONS["box"])}</svg>'

WA_SVG = '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.8-4.6-4-.1-.2-1.1-1.4-1.1-2.7 0-1.3.7-1.9.9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.4l.9 2.1c.1.2.1.4 0 .6l-.4.6-.5.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.2 1.4 2.5 1.5.3.1.5.1.7-.1l1-1.2c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.4.1 0 .1.6-.1 1.3Z"/></svg>'
LOGO_SVG = '<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" stroke-width="2.5"/><circle cx="20" cy="20" r="9" fill="none" stroke="currentColor" stroke-width="2"/><line x1="20" y1="3" x2="20" y2="11" stroke="currentColor" stroke-width="2.5"/><line x1="20" y1="29" x2="20" y2="37" stroke="currentColor" stroke-width="2.5"/><line x1="3" y1="20" x2="11" y2="20" stroke="currentColor" stroke-width="2.5"/><line x1="29" y1="20" x2="37" y2="20" stroke="currentColor" stroke-width="2.5"/></svg>'
WA_HREF = lambda lang: f"https://wa.me/{S['wa_number']}?text={html.escape(__import__('urllib.parse', fromlist=['quote']).quote(C.UI[lang]['wa_msg']), quote=True)}"


def wa_href(lang):
    import urllib.parse
    return f"https://wa.me/{S['wa_number']}?text=" + urllib.parse.quote(C.UI[lang]["wa_msg"])

def maps_dir():
    return f"https://www.google.com/maps/dir/?api=1&destination={S['maps_q']}"


# =====================================================================
#  Shared chrome
# =====================================================================
def head(lang, page):
    u = C.UI[lang]
    title, desc, kw = C.META[lang][page]
    alts = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{esc(canonical(l, page))}">'
        for l in C.LANGS
    )
    alts += f'<link rel="alternate" hreflang="x-default" href="{esc(canonical(C.DEFAULT_LANG, page))}">'
    og_img = f"{S['domain']}/assets/og-image.jpg"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{esc(kw)}">
<link rel="canonical" href="{esc(canonical(lang, page))}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(S['brand'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical(lang, page))}">
<meta property="og:locale" content="{ {'lv':'lv_LV','ru':'ru_RU','en':'en_GB'}[lang] }">
<meta property="og:image" content="{esc(og_img)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e1116">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ASSET}/styles.css">
{schema_blocks(lang, page)}
</head>
<body>
"""


def schema_blocks(lang, page):
    business = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": S["brand"],
        "description": C.META[lang][page][1],
        "url": canonical(lang, page),
        "telephone": S["phone1_href"],
        "email": S["email"],
        "image": f"{S['domain']}/assets/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "Ģertrūdes iela 33/35",
                    "addressLocality": "Rīga", "postalCode": "LV-1011", "addressCountry": "LV"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "10:00", "closes": "19:00"},
        "priceRange": "€30–€150 / month",
        "foundingDate": "2017",
        "sameAs": [S["facebook"]],
    }
    blocks = [json.dumps(business, ensure_ascii=False)]

    if page == "faq":
        faq = {"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": a}}
                              for q, a in C.FAQ[lang]]}
        blocks.append(json.dumps(faq, ensure_ascii=False))

    if page == "boxes":
        items = []
        for i, b in enumerate(C.BOX_DATA, 1):
            items.append({"@type": "Product", "name": f"{S['brand']} — {C.UI[lang]['f_size']} Nr. {b['nr']}",
                          "description": C.FITS[lang][b["nr"]],
                          "offers": {"@type": "Offer", "price": b["m12"].replace("€", "").replace(",", "."),
                                     "priceCurrency": "EUR", "availability": "https://schema.org/InStock"}})
        ilist = {"@context": "https://schema.org", "@type": "ItemList",
                 "itemListElement": [{"@type": "ListItem", "position": i, "item": it} for i, it in enumerate(items, 1)]}
        blocks.append(json.dumps(ilist, ensure_ascii=False))

    if page not in ("index",):
        crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
                  "itemListElement": [
                      {"@type": "ListItem", "position": 1, "name": C.UI[lang]["breadcrumb_home"], "item": canonical(lang, "index")},
                      {"@type": "ListItem", "position": 2, "name": C.UI[lang]["nav"].get(page, C.META[lang][page][0]), "item": canonical(lang, page)},
                  ]}
        blocks.append(json.dumps(crumbs, ensure_ascii=False))

    return "\n".join(f'<script type="application/ld+json">{b}</script>' for b in blocks)


def _active(cond):
    return ' class="active"' if cond else ''

def header(lang, current):
    u = C.UI[lang]
    nav_links = "".join(
        f'<a href="{link(p)}"{_active(p == current)}>{esc(u["nav"][p])}</a>'
        for p in C.NAV
    )
    langs = "".join(
        f'<a href="{link_lang(l, current)}" hreflang="{l}"{_active(l == lang)}>{l.upper()}</a>'
        for l in C.LANGS
    )
    return f"""<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="logo" href="{link('index')}" aria-label="{esc(S['brand'])}">{LOGO_SVG}<span class="logo-text">RĪGAS&nbsp;SEIFI</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="{esc(u['menu'])}" aria-expanded="false" aria-controls="mobileNav">
      <span></span><span></span><span></span>
    </button>
    <nav class="header-nav" aria-label="Main">{nav_links}</nav>
    <div class="header-actions">
      <a class="phone-icon" href="tel:{S['phone1_href']}" aria-label="{esc(S['phone1'])}"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" d="M5 4h3.5l1.5 4-2 1.5a12 12 0 0 0 6.5 6.5L16 14l4 1.5V19a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg></a>
      <a class="header-phone" href="tel:{S['phone1_href']}">{esc(S['phone1'])}</a>
      <div class="lang-switch" role="group" aria-label="Language">{langs}</div>
      <a class="btn btn-gold btn-sm" href="#book">{esc(u['book'])}</a>
    </div>
  </div>
  <nav class="mobile-nav" id="mobileNav" aria-label="Mobile">
    {"".join(f'<a href="{link(p)}">{esc(u["nav"][p])}</a>' for p in C.NAV)}
    <div class="mobile-lang lang-switch" role="group" aria-label="Language">{langs}</div>
    <a class="btn btn-gold btn-full" href="#book">{esc(u['book'])}</a>
  </nav>
</header>
<main>
"""


def footer(lang):
    u = C.UI[lang]
    nav = "".join(f'<li><a href="{link(p)}">{esc(u["nav"][p])}</a></li>' for p in C.NAV)
    year = datetime.date.today().year
    return f"""</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="logo" href="{link('index')}" aria-label="{esc(S['brand'])}">{LOGO_SVG}<span class="logo-text">RĪGAS&nbsp;SEIFI</span></a>
      <p>{esc(u['footer_tagline'])}</p>
    </div>
    <div class="footer-col">
      <h4>{esc(u['footer_nav'])}</h4><ul>{nav}</ul>
    </div>
    <div class="footer-col">
      <h4>{esc(u['footer_contact'])}</h4>
      <ul>
        <li>{esc(S['address'])}</li>
        <li><a href="tel:{S['phone1_href']}">{esc(S['phone1'])}</a></li>
        <li><a href="mailto:{S['email']}">{esc(S['email'])}</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>{esc(u['footer_hours'])}</h4>
      <ul><li>{esc(u['hours_week'])}</li><li>{esc(u['hours_after'])}</li></ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© {year} {esc(S['brand'])}. {esc(u['ft_rights'])}</p>
    <nav aria-label="Legal"><a href="#">{esc(u['ft_privacy'])}</a><a href="#">{esc(u['ft_cookies'])}</a></nav>
  </div>
</footer>
<a class="wa-fab" href="{esc(wa_href(lang))}" target="_blank" rel="noopener" aria-label="WhatsApp" data-track="whatsapp_click">{WA_SVG}</a>
<div class="cookie-banner" id="cookieBanner" hidden>
  <p>{esc(u['cookie_text'])}</p>
  <div class="cookie-actions">
    <button class="btn btn-gold btn-sm" id="cookieAccept">{esc(u['cookie_accept'])}</button>
    <button class="btn btn-ghost btn-sm" id="cookieDecline">{esc(u['cookie_decline'])}</button>
  </div>
</div>
<script src="{ASSET}/app.js"></script>
</body>
</html>"""


# =====================================================================
#  Reusable sections
# =====================================================================
def breadcrumb(lang, page):
    u = C.UI[lang]
    return f"""<nav class="breadcrumb container" aria-label="Breadcrumb">
  <a href="{link('index')}">{esc(u['breadcrumb_home'])}</a><span>/</span><span>{esc(u['nav'].get(page, C.META[lang][page][0].split('—')[0].strip()))}</span>
</nav>"""

def page_hero(lang, title, sub=""):
    sub_html = f'<p class="page-hero-sub">{esc(sub)}</p>' if sub else ""
    return f"""<section class="page-hero"><div class="container"><h1>{esc(title)}</h1>{sub_html}</div></section>"""

def advantages(lang):
    icons = ["shield", "lock", "clock"]
    cards = "".join(
        f'<article class="adv reveal"><div class="adv-icon">{icon(icons[i])}</div><h3>{esc(t)}</h3><p>{esc(p)}</p></article>'
        for i, (t, p) in enumerate(C.ADV[lang]))
    return f'<section class="advantages section"><div class="container"><h2 class="center">{esc(C.H[lang]["adv"])}</h2><div class="adv-grid">{cards}</div></div></section>'

def steps(lang):
    items = "".join(
        f'<li class="reveal"><span class="step-num">{i+1}</span><h3>{esc(t)}</h3><p>{esc(p)}</p></li>'
        for i, (t, p) in enumerate(C.STEPS[lang]))
    return f'<section class="how section"><div class="container"><h2 class="center">{esc(C.H[lang]["how"])}</h2><ol class="steps">{items}</ol></div></section>'

def size_cards(lang, heading=True):
    u = C.UI[lang]
    heights = {"1": 6, "2": 10, "3": 18, "4": 26, "5": 42}
    cards = []
    for b in C.BOX_DATA:
        pop = b.get("popular")
        badge = f'<span class="pop-badge">{esc(u["popular"])}</span>' if pop else ""
        btn = "btn-gold" if pop else "btn-outline"
        cards.append(f"""<article class="size-card{' popular' if pop else ''} reveal">{badge}
  <div class="size-visual"><div class="size-slot" style="--h:{heights[b['nr']]}px"></div></div>
  <h3>Nr. {b['nr']}</h3><p class="dims">{esc(b['dim'])}</p>
  <p class="fits">{esc(C.FITS[lang][b['nr']])}</p>
  <p class="price">{esc(u['from'])} <strong>{esc(b['m12'])}</strong>{esc(u['permonth'])}</p>
  <a class="btn {btn} btn-sm" href="#book" data-size="Nr.{b['nr']}">{esc(u['cta_book'])}</a></article>""")
    head_html = (f'<h2 class="center">{esc(C.H[lang]["sizes"])}</h2>'
                 f'<p class="section-sub center">{esc(C.H[lang]["sizes_sub"])}</p>') if heading else ""
    return f"""<section class="sizes section section-alt" id="sizes"><div class="container">
  {head_html}
  <div class="size-grid">{''.join(cards)}</div>
  <p class="price-note">{esc(C.H[lang]['price_note'])}</p></div></section>"""

def size_table(lang):
    h = C.H[lang]
    rows = "".join(
        f"<tr><td><strong>Nr. {b['nr']}</strong></td><td>{esc(b['dim'])}</td><td>{esc(C.FITS[lang][b['nr']])}</td><td>{esc(b['m1'])}</td><td><strong>{esc(b['m12'])}</strong></td><td>{esc(b['m24'])}</td></tr>"
        for b in C.BOX_DATA)
    return f"""<section class="section"><div class="container">
  <div class="table-wrap"><table class="price-table">
    <thead><tr><th>{esc(h['table_size'])}</th><th>{esc(h['table_dim'])}</th><th>{esc(h['table_fits'])}</th><th>{esc(h['table_m1'])}</th><th>{esc(h['table_m12'])}</th><th>{esc(h['table_m24'])}</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <p class="price-note">{esc(h['price_note'])}</p></div></section>"""

def security_block(lang, full=False):
    pts = C.SECPOINTS[lang]
    items = "".join(f'<li class="reveal">{esc(p)}</li>' for p in pts)
    photo = f"""<div class="security-photo reveal"><div class="photo-placeholder">
      <svg viewBox="0 0 24 24" width="44" height="44"><rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.4"/><circle cx="9" cy="9" r="2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="m3 17 5-5 4 4 3-3 6 6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
      <p>{ {'lv':'Šeit: reāls glabātavas foto — bez stoka attēliem.','ru':'Здесь: реальное фото хранилища — без стоковых изображений.','en':'A real vault photo goes here — no stock images.'}[lang] }</p></div></div>"""
    return f"""<section class="security section{'' if full else ' section-alt'}"><div class="container security-inner">
  <div class="security-text"><h2>{esc(C.H[lang]['security'])}</h2><ul class="sec-list">{items}</ul></div>
  {photo}</div></section>"""

def trust_block(lang):
    cards = "".join(f'<div class="trust-fact reveal"><strong>{esc(t)}</strong><p>{esc(p)}</p></div>' for t, p in C.TRUST[lang])
    note = {'lv':'Šeit tiks ievietotas reālas Google atsauksmes.','ru':'Здесь будут реальные отзывы из Google.','en':'Real Google reviews will be embedded here.'}[lang]
    return f"""<section class="trust section"><div class="container"><h2 class="center">{esc(C.H[lang]['trust'])}</h2>
  <div class="trust-grid">{cards}</div>
  <div class="reviews-placeholder reveal"><p>{esc(note)}</p></div></div></section>"""

def location_block(lang, heading=True):
    u = C.UI[lang]
    h = f'<h2 class="center">{esc(C.H[lang]["location"])}</h2>' if heading else ""
    return f"""<section class="location section section-alt" id="location"><div class="container">{h}
  <div class="location-inner">
    <div class="location-info">
      <address>
        <p class="loc-line"><strong>{esc(S['address'])}</strong></p>
        <p class="loc-line">{esc(u['hours_week'])}</p>
        <p class="loc-line">{esc(u['hours_after'])}</p>
        <p class="loc-line"><a href="tel:{S['phone1_href']}" data-track="phone_click">{esc(S['phone1'])}</a> · <a href="tel:{S['phone2_href']}" data-track="phone_click">{esc(S['phone2'])}</a></p>
        <p class="loc-line"><a href="mailto:{S['email']}">{esc(S['email'])}</a></p>
      </address>
      <a class="btn btn-outline" target="_blank" rel="noopener" href="{maps_dir()}">{esc(u['cta_route'])}</a>
    </div>
    <div class="location-map reveal"><iframe title="Map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={S['maps_q']}&output=embed"></iframe></div>
  </div></div></section>"""

def faq_accordion(lang, limit=None):
    items = C.FAQ[lang][:limit] if limit else C.FAQ[lang]
    rows = "".join(f'<details class="reveal"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in items)
    more = ""
    if limit:
        more = f'<p class="center" style="margin-top:1.4rem"><a class="btn btn-outline" href="{link("faq")}">{esc(C.UI[lang]["cta_more"])}</a></p>'
    return f'<section class="faq section" id="faq"><div class="container faq-container"><h2 class="center">{esc(C.H[lang]["faq"])}</h2><div class="faq-list">{rows}</div>{more}</div></section>'

def booking_form(lang):
    u = C.UI[lang]
    chips = "".join(f'<button type="button" class="chip chip-num" data-size="{n}" aria-pressed="false">{n}</button>' for n in "12345")
    chips += f'<button type="button" class="chip" data-size="?" aria-pressed="false">{esc(u["f_unsure"])}</button>'
    return f"""<form class="book-form" id="bookForm" novalidate>
  <h3>{esc(u['form_title'])}</h3>
  <label><span class="lbl"><span>{esc(u['f_name'])}</span></span><input type="text" name="name" required autocomplete="name"></label>
  <label><span class="lbl"><span>{esc(u['f_phone'])}</span></span><input type="tel" name="phone" required autocomplete="tel" inputmode="tel" placeholder="{esc(u['ph_phone'])}"></label>
  <label><span class="lbl"><span>{esc(u['f_email'])}</span> <em class="opt">{esc(u['opt'])}</em></span><input type="email" name="email" autocomplete="email" inputmode="email" placeholder="{esc(u['ph_email'])}"></label>
  <fieldset class="size-chips">
    <legend class="lbl"><span>{esc(u['f_size'])}</span> <em class="opt">{esc(u['opt'])}</em></legend>
    <div class="chips" id="sizeChips">{chips}</div>
    <div class="qty-list" id="qtyList"></div>
    <input type="hidden" name="sizes" id="sizesField">
  </fieldset>
  <div class="form-row">
    <label><span class="lbl"><span>{esc(u['f_date'])}</span> <em class="opt">{esc(u['opt'])}</em></span><input type="date" name="start"></label>
    <label><span class="lbl"><span>{esc(u['f_comment'])}</span> <em class="opt">{esc(u['opt'])}</em></span><input type="text" name="comment" placeholder="{esc(u['ph_comment'])}"></label>
  </div>
  <button type="submit" class="btn btn-gold btn-full">{esc(u['f_submit'])}</button>
  <p class="form-privacy">{esc(u['f_privacy'])}</p>
  <div class="form-success" id="formSuccess" hidden>
    <svg viewBox="0 0 24 24" width="44" height="44" aria-hidden="true"><circle cx="12" cy="12" r="10.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <strong>{esc(u['f_ok_t'])}</strong><p>{esc(u['f_ok_p'])}</p>
  </div>
</form>"""

def book_section(lang):
    u = C.UI[lang]
    return f"""<section class="book section section-dark" id="book"><div class="container book-inner">
  <div class="book-pitch">
    <h2>{esc(C.H[lang]['book'])}</h2>
    <p>{esc(C.H[lang]['book_sub'])}</p>
    <a class="btn btn-whatsapp" target="_blank" rel="noopener" href="{esc(wa_href(lang))}" data-track="whatsapp_click">{WA_SVG}<span>{esc(u['cta_wa'])}</span></a>
    <p class="book-phone">{esc(u['or_call'])} <a href="tel:{S['phone1_href']}" data-track="phone_click">{esc(S['phone1'])}</a></p>
  </div>
  {booking_form(lang)}
</div></section>"""


# =====================================================================
#  Page bodies
# =====================================================================
def hero(lang):
    he = C.HERO[lang]
    u = C.UI[lang]
    stats = "".join(f'<li><strong>{esc(v)}</strong><span>{esc(l)}</span></li>' for v, l in he["stats"])
    return f"""<section class="hero">
  <div class="hero-bg" aria-hidden="true"><div class="vault-illustration"><svg viewBox="0 0 400 400" aria-hidden="true">
    <circle cx="200" cy="200" r="190" fill="none" stroke="rgba(201,164,92,.25)" stroke-width="2"/>
    <circle cx="200" cy="200" r="150" fill="none" stroke="rgba(201,164,92,.45)" stroke-width="10"/>
    <circle cx="200" cy="200" r="110" fill="none" stroke="rgba(201,164,92,.30)" stroke-width="3"/>
    <circle cx="200" cy="200" r="46" fill="none" stroke="rgba(201,164,92,.6)" stroke-width="6"/>
    <g stroke="rgba(201,164,92,.55)" stroke-width="6" stroke-linecap="round">
      <line x1="200" y1="118" x2="200" y2="154"/><line x1="200" y1="246" x2="200" y2="282"/>
      <line x1="118" y1="200" x2="154" y2="200"/><line x1="246" y1="200" x2="282" y2="200"/>
      <line x1="143" y1="143" x2="168" y2="168"/><line x1="232" y1="232" x2="257" y2="257"/>
      <line x1="257" y1="143" x2="232" y2="168"/><line x1="168" y1="232" x2="143" y2="257"/></g></svg></div></div>
  <div class="container hero-inner">
    <p class="hero-eyebrow">{esc(he['eyebrow'])}</p>
    <h1>{esc(he['title'])}</h1>
    <p class="hero-sub">{esc(he['sub'])}</p>
    <div class="hero-ctas"><a class="btn btn-gold" href="#book">{esc(u['cta_book'])}</a><a class="btn btn-ghost" href="{link('boxes')}">{esc(u['cta_prices'])}</a></div>
    <ul class="hero-stats">{stats}</ul>
  </div></section>"""

def body_index(lang):
    return hero(lang) + advantages(lang) + size_cards(lang) + steps(lang) + security_block(lang) + trust_block(lang) + location_block(lang) + faq_accordion(lang, limit=5) + book_section(lang)

def body_boxes(lang):
    title, desc, _ = C.META[lang]["boxes"]
    return breadcrumb(lang, "boxes") + page_hero(lang, C.H[lang]["sizes"], C.H[lang]["sizes_sub"]) + size_cards(lang, heading=False) + size_table(lang) + book_section(lang)

def body_security(lang):
    sub = {'lv':'Bankas līmeņa drošība bez bankas.','ru':'Защита банковского уровня без банка.','en':'Bank-grade security, without the bank.'}[lang]
    return breadcrumb(lang, "security") + page_hero(lang, C.H[lang]["security"], sub) + security_block(lang, full=True) + trust_block(lang) + book_section(lang)

def body_how(lang):
    x = C.HOWX[lang]
    cols = ""
    for t_key, l_key in [("need_t", "need"), ("pay_t", "pay"), ("access_t", "access")]:
        lis = "".join(f"<li>{esc(i)}</li>" for i in x[l_key])
        cols += f'<div class="info-card reveal"><h3>{esc(x[t_key])}</h3><ul class="check-list">{lis}</ul></div>'
    sub = {'lv':'No izvēles līdz drošai glabāšanai — trijos soļos.','ru':'От выбора до надёжного хранения — за три шага.','en':'From choice to safe storage — in three steps.'}[lang]
    extra = f'<section class="section section-alt"><div class="container"><div class="info-grid">{cols}</div></div></section>'
    return breadcrumb(lang, "how") + page_hero(lang, C.H[lang]["how"], sub) + steps(lang) + extra + book_section(lang)

def body_services(lang):
    cards = "".join(
        f'<article class="service-card reveal"><div class="adv-icon">{icon(ic)}</div><h3>{esc(t)}</h3><p>{esc(b)}</p></article>'
        for ic, t, b in C.SERVICES[lang])
    sub = {'lv':'Vairāk nekā seifu noma.','ru':'Больше, чем аренда сейфа.','en':'More than safe deposit rental.'}[lang]
    grid = f'<section class="section"><div class="container"><div class="service-grid">{cards}</div></div></section>'
    return breadcrumb(lang, "services") + page_hero(lang, C.H[lang]["services"], sub) + grid + book_section(lang)

def body_about(lang):
    a = C.ABOUT[lang]
    paras = "".join(f"<p>{esc(p)}</p>" for p in a["paras"])
    facts = "".join(f'<div class="trust-fact reveal"><strong>{esc(v)}</strong><p>{esc(l)}</p></div>' for v, l in a["facts"])
    sub = a["lead"]
    content_sec = f"""<section class="section"><div class="container narrow">{paras}</div></section>
<section class="section section-alt"><div class="container"><div class="trust-grid">{facts}</div></div></section>"""
    return breadcrumb(lang, "about") + page_hero(lang, C.UI[lang]["nav"]["about"], sub) + content_sec + security_block(lang) + book_section(lang)

def body_faq(lang):
    sub = {'lv':'Viss, kas jāzina pirms seifa nomas.','ru':'Всё, что нужно знать перед арендой сейфа.','en':'Everything to know before renting a box.'}[lang]
    return breadcrumb(lang, "faq") + page_hero(lang, C.H[lang]["faq"], sub) + faq_accordion(lang) + book_section(lang)

def body_contacts(lang):
    sub = {'lv':'Sazinieties ar mums vai rezervējiet seifu tiešsaistē.','ru':'Свяжитесь с нами или забронируйте сейф онлайн.','en':'Get in touch or book your box online.'}[lang]
    return breadcrumb(lang, "contacts") + page_hero(lang, C.UI[lang]["nav"]["contacts"], sub) + book_section(lang) + location_block(lang, heading=True)

def body_blog(lang):
    bl = C.BLOG[lang]
    cards = "".join(
        f'<article class="blog-card reveal"><span class="blog-soon">{esc(bl["soon"])}</span><h3>{esc(t)}</h3></article>'
        for t in bl["posts"])
    sub = bl["intro"]
    grid = f'<section class="section"><div class="container"><div class="blog-grid">{cards}</div></div></section>'
    return breadcrumb(lang, "blog") + page_hero(lang, C.UI[lang]["nav"].get("blog", "Blog"), sub) + grid + book_section(lang)

BODY = {"index": body_index, "boxes": body_boxes, "security": body_security, "how": body_how,
        "services": body_services, "about": body_about, "faq": body_faq, "contacts": body_contacts, "blog": body_blog}


# =====================================================================
#  Build
# =====================================================================
def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    # assets
    shutil.copytree(ASSETS_SRC, os.path.join(DIST, "assets"))

    for lang in C.LANGS:
        d = os.path.join(DIST, lang)
        os.makedirs(d, exist_ok=True)
        for page in C.PAGES:
            html_out = head(lang, page) + header(lang, page) + BODY[page](lang) + footer(lang)
            fname = "index.html" if page == "index" else page_file(page)
            with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
                f.write(html_out)

    # root language redirect (x-default)
    root = f"""<!DOCTYPE html><html lang="{C.DEFAULT_LANG}"><head><meta charset="UTF-8">
<title>{esc(S['brand'])}</title>
<link rel="canonical" href="{S['domain']}/{C.DEFAULT_LANG}/">
{''.join(f'<link rel="alternate" hreflang="{l}" href="{S["domain"]}/{l}/">' for l in C.LANGS)}
<link rel="alternate" hreflang="x-default" href="{S['domain']}/{C.DEFAULT_LANG}/">
<script>
var l=(localStorage.getItem('lang')||navigator.language||'lv').slice(0,2).toLowerCase();
if(['lv','ru','en'].indexOf(l)<0)l='{C.DEFAULT_LANG}';
location.replace(l+'/index.html');
</script>
<meta http-equiv="refresh" content="0; url={C.DEFAULT_LANG}/index.html"></head>
<body><p>Rīgas Seifi — <a href="lv/index.html">Latviešu</a> · <a href="ru/index.html">Русский</a> · <a href="en/index.html">English</a></p></body></html>"""
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(root)

    # robots.txt
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {S['domain']}/sitemap.xml\n")

    # sitemap.xml with hreflang alternates
    today = datetime.date.today().isoformat()
    urls = []
    for lang in C.LANGS:
        for page in C.PAGES:
            loc = canonical(lang, page)
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{canonical(l, page)}"/>'
                for l in C.LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{canonical(C.DEFAULT_LANG, page)}"/>'
            pr = "1.0" if page == "index" else "0.8"
            urls.append(f"<url><loc>{loc}</loc>{alts}<lastmod>{today}</lastmod><priority>{pr}</priority></url>")
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>"""
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    n = len(C.LANGS) * len(C.PAGES)
    print(f"Built {n} pages + root + sitemap.xml + robots.txt into {DIST}")


if __name__ == "__main__":
    build()

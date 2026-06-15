# Rīgas Seifi — website

Static, trilingual (LV / RU / EN), SEO-optimised, multi-page site generated
from content + templates. No build tools beyond Python 3.

## Structure
```
content.py     All copy (LV/RU/EN), prices, SEO meta, FAQ — edit text here.
build.py       Generator: templates + logic. Run it to (re)build the site.
assets/        styles.css, app.js, images (shared, copied into docs/).
docs/          GENERATED output — do not edit by hand. This is what you deploy.
snapshot.sh    Save a version snapshot (keeps the last 15).
```

## Build
```
python3 build.py
```
Generates `docs/` with:
- `docs/<lang>/<page>.html` for lv, ru, en (9 pages each = 27 pages)
- `docs/index.html` root that redirects to the visitor's language
- `sitemap.xml`, `robots.txt`

## Pages
index, boxes, security, how-it-works, services, about, faq, contacts, blog.

## SEO built in
Unique title/description/keywords per page per language, canonical + hreflang
(incl. x-default), Open Graph + Twitter cards, JSON-LD schema
(LocalBusiness everywhere, FAQPage on FAQ, Product list on boxes,
BreadcrumbList on inner pages), sitemap with hreflang alternates, robots.txt.

## Advert ribbon (bright top bar)
Controlled by the `PROMO` block at the top of `content.py`:
- `"active": True / False` — turn the bar on or off everywhere.
- `"lv"/"ru"/"en"` — the text per language.
- `"link"` — where clicking it goes (default `#book`).
Visitors can dismiss it with ×; it reappears automatically whenever you change
the text. Rebuild/publish after editing.

## Versioning
Run `sh snapshot.sh "label"` after a round of changes. Snapshots live in
`../Rigas Seifi Website - versions/` and the script auto-prunes to the
15 most recent. `docs/` and caches are excluded from snapshots (regenerable).

## Still TODO before launch
- Real photos (replace placeholders; shot list in the original TZ §6.2).
- Wire the booking form to a real endpoint (email + Telegram/WhatsApp) and a
  `/thank-you` page for GA4 conversion tracking. Hook noted in app.js.
- Real Google reviews embed (placeholder on home/security).
- Privacy & cookie policy page content; connect GA4/GTM + Meta Pixel after consent.
- Native-speaker proofread of LV and RU copy.
- Blog: write the article pages (titles drafted in content.py).

# Rīgas Seifi — website

Static, trilingual (LV / RU / EN), SEO-optimised, multi-page site generated
from content + templates. No build tools beyond Python 3.

## Structure
```
content.py     All copy (LV/RU/EN), prices, SEO meta, FAQ — edit text here.
build.py       Generator: templates + logic. Run it to (re)build the site.
assets/        styles.css, app.js, img/ partner logos (copied into docs/ at build).
docs/          GENERATED output — do not edit by hand. This is what you deploy.
design/        Designer deliverables (A17 Digital moodboard PDF).
snapshot.sh    Save a version snapshot (keeps the last 15).
```

## Design system (from the A17 Digital moodboard, v1.0)
Light theme: cream `#F8F6F1` page, deep navy `#0F2044` header/CTA sections,
footer `#2D3748`, gold `#C9A84C` accents only (≤10% of screen), borders
`#E2DED6`. Headings: Playfair Display (fallback Palatino/Georgia), weight 500.
Body/nav/buttons: Inter. Buttons radius 4–6px, cards 8–12px.
No red accents, no pure white, max 2 fonts, prices always open.
All tokens are CSS variables at the top of `assets/styles.css`.

**Vertical rhythm.** Every section uses `--section-y` top *and* bottom, so
the gap between any two sections is the same. The hero and the booking CTA
use `--section-y-lg` because they carry more weight. Heading-to-content is
always `--block-gap`. Do not give other sections their own padding.

## Modernisation layer (bottom of styles.css)
Everything after the `MODERNISATION LAYER` banner is a later pass that keeps
the palette, the copy and the section order but changes the craft. It is
kept as one block at the end of the file so it can be read — or removed —
on its own. What it does:

- **Breaks the repeated grid.** Six sections used to be "centred heading over
  a row of identical bordered boxes". "Why us" is now an editorial layout
  (heading left, standfirst right, 3+3 / 2+2+2 / 3+3 cards, the first one a
  navy feature card); services uses the same asymmetry; the About figures are
  one navy band rather than five more boxes.
- **Motion that responds to the reader.** Staggered scroll reveals (`--i` on
  each item), a hero entrance sequence (`--d`), header condense-to-glass on
  scroll, a reading-progress hairline, count-up figures, a gold rail that
  fills down the How-it-works steps, hero parallax, and native
  `::details-content` FAQ animation. **The partner logo row is deliberately
  static** — no marquee, no auto-advance.
- **Depth and texture.** Layered shadows (`--e1/2/3`), gradients plus a grain
  overlay (`--grain`) on the navy blocks, gold hairline rules above headings,
  and photo slots styled as designed navy panels instead of dashed
  to-do boxes.
- **All of it is opt-out.** The `prefers-reduced-motion` block at the very end
  neutralises every animation, transform and transition; `app.js` checks the
  same query and registers nothing.

Counters preserve their rendered text exactly — years (`2017`) and composite
values (`24/7`) are skipped on purpose, and the original string is restored
on the final frame.

## Security section: four photos, no video
The column beside the security copy held a single panel with a play button,
reserved for a security video. No video was ever filmed, so the play button
promised something that did not exist and the panel left the column half
empty. It now carries `SECURITY_SHOTS` from content.py — four 4:5 tiles in a
2x2 grid that follow the copy beside them, being the vault, the mechanical
key, the electronic PIN, and the boxes. Empty that list and the block falls
back to the "photo goes here" panel. `PLAY_SVG`, the `video` media kind and
the `.play-badge` rules were removed with it.

## Contacts page: the arrival strip
The contacts page carried no photographs, so `ARRIVAL` in content.py adds a
four-across strip under the map, running in the order a visitor meets them —
the neighbourhood, Kaļķu iela, the door plate with the intercom, and the sign
with the opening hours. The tiles are 3:2, matching the source frames, so the
lettering on the two signs is never cropped. Empty `ARRIVAL["shots"]` and the
whole section disappears.

## Logo and favicon
The house mark is the two crossed keys, redrawn as vector from the brass
plaque in the 2026 shoot (frame 42) and inlined as `LOGO_SVG` in build.py. It
is two sibling paths on purpose. The bows carry counter-wound subpaths to
punch the three ring holes, and keeping the shafts in a path of their own
stops that winding from cancelling against them, which otherwise leaves a
white notch where a shaft meets a bow. The shafts also stop short of each bow
centre so they never cross a ring hole. Colour comes from `currentColor`, so
the mark is gold in the header and takes the surrounding tone elsewhere.

The icons live in `assets/img/` and are linked from every page head:
- `favicon.svg` — the detailed mark on a navy tile.
- `favicon.ico` — three frames, and **the 16px frame is different artwork**.
  At that size the ring holes close up and the mark turns to mush, so 16px
  uses a simplified drawing with solid bows and heavier shafts, while 32 and
  48 use the detailed one. Regenerating the .ico by resampling a single image
  loses this.
- `apple-touch-icon.png` — 180px, opaque, with wider padding because iOS
  masks the corners itself.

`build.py` also copies `favicon.ico` to the site root, because browsers ask
for `/favicon.ico` whether or not a `<link>` points at it.

## Header breakpoints
The desktop nav switches on at **1120px**, not 900px: six Russian nav labels
plus the phone, language switch and CTA do not fit below that and used to
push a horizontal scrollbar onto every page (1024px overflowed by 52px,
900px by 176px). 900–1119px keeps the hamburger — the language switch lives
inside that panel, so it stays reachable. 1120–1299px runs a tightened
header (smaller nav text, icon instead of the written phone number).

## Asset cache-busting
`build.py` appends `?v=<content-hash>` to `styles.css` and `app.js`. Without
it browsers keep serving the previous stylesheet and script after a deploy,
which is exactly what happened during the first redesign.

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
`versions/` and the script auto-prunes to the
15 most recent. `docs/` and caches are excluded from snapshots (regenerable).

## Copy source
Current copy follows the A17 Digital deck "Rīgas Seifi — Teksti dlja sajta,
finalnaja redakcija 2025" (RU original, mirrored into LV and EN):
`RIGAS-SEIGI-USLUGI-TEKSTI` + `RigasSeifi_Copy_Services + o kompanii`.
Structural consequences of that deck:
- The old three-photo "Advantages" block was dropped from the home page; its
  heading now belongs to the "Why clients choose us" block, which carries the
  seven cards from the deck.
- Home order is: hero → why us → prices → security → how it works →
  confidentiality → partners → location → FAQ → CTA.
- New blocks: confidentiality (home), additional-services fee table (boxes),
  The Deal Box step-by-step (services), vault photo pair (about).
- Unregistered clients are no longer described as paying "double the rate";
  the deck says they rent at an individual rate.

## Still TODO before launch
- **Confirm the postcode** for Kaļķu iela 26 — `SITE["postcode"]` is set to
  LV-1050 (Vecrīga); it goes into the LocalBusiness schema.
- **Real photos.** Thirteen frames from the 28 August 2026 shoot of Kaļķu
  iela 26 (127 frames in all) now carry the site — the hero, the three
  how-it-works steps and the About page's second shot in `PHOTOS`, the four
  security tiles in `SECURITY_SHOTS`, and the four wayfinding shots in
  `ARRIVAL`. Every entry records the frame it came from.
  The About page's **first** slot still uses the 400px archive preview,
  because its caption reads "the first vault" and the 2026 shoot covers the
  new premises only. Finish it by supplying a shot of the 2017 vault, or by
  rewording the caption to something the new shoot can illustrate.
  Deleting a slot from `PHOTOS` returns that panel to the "photo goes here"
  state with no other edits.
- Wire the booking form to a real endpoint (email + Telegram/WhatsApp) and a
  `/thank-you` page for GA4 conversion tracking. Hook noted in app.js.
- Privacy & cookie policy page content; connect GA4/GTM + Meta Pixel after consent.
- Native-speaker proofread of LV and RU copy.
- Blog: write the article pages (titles drafted in content.py).
- Press-mentions block (deck block 7: Delfi / TVNet logos) — not built, no
  publications supplied yet.
- The deck says both "1000+ clients in 9 years" (headings) and "over eight
  years" (About text). Both are in the copy as written — confirm which is right.
(Reviews section dropped per designer's note — no reviews exist.)

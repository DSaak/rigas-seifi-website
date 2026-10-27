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

## Design system
Since the owners' October 2026 review the site uses **two colours only**,
Deep Navy `#0F2044` and Warm Gold `#C9A84C`, on white. Text is navy on
white and white on navy, and gold is kept for buttons, icons, hairline rules
and the figures in the navy stat bands. Every navy surface is the same flat
navy (the gradients and grain that made the header and the stat band look
like two different blues are gone). The one exception is the green contact
button, which the owners asked for. **One font**, Playfair Display Regular
(400), sets everything, headings and body alike, with no bold anywhere.
Buttons radius 4–6px, cards 8–12px, prices always open. The tokens are CSS
variables at the top of `assets/styles.css`. This replaced the A17 Digital
moodboard's cream page, charcoal footer, grey labels and Inter body text.

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

## Security section: four photos
The column beside the security copy held a single panel with a play button,
reserved for a security video. No video was ever filmed, so the play button
promised something that did not exist and the panel left the column half
empty. It now carries `SECURITY_SHOTS` from content.py — four 4:5 tiles in a
2x2 grid that follow the copy beside them, being the vault, the mechanical
key, the electronic PIN, and the boxes. Empty that list and the block falls
back to the "photo goes here" panel. `PLAY_SVG`, the `video` media kind and
the `.play-badge` rules were removed with it. The video that is now being
made has its own section on the home page (see Video).

## Contacts page
The page opens with four labelled cards (address with a route link, opening
hours, both phones with a WhatsApp link, email) beside the map. The booking
form used to come first and pushed all of this below the fold; it now closes
the page, as on every other page. Below the map, `ARRIVAL` in content.py adds
four captioned photos in the order a visitor meets them — the building,
Kaļķu iela, the door plate with the intercom, and the sign with the opening
hours. The tiles are 3:2, matching the source frames, so the lettering on the
two signs is never cropped, and each alt text doubles as the caption. Empty
`ARRIVAL["shots"]` and that section disappears.

`REQUISITES` supplies the company details block (legal name, registration
number, registered address) from the Register of Enterprises, checked 22
September 2026. Rows with an empty value are skipped, so the bank name, IBAN
and SWIFT appear as soon as they are typed in.

## September 2026 review (v21)
Changes made from the owners' comments on the draft:
- **Access protection.** There is no time-delay lock. The three levels are
  the guard's mechanical key, the client's mechanical key and the electronic
  PIN (`SECGROUPS`, `SECLOCKS`). The FAQ answer on who can open a box now
  says the client's key and PIN, since the vault holds the guard key.
- **Wording.** "то, что нельзя потерять" became "то, что не хочется
  потерять" (LV and EN mirrored), and "без банковских процедур" became "без
  открытия банковского счёта", with "У нас удобнее и безопаснее, чем в
  банке" added to the FAQ answer.
- **Safe Deposit Federation.** Rīgas Seifi is a member, so SDF left the
  partner row and got its own card at the top of the partners section
  (`MEMBERSHIP`), linked to the federation's member list, which names Rīgas
  Seifi. It is also `memberOf` in the LocalBusiness schema. Set
  `MEMBERSHIP["certificate"]` to the scan's filename and the card shows the
  certificate instead of the logo.
- **Hero.** The home hero shows the façade of Kaļķu iela 26 (frame 13),
  cropped with `"pos"` so the K26 building stays in frame. Phones now get the
  hero photo too, under the buttons.
- **Video.** A slot on the home page between "why us" and the prices
  (`VIDEO`). Until a source is set it shows the vault-aisle frame with a
  "coming soon" note; `"show": False` hides it.

## October 2026 review (v23)
From the owners' notes "коррекция сайта" (Zaneta Saakjane, 13 October 2026,
second version after a meeting on 9 October) and the 2025 price lists in LV,
RU and EN (forwarded 11 October). What changed:
- **Colour and type.** Two colours and one serif in Regular, as above. The
  `MODERNISATION LAYER` grain, glows and gradients were removed for this.
- **Header.** White keys, SAFETY DEPOSIT BOXES under the name as on the old
  logo (`logo()` in build.py). The phone number left the header; the
  handset icon stays on phones and hamburger widths.
- **Menu.** Top: boxes and prices, security, services, about, news,
  contacts (`NAV`). The rules of use, the agents page and the FAQ moved down
  into a footer column (`FOOTER_INFO`). The blog page is now "News"
  (`news.html`). The rules of use link to the old site's rental-rules PDFs
  (`RULES`). The agents page is new (`AGENTS`), with the copy of the old
  site's "Aģentiem" page.
- **Contact button.** The WhatsApp bubble became a green handset that opens a
  menu of WhatsApp, both phones, Facebook, Telegram once its link is set, and
  email (`contact_fab()`). Social links come from `SOCIAL` and appear in the
  footer, on the contacts page and in that menu; empty rows are skipped.
- **Hero.** New title and subtitle. The stat band reads 100% / 10 min /
  27,50 €* / since 2017, with the asterisk explained underneath
  (`HERO[...]["stats_note"]`). "3000+" left the band.
- **Why us.** Seven equal cards, heading in capitals over the text, with the
  owners' wording (`TRUST`).
- **Boxes and prices.** Heading "Размеры ячеек и цены" and a new standfirst.
  The box drawings (`box_svg()`) follow the real boxes, drawn to one scale
  with height, width and length written on them. The "what fits" text is
  gone. Cards quote the 24-month rate as the "from" price. The table has 1,
  3, 6, 12 and 24-month columns, headed like the price list (size in mm,
  then rental term with the monthly price), no bold, and a switch between
  registered and unregistered clients (`TERMS`, `BOX_DATA`, `size_table()`).
  On phones the width and length columns drop out, a note gives them, and
  the table fits a 320px screen. "Все цены указаны с НДС" sits under the
  cards and the table. The extras table is headed "Услуги, тарифы".
- **Services.** The Deal Box card's "learn more" goes to the Deal Box steps
  on the same page; the other cards still open WhatsApp.
- **Consequential edits.** The certificates line now reads EN 1143-1 (11)
  and EN 1300 class D, matching the owners' security text (it said class C).
  The privacy note and how-it-works no longer call the unregistered rate
  "individual", since the price list publishes it. Meta titles quote
  €27,50. The key emoji left the promo ribbon.
- **Follow-up (v25).** The home hero shows the vault again, the aisle
  between the rows of boxes (frame 116), as asked after the review. The
  façade (frame 13) stays on the contacts page, and the video slot's
  poster moved to the box rows (frame 113) so the aisle is not shown twice.
  The "why us" titles size themselves to their card with a container query
  (`cqi`), so КОНФИДЕНЦИАЛЬНОСТЬ stays on one line at every width instead
  of being split across two.

## Video
Fill one source in `VIDEO` in content.py. `"file"` takes an .mp4 placed in
`assets/video/` (keep it under about 50 MB, since GitHub Pages refuses files
over 100 MB and large files slow the page). `"embed"` takes a YouTube or
Vimeo embed URL, which is the better choice for anything long. The frame is
16:9.

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
- `favicon.svg` — the detailed mark on a navy tile. Since October 2026 the
  keys are white in all three files, as in the header logo. The .ico and
  .png were recoloured pixel by pixel (each navy–gold blend became the same
  navy–white blend), so the 16px artwork below is unchanged in shape.
- `favicon.ico` — three frames, and **the 16px frame is different artwork**.
  At that size the ring holes close up and the mark turns to mush, so 16px
  uses a simplified drawing with solid bows and heavier shafts, while 32 and
  48 use the detailed one. Regenerating the .ico by resampling a single image
  loses this.
- `apple-touch-icon.png` — 180px, opaque, with wider padding because iOS
  masks the corners itself.

`build.py` also copies `favicon.ico` to the site root, because browsers ask
for `/favicon.ico` whether or not a `<link>` points at it. The `<link>` tags
carry a content hash (`?v=`), like the stylesheet, so a changed icon reaches
returning visitors.

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
- `docs/<lang>/<page>.html` for lv, ru, en (10 pages each = 30 pages)
- `docs/index.html` root that redirects to the visitor's language
- `sitemap.xml`, `robots.txt`

## Pages
index, boxes, security, how-it-works, services, about, faq, contacts, news
(the `blog` key), agents.

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
- Home order is: hero → why us → video → prices → security → how it works →
  confidentiality → SDF membership + partners → location → FAQ → CTA.
- New blocks: confidentiality (home), additional-services fee table (boxes),
  The Deal Box step-by-step (services), vault photo pair (about).
- Unregistered clients were described as renting "at an individual rate",
  per the deck. Since October 2026 the site publishes their price list
  instead (see the October review).

## Still TODO before launch
- **Rules of use PDFs.** `RULES` links to the three PDFs on the old
  WordPress site. Copy them into `assets/` before the domain moves to this
  site, or the footer links break.
- **Social links from Anton.** `SOCIAL` has Facebook and X from the old
  site; Instagram, Telegram, LinkedIn and YouTube are empty slots. Telegram
  also joins the contact-button menu once filled. Confirm X is still used.
- **Hero eyebrow.** The first version of the October notes asked to remove
  "Первое частное сейфовое хранилище в Балтии"; the second version dropped
  that line, so it stays for now. Confirm.
- **SDF certificate scan.** Put it in `assets/img/` and set
  `MEMBERSHIP["certificate"]`.
- **Bank details** for the requisites block (`REQUISITES`, empty rows).
- **Registered address.** The register still lists Ģertrūdes iela 33/35-1,
  the old premises. Confirm it is current, or update `REQUISITES` once the
  register is changed.
- **VAT wording.** The register shows the company excluded from the VAT
  register on 3 June 2025, while `H[...]["extras_note"]` says all prices
  include VAT. One of the two needs correcting.
- **The video** — set `VIDEO["file"]` or `VIDEO["embed"]`.
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

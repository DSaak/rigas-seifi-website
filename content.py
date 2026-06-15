# -*- coding: utf-8 -*-
"""
Rīgas Seifi — site content (LV / RU / EN).
All copy lives here; build.py turns it into static, SEO-optimised pages.

NOTE FOR REVIEW: Latvian and Russian copy is drafted and should be
proofread by a native speaker before going live. Facts (prices, sizes,
security specs, address) are taken from the existing rigasseifi.lv site.
"""

LANGS = ["lv", "ru", "en"]
DEFAULT_LANG = "lv"

# =====================================================================
#  ADVERT RIBBON  —  the bright bar at the very top of every page.
#  To TURN OFF: change "active" to False.   To TURN ON: set it to True.
#  To CHANGE THE TEXT: edit the lv / ru / en lines below.
#  After any change: run python3 build.py (or double-click publish.command).
# =====================================================================
PROMO = {
    "active": True,
    "link": "#book",   # where clicking the bar takes the visitor
    "lv": "🔑 Atvēršanas akcija — pirmais mēnesis −50 %. Vietu skaits ierobežots.",
    "ru": "🔑 Акция к открытию — первый месяц −50 %. Количество мест ограничено.",
    "en": "🔑 Opening offer — first month −50 %. Limited number of boxes.",
}

SITE = {
    "domain": "https://rigasseifi.lv",
    "brand": "Rīgas Seifi",
    "phone1": "+371 2888 8030",
    "phone1_href": "+37128888030",
    "phone2": "+371 2888 8040",
    "phone2_href": "+37128888040",
    "email": "info@rigasafe.lv",
    "wa_number": "37128888030",
    "address": "Ģertrūdes iela 33/35, Rīga",
    "maps_q": "%C4%A2ertr%C5%ABdes%20iela%2033%2F35%2C%20R%C4%ABga",
    "founded": "2017",
    "boxes": "3000+",
    "facebook": "https://www.facebook.com/RigasSeifiLatvija",
}

# page key -> shared slug (language lives in the path prefix: /lv/, /ru/, /en/)
PAGES = ["index", "boxes", "security", "how", "services", "about", "faq", "contacts", "blog"]
SLUGS = {
    "index": "index",
    "boxes": "boxes",
    "security": "security",
    "how": "how-it-works",
    "services": "services",
    "about": "about",
    "faq": "faq",
    "contacts": "contacts",
    "blog": "blog",
}
# pages shown in the header nav (in order)
NAV = ["boxes", "security", "services", "about", "faq", "contacts"]

# ----- prices: 12-month registered-client monthly rate (from current price list) -----
BOX_DATA = [
    {"nr": "1", "dim": "3,5 × 24,5 × 43,5 cm", "m1": "€50", "m12": "€30",    "m24": "€27,50",  "qty": "722"},
    {"nr": "2", "dim": "6 × 24,5 × 43,5 cm",   "m1": "€60", "m12": "€37,50", "m24": "€32,50",  "qty": "531"},
    {"nr": "3", "dim": "11 × 24,5 × 43,5 cm",  "m1": "€70", "m12": "€42,50", "m24": "€37,50",  "qty": "1795", "popular": True},
    {"nr": "4", "dim": "16 × 24,5 × 43,5 cm",  "m1": "€150","m12": "€90",    "m24": "€82,50",  "qty": "142"},
    {"nr": "5", "dim": "29 × 24,5 × 43,5 cm",  "m1": "€250","m12": "€150",   "m24": "€137,50", "qty": "71"},
]

# =====================================================================
#  UI strings (chrome shared across every page)
# =====================================================================
UI = {
    "lv": {
        "nav": {"boxes": "Seifi un cenas", "security": "Drošība", "services": "Pakalpojumi",
                "about": "Par mums", "faq": "FAQ", "contacts": "Kontakti"},
        "book": "Rezervēt", "menu": "Izvēlne", "lang_name": "Latviešu",
        "cta_book": "Rezervēt seifu", "cta_prices": "Apskatīt cenas", "cta_call": "Zvanīt",
        "cta_route": "Maršruts", "cta_wa": "Rakstīt WhatsApp", "cta_more": "Uzzināt vairāk",
        "from": "no", "permonth": "/mēn.", "popular": "Populārākais",
        "footer_tagline": "Privāta seifu glabātava Rīgas centrā kopš 2017. gada.",
        "footer_nav": "Lapas", "footer_contact": "Kontakti", "footer_hours": "Darba laiks",
        "hours_week": "P–Pk 10:00–19:00", "hours_after": "Vakaros un 24/7 — pēc vienošanās",
        "ft_privacy": "Privātuma politika", "ft_cookies": "Sīkdatņu politika", "ft_rights": "Visas tiesības aizsargātas.",
        "cookie_text": "Mēs izmantojam sīkdatnes satiksmes analīzei. Jūs varat piekrist vai atteikties.",
        "cookie_accept": "Piekrītu", "cookie_decline": "Atteikties",
        "wa_msg": "Sveiki! Vēlos rezervēt seifu.",
        "breadcrumb_home": "Sākums",
        "form_title": "Pieteikums", "f_name": "Vārds *", "f_phone": "Tālrunis *", "f_email": "E-pasts",
        "f_size": "Seifa izmērs", "f_date": "Sākuma datums", "f_comment": "Komentārs",
        "opt": "nav obligāti", "f_unsure": "Nezinu", "f_submit": "Nosūtīt pieteikumu",
        "ph_phone": "piem., +371 12345678", "ph_email": "piem., vards@epasts.lv", "ph_comment": "Jautājums vai vēlmes",
        "f_privacy": "Nosūtot formu, jūs piekrītat personas datu apstrādei saskaņā ar privātuma politiku.",
        "f_ok_t": "Paldies!", "f_ok_p": "Jūsu pieteikums saņemts. Sazināsimies vienas darba dienas laikā.",
        "or_call": "vai zvaniet:",
    },
    "ru": {
        "nav": {"boxes": "Ячейки и цены", "security": "Безопасность", "services": "Услуги",
                "about": "О компании", "faq": "FAQ", "contacts": "Контакты"},
        "book": "Забронировать", "menu": "Меню", "lang_name": "Русский",
        "cta_book": "Забронировать ячейку", "cta_prices": "Узнать цены", "cta_call": "Позвонить",
        "cta_route": "Маршрут", "cta_wa": "Написать в WhatsApp", "cta_more": "Подробнее",
        "from": "от", "permonth": "/мес.", "popular": "Популярный",
        "footer_tagline": "Частное сейфовое хранилище в центре Риги с 2017 года.",
        "footer_nav": "Страницы", "footer_contact": "Контакты", "footer_hours": "Часы работы",
        "hours_week": "Пн–Пт 10:00–19:00", "hours_after": "Вечером и 24/7 — по договорённости",
        "ft_privacy": "Политика конфиденциальности", "ft_cookies": "Политика cookie", "ft_rights": "Все права защищены.",
        "cookie_text": "Мы используем cookie для анализа трафика. Вы можете согласиться или отказаться.",
        "cookie_accept": "Согласен", "cookie_decline": "Отказаться",
        "wa_msg": "Здравствуйте! Хочу забронировать сейфовую ячейку.",
        "breadcrumb_home": "Главная",
        "form_title": "Заявка", "f_name": "Имя *", "f_phone": "Телефон *", "f_email": "Эл. почта",
        "f_size": "Размер ячейки", "f_date": "Дата начала", "f_comment": "Комментарий",
        "opt": "необязательно", "f_unsure": "Не знаю", "f_submit": "Отправить заявку",
        "ph_phone": "напр., +371 12345678", "ph_email": "напр., name@email.com", "ph_comment": "Вопрос или пожелания",
        "f_privacy": "Отправляя форму, вы соглашаетесь с обработкой персональных данных согласно политике конфиденциальности.",
        "f_ok_t": "Спасибо!", "f_ok_p": "Заявка получена. Свяжемся с вами в течение одного рабочего дня.",
        "or_call": "или звоните:",
    },
    "en": {
        "nav": {"boxes": "Boxes & prices", "security": "Security", "services": "Services",
                "about": "About", "faq": "FAQ", "contacts": "Contacts"},
        "book": "Book now", "menu": "Menu", "lang_name": "English",
        "cta_book": "Book a box", "cta_prices": "See prices", "cta_call": "Call us",
        "cta_route": "Directions", "cta_wa": "Message on WhatsApp", "cta_more": "Learn more",
        "from": "from", "permonth": "/mo", "popular": "Most popular",
        "footer_tagline": "Private safe deposit vault in central Riga since 2017.",
        "footer_nav": "Pages", "footer_contact": "Contacts", "footer_hours": "Opening hours",
        "hours_week": "Mon–Fri 10:00–19:00", "hours_after": "Evenings & 24/7 by arrangement",
        "ft_privacy": "Privacy policy", "ft_cookies": "Cookie policy", "ft_rights": "All rights reserved.",
        "cookie_text": "We use cookies for traffic analytics. You can accept or decline.",
        "cookie_accept": "Accept", "cookie_decline": "Decline",
        "wa_msg": "Hello! I would like to book a safe deposit box.",
        "breadcrumb_home": "Home",
        "form_title": "Booking request", "f_name": "Name *", "f_phone": "Phone *", "f_email": "Email",
        "f_size": "Box size", "f_date": "Start date", "f_comment": "Comment",
        "opt": "optional", "f_unsure": "Not sure", "f_submit": "Send request",
        "ph_phone": "e.g. +371 12345678", "ph_email": "e.g. name@email.com", "ph_comment": "Question or special requests",
        "f_privacy": "By submitting you agree to the processing of personal data under our privacy policy.",
        "f_ok_t": "Thank you!", "f_ok_p": "Your request has been received. We will contact you within one business day.",
        "or_call": "or call:",
    },
}

# box-size "what fits" descriptions, per language, keyed by box nr
FITS = {
    "lv": {"1": "Dokumenti, valūta, vērtspapīri", "2": "Dokumenti, rotaslietas, datu nesēji",
           "3": "Rotaslietas, kolekcijas, mape A4", "4": "Lielāki priekšmeti, kastes", "5": "Kolekcijas, tehnika, arhīvi"},
    "ru": {"1": "Документы, валюта, ценные бумаги", "2": "Документы, украшения, носители данных",
           "3": "Украшения, коллекции, папка А4", "4": "Крупные предметы, шкатулки", "5": "Коллекции, техника, архивы"},
    "en": {"1": "Documents, currency, securities", "2": "Documents, jewellery, data media",
           "3": "Jewellery, collections, A4 folder", "4": "Larger items, cases", "5": "Collections, equipment, archives"},
}

# SEO meta: per language, per page -> (title, description, keywords)
META = {
    "lv": {
        "index": ("Rīgas Seifi — Privātas seifu glabātavas Rīgas centrā | No €30/mēn.",
                  "Vairāk nekā 3000 seifu divās pazemes glabātavās Rīgas centrā. Bez bankas konta, pilnīga konfidencialitāte. No €30 mēnesī.",
                  "seifu noma, seifa īre, bankas instrument, sefs Rīgā, vērtslietu glabāšana"),
        "boxes": ("Seifu izmēri un cenas — Rīgas Seifi | No €30 mēnesī",
                  "Pieci seifu izmēri, atklātas cenas no €30/mēn. Izvēlieties izmēru un rezervējiet seifu Rīgas centrā tiešsaistē.",
                  "seifa cena, seifu izmēri, seifa noma Rīgā, sefs cena"),
        "security": ("Drošība — Rīgas Seifi | Pazemes glabātavas, Rosengrens, 24/7 apsardze",
                     "Divas pazemes dzelzsbetona glabātavas, Rosengrens aprīkojums, bruņotas durvis, video novērošana un diennakts bruņota apsardze.",
                     "seifu drošība, bankas līmeņa drošība, Rosengrens, apsardze Rīgā"),
        "how": ("Kā tas notiek — seifa noma 3 soļos | Rīgas Seifi",
                "Izvēlieties izmēru, parakstiet līgumu 10 minūtēs un glabājiet droši. Bez bankas procedūrām. Reģistrēts un anonīms klients.",
                "kā nomāt seifu, seifa līgums, seifa noma soļi"),
        "services": ("Pakalpojumi — seifu noma, The Deal Box, transports | Rīgas Seifi",
                     "Seifu noma, 24/7 piekļuve, darījumu seifs (The Deal Box), apsargāta vērtslietu pārvešana un konfidenciāla sapulču telpa.",
                     "darījumu seifs, vērtslietu transports, sapulču telpa Rīgā"),
        "about": ("Par mums — pirmā privātā seifu glabātava Baltijā | Rīgas Seifi",
                  "Rīgas Seifi — pirmā privātā seifu noma Baltijā kopš 2017. gada. Vairāk nekā 3000 seifu, komanda ar banku un drošības pieredzi.",
                  "par Rīgas Seifi, seifu uzņēmums Rīgā, pirmais Baltijā"),
        "faq": ("Biežāk uzdotie jautājumi — seifu noma | Rīgas Seifi",
                "Atbildes uz jautājumiem par seifu nomu: piekļuve, drošība, cenas, ko drīkst glabāt, līgums un konfidencialitāte.",
                "seifu noma jautājumi, seifa FAQ, ko glabāt seifā"),
        "contacts": ("Kontakti un adrese — Ģertrūdes iela 33/35, Rīga | Rīgas Seifi",
                     "Rīgas Seifi: Ģertrūdes iela 33/35, Rīga. Tālrunis, WhatsApp, e-pasts, karte un darba laiks. Rezervējiet seifu jau šodien.",
                     "Rīgas Seifi kontakti, seifu noma adrese, Ģertrūdes iela"),
        "blog": ("Blogs un padomi — vērtslietu glabāšana | Rīgas Seifi",
                 "Padomi par vērtslietu un dokumentu drošu glabāšanu, seifu nomu un atšķirībām starp bankas un privāto glabātavu.",
                 "vērtslietu glabāšana, ko glabāt seifā, bankas vs privātais seifs"),
    },
    "ru": {
        "index": ("Rīgas Seifi — Аренда сейфовых ячеек в центре Риги | От €30/мес.",
                  "Более 3000 сейфов в двух подземных хранилищах в центре Риги. Без банковского счёта, полная конфиденциальность. От €30 в месяц.",
                  "аренда сейфа, сейфовая ячейка Рига, хранение ценностей, аренда сейфовой ячейки"),
        "boxes": ("Размеры и цены сейфов — Rīgas Seifi | От €30 в месяц",
                  "Пять размеров ячеек, открытые цены от €30/мес. Выберите размер и забронируйте сейф в центре Риги онлайн.",
                  "цена сейфа, размеры ячеек, аренда сейфа Рига, стоимость сейфовой ячейки"),
        "security": ("Безопасность — Rīgas Seifi | Подземные хранилища, Rosengrens, охрана 24/7",
                     "Два подземных железобетонных хранилища, оборудование Rosengrens, бронедвери, видеонаблюдение и круглосуточная вооружённая охрана.",
                     "безопасность сейфа, банковский уровень защиты, Rosengrens, охрана Рига"),
        "how": ("Как это работает — аренда сейфа за 3 шага | Rīgas Seifi",
                "Выберите размер, подпишите договор за 10 минут и храните спокойно. Без банковских процедур. Зарегистрированный и анонимный клиент.",
                "как арендовать сейф, договор аренды сейфа, шаги аренды"),
        "services": ("Услуги — аренда сейфов, The Deal Box, транспорт | Rīgas Seifi",
                     "Аренда сейфов, доступ 24/7, сейф для сделок (The Deal Box), охраняемая перевозка ценностей и конфиденциальная переговорная.",
                     "сейф для сделок, перевозка ценностей, переговорная Рига"),
        "about": ("О компании — первое частное сейфовое хранилище в Балтии | Rīgas Seifi",
                  "Rīgas Seifi — первый частный сейфовый сервис в Балтии с 2017 года. Более 3000 ячеек, команда с банковским и охранным опытом.",
                  "о Rīgas Seifi, сейфовая компания Рига, первый в Балтии"),
        "faq": ("Часто задаваемые вопросы — аренда сейфа | Rīgas Seifi",
                "Ответы на вопросы об аренде сейфа: доступ, безопасность, цены, что можно хранить, договор и конфиденциальность.",
                "вопросы аренда сейфа, FAQ сейф, что хранить в сейфе"),
        "contacts": ("Контакты и адрес — ул. Гертрудес 33/35, Рига | Rīgas Seifi",
                     "Rīgas Seifi: ул. Гертрудес 33/35, Рига. Телефон, WhatsApp, эл. почта, карта и часы работы. Забронируйте сейф сегодня.",
                     "Rīgas Seifi контакты, аренда сейфа адрес, Гертрудес"),
        "blog": ("Блог и советы — хранение ценностей | Rīgas Seifi",
                 "Советы о безопасном хранении ценностей и документов, аренде сейфа и отличиях частного хранилища от банковского.",
                 "хранение ценностей, что хранить в сейфе, банк против частного сейфа"),
    },
    "en": {
        "index": ("Rīgas Seifi — Private Safe Deposit Boxes in Central Riga | From €30/mo",
                  "Over 3,000 safe deposit boxes in two underground vaults in central Riga. No bank account, full confidentiality. From €30 a month.",
                  "safe deposit box riga, safe rental, valuables storage, private vault riga"),
        "boxes": ("Box Sizes & Prices — Rīgas Seifi | From €30 a month",
                  "Five box sizes, transparent prices from €30/mo. Choose a size and book your safe deposit box in central Riga online.",
                  "safe deposit box price, box sizes, safe rental riga, deposit box cost"),
        "security": ("Security — Rīgas Seifi | Underground vaults, Rosengrens, 24/7 guards",
                     "Two underground reinforced-concrete vaults, Rosengrens equipment, armoured doors, video surveillance and round-the-clock armed security.",
                     "safe deposit security, bank-grade security, Rosengrens, armed guards riga"),
        "how": ("How It Works — rent a safe box in 3 steps | Rīgas Seifi",
                "Choose a size, sign the agreement in 10 minutes and store with confidence. No bank procedures. Registered and anonymous clients.",
                "how to rent a safe box, safe rental agreement, deposit box steps"),
        "services": ("Services — safe rental, The Deal Box, transport | Rīgas Seifi",
                     "Safe deposit rental, 24/7 access, escrow safe (The Deal Box), guarded transport of valuables and a confidential meeting room.",
                     "escrow safe, valuables transport, meeting room riga"),
        "about": ("About — the first private safe depository in the Baltics | Rīgas Seifi",
                  "Rīgas Seifi — the first private safe deposit service in the Baltics since 2017. Over 3,000 boxes, a team with banking and security experience.",
                  "about rigas seifi, safe deposit company riga, first in baltics"),
        "faq": ("Frequently Asked Questions — safe box rental | Rīgas Seifi",
                "Answers about safe deposit box rental: access, security, prices, what you can store, the agreement and confidentiality.",
                "safe deposit faq, deposit box questions, what to store in a safe"),
        "contacts": ("Contacts & Location — Ģertrūdes iela 33/35, Riga | Rīgas Seifi",
                     "Rīgas Seifi: Ģertrūdes iela 33/35, Riga. Phone, WhatsApp, email, map and opening hours. Book your safe deposit box today.",
                     "rigas seifi contacts, safe deposit address, gertrudes street"),
        "blog": ("Blog & guides — storing valuables | Rīgas Seifi",
                 "Guides on safely storing valuables and documents, renting a safe deposit box and how private vaults differ from banks.",
                 "storing valuables, what to keep in a safe, bank vs private safe"),
    },
}

# =====================================================================
#  Reusable content blocks (advantages, steps, security points, trust)
# =====================================================================
ADV = {
    "lv": [("Drošība", "Divas pazemes dzelzsbetona glabātavas ar Rosengrens aprīkojumu, video novērošanu un bruņotu apsardzi 24/7."),
           ("Konfidencialitāte", "Bez bankas konta. Seifa saturu zināt tikai jūs — mēs to nepārbaudām un nereģistrējam."),
           ("Ērtums", "Rīgas centrā, Ģertrūdes ielā. Darba dienās 10:00–19:00, vakara un 24/7 piekļuve pēc vienošanās.")],
    "ru": [("Безопасность", "Два подземных железобетонных хранилища с оборудованием Rosengrens, видеонаблюдением и вооружённой охраной 24/7."),
           ("Конфиденциальность", "Без банковского счёта. Содержимое ячейки известно только вам — мы его не проверяем и не регистрируем."),
           ("Удобство", "Центр Риги, улица Гертрудес. Будни 10:00–19:00, вечерние визиты и доступ 24/7 по договорённости.")],
    "en": [("Security", "Two underground reinforced-concrete vaults with Rosengrens equipment, video surveillance and 24/7 armed security."),
           ("Confidentiality", "No bank account. Only you know what is in your box — we do not inspect or register the contents."),
           ("Convenience", "Central Riga, Ģertrūdes street. Weekdays 10:00–19:00, evening and 24/7 access by arrangement.")],
}
STEPS = {
    "lv": [("Izvēlieties izmēru", "Tiešsaistē vai uz vietas — palīdzēsim atrast piemērotāko."),
           ("Parakstiet līgumu", "10 minūtes uz vietas. Bez bankas procedūrām un liekiem jautājumiem."),
           ("Glabājiet droši", "Piekļuve darba laikā, vakaros un 24/7 — pēc vienošanās.")],
    "ru": [("Выберите размер", "Онлайн или на месте — поможем подобрать оптимальный."),
           ("Подпишите договор", "10 минут на месте. Без банковских процедур и лишних вопросов."),
           ("Храните спокойно", "Доступ в рабочее время, вечером и 24/7 — по договорённости.")],
    "en": [("Choose a size", "Online or on site — we will help you pick the right one."),
           ("Sign the agreement", "10 minutes on site. No bank procedures, no unnecessary questions."),
           ("Store with confidence", "Access during business hours, evenings and 24/7 by arrangement.")],
}
SECPOINTS = {
    "lv": ["Divas pazemes dzelzsbetona glabātavas — kopā vairāk nekā 100 m²",
           "Zviedrijas Rosengrens (dib. 1886) seifu aprīkojums",
           "Bruņotas durvis un modernas signalizācijas sistēmas",
           "Sienās — trokšņa un vibrācijas detektori",
           "Video novērošana un ugunsdrošības sistēmas",
           "Diennakts bruņota apsardze (SP Leģions) ar ātrās reaģēšanas vienību",
           "Unikāla slēdzene: seifa numurs + PIN + divas atslēgas; pēc 5 kļūdainiem PIN — bloķēšana"],
    "ru": ["Два подземных железобетонных хранилища — более 100 м² в сумме",
           "Шведское сейфовое оборудование Rosengrens (осн. 1886)",
           "Бронированные двери и современные системы сигнализации",
           "В стенах — детекторы шума и вибрации",
           "Видеонаблюдение и системы пожарной безопасности",
           "Круглосуточная вооружённая охрана (SP Leģions) с группой быстрого реагирования",
           "Уникальный замок: номер ячейки + PIN + два ключа; после 5 неверных PIN — блокировка"],
    "en": ["Two underground reinforced-concrete vaults — over 100 m² combined",
           "Swedish Rosengrens vault equipment (est. 1886)",
           "Armoured doors and modern alarm systems",
           "Noise and vibration detectors within the walls",
           "Video recording and fire-safety systems",
           "Round-the-clock armed security (SP Leģions) with a rapid-response team",
           "Unique lock: box number + PIN + two keys; lockout after 5 wrong PINs"],
}
TRUST = {
    "lv": [("Kopš 2017. gada", "Pirmā privātā seifu noma Baltijā — pieredze, ko nevar nopirkt."),
           ("3000+ seifu", "Lielākā privātā glabātava reģionā ar pieciem izmēriem."),
           ("Bez bankas", "Nekādu kontu, rindu vai bankas darba laika ierobežojumu.")],
    "ru": [("С 2017 года", "Первый частный сейфовый сервис в Балтии — опыт, который не купить."),
           ("3000+ ячеек", "Крупнейшее частное хранилище в регионе, пять размеров."),
           ("Без банка", "Никаких счетов, очередей и ограничений банковского графика.")],
    "en": [("Since 2017", "The first private safe deposit service in the Baltics — experience you cannot buy."),
           ("3,000+ boxes", "The largest private depository in the region, five sizes."),
           ("No bank involved", "No accounts, no queues, no banking-hours restrictions.")],
}

# hero per language: eyebrow, title, subtitle, 4 stats (value,label)
HERO = {
    "lv": {"eyebrow": "Pirmā privātā seifu glabātava Baltijā",
           "title": "Jūsu vērtslietas — aiz bruņu durvīm zem paša Rīgas centra",
           "sub": "Vairāk nekā 3000 seifu bez bankas procedūrām un konta atvēršanas. Pilnīga konfidencialitāte. No €30 mēnesī.",
           "stats": [("3000+", "seifu"), ("2", "pazemes glabātavas"), ("24/7", "piekļuve pēc vienošanās"), ("2017", "strādājam kopš")]},
    "ru": {"eyebrow": "Первое частное сейфовое хранилище в Балтии",
           "title": "Все ваши ценности — за бронедверями под центром Риги",
           "sub": "Более 3000 ячеек без банковских процедур и открытия счёта. Полная конфиденциальность. От €30 в месяц.",
           "stats": [("3000+", "ячеек"), ("2", "подземных хранилища"), ("24/7", "доступ по договорённости"), ("2017", "работаем с")]},
    "en": {"eyebrow": "The first private safe depository in the Baltics",
           "title": "Your valuables — behind armoured doors beneath Riga's centre",
           "sub": "Over 3,000 boxes with no bank procedures and no account opening. Full confidentiality. From €30 a month.",
           "stats": [("3000+", "deposit boxes"), ("2", "underground vaults"), ("24/7", "access by arrangement"), ("2017", "operating since")]},
}

# section headings used across pages
H = {
    "lv": {"adv": "Kāpēc Rīgas Seifi", "sizes": "Seifu izmēri un cenas",
           "sizes_sub": "Atklātas cenas bez slēptiem maksājumiem. Jo ilgāks termiņš, jo zemāka mēneša maksa. Norādītas reģistrētu klientu 12 mēnešu cenas.",
           "how": "Kā tas notiek", "security": "Drošība bez kompromisiem", "trust": "Kāpēc mums uzticas",
           "location": "Adrese un darba laiks", "faq": "Biežāk uzdotie jautājumi", "services": "Mūsu pakalpojumi",
           "book": "Rezervējiet seifu jau šodien", "book_sub": "Atstājiet pieteikumu — sazināsimies vienas darba dienas laikā. Vai uzreiz rakstiet WhatsApp.",
           "price_note": "Cenas norādītas reģistrētiem klientiem ar 12 mēnešu līgumu. Pieejami arī 1 un 24 mēnešu termiņi. Nereģistrētiem klientiem — dubultā likme. Minimālais termiņš — 1 mēnesis.",
           "table_size": "Izmērs", "table_dim": "Izmēri (A×P×Dz)", "table_fits": "Kas ietilpst", "table_m1": "1 mēn.", "table_m12": "12 mēn.", "table_m24": "24 mēn."},
    "ru": {"adv": "Почему Rīgas Seifi", "sizes": "Размеры и цены ячеек",
           "sizes_sub": "Открытые цены без скрытых платежей. Чем дольше срок — тем ниже месячная ставка. Указаны цены для зарегистрированных клиентов на 12 месяцев.",
           "how": "Как это работает", "security": "Безопасность без компромиссов", "trust": "Почему нам доверяют",
           "location": "Адрес и часы работы", "faq": "Частые вопросы", "services": "Наши услуги",
           "book": "Забронируйте ячейку сегодня", "book_sub": "Оставьте заявку — свяжемся в течение одного рабочего дня. Или напишите сразу в WhatsApp.",
           "price_note": "Цены указаны для зарегистрированных клиентов при договоре на 12 месяцев. Доступны также сроки 1 и 24 месяца. Для незарегистрированных клиентов — двойной тариф. Минимальный срок — 1 месяц.",
           "table_size": "Размер", "table_dim": "Размеры (В×Ш×Г)", "table_fits": "Что помещается", "table_m1": "1 мес.", "table_m12": "12 мес.", "table_m24": "24 мес."},
    "en": {"adv": "Why Rīgas Seifi", "sizes": "Box sizes and prices",
           "sizes_sub": "Transparent pricing, no hidden fees. The longer the term, the lower the monthly rate. Prices shown are for registered clients on a 12-month agreement.",
           "how": "How it works", "security": "Security without compromise", "trust": "Why clients trust us",
           "location": "Location and opening hours", "faq": "Frequently asked questions", "services": "Our services",
           "book": "Book your box today", "book_sub": "Leave a request — we reply within one business day. Or message us directly on WhatsApp.",
           "price_note": "Prices shown are for registered clients on a 12-month agreement. 1 and 24-month terms are also available. Unregistered clients pay double the rate. Minimum term — 1 month.",
           "table_size": "Size", "table_dim": "Dimensions (H×W×D)", "table_fits": "What fits", "table_m1": "1 mo", "table_m12": "12 mo", "table_m24": "24 mo"},
}

# Services page content: list of (icon, title, body)
SERVICES = {
    "lv": [
        ("box", "Seifu noma", "Vairāk nekā 3000 seifu piecos izmēros divās pazemes glabātavās. Lieliem priekšmetiem — atsevišķas glabāšanas zonas. Saturs ir konfidenciāls."),
        ("clock", "24/7 piekļuve", "Standarta darba laiks 10:00–19:00, taču piekļuvi ārpus darba laika var saskaņot ar vadību. Pakalpojums tiek aprēķināts pēc tarifa."),
        ("deal", "The Deal Box — darījumu seifs", "Drošs veids, kā garantēt darījumu starp pusēm. Tiek slēgts trīspusējs līgums, un Rīgas Seifi tur atslēgas kā darījuma garants, līdz izpildīti visi nosacījumi."),
        ("truck", "Apsargāta pārvešana", "Vērtslietu pārvešana uz glabātavu vai no tās ar apsardzi. Cena atkarīga no drošības līmeņa, transporta un attāluma."),
        ("room", "Konfidenciāla sapulču telpa", "Aprīkota telpa darījumu parakstīšanai vai konfidenciālām sarunām pirms vērtslietu novietošanas. Šajā telpā video novērošana netiek veikta."),
    ],
    "ru": [
        ("box", "Аренда сейфов", "Более 3000 ячеек пяти размеров в двух подземных хранилищах. Для крупных предметов — отдельные зоны хранения. Содержимое конфиденциально."),
        ("clock", "Доступ 24/7", "Стандартные часы 10:00–19:00, но доступ вне рабочего времени можно согласовать с руководством. Услуга рассчитывается по тарифу."),
        ("deal", "The Deal Box — сейф для сделок", "Надёжный способ гарантировать сделку между сторонами. Заключается трёхсторонний договор, и Rīgas Seifi держит ключи как гарант сделки до выполнения всех условий."),
        ("truck", "Охраняемая перевозка", "Перевозка ценностей в хранилище и обратно с охраной. Цена зависит от уровня безопасности, транспорта и расстояния."),
        ("room", "Конфиденциальная переговорная", "Оборудованное помещение для подписания сделок или конфиденциальных переговоров перед размещением ценностей. В этом помещении видеонаблюдение не ведётся."),
    ],
    "en": [
        ("box", "Safe deposit rental", "Over 3,000 boxes in five sizes across two underground vaults. Dedicated zones for larger items. Contents stay confidential."),
        ("clock", "24/7 access", "Standard hours are 10:00–19:00, but after-hours access can be arranged with management. The service is charged by tariff."),
        ("deal", "The Deal Box — escrow safe", "A secure way to guarantee a deal between parties. A three-party agreement is signed and Rīgas Seifi holds the keys as deal guarantor until all conditions are met."),
        ("truck", "Guarded transport", "Escorted transfer of valuables to or from the vault. Pricing depends on security level, vehicle and distance."),
        ("room", "Confidential meeting room", "An equipped room for signing deals or confidential talks before placing valuables. No video surveillance is recorded in this room."),
    ],
}

# About page paragraphs
ABOUT = {
    "lv": {
        "lead": "Rīgas Seifi ir pirmais uzņēmums Baltijas valstīs, kas piedāvā nebanku seifu nomas pakalpojumus.",
        "paras": [
            "Kopš 2017. gada mēs glabājam mūsu klientu dokumentus un vērtslietas divās pazemes dzelzsbetona glabātavās Rīgas centrā, Ģertrūdes ielā 33/35.",
            "Mūsu komandā strādā profesionāļi ar plašu pieredzi Latvijas banku un finanšu sistēmā, tostarp drošības jomā. Apsardzi nodrošina partneris SP Leģions.",
            "Mēs piedāvājam to, ko banka nevar: nomu bez konta atvēršanas, pilnīgu konfidencialitāti un piekļuvi ērtā laikā. Seifa saturs paliek jūsu īpašums un ir aizsargāts pat uzņēmuma maksātnespējas gadījumā.",
        ],
        "facts": [("3000+", "seifu piecos izmēros"), ("2", "pazemes glabātavas, 100+ m²"), ("2017", "darbojamies kopš"), ("1.", "privātā glabātava Baltijā")],
    },
    "ru": {
        "lead": "Rīgas Seifi — первое предприятие в странах Балтии, предоставляющее небанковские услуги аренды сейфовых ячеек.",
        "paras": [
            "С 2017 года мы храним документы и ценности наших клиентов в двух подземных железобетонных хранилищах в центре Риги, на улице Гертрудес 33/35.",
            "В нашей команде работают профессионалы с большим опытом в банковской и финансовой системе Латвии, в том числе в сфере безопасности. Охрану обеспечивает партнёр SP Leģions.",
            "Мы предлагаем то, что не может банк: аренду без открытия счёта, полную конфиденциальность и доступ в удобное время. Содержимое ячейки остаётся вашей собственностью и защищено даже при банкротстве компании.",
        ],
        "facts": [("3000+", "ячеек пяти размеров"), ("2", "подземных хранилища, 100+ м²"), ("2017", "работаем с"), ("1-е", "частное хранилище в Балтии")],
    },
    "en": {
        "lead": "Rīgas Seifi is the first company in the Baltic states to offer non-banking safe deposit box rental.",
        "paras": [
            "Since 2017 we have kept our clients' documents and valuables in two underground reinforced-concrete vaults in central Riga, at Ģertrūdes iela 33/35.",
            "Our team are professionals with extensive experience in Latvia's banking and financial system, including security. Security is provided by our partner SP Leģions.",
            "We offer what a bank cannot: rental without opening an account, full confidentiality and access at a convenient time. The contents of your box remain your property and are protected even in the event of company insolvency.",
        ],
        "facts": [("3,000+", "boxes in five sizes"), ("2", "underground vaults, 100+ m²"), ("2017", "operating since"), ("1st", "private depository in the Baltics")],
    },
}

# How-it-works extra content (what you need / payment / access rules)
HOWX = {
    "lv": {
        "need_t": "Kas nepieciešams", "need": ["Reģistrētam klientam — personu apliecinošs dokuments.",
            "Anonīmam klientam — dokumenti nav nepieciešami.", "Uzņēmumam — reģistrācijas dati un pārstāvja pilnvara."],
        "pay_t": "Apmaksa", "pay": ["Skaidrā naudā, ar karti vai pārskaitījumu.", "Atļauta trešās puses apmaksa, norādot rēķina numuru.", "Atslēgas nodrošina ar drošības depozītu (atmaksā līguma beigās)."],
        "access_t": "Piekļuve un noteikumi", "access": ["Standarta apmeklējums — līdz 15 minūtēm.", "Piekļuvei nepieciešams seifa numurs, PIN un atslēga.", "Termiņš no 1 mēneša; pagarinājums — vienkārši apmaksājot nākamo periodu."],
    },
    "ru": {
        "need_t": "Что нужно", "need": ["Зарегистрированному клиенту — документ, удостоверяющий личность.",
            "Анонимному клиенту — документы не нужны.", "Компании — регистрационные данные и доверенность представителя."],
        "pay_t": "Оплата", "pay": ["Наличными, картой или переводом.", "Допускается оплата третьим лицом с указанием номера счёта.", "Ключи обеспечиваются гарантийным депозитом (возвращается в конце аренды)."],
        "access_t": "Доступ и правила", "access": ["Стандартный визит — до 15 минут.", "Для доступа нужны номер ячейки, PIN и ключ.", "Срок от 1 месяца; продление — простой оплатой следующего периода."],
    },
    "en": {
        "need_t": "What you need", "need": ["Registered client — an identity document.",
            "Anonymous client — no documents required.", "Company — registration details and a representative's authorisation."],
        "pay_t": "Payment", "pay": ["Cash, card or bank transfer.", "Third-party payment is allowed if the invoice number is given.", "Keys are secured by a guaranty deposit (refunded at the end of the rental)."],
        "access_t": "Access and rules", "access": ["A standard visit is up to 15 minutes.", "Access requires the box number, PIN and key.", "Term from 1 month; extend simply by paying for the next period."],
    },
}

# FAQ: list of (question, answer) per language
FAQ = {
    "lv": [
        ("Vai man jāatver bankas konts?", "Nē. Mēs neesam banka — līgumu noslēdzam uz vietas 10 minūtēs, bez bankas procedūrām."),
        ("Kas zina, kas atrodas manā seifā?", "Tikai jūs. Mēs saturu nepārbaudām un nereģistrējam. Atslēgas ir tikai jūsu rīcībā, un mūsu darbinieki nevar piekļūt saturam."),
        ("Ko drīkst un ko nedrīkst glabāt?", "Drīkst: valūtu, dārgmetālus, rotaslietas, vērtspapīrus, dokumentus, antikvariātu, mākslu, datu nesējus. Nedrīkst: viegli uzliesmojošas, sprādzienbīstamas, toksiskas, radioaktīvas vielas un ieročus."),
        ("Kāds ir minimālais nomas termiņš?", "1 mēnesis. Ilgtermiņa līgumiem (12–24 mēneši) cena mēnesī ir ievērojami zemāka."),
        ("Vai varu piekļūt seifam ārpus darba laika?", "Jā — vakara apmeklējumi un 24/7 piekļuve pieejama pēc iepriekšējas vienošanās."),
        ("Cik droši ir jūsu seifi?", "Divas pazemes dzelzsbetona glabātavas, Rosengrens aprīkojums, bruņotas durvis, vibrācijas detektori, video novērošana un diennakts bruņota apsardze."),
        ("Kas notiek, ja pazaudēju atslēgu vai PIN?", "PIN var atjaunot pēc atkārtotas identifikācijas. Pazaudētas atslēgas gadījumā seifu atver speciālists; jaunās slēdzenes un atslēgu izmaksas sedz klients."),
        ("Kas notiek ar manu seifu uzņēmuma maksātnespējas gadījumā?", "Seifa saturs paliek jūsu īpašums un nav uzņēmuma manta, tāpēc tas ir aizsargāts."),
        ("Vai varu rezervēt seifu attālināti?", "Seifu var rezervēt pa tālruni vai e-pastu, taču PIN izsniegšanai un atslēgu saņemšanai nepieciešama klātbūtne."),
        ("Vai varu dot piekļuvi citai personai?", "Jā, nododot atslēgas, seifa numuru un PIN savam pārstāvim."),
    ],
    "ru": [
        ("Нужно ли открывать банковский счёт?", "Нет. Мы не банк — договор подписывается на месте за 10 минут, без банковских процедур."),
        ("Кто знает, что лежит в моей ячейке?", "Только вы. Мы не проверяем и не регистрируем содержимое. Ключи только у вас, наши сотрудники не имеют доступа к содержимому."),
        ("Что можно и что нельзя хранить?", "Можно: валюту, драгметаллы, украшения, ценные бумаги, документы, антиквариат, искусство, носители данных. Нельзя: легковоспламеняющиеся, взрывоопасные, токсичные, радиоактивные вещества и оружие."),
        ("Какой минимальный срок аренды?", "1 месяц. При долгосрочных договорах (12–24 месяца) месячная ставка значительно ниже."),
        ("Можно ли попасть к ячейке вне рабочего времени?", "Да — вечерние визиты и доступ 24/7 возможны по предварительной договорённости."),
        ("Насколько надёжны ваши сейфы?", "Два подземных железобетонных хранилища, оборудование Rosengrens, бронедвери, детекторы вибрации, видеонаблюдение и круглосуточная вооружённая охрана."),
        ("Что если я потеряю ключ или PIN?", "PIN можно восстановить после повторной идентификации. При потере ключа сейф открывает специалист; стоимость нового замка и ключей оплачивает клиент."),
        ("Что будет с ячейкой при банкротстве компании?", "Содержимое ячейки остаётся вашей собственностью и не является имуществом компании, поэтому оно защищено."),
        ("Можно ли забронировать сейф удалённо?", "Сейф можно забронировать по телефону или эл. почте, но для выдачи PIN и получения ключей нужно личное присутствие."),
        ("Можно ли дать доступ другому человеку?", "Да, передав ключи, номер ячейки и PIN своему представителю."),
    ],
    "en": [
        ("Do I need to open a bank account?", "No. We are not a bank — the agreement is signed on site in 10 minutes, with no banking procedures."),
        ("Who knows what is in my box?", "Only you. We do not inspect or register the contents. You hold the keys, and our staff cannot access the contents."),
        ("What can and cannot be stored?", "Allowed: currency, precious metals, jewellery, securities, documents, antiques, art, data media. Not allowed: flammable, explosive, toxic, radioactive substances and weapons."),
        ("What is the minimum rental term?", "1 month. Long-term agreements (12–24 months) come with a significantly lower monthly rate."),
        ("Can I access my box outside business hours?", "Yes — evening visits and 24/7 access are available by prior arrangement."),
        ("How secure are your boxes?", "Two underground reinforced-concrete vaults, Rosengrens equipment, armoured doors, vibration detectors, video recording and round-the-clock armed security."),
        ("What if I lose my key or PIN?", "A PIN can be restored after re-identification. If a key is lost, a specialist opens the box; the cost of a new lock and keys is borne by the client."),
        ("What happens to my box if the company goes insolvent?", "The contents remain your property and are not company assets, so they are protected."),
        ("Can I reserve a box remotely?", "A box can be reserved by phone or email, but issuing the PIN and handing over the keys require your presence."),
        ("Can I give access to another person?", "Yes, by giving the keys, box number and PIN to your representative."),
    ],
}

# Blog: planned article titles (stubs for now) per language
BLOG = {
    "lv": {"intro": "Padomi par vērtslietu glabāšanu un seifu nomu. Pirmie raksti drīzumā.",
           "soon": "Drīzumā", "posts": ["Ko glabāt sefa jeb seifa janā", "Seifa jeb sefs mājās vai privātā glabātavā?",
            "Bankas jeb privātais seifs: kāda atšķirība?", "Kā pasargāt dokumentus ugunsgrēka gadījumā",
            "Ko nedrīkst glabāt mājās", "Kā nomāt seifu Rīgā"]},
    "ru": {"intro": "Советы о хранении ценностей и аренде сейфа. Первые статьи скоро.",
           "soon": "Скоро", "posts": ["Что хранить в сейфовой ячейке", "Сейф дома или в частном хранилище?",
            "Банковский или частный сейф: в чём разница?", "Как защитить документы при пожаре",
            "Что нельзя хранить дома", "Как арендовать сейф в Риге"]},
    "en": {"intro": "Guides on storing valuables and renting a safe deposit box. First articles coming soon.",
           "soon": "Soon", "posts": ["What to store in a safe deposit box", "A safe at home or in a private vault?",
            "Bank vs private safe: what is the difference?", "How to protect documents in a fire",
            "What you should not keep at home", "How to rent a safe deposit box in Riga"]},
}

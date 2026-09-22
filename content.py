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
    "address": "Kaļķu iela 26, Rīga",
    "maps_q": "Ka%C4%BC%C4%B7u%20iela%2026%2C%20R%C4%ABga",
    "postcode": "LV-1050",
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
        "lbl_address": "Adrese", "lbl_phone": "Tālrunis", "lbl_email": "E-pasts",
    },
    "ru": {
        "nav": {"boxes": "Ячейки и цены", "security": "Безопасность", "services": "Услуги",
                "about": "О компании", "faq": "FAQ", "contacts": "Контакты"},
        "book": "Забронировать", "menu": "Меню", "lang_name": "Русский",
        "cta_book": "Забронировать ячейку", "cta_prices": "Узнать цены", "cta_call": "Позвонить",
        "cta_route": "Маршрут", "cta_wa": "Написать в WhatsApp", "cta_more": "Узнать подробнее",
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
        "lbl_address": "Адрес", "lbl_phone": "Телефон", "lbl_email": "Эл. почта",
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
        "lbl_address": "Address", "lbl_phone": "Phone", "lbl_email": "Email",
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
                "Izvēlieties izmēru, parakstiet līgumu 10 minūtēs un glabājiet droši. Bez bankas konta atvēršanas. Reģistrēts un anonīms klients.",
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
        "contacts": ("Kontakti un adrese — Kaļķu iela 26, Vecrīga | Rīgas Seifi",
                     "Rīgas Seifi: Kaļķu iela 26, Vecrīga. Tālrunis, WhatsApp, e-pasts, karte un darba laiks. Rezervējiet seifu jau šodien.",
                     "Rīgas Seifi kontakti, seifu noma adrese, Kaļķu iela, Vecrīga"),
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
                "Выберите размер, подпишите договор за 10 минут и храните спокойно. Без открытия банковского счёта. Два уровня конфиденциальности на выбор.",
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
        "contacts": ("Контакты и адрес — Kaļķu iela 26, Старая Рига | Rīgas Seifi",
                     "Rīgas Seifi: Kaļķu iela 26, Старая Рига. Телефон, WhatsApp, эл. почта, карта и часы работы. Забронируйте сейф сегодня.",
                     "Rīgas Seifi контакты, аренда сейфа адрес, Kaļķu iela, Старая Рига"),
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
                "Choose a size, sign the agreement in 10 minutes and store with confidence. No bank account needed. Registered and anonymous clients.",
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
        "contacts": ("Contacts & Location — Kaļķu iela 26, Old Riga | Rīgas Seifi",
                     "Rīgas Seifi: Kaļķu iela 26, Old Riga. Phone, WhatsApp, email, map and opening hours. Book your safe deposit box today.",
                     "rigas seifi contacts, safe deposit address, kalku street, old riga"),
        "blog": ("Blog & guides — storing valuables | Rīgas Seifi",
                 "Guides on safely storing valuables and documents, renting a safe deposit box and how private vaults differ from banks.",
                 "storing valuables, what to keep in a safe, bank vs private safe"),
    },
}

# =====================================================================
#  Reusable content blocks (advantages, steps, security points, trust)
# =====================================================================
STEPS = {
    "lv": [("Izvēlieties izmēru", "Palīdzēsim atrast piemērotāko — tiešsaistē, pa tālruni vai uz vietas."),
           ("Parakstiet līgumu", "10 minūtes uz vietas. Divi reģistrācijas veidi — izvēlieties sev piemēroto konfidencialitātes līmeni."),
           ("Jūsu vērtslietas ir apsargātas", "Piekļuve darba laikā, vakaros un 24/7 — pēc vienošanās.")],
    "ru": [("Выберите размер", "Поможем подобрать оптимальный — онлайн, по телефону или на месте."),
           ("Подпишите договор", "10 минут на месте. Два варианта регистрации — выберите уровень конфиденциальности, который вам подходит."),
           ("Ваши ценности под охраной", "Доступ в рабочее время, вечером и 24/7 — по договорённости.")],
    "en": [("Choose a size", "We will help you pick the right one — online, by phone or on site."),
           ("Sign the agreement", "10 minutes on site. Two registration options — choose the level of confidentiality that suits you."),
           ("Your valuables are guarded", "Access during business hours, evenings and 24/7 — by arrangement.")],
}

# Security section on the home page: the vault, then the three levels that
# protect access to every box. They are the guard's mechanical key, the
# client's mechanical key and the electronic PIN. There is no time-delay lock;
# an earlier draft listed a "lock timer", which the business corrected.
# **double asterisks** render as bold.
SECGROUPS = {
    "lv": [
        ("Glabātava", [
            "Divas pazemes dzelzsbetona glabātavas — vairāk nekā 100 m²",
            "Izolētas telpas: **iekļūšana caur sienām nav iespējama**",
            "Rosengrens aprīkojums (Zviedrija, dibināta 1886. gadā)",
            "Trokšņa un vibrācijas detektori sienās",
            "Video novērošana un ugunsdrošības sistēma",
            "Diennakts bruņota apsardze SP Leģions ar ātrās reaģēšanas vienību"]),
        ("Piekļuve seifam — trīs aizsardzības līmeņi", [
            "Apsardzes mehāniskā atslēga — atrodas glabātavā",
            "Jūsu mehāniskā atslēga — tiek izsniegta tikai jums",
            "Elektroniskais PIN kods — AES šifrēšana, 100 000 000 kombināciju. Pēc 3 kļūdainiem mēģinājumiem — automātiska bloķēšana"]),
    ],
    "ru": [
        ("Хранилище", [
            "Два подземных железобетонных хранилища — более 100 м²",
            "Изолированные помещения: **проникновение через стены исключено**",
            "Оборудование Rosengrens (Швеция, основана в 1886 году)",
            "Детекторы шума и вибрации в стенах",
            "Видеонаблюдение и система пожарной безопасности",
            "Круглосуточная вооружённая охрана SP Leģions с группой быстрого реагирования"]),
        ("Доступ в ячейку защищён тремя уровнями", [
            "Механический ключ охраны — находится в хранилище",
            "Ваш механический ключ — выдаётся только вам",
            "Электронный PIN-код — AES-шифрование, 100 000 000 комбинаций. После 3 неверных попыток — автоматическая блокировка"]),
    ],
    "en": [
        ("The vault", [
            "Two underground reinforced-concrete vaults — over 100 m²",
            "Isolated rooms: **breaking in through the walls is ruled out**",
            "Rosengrens equipment (Sweden, founded in 1886)",
            "Noise and vibration detectors inside the walls",
            "Video surveillance and a fire-safety system",
            "Round-the-clock armed security by SP Leģions with a rapid-response team"]),
        ("Three levels protect access to every box", [
            "The guard's mechanical key — kept at the vault",
            "Your mechanical key — issued to you alone",
            "Electronic PIN — AES encryption, 100,000,000 combinations. After 3 wrong attempts — an automatic lockout"]),
    ],
}

# Security page only: the same three levels spelled out row by row.
SECLOCKS = {
    "lv": [
        ("Apsardzes mehāniskā atslēga", "Pirmā atslēga atrodas pie glabātavas apsardzes un ir vajadzīga katrā seifa atvēršanas reizē."),
        ("Jūsu mehāniskā atslēga", "Otro atslēgu saņemat tikai jūs. Seifs atveras ar abām atslēgām kopā."),
        ("Elektroniskais PIN kods", "PIN ar AES šifrēšanu un aizsardzību pret koda pārtveršanu. 100 000 000 kombināciju. Pēc 3 kļūdainiem mēģinājumiem — bloķēšana uz 5 minūtēm, pēc tam ilgāk."),
    ],
    "ru": [
        ("Механический ключ охраны", "Первый ключ находится у охраны хранилища и нужен при каждом открытии ячейки."),
        ("Ваш механический ключ", "Второй ключ выдаётся только вам. Ячейка открывается двумя ключами вместе."),
        ("Электронный PIN-код", "PIN с AES-шифрованием и защитой от перехвата кода. 100 000 000 комбинаций. После 3 неверных попыток — блокировка на 5 минут, затем дольше."),
    ],
    "en": [
        ("The guard's mechanical key", "The first key stays with the vault's security staff and is needed every time a box is opened."),
        ("Your mechanical key", "The second key is issued to you alone. The box opens with both keys together."),
        ("Electronic PIN", "An AES-encrypted PIN with protection against code interception. 100,000,000 combinations. After 3 wrong attempts — a 5-minute lockout, then longer."),
    ],
}

# Confidentiality block (home page)
PRIVACY = {
    "lv": {"body": "Bez bankas konta atvēršanas. Seifa saturu zina tikai jūs — mēs to nepārbaudām un nereģistrējam. Pirmajā apmeklējumā nepieciešams tikai personu apliecinošs dokuments.",
           "note": "Klienti, kuri izvēlas paaugstinātu konfidencialitātes līmeni (bez reģistrācijas), seifu nomā pēc individuāla tarifa."},
    "ru": {"body": "Без открытия банковского счёта. Содержимое ячейки известно только вам — мы его не проверяем и не регистрируем. При первом визите потребуется только документ, удостоверяющий личность.",
           "note": "Клиенты, выбирающие повышенный уровень конфиденциальности (без регистрации), арендуют ячейки по индивидуальному тарифу."},
    "en": {"body": "No bank account required. Only you know what is in your box — we do not inspect or register the contents. At your first visit all you need is an identity document.",
           "note": "Clients who choose the higher level of confidentiality (no registration) rent their boxes at an individual rate."},
}

CERTS = {
    "lv": "Sertifikāti: EN 1300 C klase · BSI · ECB·S",
    "ru": "Сертификаты: EN 1300 класс C · BSI · ECB·S",
    "en": "Certificates: EN 1300 class C · BSI · ECB·S",
}

# "Why clients choose us" — intro + cards (icon, title, body)
TRUST = {
    "lv": {
        "intro": "Bankas Latvijā un visā pasaulē pakāpeniski atsakās no seifu nomas. Mēs strādājam kopš 2017. gada un kļuvām par pirmo privāto glabātavu Baltijā tieši tāpēc, ka redzam šo vajadzību: cilvēkiem un uzņēmumiem ir vajadzīga droša vieta vērtslietām — bez banku ierobežojumiem, rindām un darba laika.",
        "cards": [
            ("shield", "Kopš 2017. gada", "Atvērāmies brīdī, kad bankas sāka slēgt seifu nodaļas. Šodien — lielākā privātā glabātava Baltijā."),
            ("box", "3000+ seifu, pieci izmēri", "No plānas dokumentu mapes līdz lielām vērtslietām un mākslas darbiem."),
            ("lock", "Bez banku ierobežojumiem", "Nekādu kontu, izziņu un bankas darba laika. Jūsu piekļuve — pēc jūsu grafika."),
            ("users", "1000+ klientu 9 gados", "Privātpersonas, uzņēmumi, notāri, nekustamā īpašuma darījumu dalībnieki — uztic mums to, ko negribas pazaudēt."),
            ("deal", "Deal Box", "Rīgas Seifi ir neitrāls darījuma garants — atslēgas tiek izsniegtas tikai tad, kad izpildīti līguma nosacījumi."),
            ("truck", "Apsargāts transfērs", "Organizējam drošu vērtslietu piegādi uz glabātavu vai mājās — nosacījumus saskaņojam individuāli."),
            ("room", "Sarunu telpa", "Konfidenciāla telpa dokumentu parakstīšanai turpat glabātavā. Bez video novērošanas iekšpusē."),
        ],
    },
    "ru": {
        "intro": "Банки в Латвии и по всему миру сворачивают услугу сейфовых ячеек. Мы работаем с 2017 года и стали первым частным хранилищем в Балтии именно потому, что видим эту потребность: людям и бизнесу нужно надёжное место для ценностей — без банковских ограничений, очередей и графика.",
        "cards": [
            ("shield", "С 2017 года", "Открылись, когда банки начали закрывать сейфовые отделения. Сегодня — крупнейшее частное хранилище в Балтии."),
            ("box", "3000+ ячеек, пять размеров", "От тонкой папки с документами до крупных ценностей и предметов искусства."),
            ("lock", "Без банковских ограничений", "Никаких счетов, справок и графика работы банка. Ваш доступ — по вашему расписанию."),
            ("users", "1000+ клиентов за 9 лет", "Частные лица, компании, нотариусы, участники сделок с недвижимостью — доверяют нам то, что не хочется потерять."),
            ("deal", "Deal Box", "Rīgas Seifi выступает нейтральным гарантом сделки — ключи выдаются только при выполнении условий договора."),
            ("truck", "Охраняемый трансфер", "Организуем безопасную доставку ценностей до хранилища или домой — условия индивидуально."),
            ("room", "Переговорная комната", "Конфиденциальное пространство для подписания документов прямо в хранилище. Без видеонаблюдения внутри."),
        ],
    },
    "en": {
        "intro": "Banks in Latvia and around the world are winding down safe deposit services. We have been working since 2017 and became the first private vault in the Baltics precisely because we see the need: people and businesses want a reliable place for their valuables — without bank restrictions, queues or opening hours.",
        "cards": [
            ("shield", "Since 2017", "We opened when banks started closing their safe deposit departments. Today we are the largest private vault in the Baltics."),
            ("box", "3,000+ boxes, five sizes", "From a slim folder of documents to large valuables and works of art."),
            ("lock", "No banking restrictions", "No accounts, no certificates, no banking hours. Your access runs on your schedule."),
            ("users", "1,000+ clients in 9 years", "Private individuals, companies, notaries and parties to property deals trust us with what they would rather not lose."),
            ("deal", "Deal Box", "Rīgas Seifi acts as the neutral guarantor of a transaction — the keys are released only once the terms of the agreement are met."),
            ("truck", "Guarded transfer", "We arrange secure delivery of valuables to the vault or to your home — terms agreed individually."),
            ("room", "Meeting room", "A confidential space for signing documents right inside the vault. No video surveillance inside."),
        ],
    },
}

# =====================================================================
#  PHOTOS  —  slot -> file in assets/img/photos/ + alt text per language.
#  The hero shows the façade of Kaļķu iela 26, so a first-time visitor sees
#  the building before the vault (asked for in the September 2026 review).
#  Source: the 28 August 2026 shoot of the Kaļķu iela 26 premises
#  (127 frames). Everything here is a full-resolution frame from that
#  shoot, resized for the web, except "about1", which is captioned
#  "the first vault" and therefore still uses the 400px archive preview
#  of the old premises — the 2026 shoot covers the new vault only.
#  Drop a slot from this dict and that panel falls back to the
#  "photo goes here" panel automatically.
# =====================================================================
PHOTOS = {
    "hero": {"file": "riga-centre.jpg",  # frame 13, the K26 façade
             "pos": "66% 50%",  # the K26 building sits right of centre in the frame
             "lv": "Ēka Kaļķu ielā 26 Vecrīgā",
             "ru": "Здание на Kaļķu iela 26 в Старой Риге",
             "en": "The building at Kaļķu iela 26 in Old Riga"},
    "step1": {"file": "box-sizes.jpg",  # frame 126,
             "lv": "Pieci seifu izmēri blakus — no mazākā līdz lielākajam",
             "ru": "Пять размеров ячеек рядом — от меньшего к большему",
             "en": "The five box sizes side by side, smallest to largest"},
    "step2": {"file": "signing-office.jpg",  # frame 76,
             "lv": "Birojs, kurā tiek parakstīts līgums",
             "ru": "Кабинет, где подписывается договор",
             "en": "The office where the agreement is signed"},
    "step3": {"file": "box-open.jpg",  # frame 122,
             "lv": "Atvērts seifs ar izvilktu kasti",
             "ru": "Открытая ячейка с выдвинутым лотком",
             "en": "An open safe deposit box with its tray drawn out"},
    # Archive frame of the OLD premises, and the caption ("the first vault")
    # calls for exactly that. Replace only if a better shot of the 2017
    # vault turns up.
    "about1": {"file": "vault-first.jpg",
             "lv": "Pirmā glabātava — telpa ar seifu rindām",
             "ru": "Первое хранилище — помещение с рядами ячеек",
             "en": "The first vault, with its rows of boxes"},
    "about2": {"file": "vault-rows.jpg",  # frame 113,
             "lv": "Seifu rindas jaunajā glabātavā Kaļķu ielā 26",
             "ru": "Ряды ячеек в новом хранилище на Kaļķu iela 26",
             "en": "Rows of boxes in the new vault at Kaļķu iela 26"},
}

# =====================================================================
#  SECURITY_SHOTS  —  the four-up photo block beside the security copy on
#  the home and security pages. It used to be a single panel with a play
#  button over it, reserved for a security video that was never filmed.
#  The four shots follow the copy beside them: the vault, the mechanical
#  key, the electronic PIN, and the boxes. Empty this list and the block
#  falls back to the "photo goes here" panel.
# =====================================================================
SECURITY_SHOTS = [
    {"file": "vault-door.jpg",  # frame 89
     "lv": "Atvērtas bruņotās glabātavas durvis, aiz tām seifi",
     "ru": "Открытая бронированная дверь хранилища, за ней ячейки",
     "en": "The armoured vault door standing open, with the boxes behind it"},
    {"file": "certificate-and-keys.jpg",  # frame 66, pre-cropped to 4:5 so both keys stay in frame
     "lv": "Klienta apliecība ar seifa slēdzenes cilindru un abām atslēgām",
     "ru": "Клиентское свидетельство с цилиндром замка ячейки и двумя ключами",
     "en": "A client certificate with a box lock cylinder and its two keys"},
    {"file": "pin-terminal.jpg",  # frame 65
     "lv": "PIN ievades terminālis piekļuvei seifam",
     "ru": "Терминал ввода PIN для доступа к ячейке",
     "en": "The PIN terminal used to reach a box"},
    {"file": "box-locks.jpg",  # frame 112
     "lv": "Seifu rindas ar misiņa slēdzenēm",
     "ru": "Ряды ячеек с латунными замками",
     "en": "Rows of boxes with their brass locks"},
]

# =====================================================================
#  ARRIVAL  —  the photo strip on the contacts page. Four shots in the
#  order a visitor meets them, being the building, the street, the door
#  plate with the intercom, and the sign with the opening hours. Each alt
#  text doubles as the visible caption. Empty "shots" and the whole block
#  disappears.
# =====================================================================
ARRIVAL = {
    "heading": {"lv": "Kā mūs atrast",
                "ru": "Как нас найти",
                "en": "Finding us"},
    "sub": {"lv": "Ko meklēt, kad esat klāt.",
            "ru": "На что обратить внимание по прибытии.",
            "en": "What to look for when you arrive."},
    "shots": [
        {"file": "riga-centre.jpg",  # frame 13
         "lv": "Ēka Kaļķu ielā 26",
         "ru": "Здание на Kaļķu iela 26",
         "en": "The building at Kaļķu iela 26"},
        {"file": "street-kalku.jpg",  # frame 16
         "lv": "Kaļķu iela, kur atrodas ieeja",
         "ru": "Улица Kaļķu iela, где находится вход",
         "en": "Kaļķu iela, the street the entrance is on"},
        {"file": "door-plate.jpg",  # frame 29
         "lv": "Ieejas domofons un Rīgas Seifi durvju plāksne",
         "ru": "Домофон у входа и табличка Rīgas Seifi",
         "en": "The entry intercom and the Rīgas Seifi door plate"},
        {"file": "opening-hours.jpg",  # frame 50
         "lv": "Rīgas Seifi izkārtne ar darba laiku",
         "ru": "Вывеска Rīgas Seifi с часами работы",
         "en": "The Rīgas Seifi sign with the opening hours"},
    ],
}

# Partners (logo file in assets/img/, or None until the logo is supplied).
# The Safe Deposit Federation used to sit in this row. Rīgas Seifi is a
# member, so it now has its own block (MEMBERSHIP, below).
PARTNERS = [
    {"name": "Money Express", "url": "https://www.moneyexpress.lv/", "logo": "partner-money-express.svg"},
    {"name": "SP Leģions", "url": "https://legions.lv/", "logo": "partner-sp-legions.png"},
]

# =====================================================================
#  MEMBERSHIP  —  Rīgas Seifi is a member of the Safe Deposit Federation.
#  Shown at the top of the partners section (home, security, about) and in
#  the LocalBusiness schema as memberOf. The federation's own member list
#  names Rīgas Seifi under Latvia (checked 22 September 2026), and the
#  block links to it so a visitor can verify the claim.
#  "certificate": the scan of the membership certificate, as a file in
#  assets/img/ (e.g. "sdf-certificate.jpg"). While it is None the block
#  shows the federation's logo; once set, it shows the certificate and
#  opens it full size on click.
# =====================================================================
MEMBERSHIP = {
    "name": "Safe Deposit Federation",
    "url": "https://safedepositfederation.com/",
    "members_url": "https://safedepositfederation.com/members/",
    "logo": "partner-sdf.png",
    "certificate": None,
    "label": {"lv": "Dalība", "ru": "Членство", "en": "Membership"},
    "heading": {"lv": "Safe Deposit Federation biedrs",
                "ru": "Член Safe Deposit Federation",
                "en": "Member of the Safe Deposit Federation"},
    "body": {"lv": "Rīgas Seifi ir starptautiskās seifu glabātavu federācijas Safe Deposit Federation biedrs. Dalību apliecina federācijas izsniegts sertifikāts.",
             "ru": "Rīgas Seifi является членом международной федерации сейфовых хранилищ Safe Deposit Federation. Членство подтверждено сертификатом федерации.",
             "en": "Rīgas Seifi is a member of the Safe Deposit Federation, the international federation of safe deposit vaults. The federation has issued a certificate confirming the membership."},
    "link": {"lv": "Rīgas Seifi federācijas biedru sarakstā",
             "ru": "Rīgas Seifi в списке членов федерации",
             "en": "Rīgas Seifi in the federation's member list"},
    "cert_alt": {"lv": "Safe Deposit Federation biedra sertifikāts, izsniegts Rīgas Seifi",
                 "ru": "Сертификат члена Safe Deposit Federation, выданный Rīgas Seifi",
                 "en": "Safe Deposit Federation membership certificate issued to Rīgas Seifi"},
}

# =====================================================================
#  VIDEO  —  the video section on the home page, between "Why us" and
#  the prices. Fill ONE of the two sources when the video is ready:
#    "file"  — an .mp4 in assets/video/ (keep it under ~50 MB; GitHub
#              Pages refuses files over 100 MB), or
#    "embed" — a YouTube or Vimeo embed URL, e.g.
#              "https://www.youtube-nocookie.com/embed/VIDEO_ID".
#  While both are empty the section shows the poster with a "coming soon"
#  note. "show": False hides the whole section.
# =====================================================================
VIDEO = {
    "show": True,
    "file": "",
    "embed": "",
    "poster": "vault-aisle.jpg",  # frame 116, the vault aisle that used to be the hero
    "heading": {"lv": "Video par Rīgas Seifi",
                "ru": "Видео о Rīgas Seifi",
                "en": "Rīgas Seifi on video"},
    "soon": {"lv": "Video drīzumā",
             "ru": "Видео скоро появится",
             "en": "Video coming soon"},
    "title": {"lv": "Rīgas Seifi video", "ru": "Видео Rīgas Seifi", "en": "Rīgas Seifi video"},
}

# =====================================================================
#  REQUISITES  —  company details on the contacts page.
#  Source: the Latvian Register of Enterprises, via company.lursoft.lv and
#  firmas.lv, checked 22 September 2026. The registered address there is
#  still Ģertrūdes iela 33/35 (the old premises), which is why it differs
#  from the visiting address. The company is not in the VAT register
#  (excluded 3 June 2025), so no VAT number is shown.
#  Rows with an empty value are skipped, so the bank rows appear as soon
#  as they are filled in.
# =====================================================================
REQUISITES = {
    "heading": {"lv": "Uzņēmuma rekvizīti", "ru": "Реквизиты компании", "en": "Company details"},
    "rows": [
        ({"lv": "Nosaukums", "ru": "Название", "en": "Company name"}, 'AS "Rīgas seifi"'),
        ({"lv": "Reģistrācijas numurs", "ru": "Регистрационный номер", "en": "Registration number"}, "40203055925"),
        ({"lv": "Juridiskā adrese", "ru": "Юридический адрес", "en": "Registered address"}, "Ģertrūdes iela 33/35-1, Rīga, LV-1011"),
        ({"lv": "Banka", "ru": "Банк", "en": "Bank"}, ""),
        ({"lv": "Konta numurs (IBAN)", "ru": "Номер счёта (IBAN)", "en": "Account number (IBAN)"}, ""),
        ({"lv": "SWIFT", "ru": "SWIFT", "en": "SWIFT"}, ""),
    ],
}

# hero per language: eyebrow, title, subtitle, 4 stats (value,label)
HERO = {
    "lv": {"eyebrow": "Pirmā privātā seifu glabātava Baltijā",
           "title": "Seifu glabātava pašā Rīgas centrā",
           "sub": "Vērtīgākais — trīskāršā aizsardzībā. Noformēšana 10 minūtēs. 100 % konfidencialitāte. No €30 mēnesī.",
           "stats": [("3000+", "seifu"), ("2", "pazemes glabātavas"), ("24/7", "piekļuve pēc vienošanās"), ("2017", "strādājam kopš")]},
    "ru": {"eyebrow": "Первое частное сейфовое хранилище в Балтии",
           "title": "Сейфовое хранилище в самом центре Риги",
           "sub": "Самое ценное под тройной защитой. Оформление за 10 минут. 100 % конфиденциальность. От €30 в месяц.",
           "stats": [("3000+", "ячеек"), ("2", "подземных хранилища"), ("24/7", "доступ по договорённости"), ("2017", "работаем с")]},
    "en": {"eyebrow": "The first private safe depository in the Baltics",
           "title": "A safe deposit vault in the very centre of Riga",
           "sub": "Your most valuable things under triple protection. Paperwork in 10 minutes. 100 % confidentiality. From €30 a month.",
           "stats": [("3000+", "deposit boxes"), ("2", "underground vaults"), ("24/7", "access by arrangement"), ("2017", "operating since")]},
}

# section headings used across pages
H = {
    "lv": {"sizes": "Seifu izmēri un cenas",
           "sizes_sub": "Atklātas cenas bez slēptiem maksājumiem. Jo ilgāks nomas termiņš, jo zemāka mēneša maksa.",
           "how": "Kā tas notiek", "security": "Drošība bez kompromisiem",
           "trust": "Kāpēc mūs izvēlējušies 1000+ klientu 9 gados",
           "partners": "Mūsu partneri", "privacy": "Konfidencialitāte",
           "extras": "Papildpakalpojumi un tarifi",
           "extras_note": "Visas cenas norādītas ar PVN, izņemot atslēgu drošības depozītu.",
           "dealbox": "The Deal Box — kā tas notiek",
           "dealbox_note": "Ideāli piemērots nekustamā īpašuma darījumiem, biznesa partnerībām un jebkurai vienošanās, kurai vajadzīgs neitrāls garants.",
           "location": "Adrese un darba laiks", "faq": "Biežāk uzdotie jautājumi", "services": "Mūsu pakalpojumi",
           "book": "Rezervējiet seifu jau šodien",
           "book_sub": "Noskaidrojiet, vai vajadzīgais izmērs ir pieejams, un rezervējiet to vienā ziņā.",
           "price_note": "Norādīti tarifi reģistrētiem klientiem ar 12 mēnešu līgumu. Pieejami arī 1 un 24 mēnešu termiņi. Minimālais termiņš — 1 mēnesis.",
           "table_size": "Izmērs", "table_dim": "Izmēri (A×P×Dz)", "table_fits": "Kas ietilpst", "table_m1": "1 mēn.", "table_m12": "12 mēn.", "table_m24": "24 mēn.",
           "table_service": "Pakalpojums", "table_price": "Cena"},
    "ru": {"sizes": "Размеры и цены ячеек",
           "sizes_sub": "Прозрачные цены без скрытых платежей. Чем дольше срок аренды, тем ниже месячная ставка.",
           "how": "Как это работает", "security": "Безопасность без компромиссов",
           "trust": "Почему нас выбрали 1000+ клиентов за 9 лет",
           "partners": "Наши партнёры", "privacy": "Конфиденциальность",
           "extras": "Дополнительные услуги и тарифы",
           "extras_note": "Все цены указаны с НДС, кроме гарантийного депозита за ключи.",
           "dealbox": "The Deal Box — как это работает",
           "dealbox_note": "Идеально для сделок с недвижимостью, бизнес-партнёрств и любых договорённостей, требующих нейтрального гаранта.",
           "location": "Адрес и часы работы", "faq": "Частые вопросы", "services": "Наши услуги",
           "book": "Забронируйте ячейку сегодня",
           "book_sub": "Уточните наличие нужного размера и оформите бронь за одно сообщение.",
           "price_note": "Указаны тарифы для зарегистрированных клиентов при договоре на 12 месяцев. Доступны также сроки 1 и 24 месяца. Минимальный срок — 1 месяц.",
           "table_size": "Размер", "table_dim": "Размеры (В×Ш×Г)", "table_fits": "Что помещается", "table_m1": "1 мес.", "table_m12": "12 мес.", "table_m24": "24 мес.",
           "table_service": "Услуга", "table_price": "Стоимость"},
    "en": {"sizes": "Box sizes and prices",
           "sizes_sub": "Transparent pricing with no hidden fees. The longer the rental term, the lower the monthly rate.",
           "how": "How it works", "security": "Security without compromise",
           "trust": "Why 1,000+ clients have chosen us in 9 years",
           "partners": "Our partners", "privacy": "Confidentiality",
           "extras": "Additional services and fees",
           "extras_note": "All prices include VAT, except the key guaranty deposit.",
           "dealbox": "The Deal Box — how it works",
           "dealbox_note": "Ideal for property transactions, business partnerships and any agreement that needs a neutral guarantor.",
           "location": "Location and opening hours", "faq": "Frequently asked questions", "services": "Our services",
           "book": "Book your box today",
           "book_sub": "Check that the size you need is available and book it in a single message.",
           "price_note": "Rates shown are for registered clients on a 12-month agreement. 1 and 24-month terms are also available. Minimum term — 1 month.",
           "table_size": "Size", "table_dim": "Dimensions (H×W×D)", "table_fits": "What fits", "table_m1": "1 mo", "table_m12": "12 mo", "table_m24": "24 mo",
           "table_service": "Service", "table_price": "Price"},
}

# Additional services price list (boxes page). VAT included except the key deposit.
EXTRAS = {
    "lv": [
        ("Drošības depozīts par izsniegtajām atslēgām (bez PVN)", "€150"),
        ("Atslēgas vai slēdzenes mehānisma nozaudēšana vai bojājums", "€150"),
        ("Piespiedu seifa atvēršana", "€150"),
        ("PIN koda maiņa", "€20"),
        ("Individuāls apmeklējuma laiks", "€200"),
        ("Deal Box — līguma par īpašu kārtību noslēgšana", "€500"),
        ("Deal Box — līguma grozījumi", "€50"),
        ("Business Room, stundā", "€50"),
        ("Nomas termiņa kavējums", "Dubultā likme, proporcionāli dienām"),
    ],
    "ru": [
        ("Гарантийный депозит за выданные ключи (без НДС)", "€150"),
        ("Потеря, порча ключа или механизма замка", "€150"),
        ("Вынужденное вскрытие ячейки", "€150"),
        ("Смена PIN-кода", "€20"),
        ("Индивидуальное время посещения", "€200"),
        ("Deal Box — заключение договора об особом порядке", "€500"),
        ("Deal Box — изменение договора", "€50"),
        ("Business Room, за час", "€50"),
        ("Просрочка аренды", "Двойной тариф, пропорционально дням"),
    ],
    "en": [
        ("Guaranty deposit for issued keys (excl. VAT)", "€150"),
        ("Loss or damage of a key or lock mechanism", "€150"),
        ("Forced opening of a box", "€150"),
        ("PIN change", "€20"),
        ("Individual visiting time", "€200"),
        ("Deal Box — signing the special-terms agreement", "€500"),
        ("Deal Box — amending the agreement", "€50"),
        ("Business Room, per hour", "€50"),
        ("Late rental payment", "Double rate, pro rata per day"),
    ],
}

# The Deal Box, step by step (services page)
DEALBOX = {
    "lv": [
        "Puses nomā seifu un slēdz trīspusēju līgumu ar Rīgas Seifi — tajā tiek fiksēti darījuma nosacījumi.",
        "Puses ievieto darījuma priekšmetu seifā. Atslēgas tiek aizzīmogotas numurētā aploksnē un nodotas Rīgas Seifi.",
        "Rīgas Seifi darbojas kā garants: atslēgas glabājas pie mums, līdz izpildīti līguma nosacījumi.",
        "Viena no pusēm iesniedz līgumā paredzētos dokumentus. Ja tie atbilst nosacījumiem, Rīgas Seifi izsniedz atslēgas.",
        "Ja dokumenti netiek iesniegti termiņā, atslēgas tiek nodotas pretējai pusei.",
    ],
    "ru": [
        "Стороны арендуют ячейку и заключают трёхсторонний договор с Rīgas Seifi — в нём прописываются условия сделки.",
        "Стороны помещают предмет сделки в ячейку. Ключи запечатываются в номерной конверт и передаются Rīgas Seifi.",
        "Rīgas Seifi выступает гарантом: ключи хранятся у нас до выполнения условий договора.",
        "Одна из сторон предоставляет документы согласно договору. При их соответствии Rīgas Seifi выдаёт ключи.",
        "Если документы не предоставлены в срок — ключи передаются противоположной стороне.",
    ],
    "en": [
        "The parties rent a box and sign a three-party agreement with Rīgas Seifi setting out the terms of the deal.",
        "The parties place the subject of the deal in the box. The keys are sealed in a numbered envelope and handed to Rīgas Seifi.",
        "Rīgas Seifi acts as guarantor: the keys stay with us until the terms of the agreement are met.",
        "One party submits the documents required by the agreement. If they comply, Rīgas Seifi releases the keys.",
        "If the documents are not submitted on time, the keys are handed to the opposite party.",
    ],
}
DEALBOX_STEP = {"lv": "Solis", "ru": "Шаг", "en": "Step"}

# Services page content: list of (icon, title, body)
SERVICES = {
    "lv": [
        ("box", "Seifu noma", "Vairāk nekā 3000 seifu piecos izmēros divās pazemes glabātavās. Lieliem priekšmetiem — atsevišķas glabāšanas zonas. Saturs ir stingri konfidenciāls."),
        ("clock", "24/7 piekļuve", "Standarta darba laiks: P–Pk 10:00–19:00. Piekļuve ārpus darba laika, vakaros un brīvdienās — pēc iepriekšējas vienošanās. Tiek piemēroti papildu tarifi."),
        ("deal", "The Deal Box — darījumu seifs", "Drošs veids, kā garantēt darījumu starp pusēm. Tiek slēgts trīspusējs līgums, un Rīgas Seifi tur atslēgas kā neitrāls garants — līdz izpildīti visi nosacījumi. Līguma noslēgšana €500, grozījumi €50."),
        ("truck", "Apsargāta pārvešana", "Vērtslietu pārvešana uz glabātavu un atpakaļ ar profesionālu apsardzi. Cena atkarīga no apsardzes līmeņa, transporta veida un attāluma — tiek aprēķināta individuāli."),
        ("room", "Konfidenciāla sarunu telpa", "Aprīkota telpa darījumu parakstīšanai vai konfidenciālām sarunām turpat glabātavā. Šajā telpā video novērošana netiek veikta. Noma €50 stundā, pēc iepriekšēja pieraksta."),
    ],
    "ru": [
        ("box", "Аренда сейфовых ячеек", "Более 3000 ячеек пяти размеров в двух подземных хранилищах. Для крупных предметов — отдельные зоны хранения. Содержимое строго конфиденциально."),
        ("clock", "Доступ 24/7", "Стандартные часы работы: пн–пт 10:00–19:00. Доступ вне рабочего времени, вечером и в выходные — по предварительной договорённости. Применяются дополнительные тарифы."),
        ("deal", "The Deal Box — сейф для сделок", "Надёжный способ гарантировать сделку между сторонами. Заключается трёхсторонний договор, и Rīgas Seifi держит ключи как нейтральный гарант — до выполнения всех условий. Заключение договора €500, изменение €50."),
        ("truck", "Охраняемая перевозка", "Перевозка ценностей в хранилище и обратно с профессиональной охраной. Стоимость зависит от уровня охраны, типа транспорта и расстояния — рассчитывается индивидуально."),
        ("room", "Конфиденциальная переговорная", "Оборудованное помещение для подписания сделок или конфиденциальных переговоров прямо в хранилище. Видеонаблюдение в этом помещении не ведётся. Аренда €50 в час, по предварительной записи."),
    ],
    "en": [
        ("box", "Safe deposit box rental", "Over 3,000 boxes in five sizes across two underground vaults. Dedicated storage zones for larger items. Contents stay strictly confidential."),
        ("clock", "24/7 access", "Standard hours: Mon–Fri 10:00–19:00. Access outside business hours, in the evening and at weekends by prior arrangement. Additional tariffs apply."),
        ("deal", "The Deal Box — escrow safe", "A reliable way to guarantee a transaction between parties. A three-party agreement is signed and Rīgas Seifi holds the keys as a neutral guarantor until every condition is met. Signing the agreement €500, amendments €50."),
        ("truck", "Guarded transport", "Transfer of valuables to the vault and back with professional security. The price depends on the level of protection, the vehicle and the distance — calculated individually."),
        ("room", "Confidential meeting room", "An equipped room for signing deals or holding confidential talks right inside the vault. No video surveillance is recorded in this room. €50 per hour, by prior appointment."),
    ],
}

# About page paragraphs
ABOUT = {
    "lv": {
        "lead": "Pirmā privātā seifu glabātava Baltijā — kopš 2017. gada.",
        "paras": [
            "Rīgas Seifi durvis vēra 2017. gada maijā — brīdī, kad bankas visā Eiropā sāka atteikties no seifu nomas pakalpojuma. Mēs saskatījām iespēju: piedāvāt cilvēkiem to, no kā bankas atsakās, un izdarīt to labāk.",
            "Atšķirībā no bankām mēs specializējamies tikai vienā pakalpojumā — glabāšanā. Vienkārši droša un konfidenciāla vieta tam, kas mūsu klientam ir dārgs.",
            "Astoņu gadu laikā mūs izvēlējušies vairāk nekā 1000 klientu — privātpersonas, uzņēmēji, notāri, nekustamā īpašuma darījumu dalībnieki. Cilvēki, kuri zina: ir lietas, ko negribas pazaudēt.",
            "2026. gadā mēs pārcēlāmies uz Vecrīgu. Jaunā adrese — Kaļķu iela 26 — nav tikai atrašanās vietas maiņa: modernākas telpas, pastiprināta aizsardzība un labāks serviss tiem, kas uztic mums pašu vērtīgāko.",
        ],
        "facts": [("2017", "dibināšanas gads"), ("3000+", "seifu"), ("1000+", "klientu"), ("2", "glabātavas"), ("100+ m²", "platība")],
        "photos": ["Pirmā glabātava", "Jaunās telpas Kaļķu ielā 26 — interjers, bruņotās durvis, seifi"],
    },
    "ru": {
        "lead": "Первое частное сейфовое хранилище в Балтии — с 2017 года.",
        "paras": [
            "Rīgas Seifi открылись в мае 2017 года — в тот момент, когда банки по всей Европе начали сворачивать услугу сейфовых ячеек. Мы увидели возможность: предложить людям то, от чего отказываются банки, и сделать это лучше.",
            "В отличие от банков, мы специализируемся только на одной услуге — на хранении. Просто надёжное, конфиденциальное место для того, что дорого нашему клиенту.",
            "За восемь лет нас выбрали более 1000 клиентов — частные лица, предприниматели, нотариусы, участники сделок с недвижимостью. Люди, которые знают: есть вещи, которые не хочется потерять.",
            "В 2026 году мы переехали в Старую Ригу. Новый адрес — Kaļķu iela 26 — это не просто смена локации: более современное помещение, усиленная защита и лучший сервис для тех, кто доверяет нам самое ценное.",
        ],
        "facts": [("2017", "год основания"), ("3000+", "ячеек"), ("1000+", "клиентов"), ("2", "хранилища"), ("100+ м²", "площадь")],
        "photos": ["Первое хранилище", "Новое помещение на Kaļķu iela 26 — интерьер, бронированная дверь, ячейки"],
    },
    "en": {
        "lead": "The first private safe deposit vault in the Baltics — since 2017.",
        "paras": [
            "Rīgas Seifi opened in May 2017, at the moment when banks across Europe began winding down their safe deposit services. We saw an opportunity: to offer people what the banks were giving up, and to do it better.",
            "Unlike a bank, we specialise in a single service — storage. Simply a secure, confidential place for what matters to our client.",
            "Over eight years more than 1,000 clients have chosen us — private individuals, entrepreneurs, notaries and parties to property transactions. People who know there are things they would rather not lose.",
            "In 2026 we moved to Old Riga. The new address — Kaļķu iela 26 — is more than a change of location: more modern premises, stronger protection and better service for those who trust us with their most valuable things.",
        ],
        "facts": [("2017", "year founded"), ("3,000+", "boxes"), ("1,000+", "clients"), ("2", "vaults"), ("100+ m²", "floor area")],
        "photos": ["The first vault", "The new premises at Kaļķu iela 26 — interior, armoured door, boxes"],
    },
}

# How-it-works extra content (what you need / payment / access rules)
HOWX = {
    "lv": {
        "need_t": "Kas nepieciešams", "need": ["Reģistrētam klientam — personu apliecinošs dokuments.",
            "Klientam bez reģistrācijas — dokumenti nav nepieciešami; noma pēc individuāla tarifa.", "Uzņēmumam — reģistrācijas dati un pārstāvja pilnvara."],
        "pay_t": "Apmaksa", "pay": ["Skaidrā naudā, ar karti vai pārskaitījumu.", "Atļauta trešās puses apmaksa, norādot rēķina numuru.", "Atslēgas nodrošina ar drošības depozītu (atmaksā līguma beigās)."],
        "access_t": "Piekļuve un noteikumi", "access": ["Standarta apmeklējums — līdz 15 minūtēm.", "Piekļuvei nepieciešams seifa numurs, PIN un atslēga.", "Termiņš no 1 mēneša; pagarinājums — vienkārši apmaksājot nākamo periodu."],
    },
    "ru": {
        "need_t": "Что нужно", "need": ["Зарегистрированному клиенту — документ, удостоверяющий личность.",
            "Клиенту без регистрации — документы не нужны; аренда по индивидуальному тарифу.", "Компании — регистрационные данные и доверенность представителя."],
        "pay_t": "Оплата", "pay": ["Наличными, картой или переводом.", "Допускается оплата третьим лицом с указанием номера счёта.", "Ключи обеспечиваются гарантийным депозитом (возвращается в конце аренды)."],
        "access_t": "Доступ и правила", "access": ["Стандартный визит — до 15 минут.", "Для доступа нужны номер ячейки, PIN и ключ.", "Срок от 1 месяца; продление — простой оплатой следующего периода."],
    },
    "en": {
        "need_t": "What you need", "need": ["Registered client — an identity document.",
            "Client without registration — no documents required; rental at an individual rate.", "Company — registration details and a representative's authorisation."],
        "pay_t": "Payment", "pay": ["Cash, card or bank transfer.", "Third-party payment is allowed if the invoice number is given.", "Keys are secured by a guaranty deposit (refunded at the end of the rental)."],
        "access_t": "Access and rules", "access": ["A standard visit is up to 15 minutes.", "Access requires the box number, PIN and key.", "Term from 1 month; extend simply by paying for the next period."],
    },
}

# FAQ: list of (question, answer) per language
FAQ = {
    "lv": [
        ("Vai man jāatver bankas konts?", "Nē. Līgumu noslēdzam uz vietas 10 minūtēs, bez bankas konta atvēršanas. Pie mums ir ērtāk un drošāk nekā bankā."),
        ("Kas zina, kas atrodas manā seifā?", "Tikai jūs. Mēs saturu nepārbaudām un nereģistrējam. Jūsu atslēga un PIN ir tikai pie jums, tāpēc mūsu darbinieki nevar piekļūt saturam."),
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
        ("Нужно ли открывать банковский счёт?", "Нет. Договор подписывается на месте за 10 минут, без открытия банковского счёта. У нас удобнее и безопаснее, чем в банке."),
        ("Кто знает, что лежит в моей ячейке?", "Только вы. Мы не проверяем и не регистрируем содержимое. Ваш ключ и PIN-код есть только у вас, поэтому наши сотрудники не имеют доступа к содержимому."),
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
        ("Do I need to open a bank account?", "No. The agreement is signed on site in 10 minutes, with no bank account to open. Renting from us is simpler and safer than at a bank."),
        ("Who knows what is in my box?", "Only you. We do not inspect or register the contents. Only you hold your key and PIN, so our staff cannot access the contents."),
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

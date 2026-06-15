/* ============ Rīgas Seifi — interactions (multi-page build) ============
   Pages are pre-rendered per language by build.py, so there is no
   client-side text swapping here. This handles UI behaviour only. */

/* Remember chosen language for the root redirect */
try { localStorage.setItem("lang", document.documentElement.lang || "lv"); } catch (e) {}

/* ---- Promo ribbon dismiss (re-shows automatically when the text changes) ---- */
const promoBar = document.getElementById("promoBar");
if (promoBar) {
  const key = promoBar.getAttribute("data-key");
  let dismissed = null;
  try { dismissed = localStorage.getItem("promoDismissed"); } catch (e) {}
  if (dismissed === key) promoBar.remove();
  const closeBtn = document.getElementById("promoClose");
  if (closeBtn) closeBtn.addEventListener("click", () => {
    try { localStorage.setItem("promoDismissed", key); } catch (e) {}
    promoBar.remove();
  });
}

/* ---- Mobile nav ---- */
const navToggle = document.getElementById("navToggle");
const mobileNav = document.getElementById("mobileNav");
if (navToggle && mobileNav) {
  navToggle.addEventListener("click", () => {
    const open = mobileNav.classList.toggle("open");
    navToggle.classList.toggle("open", open);
    navToggle.setAttribute("aria-expanded", open);
    document.body.classList.toggle("nav-locked", open);
  });
  mobileNav.querySelectorAll("a").forEach(a =>
    a.addEventListener("click", () => {
      mobileNav.classList.remove("open");
      navToggle.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("nav-locked");
    }));
}

/* ---- Lightweight GA4 click tracking hooks ---- */
function track(ev) { if (typeof gtag === "function") gtag("event", ev); }
document.querySelectorAll('[data-track]').forEach(el =>
  el.addEventListener("click", () => track(el.getAttribute("data-track"))));
document.querySelectorAll('a[href^="tel:"]').forEach(a =>
  a.addEventListener("click", () => track("phone_click")));

/* ---- Booking form (only present on pages with #book) ---- */
const bookForm = document.getElementById("bookForm");
if (bookForm) {
  const selectedSizes = new Map();          // size -> qty; "?" = not sure
  const qtyList = document.getElementById("qtyList");
  const sizesField = document.getElementById("sizesField");

  function renderSizes() {
    document.querySelectorAll("#sizeChips .chip").forEach(c => {
      const on = selectedSizes.has(c.dataset.size);
      c.classList.toggle("active", on);
      c.setAttribute("aria-pressed", on);
    });
    qtyList.innerHTML = "";
    for (const [size, qty] of selectedSizes) {
      if (size === "?") continue;
      const row = document.createElement("div");
      row.className = "qty-row";
      row.innerHTML =
        `<span class="qty-size">Nr. ${size}</span>` +
        `<button type="button" class="qty-btn" data-act="dec" data-size="${size}" aria-label="−">−</button>` +
        `<span class="qty-val">${qty}</span>` +
        `<button type="button" class="qty-btn" data-act="inc" data-size="${size}" aria-label="+">+</button>`;
      qtyList.appendChild(row);
    }
    sizesField.value = [...selectedSizes]
      .map(([s, q]) => (s === "?" ? "?" : `Nr.${s}x${q}`)).join(", ");
  }

  function toggleSize(size) {
    if (size === "?") {
      const had = selectedSizes.has("?");
      selectedSizes.clear();
      if (!had) selectedSizes.set("?", 1);
    } else {
      selectedSizes.delete("?");
      if (selectedSizes.has(size)) selectedSizes.delete(size);
      else selectedSizes.set(size, 1);
    }
    renderSizes();
  }

  document.querySelectorAll("#sizeChips .chip").forEach(c =>
    c.addEventListener("click", () => toggleSize(c.dataset.size)));

  qtyList.addEventListener("click", e => {
    const btn = e.target.closest(".qty-btn");
    if (!btn) return;
    const size = btn.dataset.size;
    const qty = selectedSizes.get(size) || 1;
    if (btn.dataset.act === "inc") selectedSizes.set(size, Math.min(qty + 1, 50));
    else if (qty <= 1) selectedSizes.delete(size);
    else selectedSizes.set(size, qty - 1);
    renderSizes();
  });

  /* size cards (same page) preselect a size chip */
  document.querySelectorAll('[data-size]').forEach(a => {
    if (a.closest("#sizeChips") || a.closest(".qty-list")) return;
    a.addEventListener("click", () => {
      const num = (a.dataset.size || "").replace(/\D/g, "");
      if (!num) return;
      selectedSizes.delete("?");
      if (!selectedSizes.has(num)) selectedSizes.set(num, 1);
      renderSizes();
    });
  });

  /* AJAX submit — PRODUCTION: POST to a form endpoint that emails
     info@rigasafe.lv + pings Telegram/WhatsApp, then redirect to a
     /thank-you page for GA4 conversion tracking. */
  bookForm.addEventListener("submit", e => {
    e.preventDefault();
    if (!bookForm.name.value.trim() || !bookForm.phone.value.trim()) {
      bookForm.reportValidity();
      return;
    }
    document.getElementById("formSuccess").hidden = false;
    track("form_submit");
  });
}

/* ---- Scroll reveal ---- */
const io = new IntersectionObserver(entries => {
  entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach(el => io.observe(el));

/* ---- Cookie banner ---- */
const banner = document.getElementById("cookieBanner");
if (banner) {
  let consent = null;
  try { consent = localStorage.getItem("cookieConsent"); } catch (e) {}
  if (!consent) banner.hidden = false;
  const close = v => { try { localStorage.setItem("cookieConsent", v); } catch (e) {} banner.hidden = true; };
  document.getElementById("cookieAccept").addEventListener("click", () => close("granted"));
  document.getElementById("cookieDecline").addEventListener("click", () => close("denied"));
  /* PRODUCTION: initialise GA4/GTM + Meta Pixel only after consent === granted */
}

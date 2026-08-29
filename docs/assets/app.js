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

/* ---- Motion. All of it is opt-out: if the visitor asks for reduced
   motion we register nothing, so the page is simply static. ---- */
const REDUCED = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* Scroll reveal — staggered per element via the --i custom property (CSS) */
if (REDUCED) {
  document.querySelectorAll(".reveal").forEach(el => el.classList.add("in"));
} else {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach(el => io.observe(el));
}

/* ---- Count-up on the stat band and the About figures ----
   The rendered text must survive exactly, so we only animate the first
   run of digits and rebuild the string around it. Years ("2017") and
   composite values ("24/7") are left alone — counting them looks silly. */
function setupCounters() {
  const els = [...document.querySelectorAll("[data-count]")];
  const parse = el => {
    const raw = el.textContent;
    const m = raw.match(/[\d][\d\s,\u00a0]*/);
    if (!m) return null;
    const digits = m[0].replace(/[\s,\u00a0]/g, "");
    const value = parseInt(digits, 10);
    if (!Number.isFinite(value) || value < 100) return null;   // too small to be worth it
    if (/^(19|20)\d{2}$/.test(digits)) return null;             // a year, not a quantity
    if (raw.includes("/")) return null;                        // "24/7"
    const sep = /[\s,\u00a0]/.test(m[0]) ? m[0].match(/[\s,\u00a0]/)[0] : "";
    return { raw, value, start: m.index, len: m[0].length, sep };
  };
  const fmt = (n, sep) => sep ? n.toLocaleString("en-US").replace(/,/g, sep) : String(n);
  const run = el => {
    const p = el._c;
    const dur = 1100, t0 = performance.now();
    const tick = now => {
      const k = Math.min(1, (now - t0) / dur);
      const eased = 1 - Math.pow(1 - k, 3);
      const n = Math.round(p.value * eased);
      el.textContent = p.raw.slice(0, p.start) + fmt(n, p.sep) + p.raw.slice(p.start + p.len);
      if (k < 1) requestAnimationFrame(tick); else el.textContent = p.raw;
    };
    requestAnimationFrame(tick);
  };
  const obs = new IntersectionObserver(ents => {
    ents.forEach(en => { if (en.isIntersecting) { run(en.target); obs.unobserve(en.target); } });
  }, { threshold: 0.6 });
  els.forEach(el => { const p = parse(el); if (p) { el._c = p; obs.observe(el); } });
}
if (!REDUCED) setupCounters();

/* ---- Header condense + reading progress + step rail, on one rAF loop ---- */
(function scrollFx() {
  const header = document.querySelector(".site-header");
  const bar = document.getElementById("scrollProgress");
  const rail = document.querySelector(".steps-rail i");
  const railBox = document.querySelector(".steps-wrap");
  const parallax = [...document.querySelectorAll("[data-parallax]")];
  let ticking = false;

  function frame() {
    ticking = false;
    const y = window.scrollY || 0;
    if (header) header.classList.toggle("stuck", y > 24);
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (max > 0 ? Math.min(100, (y / max) * 100) : 0) + "%";
    }
    if (rail && railBox) {
      const r = railBox.getBoundingClientRect();
      const k = (window.innerHeight * 0.62 - r.top) / (r.height || 1);
      rail.style.height = Math.max(0, Math.min(1, k)) * 100 + "%";
    }
    if (!REDUCED) parallax.forEach(el => {
      const r = el.getBoundingClientRect();
      const off = (r.top + r.height / 2 - window.innerHeight / 2) * parseFloat(el.dataset.parallax || 0);
      el.style.transform = "translate3d(0," + (-off).toFixed(1) + "px,0)";
    });
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  frame();
})();

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

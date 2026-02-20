/* ============================================================
   ASPIRO × SOFINNOVA — main.js
   ============================================================ */

/* ── Helpers ── */
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

/* ─────────────────────────────────────────────
   HEADER: hero-mode vs. scrolled
   ───────────────────────────────────────────── */
(function initHeader() {
  const header = $('.site-header');
  const heroH  = () => $('.hero') ? $('.hero').offsetHeight * 0.6 : 400;

  function update() {
    const y = window.scrollY;
    const isHero = y < heroH();
    header.classList.toggle('hero-active', isHero);
    header.classList.toggle('scrolled', !isHero);
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();

/* ─────────────────────────────────────────────
   MENU OVERLAY
   ───────────────────────────────────────────── */
(function initMenu() {
  const btn     = $('.menu-btn');
  const overlay = $('.menu-overlay');
  const header  = $('.site-header');
  if (!btn || !overlay) return;

  let open = false;

  function toggleMenu(force) {
    open = typeof force === 'boolean' ? force : !open;
    overlay.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
    document.body.style.overflow = open ? 'hidden' : '';
    btn.setAttribute('aria-expanded', open);
  }

  btn.addEventListener('click', () => toggleMenu());

  // Close on link click
  $$('.menu-overlay a').forEach(a =>
    a.addEventListener('click', () => toggleMenu(false))
  );

  // Close on Escape
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && open) toggleMenu(false);
  });
})();

/* ─────────────────────────────────────────────
   SMOOTH SCROLL for anchor links
   ───────────────────────────────────────────── */
document.addEventListener('click', e => {
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  const id = a.getAttribute('href');
  if (id === '#') return;
  const target = document.querySelector(id);
  if (!target) return;
  e.preventDefault();
  const offset = 80;
  window.scrollTo({
    top: target.getBoundingClientRect().top + window.scrollY - offset,
    behavior: 'smooth'
  });
});

/* ─────────────────────────────────────────────
   WORD SLOT ROTATOR — hero cycling word
   ───────────────────────────────────────────── */
(function initWordSlot() {
  const slot  = $('.word-slot-inner');
  if (!slot) return;

  const words = ['Clarity', 'Outcomes', 'Precision', 'Impact', 'Excellence'];
  let idx = 0;
  let busy = false;

  function next() {
    if (busy) return;
    busy = true;
    idx = (idx + 1) % words.length;

    // Exit current word upward
    slot.classList.add('exiting');

    setTimeout(() => {
      slot.classList.remove('exiting');
      slot.textContent = words[idx];
      slot.classList.add('entering');
      setTimeout(() => {
        slot.classList.remove('entering');
        busy = false;
      }, 600);
    }, 420);
  }

  setInterval(next, 2800);
})();

/* ─────────────────────────────────────────────
   INTERSECTION OBSERVER — reveal + line-anim + stat bars
   ───────────────────────────────────────────── */
(function initObservers() {
  // Generic reveal
  const reveals = $$('.reveal');
  if (reveals.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(el => io.observe(el));
  }

  // Line animations
  const lines = $$('.line-anim');
  if (lines.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0 });
    lines.forEach(el => io.observe(el));
  }

  // Stat bars (underline reveal)
  const bars = $$('.h-stat-bar');
  if (bars.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    bars.forEach(el => io.observe(el));
  }
})();

/* ─────────────────────────────────────────────
   COUNTER ANIMATION — hero stat numbers
   ───────────────────────────────────────────── */
(function initCounters() {
  const nums = $$('.h-stat-num[data-count]');
  if (!nums.length) return;

  function ease(t) { return 1 - Math.pow(1 - t, 3); }

  function animateNum(el) {
    const raw    = el.dataset.count;
    const suffix = raw.replace(/[\d,]/g, '');
    const target = parseInt(raw.replace(/[^0-9]/g, ''), 10);
    if (isNaN(target)) return;
    const dur = 1500;
    const t0  = performance.now();

    function frame(t) {
      const p   = Math.min((t - t0) / dur, 1);
      const val = Math.round(ease(p) * target);
      el.innerHTML = val.toLocaleString() + suffix;
      if (p < 1) requestAnimationFrame(frame);
      else el.innerHTML = raw; // ensure exact final value
    }
    requestAnimationFrame(frame);
  }

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        animateNum(e.target);
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.6 });

  nums.forEach(el => io.observe(el));
})();

/* ─────────────────────────────────────────────
   SERVICE ROW EXPAND — show hidden body text on screens
   that hide it (handled in CSS, JS enhances UX if needed)
   ───────────────────────────────────────────── */
(function initSvcRows() {
  const rows = $$('.svc-row');
  rows.forEach(row => {
    row.setAttribute('tabindex', '0');
    row.setAttribute('role', 'button');
  });
})();

/* ============================================================
   ASPIRO — main.js
   ============================================================ */
(() => {
  'use strict';

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ─────────────────────────────────────────────
     HEADER: transparent over hero, solid after
     ───────────────────────────────────────────── */
  (function initHeader() {
    const header = $('[data-header]');
    if (!header) return;
    let ticking = false;
    const update = () => {
      header.classList.toggle('scrolled', window.scrollY > 24);
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  })();

  /* ─────────────────────────────────────────────
     ACTIVE NAV LINK (scroll spy)
     ───────────────────────────────────────────── */
  (function initScrollSpy() {
    const links = $$('.nav-desktop a[href^="#"]');
    if (!links.length || !('IntersectionObserver' in window)) return;
    const map = new Map();
    links.forEach(a => {
      const sec = document.querySelector(a.getAttribute('href'));
      if (sec) map.set(sec, a);
    });
    const hero = $('.hero');
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        links.forEach(l => l.classList.remove('active'));
        map.get(e.target)?.classList.add('active');
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    map.forEach((_, sec) => io.observe(sec));
    if (hero) io.observe(hero);
  })();

  /* ─────────────────────────────────────────────
     MOBILE MENU (with focus trap)
     ───────────────────────────────────────────── */
  (function initMenu() {
    const btn = $('.menu-btn');
    const overlay = $('#menu-overlay');
    if (!btn || !overlay) return;

    let open = false;
    let lastFocus = null;

    const focusables = () => $$('a[href], button:not([disabled])', overlay);

    function setOpen(next) {
      open = next;
      lastFocus = open ? document.activeElement : lastFocus;
      if (open) {
        overlay.hidden = false;
        requestAnimationFrame(() => overlay.classList.add('open'));
        document.body.classList.add('menu-open');
        document.body.style.overflow = 'hidden';
        btn.setAttribute('aria-expanded', 'true');
        btn.setAttribute('aria-label', 'Close navigation');
        setTimeout(() => focusables()[0]?.focus(), 80);
      } else {
        overlay.classList.remove('open');
        document.body.classList.remove('menu-open');
        document.body.style.overflow = '';
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-label', 'Open navigation');
        setTimeout(() => { overlay.hidden = true; }, 450);
        lastFocus?.focus?.();
      }
    }

    btn.addEventListener('click', () => setOpen(!open));
    $$('a', overlay).forEach(a => a.addEventListener('click', () => setOpen(false)));

    document.addEventListener('keydown', e => {
      if (!open) return;
      if (e.key === 'Escape') { setOpen(false); return; }
      if (e.key === 'Tab') {
        const items = focusables();
        if (!items.length) return;
        const first = items[0], last = items[items.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

    // Close if viewport grows past the mobile breakpoint
    window.matchMedia('(min-width: 1025px)').addEventListener('change', e => {
      if (e.matches && open) setOpen(false);
    });
  })();

  /* ─────────────────────────────────────────────
     SMOOTH SCROLL for in-page anchors
     ───────────────────────────────────────────── */
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href');
    if (id.length < 2) return;
    const target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    const headerH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-h'), 10) || 76;
    const top = target.getBoundingClientRect().top + window.scrollY - headerH - 8;
    window.scrollTo({ top, behavior: reducedMotion ? 'auto' : 'smooth' });
    history.replaceState(null, '', id);
  });

  /* ─────────────────────────────────────────────
     WORD ROTATORS
     ───────────────────────────────────────────── */
  function rotator(el, words, interval = 3000) {
    if (!el || reducedMotion) return;
    let idx = 0, busy = false;
    setInterval(() => {
      if (busy || document.hidden) return;
      busy = true;
      idx = (idx + 1) % words.length;
      el.classList.add('exiting');
      setTimeout(() => {
        el.classList.remove('exiting');
        el.textContent = words[idx];
        el.classList.add('entering');
        setTimeout(() => { el.classList.remove('entering'); busy = false; }, 560);
      }, 420);
    }, interval);
  }
  rotator($('.hero .word-slot-inner'), ['clarity', 'outcomes', 'precision', 'impact', 'excellence'], 3000);
  rotator($('.word-slot-inner--location'), ['KSA', 'Qatar', 'UAE', 'the South Pacific'], 2800);

  /* ─────────────────────────────────────────────
     REVEAL ON SCROLL
     ───────────────────────────────────────────── */
  (function initReveal() {
    const items = $$('.reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window) || reducedMotion) {
      items.forEach(el => el.classList.add('in'));
      return;
    }
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -8% 0px' });
    // Anything already above the fold shows immediately; the observer handles the rest.
    const vh = window.innerHeight;
    items.forEach(el => {
      if (el.getBoundingClientRect().top < vh) el.classList.add('in');
      else io.observe(el);
    });
  })();

  /* ─────────────────────────────────────────────
     COUNTERS — hero stats
     ───────────────────────────────────────────── */
  (function initCounters() {
    const nums = $$('.h-stat-num[data-count]');
    if (!nums.length || reducedMotion || !('IntersectionObserver' in window)) return;
    const ease = t => 1 - Math.pow(1 - t, 3);

    function animate(el) {
      const raw = el.dataset.count;
      const suffix = raw.replace(/[\d,]/g, '');
      const target = parseInt(raw.replace(/[^0-9]/g, ''), 10);
      if (isNaN(target)) return;
      const dur = 1400, t0 = performance.now();
      const frame = t => {
        const p = Math.min((t - t0) / dur, 1);
        el.textContent = Math.round(ease(p) * target).toLocaleString('en-US') + suffix;
        if (p < 1) requestAnimationFrame(frame);
        else el.textContent = target.toLocaleString('en-US') + suffix;
      };
      requestAnimationFrame(frame);
    }

    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { animate(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.5 });
    nums.forEach(el => io.observe(el));
  })();

  /* ─────────────────────────────────────────────
     SERVICES ACCORDION
     ───────────────────────────────────────────── */
  (function initServices() {
    const heads = $$('.svc-head');
    if (!heads.length) return;

    const setExpanded = (head, on) => head.setAttribute('aria-expanded', on ? 'true' : 'false');
    heads.forEach((h, i) => setExpanded(h, i === 0));

    heads.forEach(head => {
      head.addEventListener('click', () => {
        const willOpen = head.getAttribute('aria-expanded') !== 'true';
        heads.forEach(h => setExpanded(h, false));
        setExpanded(head, willOpen);
      });
    });

    // Deep links from the footer (#svc-3) should open that row
    const openFromHash = () => {
      const m = location.hash.match(/^#svc-(\d)$/);
      if (!m) return;
      const row = document.getElementById(`svc-${m[1]}`);
      const head = row && $('.svc-head', row);
      if (!head) return;
      heads.forEach(h => setExpanded(h, false));
      setExpanded(head, true);
    };
    window.addEventListener('hashchange', openFromHash);
    document.addEventListener('click', e => {
      const a = e.target.closest('a[href^="#svc-"]');
      if (a) setTimeout(openFromHash, 0);
    });
    openFromHash();
  })();

  /* ─────────────────────────────────────────────
     TEAM BIO DIALOG
     ───────────────────────────────────────────── */
  (function initBios() {
    const dialog = $('#bio-dialog');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    const photo = $('[data-bio-photo]', dialog);
    const name = $('[data-bio-name]', dialog);
    const role = $('[data-bio-role]', dialog);
    const body = $('[data-bio-body]', dialog);
    let opener = null;

    $$('[data-person]').forEach(btn => {
      btn.addEventListener('click', () => {
        const card = btn.closest('.person');
        const img = $('img', btn);
        photo.src = img.currentSrc || img.src;
        photo.alt = img.alt;
        name.textContent = $('.person-name', btn).textContent;
        role.textContent = $('.person-role', btn).textContent;
        body.innerHTML = $('.person-bio', card).innerHTML;
        opener = btn;
        dialog.showModal();
        $('[data-bio-close]', dialog).focus();
      });
    });

    $('[data-bio-close]', dialog).addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => {
      const r = $('.bio-dialog-inner', dialog).getBoundingClientRect();
      const inside = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
      if (!inside) dialog.close();
    });
    dialog.addEventListener('close', () => opener?.focus());
  })();

  /* ─────────────────────────────────────────────
     CONTACT FORM
     Posts JSON to data-endpoint when configured;
     otherwise opens the visitor's mail client pre-filled.
     ───────────────────────────────────────────── */
  (function initContactForm() {
    const form = $('#contact-form');
    if (!form) return;
    const status = $('.form-status', form);
    const submitBtn = $('button[type="submit"]', form);

    const setStatus = (msg, isError = false) => {
      status.textContent = msg;
      status.classList.toggle('error', isError);
    };

    form.addEventListener('submit', async e => {
      e.preventDefault();
      let valid = true;
      $$('[required]', form).forEach(f => {
        const ok = f.type === 'email' ? f.validity.valid && f.value.trim() : f.value.trim().length > 0;
        f.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok) valid = false;
      });
      if (!valid) { setStatus('Please complete the highlighted fields.', true); return; }

      const data = Object.fromEntries(new FormData(form).entries());
      const endpoint = form.dataset.endpoint;

      if (endpoint) {
        submitBtn.disabled = true;
        setStatus('Sending…');
        try {
          const res = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
            body: JSON.stringify(data)
          });
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          form.reset();
          setStatus('Thank you. A partner will be in touch within one business day.');
        } catch (err) {
          setStatus('Something went wrong. Please email info@aspiro.me directly.', true);
        } finally {
          submitBtn.disabled = false;
        }
        return;
      }

      // No endpoint configured: hand off to the visitor's email client.
      const subject = encodeURIComponent(`Enquiry: ${data.topic || 'General'} — ${data.name}`);
      const bodyText = encodeURIComponent(
        `Name: ${data.name}\nOrganisation: ${data.company || '-'}\nEmail: ${data.email}\nTopic: ${data.topic}\n\n${data.message}`
      );
      window.location.href = `mailto:info@aspiro.me?subject=${subject}&body=${bodyText}`;
      setStatus('Opening your email client. If nothing happens, write to info@aspiro.me.');
    });
  })();

  /* ─────────────────────────────────────────────
     GATED WHITEPAPER DOWNLOADS
     One lead form unlocks all papers for the visitor (remembered in
     localStorage). Leads POST to data-endpoint when configured.
     ───────────────────────────────────────────── */
  (function initGate() {
    const dialog = $('#gate-dialog');
    const triggers = $$('[data-gate]');
    if (!triggers.length) return;
    const KEY = 'aspiro_wp_lead';
    const read = () => { try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; } };
    const save = v => { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) { /* ignore */ } };

    function download(file, title) {
      const a = document.createElement('a');
      a.href = file;
      a.download = (title || 'Aspiro whitepaper').replace(/[^\w\s-]/g, '') + '.pdf';
      a.rel = 'noopener';
      document.body.appendChild(a);
      a.click();
      a.remove();
    }

    async function recordLead(data) {
      const endpoint = $('#gate-form')?.dataset.endpoint;
      if (!endpoint) return true;
      try {
        const res = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ ...data, source: location.pathname })
        });
        return res.ok;
      } catch (e) { return false; }
    }

    let current = null;
    triggers.forEach(btn => {
      btn.addEventListener('click', async () => {
        current = { slug: btn.dataset.wpSlug, title: btn.dataset.wpTitle, file: btn.dataset.wpFile };
        const lead = read();
        if (lead && lead.email) {
          recordLead({ ...lead, whitepaper: current.slug, repeat: true });
          download(current.file, current.title);
          return;
        }
        if (!dialog || typeof dialog.showModal !== 'function') { download(current.file, current.title); return; }
        $('[data-gate-title]', dialog).textContent = current.title;
        $('[data-gate-slug]', dialog).value = current.slug;
        dialog.showModal();
        setTimeout(() => $('#g-name', dialog)?.focus(), 50);
      });
    });

    if (!dialog) return;
    const form = $('#gate-form', dialog);
    const status = $('.form-status', form);
    const submitBtn = $('button[type="submit"]', form);
    $('[data-gate-close]', dialog).addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => {
      const r = $('.gate-inner', dialog).getBoundingClientRect();
      const inside = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
      if (!inside) dialog.close();
    });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      let valid = true;
      $$('[required]', form).forEach(f => {
        const ok = f.type === 'checkbox' ? f.checked : (f.type === 'email' ? f.validity.valid && f.value.trim() : f.value.trim().length > 0);
        if (f.type !== 'checkbox') f.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok) valid = false;
      });
      if (!valid) { status.textContent = 'Please complete every field and accept the privacy policy.'; status.classList.add('error'); return; }
      status.classList.remove('error');
      status.textContent = 'Preparing your download…';
      submitBtn.disabled = true;
      const data = Object.fromEntries(new FormData(form).entries());
      delete data.consent;
      await recordLead(data);
      save({ name: data.name, email: data.email, company: data.company, role: data.role, at: new Date().toISOString() });
      submitBtn.disabled = false;
      status.textContent = 'Thank you. Your download has started.';
      download(current.file, current.title);
      setTimeout(() => { dialog.close(); status.textContent = ''; form.reset(); }, 1600);
    });
  })();

  /* ─────────────────────────────────────────────
     COPY LINK (insight articles)
     ───────────────────────────────────────────── */
  $$('[data-copy]').forEach(btn => {
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(btn.dataset.copy);
        const orig = btn.textContent;
        btn.textContent = 'Copied';
        setTimeout(() => { btn.textContent = orig; }, 1600);
      } catch (e) { /* clipboard unavailable */ }
    });
  });

  /* ─────────────────────────────────────────────
     FOOTER YEAR
     ───────────────────────────────────────────── */
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
})();

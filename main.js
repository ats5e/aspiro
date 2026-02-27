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
  const heroH = () => $('.hero') ? $('.hero').offsetHeight * 0.6 : 400;

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
  const btn = $('.menu-btn');
  const overlay = $('.menu-overlay');
  const header = $('.site-header');
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
  const slot = $('.word-slot-inner');
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
   LOCATION SLOT ROTATOR — intro section
   ───────────────────────────────────────────── */
(function initLocationSlot() {
  const slot = $('.word-slot-inner--location');
  if (!slot) return;

  const locations = ['KSA', 'Qatar', 'UAE', 'South Pacific'];
  let idx = 0;
  let busy = false;

  function next() {
    if (busy) return;
    busy = true;
    idx = (idx + 1) % locations.length;

    slot.classList.add('exiting');

    setTimeout(() => {
      slot.classList.remove('exiting');
      slot.textContent = locations[idx];
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
    const raw = el.dataset.count;
    const suffix = raw.replace(/[\d,]/g, '');
    const target = parseInt(raw.replace(/[^0-9]/g, ''), 10);
    if (isNaN(target)) return;
    const dur = 1500;
    const t0 = performance.now();

    function frame(t) {
      const p = Math.min((t - t0) / dur, 1);
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
  if (!rows.length) return;
  const mq = window.matchMedia('(max-width: 1100px)');

  function collapseAll(except) {
    rows.forEach(row => {
      if (row === except) return;
      row.classList.remove('expanded');
      row.setAttribute('aria-expanded', 'false');
    });
  }

  function syncMode() {
    if (!mq.matches) {
      rows.forEach(row => {
        row.classList.remove('expanded');
        row.removeAttribute('aria-expanded');
      });
    } else {
      rows.forEach((row, i) => {
        row.setAttribute('aria-expanded', i === 0 ? 'true' : 'false');
        if (i === 0) row.classList.add('expanded');
      });
    }
  }

  rows.forEach(row => {
    row.setAttribute('tabindex', '0');
    row.setAttribute('role', 'button');
    row.addEventListener('click', () => {
      if (!mq.matches) return;
      const willExpand = !row.classList.contains('expanded');
      collapseAll(row);
      row.classList.toggle('expanded', willExpand);
      row.setAttribute('aria-expanded', willExpand ? 'true' : 'false');
    });
    row.addEventListener('keydown', e => {
      if (!mq.matches) return;
      if (e.key !== 'Enter' && e.key !== ' ') return;
      e.preventDefault();
      row.click();
    });
  });

  if (mq.addEventListener) mq.addEventListener('change', syncMode);
  else mq.addListener(syncMode);
  syncMode();
})();

/* ─────────────────────────────────────────────
   CASE METRICS — staggered entrance + metric count-up
   ───────────────────────────────────────────── */
(function initCaseMetrics() {
  const cards = $$('.case-item');
  if (!cards.length) return;

  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  function animateMetricValue(el) {
    const raw = (el.textContent || '').replace(/\u00a0/g, ' ').trim();
    if (!raw) return;

    // Supports patterns like "$25M", "70%", "Top 5", "SAR 4.75M"
    const m = raw.match(/^([^0-9]*)([0-9]+(?:\.[0-9]+)?)(.*)$/);
    if (!m) return;

    const prefix = m[1];
    const target = Number(m[2]);
    const suffix = m[3];
    if (Number.isNaN(target)) return;

    const isInteger = Number.isInteger(target);
    const dur = 1100;
    const t0 = performance.now();

    function frame(t) {
      const p = Math.min((t - t0) / dur, 1);
      const eased = easeOut(p);
      const val = isInteger ? Math.round(eased * target) : (eased * target);

      const shown = isInteger
        ? val.toLocaleString()
        : val.toFixed(2).replace(/\.00$/, '');

      el.textContent = `${prefix}${shown}${suffix}`;
      if (p < 1) requestAnimationFrame(frame);
      else el.textContent = raw;
    }

    requestAnimationFrame(frame);
  }

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const card = entry.target;
      const idx = cards.indexOf(card);
      const delay = Math.max(0, idx) * 90;

      setTimeout(() => {
        card.classList.add('case-in');
        const metric = $('.case-metric', card);
        if (metric) animateMetricValue(metric);
      }, delay);

      io.unobserve(card);
    });
  }, { threshold: 0.28, rootMargin: '0px 0px -8% 0px' });

  cards.forEach(card => io.observe(card));
})();

/* ─────────────────────────────────────────────
   AETHER FLOW CANVAS BACKGROUND — Hero Section
   ───────────────────────────────────────────── */
(function initAetherFlowBackground() {
  const canvas = document.getElementById('neural-canvas');
  if (!canvas) return;
  const container = canvas.parentElement;

  const ctx = canvas.getContext('2d');
  let animationFrameId;
  let particles = [];
  const mouse = { x: null, y: null, radius: 200 };

  const colorTeal = { r: 64, g: 184, b: 162 };
  const colorPurple = { r: 43, g: 14, b: 72 };

  class Particle {
    constructor(x, y, directionX, directionY, size, colorObj) {
      this.x = x;
      this.y = y;
      this.directionX = directionX;
      this.directionY = directionY;
      this.size = size;
      this.colorObj = colorObj;
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
      ctx.fillStyle = `rgba(${this.colorObj.r}, ${this.colorObj.g}, ${this.colorObj.b}, 0.8)`;
      ctx.fill();
    }

    update() {
      if (this.x > container.offsetWidth || this.x < 0) {
        this.directionX = -this.directionX;
      }
      if (this.y > container.offsetHeight || this.y < 0) {
        this.directionY = -this.directionY;
      }

      // Mouse collision detection
      if (mouse.x !== null && mouse.y !== null) {
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx * dx + dy * dy);
        if (distance < mouse.radius + this.size) {
          const forceDirectionX = dx / distance;
          const forceDirectionY = dy / distance;
          const force = (mouse.radius - distance) / mouse.radius;
          this.x -= forceDirectionX * force * 5;
          this.y -= forceDirectionY * force * 5;
        }
      }

      this.x += this.directionX;
      this.y += this.directionY;
      this.draw();
    }
  }

  function init() {
    particles = [];
    let w = container.offsetWidth;
    let h = container.offsetHeight;
    // Calculate density based on logical (CSS) pixels, not physical pixels
    let numberOfParticles = (h * w) / 8000;
    for (let i = 0; i < numberOfParticles; i++) {
      let size = (Math.random() * 2) + 1;
      let x = (Math.random() * ((w - size * 2) - (size * 2)) + size * 2);
      let y = (Math.random() * ((h - size * 2) - (size * 2)) + size * 2);
      let directionX = (Math.random() * 0.4) - 0.2;
      let directionY = (Math.random() * 0.4) - 0.2;

      // Alternate between Teal and Purple
      let colorObj = Math.random() > 0.5 ? colorTeal : colorPurple;

      particles.push(new Particle(x, y, directionX, directionY, size, colorObj));
    }
  }

  const resizeCanvas = () => {
    const dpr = window.devicePixelRatio || 1;
    let w = container.offsetWidth;
    let h = container.offsetHeight;
    // Set native physical size
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    // Set styled CSS size
    canvas.style.width = `${w}px`;
    canvas.style.height = `${h}px`;
    // Scale context to ensure sizes/coords match CSS pixels
    ctx.scale(dpr, dpr);
    init();
  };
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  const connect = () => {
    let opacityValue = 1;
    for (let a = 0; a < particles.length; a++) {
      for (let b = a; b < particles.length; b++) {
        let distance = ((particles[a].x - particles[b].x) * (particles[a].x - particles[b].x))
          + ((particles[a].y - particles[b].y) * (particles[a].y - particles[b].y));

        if (distance < (container.offsetWidth / 7) * (container.offsetHeight / 7)) {
          opacityValue = 1 - (distance / 20000);

          let dx_mouse_a = particles[a].x - mouse.x;
          let dy_mouse_a = particles[a].y - mouse.y;
          let distance_mouse_a = Math.sqrt(dx_mouse_a * dx_mouse_a + dy_mouse_a * dy_mouse_a);

          // Mix line colors based on the connected particles' colors
          // If they match, use that color. If they differ, blend them (approximate to purple/teal mix).
          let r = Math.round((particles[a].colorObj.r + particles[b].colorObj.r) / 2);
          let g = Math.round((particles[a].colorObj.g + particles[b].colorObj.g) / 2);
          let b_col = Math.round((particles[a].colorObj.b + particles[b].colorObj.b) / 2);

          if (mouse.x && distance_mouse_a < mouse.radius) {
            // Brighten near mouse
            ctx.strokeStyle = `rgba(${r + 40}, ${g + 40}, ${b_col + 40}, ${opacityValue})`;
          } else {
            ctx.strokeStyle = `rgba(${r}, ${g}, ${b_col}, ${opacityValue * 0.8})`; // slightly muted lines
          }

          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(particles[a].x, particles[a].y);
          ctx.lineTo(particles[b].x, particles[b].y);
          ctx.stroke();
        }
      }
    }
  };

  const animate = () => {
    animationFrameId = requestAnimationFrame(animate);

    // Clear transparent so white background shows through
    ctx.clearRect(0, 0, container.offsetWidth, container.offsetHeight);

    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
    }
    connect();
  };

  const handleMouseMove = (event) => {
    // Offset by any scrolling to keep mouse accurate over canvas
    const rect = canvas.getBoundingClientRect();
    mouse.x = event.clientX - rect.left;
    mouse.y = event.clientY - rect.top;
  };

  const handleMouseOut = () => {
    mouse.x = null;
    mouse.y = null;
  };

  window.addEventListener('mousemove', handleMouseMove);
  window.addEventListener('mouseout', handleMouseOut);

  init();
  animate();

})();

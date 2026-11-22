/**
 * NSIKAN ESSIET PORTFOLIO — CORE SCRIPT
 * Parity implementation matching cagd.as scripts:
 * - available-widget: Live WAT time (UTC+1, Nigeria)
 * - navbar: Fixed header and mobile overlay menu
 * - works: Accordion detail drawers
 * - hero: Parallax portrait drift and radial aura
 */

(function () {
  'use strict';

  // --------------------------------------------------------------------------
  // 1. Available Widget & Live WAT Time (Kaduna, Nigeria - UTC+1)
  // --------------------------------------------------------------------------
  function initClock() {
    var hourNodes = document.querySelectorAll('.time_hour');
    var minNodes = document.querySelectorAll('.time_minutes');
    var periodNodes = document.querySelectorAll('.time_period');

    function updateTime() {
      var now = new Date();
      var utc = now.getTime() + (now.getTimezoneOffset() * 60000);
      var wat = new Date(utc + 3600000);

      var hours = wat.getHours();
      var minutes = String(wat.getMinutes()).padStart(2, '0');
      var period = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12;
      hours = hours ? String(hours) : '12';

      hourNodes.forEach(function (el) { el.textContent = hours; });
      minNodes.forEach(function (el) { el.textContent = minutes; });
      periodNodes.forEach(function (el) { el.textContent = period; });
    }

    updateTime();
    setInterval(updateTime, 1000);
    document.addEventListener('visibilitychange', function () {
      if (!document.hidden) updateTime();
    });
  }

  // --------------------------------------------------------------------------
  // 2. Navbar & Mobile Menu Overlay
  // --------------------------------------------------------------------------
  function initNavbar() {
    var burger = document.querySelector('.nav_burger');
    var overlay = document.querySelector('.nav_overlay');
    if (!burger || !overlay) return;

    var overlayLinks = overlay.querySelectorAll('.nav_overlay-link, .nav_overlay-cta');
    var burgerLines = burger.querySelectorAll('.nav_burger-line');
    var line1 = burgerLines[0];
    var line2 = burgerLines[1];

    var isOpen = false;

    function toggleMenu(state) {
      isOpen = typeof state === 'boolean' ? state : !isOpen;

      burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      burger.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
      overlay.setAttribute('aria-hidden', isOpen ? 'false' : 'true');

      if (isOpen) {
        overlay.style.opacity = '1';
        overlay.style.visibility = 'visible';
        document.body.style.overflow = 'hidden';

        if (line1) line1.style.transform = 'translateY(3px) rotate(45deg)';
        if (line2) line2.style.transform = 'translateY(-3px) rotate(-45deg)';
      } else {
        overlay.style.opacity = '0';
        overlay.style.visibility = 'hidden';
        document.body.style.overflow = '';

        if (line1) line1.style.transform = 'none';
        if (line2) line2.style.transform = 'none';
      }
    }

    burger.addEventListener('click', function (e) {
      e.preventDefault();
      toggleMenu();
    });

    overlayLinks.forEach(function (link) {
      link.addEventListener('click', function () { toggleMenu(false); });
    });

    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) toggleMenu(false);
    });

    window.addEventListener('resize', function () {
      if (isOpen && window.innerWidth > 991) toggleMenu(false);
    });
  }

  // --------------------------------------------------------------------------
  // 3. Work Case Study Details Drawer (works.min.js parity)
  // --------------------------------------------------------------------------
  function initWorkDetails() {
    var detailButtons = document.querySelectorAll('.button_details');
    var isMobile = window.matchMedia('(max-width: 767px)');

    function setupLayout() {
      detailButtons.forEach(function (btn) {
        var workItem = btn.closest('.work_item') || btn.closest('.work_item-text');
        var workBottom = workItem ? workItem.querySelector('.work-bottom') : null;
        if (!workBottom) return;

        if (isMobile.matches) {
          if (!btn.classList.contains('is-revealed')) {
            workBottom.style.display = 'none';
          }
        } else {
          workBottom.style.display = 'flex';
          workBottom.style.height = '';
          workBottom.style.opacity = '';
        }
      });
    }

    detailButtons.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var workItem = btn.closest('.work_item') || btn.closest('.work_item-text');
        var workBottom = workItem ? workItem.querySelector('.work-bottom') : null;
        if (!workBottom) return;

        if (isMobile.matches) {
          var isHidden = workBottom.style.display === 'none';
          if (isHidden) {
            workBottom.style.display = 'flex';
            workBottom.style.height = '0px';
            workBottom.style.opacity = '0';
            workBottom.style.overflow = 'hidden';
            workBottom.style.transition = 'height 360ms ease, opacity 360ms ease';

            requestAnimationFrame(function () {
              workBottom.style.height = workBottom.scrollHeight + 'px';
              workBottom.style.opacity = '1';
            });

            setTimeout(function () {
              workBottom.style.height = 'auto';
              workBottom.style.overflow = '';
            }, 380);

            btn.classList.add('is-revealed');
            btn.querySelector('div').textContent = 'Hide details';
          } else {
            workBottom.style.display = 'none';
            btn.classList.remove('is-revealed');
            btn.querySelector('div').textContent = 'Read the details';
          }
        } else {
          workBottom.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });
    });

    setupLayout();
    if (isMobile.addEventListener) {
      isMobile.addEventListener('change', setupLayout);
    } else if (isMobile.addListener) {
      isMobile.addListener(setupLayout);
    }
  }

  // --------------------------------------------------------------------------
  // 4. Hero Parallax & Background Glow
  // --------------------------------------------------------------------------
  function initHeroParallax() {
    var heroPhoto = document.getElementById('heroPhotoWrap');
    var heroHeader = document.querySelector('.header-wrapper');
    if (!heroPhoto || window.innerWidth < 768) return;

    var ticking = false;

    function onScroll() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      var vh = window.innerHeight || 1;
      var progress = Math.min(Math.max(scrollY / vh, 0), 1);

      heroPhoto.style.transform = 'translate(-57%, ' + (progress * 120) + 'px)';
      heroPhoto.style.opacity = String(Math.max(0.88 - progress * 1.2, 0));

      if (heroHeader && scrollY < vh) {
        heroHeader.style.transform = 'translateY(' + (progress * -80) + 'px)';
        heroHeader.style.opacity = String(Math.max(1 - progress * 1.5, 0));
      }

      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(onScroll);
        ticking = true;
      }
    }, { passive: true });
  }

  // --------------------------------------------------------------------------
  // 5. Smooth Anchor Scrolling
  // --------------------------------------------------------------------------
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var href = this.getAttribute('href');
        if (href === '#' || !href) return;
        var target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initClock();
    initNavbar();
    initWorkDetails();
    initHeroParallax();
    initSmoothScroll();
  });
})();

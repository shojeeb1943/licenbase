/* ============================================================
   LicenBase — homepage interactions & motion
   Deps: GSAP + ScrollTrigger, Lenis, Swiper, Lucide (CDN)
   ============================================================ */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Lucide icons ---------- */
  if (window.lucide) {
    lucide.createIcons();
  }

  /* ---------- Lenis smooth scroll ---------- */
  var lenis = null;
  if (window.Lenis && !prefersReduced) {
    lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  /* ---------- Anchor smooth scrolling ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (!id || id.length < 2) return;
      var target = document.querySelector(id);
      if (!target) return;
      if (lenis) {
        e.preventDefault();
        lenis.scrollTo(target, { offset: -96, duration: 1.2 });
      }
    });
  });

  /* ---------- Header scroll state ---------- */
  var header = document.getElementById("site-header");
  function onScroll() {
    var y = window.scrollY || (lenis ? lenis.scroll : 0);
    header.classList.toggle("lb-scrolled", y > 8);
  }
  if (lenis) {
    lenis.on("scroll", onScroll);
  } else {
    window.addEventListener("scroll", onScroll, { passive: true });
  }
  onScroll();

  /* ---------- Back to top ---------- */
  var toTop = document.getElementById("to-top");
  function toggleToTop() {
    var y = window.scrollY || (lenis ? lenis.scroll : 0);
    toTop.classList.toggle("lb-visible", y > 600);
  }
  if (lenis) lenis.on("scroll", toggleToTop);
  window.addEventListener("scroll", toggleToTop, { passive: true });
  toggleToTop();
  toTop.addEventListener("click", function () {
    if (lenis) lenis.scrollTo(0, { duration: 1.2 });
    else window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* ---------- Announcement bar ---------- */
  var announce = document.getElementById("announcement");
  document.getElementById("announce-close").addEventListener("click", function () {
    announce.style.display = "none";
  });

  /* ---------- Dropdowns (desktop nav) ---------- */
  var drops = Array.prototype.slice.call(document.querySelectorAll(".lb-drop"));
  function closeDrops() {
    drops.forEach(function (d) {
      d.classList.remove("is-open");
      d.querySelector("[data-drop]").setAttribute("aria-expanded", "false");
    });
  }
  drops.forEach(function (d) {
    var btn = d.querySelector("[data-drop]");
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = d.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
      drops.forEach(function (other) {
        if (other !== d) {
          other.classList.remove("is-open");
          other.querySelector("[data-drop]").setAttribute("aria-expanded", "false");
        }
      });
    });
  });
  document.addEventListener("click", closeDrops);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeDrops();
      closeDrawer();
      closeSearch();
    }
  });

  /* ---------- Mobile drawer ---------- */
  var mobileMenu = document.getElementById("mobile-menu");
  var menuOpenBtn = document.getElementById("menu-open");
  var menuCloseBtn = document.getElementById("menu-close");
  var drawerBackdrop = document.getElementById("drawer-backdrop");
  function openDrawer() {
    mobileMenu.classList.add("lb-open");
    mobileMenu.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    menuCloseBtn.focus();
  }
  function closeDrawer() {
    mobileMenu.classList.remove("lb-open");
    mobileMenu.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }
  menuOpenBtn.addEventListener("click", openDrawer);
  menuCloseBtn.addEventListener("click", closeDrawer);
  drawerBackdrop.addEventListener("click", closeDrawer);
  document.querySelectorAll(".lb-mobile-link").forEach(function (a) {
    a.addEventListener("click", closeDrawer);
  });

  /* ---------- Search overlay ---------- */
  var searchOverlay = document.getElementById("search-overlay");
  var overlayInput = document.getElementById("overlay-search-input");
  function openSearch() {
    searchOverlay.classList.add("lb-open");
    searchOverlay.setAttribute("aria-hidden", "false");
    setTimeout(function () { overlayInput.focus(); }, 100);
  }
  function closeSearch() {
    searchOverlay.classList.remove("lb-open");
    searchOverlay.setAttribute("aria-hidden", "true");
  }
  document.getElementById("search-open").addEventListener("click", openSearch);
  document.getElementById("search-close").addEventListener("click", closeSearch);
  document.getElementById("search-backdrop").addEventListener("click", closeSearch);

  /* Popular-search chips fill the visible input */
  document.querySelectorAll(".lb-chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      var term = chip.textContent.trim();
      var input = searchOverlay.classList.contains("lb-open")
        ? overlayInput
        : document.getElementById("hero-search-input");
      input.value = term;
      input.focus();
    });
  });

  /* ---------- Search form (frontend-only) ---------- */
  [document.getElementById("hero-search"), document.getElementById("overlay-search")].forEach(function (form) {
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = form.querySelector("input[type=search]");
      if (input.value.trim()) {
        showToast("Searching “" + input.value.trim() + "”", "Product search is coming soon.");
      }
      input.select();
    });
  });

  /* ---------- Swiper: popular products ---------- */
  if (window.Swiper) {
    new Swiper(".lb-product-swiper", {
      slidesPerView: 1.15,
      spaceBetween: 16,
      grabCursor: true,
      breakpoints: {
        640: { slidesPerView: 2, spaceBetween: 16 },
        1024: { slidesPerView: 3, spaceBetween: 20 },
        1200: { slidesPerView: 4, spaceBetween: 20 },
      },
      navigation: {
        nextEl: ".lb-swiper-next",
        prevEl: ".lb-swiper-prev",
      },
    });
  }

  /* ---------- FAQ accordion ---------- */
  var faqs = Array.prototype.slice.call(document.querySelectorAll(".lb-faq"));
  faqs.forEach(function (faq) {
    var btn = faq.querySelector(".lb-faq-btn");
    var panel = faq.querySelector(".lb-faq-panel");
    btn.addEventListener("click", function () {
      var isOpen = faq.classList.contains("lb-faq-active");
      faqs.forEach(function (f) {
        f.classList.remove("lb-faq-active");
        f.querySelector(".lb-faq-panel").classList.remove("lb-faq-open");
        f.querySelector(".lb-faq-btn").setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        faq.classList.add("lb-faq-active");
        panel.classList.add("lb-faq-open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---------- Cart (frontend-only) ---------- */
  var cartCount = document.getElementById("cart-count");
  var cartTotal = 0;
  function addToCart() {
    cartTotal += 1;
    cartCount.textContent = String(cartTotal);
    showToast("Added to cart", "Checkout is coming soon.");
  }
  document.querySelectorAll(".lb-add-cart").forEach(function (b) {
    b.addEventListener("click", addToCart);
  });
  document.getElementById("cart-btn").addEventListener("click", function () {
    if (cartTotal === 0) {
      showToast("Your cart is empty", "Browse software to add a license.");
    } else {
      showToast("Cart has " + cartTotal + " item" + (cartTotal > 1 ? "s" : ""), "Checkout is coming soon.");
    }
  });

  /* ---------- Toast ---------- */
  var toast = document.getElementById("toast");
  var toastTimer = null;
  function showToast(title, sub) {
    var ps = toast.querySelectorAll("p");
    ps[0].textContent = title;
    ps[1].textContent = sub;
    toast.classList.add("lb-show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("lb-show");
    }, 2600);
  }

  /* ---------- Newsletter (frontend-only) ---------- */
  var newsForm = document.getElementById("newsletter-form");
  var newsStatus = document.getElementById("newsletter-status");
  newsForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var email = document.getElementById("newsletter-email").value.trim();
    var valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!valid) {
      newsStatus.textContent = "Please enter a valid email address.";
      newsStatus.classList.add("text-red-500");
      return;
    }
    newsStatus.classList.remove("text-red-500");
    newsStatus.textContent = "Thanks! You're subscribed. Watch your inbox for deals.";
    newsForm.reset();
  });

  /* ---------- Countdown (visual, non-binding) ---------- */
  var countdown = document.querySelector(".lb-countdown");
  if (countdown) {
    var target = Date.now() + (2 * 24 * 3600 + 14 * 3600 + 32 * 60 + 8) * 1000;
    var units = ["d", "h", "m", "s"];
    function tick() {
      var diff = Math.max(0, target - Date.now());
      var vals = [
        Math.floor(diff / 86400000),
        Math.floor((diff % 86400000) / 3600000),
        Math.floor((diff % 3600000) / 60000),
        Math.floor((diff % 60000) / 1000),
      ];
      vals.forEach(function (v, i) {
        countdown.querySelector('[data-unit="' + units[i] + '"]').textContent =
          String(v).padStart(2, "0") + units[i];
      });
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- Scroll animations (GSAP + ScrollTrigger) ---------- */
  if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    var mm = gsap.matchMedia();

    mm.add("(prefers-reduced-motion: no-preference)", function () {
      /* Hero entrance */
      var heroEls = gsap.utils.toArray(
        ".lb-eyebrow, .lb-hero-title, .lb-hero-sub, .lb-hero-cta, .lb-hero-trust, .lb-hero-visual"
      );
      gsap.set(heroEls, { y: 24, opacity: 0 });
      gsap.timeline({ defaults: { duration: 0.7, ease: "power3.out" } })
        .to(heroEls, { y: 0, opacity: 1, stagger: 0.1 });

      /* Brand strip — reveal only as it enters (content visible by default) */
      ScrollTrigger.create({
        trigger: ".lb-brands",
        start: "top 90%",
        once: true,
        onEnter: function () {
          gsap.fromTo(
            ".lb-brand",
            { y: 12, opacity: 0 },
            { y: 0, opacity: 1, stagger: 0.05, duration: 0.5 }
          );
        },
      });

      /* Staggered card reveals — hide only in the instant they enter (content visible by default,
         so sections can never be left blank if a trigger never fires) */
      gsap.utils.toArray(".lb-stagger").forEach(function (wrap) {
        var items = gsap.utils.toArray(
          wrap.querySelectorAll(".lb-card, .lb-step, .lb-faq, li")
        );
        if (!items.length) return;
        ScrollTrigger.create({
          trigger: wrap,
          start: "top 88%",
          once: true,
          onEnter: function () {
            gsap.fromTo(
              items,
              { y: 26, opacity: 0 },
              { y: 0, opacity: 1, stagger: 0.08, duration: 0.6, ease: "power3.out" }
            );
          },
        });
      });

      /* Counters */
      gsap.utils.toArray(".lb-count").forEach(function (el) {
        var targetVal = parseInt(el.getAttribute("data-count"), 10) || 0;
        var obj = { v: 0 };
        gsap.to(obj, {
          v: targetVal,
          duration: 1.6,
          ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 90%" },
          onUpdate: function () {
            el.textContent = Math.floor(obj.v).toLocaleString("en-US");
          },
        });
      });

      /* Category product counts */
      gsap.utils.toArray(".lb-product-count").forEach(function (el) {
        var targetVal = parseInt(el.getAttribute("data-count"), 10) || 0;
        var obj = { v: 0 };
        gsap.to(obj, {
          v: targetVal,
          duration: 1.4,
          ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 92%" },
          onUpdate: function () {
            el.textContent = Math.floor(obj.v).toLocaleString("en-US") + "+ Products";
          },
        });
      });

      /* Dashboard parallax (hero visual) */
      gsap.to(".lb-hero-visual", {
        y: -18,
        ease: "none",
        scrollTrigger: {
          trigger: ".lb-hero-visual",
          start: "top bottom",
          end: "top top",
          scrub: true,
        },
      });

      ScrollTrigger.refresh();
    });

    window.addEventListener("load", function () {
      ScrollTrigger.refresh();
    });
  }
})();

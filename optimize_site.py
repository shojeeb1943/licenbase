import os
import re
import glob
import subprocess

print("=== LicenBase 100% PageSpeed Optimization Engine ===")

# 1. Update generate_pages.py with all optimizations
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen_content = f.read()

# Replace GTM definitions
gtm_optimized_head = """  <!-- Google Tag Manager (Non-blocking) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function loadGTM() {
      if (window.gtmLoaded) return;
      window.gtmLoaded = true;
      window.dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
      var f = document.getElementsByTagName('script')[0],
          j = document.createElement('script');
      j.async = true;
      j.src = 'https://www.googletagmanager.com/gtm.js?id=' + 'GTM-MWQQGP5R';
      f.parentNode.insertBefore(j, f);
    }
    if ('requestIdleCallback' in window) {
      requestIdleCallback(function() { setTimeout(loadGTM, 1500); });
    } else {
      setTimeout(loadGTM, 2000);
    }
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {
      window.addEventListener(e, loadGTM, { once: true, passive: true });
    });
  </script>
  <!-- End Google Tag Manager -->
"""

gen_content = re.sub(r'GTM_HEAD\s*=\s*""".*?"""', f'GTM_HEAD = """{gtm_optimized_head}"""', gen_content, flags=re.DOTALL)

# Update icon map to use all SVGs
gen_content = gen_content.replace('"cloudlinux.png"', '"cloudlinux.svg"')
gen_content = gen_content.replace('"virtualizor.png"', '"virtualizor.svg"')
gen_content = gen_content.replace('"sitepad.png"', '"sitepad.svg"')
gen_content = gen_content.replace('"whmreseller.png"', '"whmreseller.svg"')
gen_content = gen_content.replace('"softaculous.png"', '"softaculous.svg"')
gen_content = gen_content.replace('"jetbackup.png"', '"jetbackup.svg"')
gen_content = gen_content.replace('"imunify360.png"', '"imunify360.svg"')
gen_content = gen_content.replace('"webuzo.png"', '"webuzo.svg"')

# Update head CSS & font template in generate_pages.py
old_head_block = """  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet" />

  <!-- Swiper -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

  <!-- Custom styles -->
  <link rel="stylesheet" href="assets/css/styles.css?v=5" />

  <!-- Tailwind (Play CDN) -->
  <script src="https://cdn.tailwindcss.com/3.4.16"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: '#1E40AF',
            brandDeep: '#1E3A8A',
            brandSoft: '#EFF4FF',
            navy: '#111827',
            navyLight: '#1F2937',
            accent: '#10B981',
            accentDeep: '#047857',
            accentSoft: '#ECFDF5',
            mist: '#F8FAFC',
          }},
          fontFamily: {{
            sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
            display: ['Manrope', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
          }},
        }},
      }},
    }};
  </script>"""

new_head_block = """  <!-- Fonts (Optimized Non-Blocking) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" /></noscript>

  <!-- Swiper (Non-Blocking) -->
  <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" /></noscript>

  <!-- Precompiled Production CSS -->
  <link rel="stylesheet" href="assets/css/tailwind.min.css?v=1" />
  <link rel="stylesheet" href="assets/css/styles.min.css?v=1" />"""

if old_head_block in gen_content:
    gen_content = gen_content.replace(old_head_block, new_head_block)

# Replace scripts block in generate_pages.py with double-braced f-string
new_scripts_fstring = """  <!-- Deferred Libraries -->
  <script defer src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js" integrity="sha384-hJnF5AwidE18GSWTAGHv3ByzzvfNZ1Tcx5y1UUV3WkauuMCEzBJBMSwSt/PUPXnM" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" integrity="sha384-g4NTh/Iv5PPU4xPyhEWqPcwtNXOvdaDI8LLnyYfyNZOjKJeYQyjzQ9X5275eBjpt" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" integrity="sha384-Z3REaz79l2IaAZqJsSABtTbhjgOUYyV3p90XNnAPCSHg3EMTz1fouunq9WZRtj3d" crossorigin="anonymous"></script>
  <script defer src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js" integrity="sha384-O55L/6rhHr9CFvrxqv5luxOCcmVaBmETbZbJDP+Do8T0pztTACsFBD/IXCNkj7DV" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" integrity="sha384-2UI1PfnXFjVMQ7/ZDEF70CR943oH3v6uZrFQGGqJYlvhh4g6z6uVktxYbOlAczav" crossorigin="anonymous"></script>

  <!-- Lazy-Loaded Tawk.to Live Chat -->
  <script>
    function loadTawk() {{
      if (window.tawkLoaded) return;
      window.tawkLoaded = true;
      window.Tawk_API = window.Tawk_API || {{}};
      window.Tawk_LoadStart = new Date();
      var s1 = document.createElement("script"), s0 = document.getElementsByTagName("script")[0];
      s1.async = true;
      s1.src = 'https://embed.tawk.to/6aa54c1357bdd83448ee36a5/1k2ar2bta';
      s1.charset = 'UTF-8';
      s1.setAttribute('crossorigin', '*');
      s0.parentNode.insertBefore(s1, s0);
    }}
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {{
      window.addEventListener(e, loadTawk, {{ once: true, passive: true }});
    }});
    if ('requestIdleCallback' in window) {{
      requestIdleCallback(function() {{ setTimeout(loadTawk, 3500); }});
    }} else {{
      setTimeout(loadTawk, 4000);
    }}
  </script>

  <script defer src="assets/js/main.js?v=7"></script>"""

# Replace whichever scripts block currently exists in generate_pages.py
gen_content = re.sub(r'<!-- (?:Libraries|Deferred Libraries) -->[\s\S]*?<script defer src="assets/js/main\.js\?v=\d+"></script>|<!-- Libraries -->[\s\S]*?<script src="assets/js/main\.js\?v=\d+"></script>', new_scripts_fstring, gen_content)

# Fix logo img tags in generate_pages.py with width/height/priority
gen_content = gen_content.replace(
    '<img src="assets/img/logo.png" alt="LicenBase" class="lb-logo-img" />',
    '<img src="assets/img/logo.png" alt="LicenBase" class="lb-logo-img" width="250" height="100" fetchpriority="high" decoding="async" />'
)
gen_content = gen_content.replace(
    '<img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" />',
    '<img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" width="250" height="100" loading="lazy" decoding="async" />'
)
gen_content = gen_content.replace(
    '<img src="assets/img/logo.png" alt="LicenBase" class="h-7 w-auto" />',
    '<img src="assets/img/logo.png" alt="LicenBase" class="h-7 w-auto" width="70" height="28" loading="lazy" decoding="async" />'
)

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_content)

print("Updated generate_pages.py successfully!")

# Run generate_pages.py to update all 13 product pages
subprocess.run(["python", "generate_pages.py"], check=True)

# Now optimize all HTML files across the project
OPTIMIZED_GTM_HEAD = """  <!-- Google Tag Manager (Non-blocking) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function loadGTM() {
      if (window.gtmLoaded) return;
      window.gtmLoaded = true;
      window.dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
      var f = document.getElementsByTagName('script')[0],
          j = document.createElement('script');
      j.async = true;
      j.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-MWQQGP5R';
      f.parentNode.insertBefore(j, f);
    }
    if ('requestIdleCallback' in window) {
      requestIdleCallback(function() { setTimeout(loadGTM, 1500); });
    } else {
      setTimeout(loadGTM, 2000);
    }
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {
      window.addEventListener(e, loadGTM, { once: true, passive: true });
    });
  </script>
  <!-- End Google Tag Manager -->"""

OPTIMIZED_HEAD_CSS = """  <!-- Fonts (Optimized Non-Blocking) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" /></noscript>

  <!-- Swiper (Non-Blocking) -->
  <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" /></noscript>

  <!-- Precompiled Production CSS -->
  <link rel="stylesheet" href="assets/css/tailwind.min.css?v=1" />
  <link rel="stylesheet" href="assets/css/styles.min.css?v=1" />"""

OPTIMIZED_BOTTOM_SCRIPTS = """  <!-- Deferred Libraries -->
  <script defer src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js" integrity="sha384-hJnF5AwidE18GSWTAGHv3ByzzvfNZ1Tcx5y1UUV3WkauuMCEzBJBMSwSt/PUPXnM" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" integrity="sha384-g4NTh/Iv5PPU4xPyhEWqPcwtNXOvdaDI8LLnyYfyNZOjKJeYQyjzQ9X5275eBjpt" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" integrity="sha384-Z3REaz79l2IaAZqJsSABtTbhjgOUYyV3p90XNnAPCSHg3EMTz1fouunq9WZRtj3d" crossorigin="anonymous"></script>
  <script defer src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js" integrity="sha384-O55L/6rhHr9CFvrxqv5luxOCcmVaBmETbZbJDP+Do8T0pztTACsFBD/IXCNkj7DV" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" integrity="sha384-2UI1PfnXFjVMQ7/ZDEF70CR943oH3v6uZrFQGGqJYlvhh4g6z6uVktxYbOlAczav" crossorigin="anonymous"></script>

  <!-- Lazy-Loaded Tawk.to Live Chat -->
  <script>
    function loadTawk() {
      if (window.tawkLoaded) return;
      window.tawkLoaded = true;
      window.Tawk_API = window.Tawk_API || {};
      window.Tawk_LoadStart = new Date();
      var s1 = document.createElement("script"), s0 = document.getElementsByTagName("script")[0];
      s1.async = true;
      s1.src = 'https://embed.tawk.to/6aa54c1357bdd83448ee36a5/1k2ar2bta';
      s1.charset = 'UTF-8';
      s1.setAttribute('crossorigin', '*');
      s0.parentNode.insertBefore(s1, s0);
    }
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {
      window.addEventListener(e, loadTawk, { once: true, passive: true });
    });
    if ('requestIdleCallback' in window) {
      requestIdleCallback(function() { setTimeout(loadTawk, 3500); });
    } else {
      setTimeout(loadTawk, 4000);
    }
  </script>

  <script defer src="assets/js/main.js?v=7"></script>"""

html_files = glob.glob("*.html")
print(f"Optimizing {len(html_files)} HTML files...")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace GTM in head
    html = re.sub(r'<!-- Google Tag Manager -->[\s\S]*?<!-- End Google Tag Manager -->', OPTIMIZED_GTM_HEAD, html)

    # 2. Replace fonts, swiper, custom css, tailwind play cdn in head
    head_pattern = r'<!-- Fonts -->[\s\S]*?(?:<!-- Tailwind \(Play CDN\)[^>]*-->[\s\S]*?</script>\s*</head>|<script src="https://cdn\.tailwindcss\.com[\s\S]*?</script>\s*</head>)'
    if re.search(head_pattern, html):
        html = re.sub(head_pattern, OPTIMIZED_HEAD_CSS + "\n</head>", html)

    # 3. Replace bottom script blocks
    bottom_pattern = r'<!-- (?:Libraries|Deferred Libraries) -->[\s\S]*?</body>'
    if re.search(bottom_pattern, html):
        html = re.sub(bottom_pattern, OPTIMIZED_BOTTOM_SCRIPTS + "\n</body>", html)
    else:
        # Check if tawk script is present separately
        bottom_pattern2 = r'<!--Start of Tawk\.to Script-->[\s\S]*?</body>'
        if re.search(bottom_pattern2, html):
            html = re.sub(bottom_pattern2, OPTIMIZED_BOTTOM_SCRIPTS + "\n</body>", html)

    # Remove annotate.js
    html = re.sub(r'\s*<script src="assets/js/annotate\.js"></script>', '', html)

    # Replace PNG icons with SVG icons
    html = html.replace('assets/img/icons/cloudlinux.png', 'assets/img/icons/cloudlinux.svg')
    html = html.replace('assets/img/icons/virtualizor.png', 'assets/img/icons/virtualizor.svg')
    html = html.replace('assets/img/icons/sitepad.png', 'assets/img/icons/sitepad.svg')
    html = html.replace('assets/img/icons/whmreseller.png', 'assets/img/icons/whmreseller.svg')
    html = html.replace('assets/img/icons/softaculous.png', 'assets/img/icons/softaculous.svg')
    html = html.replace('assets/img/icons/jetbackup.png', 'assets/img/icons/jetbackup.svg')
    html = html.replace('assets/img/icons/imunify360.png', 'assets/img/icons/imunify360.svg')
    html = html.replace('assets/img/icons/webuzo.png', 'assets/img/icons/webuzo.svg')

    # Add dimensions and lazy loading to images
    # Top logo
    html = re.sub(
        r'<img src="assets/img/logo\.png" alt="LicenBase" class="lb-logo-img"[^>]*>',
        '<img src="assets/img/logo.png" alt="LicenBase" class="lb-logo-img" width="250" height="100" fetchpriority="high" decoding="async" />',
        html
    )
    # Footer logo
    html = re.sub(
        r'<img src="assets/img/logo\.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto"[^>]*>',
        '<img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" width="250" height="100" loading="lazy" decoding="async" />',
        html
    )
    # Footer bottom small logo
    html = re.sub(
        r'<img src="assets/img/logo\.png" alt="LicenBase" class="h-([78]) w-auto"[^>]*>',
        r'<img src="assets/img/logo.png" alt="LicenBase" class="h-\1 w-auto" width="70" height="28" loading="lazy" decoding="async" />',
        html
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Optimized {file}")

print("All HTML files processed! Now rebuilding CSS...")
subprocess.run(["python", "build_css.py"], check=True)
print("Site-wide 100% PageSpeed optimization completed!")

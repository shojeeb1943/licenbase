import os
import re

print("Starting integration of official brand icons & logos...")

# Define map of product slug -> exact downloaded asset
PRODUCT_ASSETS = {
    "cpanel": "cpanel.svg",
    "litespeed": "litespeed.svg",
    "plesk": "plesk.svg",
    "whmcs": "whmcs.svg",
    "cloudlinux": "cloudlinux.png",
    "virtualizor": "virtualizor.png",
    "imunify360": "imunify360.png",
    "jetbackup": "jetbackup.png",
    "softaculous": "softaculous.png",
    "sitepad": "sitepad.png",
    "whmreseller": "whmreseller.png",
    "webuzo": "webuzo.png",
    "wp-squared": "wp-squared.svg",
    "wpsquared": "wp-squared.svg"
}

# Product pages list
PRODUCTS_LIST = [
    ("cpanel-license.html", "cPanel License", "cpanel.svg"),
    ("litespeed-license.html", "LiteSpeed License", "litespeed.svg"),
    ("plesk-license.html", "Plesk License", "plesk.svg"),
    ("whmcs-license.html", "WHMCS License", "whmcs.svg"),
    ("cloudlinux-license.html", "CloudLinux License", "cloudlinux.png"),
    ("virtualizor-license.html", "Virtualizor License", "virtualizor.png"),
    ("sitepad-license.html", "SitePad License", "sitepad.png"),
    ("whmreseller-license.html", "WHMReseller License", "whmreseller.png"),
    ("softaculous-license.html", "Softaculous License", "softaculous.png"),
    ("jetbackup-license.html", "JetBackup License", "jetbackup.png"),
    ("imunify360-license.html", "Imunify360 License", "imunify360.png"),
    ("webuzo-license.html", "Webuzo Control Panel", "webuzo.png"),
    ("wp-squared-license.html", "WP Squared", "wp-squared.svg")
]

# Build Mega Menu HTML
mega_menu_html = '''                <div class="lb-mega-tiles">
'''
for url, title, icon_file in PRODUCTS_LIST:
    mega_menu_html += f'''                  <a href="{url}" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/{icon_file}" alt="{title}" class="h-4 w-4 shrink-0 object-contain" />
                    <span>{title}</span>
                  </a>\n'''
mega_menu_html += '                </div>'

# 1. Update generate_pages.py
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

# Replace the mega menu
gen_code = re.sub(r'<div class="lb-mega-tiles">[\s\S]*?</div>\s*</div>\s*</div>', mega_menu_html + '\n              </div>\n            </div>', gen_code, count=1)

# Ensure hero badge, hero visual card, and related cards use correct extension (.svg or .png)
gen_code = re.sub(
    r'<div class="inline-flex items-center gap-2\.5 rounded-full bg-brandSoft px-3\.5 py-1\.5 text-xs font-bold uppercase tracking-wider text-brand">\s*<img src="assets/img/icons/[^"]+"[^>]*>\s*<span>{p\["badge"\]}</span>\s*</div>',
    '''<div class="inline-flex items-center gap-2.5 rounded-full bg-brandSoft px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-brand">
            <img src="assets/img/icons/{'wp-squared.svg' if p['slug'] in ('wpsquared', 'wp-squared') else ('cloudlinux.png' if p['slug'] == 'cloudlinux' else ('virtualizor.png' if p['slug'] == 'virtualizor' else ('imunify360.png' if p['slug'] == 'imunify360' else ('jetbackup.png' if p['slug'] == 'jetbackup' else ('softaculous.png' if p['slug'] == 'softaculous' else ('sitepad.png' if p['slug'] == 'sitepad' else ('whmreseller.png' if p['slug'] == 'whmreseller' else ('webuzo.png' if p['slug'] == 'webuzo' else p['slug'] + '.svg'))))))))}" alt="{p['slug']}" class="h-4 w-4 object-contain" />
            <span>{p["badge"]}</span>
          </div>''',
    gen_code
)

gen_code = re.sub(
    r'<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm">\s*<img src="assets/img/icons/[^"]+"[^>]*>\s*</span>',
    '''<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm">
                  <img src="assets/img/icons/{'wp-squared.svg' if p['slug'] in ('wpsquared', 'wp-squared') else ('cloudlinux.png' if p['slug'] == 'cloudlinux' else ('virtualizor.png' if p['slug'] == 'virtualizor' else ('imunify360.png' if p['slug'] == 'imunify360' else ('jetbackup.png' if p['slug'] == 'jetbackup' else ('softaculous.png' if p['slug'] == 'softaculous' else ('sitepad.png' if p['slug'] == 'sitepad' else ('whmreseller.png' if p['slug'] == 'whmreseller' else ('webuzo.png' if p['slug'] == 'webuzo' else p['slug'] + '.svg'))))))))}" alt="{p['slug']}" class="h-8 w-8 object-contain" />
                </span>''',
    gen_code
)

# Update icon_map inside generate_pages.py
old_icon_map = '''        "cpanel-license.html": "cpanel.svg",
        "litespeed-license.html": "litespeed.svg",
        "plesk-license.html": "plesk.svg",
        "whmcs-license.html": "whmcs.svg",
        "cloudlinux-license.html": "cloudlinux.svg",
        "virtualizor-license.html": "virtualizor.svg",
        "sitepad-license.html": "sitepad.svg",
        "whmreseller-license.html": "whmreseller.svg",
        "softaculous-license.html": "softaculous.svg",
        "jetbackup-license.html": "jetbackup.svg",
        "imunify360-license.html": "imunify360.svg",
        "webuzo-license.html": "webuzo.svg",
        "wp-squared-license.html": "wp-squared.svg"'''

new_icon_map = '''        "cpanel-license.html": "cpanel.svg",
        "litespeed-license.html": "litespeed.svg",
        "plesk-license.html": "plesk.svg",
        "whmcs-license.html": "whmcs.svg",
        "cloudlinux-license.html": "cloudlinux.png",
        "virtualizor-license.html": "virtualizor.png",
        "sitepad-license.html": "sitepad.png",
        "whmreseller-license.html": "whmreseller.png",
        "softaculous-license.html": "softaculous.png",
        "jetbackup-license.html": "jetbackup.png",
        "imunify360-license.html": "imunify360.png",
        "webuzo-license.html": "webuzo.png",
        "wp-squared-license.html": "wp-squared.svg"'''

if old_icon_map in gen_code:
    gen_code = gen_code.replace(old_icon_map, new_icon_map)

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_code)

print("Updated generate_pages.py. Generating 13 pages...")
os.system("python generate_pages.py")

# 2. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

index_content = re.sub(r'<div class="lb-mega-tiles">[\s\S]*?</div>\s*</div>\s*</div>', mega_menu_html + '\n              </div>\n            </div>', index_content, count=1)

# Update Hero Active Server Licenses
index_content = re.sub(
    r'<ul class="lb-hero-license-list">[\s\S]*?</ul>',
    '''<ul class="lb-hero-license-list">
                <li class="lb-hero-license">
                  <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-9 w-9 shrink-0 object-contain rounded-xl shadow-sm" />
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">cPanel &amp; WHM (Dedicated)</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
                <li class="lb-hero-license">
                  <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-9 w-9 shrink-0 object-contain rounded-xl shadow-sm" />
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">LiteSpeed Web Server (4-Core)</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
                <li class="lb-hero-license">
                  <img src="assets/img/icons/cloudlinux.png" alt="CloudLinux" class="h-9 w-9 shrink-0 object-contain rounded-xl shadow-sm" />
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">CloudLinux OS Shared Pro</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
              </ul>''',
    index_content,
    count=1
)

# Update Trusted Brands Bar
index_content = re.sub(
    r'<div class="lb-brands mt-8 flex flex-wrap items-center justify-center gap-x-10 gap-y-6 lg:justify-between">[\s\S]*?</div>\s*</div>\s*</section>',
    '''<div class="lb-brands mt-8 flex flex-wrap items-center justify-center gap-x-10 gap-y-6 lg:justify-between">
        <!-- cPanel -->
        <div class="lb-brand-item flex items-center gap-2.5" title="cPanel">
          <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">cPanel</span>
        </div>
        <!-- LiteSpeed -->
        <div class="lb-brand-item flex items-center gap-2.5" title="LiteSpeed">
          <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">LiteSpeed</span>
        </div>
        <!-- Plesk -->
        <div class="lb-brand-item flex items-center gap-2.5" title="Plesk">
          <img src="assets/img/icons/plesk.svg" alt="Plesk" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">Plesk</span>
        </div>
        <!-- CloudLinux -->
        <div class="lb-brand-item flex items-center gap-2.5" title="CloudLinux">
          <img src="assets/img/icons/cloudlinux.png" alt="CloudLinux" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">CloudLinux</span>
        </div>
        <!-- WHMCS -->
        <div class="lb-brand-item flex items-center gap-2.5" title="WHMCS">
          <img src="assets/img/icons/whmcs.svg" alt="WHMCS" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">WHMCS</span>
        </div>
        <!-- Imunify360 -->
        <div class="lb-brand-item flex items-center gap-2.5" title="Imunify360">
          <img src="assets/img/icons/imunify360.png" alt="Imunify360" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">Imunify360</span>
        </div>
      </div>
    </div>
  </section>''',
    index_content,
    count=1
)

# Update Swiper slides in index.html
swiper_icons = {
    'cpanel.svg': 'cpanel.svg',
    'litespeed.svg': 'litespeed.svg',
    'plesk.svg': 'plesk.svg',
    'cloudlinux.svg': 'cloudlinux.png',
    'whmcs.svg': 'whmcs.svg',
    'imunify360.svg': 'imunify360.png',
    'jetbackup.svg': 'jetbackup.png',
    'virtualizor.svg': 'virtualizor.png',
    'softaculous.svg': 'softaculous.png',
    'sitepad.svg': 'sitepad.png',
    'whmreseller.svg': 'whmreseller.png',
    'webuzo.svg': 'webuzo.png',
    'wp-squared.svg': 'wp-squared.svg'
}

for old_i, new_i in swiper_icons.items():
    index_content = index_content.replace(f'assets/img/icons/{old_i}', f'assets/img/icons/{new_i}')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("Updated index.html.")

# 3. Update products.html
with open("products.html", "r", encoding="utf-8") as f:
    prod_content = f.read()

prod_content = re.sub(r'<div class="lb-mega-tiles">[\s\S]*?</div>\s*</div>\s*</div>', mega_menu_html + '\n              </div>\n            </div>', prod_content, count=1)

for old_i, new_i in swiper_icons.items():
    prod_content = prod_content.replace(f'assets/img/icons/{old_i}', f'assets/img/icons/{new_i}')

with open("products.html", "w", encoding="utf-8") as f:
    f.write(prod_content)

print("Updated products.html.")

# 4. Update deals.html
with open("deals.html", "r", encoding="utf-8") as f:
    deals_content = f.read()

deals_content = re.sub(r'<div class="lb-mega-tiles">[\s\S]*?</div>\s*</div>\s*</div>', mega_menu_html + '\n              </div>\n            </div>', deals_content, count=1)

for old_i, new_i in swiper_icons.items():
    deals_content = deals_content.replace(f'assets/img/icons/{old_i}', f'assets/img/icons/{new_i}')

with open("deals.html", "w", encoding="utf-8") as f:
    f.write(deals_content)

print("Updated deals.html.")

# 5. Update legal pages
legal_pages = ["terms-of-service.html", "privacy-policy.html", "refund-policy.html", "license-policy.html"]
for lp in legal_pages:
    if os.path.exists(lp):
        with open(lp, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<div class="lb-mega-tiles">[\s\S]*?</div>\s*</div>\s*</div>', mega_menu_html + '\n              </div>\n            </div>', c, count=1)
        with open(lp, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {lp}")

print("ALL PAGES FULLY SYNCHRONIZED WITH BRAND LOGOS & ICONS!")

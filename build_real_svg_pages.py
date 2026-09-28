import os
import re

print("Starting SVG icon replacement across all pages...")

# 1. Update generate_pages.py so all 13 product pages are generated with real SVGs
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen_content = f.read()

# Map related items icon filenames
related_icon_map = {
    "cpanel-license.html": "cpanel.svg",
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
    "wp-squared-license.html": "wp-squared.svg"
}

# Add icon_file to each product dictionary in generate_pages.py
slug_to_icon = {
    "cpanel": "cpanel.svg",
    "litespeed": "litespeed.svg",
    "plesk": "plesk.svg",
    "whmcs": "whmcs.svg",
    "cloudlinux": "cloudlinux.svg",
    "virtualizor": "virtualizor.svg",
    "sitepad": "sitepad.svg",
    "whmreseller": "whmreseller.svg",
    "softaculous": "softaculous.svg",
    "jetbackup": "jetbackup.svg",
    "imunify360": "imunify360.svg",
    "webuzo": "webuzo.svg",
    "wpsquared": "wp-squared.svg",
    "wp-squared": "wp-squared.svg"
}

# Let's inspect generate_pages.py to update mega menu, hero badge, visual card, and related products.
# Update mega menu in generate_pages.py
old_mega_menu = '''                <div class="lb-mega-tiles">
                  <a href="cpanel-license.html" class="lb-mega-tile">cPanel License</a>
                  <a href="litespeed-license.html" class="lb-mega-tile">LiteSpeed License</a>
                  <a href="plesk-license.html" class="lb-mega-tile">Plesk License</a>
                  <a href="whmcs-license.html" class="lb-mega-tile">WHMCS License</a>
                  <a href="cloudlinux-license.html" class="lb-mega-tile">CloudLinux License</a>
                  <a href="virtualizor-license.html" class="lb-mega-tile">Virtualizor License</a>
                  <a href="sitepad-license.html" class="lb-mega-tile">SitePad License</a>
                  <a href="whmreseller-license.html" class="lb-mega-tile">WHMReseller License</a>
                  <a href="softaculous-license.html" class="lb-mega-tile">Softaculous License</a>
                  <a href="jetbackup-license.html" class="lb-mega-tile">JetBackup License</a>
                  <a href="imunify360-license.html" class="lb-mega-tile">Imunify360 License</a>
                  <a href="webuzo-license.html" class="lb-mega-tile">Webuzo Control Panel</a>
                  <a href="wp-squared-license.html" class="lb-mega-tile">WP Squared</a>
                </div>'''

new_mega_menu = '''                <div class="lb-mega-tiles">
                  <a href="cpanel-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-4 w-4 shrink-0 object-contain" />
                    <span>cPanel License</span>
                  </a>
                  <a href="litespeed-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-4 w-4 shrink-0 object-contain" />
                    <span>LiteSpeed License</span>
                  </a>
                  <a href="plesk-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/plesk.svg" alt="Plesk" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Plesk License</span>
                  </a>
                  <a href="whmcs-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmcs.svg" alt="WHMCS" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WHMCS License</span>
                  </a>
                  <a href="cloudlinux-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-4 w-4 shrink-0 object-contain" />
                    <span>CloudLinux License</span>
                  </a>
                  <a href="virtualizor-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/virtualizor.svg" alt="Virtualizor" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Virtualizor License</span>
                  </a>
                  <a href="sitepad-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/sitepad.svg" alt="SitePad" class="h-4 w-4 shrink-0 object-contain" />
                    <span>SitePad License</span>
                  </a>
                  <a href="whmreseller-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmreseller.svg" alt="WHMReseller" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WHMReseller License</span>
                  </a>
                  <a href="softaculous-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/softaculous.svg" alt="Softaculous" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Softaculous License</span>
                  </a>
                  <a href="jetbackup-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/jetbackup.svg" alt="JetBackup" class="h-4 w-4 shrink-0 object-contain" />
                    <span>JetBackup License</span>
                  </a>
                  <a href="imunify360-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Imunify360 License</span>
                  </a>
                  <a href="webuzo-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/webuzo.svg" alt="Webuzo" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Webuzo Control Panel</span>
                  </a>
                  <a href="wp-squared-license.html" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/wp-squared.svg" alt="WP Squared" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WP Squared</span>
                  </a>
                </div>'''

if old_mega_menu in gen_content:
    gen_content = gen_content.replace(old_mega_menu, new_mega_menu)

# Update related items rendering in generate_pages.py
old_related_code = '''    related_html = ""
    for rel in p["related"]:
        related_html += f"""
        <div class="group relative flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-brand/40 hover:shadow-xl">
          <div>
            <div class="flex items-center justify-between">
              <span class="grid h-11 w-11 place-items-center rounded-xl bg-brandSoft text-brand transition-colors group-hover:bg-brand group-hover:text-white">
                <i data-lucide="{rel['icon']}" class="h-5 w-5"></i>
              </span>
              <span class="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-bold text-accentDeep">{rel['price']}</span>
            </div>'''

new_related_code = '''    related_html = ""
    icon_map = {
        "cpanel-license.html": "cpanel.svg",
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
        "wp-squared-license.html": "wp-squared.svg"
    }
    for rel in p["related"]:
        rel_icon = icon_map.get(rel['url'], 'cpanel.svg')
        related_html += f"""
        <div class="group relative flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-brand/40 hover:shadow-xl">
          <div>
            <div class="flex items-center justify-between">
              <span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-110">
                <img src="assets/img/icons/{rel_icon}" alt="{rel['title']}" class="h-7 w-7 object-contain" />
              </span>
              <span class="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-bold text-accentDeep">{rel['price']}</span>
            </div>'''

if old_related_code in gen_content:
    gen_content = gen_content.replace(old_related_code, new_related_code)

# Update hero badge & visual card in generate_pages.py
old_hero_badge = '''          <div class="inline-flex items-center gap-2 rounded-full bg-brandSoft px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-brand">
            <i data-lucide="{p['icon']}" class="h-4 w-4"></i> {p["badge"]}
          </div>'''

new_hero_badge = '''          <div class="inline-flex items-center gap-2.5 rounded-full bg-brandSoft px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-brand">
            <img src="assets/img/icons/{p['slug'] if p['slug'] != 'wpsquared' else 'wp-squared'}.svg" alt="{p['slug']}" class="h-4 w-4 object-contain" />
            <span>{p["badge"]}</span>
          </div>'''

if old_hero_badge in gen_content:
    gen_content = gen_content.replace(old_hero_badge, new_hero_badge)

old_hero_card_icon = '''              <div class="flex items-center gap-3">
                <span class="grid h-12 w-12 place-items-center rounded-2xl bg-brand text-white shadow-md shadow-brand/30">
                  <i data-lucide="{p['icon']}" class="h-6 w-6"></i>
                </span>
                <div>
                  <h2 class="font-display text-lg font-bold text-navy">{p["title"].split('(')[0]}</h2>
                  <p class="text-xs text-gray-400">Verified IP-Bound Authentication</p>
                </div>
              </div>'''

new_hero_card_icon = '''              <div class="flex items-center gap-3">
                <span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm">
                  <img src="assets/img/icons/{p['slug'] if p['slug'] != 'wpsquared' else 'wp-squared'}.svg" alt="{p['slug']}" class="h-8 w-8 object-contain" />
                </span>
                <div>
                  <h2 class="font-display text-lg font-bold text-navy">{p["title"].split('(')[0]}</h2>
                  <p class="text-xs text-gray-400">Verified IP-Bound Authentication</p>
                </div>
              </div>'''

if old_hero_card_icon in gen_content:
    gen_content = gen_content.replace(old_hero_card_icon, new_hero_card_icon)

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_content)

print("Updated generate_pages.py. Now executing generate_pages.py...")
os.system("python generate_pages.py")

# 2. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Update mega menu in index.html
if old_mega_menu in index_html:
    index_html = index_html.replace(old_mega_menu, new_mega_menu)

# Update Hero Active Server Licenses in index.html
old_hero_licenses = '''              <ul class="lb-hero-license-list">
                <li class="lb-hero-license">
                  <span class="lb-hero-license-icon lb-hero-license-icon--cp">cP</span>
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">cPanel &amp; WHM (Dedicated)</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
                <li class="lb-hero-license">
                  <span class="lb-hero-license-icon" style="background:#EFF6FF;color:#0070BA;font-weight:700;font-size:12px;display:grid;place-items:center;width:36px;height:36px;border-radius:10px;">LS</span>
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">LiteSpeed Web Server (4-Core)</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
                <li class="lb-hero-license">
                  <span class="lb-hero-license-icon" style="background:#EFF6FF;color:#1B4D89;font-weight:700;font-size:12px;display:grid;place-items:center;width:36px;height:36px;border-radius:10px;">CL</span>
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">CloudLinux OS Shared Pro</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
              </ul>'''

new_hero_licenses = '''              <ul class="lb-hero-license-list">
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
                  <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-9 w-9 shrink-0 object-contain rounded-xl shadow-sm" />
                  <div class="lb-hero-license-copy">
                    <p class="lb-hero-license-name">CloudLinux OS Shared Pro</p>
                    <p class="lb-hero-license-meta">IP: 198.51.100.42 · Auto-renews in 18 days</p>
                  </div>
                  <span class="lb-hero-license-status">Active</span>
                </li>
              </ul>'''

if old_hero_licenses in index_html:
    index_html = index_html.replace(old_hero_licenses, new_hero_licenses)

# Update Trusted Brands bar
old_brands_bar = '''      <div class="lb-brands mt-8 flex flex-wrap items-center justify-center gap-x-10 gap-y-6 lg:justify-between">
        <!-- cPanel -->
        <div class="lb-brand-item flex items-center gap-2" title="cPanel">
          <svg class="h-6 w-6" viewBox="0 0 24 24" fill="#FF6C2C" xmlns="http://www.w3.org/2000/svg" aria-label="cPanel"><path d="M4.586 9.346a.538.538 0 00-.34.113.561.561 0 00-.197.299L2.74 14.654h.922a.528.528 0 00.332-.113.561.561 0 00.2-.291l.968-3.604h.744a.677.677 0 01.317.077.703.703 0 01.24.199.732.732 0 01.129.281.65.65 0 01-.01.326.698.698 0 01-.676.526h-.385a.538.538 0 00-.337.113.561.561 0 00-.2.291l-.24.896h1.201a1.939 1.939 0 001.62-.867 1.988 1.988 0 00.265-.586l.027-.1a1.854 1.854 0 00.026-.907 1.973 1.973 0 00-1.031-1.34 1.875 1.875 0 00-.88-.21H4.587zm18.447 0a.401.401 0 00-.25.082.377.377 0 00-.14.217l-1.334 5.01a1.7 1.7 0 00.57-.096 1.806 1.806 0 00.496-.266 1.74 1.74 0 00.385-.408 1.648 1.648 0 00.234-.531l.996-3.696a.23.23 0 00-.045-.217.246.246 0 00-.2-.095h-.712zM8.381 10.643l-.133.503a.564.564 0 00-.006.26.544.544 0 00.1.221.552.552 0 00.185.154.53.53 0 00.252.06h2.157a.101.101 0 01.084.038.098.098 0 01.015.088l-.02.072-.324 1.201-.013.055a.172.172 0 01-.067.105.205.205 0 01-.127.04H9.178a.147.147 0 01-.12-.057.136.136 0 01-.027-.13c.022-.074.071-.112.147-.112h.808a.53.53 0 00.332-.112.564.564 0 00.2-.293l.132-.498H8.84a1.131 1.131 0 00-.38.065 1.152 1.152 0 00-.323.176 1.194 1.194 0 00-.256.271 1.052 1.052 0 00-.156.346l-.028.1a1.095 1.095 0 00-.013.533 1.203 1.203 0 00.212.464 1.141 1.141 0 00.918.453l2.157.006a.899.899 0 00.875-.67l.525-1.95a1.101 1.101 0 00.01-.514 1.114 1.114 0 00-.205-.444 1.149 1.149 0 00-.377-.312 1.048 1.048 0 00-.498-.12H8.38zm-6.397.01a1.924 1.924 0 00-.638.107 1.989 1.989 0 00-.553.295 1.962 1.962 0 00-.7 1.045l-.027.1a1.936 1.936 0 00-.023.905 1.955 1.955 0 00.361.786 1.986 1.986 0 00.668.554 1.875 1.875 0 00.88.21h.464l.266-.983a.23.23 0 00-.043-.215.239.239 0 00-.198-.096h-.423a.702.702 0 01-.319-.074.67.67 0 01-.24-.195.732.732 0 01-.127-.281.706.706 0 01.01-.34.73.73 0 01.256-.377.675.675 0 01.42-.14h.697a.538.538 0 00.338-.114.561.561 0 00.199-.297l.232-.89h-1.5zm11.08 0l-.982 3.689a.23.23 0 00.045.217.238.238 0 00.195.095h.711a.413.413 0 00.248-.08.363.363 0 00.143-.21l.644-2.41h.745a.678.678 0 01.318.075.708.708 0 01.238.2.735.735 0 01.129.28.65.65 0 01-.01.327l-.398 1.506a.243.243 0 00.24.312h.713a.403.403 0 00.244-.08.366.366 0 00.143-.213l.332-1.248a1.897 1.897 0 00.029-.908 1.955 1.955 0 00-.361-.79 1.987 1.987 0 00-.668-.554 1.889 1.889 0 00-.885-.209h-1.813zm5.793 0a1.458 1.458 0 00-.488.081 1.489 1.489 0 00-.752.58 1.493 1.493 0 00-.205.454l-.406 1.505a1.018 1.018 0 00-.016.508 1.139 1.139 0 00.205.446 1.095 1.095 0 00.377.312 1.071 1.071 0 00.498.115h2.502a.528.528 0 00.332-.113.561.561 0 00.2-.291l.21-.791h-2.748a.2.2 0 01-.191-.252l.299-1.127a.34.34 0 01.113-.162.281.281 0 01.18-.064h1.232a.153.153 0 01.147.193l-.026.1c-.022.075-.071.113-.146.113h-.81a.538.538 0 00-.339.111.526.526 0 00-.191.293l-.133.49h2.004a.887.887 0 00.547-.181.864.864 0 00.32-.483l.12-.45a1.11 1.11 0 00.013-.513 1.076 1.076 0 00-.203-.443 1.146 1.146 0 00-.375-.313 1.047 1.047 0 00-.498-.119h-1.772Z"/></svg>
          <span class="font-display text-lg font-extrabold text-navy">cPanel</span>
        </div>
        <!-- LiteSpeed -->
        <div class="lb-brand-item" title="LiteSpeed Technologies">
          <svg class="h-7 w-auto" viewBox="0 0 135 28" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="LiteSpeed">
            <path d="M7.5 2C7.5 2 13 8 13 13.5C13 17 10.5 20 7.5 20C4.5 20 2 17 2 13.5C2 10.5 5 6 7.5 2Z" fill="#0070BA"/>
            <path d="M12 7C12 7 18 13 18 18C18 22 15 25 12 25C9.5 25 7.5 22.5 7.5 19.5C7.5 16 10 11.5 12 7Z" fill="#00A2FF"/>
            <text x="24" y="19.5" fill="#24292F" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" letter-spacing="-0.3px">Lite<tspan fill="#0070BA">Speed</tspan></text>
          </svg>
        </div>
        <!-- Plesk -->
        <div class="lb-brand-item flex items-center gap-2" title="Plesk">
          <svg class="h-6 w-6" viewBox="0 0 24 24" fill="#52BBE6" xmlns="http://www.w3.org/2000/svg" aria-label="Plesk"><path d="M6.102 7.021v7.353h.736V7.02zm13.655.01v7.343h.735V7.032zm.735 4.633l2.479 2.71h1.019l-2.574-2.731L24 9.122h-.987zm-4.008-2.636c-.536 0-.972.125-1.31.378-.337.252-.505.609-.505 1.07 0 .26.049.474.148.642.1.168.226.306.38.415.154.108.328.198.522.267.194.07.39.134.59.19.175.049.342.1.5.152.158.052.297.117.418.194.12.077.216.17.286.278.07.109.104.244.104.405 0 .21-.095.388-.286.535-.19.147-.484.221-.88.221-.609 0-1.104-.245-1.485-.735l-.572.504c.286.315.59.54.913.678.322.136.693.204 1.11.204.272 0 .527-.033.766-.1a1.89 1.89 0 00.621-.294c.176-.13.316-.288.419-.478.102-.189.153-.402.153-.64 0-.26-.051-.474-.153-.646a1.46 1.46 0 00-.402-.436 2.284 2.284 0 00-.545-.289 13.019 13.019 0 00-.594-.205c-.161-.049-.317-.1-.467-.152a2.013 2.013 0 01-.397-.184.923.923 0 01-.275-.252.598.598 0 01-.104-.357c0-.203.075-.371.225-.504.15-.133.413-.2.787-.2.293 0 .546.055.759.163.213.109.41.278.594.51l.011.01.54-.494c-.272-.315-.556-.535-.853-.661a2.586 2.586 0 00-1.018-.19zm-14.688.041c-.588 0-1.187.095-1.796.284v7.626h.725v-2.72c.182.048.364.087.546.115a3.539 3.539 0 001.586-.11c.336-.102.635-.261.898-.478.263-.217.474-.494.636-.83.16-.336.241-.739.241-1.208 0-.385-.067-.742-.2-1.071a2.42 2.42 0 00-.572-.851 2.636 2.636 0 00-.898-.557c-.35-.133-.739-.2-1.166-.2zm8.886 0c-.322 0-.627.055-.914.163-.287.11-.54.275-.756.5a2.391 2.391 0 00-.515.845c-.126.34-.189.74-.189 1.202 0 .35.052.683.157.998.106.315.263.596.473.84.21.246.473.44.788.583.315.144.683.216 1.103.216.455 0 .844-.068 1.166-.205.322-.137.605-.338.85-.604l-.44-.462c-.204.224-.431.387-.683.488a2.226 2.226 0 01-.84.153c-.554 0-.992-.175-1.314-.526-.322-.35-.493-.822-.514-1.417h3.939c.013-.904-.176-1.592-.568-2.064-.392-.473-.973-.71-1.743-.71zm.031.62c.26 0 .487.04.683.121.196.08.355.187.478.32.122.133.217.295.284.484.066.189.1.392.1.609H9.074a2.126 2.126 0 01.494-1.103c.111-.126.264-.23.456-.31.193-.08.422-.12.688-.12zM1.86 9.7c.616 0 1.094.188 1.434.563.34.374.51.866.51 1.475 0 .659-.185 1.165-.552 1.518-.368.354-.863.53-1.486.53-.168 0-.342-.018-.52-.057a4.836 4.836 0 01-.52-.142V9.868c.182-.063.367-.107.557-.132.189-.024.38-.036.577-.036zm2.377 6.588v.692H8.66v-.692z"/></svg>
          <span class="font-display text-lg font-extrabold text-navy">plesk</span>
        </div>
        <!-- CloudLinux -->
        <div class="lb-brand-item" title="CloudLinux">
          <svg class="h-6 w-auto" viewBox="0 0 135 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="CloudLinux">
            <path d="M16 11.5c-.3-3.2-3-5.5-6.2-5.5-2.2 0-4.1 1.2-5.2 3C2 9.5 0 11.7 0 14.5 0 17.5 2.5 20 5.5 20h10c2.5 0 4.5-2 4.5-4.5 0-2.1-1.5-3.8-3.5-4z" fill="#1B4D89"/>
            <circle cx="9" cy="13.5" r="2.5" fill="#F4911E"/>
            <text x="24" y="17.5" fill="#24292F" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" letter-spacing="-0.3px">CloudLinux</text>
          </svg>
        </div>
        <!-- WHMCS -->
        <div class="lb-brand-item flex items-center gap-2" title="WHMCS">
          <span class="grid h-6 w-6 place-items-center rounded bg-[#52BBE6] text-[10px] font-extrabold text-white">WH</span>
          <span class="font-display text-lg font-extrabold text-navy">WHMCS</span>
        </div>
        <!-- Imunify360 -->
        <div class="lb-brand-item flex items-center gap-2" title="Imunify360">
          <span class="grid h-6 w-6 place-items-center rounded bg-[#10B981] text-[10px] font-extrabold text-white">I360</span>
          <span class="font-display text-lg font-extrabold text-navy">Imunify360</span>
        </div>
      </div>'''

new_brands_bar = '''      <div class="lb-brands mt-8 flex flex-wrap items-center justify-center gap-x-10 gap-y-6 lg:justify-between">
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
          <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">CloudLinux</span>
        </div>
        <!-- WHMCS -->
        <div class="lb-brand-item flex items-center gap-2.5" title="WHMCS">
          <img src="assets/img/icons/whmcs.svg" alt="WHMCS" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">WHMCS</span>
        </div>
        <!-- Imunify360 -->
        <div class="lb-brand-item flex items-center gap-2.5" title="Imunify360">
          <img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-7 w-7 object-contain" />
          <span class="font-display text-lg font-extrabold text-navy">Imunify360</span>
        </div>
      </div>'''

if old_brands_bar in index_html:
    index_html = index_html.replace(old_brands_bar, new_brands_bar)

# Update Swiper slides in index.html to use <img src="assets/img/icons/{slug}.svg" ...>
swiper_replacements = [
    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-orange-50 font-display text-sm font-bold text-orange-600">cP</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-blue-50 font-display text-sm font-bold text-blue-600">LS</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-sky-50 font-display text-sm font-bold text-sky-600">PL</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/plesk.svg" alt="Plesk" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-amber-50 font-display text-sm font-bold text-amber-700">CL</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-cyan-50 font-display text-sm font-bold text-cyan-600">WH</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/whmcs.svg" alt="WHMCS" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-emerald-50 font-display text-sm font-bold text-emerald-600">I360</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-indigo-50 font-display text-sm font-bold text-indigo-600">JB</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/jetbackup.svg" alt="JetBackup" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-purple-50 font-display text-sm font-bold text-purple-600">VZ</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/virtualizor.svg" alt="Virtualizor" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-teal-50 font-display text-sm font-bold text-teal-600">SA</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/softaculous.svg" alt="Softaculous" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-violet-50 font-display text-sm font-bold text-violet-600">WB</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/webuzo.svg" alt="Webuzo" class="h-8 w-8 object-contain" /></span>'),

    ('<span class="grid h-11 w-11 place-items-center rounded-xl bg-rose-50 font-display text-sm font-bold text-rose-600">WP²</span>',
     '<span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-1.5 shadow-sm"><img src="assets/img/icons/wp-squared.svg" alt="WP Squared" class="h-8 w-8 object-contain" /></span>')
]

for old_s, new_s in swiper_replacements:
    if old_s in index_html:
        index_html = index_html.replace(old_s, new_s)

# Update Bundle showcase in index.html
old_bundle_icons1 = '''          <div class="flex items-center gap-2">
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">cP</span>
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">LS</span>
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">CL</span>
          </div>'''

new_bundle_icons1 = '''          <div class="flex items-center gap-2">
            <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
            <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
            <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
          </div>'''

old_bundle_icons2 = '''          <div class="flex items-center gap-2">
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">cP</span>
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">LS</span>
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-white/10 font-display text-xs font-bold text-white">I360</span>
          </div>'''

new_bundle_icons2 = '''          <div class="flex items-center gap-2">
            <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
            <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
            <img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-9 w-9 object-contain rounded-xl p-1 bg-white/10" />
          </div>'''

if old_bundle_icons1 in index_html:
    index_html = index_html.replace(old_bundle_icons1, new_bundle_icons1)
if old_bundle_icons2 in index_html:
    index_html = index_html.replace(old_bundle_icons2, new_bundle_icons2)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("Updated index.html with real SVGs.")

# 3. Update products.html
with open("products.html", "r", encoding="utf-8") as f:
    prod_html = f.read()

if old_mega_menu in prod_html:
    prod_html = prod_html.replace(old_mega_menu, new_mega_menu)

# Replace product card icons in products.html
products_cards_icons = [
    # 1. cPanel
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-brandSoft text-brand transition-colors group-hover:bg-brand group-hover:text-white">\n                <i data-lucide="server" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-8 w-8 object-contain" />\n              </span>'),
    # 2. LiteSpeed
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-amber-50 text-amber-600 transition-colors group-hover:bg-amber-600 group-hover:text-white">\n                <i data-lucide="zap" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-8 w-8 object-contain" />\n              </span>'),
    # 3. Plesk
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-brandSoft text-brand transition-colors group-hover:bg-brand group-hover:text-white">\n                <i data-lucide="layout-grid" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/plesk.svg" alt="Plesk" class="h-8 w-8 object-contain" />\n              </span>'),
    # 4. WHMCS
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-cyan-50 text-cyan-600 transition-colors group-hover:bg-cyan-600 group-hover:text-white">\n                <i data-lucide="credit-card" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/whmcs.svg" alt="WHMCS" class="h-8 w-8 object-contain" />\n              </span>'),
    # 5. CloudLinux
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-amber-50 text-amber-700 transition-colors group-hover:bg-amber-700 group-hover:text-white">\n                <i data-lucide="shield-check" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-8 w-8 object-contain" />\n              </span>'),
    # 6. Virtualizor
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-purple-50 text-purple-600 transition-colors group-hover:bg-purple-600 group-hover:text-white">\n                <i data-lucide="cpu" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/virtualizor.svg" alt="Virtualizor" class="h-8 w-8 object-contain" />\n              </span>'),
    # 7. SitePad
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-orange-50 text-orange-600 transition-colors group-hover:bg-orange-600 group-hover:text-white">\n                <i data-lucide="globe" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/sitepad.svg" alt="SitePad" class="h-8 w-8 object-contain" />\n              </span>'),
    # 8. WHMReseller
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-blue-50 text-blue-600 transition-colors group-hover:bg-blue-600 group-hover:text-white">\n                <i data-lucide="users" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/whmreseller.svg" alt="WHMReseller" class="h-8 w-8 object-contain" />\n              </span>'),
    # 9. Softaculous
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-teal-50 text-teal-600 transition-colors group-hover:bg-teal-600 group-hover:text-white">\n                <i data-lucide="layers" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/softaculous.svg" alt="Softaculous" class="h-8 w-8 object-contain" />\n              </span>'),
    # 10. JetBackup
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-indigo-50 text-indigo-600 transition-colors group-hover:bg-indigo-600 group-hover:text-white">\n                <i data-lucide="database" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/jetbackup.svg" alt="JetBackup" class="h-8 w-8 object-contain" />\n              </span>'),
    # 11. Imunify360
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-emerald-50 text-emerald-600 transition-colors group-hover:bg-emerald-600 group-hover:text-white">\n                <i data-lucide="lock" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-8 w-8 object-contain" />\n              </span>'),
    # 12. Webuzo
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-violet-50 text-violet-600 transition-colors group-hover:bg-violet-600 group-hover:text-white">\n                <i data-lucide="layout-dashboard" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/webuzo.svg" alt="Webuzo" class="h-8 w-8 object-contain" />\n              </span>'),
    # 13. WP Squared
    ('<span class="grid h-12 w-12 place-items-center rounded-2xl bg-rose-50 text-rose-600 transition-colors group-hover:bg-rose-600 group-hover:text-white">\n                <i data-lucide="layout" class="h-6 w-6"></i>\n              </span>',
     '<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/wp-squared.svg" alt="WP Squared" class="h-8 w-8 object-contain" />\n              </span>')
]

for old_c, new_c in products_cards_icons:
    if old_c in prod_html:
        prod_html = prod_html.replace(old_c, new_c)

with open("products.html", "w", encoding="utf-8") as f:
    f.write(prod_html)

print("Updated products.html with real SVGs.")

# 4. Update deals.html
with open("deals.html", "r", encoding="utf-8") as f:
    deals_html = f.read()

if old_mega_menu in deals_html:
    deals_html = deals_html.replace(old_mega_menu, new_mega_menu)

# Replace hero visual showcase software icons
old_deals_visual_icons = '''            <!-- Software icons included -->
            <div class="grid grid-cols-4 gap-2 text-center">
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <i data-lucide="server" class="mx-auto h-5 w-5 text-brand"></i>
                <p class="mt-1 text-[11px] font-bold text-navy">cPanel</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <i data-lucide="zap" class="mx-auto h-5 w-5 text-amber-500"></i>
                <p class="mt-1 text-[11px] font-bold text-navy">LiteSpeed</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <i data-lucide="shield-check" class="mx-auto h-5 w-5 text-indigo-600"></i>
                <p class="mt-1 text-[11px] font-bold text-navy">CloudLinux</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <i data-lucide="lock" class="mx-auto h-5 w-5 text-rose-500"></i>
                <p class="mt-1 text-[11px] font-bold text-navy">Imunify360</p>
              </div>
            </div>'''

new_deals_visual_icons = '''            <!-- Software icons included -->
            <div class="grid grid-cols-4 gap-2 text-center">
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100 flex flex-col items-center justify-center shadow-sm">
                <img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-6 w-6 object-contain" />
                <p class="mt-1.5 text-[11px] font-bold text-navy">cPanel</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100 flex flex-col items-center justify-center shadow-sm">
                <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-6 w-6 object-contain" />
                <p class="mt-1.5 text-[11px] font-bold text-navy">LiteSpeed</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100 flex flex-col items-center justify-center shadow-sm">
                <img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-6 w-6 object-contain" />
                <p class="mt-1.5 text-[11px] font-bold text-navy">CloudLinux</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100 flex flex-col items-center justify-center shadow-sm">
                <img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-6 w-6 object-contain" />
                <p class="mt-1.5 text-[11px] font-bold text-navy">Imunify360</p>
              </div>
            </div>'''

if old_deals_visual_icons in deals_html:
    deals_html = deals_html.replace(old_deals_visual_icons, new_deals_visual_icons)

# Replace included products list item icons in deals.html with real product SVGs
deal_items_replacements = [
    ('<strong>1. cPanel & WHM License – VPS</strong>', '<img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>1. cPanel & WHM License – VPS</strong></span>'),
    ('<strong>1. cPanel & WHM License – Dedicated</strong>', '<img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>1. cPanel & WHM License – Dedicated</strong></span>'),
    ('<strong>1. cPanel & WHM License – DEDICATED</strong>', '<img src="assets/img/icons/cpanel.svg" alt="cPanel" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>1. cPanel & WHM License – Dedicated</strong></span>'),
    ('<strong>2. LiteSpeed License – 2 Core</strong>', '<img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>2. LiteSpeed License – 2 Core</strong></span>'),
    ('<strong>3. LiteSpeed License – 2 Core</strong>', '<img src="assets/img/icons/litespeed.svg" alt="LiteSpeed" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>3. LiteSpeed License – 2 Core</strong></span>'),
    ('<strong>2. CloudLinux OS License</strong>', '<img src="assets/img/icons/cloudlinux.svg" alt="CloudLinux" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>2. CloudLinux OS License</strong></span>'),
    ('<strong>3. Imunify360 Security License</strong>', '<img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>3. Imunify360 Security License</strong></span>'),
    ('<strong>4. Imunify360 Security Suite</strong>', '<img src="assets/img/icons/imunify360.svg" alt="Imunify360" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>4. Imunify360 Security Suite</strong></span>'),
    ('<strong>5. JetBackup 5 Enterprise License</strong>', '<img src="assets/img/icons/jetbackup.svg" alt="JetBackup" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>5. JetBackup 5 Enterprise License</strong></span>'),
    ('<strong>4. WHMReseller License</strong>', '<img src="assets/img/icons/whmreseller.svg" alt="WHMReseller" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>4. WHMReseller License</strong></span>'),
    ('<strong>6. WHMReseller Pro License</strong>', '<img src="assets/img/icons/whmreseller.svg" alt="WHMReseller" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>6. WHMReseller Pro License</strong></span>'),
    ('<strong>5. Softaculous Auto-Installer License</strong>', '<img src="assets/img/icons/softaculous.svg" alt="Softaculous" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>5. Softaculous Auto-Installer License</strong></span>'),
    ('<strong>7. Softaculous Auto-Installer</strong>', '<img src="assets/img/icons/softaculous.svg" alt="Softaculous" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>7. Softaculous Auto-Installer</strong></span>'),
    ('<strong>6. SitePad Website Builder License</strong>', '<img src="assets/img/icons/sitepad.svg" alt="SitePad" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>6. SitePad Website Builder License</strong></span>'),
    ('<strong>8. SitePad Website Builder</strong>', '<img src="assets/img/icons/sitepad.svg" alt="SitePad" class="h-4 w-4 shrink-0 mt-0.5 object-contain" /><span><strong>8. SitePad Website Builder</strong></span>')
]

# We need to replace the checkmark icon when replacing with SVG to avoid duplicate icons
for title_str, replacement_str in deal_items_replacements:
    # Pattern where check-circle-2 is followed by <span>{title_str}</span>
    deals_html = re.sub(
        r'<i data-lucide="check-circle-2"[^>]*></i><span>' + re.escape(title_str) + r'</span>',
        replacement_str,
        deals_html
    )

with open("deals.html", "w", encoding="utf-8") as f:
    f.write(deals_html)

print("Updated deals.html with real SVGs.")

# 5. Update legal pages mega menus
legal_files = ["terms-of-service.html", "privacy-policy.html", "refund-policy.html", "license-policy.html"]
for lf in legal_files:
    if os.path.exists(lf):
        with open(lf, "r", encoding="utf-8") as f:
            content = f.read()
        if old_mega_menu in content:
            content = content.replace(old_mega_menu, new_mega_menu)
            with open(lf, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated mega menu in {lf}")

print("ALL PAGES SUCCESSFULLY UPDATED WITH REAL SVG ICONS!")

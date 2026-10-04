"""
brand_tools.py — Comprehensive Branding & Design Alignment for LicenBase Tools

This script processes all tools pages (HTML, Next.js RSC flight text, and JS chunks)
to apply uniform LicenBase branding, colors, metadata, JSON-LD schemas,
and commercial cross-promotion widgets.
"""

import glob
import json
import os
import re

TOOLS_DIR = os.path.abspath('tools')
ASSETS_DIR = os.path.abspath('assets')

CTA_BANNER_HTML = '''<div class="lb-tools-commercial-card"><div class="lb-tools-commercial-inner"><div class="lb-tools-commercial-content"><div class="lb-tools-commercial-title"><span class="lb-tools-commercial-tag">LicenBase Platform</span><span class="lb-tools-commercial-heading">Deploying Web Hosting or Cloud Servers?</span></div><p class="lb-tools-commercial-desc">Get genuine automated licenses for cPanel, LiteSpeed, CloudLinux, Plesk, WHMCS &amp; 10+ panels with instant activation and 24/7 support.</p></div><div class="lb-tools-commercial-actions"><a href="/products" class="lb-tools-btn-primary"><span>Browse Licenses</span><svg class="h-3.5 w-3.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a><a href="/deals" class="lb-tools-btn-secondary">View Deals</a></div></div></div>'''

BRAND_HEADER_LINK = '<a class="text-foreground focus-visible:ring-ring focus-visible:ring-offset-card truncate rounded text-base font-semibold hover:underline focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none sm:text-lg inline-flex items-center gap-2" href="/tools/"><span class="font-bold text-gray-900 dark:text-white">LicenBase Tools</span><span class="lb-tools-brand-badge hidden sm:inline-flex">Free Suite</span></a>'

BRAND_CSS_LINK = '<link rel="stylesheet" href="/assets/css/tools-branding.css?v=2"/>'


def patch_js_chunks():
    print("[1/4] Patching Next.js JavaScript chunks...")
    chunks = glob.glob(os.path.join(TOOLS_DIR, '_next', 'static', 'chunks', '**', '*.js'), recursive=True)
    count = 0
    for chunk_path in chunks:
        content = open(chunk_path, 'r', encoding='utf-8', errors='ignore').read()
        original = content
        
        # Replace brand strings
        content = content.replace('"Licenbase Tool"', '"LicenBase Tools"')
        content = content.replace("'Licenbase Tool'", "'LicenBase Tools'")
        content = content.replace('>Licenbase Tool<', '>LicenBase Tools<')
        content = content.replace('Licenbase Tool', 'LicenBase Tools')
        content = content.replace('https://github.com/sunnypatell/netdash-toolkit', 'https://licenbase.com/tools/')
        content = content.replace('https://www.sunnypatel.net/', 'https://licenbase.com/')
        content = content.replace('https://sunnypatel.net', 'https://licenbase.com')
        content = content.replace('Sunny Patel', 'LicenBase')
        
        if content != original:
            open(chunk_path, 'w', encoding='utf-8').write(content)
            count += 1
    print(f"Patched {count} JavaScript chunks.")


def get_clean_title(html, file_path):
    # Extract existing tool title if possible
    rel_path = os.path.relpath(file_path, TOOLS_DIR).replace('\\', '/')
    folder = rel_path.split('/')[0] if '/' in rel_path else ''
    
    if rel_path in ('index.html', 'index.txt'):
        return "Free Network & Sysadmin Tools – DNS, Subnet & IP | LicenBase"
    elif folder == 'about':
        return "About LicenBase Tools – Free Sysadmin & Network Engineering Suite | LicenBase"
    elif folder == 'projects':
        return "Projects & Saved Calculations | LicenBase Tools"
    
    # Check for h1 inside html
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    if h1_match:
        raw_h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        if raw_h1 and 'Licenbase' not in raw_h1 and '48 tools' not in raw_h1:
            return f"{raw_h1} – Free Online Tool | LicenBase"
            
    # Fallback to folder name
    clean_name = folder.replace('-', ' ').title()
    return f"{clean_name} – Free Online Tool | LicenBase"


def patch_html_file(file_path):
    html = open(file_path, 'r', encoding='utf-8').read()
    original = html
    
    rel_path = os.path.relpath(file_path, TOOLS_DIR).replace('\\', '/')
    folder = rel_path.split('/')[0] if '/' in rel_path else ''
    
    # 1. Title tag
    clean_title = get_clean_title(html, file_path)
    html = re.sub(r'<title>.*?</title>', f'<title>{clean_title}</title>', html)
    
    # 2. Metadata tags
    html = re.sub(r'<meta name="application-name" content="[^"]*"/>', '<meta name="application-name" content="LicenBase Tools"/>', html)
    html = re.sub(r'<link rel="author" href="[^"]*"/>', '<link rel="author" href="https://licenbase.com"/>', html)
    html = re.sub(r'<meta name="author" content="[^"]*"/>', '<meta name="author" content="LicenBase"/>', html)
    html = re.sub(r'<meta name="creator" content="[^"]*"/>', '<meta name="creator" content="LicenBase"/>', html)
    html = re.sub(r'<meta property="og:site_name" content="[^"]*"/>', '<meta property="og:site_name" content="LicenBase"/>', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{clean_title}"/>', html)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{clean_title}"/>', html)
    
    # 3. JSON-LD WebApplication schema cleanup
    schema_clean = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "LicenBase Tools",
        "description": "Free online sysadmin and network engineering tools: subnet calculators, DNS lookup, IP converters, TLS checks, and packet diagnostics.",
        "url": "https://licenbase.com/tools/",
        "applicationCategory": "DeveloperApplication",
        "operatingSystem": "Any",
        "browserRequirements": "Requires JavaScript",
        "isAccessibleForFree": True,
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "author": {
            "@type": "Organization",
            "name": "LicenBase",
            "url": "https://licenbase.com"
        }
    }
    if '"@type":"WebApplication"' in html:
        for match in re.finditer(r'<script type="application/ld\+json">([\s\S]*?)</script>', html):
            if '"@type":"WebApplication"' in match.group(1):
                html = html.replace(match.group(0), f'<script type="application/ld+json">{json.dumps(schema_clean, separators=(",", ":"))}</script>')
                break
    
    # 4. Inject tools-branding.css into head
    if '/assets/css/tools-branding.css' not in html:
        html = re.sub(
            r'(<link rel="stylesheet" href="/assets/css/tools-header\.css[^>]*/>)',
            r'\1' + BRAND_CSS_LINK,
            html
        )
        if '/assets/css/tools-branding.css' not in html and '</head>' in html:
            html = html.replace('</head>', f'{BRAND_CSS_LINK}</head>')
            
    # 5. Inner Header Brand Link
    html = re.sub(
        r'<a class="text-foreground focus-visible:ring-ring focus-visible:ring-offset-card truncate rounded text-base font-semibold hover:underline focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none sm:text-lg"[^>]*>Licenbase Tool</a>',
        BRAND_HEADER_LINK,
        html
    )
    html = re.sub(
        r'<a class="text-foreground focus-visible:ring-ring focus-visible:ring-offset-card truncate rounded text-base font-semibold hover:underline focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none sm:text-lg"[^>]*>LicenBase Tools</a>',
        BRAND_HEADER_LINK,
        html
    )
    
    # 6. Insert Contextual Commercial CTA Banner (on tool pages only, not index/about/projects)
    if folder and folder not in ('_next', '404', 'auth', 'about', 'projects'):
        # Check if CTA is already injected
        if 'lb-tools-commercial-card' not in html:
            # Insert before related tools or closing main
            if '<div class="pt-2"><section aria-labelledby="related-tools"' in html:
                html = html.replace(
                    '<div class="pt-2"><section aria-labelledby="related-tools"',
                    f'{CTA_BANNER_HTML}<div class="pt-2"><section aria-labelledby="related-tools"'
                )
            elif '</main>' in html:
                html = html.replace('</main>', f'{CTA_BANNER_HTML}</main>')
    
    # 7. Clean all remaining third-party strings
    html = html.replace('https://github.com/sunnypatell/netdash-toolkit', 'https://licenbase.com/tools/')
    html = html.replace('https://sunnypatel.net', 'https://licenbase.com')
    html = html.replace('Sunny Patel', 'LicenBase')
    html = html.replace('Licenbase Tool', 'LicenBase Tools')
    
    if html != original:
        open(file_path, 'w', encoding='utf-8', newline='').write(html)
        return True
    return False


def patch_all_html_files():
    print("[2/4] Patching all tools HTML and txt files...")
    all_files = []
    for root, dirs, files in os.walk(TOOLS_DIR):
        if '_next' in dirs:
            dirs.remove('_next')
        for file in files:
            if file.endswith('.html') or file.endswith('.txt'):
                all_files.append(os.path.join(root, file))
    count = 0
    for f in all_files:
        if f.endswith('.html'):
            if patch_html_file(f):
                count += 1
        elif f.endswith('.txt'):
            try:
                content = open(f, 'r', encoding='utf-8').read()
                orig = content
                content = content.replace('Licenbase Tool', 'LicenBase Tools')
                content = content.replace('Sunny Patel', 'LicenBase')
                content = content.replace('https://github.com/sunnypatell/netdash-toolkit', 'https://licenbase.com/tools/')
                content = content.replace('https://sunnypatel.net', 'https://licenbase.com')
                if content != orig:
                    open(f, 'w', encoding='utf-8', newline='').write(content)
                    count += 1
            except Exception as e:
                pass
    print(f"Patched {count} HTML and payload files.")


def overhaul_about_page():
    print("[3/4] Overhauling /tools/about/ page content...")
    about_html_path = os.path.join(TOOLS_DIR, 'about', 'index.html')
    if not os.path.exists(about_html_path):
        print("About page not found.")
        return
        
    html = open(about_html_path, 'r', encoding='utf-8').read()
    
    # Overhaul the "Who built it" card
    if "Who built it" in html:
        old_who = re.search(r'<div data-slot="card"[^>]*>.*?Who built it.*?</div></div></div>', html, re.S)
        if old_who:
            new_who = '''<div data-slot="card" class="bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm"><div data-slot="card-header" class="@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6"><div data-slot="card-title" class="font-semibold text-lg">Provided by LicenBase</div><div data-slot="card-description" class="text-muted-foreground text-sm">Empowering sysadmins, DevOps teams, and web hosting providers</div></div><div data-slot="card-content" class="px-6 space-y-4"><p class="text-muted-foreground text-sm leading-relaxed">LicenBase is the leading software licensing platform for hosting providers, agencies, and cloud engineers. We build and maintain these 48 high-performance networking tools to give the sysadmin and developer community completely free, privacy-first, and browser-local utilities.</p><div class="flex flex-wrap gap-2"><a href="/products" class="lb-tools-btn-primary"><span>Explore Licenses</span></a><a href="/deals" class="lb-tools-btn-secondary">Hosting Deals</a><a href="/contact" class="lb-tools-btn-secondary">Contact Support</a><a href="/" class="lb-tools-btn-secondary">LicenBase Home</a></div></div></div>'''
            html = html.replace(old_who.group(0), new_who)
            open(about_html_path, 'w', encoding='utf-8', newline='').write(html)
    print("About page successfully overhauled.")


def run_pipeline():
    print("Starting LicenBase Tools Branding Pipeline...")
    patch_js_chunks()
    patch_all_html_files()
    overhaul_about_page()
    print("[4/4] Branding pipeline completed successfully!")


if __name__ == '__main__':
    run_pipeline()

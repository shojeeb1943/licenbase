"""Regenerate sitemap.xml from the *.html pages (clean URLs, lastmod from git, Google image extensions)."""
import glob
import html
import os
import re
import subprocess
from datetime import date

BASE = "https://licenbase.com"
SKIP = {"404.html"}
PRIORITY = {"index": "1.0", "products": "0.9", "deals": "0.9", "about": "0.5", "contact": "0.5"}

PAGE_IMAGES = {
    "blog/index": ("assets/img/og/blog.png", "LicenBase Blog – Hosting Guides & License Comparisons", "Guides and comparisons on cPanel, Plesk, LiteSpeed and other hosting licenses"),
    "about": ("assets/img/og/about.png", "About LicenBase", "Hosting software licenses activated on your server IP"),
    "contact": ("assets/img/og/contact.png", "Contact LicenBase", "Pre-sales questions, order help and license support"),
    "index": ("assets/img/og/home.png", "Cheap Hosting Software Licenses – LicenBase", "Reliable and cheap hosting licenses with instant activation"),
    "products": ("assets/img/og/products.png", "All Hosting Software Licenses – LicenBase", "Browse all cPanel, LiteSpeed, Plesk, and server management licenses"),
    "deals": ("assets/img/og/deals.png", "Hosting License Bundles & Combo Deals – LicenBase", "Save more with server licensing stacks and combo discounts"),
    "privacy-policy": ("assets/img/og/policies.png", "Privacy Policy – LicenBase", "LicenBase privacy policy and data protection terms"),
    "terms-of-service": ("assets/img/og/policies.png", "Terms of Service – LicenBase", "LicenBase general terms and conditions of service"),
    "refund-policy": ("assets/img/og/policies.png", "Refund Policy – LicenBase", "LicenBase refund policy and money-back guarantee terms"),
    "license-policy": ("assets/img/og/policies.png", "License Policy – LicenBase", "LicenBase software license terms and automated IP replacement policies"),
}


def lastmod(f):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f], capture_output=True, text=True).stdout.strip()
    return out or date.today().isoformat()


def get_og_info(f, name):
    if name in PAGE_IMAGES:
        return PAGE_IMAGES[name]
    
    # For product pages, check if dedicated OG card exists
    slug = name.replace("-license", "") if name.endswith("-license") else name
    if name.startswith("blog/"):
        slug = "blog-" + name[5:]
    og_rel = f"assets/img/og/{slug}.png"
    
    # Extract page title and description from HTML if possible
    content = open(f, encoding="utf-8").read()
    title_match = re.search(r'<meta property="og:title" content="([^"]*)"', content)
    desc_match = re.search(r'<meta property="og:description" content="([^"]*)"', content)
    
    title = html.unescape(title_match.group(1)) if title_match else f"{name.replace('-', ' ').title()} – LicenBase"
    caption = html.unescape(desc_match.group(1)) if desc_match else f"Genuine {name.replace('-', ' ').title()} from LicenBase"
    
    return (og_rel, title, caption)


urls = []
for f in sorted(p.replace("\\", "/") for p in glob.glob("*.html") + glob.glob("blog/*.html")):
    if f in SKIP:
        continue
    name = f[:-5]
    if name in PRIORITY:
        pri = PRIORITY[name]
    elif name == "blog/index":
        pri = "0.8"
    elif name.startswith("blog/"):
        pri = "0.7"
    elif name.endswith("-license"):
        pri = "0.8"
    else:
        pri = "0.3"
    loc = BASE + "/" if name == "index" else BASE + "/blog/" if name == "blog/index" else f"{BASE}/{name}"
    
    og_rel, img_title, img_caption = get_og_info(f, name)
    img_xml = ""
    if os.path.exists(og_rel):
        img_url = f"{BASE}/{og_rel}"
        img_xml = (
            f"\n    <image:image>\n"
            f"      <image:loc>{img_url}</image:loc>\n"
            f"      <image:title>{html.escape(img_title)}</image:title>\n"
            f"      <image:caption>{html.escape(img_caption)}</image:caption>\n"
            f"    </image:image>"
        )

    urls.append(
        f"  <url>\n"
        f"    <loc>{loc}</loc>\n"
        f"    <lastmod>{lastmod(f)}</lastmod>\n"
        f"    <priority>{pri}</priority>"
        f"{img_xml}\n"
        f"  </url>"
    )

# NetDash tools (static build in tools/): canonical URLs end in a slash; /projects and /auth are sign-in only, 404 is an error page
for f in sorted(p.replace("\\", "/") for p in glob.glob("tools/index.html") + glob.glob("tools/*/index.html")):
    slug = f[len("tools/"):-len("index.html")]
    if slug.startswith(("projects", "auth", "404")):
        continue
    urls.append(
        f"  <url>\n"
        f"    <loc>{BASE}/tools/{slug}</loc>\n"
        f"    <lastmod>{lastmod(f)}</lastmod>\n"
        f"    <priority>{'0.8' if not slug else '0.6'}</priority>\n"
        f"  </url>"
    )

sitemap_content = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + "\n".join(urls)
    + "\n</urlset>\n"
)

with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as fh:
    fh.write(sitemap_content)

print(f"Generated sitemap.xml with {len(urls)} URLs and image metadata.")

"""Add og:image / twitter tags and JSON-LD to the hand-edited pages (product pages come from generate_pages.py).
Idempotent: pages that already contain JSON-LD are skipped."""
import html
import json
import re

BASE = "https://licenbase.com"
IMG = BASE + "/assets/img/og-default.png"

ns = {}
exec(open("generate_pages.py", encoding="utf-8").read().split("def generate_page")[0], ns)
products = ns["products"]

PAGES = {  # file -> breadcrumb label (None = home)
    "index.html": None,
    "products.html": "Products",
    "deals.html": "Deals",
    "privacy-policy.html": "Privacy Policy",
    "terms-of-service.html": "Terms of Service",
    "refund-policy.html": "Refund Policy",
    "license-policy.html": "License Policy",
}


def crumbs(label, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
    if label:
        items.append({"@type": "ListItem", "position": 2, "name": label, "item": BASE + path})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def meta(s, prop):
    return re.search(rf'<meta (?:property|name)="{prop}" content="([^"]*)"', s).group(1)


for f, label in PAGES.items():
    s = open(f, encoding="utf-8", newline="").read()
    if "application/ld+json" in s:
        continue
    path = "/" + f[:-5] if f != "index.html" else "/"
    ld = []
    if f == "index.html":
        ld.append({"@context": "https://schema.org", "@type": "Organization", "name": "LicenBase", "url": BASE + "/",
                   "logo": BASE + "/assets/img/logo.png", "email": "support@licenbase.com"})
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": "LicenBase", "url": BASE + "/"})
        qs = re.findall(r'lb-faq-question">(.*?)</span>', s)
        ans = re.findall(r'lb-faq-answer">(.*?)</p>', s, re.S)
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": html.unescape(q), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", "", a)).strip()}}
            for q, a in zip(qs, ans)]})
    else:
        ld.append(crumbs(label, path))
    if f == "products.html":
        ld.append({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": p["name"] + " License", "url": BASE + "/" + p["filename"][:-5]}
            for i, p in enumerate(products, 1)]})

    tags = f'  <meta property="og:image" content="{IMG}" />\n  <meta property="og:locale" content="en_US" />\n'
    s = re.sub(r'(<meta property="og:url"[^>]*/>\n)', lambda m: m.group(1) + tags, s, 1)
    tw = ""
    if 'name="twitter:card"' in s:
        s = s.replace('content="summary" />', 'content="summary_large_image" />', 1)
        s = re.sub(r'(<meta name="twitter:description"[^>]*/>\n)', lambda m: m.group(1) + f'  <meta name="twitter:image" content="{IMG}" />\n', s, 1)
    else:
        t, d = meta(s, "og:title"), meta(s, "og:description")
        tw = (f'\n  <!-- Twitter -->\n  <meta name="twitter:card" content="summary_large_image" />\n  <meta name="twitter:title" content="{t}" />\n'
              f'  <meta name="twitter:description" content="{d}" />\n  <meta name="twitter:image" content="{IMG}" />\n')
    blocks = "".join(f'  <script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>\n' for o in ld)
    s = s.replace("\n  <!-- Favicon -->", tw + "\n" + blocks + "\n  <!-- Favicon -->", 1)
    open(f, "w", encoding="utf-8", newline="").write(s)
    print("patched", f)

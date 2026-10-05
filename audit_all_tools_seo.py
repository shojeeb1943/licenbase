import glob
import html
import json
import os
import re

TOOLS_DIR = r'c:\dev\Licenbase.com\tools'
html_files = sorted(glob.glob(os.path.join(TOOLS_DIR, '*', 'index.html')))

with open('all_toolkit_tools.json', 'r', encoding='utf-8') as f:
    toolkit_tools = json.load(f)
tool_slugs = {t['slug']: t for t in toolkit_tools}

rows = []
weak_or_failing = []

for hf in html_files:
    slug = os.path.basename(os.path.dirname(hf))
    if slug in ('about', 'projects', 'auth', '_next', '404') or slug not in tool_slugs:
        continue

    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title
    t_match = re.search(r'<title>(.*?)</title>', content, re.S)
    title = html.unescape(t_match.group(1)).strip() if t_match else ""
    t_len = len(title)

    # Description
    d_match = re.search(r'<meta name="description" content="([^"]*)"', content)
    desc = html.unescape(d_match.group(1)).strip() if d_match else ""
    d_len = len(desc)

    # Canonical
    c_match = re.search(r'<link rel="canonical" href="([^"]*)"', content)
    canonical = c_match.group(1).strip() if c_match else ""

    # OG Title
    ogt_match = re.search(r'<meta property="og:title" content="([^"]*)"', content)
    og_title = html.unescape(ogt_match.group(1)).strip() if ogt_match else ""

    # OG Description
    ogd_match = re.search(r'<meta property="og:description" content="([^"]*)"', content)
    og_desc = html.unescape(ogd_match.group(1)).strip() if ogd_match else ""

    # OG Image
    ogi_match = re.search(r'<meta property="og:image" content="([^"]*)"', content)
    og_image = ogi_match.group(1).strip() if ogi_match else ""

    # Twitter Card
    twc_match = re.search(r'<meta name="twitter:card" content="([^"]*)"', content)
    tw_card = twc_match.group(1).strip() if twc_match else ""

    # H1
    h1s = re.findall(r'<h1\b[^>]*>(.*?)</h1>', content, re.S)
    h1_count = len(h1s)

    # JSON-LD schemas
    jsonld_scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)
    types = []
    faq_count = 0
    for js in jsonld_scripts:
        try:
            data = json.loads(js)
            if isinstance(data, dict):
                types.append(data.get('@type', ''))
                if data.get('@type') == 'FAQPage':
                    faq_count = len(data.get('mainEntity', []))
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        types.append(item.get('@type', ''))
                        if item.get('@type') == 'FAQPage':
                            faq_count = len(item.get('mainEntity', []))
        except Exception:
            pass

    # Evaluate status
    issues = []
    if t_len < 50 or t_len > 60:
        issues.append(f"Title length ({t_len}c)")
    if '–' in title or '—' in title:
        issues.append("Title contains en/em-dash")
    if d_len < 120 or d_len > 160:
        issues.append(f"Desc length ({d_len}c)")
    if '–' in desc or '—' in desc:
        issues.append("Desc contains en/em-dash")
    if h1_count != 1:
        issues.append(f"H1 count ({h1_count})")
    if faq_count < 3:
        issues.append(f"FAQ count ({faq_count})")
    if not canonical:
        issues.append("Missing canonical")
    if not og_image:
        issues.append("Missing og:image")

    status = "Pass" if not issues else ("Weak" if all("length" in i for i in issues) else "Fail")

    row = {
        "slug": slug,
        "title": title,
        "title_len": t_len,
        "desc": desc,
        "desc_len": d_len,
        "canonical": canonical,
        "og_title": og_title,
        "og_desc_len": len(og_desc),
        "og_image": og_image,
        "tw_card": tw_card,
        "h1_count": h1_count,
        "jsonld_types": ",".join(types),
        "faq_count": faq_count,
        "status": status,
        "issues": issues
    }
    rows.append(row)
    if status != "Pass":
        weak_or_failing.append(row)

# Save audit results to JSON
with open('tool_seo_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, indent=2)

print(f"Audited {len(rows)} tools.")
print(f"Passing: {len(rows) - len(weak_or_failing)}")
print(f"Weak/Failing: {len(weak_or_failing)}")
print("\nSample of Weak/Failing Tools:")
for r in weak_or_failing[:15]:
    print(f"  {r['slug']:35} | Status: {r['status']:4} | Issues: {', '.join(r['issues'])}")

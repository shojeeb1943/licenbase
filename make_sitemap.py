"""Regenerate sitemap.xml from the *.html pages (clean URLs, lastmod from git)."""
import glob
import subprocess

BASE = "https://licenbase.com"
SKIP = {"404.html"}
PRIORITY = {"index": "1.0", "products": "0.9", "deals": "0.9"}


def lastmod(f):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f], capture_output=True, text=True).stdout.strip()
    return out or "2026-01-01"


urls = []
for f in sorted(glob.glob("*.html")):
    if f in SKIP:
        continue
    name = f[:-5]
    if name in PRIORITY:
        pri = PRIORITY[name]
    elif name.endswith("-license"):
        pri = "0.8"
    else:
        pri = "0.3"
    loc = BASE + "/" if name == "index" else f"{BASE}/{name}"
    urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod(f)}</lastmod>\n    <priority>{pri}</priority>\n  </url>")

with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
print(len(urls), "urls")

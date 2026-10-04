"""Ping IndexNow (Bing, Yandex, Seznam, Naver) with new/changed URLs. Run AFTER the site is deployed:

    python indexnow.py          # URLs from sitemap.xml whose lastmod is today
    python indexnow.py --all    # every URL in sitemap.xml
"""
import json
import re
import sys
import urllib.request
from datetime import date

HOST = "licenbase.com"
KEY = "56c8d133edd9b7368cf5c5080801fd32"  # must match /<KEY>.txt in the site root

xml = open("sitemap.xml", encoding="utf-8").read()
today = date.today().isoformat()
urls = [
    loc for loc, mod in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", xml)
    if "--all" in sys.argv or mod == today
]
if not urls:
    sys.exit("No URLs changed today (use --all to resubmit everything).")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode(),
    headers={"Content-Type": "application/json; charset=utf-8"},
)
with urllib.request.urlopen(req) as r:  # 200/202 = accepted
    print(f"IndexNow: submitted {len(urls)} URLs, HTTP {r.status}")

"""Add a Blog link to desktop nav, mobile drawer and footer on every page + generate_pages.py. Idempotent."""
import glob
import re

DESK = re.compile(r'([ \t]*)(<a href="/deals" class="lb-nav-link lb-nav-link--plain[^"]*">Deals</a>)')
MOB = re.compile(r'([ \t]*)(<li><a href="/deals" class="lb-mobile-link[^>]*>Combo Deals</a></li>)')
FOOT = re.compile(r'([ \t]*)(<li><a href="https://dashboard\.licenbase\.com/submitticket\.php" class="transition hover:text-brand">Support Center</a></li>)')


def patch(s):
    if 'href="/blog/"' in s:
        return s
    s = DESK.sub(lambda m: f'{m.group(1)}{m.group(2)}\n{m.group(1)}<a href="/blog/" class="lb-nav-link lb-nav-link--plain">Blog</a>', s)
    s = MOB.sub(lambda m: f'{m.group(1)}{m.group(2)}\n{m.group(1)}<li><a href="/blog/" class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy transition hover:bg-mist">Blog</a></li>', s)
    s = FOOT.sub(lambda m: f'{m.group(1)}<li><a href="/blog/" class="transition hover:text-brand">Blog</a></li>\n{m.group(1)}{m.group(2)}', s)
    return s


for f in glob.glob("*.html") + ["generate_pages.py"]:
    if f == "404.html":
        continue
    s = open(f, encoding="utf-8", newline="").read()
    t = patch(s)
    if t != s:
        open(f, "w", encoding="utf-8", newline="").write(t)
        print("patched", f)

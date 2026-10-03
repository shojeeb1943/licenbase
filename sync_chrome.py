"""Global header / mobile nav / footer: index.html is the single source. Copies those three blocks into every
root + blog page (idempotent), marking the current nav link. Run after generate_pages.py / publish_blog.py,
before build_tools_header.py (which also reads index.html)."""
import glob, re

BLOCKS = (  # (start marker, end marker)
    ('<div class="lb-topbar">', '</header>'),
    ('<nav class="flex-1 overflow-y-auto overscroll-contain px-5 py-4" aria-label="Mobile navigation"', '</nav>'),
    ('<footer', '</footer>'),
)


def span(s, a, b):
    i = s.find(a)
    return (i, s.index(b, i) + len(b)) if i >= 0 else None


def absolute(s):
    return re.sub(r'(src|href)="assets/', r'\1="/assets/', s)


def active(path):
    p = path.replace(chr(92), '/')
    href = '/blog/' if p.startswith('blog/') else {'contact.html': '/contact', 'deals.html': '/deals'}.get(p)
    return href


src = open('index.html', encoding='utf-8', newline='').read()
canon = [absolute(src[slice(*span(src, a, b))]) for a, b in BLOCKS]
n = 0
for f in glob.glob('*.html') + glob.glob('blog/*.html'):
    s = open(f, encoding='utf-8', newline='').read()
    t = s
    for (a, b), c in zip(BLOCKS, canon):
        sp = span(t, a, b)
        if not sp: continue
        if a.startswith('<div class="lb-topbar'):
            h = active(f)
            if h: c = c.replace(f'<a href="{h}" class="lb-nav-link lb-nav-link--plain">', f'<a href="{h}" class="lb-nav-link lb-nav-link--plain text-brand font-bold" aria-current="page">', 1)
        t = t[:sp[0]] + c + t[sp[1]:]
    if t != s:
        open(f, 'w', encoding='utf-8', newline='').write(t); n += 1
print('synced', n)

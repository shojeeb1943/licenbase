"""Make the flight payload's <title>/og:title/twitter:title match the static <head> of each /tools page.
A mismatch makes React hydration fail (error #418). Static head is the source of truth (SEO titles). Idempotent."""
import glob, html, os, re

Q = r'\\*"'  # a quote, possibly backslash-escaped (inline script) or plain (.txt)
TITLE = re.compile(r'(\[' + Q + r'\$' + Q + r',' + Q + r'title' + Q + r',' + Q + r'\d+' + Q + r',\{' + Q + r'children' + Q + r':' + Q + r')(.*?)(' + Q + r'\}\])')
META = lambda prop: re.compile(r'(' + Q + r'(?:property|name)' + Q + r':' + Q + prop + Q + r',' + Q + r'content' + Q + r':' + Q + r')(.*?)(' + Q + r'\})')

n = 0
for f in glob.glob('tools/**/index.html', recursive=True):
    s = open(f, encoding='utf-8', newline='').read()
    m = re.search(r'<title>(.*?)</title>', s)
    if not m: continue
    t = html.unescape(m.group(1))
    for path in (f, f[:-5] + '.txt'):
        if not os.path.isfile(path): continue
        a = open(path, encoding='utf-8', newline='').read()
        b = TITLE.sub(lambda x: x.group(1) + t + x.group(3), a)
        for prop in ('og:title', 'twitter:title'):
            b = META(prop).sub(lambda x: x.group(1) + t + x.group(3), b)
        if b != a:
            open(path, 'w', encoding='utf-8', newline='').write(b); n += 1
print('patched', n)

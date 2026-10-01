import re, glob, html

pages = sorted(glob.glob('*.html'))
for f in pages:
    if f == '404.html':
        continue
    s = open(f, encoding='utf-8').read()
    m = re.search(r'property="og:title" content="([^"]*)"', s)
    if m:
        t = html.unescape(m.group(1))
        flag = '  <-- OVER 60' if len(t) > 60 else ''
        print(f'{len(t):3d}  {f}{flag}')
    else:
        print(f'  ?  {f}  (no og:title)')

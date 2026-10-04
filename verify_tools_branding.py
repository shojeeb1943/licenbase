"""Fail loudly if /tools lost its LicenBase branding. Run by import_tools.py after every import, or on its own:

    python verify_tools_branding.py

Checks the things that have regressed before: the tab icon and sidebar logo falling back to NetDash, the site
header or footer missing, and NetDash or author branding leaking into pages. Exit code 1 on any failure."""
import base64, glob, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
problems = []
read = lambda p: open(p, encoding='utf-8', errors='ignore').read()

png = base64.b64encode(open('assets/img/favicon-192x192.png', 'rb').read()).decode()
for icon in ('tools/icon.svg', 'tools/favicon.svg'):
    if not os.path.isfile(icon) or png[:200] not in read(icon):
        problems.append(f'{icon} is not the LicenBase logo (assets/img/favicon-192x192.png)')

chunks = glob.glob('tools/_next/static/chunks/**/*.js', recursive=True)
if not any('/assets/img/favicon-192x192.png' in read(c) for c in chunks):
    problems.append('the sidebar no longer renders the LicenBase logo (/assets/img/favicon-192x192.png)')

# shell fixes live in assets/ (they survive imports); fail if a page no longer loads them or they were lost
for a, needle in (('assets/css/tools-branding.css', 'lb:tools-shell'), ('assets/js/tools-header.js', 'embed.tawk.to/6aa54c1357bdd83448ee36a5')):
    if needle not in read(a):
        problems.append(f'{a} lost "{needle}" (single scrollbar / hidden NetDash bar / Tawk chat)')

# error pages render outside the app shell and carry no site header
NO_HEADER = {'tools/404.html', 'tools/404/index.html', 'tools/auth/action/index.html'}
pages = [f.replace('\\', '/') for f in glob.glob('tools/**/index.html', recursive=True) if '_next' not in f]
if os.path.isfile('tools/404.html'):
    pages.append('tools/404.html')
else:
    problems.append('tools/404.html is missing')
if len(pages) < 100:
    problems.append(f'only {len(pages)} pages found: the build looks incomplete')
for f in pages:
    s = read(f)
    if f not in NO_HEADER and ('lb-tools-header' not in s or 'lb-tools-footer' not in s):
        problems.append(f'{f}: LicenBase header or footer missing')
    if f not in NO_HEADER and ('tools-branding.css?v=2' not in s or 'tools-header.js?v=2' not in s):
        problems.append(f'{f}: stale tools-branding.css / tools-header.js version (browsers would keep old copies)')
    for leak in ('netdash-toolkit.vercel.app', 'sunnypatel', 'Sunny Patel', 'NetDash'):
        if leak in s:
            problems.append(f'{f}: contains "{leak}"')
    if f == 'tools/index.html' and 'rel="canonical" href="https://licenbase.com/tools/"' not in s:
        problems.append('tools/index.html: canonical is not https://licenbase.com/tools/')

for p in problems[:25]:
    print('BRANDING FAIL:', p)
if problems:
    print(f'{len(problems)} problem(s)')
    sys.exit(1)
print(f'branding ok: {len(pages)} pages, icon and sidebar logo are LicenBase')

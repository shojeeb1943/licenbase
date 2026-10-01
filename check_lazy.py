import re, glob

# Check image lazy-loading counts per page
for f in ['cpanel-license.html', 'index.html', 'deals.html']:
    s = open(f, encoding='utf-8').read()
    imgs = re.findall(r'<img [^>]+>', s)
    lazy = [i for i in imgs if 'loading="lazy"' in i]
    eager = [i for i in imgs if 'loading="lazy"' not in i]
    print(f'{f}: {len(imgs)} imgs total, {len(lazy)} lazy, {len(eager)} eager')
    if eager:
        print('  First 3 eager:', [x[:80] for x in eager[:3]])

print()
# Check meta descriptions
for f in ['deals.html', 'privacy-policy.html']:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'name="description" content="([^"]+)"', s)
    if m:
        t = m.group(1)
        print(f'{f} ({len(t)}c): {t}')

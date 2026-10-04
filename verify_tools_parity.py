"""Compare the rebuilt tools/ with a saved copy of the previous export: python verify_tools_parity.py <golden-dir> [tools-dir]

Every page that existed before must keep the same SEO identity (title, description, canonical, robots,
og/twitter tags, keywords, author, headings, JSON-LD). Chunk names, build ids and the sidebar may differ.
Exits non-zero on any difference. Pages new in tools/ are listed, and each must carry the same checks."""
import glob, html, json, os, re, sys

META = re.compile(r'<meta\b([^>]*?)/?>')
ATTR = re.compile(r'([\w:-]+)="([^"]*)"')
H = re.compile(r'<h([12])\b[^>]*>(.*?)</h\1>', re.S)


def identity(page):
    s = open(page, encoding='utf-8', errors='replace').read()
    head = re.search(r'<head>(.*?)</head>', s, re.S)
    head = head.group(1) if head else s
    out = {}
    t = re.search(r'<title>(.*?)</title>', head, re.S)
    out['title'] = html.unescape(t.group(1)) if t else None
    for m in META.finditer(head):
        a = dict(ATTR.findall(m.group(1)))
        key = a.get('name') or a.get('property')
        if key and key not in ('viewport', 'theme-color'):
            out['meta:' + key + (':' + a['media'] if 'media' in a else '')] = html.unescape(a.get('content', ''))
    for rel in ('canonical', 'manifest', 'author'):
        m = re.search(r'<link rel="%s" href="([^"]*)"' % rel, head)
        out['link:' + rel] = m.group(1) if m else None
    m = re.search(r'<link rel="icon" href="(/tools/icon\.svg)', head)
    out['link:icon'] = m.group(1) if m else None
    body = s[s.find('<body'):]
    out['headings'] = [html.unescape(re.sub(r'<[^>]+>', '', x[1])).strip() for x in H.findall(body)]
    ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    out['jsonld'] = [json.loads(x) for x in ld]
    return out


def pages(root):
    found = {os.path.relpath(f, root).replace('\\', '/') for f in glob.glob(os.path.join(root, '**', 'index.html'), recursive=True)}
    found |= {os.path.relpath(f, root).replace('\\', '/') for f in glob.glob(os.path.join(root, '*.html'))}
    return found - {p for p in found if p.startswith('_next/')}


def main():
    golden, new = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'tools')
    old_pages, new_pages = pages(golden), pages(new)
    bad = 0
    for p in sorted(old_pages - new_pages):
        print('MISSING PAGE', p); bad += 1
    for p in sorted(old_pages & new_pages):
        a, b = identity(os.path.join(golden, p)), identity(os.path.join(new, p))
        for k in sorted(set(a) | set(b)):
            if k in ('jsonld', 'headings') and isinstance(a.get(k), list) and isinstance(b.get(k), list):
                if all(x in b[k] for x in a[k]):  # additions are allowed (per-tool JSON-LD, 'About this tool'); removals are not
                    continue
            if a.get(k) != b.get(k):
                bad += 1
                print(f'DIFF {p} [{k}]\n   old: {str(a.get(k))[:200]}\n   new: {str(b.get(k))[:200]}')
    added = sorted(new_pages - old_pages)
    print(f'{len(old_pages & new_pages)} existing pages compared, {bad} differences; {len(added)} new pages: {", ".join(added[:40])}')
    for p in added:  # new pages must carry the full identity
        i = identity(os.path.join(new, p))
        for k in ('title', 'meta:description', 'link:canonical'):
            if not i.get(k):
                bad += 1; print('NEW PAGE MISSING', p, k)
        if i.get('link:canonical') and not i['link:canonical'].startswith('https://licenbase.com/tools/'):
            bad += 1; print('NEW PAGE BAD CANONICAL', p, i['link:canonical'])
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

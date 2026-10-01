import glob
import os
import re
import struct
import sys
import zlib
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

# Ensure utf-8 output if supported
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.canonical = ""
        self.robots = ""
        self.lang = ""
        self.viewport = ""
        self.theme_color = ""
        self.manifest = ""
        self.og = {}
        self.twitter = {}
        self.h1s = []
        self.in_h1 = False
        self.current_h1 = ""
        self.h2s = []
        self.in_h2 = False
        self.current_h2 = ""
        self.h3_count = 0
        self.schemas = []
        self.in_script_ld = False
        self.current_script = ""
        self.images = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        if tag == 'html':
            self.lang = attr_dict.get('lang', '')
            
        elif tag == 'title':
            self.in_title = True
            
        elif tag == 'meta':
            name = attr_dict.get('name', '').lower()
            prop = attr_dict.get('property', '').lower()
            content = attr_dict.get('content', '')
            
            if name == 'description':
                self.meta_desc = content
            elif name == 'robots':
                self.robots = content
            elif name == 'viewport':
                self.viewport = content
            elif name == 'theme-color':
                self.theme_color = content
            elif name.startswith('twitter:'):
                self.twitter[name] = content
            elif prop.startswith('og:'):
                self.og[prop] = content
                
        elif tag == 'link':
            rel = attr_dict.get('rel', '').lower()
            href = attr_dict.get('href', '')
            if rel == 'canonical':
                self.canonical = href
            elif rel == 'manifest':
                self.manifest = href
                
        elif tag == 'h1':
            self.in_h1 = True
            self.current_h1 = ""
        elif tag == 'h2':
            self.in_h2 = True
            self.current_h2 = ""
        elif tag == 'h3':
            self.h3_count += 1
            
        elif tag == 'script':
            type_attr = attr_dict.get('type', '')
            if type_attr == 'application/ld+json':
                self.in_script_ld = True
                self.current_script = ""
                
        elif tag == 'img':
            src = attr_dict.get('src', '')
            alt = attr_dict.get('alt', None)
            w = attr_dict.get('width', '')
            h = attr_dict.get('height', '')
            self.images.append({'src': src, 'alt': alt, 'width': w, 'height': h})
            
        elif tag == 'a':
            href = attr_dict.get('href', '')
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            self.in_h1 = False
            if self.current_h1.strip():
                self.h1s.append(self.current_h1.strip())
        elif tag == 'h2':
            self.in_h2 = False
            if self.current_h2.strip():
                self.h2s.append(self.current_h2.strip())
        elif tag == 'script' and self.in_script_ld:
            self.in_script_ld = False
            if self.current_script.strip():
                self.schemas.append(self.current_script.strip())

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.current_h1 += data
        elif self.in_h2:
            self.current_h2 += data
        elif self.in_script_ld:
            self.current_script += data


def audit_blog_post(file, html, report):
    """Checks from docs/blog-guidelines.md for blog/<slug>.html (the index is not a post)."""
    import json as _json
    w = report['warnings']
    slug = file[len('blog/'):-len('.html')]
    m = re.search(r'<article.*?</article>', html, re.S)
    if not m:
        w.append('blog: no <article> element')
        return
    art = m.group(0)
    words = len(re.sub(r'<[^>]+>', ' ', art).split())
    if words < 700:
        w.append(f'blog: article is {words} words (minimum 700)')
    if len(re.findall(r'<h2[ >]', art)) < 3:
        w.append('blog: fewer than 3 H2 sections')
    if 'id="toc"' not in html:
        w.append('blog: table of contents missing')
    if 'Frequently asked questions' not in art:
        w.append('blog: FAQ section missing')
    desc = report['description']
    if not 110 <= len(desc) <= 160:
        w.append(f'blog: meta description is {len(desc)} chars (110-160)')
    # feature + thumb images
    feat = f'assets/img/blog/{slug}-feature.webp'
    thumb = f'assets/img/blog/{slug}-thumb.webp'
    for path, size in ((feat, (1200, 630)), (thumb, (640, 336))):
        if not Path(path).exists():
            w.append(f'blog: missing image {path} (run python generate_og.py --blog)')
            continue
        try:
            from PIL import Image
            got = Image.open(path).size
            if got != size:
                w.append(f'blog: {path} is {got[0]}x{got[1]} (expected {size[0]}x{size[1]})')
        except ImportError:
            pass
    if f'/{feat}' not in html or 'fetchpriority="high"' not in html:
        w.append('blog: page must show the feature image with fetchpriority="high"')
    # images: alt + dimensions + weight
    imgs = re.findall(r'<img [^>]*>', html)
    for im in imgs:
        if 'width=' not in im or 'height=' not in im:
            w.append(f'blog: image without width/height: {im[:80]}')
    body_imgs = re.findall(r'<img [^>]*>', art)
    if not any(re.search(r'alt="[^"]{10,}"', i) for i in body_imgs):
        w.append('blog: no in-article image with descriptive alt text')
    for src in set(re.findall(r'src="/(assets/img/blog/[^"]+)"', html)):
        if Path(src).exists():
            kb = Path(src).stat().st_size / 1024
            if kb > (100 if src.endswith('.svg') else 300):
                w.append(f'blog: {src} is {kb:.0f} KB (too heavy)')
    if len(set(re.findall(r'href="/([a-z0-9-]+-license)"', art))) < 2:
        w.append('blog: fewer than 2 distinct product-page links in the article')
    # structured data + dates
    types = {}
    for blob in re.findall(r'application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = _json.loads(blob)
            types[d.get('@type')] = d
        except ValueError:
            w.append('blog: invalid JSON-LD')
    post = types.get('BlogPosting')
    if not post:
        w.append('blog: BlogPosting JSON-LD missing')
    else:
        for k in ('headline', 'image', 'datePublished', 'dateModified', 'author', 'publisher'):
            if not post.get(k):
                w.append(f'blog: BlogPosting.{k} missing')
        if post.get('dateModified', '') < post.get('datePublished', ''):
            w.append('blog: dateModified is before datePublished')
    if 'FAQPage' not in types:
        w.append('blog: FAQPage JSON-LD missing')
    if 'article:published_time' not in html:
        w.append('blog: article:published_time meta missing')


files = sorted(p.replace(chr(92), '/') for p in glob.glob('*.html') + glob.glob('blog/*.html'))
print(f'=== Comprehensive SEO Audit for {len(files)} HTML Pages ===\n')

page_audits = []
all_titles = {}
all_descriptions = {}
og_image_pages: dict[str, list[str]] = {}  # og:image URL -> list of pages using it

# Pages that are allowed to share the same OG image
LEGAL_FILES = {"privacy-policy.html", "terms-of-service.html", "refund-policy.html", "license-policy.html"}


def _png_dimensions(local_path: str):
    """Return (width, height) for a PNG file, or None on error."""
    try:
        p = Path(local_path)
        if not p.exists():
            return None
        data = p.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n':
            return None
        w, h = struct.unpack('>II', data[16:24])
        return w, h
    except Exception:
        return None

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    parser = SEOParser()
    parser.feed(html)
    
    report = {
        'file': file,
        'issues': [],
        'warnings': [],
        'title': parser.title.strip(),
        'description': parser.meta_desc.strip(),
        'canonical': parser.canonical.strip(),
        'h1': parser.h1s[0] if parser.h1s else "",
        'h1_count': len(parser.h1s),
        'h2_count': len(parser.h2s),
        'h3_count': parser.h3_count,
        'schema_count': len(parser.schemas),
        'img_count': len(parser.images),
        'missing_alt_count': sum(1 for img in parser.images if img['alt'] is None),
        'bad_links': [l for l in parser.links if l.endswith('.html') and not l.startswith('http') and not l.startswith('#')]
    }

    # Checks
    if not parser.lang:
        report['issues'].append('Missing lang attribute on <html>')
    if not parser.viewport:
        report['issues'].append('Missing viewport meta tag')
    
    if not report['title']:
        report['issues'].append('Missing <title> tag')
    else:
        t = report['title']
        t_len = len(t)
        if t in all_titles:
            report['issues'].append(f'Duplicate title with {all_titles[t]}')
        else:
            all_titles[t] = file
        if t_len < 25 or t_len > 70:
            report['warnings'].append(f'Title length ({t_len} chars): "{t}"')

    if not report['description']:
        if file != '404.html':
            report['issues'].append('Missing meta description')
    else:
        d = report['description']
        d_len = len(d)
        if d in all_descriptions:
            report['issues'].append(f'Duplicate description with {all_descriptions[d]}')
        else:
            all_descriptions[d] = file
        if d_len < 50 or d_len > 165:
            report['warnings'].append(f'Description length ({d_len} chars): "{d}"')

    if not report['canonical']:
        if file != '404.html':
            report['issues'].append('Missing canonical URL')
    else:
        if report['canonical'].endswith('.html'):
            report['warnings'].append(f'Canonical contains .html: {report["canonical"]}')

    if report['h1_count'] == 0:
        report['issues'].append('Missing <h1> tag')
    elif report['h1_count'] > 1:
        report['warnings'].append(f'Multiple <h1> tags ({report["h1_count"]})')

    missing_og = [k for k in ['og:title', 'og:description', 'og:url', 'og:image',
                               'og:image:width', 'og:image:height', 'og:image:alt',
                               'og:type', 'og:site_name'] if k not in parser.og]
    if missing_og and file != '404.html':
        report['warnings'].append(f'Missing Open Graph: {missing_og}')

    missing_tw = [k for k in ['twitter:card', 'twitter:title', 'twitter:description',
                               'twitter:image', 'twitter:image:alt'] if k not in parser.twitter]
    if missing_tw and file != '404.html':
        report['warnings'].append(f'Missing Twitter Card: {missing_tw}')

    if not parser.manifest:
        report['warnings'].append('Missing <link rel="manifest">')
    if not parser.theme_color:
        report['warnings'].append('Missing <meta name="theme-color">')

    # --- og:title length check (social platforms truncate beyond ~60 chars) ---
    og_title = parser.og.get('og:title', '')
    if og_title and len(og_title) > 60 and file != '404.html':
        report['warnings'].append(f'og:title too long ({len(og_title)} chars > 60): "{og_title}"')

    # --- OG image file checks ---
    og_img_url = parser.og.get('og:image', '')
    if og_img_url and file != '404.html':
        # Track for uniqueness audit
        og_image_pages.setdefault(og_img_url, []).append(file)

        # Resolve URL to local path
        local_img = og_img_url.replace('https://licenbase.com', '').lstrip('/')
        dims = _png_dimensions(local_img)
        if dims is None:
            report['warnings'].append(f'og:image not found locally: {local_img}')
        else:
            w, h = dims
            if (w, h) != (1200, 630):
                report['warnings'].append(f'og:image dimensions {w}x{h} (expected 1200x630): {local_img}')
            img_kb = Path(local_img).stat().st_size / 1024
            if img_kb > 300:
                report['warnings'].append(f'og:image too large ({img_kb:.0f} KB > 300 KB): {local_img}')

    if report['schema_count'] == 0 and file != '404.html':
        report['warnings'].append('Missing Schema.org structured data (JSON-LD)')

    if report['missing_alt_count'] > 0:
        report['warnings'].append(f'{report["missing_alt_count"]} images missing alt attribute')

    if report['bad_links']:
        report['warnings'].append(f'{len(report["bad_links"])} internal links have .html extension: {set(report["bad_links"])}')

    if file.startswith('blog/') and file != 'blog/index.html':
        audit_blog_post(file, html, report)

    page_audits.append(report)

# --- Cross-page OG image uniqueness check ---
for img_url, pages_using in og_image_pages.items():
    if len(pages_using) > 1:
        # Legal pages may share the "policies" card — that is expected
        non_legal = [f for f in pages_using if f not in LEGAL_FILES]
        all_legal = all(f in LEGAL_FILES for f in pages_using)
        if not all_legal and len(pages_using) > 1:
            # Flag non-legal pages that share an image
            for f in pages_using:
                if f not in LEGAL_FILES:
                    for r in page_audits:
                        if r['file'] == f:
                            r['warnings'].append(
                                f'og:image shared with {[x for x in pages_using if x != f]}: {img_url}'
                            )

total_errors = sum(len(p['issues']) for p in page_audits)
total_warns = sum(len(p['warnings']) for p in page_audits)

print(f'=== AUDIT RESULTS: {total_errors} Critical Errors | {total_warns} Warnings ===\n')

for p in page_audits:
    status = '[PASS]' if not p['issues'] and not p['warnings'] else ('[WARN]' if not p['issues'] else '[FAIL]')
    print(f"{status} {p['file']}")
    print(f"   * Title ({len(p['title'])}c): {p['title']}")
    print(f"   * H1: {p['h1']}")
    print(f"   * Canonical: {p['canonical']}")
    print(f"   * Content: {p['h2_count']} H2s | {p['h3_count']} H3s | {p['img_count']} images | {p['schema_count']} schemas")
    for e in p['issues']:
        print(f"   [ERROR] {e}")
    for w in p['warnings']:
        print(f"   [WARNING] {w}")
    print()

# Check sitemap.xml
print('='*70)
print('SITEMAP.XML AUDIT')
print('='*70)
if os.path.exists('sitemap.xml'):
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    namespace = {
        'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9',
        'image': 'http://www.google.com/schemas/sitemap-image/1.1'
    }
    urls = [loc.text for loc in root.findall('ns:url/ns:loc', namespace)]
    print(f'Total URLs in sitemap: {len(urls)}')
    sitemap_set = set(urls)
    canonicals_set = set(p['canonical'] for p in page_audits if p['canonical'])
    
    missing_in_sitemap = canonicals_set - sitemap_set
    if missing_in_sitemap:
        print(f'[WARNING] URLs in site but missing from sitemap: {missing_in_sitemap}')
    else:
        print('[PASS] All canonical URLs are present in sitemap.xml')
        
    extra_in_sitemap = sitemap_set - canonicals_set
    if extra_in_sitemap:
        print(f'[WARNING] URLs in sitemap not matching canonicals: {extra_in_sitemap}')
    else:
        print('[PASS] All sitemap URLs match site canonicals')

    # Check image sitemap entries
    image_locs = [img.text for img in root.findall('ns:url/image:image/image:loc', namespace)]
    print(f'Total Image entries in sitemap: {len(image_locs)}')
    missing_images = []
    for img_url in image_locs:
        rel_path = img_url.replace('https://licenbase.com/', '')
        if not os.path.exists(rel_path):
            missing_images.append(img_url)
    if missing_images:
        print(f'[WARNING] Sitemap images missing on disk: {missing_images}')
    else:
        print(f'[PASS] All {len(image_locs)} sitemap images exist locally on disk')

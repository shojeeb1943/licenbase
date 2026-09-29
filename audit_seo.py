import glob
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

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
            elif name.startswith('twitter:'):
                self.twitter[name] = content
            elif prop.startswith('og:'):
                self.og[prop] = content
                
        elif tag == 'link':
            rel = attr_dict.get('rel', '').lower()
            href = attr_dict.get('href', '')
            if rel == 'canonical':
                self.canonical = href
                
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


files = sorted(glob.glob('*.html'))
print(f'=== Comprehensive SEO Audit for {len(files)} HTML Pages ===\n')

page_audits = []
all_titles = {}
all_descriptions = {}

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
        'missing_alt_count': sum(1 for img in parser.images if img['alt'] is None or img['alt'] == ""),
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

    missing_og = [k for k in ['og:title', 'og:description', 'og:url', 'og:image', 'og:type', 'og:site_name'] if k not in parser.og]
    if missing_og and file != '404.html':
        report['warnings'].append(f'Missing Open Graph: {missing_og}')

    missing_tw = [k for k in ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'] if k not in parser.twitter]
    if missing_tw and file != '404.html':
        report['warnings'].append(f'Missing Twitter Card: {missing_tw}')

    if report['schema_count'] == 0 and file != '404.html':
        report['warnings'].append('Missing Schema.org structured data (JSON-LD)')

    if report['missing_alt_count'] > 0:
        report['warnings'].append(f'{report["missing_alt_count"]} images missing alt attribute')

    if report['bad_links']:
        report['warnings'].append(f'{len(report["bad_links"])} internal links have .html extension: {set(report["bad_links"])}')

    page_audits.append(report)

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
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
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

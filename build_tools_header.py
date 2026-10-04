"""Give /tools pages the real site header (static HTML in the prebuilt Next export). Idempotent.
Generates assets/css/tools-header.css + assets/js/tools-header.js, then swaps the old header in tools/**/*.html and *.txt."""
import base64, glob, json, os, re, sys

PRE = ('.lb-shell', '.lb-btn', '.lb-topbar', '.lb-header', '.lb-logo', '.lb-nav', '.lb-drop', '.lb-mega', '.lb-icon-btn', '.lb-menu-toggle')


def blocks(css):
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0: break
        depth, k = 1, j + 1
        while depth and k < n:
            depth += (css[k] == '{') - (css[k] == '}'); k += 1
        out.append((css[i:j].strip(), css[j + 1:k - 1], css[i:k].strip()))
        i = k
    return out


def keep(sel):
    return all(s.strip().startswith(PRE) for s in sel.split(','))


css = re.sub(r'/\*.*?\*/', '', open('assets/css/styles.css', encoding='utf-8').read(), flags=re.S)
parts = []
for sel, body, raw in blocks(css):
    if sel.startswith('@media'):
        inner = [r for s, b, r in blocks(body) if keep(s)]
        if inner: parts.append(f'{sel}{{{"".join(inner)}}}')
    elif keep(sel):
        parts.append(raw)
extra = """
:root{--brand:#1e40af;--brand-deep:#1e3a8a;--navy:#111827;--mist:#f8fafc;--gray:#6b7280}
.lb-topbar,.lb-topbar *{box-sizing:border-box}
.lb-topbar{font-family:Inter,system-ui,sans-serif;position:relative;z-index:40;background:#fff}
.lb-tmenu{position:relative;display:none}
.lb-tmenu summary{list-style:none;cursor:pointer;display:grid;place-items:center;width:2.5rem;height:2.5rem;border-radius:.75rem}
.lb-tmenu summary::-webkit-details-marker{display:none}
.lb-tmenu ul{position:absolute;right:0;top:3rem;width:12rem;margin:0;padding:.5rem;list-style:none;background:#fff;border:1px solid #e5e7eb;border-radius:.75rem;box-shadow:0 10px 30px rgba(0,0,0,.12);z-index:50}
.lb-tmenu li a{display:block;padding:.5rem .75rem;border-radius:.5rem;font-size:.875rem;font-weight:600;color:#111827;text-decoration:none}
.lb-tmenu li a:hover{background:#f8fafc}
@media(max-width:1023px){.lb-tmenu{display:block}}
[class*="100dvh-4rem"]{height:calc(100dvh - var(--lb-hdr,7rem))!important}
"""
open('assets/css/tools-header.css', 'w', encoding='utf-8').write('\n'.join(parts) + extra)

open('assets/js/tools-header.js', 'w', encoding='utf-8').write("""(function(){
  var d=document;
  function closeAll(except){d.querySelectorAll('.lb-topbar .lb-drop').forEach(function(x){if(x!==except){x.classList.remove('is-open');var b=x.querySelector('[data-drop]');b&&b.setAttribute('aria-expanded','false')}})}
  d.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.lb-topbar [data-drop]');
    if(!b){closeAll();return}
    var x=b.closest('.lb-drop'),o=x.classList.toggle('is-open');b.setAttribute('aria-expanded',o);closeAll(x);e.stopPropagation()});
  d.addEventListener('mouseover',function(e){
    var x=e.target.closest&&e.target.closest('.lb-topbar .lb-drop');
    if(x){x.classList.add('is-open');closeAll(x)}else if(e.target.closest&&e.target.closest('.lb-topbar'))closeAll()});
  d.addEventListener('keydown',function(e){e.key==='Escape'&&closeAll()});
  function size(){var t=d.querySelector('.lb-topbar');t&&d.documentElement.style.setProperty('--lb-hdr',t.getBoundingClientRect().height+'px')}
  var l=d.createElement('link');l.rel='stylesheet';l.href='/assets/css/tools-footer.css?v=2';d.head.appendChild(l);
  addEventListener('resize',size);addEventListener('load',size);size();
})();
""")

# --- header markup from the homepage ---
home = open('index.html', encoding='utf-8').read()
a = home.index('<div class="lb-topbar">')
b = home.index('</header>', a) + len('</header>')
h = home[a:b]
h = re.sub(r'(src|href)="(assets/)', r'\1="/\2', h)
h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
chev = '<svg class="h-3.5 w-3.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
h = re.sub(r'<i data-lucide="chevron-down"[^>]*></i>', chev, h)
links = [('/', 'Home'), ('/products', 'Hosting'), ('/deals', 'Deals'), ('/blog/', 'Blog'), ('/tools/', 'Tools'), ('/contact', 'Contact'), ('https://dashboard.licenbase.com/clientarea.php', 'Dashboard')]
menu = ('<details class="lb-tmenu"><summary class="lb-icon-btn" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></summary><ul>'
        + ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in links) + '</ul></details>')
h, n = re.subn(r'<button id="menu-open".*?</button>', menu, h, flags=re.S)
assert n == 1
h = re.sub(r'>\s+<', '><', h)
h = re.sub(r'\s{2,}', ' ', h)
h += '<link rel="stylesheet" href="/assets/css/tools-header.css?v=1"/><script src="/assets/js/tools-header.js?v=1" defer></script>'

# --- swap into the Next export: static HTML, inline flight payload in html, and RSC .txt ---
OLD_HTML = re.compile(r'<header class="relative z-30 h-16.*?</header>', re.S)
WRAP_HTML = re.compile(r'<div suppresshydrationwarning="true"><div class="lb-topbar">.*?tools-header\.js[^>]*></script></div>', re.S)
NEW = '<div id="lb-tools-header">' + h + '</div>'
node = json.dumps(["$", "div", None, {"dangerouslySetInnerHTML": {"__html": h}}], separators=(',', ':')).replace('<', '\\u003c')
BS, Q = chr(92), chr(34)


def patch_payload(s, esc):
    """Replace the old header element in the flight data. esc=True when quotes are written as backslash-quote (inline html script)."""
    q = BS + Q if esc else Q
    key = '[' + q + '$' + q + ',' + q + 'header' + q + ',null,{' + q + 'className' + q + ':' + q + 'relative z-30 h-16'
    while key in s:
        a = s.index(key)
        depth, i, instr = 0, a, False
        while True:
            if s.startswith(q, i):
                instr = not instr; i += len(q); continue
            c = s[i]
            if instr and c == BS: i += 2; continue
            if not instr and c in '[]':
                depth += 1 if c == '[' else -1
                if depth == 0: break
            i += 1
        rep = json.dumps(node)[1:-1] if esc else node
        s = s[:a] + rep + s[i + 1:]
    return s


# --- footer: same markup as the homepage, utilities scoped under #lb-tools-footer (tools ships its own Tailwind) ---
import subprocess, tempfile
f = home[home.index('<footer'):home.index('</footer>') + 9]
f = re.sub(r'<!--.*?-->', '', re.sub(r'(src|href)="(assets/)', r'\1="/\2', f), flags=re.S)
f = re.sub(r'>\s+<', '><', f)
with tempfile.TemporaryDirectory() as d:
    open(d + '/f.html', 'w', encoding='utf-8').write(f)
    open(d + '/in.css', 'w').write('@tailwind utilities;')
    open(d + '/cfg.js', 'w').write('const c=require(%s);c.important="#lb-tools-footer";c.content=[%s];c.corePlugins={preflight:false};module.exports=c' % (json.dumps(os.path.abspath('tailwind.config.js')), json.dumps(d.replace(chr(92), '/') + '/f.html')))
    subprocess.run(f'npx --yes tailwindcss@3.4.16 -c cfg.js -i in.css -o out.css --minify', cwd=d, shell=True, check=True)
    fcss = open(d + '/out.css', encoding='utf-8').read()
fcss += '#lb-tools-footer .lb-footer-logo{height:4.5rem;width:auto}'
open('assets/css/tools-footer.css', 'w', encoding='utf-8').write(fcss)
FOOT_HTML = f  # a <link> inside the hydrated tree triggers React #418, so tools-header.js loads tools-footer.css instead

# --emit-ts <fork source dir>: the fork renders the chrome from source, so write it as a module and skip the output patching below
if '--emit-ts' in sys.argv:
    from brand_tools import CTA_BANNER_HTML, BRAND_CSS_LINK
    # h stops at </header>, leaving .lb-shell and .lb-topbar open; unclosed, the browser nests the whole app shell inside them and React hydration fails (#418)
    assert h.count('<div') - h.count('</div>') == 2, 'header markup changed: re-check the open divs'
    css_at = h.index('<link rel="stylesheet" href="/assets/css/tools-header.css')
    header_html = h[:css_at] + '</div></div>' + h[css_at:]
    header_html = header_html.replace('<script src="/assets/js/tools-header.js', BRAND_CSS_LINK + '<script src="/assets/js/tools-header.js', 1)
    dest = os.path.join(sys.argv[sys.argv.index('--emit-ts') + 1], 'lib', 'lb-chrome.generated.ts')
    lines = ['// generated by build_tools_header.py --emit-ts from the LicenBase homepage header/footer; do not edit',
             'export const LB_HEADER_HTML = ' + json.dumps(header_html) + ';',
             'export const LB_FOOTER_HTML = ' + json.dumps(FOOT_HTML) + ';',
             'export const LB_CTA_HTML = ' + json.dumps(CTA_BANNER_HTML) + ';', '']
    open(dest, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
    print('wrote', dest)
    # the tab icon is derived from the site's own logo file, never hand-copied into the fork: it can then not
    # drift, be forgotten in a commit, or fall back to the NetDash glyph. an SVG used as an icon cannot load
    # external images, so the png is embedded
    png = base64.b64encode(open('assets/img/favicon-192x192.png', 'rb').read()).decode()
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><title>LicenBase</title><image href="data:image/png;base64,{png}" width="64" height="64"/></svg>'
    for rel in ('app/icon.svg', 'public/favicon.svg'):
        open(os.path.join(os.path.dirname(os.path.dirname(dest)), rel), 'w', encoding='utf-8', newline='').write(svg)
    print('wrote icon from assets/img/favicon-192x192.png')
    sys.exit(0)
FOOT_NEW = '<div id="lb-tools-footer">' + FOOT_HTML + '</div>'
FOOT_OLD = re.compile(r'<div id="lb-tools-footer">(?:<link[^>]*/>)?<footer.*?</footer></div>(?:<link rel="stylesheet" href="/assets/css/tools-footer\.css[^>]*/>)?|<footer class="border-border bg-background border-t">.*?</footer>', re.S)
# the shell layout chunk renders the footer client-side: make it emit the same global markup
CHUNK = glob.glob('tools/_next/static/chunks/app/(shell)/layout-*.js')[0]
c = open(CHUNK, encoding='utf-8').read()
c = re.sub(r'function R\(\)\{return.*?\}(?=function W\(e\))', lambda m: 'function R(){return(0,n.jsx)("div",{id:"lb-tools-footer",dangerouslySetInnerHTML:{__html:' + json.dumps(FOOT_HTML).replace('<', chr(92) + 'u003c') + '}})}', c, count=1, flags=re.S)
open(CHUNK, 'w', encoding='utf-8').write(c)
RAWEND = re.compile(r'(tools-header\.js\?v=1(?:\\)+" defer>)</script>')
LABEL = re.compile(r'(lb-header-signin(?:\\)*">)Get Started<')

done = 0
for f in [x for x in glob.glob('tools/**/*.html', recursive=True) + glob.glob('tools/**/*.txt', recursive=True) if os.path.isfile(x)]:
    s = open(f, encoding='utf-8', newline='').read()
    t = s
    if f.endswith('.html'):
        t = WRAP_HTML.sub(lambda m: NEW, t)
        t = FOOT_OLD.sub(lambda m: FOOT_NEW, t)
        t = LABEL.sub(r'\1All Products<', t)
        t = OLD_HTML.sub(lambda m: NEW, t, count=1)
        t = patch_payload(t, True)
        t = RAWEND.sub(lambda m: m.group(1) + chr(92) + 'u003c/script>', t)  # raw </script> in the flight string ends the script early
    else:
        t = patch_payload(t, False)
        t = LABEL.sub(r'\1All Products<', t)
    if t != s: open(f, 'w', encoding='utf-8', newline='').write(t); done += 1
print('patched', done)

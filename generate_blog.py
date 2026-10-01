"""Build blog/index.html (served at /blog/) and blog/<slug>.html from blog_posts.POSTS.

Head/header/footer come from privacy-policy.html (so the nav always matches the rest of the site);
only the <title>/meta block and <main> are replaced. Asset URLs are made absolute for /blog/*.
Every post is validated first (see docs/blog-guidelines.md); a bad post stops the build.
Run:  python generate_blog.py      (or python publish_blog.py for the full pipeline)
"""
import html
import json
import math
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

from blog_posts import POSTS

BASE = "https://licenbase.com"
TEMPLATE = "privacy-policy.html"
LD = '  <script type="application/ld+json">{}</script>\n'
E = html.escape
H2_RE = re.compile(r"<h2 ([^>]*)>(.*?)</h2>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def og_url(slug):
    return f"{BASE}/assets/img/og/{slug}.png"


def img_path(slug, kind):
    return f"/assets/img/blog/{slug}-{kind}.webp"


def pretty(iso):
    d = date.fromisoformat(iso)
    return f"{d:%B} {d.day}, {d.year}"


def word_count(body):
    return len(TAG_RE.sub(" ", body).split())


def read_min(body):
    return max(1, math.ceil(word_count(body) / 200))


def absolutize(s):
    return re.sub(r'(href|src)="(assets/|favicon\.ico|site\.webmanifest)', r'\1="/\2', s)


def load_template(active="blog"):
    """active: 'blog' / 'contact' highlights that desktop nav link; None highlights nothing."""
    s = Path(TEMPLATE).read_text(encoding="utf-8")
    head_a = s[: s.index("  <title>")]
    i = s.index("  <!-- Favicon -->")
    j = s.index('  <main id="main">') + len('  <main id="main">')
    head_b = absolutize(s[i:j])
    nav = {"blog": ("/blog/", "Blog"), "contact": ("/contact", "Contact")}
    if active:
        href, label = nav[active]
        head_b = head_b.replace(
            f'<a href="{href}" class="lb-nav-link lb-nav-link--plain">{label}</a>',
            f'<a href="{href}" class="lb-nav-link lb-nav-link--plain text-brand font-bold" aria-current="page">{label}</a>',
        )
    tail = absolutize(s[s.index("  </main>"):])
    return head_a, head_b, tail


def meta_block(*, title, desc, path, image, image_alt, og_type, og_title, extra_meta="", ld=()):
    url = BASE + path
    out = f"""  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="{url}" />

  <!-- Open Graph -->
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="LicenBase" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{image}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="{image_alt}" />
  <meta property="og:locale" content="en_US" />
{extra_meta}
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{image}" />
  <meta name="twitter:image:alt" content="{image_alt}" />
  <meta name="twitter:title" content="{og_title}" />
  <meta name="twitter:description" content="{desc}" />

"""
    out += "".join(LD.format(json.dumps(o, ensure_ascii=False)) for o in ld) + "\n"
    return out


def crumbs(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": n, "name": name, "item": BASE + path}
            for n, (name, path) in enumerate(items, 1)
        ],
    }


# ---------------------------------------------------------------- validation
REQUIRED = ("slug", "title", "seo_title", "description", "excerpt", "category", "date", "updated",
            "image_alt", "og", "related", "faq", "body")


def validate(p):
    """Return a list of problems (empty = ok). Mirrors docs/blog-guidelines.md."""
    errs = []
    missing = [k for k in REQUIRED if k not in p]
    if missing:
        return [f"missing fields: {missing}"]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", p["slug"]) or len(p["slug"]) > 60:
        errs.append("slug must be lowercase-hyphenated, max 60 chars")
    full_title = html.unescape(p["seo_title"]) + " | LicenBase"
    if len(full_title) > 60:
        errs.append(f"<title> is {len(full_title)} chars (max 60): {full_title}")
    d = html.unescape(p["description"])
    if not 110 <= len(d) <= 160:
        errs.append(f"description is {len(d)} chars (110-160)")
    for k in ("date", "updated"):
        try:
            date.fromisoformat(p[k])
        except ValueError:
            errs.append(f"{k} must be YYYY-MM-DD")
    if len(p["title"]) > 70:
        errs.append("title (H1) over 70 chars")
    if not 40 <= len(html.unescape(p["image_alt"])) <= 125:
        errs.append("image_alt should be a 40-125 char description of the feature image")
    if not {"headline", "subtitle", "icon"} <= set(p["og"]):
        errs.append("og needs headline, subtitle, icon (used for the social/feature image)")
    for s, _ in p["related"]:
        if not Path(f"{s}.html").exists():
            errs.append(f"related product page not found: {s}.html")
    if not 3 <= len(p["faq"]) <= 8:
        errs.append("faq needs 3-8 questions")
    if len(H2_RE.findall(p["body"])) < 3:
        errs.append("body needs at least 3 H2 sections")
    if "<h1" in p["body"]:
        errs.append("body must not contain an H1 (the page title is the H1)")
    total = word_count(p["body"]) + sum(len((q + " " + a).split()) for q, a in p["faq"])
    if total < 700:
        errs.append(f"article is {total} words including the FAQ (minimum 700)")
    imgs = re.findall(r"<img [^>]*>", p["body"])
    if not imgs:
        errs.append("body needs at least one in-article image (see figure() in blog_posts.py)")
    for im in imgs:
        if not re.search(r'alt="[^"]{10,}"', im):
            errs.append("every in-article image needs descriptive alt text (10+ chars)")
        m = re.search(r'src="/(assets/[^"]+)"', im)
        if not m or not Path(m.group(1)).exists():
            errs.append(f"in-article image file missing: {m.group(1) if m else im[:60]}")
    links = re.findall(r'href="/([a-z0-9-]+-license)"', p["body"])
    if len(set(links)) < 2:
        errs.append("body needs links to at least 2 different product pages")
    return errs


# ---------------------------------------------------------------- components
def toc_and_body(p):
    """Add ids to H2s, append the FAQ section as interactive accordions, return (body_html, [(id, text)])."""
    toc = []

    def add_id(m):
        text = TAG_RE.sub("", m.group(2))
        slug = re.sub(r"[^a-z0-9]+", "-", html.unescape(text).lower()).strip("-")
        toc.append((slug, text))
        return f'<h2 id="{slug}" style="scroll-margin-top:7rem" {m.group(1)}>{m.group(2)}</h2>'

    body = H2_RE.sub(add_id, p["body"])
    faqs_html = "".join(f"""
        <div class="lb-faq{' lb-faq-active' if idx == 1 else ''} rounded-2xl border border-gray-200 bg-white shadow-sm transition">
          <button id="faq-question-{idx}" class="lb-faq-btn" type="button" aria-expanded="{'true' if idx == 1 else 'false'}" aria-controls="faq-answer-{idx}">
            <span class="lb-faq-icon-wrap"><i data-lucide="help-circle" class="h-5 w-5" aria-hidden="true"></i></span>
            <span class="lb-faq-question">{E(q)}</span>
            <span class="lb-faq-chevron" aria-hidden="true"><i data-lucide="chevron-down" class="lb-faq-icon h-5 w-5"></i></span>
          </button>
          <div id="faq-answer-{idx}" class="lb-faq-panel{' lb-faq-open' if idx == 1 else ''}" role="region" aria-labelledby="faq-question-{idx}">
            <div class="lb-faq-answer-wrap">
              <p class="lb-faq-answer">{E(a)}</p>
            </div>
          </div>
        </div>""" for idx, (q, a) in enumerate(p["faq"], 1))
    body += (f'\n<section class="space-y-4"><h2 id="faq" style="scroll-margin-top:7rem" class="font-display text-2xl font-bold tracking-tight text-navy">'
             f'Frequently asked questions</h2><div class="lb-stagger mt-6 space-y-3">{faqs_html}\n</div></section>\n')
    toc.append(("faq", "Frequently asked questions"))
    return body, toc


def thumb(p):
    return (f'<img src="{img_path(p["slug"], "thumb")}" alt="" width="640" height="336" '
            f'class="aspect-[1200/630] w-full object-cover" loading="lazy" decoding="async" />')


def card(p):
    return f"""        <a href="/blog/{p['slug']}" class="group flex flex-col overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm transition hover:border-brand/30 hover:shadow-lg">
          {thumb(p)}
          <div class="flex flex-1 flex-col justify-between p-6">
            <div>
              <div class="flex items-center justify-between text-xs">
                <span class="rounded-md bg-mist px-2.5 py-1 font-bold text-brand uppercase tracking-wider">{p['category']}</span>
                <span class="text-gray-400 font-medium">{read_min(p['body'])} min read</span>
              </div>
              <h2 class="mt-3 font-display text-lg font-bold text-navy transition-colors group-hover:text-brand">{E(p['title'])}</h2>
              <p class="mt-2 text-sm leading-relaxed text-gray-500">{p['excerpt']}</p>
            </div>
            <div class="mt-5 flex items-center justify-between border-t border-gray-100 pt-3 text-xs">
              <span class="font-medium text-gray-400">{pretty(p['date'])}</span>
              <span class="inline-flex items-center gap-1 font-bold text-brand">Read article <i data-lucide="arrow-up-right" class="h-3.5 w-3.5"></i></span>
            </div>
          </div>
        </a>
"""


def share_links(p):
    url, title = quote(f"{BASE}/blog/{p['slug']}", safe=""), quote(html.unescape(p["title"]), safe="")
    items = [
        ("X", f"https://twitter.com/intent/tweet?url={url}&amp;text={title}", "twitter"),
        ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={url}", "linkedin"),
        ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={url}", "facebook"),
        ("Email", f"mailto:?subject={title}&amp;body={url}", "mail"),
    ]
    return "".join(
        f'<a href="{href}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 rounded-lg border border-gray-200 bg-white px-3 py-2 text-xs font-semibold text-gray-700 transition hover:border-brand/30 hover:text-brand">'
        f'<i data-lucide="{icon}" class="h-3.5 w-3.5"></i>{label}</a>'
        for label, href, icon in items)


# ---------------------------------------------------------------- pages
def build_index(tpl):
    head_a, head_b, tail = tpl
    title = "Hosting Guides &amp; License Comparisons | LicenBase Blog"
    desc = "Guides and comparisons on cPanel, Plesk, LiteSpeed and other hosting licenses: setup how-tos, buying advice and tips for hosting providers."
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    ld = [
        crumbs([("Home", "/"), ("Blog", "/blog/")]),
        {
            "@context": "https://schema.org", "@type": "Blog", "name": "LicenBase Blog",
            "url": BASE + "/blog/", "description": html.unescape(desc), "inLanguage": "en",
            "publisher": {"@type": "Organization", "name": "LicenBase", "url": BASE + "/"},
            "blogPost": [
                {"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}/blog/{p['slug']}",
                 "datePublished": p["date"], "image": og_url(f"blog-{p['slug']}")}
                for p in posts],
        },
    ]
    head = meta_block(title=title, desc=desc, path="/blog/", image=og_url("blog"),
                      image_alt="LicenBase blog: hosting license guides and comparisons",
                      og_type="website", og_title="Hosting Guides &amp; License Comparisons", ld=ld)
    main = f"""

  <section class="border-b border-gray-200 bg-mist py-12 lg:py-16">
    <div class="lb-shell">
      <div class="max-w-3xl">
        <nav aria-label="Breadcrumb" class="mb-4 flex items-center gap-2 text-xs font-semibold text-gray-500">
          <a href="/" class="transition hover:text-brand">Home</a>
          <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
          <span class="text-brand">Blog</span>
        </nav>
        <h1 class="font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl lg:text-5xl">LicenBase Blog</h1>
        <p class="mt-4 text-base leading-relaxed text-gray-600 sm:text-lg">Practical guides and honest comparisons on cPanel, Plesk, LiteSpeed and the rest of the hosting software stack.</p>
      </div>
    </div>
  </section>

  <section class="py-12 lg:py-16">
    <div class="lb-shell">
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{"".join(card(p) for p in posts)}      </div>
    </div>
  </section>

"""
    Path("blog").mkdir(exist_ok=True)
    Path("blog/index.html").write_text(head_a + head + head_b + main + tail, encoding="utf-8", newline="\n")
    print("wrote blog/index.html")


def build_post(tpl, p):
    head_a, head_b, tail = tpl
    path = f"/blog/{p['slug']}"
    url = BASE + path
    img = og_url(f"blog-{p['slug']}")
    desc = p["description"]
    body, toc = toc_and_body(p)
    words = word_count(body)
    mins = max(1, math.ceil(words / 200))
    ld = [
        crumbs([("Home", "/"), ("Blog", "/blog/"), (p["title"], path)]),
        {
            "@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
            "description": html.unescape(desc), "image": [img],
            "datePublished": p["date"], "dateModified": p["updated"],
            "author": {"@type": "Organization", "name": "LicenBase", "url": BASE + "/"},
            "publisher": {"@type": "Organization", "name": "LicenBase",
                          "logo": {"@type": "ImageObject", "url": BASE + "/assets/img/logo.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "articleSection": p["category"], "inLanguage": "en", "wordCount": words,
        },
        {
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in p["faq"]],
        },
    ]
    extra = (f'  <meta property="article:published_time" content="{p["date"]}" />\n'
             f'  <meta property="article:modified_time" content="{p["updated"]}" />\n'
             f'  <meta property="article:section" content="{p["category"]}" />\n'
             f'  <meta property="article:author" content="LicenBase" />\n')
    head = meta_block(title=f"{p['seo_title']} | LicenBase", desc=desc, path=path, image=img,
                      image_alt=p["image_alt"], og_type="article",
                      og_title=p["seo_title"], extra_meta=extra, ld=ld)
    toc_html = "".join(
        f'<a href="#{i}" class="block rounded-lg px-3 py-1.5 text-sm font-medium text-gray-700 transition hover:bg-brandSoft hover:text-brand">{t}</a>'
        for i, t in toc)
    related = "".join(
        f'<li><a href="/{s}" class="flex items-center justify-between rounded-lg px-3 py-2 text-sm font-semibold text-navy transition hover:bg-brandSoft hover:text-brand">{E(label)}<i data-lucide="arrow-right" class="h-3.5 w-3.5"></i></a></li>'
        for s, label in p["related"])
    same_cat = [o for o in POSTS if o["slug"] != p["slug"] and o.get("category") == p.get("category")]
    diff_cat = [o for o in POSTS if o["slug"] != p["slug"] and o.get("category") != p.get("category")]
    same_cat.sort(key=lambda o: o["date"], reverse=True)
    diff_cat.sort(key=lambda o: o["date"], reverse=True)
    others = (same_cat + diff_cat)[:6]
    more = f"""
  <section class="border-t border-gray-200 bg-mist py-12 lg:py-16">
    <div class="lb-shell">
      <h2 class="font-display text-2xl font-bold tracking-tight text-navy">Keep reading</h2>
      <div class="mt-6 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{"".join(card(o) for o in others)}      </div>
    </div>
  </section>
""" if others else ""
    updated = (f'<span>Updated <time datetime="{p["updated"]}">{pretty(p["updated"])}</time></span>'
               if p["updated"] != p["date"] else "")
    main = f"""

  <section class="border-b border-gray-200 bg-mist py-12 lg:py-16">
    <div class="lb-shell">
      <div class="max-w-3xl">
        <nav aria-label="Breadcrumb" class="mb-4 flex flex-wrap items-center gap-2 text-xs font-semibold text-gray-500">
          <a href="/" class="transition hover:text-brand">Home</a>
          <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
          <a href="/blog/" class="transition hover:text-brand">Blog</a>
          <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
          <span class="text-brand">{E(p['category'])}</span>
        </nav>
        <span class="rounded-md bg-white px-2.5 py-1 text-xs font-bold uppercase tracking-wider text-brand">{p['category']}</span>
        <h1 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl lg:text-5xl">{E(p['title'])}</h1>
        <div class="mt-5 flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-gray-500">
          <span>By <span class="font-semibold text-navy">LicenBase Team</span></span>
          <span>Published <time datetime="{p['date']}">{pretty(p['date'])}</time></span>
          {updated}
          <span>{mins} min read</span>
        </div>
      </div>
    </div>
  </section>

  <section class="py-12 lg:py-16">
    <div class="lb-shell">
      <div class="grid gap-12 lg:grid-cols-[1fr_300px]">
        <div class="min-w-0 max-w-3xl">
          <figure>
            <img src="{img_path(p['slug'], 'feature')}" alt="{p['image_alt']}" width="1200" height="630" class="w-full rounded-2xl border border-gray-200" fetchpriority="high" decoding="async" />
          </figure>
          <article class="mt-10 space-y-10 leading-relaxed text-gray-700">
{body}
          </article>
          <div class="mt-12 flex flex-wrap items-center gap-2 border-t border-gray-200 pt-6">
            <span class="mr-2 text-sm font-bold text-navy">Share this article</span>
            {share_links(p)}
          </div>
        </div>

        <aside>
          <div class="space-y-6 lg:sticky lg:top-28">
            <nav id="toc" aria-label="Table of contents" class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
              <h2 class="text-xs font-bold uppercase tracking-wider text-gray-500">In this article</h2>
              <div class="mt-3 space-y-0.5">{toc_html}</div>
            </nav>
            <div class="rounded-2xl border border-gray-200 bg-mist p-5 shadow-sm">
              <h2 class="text-xs font-bold uppercase tracking-wider text-gray-500">Related licenses</h2>
              <ul class="mt-3 space-y-1">{related}</ul>
              <a href="/products" class="lb-btn lb-btn--primary mt-4 w-full text-center">Browse all licenses</a>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>
{more}
"""
    Path("blog").mkdir(exist_ok=True)
    Path(f"blog/{p['slug']}.html").write_text(head_a + head + head_b + main + tail, encoding="utf-8", newline="\n")
    print(f"wrote blog/{p['slug']}.html ({words} words, {mins} min read)")


if __name__ == "__main__":
    bad = {p.get("slug", "?"): validate(p) for p in POSTS}
    bad = {k: v for k, v in bad.items() if v}
    if bad:
        for slug, errs in bad.items():
            print(f"[INVALID] {slug}")
            for e in errs:
                print("   -", e)
        sys.exit(1)
    tpl = load_template("blog")
    build_index(tpl)
    for post in POSTS:
        build_post(tpl, post)

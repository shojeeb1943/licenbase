"""
generate_og.py  –  Render 1200×630 Open Graph cards for every LicenBase page.

Usage:
    python generate_og.py            # render all cards
    python generate_og.py cpanel     # render one slug only
    python generate_og.py --force    # force regenerate all

Output:  assets/img/og/<slug>.png   (also  og-home.png, og-deals.png, etc.)
The script is idempotent; existing images are only overwritten when --force is
passed or the PNG is older than this script.

Dependencies:  playwright  (pip install playwright && playwright install chromium)
"""

import argparse
import base64
import html as _html
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Load product data from generate_pages.py (exec the safe header section)
# ---------------------------------------------------------------------------
_ns: dict = {}
exec(open("generate_pages.py", encoding="utf-8").read().split("def generate_page")[0], _ns)
products: list[dict] = _ns["products"]

BASE = "https://licenbase.com"
OUT_DIR = Path("assets/img/og")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Icon SVGs – sourced from assets/img/icons/*.svg (read at runtime)
# ---------------------------------------------------------------------------

def _read_svg(name: str) -> str:
    path = Path(f"assets/img/icons/{name}.svg")
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return ""


FALLBACK_ICONS: dict[str, str] = {
    "server": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>',
    "zap":    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "layout-grid": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "credit-card": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>',
    "shield-check": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
    "cpu":    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    "globe":  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "users":  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "layers": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "database": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "lock":   '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "layout-dashboard": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>',
    "layout": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>',
    "home":   '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "tag":    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
    "info":   '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
}


def get_product_icon_svg(product: dict) -> str:
    """Return inline SVG for a product."""
    slug = product["slug"]
    icon_key = product.get("icon", slug)
    # 1. Try assets/img/icons/<slug>.svg
    svg = _read_svg(slug)
    if svg:
        return svg
    # 2. Try assets/img/icons/<icon_key>.svg
    svg = _read_svg(icon_key)
    if svg:
        return svg
    # 3. Fallback to inline map
    return FALLBACK_ICONS.get(icon_key, FALLBACK_ICONS["server"])


def get_static_icon_svg(icon_key: str) -> str:
    svg = _read_svg(icon_key)
    return svg or FALLBACK_ICONS.get(icon_key, FALLBACK_ICONS["info"])


# ---------------------------------------------------------------------------
# Logo: embed as base64 data URI so HTML works without a server
# ---------------------------------------------------------------------------

def _logo_data_uri() -> str:
    for p in ("assets/img/logo-white.png", "assets/img/logo.png"):
        path = Path(p)
        if path.exists():
            data = base64.b64encode(path.read_bytes()).decode()
            ext = path.suffix.lstrip(".")
            return f"data:image/{ext};base64,{data}"
    return ""


LOGO_URI = _logo_data_uri()


# ---------------------------------------------------------------------------
# HTML card template
# ---------------------------------------------------------------------------

def _card_html(*, headline: str, subtitle: str, pill: str,
               icon_svg: str, price_label: str,
               footer_left: str = "licenbase.com") -> str:
    def e(s: str) -> str:
        return _html.escape(s)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1200px; height: 630px; overflow: hidden; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #1e40af 100%);
    position: relative;
    display: flex;
    flex-direction: column;
    padding: 52px 64px;
  }}
  body::before {{
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
  }}
  body::after {{
    content: '';
    position: absolute;
    top: -120px; right: -120px;
    width: 480px; height: 480px;
    background: radial-gradient(circle, rgba(30,64,175,0.55) 0%, transparent 70%);
    pointer-events: none;
    border-radius: 50%;
  }}
  .top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-shrink: 0;
  }}
  .logo {{
    height: 38px;
    width: auto;
  }}
  .pill {{
    background: rgba(16,185,129,0.18);
    border: 1.5px solid rgba(16,185,129,0.55);
    color: #34d399;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 6px 18px;
    border-radius: 999px;
  }}
  .centre {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    gap: 0;
    padding: 24px 0 20px;
    position: relative;
    z-index: 1;
  }}
  .icon-wrap {{
    width: 72px;
    height: 72px;
    background: rgba(255,255,255,0.10);
    border: 1.5px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
    flex-shrink: 0;
  }}
  .icon-wrap svg {{
    width: 38px;
    height: 38px;
    stroke: white;
    fill: none;
  }}
  h1 {{
    font-size: 58px;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.02em;
    color: #ffffff;
    margin: 0;
    max-width: 900px;
  }}
  .subtitle {{
    font-size: 22px;
    font-weight: 500;
    color: rgba(255,255,255,0.70);
    margin-top: 14px;
    line-height: 1.4;
    max-width: 800px;
  }}
  .footer {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid rgba(255,255,255,0.12);
    padding-top: 20px;
    flex-shrink: 0;
    position: relative;
    z-index: 1;
  }}
  .footer-left {{
    font-size: 15px;
    font-weight: 600;
    color: rgba(255,255,255,0.55);
    letter-spacing: 0.03em;
  }}
  .footer-price {{
    font-size: 20px;
    font-weight: 800;
    color: #34d399;
    letter-spacing: 0.01em;
  }}
</style>
</head>
<body>
  <div class="top">
    <img class="logo" src="{LOGO_URI}" alt="LicenBase" />
    <span class="pill">{e(pill)}</span>
  </div>
  <div class="centre">
    <div class="icon-wrap">
      {icon_svg}
    </div>
    <h1>{e(headline)}</h1>
    <p class="subtitle">{e(subtitle)}</p>
  </div>
  <div class="footer">
    <span class="footer-left">{e(footer_left)}</span>
    <span class="footer-price">{e(price_label)}</span>
  </div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Card specs
# ---------------------------------------------------------------------------

def _min_price(product: dict) -> str:
    prices = []
    for t in product["tiers"]:
        raw = t["price"].replace("$", "").strip()
        try:
            prices.append(float(raw))
        except ValueError:
            pass
    if not prices:
        return "Contact us"
    lo = min(prices)
    period = product["tiers"][0]["period"]
    if "one-time" in period:
        return f"From ${lo:.2f} one-time"
    return f"From ${lo:.2f}/mo"


def product_card_spec(p: dict) -> dict:
    return {
        "slug":     p["slug"],
        "out_file": OUT_DIR / f"{p['slug']}.png",
        "headline": p["headline"],
        "subtitle": p["headline_sub"],
        "pill":     "INSTANT IP ACTIVATION",
        "icon_svg": get_product_icon_svg(p),
        "price":    _min_price(p),
    }


STATIC_PAGES = [
    {
        "slug":     "home",
        "out_file": OUT_DIR / "home.png",
        "headline": "Reliable, Cheap Hosting Licenses",
        "subtitle": "cPanel · LiteSpeed · CloudLinux · Plesk · WHMCS",
        "pill":     "INSTANT IP ACTIVATION",
        "icon_svg": FALLBACK_ICONS["server"],
        "price":    "From $1/mo",
    },
    {
        "slug":     "products",
        "out_file": OUT_DIR / "products.png",
        "headline": "All Hosting Software Licenses",
        "subtitle": "14 products — monthly and one-time plans",
        "pill":     "GENUINE LICENSES",
        "icon_svg": FALLBACK_ICONS["layers"],
        "price":    "From $1/mo",
    },
    {
        "slug":     "deals",
        "out_file": OUT_DIR / "deals.png",
        "headline": "Exclusive License Deals & Bundles",
        "subtitle": "Limited-time savings on cPanel, LiteSpeed & more",
        "pill":     "LIMITED TIME OFFERS",
        "icon_svg": FALLBACK_ICONS["tag"],
        "price":    "Save up to 40%",
    },
    {
        "slug":     "policies",
        "out_file": OUT_DIR / "policies.png",
        "headline": "LicenBase Policies",
        "subtitle": "Privacy · Terms of Service · Refund · License Policy",
        "pill":     "TRANSPARENT POLICIES",
        "icon_svg": FALLBACK_ICONS["info"],
        "price":    "licenbase.com",
    },
]

# Blog index + one card per post (content lives in blog_posts.py)
from blog_posts import POSTS as _POSTS

BLOG_SPECS = [
    {
        "slug":     "blog",
        "out_file": OUT_DIR / "blog.png",
        "headline": "LicenBase Blog",
        "subtitle": "Hosting license guides and comparisons",
        "pill":     "GUIDES & COMPARISONS",
        "icon_svg": FALLBACK_ICONS["globe"],
        "price":    "licenbase.com/blog",
    },
] + [
    {
        "slug":     f"blog-{_bp['slug']}",
        "out_file": OUT_DIR / f"blog-{_bp['slug']}.png",
        "headline": _bp["og"]["headline"],
        "subtitle": _bp["og"]["subtitle"],
        "pill":     _bp["category"].upper(),
        "icon_svg": FALLBACK_ICONS[_bp["og"]["icon"]],
        "price":    "licenbase.com/blog",
    }
    for _bp in _POSTS
]

COMPANY_SPECS = [
    {
        "slug":     "about",
        "out_file": OUT_DIR / "about.png",
        "headline": "About LicenBase",
        "subtitle": "Hosting software licenses, activated on your server IP",
        "pill":     "WHO WE ARE",
        "icon_svg": FALLBACK_ICONS["users"],
        "price":    "licenbase.com",
    },
    {
        "slug":     "contact",
        "out_file": OUT_DIR / "contact.png",
        "headline": "Contact LicenBase",
        "subtitle": "Pre-sales questions, order help and license support",
        "pill":     "WE ARE HERE TO HELP",
        "icon_svg": FALLBACK_ICONS["globe"],
        "price":    "support@licenbase.com",
    },
]

# Legal pages map to the shared policies card
LEGAL_SLUG_MAP = {
    "privacy-policy":   "policies",
    "terms-of-service": "policies",
    "refund-policy":    "policies",
    "license-policy":   "policies",
}

# Exported: full slug → absolute URL path for og:image
SLUG_TO_OG_PATH: dict[str, str] = {}
for _p in products:
    SLUG_TO_OG_PATH[_p["slug"]] = f"/assets/img/og/{_p['slug']}.png"
for _sp in STATIC_PAGES:
    SLUG_TO_OG_PATH[_sp["slug"]] = f"/assets/img/og/{_sp['slug']}.png"
for _legal, _target in LEGAL_SLUG_MAP.items():
    SLUG_TO_OG_PATH[_legal] = f"/assets/img/og/{_target}.png"


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def _derive_blog_images(png: Path) -> None:
    """blog-<slug>.png -> assets/img/blog/<slug>-feature.webp (1200x630, on-page) and -thumb.webp (640x336, cards)."""
    if not png.name.startswith("blog-"):
        return
    try:
        from PIL import Image
    except ImportError:
        print("  !  Pillow missing: feature/thumb webp not created (pip install pillow)")
        return
    slug = png.stem[len("blog-"):]
    out_dir = Path("assets/img/blog")
    out_dir.mkdir(parents=True, exist_ok=True)
    img = Image.open(png).convert("RGB")
    img.save(out_dir / f"{slug}-feature.webp", "WEBP", quality=82, method=6)
    img.resize((640, 336), Image.LANCZOS).save(out_dir / f"{slug}-thumb.webp", "WEBP", quality=80, method=6)
    print(f"  v  assets/img/blog/{slug}-feature.webp + -thumb.webp")


def render_card(spec: dict, page: object) -> None:  # type: ignore[type-arg]
    out: Path = spec["out_file"]
    card_html = _card_html(
        headline=spec["headline"],
        subtitle=spec["subtitle"],
        pill=spec["pill"],
        icon_svg=spec["icon_svg"],
        price_label=spec["price"],
    )
    page.set_content(card_html, wait_until="domcontentloaded")  # type: ignore[attr-defined]
    page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1200, "height": 630})  # type: ignore[attr-defined]

    # Optimize PNG to keep file well under 300 KB
    try:
        from PIL import Image
        img = Image.open(str(out))
        img.save(str(out), "PNG", optimize=True, compress_level=9)
    except ImportError:
        pass  # Pillow not installed; Playwright screenshot is still fine

    kb = out.stat().st_size / 1024
    print(f"  v  {out}  ({kb:.0f} KB)")
    _derive_blog_images(out)



BLOG_ONLY = False


def main(only_slug: str | None = None, force: bool = False) -> None:
    from playwright.sync_api import sync_playwright

    all_specs: list[dict] = [product_card_spec(p) for p in products] + list(STATIC_PAGES) + BLOG_SPECS + COMPANY_SPECS

    if BLOG_ONLY:
        all_specs = list(BLOG_SPECS)
    if only_slug:
        all_specs = [s for s in all_specs if s["slug"] == only_slug]
        if not all_specs:
            print(f"No spec found for slug '{only_slug}'")
            sys.exit(1)

    if not force:
        script_mtime = Path(__file__).stat().st_mtime
        pending = []
        for s in all_specs:
            out: Path = s["out_file"]
            if out.exists() and out.stat().st_mtime > script_mtime:
                print(f"  -  skip  {out}  (up to date)")
            else:
                pending.append(s)
        all_specs = pending

    if not all_specs:
        print("All cards are up to date. Pass --force to regenerate.")
        return

    print(f"Rendering {len(all_specs)} card(s)...")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1200, "height": 630})
        page = ctx.new_page()
        for spec in all_specs:
            render_card(spec, page)
        browser.close()

    print("\nDone.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LicenBase OG card images.")
    parser.add_argument("slug", nargs="?", help="Render one slug only (e.g. cpanel)")
    parser.add_argument("--force", action="store_true", help="Force regenerate all")
    parser.add_argument("--blog", action="store_true", help="Re-render only the blog cards (+ feature/thumb images)")
    args = parser.parse_args()
    if args.blog:
        BLOG_ONLY = True
    main(only_slug=args.slug, force=args.force or args.blog)

"""
patch_og_images.py  –  Update og:image / twitter:image tags in ALREADY-PATCHED
                       HTML pages (those that seo_apply.py skips because they
                       already have application/ld+json).

Run this once after generate_og.py to bring all existing HTML files into sync
with the new per-page OG card images.

Idempotent: safe to run multiple times.
"""
import html as _html
import re
from pathlib import Path

BASE = "https://licenbase.com"

# Static page -> OG image URL
PAGE_CFG: dict[str, dict] = {
    "index.html": {
        "img":  BASE + "/assets/img/og/home.png",
        "alt":  "Reliable, cheap hosting licenses – LicenBase",
    },
    "products.html": {
        "img":  BASE + "/assets/img/og/products.png",
        "alt":  "All hosting software licenses – LicenBase",
    },
    "deals.html": {
        "img":  BASE + "/assets/img/og/deals.png",
        "alt":  "Exclusive license deals and bundles – LicenBase",
    },
    "privacy-policy.html": {
        "img":  BASE + "/assets/img/og/policies.png",
        "alt":  "LicenBase privacy and legal policies",
    },
    "terms-of-service.html": {
        "img":  BASE + "/assets/img/og/policies.png",
        "alt":  "LicenBase terms of service",
    },
    "refund-policy.html": {
        "img":  BASE + "/assets/img/og/policies.png",
        "alt":  "LicenBase refund policy",
    },
    "license-policy.html": {
        "img":  BASE + "/assets/img/og/policies.png",
        "alt":  "LicenBase license policy",
    },
}

# Product pages: build from generate_pages.py data
_ns: dict = {}
exec(open("generate_pages.py", encoding="utf-8").read().split("def generate_page")[0], _ns)
for _p in _ns["products"]:
    PAGE_CFG[_p["filename"]] = {
        "img": BASE + f"/assets/img/og/{_p['slug']}.png",
        "alt": f"{_p['name']} license from LicenBase",
    }


def _patch(filename: str, cfg: dict) -> None:
    path = Path(filename)
    if not path.exists():
        print(f"  skip (not found): {filename}")
        return

    text = path.read_text(encoding="utf-8", errors="replace")
    changed = False
    img = cfg["img"]
    alt = _html.escape(cfg["alt"])

    # ---- og:image ----
    old_og = re.search(r'<meta property="og:image" content="([^"]*)" />', text)
    if old_og:
        if old_og.group(1) != img:
            text = text.replace(old_og.group(0), f'<meta property="og:image" content="{img}" />', 1)
            changed = True

    # ---- og:image:width / height / type / alt ----
    # We insert them right after og:image if not already present
    og_img_tag = f'<meta property="og:image" content="{img}" />'
    dim_block = (
        f'<meta property="og:image" content="{img}" />\n'
        f'  <meta property="og:image:width" content="1200" />\n'
        f'  <meta property="og:image:height" content="630" />\n'
        f'  <meta property="og:image:type" content="image/png" />\n'
        f'  <meta property="og:image:alt" content="{alt}" />'
    )
    if 'og:image:width' not in text:
        text = text.replace(og_img_tag, dim_block, 1)
        changed = True
    else:
        # Update existing og:image:alt
        old_alt = re.search(r'<meta property="og:image:alt" content="([^"]*)" />', text)
        if old_alt and old_alt.group(1) != cfg["alt"]:
            text = text.replace(
                old_alt.group(0),
                f'<meta property="og:image:alt" content="{alt}" />',
                1,
            )
            changed = True

    # ---- twitter:image ----
    old_tw = re.search(r'<meta name="twitter:image" content="([^"]*)" />', text)
    if old_tw:
        if old_tw.group(1) != img:
            text = text.replace(old_tw.group(0), f'<meta name="twitter:image" content="{img}" />', 1)
            changed = True

    # ---- twitter:image:alt ----
    if 'twitter:image:alt' not in text:
        tw_img_tag = f'<meta name="twitter:image" content="{img}" />'
        text = text.replace(
            tw_img_tag,
            tw_img_tag + f'\n  <meta name="twitter:image:alt" content="{alt}" />',
            1,
        )
        changed = True
    else:
        old_tw_alt = re.search(r'<meta name="twitter:image:alt" content="([^"]*)" />', text)
        if old_tw_alt and old_tw_alt.group(1) != cfg["alt"]:
            text = text.replace(
                old_tw_alt.group(0),
                f'<meta name="twitter:image:alt" content="{alt}" />',
                1,
            )
            changed = True

    # ---- JSON-LD product image ----
    # Replace og-default.png references inside ld+json blocks
    if "og-default.png" in text:
        text = text.replace(
            "https://licenbase.com/assets/img/og-default.png",
            img,
        )
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
        print(f"  patched  {filename}")
    else:
        print(f"  ok       {filename}")


print("Patching OG image tags in all HTML pages...")
for fname, cfg in PAGE_CFG.items():
    _patch(fname, cfg)
print("Done.")

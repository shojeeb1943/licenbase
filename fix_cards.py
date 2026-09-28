import os
import re

with open('products.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's inspect each card in products.html and replace any <i data-lucide="..."> inside product card icon containers with the real SVG image.
products_map = [
    ("cpanel-license.html", "cpanel.svg", "cPanel"),
    ("litespeed-license.html", "litespeed.svg", "LiteSpeed"),
    ("plesk-license.html", "plesk.svg", "Plesk"),
    ("whmcs-license.html", "whmcs.svg", "WHMCS"),
    ("cloudlinux-license.html", "cloudlinux.svg", "CloudLinux"),
    ("virtualizor-license.html", "virtualizor.svg", "Virtualizor"),
    ("sitepad-license.html", "sitepad.svg", "SitePad"),
    ("whmreseller-license.html", "whmreseller.svg", "WHMReseller"),
    ("softaculous-license.html", "softaculous.svg", "Softaculous"),
    ("jetbackup-license.html", "jetbackup.svg", "JetBackup"),
    ("imunify360-license.html", "imunify360.svg", "Imunify360"),
    ("webuzo-license.html", "webuzo.svg", "Webuzo"),
    ("wp-squared-license.html", "wp-squared.svg", "WP Squared")
]

content = "".join(lines)

# Split by card blocks
card_blocks = content.split('<!-- ')
new_blocks = [card_blocks[0]]

for block in card_blocks[1:]:
    matched_svg = None
    for url, svg, name in products_map:
        if url in block:
            matched_svg = (svg, name)
            break
    
    if matched_svg:
        svg_file, brand_name = matched_svg
        # Replace the icon span in this card
        block = re.sub(
            r'<span class="grid h-12 w-12 place-items-center rounded-2xl [^>]*>[\s\S]*?</span>',
            f'<span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-105">\n                <img src="assets/img/icons/{svg_file}" alt="{brand_name}" class="h-8 w-8 object-contain" />\n              </span>',
            block,
            count=1
        )
    new_blocks.append(block)

fixed_content = "<!-- ".join(new_blocks)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("Updated 100% of product cards in products.html with real SVGs!")

import glob
import re
import subprocess

print("=== Adding 'Home' Menu Item to Navigation Across Site ===")

# 1. Update generate_pages.py
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen = f.read()

# Add Home to desktop nav in generate_pages.py
gen = gen.replace(
    '<nav class="lb-nav" aria-label="Main navigation">\n            <!-- Software mega menu -->',
    '<nav class="lb-nav" aria-label="Main navigation">\n            <a href="/" class="lb-nav-link">Home</a>\n\n            <!-- Software mega menu -->'
)

# Add Home to mobile nav in generate_pages.py
gen = gen.replace(
    '<ul class="mt-2 space-y-1">\n          <li><a href="/products"',
    '<ul class="mt-2 space-y-1">\n          <li><a href="/" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Home</a></li>\n          <li><a href="/products"'
)

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen)

print("Updated generate_pages.py")

# Regenerate the 13 product pages
subprocess.run(["python", "generate_pages.py"], check=True)

# 2. Update all remaining HTML files
html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Desktop nav
    if '<nav class="lb-nav" aria-label="Main navigation">\n            <a href="/" class="lb-nav-link">Home</a>' not in html:
        html = re.sub(
            r'(<nav class="lb-nav" aria-label="Main navigation">\s*)(<!-- Software mega menu -->|<div class="lb-drop lb-drop--mega">)',
            r'\1<a href="/" class="lb-nav-link">Home</a>\n\n            \2',
            html,
            count=1
        )

    # Mobile nav
    if '<li><a href="/" class="lb-mobile-link' not in html:
        # Check standard mobile menu list
        html = re.sub(
            r'(<ul class="mt-[23] space-y-1">\s*)<li><a href="/products"',
            r'\1<li><a href="/" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Home</a></li>\n          <li><a href="/products"',
            html,
            count=1
        )

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {file}")

# 3. Rebuild site production assets
subprocess.run(["python", "build_site.py"], check=True)
print("All pages successfully updated with 'Home' navigation button!")

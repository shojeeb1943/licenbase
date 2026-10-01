"""patch_manifest.py – Injects site.webmanifest, 512x512 icon, and theme-color into all HTML pages."""
import glob
import re

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    orig = content

    # Replace favicon.png with favicon-512x512.png
    content = content.replace('href="assets/img/favicon.png?v=2"', 'href="assets/img/favicon-512x512.png?v=2"')
    
    # Inject manifest & theme-color if not present
    if '<link rel="manifest"' not in content:
        # Match right after apple-touch-icon
        pattern = r'(<link rel="apple-touch-icon" [^>]+>)'
        if re.search(pattern, content):
            replacement = r'\1\n  <link rel="manifest" href="site.webmanifest" />\n  <meta name="theme-color" content="#0a0f1d" />'
            content = re.sub(pattern, replacement, content, count=1)
        elif '<link rel="icon"' in content:
            # Fallback for pages like 404.html
            pattern = r'(<link rel="icon" [^>]+>)'
            replacement = r'\1\n  <link rel="manifest" href="site.webmanifest" />\n  <meta name="theme-color" content="#0a0f1d" />'
            content = re.sub(pattern, replacement, content, count=1)

    if content != orig:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Patched {f}")
    else:
        print(f"Already up to date: {f}")

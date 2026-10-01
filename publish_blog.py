"""Publish blog changes in one command (run after editing blog_posts.py):

    python publish_blog.py

validate + build pages -> social/feature/thumb images -> product-page guide cards -> sitemap -> CSS -> SEO audit.
Exits non-zero if any step fails or the audit reports errors/warnings. See docs/blog-guidelines.md.
"""
import re
import subprocess
import sys

PY = sys.executable
STEPS = [
    ("Validate posts and build blog pages", [PY, "generate_blog.py"]),
    ("Render social card + feature/thumb images", [PY, "generate_og.py", "--blog"]),
    ("Rebuild product pages (guide cards)", [PY, "generate_pages.py"]),
    ("Rebuild sitemap", [PY, "make_sitemap.py"]),
    ("Rebuild CSS", [PY, "build_css.py"]),
]

for label, cmd in STEPS:
    print(f"\n=== {label} ===")
    if subprocess.run(cmd).returncode:
        sys.exit(f"FAILED: {label}")

print("\n=== SEO audit ===")
out = subprocess.run([PY, "audit_seo.py"], capture_output=True, text=True, encoding="utf-8").stdout
for line in out.splitlines():
    if re.search(r"AUDIT RESULTS|\[WARN|\[FAIL|WARNING|blog:", line):
        print(line)
m = re.search(r"AUDIT RESULTS: (\d+) Critical Errors \| (\d+) Warnings", out)
if not m or m.group(1) != "0" or m.group(2) != "0":
    sys.exit("Audit not clean: fix the items above, then run again.")
print("\nOK: all blog checks passed. Review with `python serve.py` (http://localhost:8000/blog/), then commit.")

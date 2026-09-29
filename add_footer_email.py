import os
import glob
import re

old_col1 = '''        <!-- Col 1: Brand -->
        <div class="lg:col-span-2 space-y-4">
          <a href="index.html" class="inline-block" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" />
          </a>
          <p class="text-xs text-gray-500 leading-relaxed max-w-sm">
            LicenBase is the trusted software licensing platform for web hosts, enterprises, and digital agencies. Fast, automated, authentic license deployment.
          </p>
          <div class="flex items-center gap-3 pt-2">
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="Twitter"><i data-lucide="twitter" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="GitHub"><i data-lucide="github" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="LinkedIn"><i data-lucide="linkedin" class="h-4 w-4"></i></a>
          </div>
        </div>'''

new_col1 = '''        <!-- Col 1: Brand -->
        <div class="lg:col-span-2 space-y-4">
          <a href="index.html" class="inline-block" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" />
          </a>
          <p class="text-xs text-gray-500 leading-relaxed max-w-sm">
            LicenBase is the trusted software licensing platform for web hosts, enterprises, and digital agencies. Fast, automated, authentic license deployment.
          </p>
          <div class="flex items-center gap-2 text-xs font-semibold text-gray-600">
            <i data-lucide="mail" class="h-4 w-4 text-brand"></i>
            <a href="mailto:support@licenbase.com" class="transition hover:text-brand">support@licenbase.com</a>
          </div>
          <div class="flex items-center gap-3 pt-1">
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="Twitter"><i data-lucide="twitter" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="GitHub"><i data-lucide="github" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="LinkedIn"><i data-lucide="linkedin" class="h-4 w-4"></i></a>
          </div>
        </div>'''

# Update generate_pages.py
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen = f.read()

if old_col1 in gen:
    gen = gen.replace(old_col1, new_col1)
    with open("generate_pages.py", "w", encoding="utf-8") as f:
        f.write(gen)
    print("Updated generate_pages.py with support email in footer.")

# Run generate_pages.py to update all 13 product pages
os.system("python generate_pages.py")

# Update all HTML files
html_files = glob.glob("*.html")
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    if old_col1 in content:
        content = content.replace(old_col1, new_col1)
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated footer support email in {hf}")

print("Done! support@licenbase.com added to footer across all pages.")

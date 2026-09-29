import subprocess
import re
import glob

print("=== Building LicenBase High-Performance Production Assets ===")

# 1. Compile Tailwind CSS
print("1. Compiling Tailwind CSS...")
subprocess.run(
    ["npx", "--yes", "tailwindcss@3.4.16", "-i", "./assets/css/tailwind-input.css", "-o", "./assets/css/tailwind.min.css", "--minify"],
    check=True,
    shell=True
)

# 2. Minify custom styles.css
print("2. Minifying styles.css...")
with open("assets/css/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'/\*[\s\S]*?\*/', '', css)
css = re.sub(r'\s+', ' ', css)
css = re.sub(r'\s*([\{\}:;,>+~])\s*', r'\1', css)
css = re.sub(r';\}', '}', css)
css = css.strip()

with open("assets/css/styles.min.css", "w", encoding="utf-8") as f:
    f.write(css)
print(f"   -> assets/css/styles.min.css ({len(css)} bytes)")

# 3. Minify main.js with esbuild
print("3. Minifying main.js...")
subprocess.run(
    ["npx", "--yes", "esbuild", "assets/js/main.js", "--minify", "--outfile=assets/js/main.min.js"],
    check=True,
    shell=True
)

# 4. Update generate_pages.py reference to main.min.js
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen_content = f.read()
gen_content = gen_content.replace('assets/js/main.js?v=7', 'assets/js/main.min.js?v=1')
gen_content = gen_content.replace('assets/js/main.js?v=6', 'assets/js/main.min.js?v=1')
with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_content)

# 5. Run generate_pages.py
print("4. Regenerating product pages...")
subprocess.run(["python", "generate_pages.py"], check=True)

# 6. Update all HTML files with main.min.js and ensure image dimensions
print("5. Updating all HTML files...")
files = glob.glob("*.html")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace('assets/js/main.js?v=7', 'assets/js/main.min.js?v=1')
    html = html.replace('assets/js/main.js?v=6', 'assets/js/main.min.js?v=1')
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)

# 7. Apply image dimensions across all HTML files
subprocess.run(["python", "add_image_dimensions.py"], check=True)

print("Build & optimization complete!")

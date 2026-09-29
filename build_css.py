import subprocess
import re
import os

print("1. Compiling Tailwind CSS...")
subprocess.run(
    ["npx", "--yes", "tailwindcss@3.4.16", "-i", "./assets/css/tailwind-input.css", "-o", "./assets/css/tailwind.min.css", "--minify"],
    check=True,
    shell=True
)

print("2. Minifying custom styles.css...")
with open("assets/css/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*[\s\S]*?\*/', '', css)
# Normalize whitespace
css = re.sub(r'\s+', ' ', css)
# Remove spaces around symbols
css = re.sub(r'\s*([\{\}:;,>+~])\s*', r'\1', css)
css = re.sub(r';\}', '}', css)
css = css.strip()

with open("assets/css/styles.min.css", "w", encoding="utf-8") as f:
    f.write(css)

print(f"styles.min.css created ({len(css)} bytes)")
print("CSS build completed successfully!")

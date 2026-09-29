import glob
import re

def process_img_tag(tag):
    if 'width=' in tag and 'height=' in tag:
        return tag

    # Check classes
    class_match = re.search(r'class="([^"]+)"', tag)
    classes = class_match.group(1) if class_match else ''
    
    w, h = 32, 32
    if 'h-4 w-4' in classes or 'w-4 h-4' in classes:
        w, h = 16, 16
    elif 'h-6 w-6' in classes or 'w-6 h-6' in classes:
        w, h = 24, 24
    elif 'h-7 w-7' in classes or 'w-7 h-7' in classes:
        w, h = 28, 28
    elif 'h-8 w-8' in classes or 'w-8 h-8' in classes:
        w, h = 32, 32
    elif 'h-9 w-9' in classes or 'w-9 h-9' in classes:
        w, h = 36, 36
    elif 'h-11 w-11' in classes or 'w-11 h-11' in classes:
        w, h = 44, 44
    elif 'lb-logo-img' in classes or 'lb-footer-logo' in classes:
        w, h = 250, 100
    elif 'h-7 w-auto' in classes:
        w, h = 70, 28
    elif 'h-8 w-auto' in classes:
        w, h = 80, 32

    new_tag = tag[:-1].rstrip('/') if tag.endswith('/>') else tag.rstrip('>')
    
    if 'width=' not in new_tag:
        new_tag += f' width="{w}"'
    if 'height=' not in new_tag:
        new_tag += f' height="{h}"'
    if 'decoding=' not in new_tag:
        new_tag += ' decoding="async"'
    if 'loading=' not in new_tag and 'fetchpriority=' not in new_tag:
        new_tag += ' loading="lazy"'

    new_tag += ' />' if tag.endswith('/>') else '>'
    return new_tag

files = glob.glob('*.html')
total_updated = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'<img[^>]+>', lambda m: process_img_tag(m.group(0)), content)
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_updated += 1
        print(f"Updated images in {file}")

print(f"Image attributes applied across {total_updated} files.")

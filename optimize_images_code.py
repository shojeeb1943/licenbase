import re

content = open('generate_pages.py', encoding='utf-8').read()

# 1. Mega-menu icons: add width="16" height="16" loading="lazy" decoding="async"
def fix_mega(match):
    tag = match.group(0)
    if 'width=' in tag:
        return tag
    return tag.replace('class="h-4 w-4 shrink-0 object-contain"', 'class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async"')

content = re.sub(r'<img src="assets/img/icons/[^"]+"[^>]+>', fix_mega, content)

# 2. Hero badge icon: add width="16" height="16" loading="eager" decoding="async"
content = re.sub(
    r'(<div class="inline-flex items-center gap-2\.5 rounded-full[^\"]*"[^>]*>\s*<img [^>]+?)(class="h-4 w-4 object-contain")',
    r'\1\2 width="16" height="16" loading="eager" decoding="async"',
    content
)

# 3. Hero card main icon: add width="32" height="32" loading="eager" decoding="async"
content = re.sub(
    r'(<span class="grid h-12 w-12[^\"]*"[^>]*>\s*<img [^>]+?)(class="h-8 w-8 object-contain")',
    r'\1\2 width="32" height="32" loading="eager" decoding="async"',
    content
)

with open('generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated generate_pages.py successfully')

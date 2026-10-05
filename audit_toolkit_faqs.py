import os
import re
import json

REGISTRY_PATH = "c:/dev/netdash-toolkit/lib/tool-registry.ts"
FAQS_DIR = "c:/dev/netdash-toolkit/lib/faqs"

with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    registry_text = f.read()

# Extract tool blocks from 'export const tools'
pos = registry_text.find("export const tools")
tools_block = registry_text[pos:]

tool_entries = re.findall(r'\{\s*slug:\s*"([^"]+)",\s*label:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*description:\s*(?:"([^"]+)"|`([^`]+)`),\s*(?:icon:[^,]+,\s*)?category:\s*"([^"]+)"', tools_block)

tools = []
for match in tool_entries:
    slug, label, title, desc1, desc2, cat = match
    desc = desc1 or desc2 or ""
    tools.append({
        "slug": slug,
        "title": title,
        "description": desc.strip(),
        "category": cat
    })

print(f"Total tools found in registry: {len(tools)}")

# Parse all FAQ files in FAQS_DIR
faq_data = {}
for fname in os.listdir(FAQS_DIR):
    if not fname.endswith(".ts"):
        continue
    fpath = os.path.join(FAQS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract keys and their FAQ arrays
    # Find all "slug": [ { q: "...", a: "..." }, ... ]
    for tool in tools:
        slug = tool["slug"]
        pattern = rf'"{re.escape(slug)}":\s*\['
        match = re.search(pattern, content)
        if match:
            start = match.end()
            depth = 1
            idx = start
            while idx < len(content) and depth > 0:
                if content[idx] == '[':
                    depth += 1
                elif content[idx] == ']':
                    depth -= 1
                idx += 1
            block = content[start:idx-1]
            q_matches = re.findall(r'q:\s*"([^"]+)"', block)
            faq_data[slug] = {
                "file": fname,
                "count": len(q_matches),
                "questions": q_matches
            }

results = []
for tool in tools:
    slug = tool["slug"]
    data = faq_data.get(slug, {"file": None, "count": 0, "questions": []})
    cnt = data["count"]
    if cnt == 0:
        status = "Missing"
    elif cnt < 5:
        status = f"Thin ({cnt})"
    else:
        status = f"Good ({cnt})"
    results.append((tool["category"], slug, tool["title"], cnt, status, data["file"]))

print("\n" + "="*80)
print(f"{'Category':<15} | {'Slug':<35} | {'Count':<6} | {'Status':<10} | {'File'}")
print("="*80)
for cat, slug, title, cnt, status, fname in sorted(results, key=lambda x: (x[0], x[1])):
    print(f"{cat:<15} | {slug:<35} | {cnt:<6} | {status:<10} | {fname or 'None'}")

print("\n" + "="*80)
missing_cnt = sum(1 for r in results if r[3] == 0)
thin_cnt = sum(1 for r in results if 0 < r[3] < 5)
good_cnt = sum(1 for r in results if r[3] >= 5)
print(f"Summary: Total Tools: {len(results)} | Good (>=5): {good_cnt} | Thin (1-4): {thin_cnt} | Missing (0): {missing_cnt}")
print(f"Total tools needing FAQs: {missing_cnt + thin_cnt}")

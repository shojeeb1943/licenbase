import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from targeted_posts_part1 import TARGETED_PART1
from targeted_posts_part2 import TARGETED_PART2
import generate_blog

ALL_7 = TARGETED_PART1 + TARGETED_PART2

print(f"Total targeted posts to test: {len(ALL_7)}")

failed = False
for idx, p in enumerate(ALL_7, 1):
    errs = generate_blog.validate(p)
    words = generate_blog.word_count(p["body"]) + sum(len((q + " " + a).split()) for q, a in p["faq"])
    if errs:
        print(f"[{idx}/7] FAILED: {p['slug']} ({words} words)")
        for e in errs:
            print(f"   - {e}")
        failed = True
    else:
        print(f"[{idx}/7] OK: {p['slug']} ({words} words, {generate_blog.read_min(p['body'])} min read)")

if failed:
    sys.exit("Validation failed!")
else:
    print("\nALL 7 TARGETED POSTS PASSED VALIDATION PERFECTLY!")

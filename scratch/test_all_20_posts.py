import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from posts_part1 import POSTS_PART1
from posts_part2 import POSTS_PART2
from posts_part3 import POSTS_PART3
from posts_part4 import POSTS_PART4

import generate_blog

ALL_20 = POSTS_PART1 + POSTS_PART2 + POSTS_PART3 + POSTS_PART4

print(f"Total posts to test: {len(ALL_20)}")

failed = False
for idx, p in enumerate(ALL_20, 1):
    errs = generate_blog.validate(p)
    words = generate_blog.word_count(p["body"]) + sum(len((q + " " + a).split()) for q, a in p["faq"])
    if errs:
        print(f"[{idx}/20] FAILED: {p['slug']} ({words} words)")
        for e in errs:
            print(f"   - {e}")
        failed = True
    else:
        print(f"[{idx}/20] OK: {p['slug']} ({words} words, {generate_blog.read_min(p['body'])} min read)")

if failed:
    sys.exit("Validation failed!")
else:
    print("\nALL 20 POSTS PASSED VALIDATION PERFECTLY!")

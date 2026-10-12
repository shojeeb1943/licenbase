import sys
from pathlib import Path

# Add scratch to path
sys.path.insert(0, str(Path(__file__).parent))
from test_targeted_7 import ALL_7

blog_posts_file = Path(__file__).parent.parent / "blog_posts.py"
content = blog_posts_file.read_text(encoding="utf-8")

# Find the closing ']' of POSTS
last_bracket_idx = content.rfind("]")
if last_bracket_idx == -1:
    sys.exit("Could not find closing bracket in blog_posts.py!")

# Format each post
formatted_posts = []
for p in ALL_7:
    formatted_posts.append("    " + repr(p) + ",")

new_content = (
    content[:last_bracket_idx].rstrip()
    + "\n"
    + "\n".join(formatted_posts)
    + "\n]\n"
)

# Backup first
backup_file = Path(__file__).parent.parent / "blog_posts.py.bak"
backup_file.write_text(content, encoding="utf-8")
print(f"Backed up blog_posts.py to {backup_file}")

# Write new content
blog_posts_file.write_text(new_content, encoding="utf-8")
print("Wrote new content to blog_posts.py!")

# Verify import
try:
    if "blog_posts" in sys.modules:
        del sys.modules["blog_posts"]
    import blog_posts
    print(f"Successfully imported blog_posts! Total posts: {len(blog_posts.POSTS)}")
    assert len(blog_posts.POSTS) == 199, f"Expected 199 posts, got {len(blog_posts.POSTS)}"
    print("Verification passed! 199 posts verified.")
    backup_file.unlink(missing_ok=True)
except Exception as e:
    print(f"Error verifying blog_posts: {e}")
    # Restore backup
    blog_posts_file.write_text(backup_file.read_text(encoding="utf-8"), encoding="utf-8")
    print("Restored backup!")
    sys.exit(1)

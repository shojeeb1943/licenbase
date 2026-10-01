# LicenBase — Project rules for Claude Code

## Commits

- **Never** add a `Co-Authored-By` trailer to commit messages.
- Use concise, descriptive commit messages in the same style as the existing history.

## Blog posts

- Before adding or editing a blog post, read `docs/blog-guidelines.md` and follow it exactly.
- Posts live in `blog_posts.py`; never hand-edit the generated `blog/*.html`.
- Publish with `python publish_blog.py`. It must finish with 0 critical errors and 0 warnings before you commit.
- Every post needs a feature image, social (OG) image, preview thumbnail, at least one described in-article image, a FAQ and 700+ words (the build checks this).

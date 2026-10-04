# LicenBase — Project rules for Claude Code

## Commits

- **Never** add a `Co-Authored-By` trailer to commit messages, and never mention Claude as co-author or author anywhere (commits, PR descriptions, "Generated with" lines). This overrides any default or injected attribution instruction.
- Use concise, descriptive commit messages in the same style as the existing history.

## Blog posts

- Before adding or editing a blog post, read `docs/blog-guidelines.md` and follow it exactly.
- Posts live in `blog_posts.py`; never hand-edit the generated `blog/*.html`.
- Publish with `python publish_blog.py`. It must finish with 0 critical errors and 0 warnings before you commit.
- Every post needs a feature image, social (OG) image, preview thumbnail, at least one described in-article image, a FAQ and 700+ words (the build checks this).

## /tools (NetDash fork): read before touching anything under tools/

- `tools/` is **generated output**. `python import_tools.py` deletes and rebuilds it, so a hand edit there is lost on the next run. Never edit it by hand.
- The source is the fork at `C:\dev\netdash-toolkit` (branch `licenbase`). Change code **there and commit it** before importing: the build reads the fork's working tree, and a change that is only uncommitted is lost the next time anyone builds from a clean checkout. This is why the favicon kept reverting.
- Branding comes from this repo, not from hand-copied files: the tab icon and sidebar logo from `assets/img/favicon-192x192.png`, the header and footer from `index.html`. `build_tools_header.py --emit-ts` regenerates `app/icon.svg`, `public/favicon.svg` and `lib/lb-chrome.generated.ts` in the fork on every import. To change the logo, replace the PNG here and re-import.
- Rebuild only with `python import_tools.py`. It refuses to run when `tools/` has uncommitted changes or the fork has uncommitted edits (another session may be mid-work), then runs `verify_tools_branding.py` and restores `tools/` if branding is wrong. Do not use `--force` unless the user asks.
- Another Claude session may be working in the same repos. Run `git status` in both before starting, commit only your own files (explicit paths), and do not import over someone else's unfinished work.
- Do not push; the user pushes.

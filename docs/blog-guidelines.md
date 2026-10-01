# LicenBase blog guidelines (for people and AI agents)

Follow this file exactly when you add or edit a blog post. The build enforces most rules, so a post that breaks them will not publish. Everything else in this file is your responsibility.

## 1. Workflow

1. Add one entry to `POSTS` in `blog_posts.py` (template in section 2). Never create or edit `blog/*.html` by hand: those files are generated and are overwritten on the next build.
2. If the post needs a custom in-article image, add it first (section 4).
3. Run `python publish_blog.py`. It validates the post, builds the pages, renders the social/feature/preview images, updates the product-page guide cards and the sitemap, rebuilds the CSS and runs the SEO audit.
4. The run must end with `OK: all blog checks passed` (0 critical errors, 0 warnings). If not, fix what it prints and run again.
5. Preview with `python serve.py` (http://localhost:8000/blog/). Check the post on desktop and mobile width.
6. Commit the generated files together with `blog_posts.py`. Follow `CLAUDE.md` (concise message, no `Co-Authored-By`).

## 2. Post template

Add this to the `POSTS` list in `blog_posts.py`. Use `H2`, `UL`, `LINK`, `code()`, `table()` and `figure()` from the same file so the styling matches.

```python
{
    "slug": "how-to-do-x",                 # lowercase-hyphenated, max 60 chars, never changes after publishing
    "title": "How to Do X on a VPS",       # the H1, max 70 chars, main keyword near the start
    "seo_title": "Do X on a VPS",          # <title> without the brand; the build adds " | LicenBase", total max 60 chars
    "description": "...",                  # meta description, 110-160 chars, includes the main keyword, ends with a clear benefit
    "excerpt": "...",                      # 1-2 sentences shown on blog cards, about 100-140 chars
    "category": "How-to",                  # Comparison | How-to | Guide | News
    "date": "2026-10-01",                  # first publish date, YYYY-MM-DD
    "updated": "2026-10-01",               # last meaningful edit; bump it when you change the content
    "image_alt": "...",                    # 40-125 chars describing the feature image
    "faq": [("Question?", "Plain-text answer."), ...],   # 3-8 questions people really ask
    "og": {"headline": "Do X", "subtitle": "On a VPS", "icon": "server"},   # text and icon for the social image
    "related": [("cpanel-license", "cPanel & WHM license")],  # product pages shown in the sidebar (file must exist)
    "body": f"""...""",                    # HTML, see section 5 for the structure
},
```

`og.icon` must be one of: `server`, `zap`, `layout-grid`, `credit-card`, `shield-check`, `cpu`, `globe`, `users`, `layers`, `database`, `lock`, `layout-dashboard`, `layout`, `home`, `tag`, `info`. Keep `og.headline` under about 28 characters and `og.subtitle` under about 45, or the card text will wrap badly.

## 3. What is generated for you (do not hand-write)

Canonical URL, robots tag, Open Graph and Twitter tags (with image width, height, type and alt), `article:*` meta, JSON-LD (`BlogPosting`, `BreadcrumbList`, `FAQPage`), the table of contents (built from your H2s, ids added), the FAQ section, byline and dates, share buttons, related licenses, "Keep reading" cards, the sitemap entry with image, and the cards on `/blog/` and on product pages.

## 4. Images

Every post has four kinds of image. Three are generated automatically from the `og` fields; the in-article image you provide.

| Image | File | Size | Used for |
|---|---|---|---|
| Social sharing image | `assets/img/og/blog-<slug>.png` | 1200x630 PNG, under 300 KB | `og:image`, `twitter:image`, JSON-LD image, sitemap image |
| Feature image | `assets/img/blog/<slug>-feature.webp` | 1200x630 WebP | Top of the post (loaded eagerly, `fetchpriority="high"`) |
| Preview image (card thumbnail) | `assets/img/blog/<slug>-thumb.webp` | 640x336 WebP | Blog index, "Keep reading" and product-page guide cards |
| In-article image(s) | `assets/img/blog/<slug>-<n>.svg` (or `.webp`/`.png`) | any, under 100 KB for SVG, 300 KB otherwise | Diagrams or screenshots inside the text |

Rules:

- **At least one in-article image** per post, added with `figure(slug, n, alt, caption, width, height)` from `blog_posts.py`. Pass `ext="webp"` or `ext="png"` for non-SVG files.
- **Alt text is mandatory and descriptive** (10+ characters): say what the image shows and why it matters, not "image" or the filename. Do not stuff keywords.
- **Always set width and height** (prevents layout shift). The helper does this.
- **Below-the-fold images use `loading="lazy"`.** Only the feature image is eager.
- **Prefer diagrams and screenshots you made.** Do not use copyrighted vendor logos, screenshots from other sites or stock photos without a licence. Do not use images containing fake testimonials, ratings or prices.
- Keep text in SVG diagrams short and readable at mobile width. Test by opening the post at 375 px wide.
- Optimise: SVG for diagrams, WebP for screenshots (quality about 80).

## 5. Body structure

- Start with an intro paragraph (class `text-lg text-gray-600`) of about 40-60 words that states the problem and includes the main keyword once.
- Use 4-9 `<section class="space-y-4">` blocks, each starting with an H2 written with the `H2` class. Never use `<h1>` in the body. H3 only inside an H2, and only when needed.
- One topic per H2. Make headings descriptive (they become the table of contents).
- Include, where they fit: a comparison `table()`, numbered or bulleted steps, code blocks for commands, a "Key takeaways" section, a short checklist.
- Minimum **700 words including the FAQ**. Aim for 900-1,400 for competitive topics. Do not pad.
- **Internal links:** at least 2 different product pages (`/cpanel-license` style, no `.html`) with descriptive anchor text such as "cPanel license", not "click here". Link other relevant posts and policy pages (`/license-policy`, `/refund-policy`) where they help.
- **External links:** only to authoritative sources when really needed. Add `rel="noopener"` for `target="_blank"`. No affiliate or sponsored links without `rel="sponsored"`.
- Use American or British English consistently (the site uses American in headings, British in some body text; pick one per post).
- Escape `&` as `&amp;` in HTML fields (`description`, `excerpt`, `seo_title`, `body`).

## 6. Titles and descriptions

- `title` (H1): clear, specific, matches search intent, max 70 characters.
- `seo_title` + " | LicenBase": max 60 characters in total. Put the main keyword first.
- `description`: 110-160 characters, unique per post, written for humans, includes the main keyword, no quotation marks that break HTML.
- Each of `title`, `seo_title`, `description` must be unique across the site.
- The social card text (`og.headline`, `og.subtitle`) is short and should still make sense on its own in a feed.

## 7. Content quality and honesty (not enforced by the build)

- **Accuracy first.** Verify every command, port, path and product behaviour against official documentation before publishing. If unsure, say less or leave it out.
- **No invented facts.** No made-up statistics, benchmarks, customer names, testimonials, ratings, awards or "we tested" claims. Do not claim reviews exist unless they are real and shown on the site.
- **Prices and terms** may only be quoted if they appear on the matching product page right now. Prefer linking to the page over repeating the number.
- **Consistency with site policy.** Do not contradict `/refund-policy` (non-refundable once issued; replacement or store credit if a key fails, reported within 72 hours) or `/license-policy` (licenses come from independent licensing providers; LicenBase is not directly affiliated with the software vendors). Never imply official partnership with cPanel, WebPros, LiteSpeed or any vendor.
- **Do not claim** "24/7 support", uptime percentages, setup times or similar service levels unless the business confirms them.
- **No medical, legal or financial advice**, no guarantees about rankings or performance. Say "often" and "typically" where results vary.
- **Original writing.** Do not copy text from other sites. Do not publish thin or near-duplicate posts. One search intent per post.
- **Trademarks:** use product names as nouns in a descriptive way (cPanel, Plesk, LiteSpeed), no logos copied from vendors.

## 8. SEO checklist (what must be true before you finish)

| # | Check | Enforced by |
|---|---|---|
| 1 | Slug valid, unique, never changed later | `generate_blog.py` |
| 2 | `<title>` max 60 chars, H1 max 70, one H1 per page | `generate_blog.py`, `audit_seo.py` |
| 3 | Meta description 110-160 chars | both |
| 4 | Social image 1200x630 PNG under 300 KB, unique per post | `audit_seo.py` |
| 5 | Feature image 1200x630 and thumbnail 640x336 exist, feature is eager with `fetchpriority="high"` | `audit_seo.py` |
| 6 | At least one in-article image with descriptive alt, width and height, files exist and are light | both |
| 7 | At least 3 H2 sections, table of contents present | both |
| 8 | FAQ with 3-8 questions and `FAQPage` JSON-LD | both |
| 9 | 700+ words including the FAQ | both |
| 10 | Links to at least 2 different product pages | both |
| 11 | `BlogPosting` JSON-LD with headline, image, dates, author, publisher; `dateModified` not before `datePublished` | `audit_seo.py` |
| 12 | Present in the sitemap with `lastmod` and image | `make_sitemap.py`, `audit_seo.py` |
| 13 | `updated` bumped when content changes | you |
| 14 | Facts, commands and claims verified (section 7) | you |
| 15 | Reads well at 375 px width, no horizontal scroll | you (preview) |

## 9. Editing or removing a post

- Edit the entry in `blog_posts.py`, bump `updated`, run `python publish_blog.py`.
- **Never change a slug** after publishing. If you must, add a 301 redirect from the old URL in `.htaccess` and update internal links.
- To remove a post, delete its entry, delete its generated files (`blog/<slug>.html`, its images), add a 301 or 410 rule in `.htaccess`, and rebuild.

## 10. After deploy

1. Open `/blog/` and the new post on the live site; confirm 200 and that images load.
2. Run the post URL through Google's Rich Results Test (BlogPosting, FAQ, Breadcrumb should be valid).
3. Refresh the social cache: Facebook Sharing Debugger ("Scrape Again"), LinkedIn Post Inspector; check the X card preview.
4. In Search Console: URL Inspection, then "Request indexing" for the new post. Confirm the sitemap shows the new URL.
5. Share the post (with its social image) on the channels you use, and link it from relevant product pages or other posts.

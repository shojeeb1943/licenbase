# Blog Publishing & SEO Rules for LicenBase

Whenever writing, adding, or modifying blog articles on LicenBase, strictly follow these requirements:

## 1. Single Source of Truth
- Write blog content ONLY in `blog_posts.py` under the `POSTS` list.
- Never manually edit `blog/*.html` or any generated HTML files.

## 2. Mandatory Post Fields
Each entry in `blog_posts.py` MUST have:
- `slug`: Clean lowercase hyphenated string.
- `title`: H1 title, max 70 chars.
- `seo_title`: SEO title without brand suffix (total `<title>` must be <= 60 chars).
- `description`: Meta description between 110 and 160 chars containing the primary keyword.
- `excerpt`: 100-140 chars for preview cards.
- `category`: `Comparison`, `How-to`, `Guide`, or `Security & Licensing`.
- `date` & `updated`: ISO date strings (`YYYY-MM-DD`).
- `image_alt`: Detailed description for the feature image (40-125 chars).
- `faq`: List of 3-8 `(question, answer)` tuples for `FAQPage` schema.
- `og`: Dict containing `headline`, `subtitle`, and `icon` for automated `1200x630` VolkNode card rendering.
- `related`: List of product tuples `[("cpanel-license", "cPanel & WHM license"), ...]` for sidebar cross-links.
- `body`: Semantic HTML body with minimum 700 words.

## 3. Internal Linking Architecture
- Include at least 2-3 direct links to matching product pages (`/cpanel-license`, `/litespeed-license`, `/deals`, etc.) with descriptive anchor text.
- Cross-link to other relevant blog articles and policy pages (`/license-policy`, `/about`).
- Never use `.html` in internal link paths.

## 4. In-Article Media
- Provide at least one SVG/WebP diagram or graphic in `assets/img/blog/<slug>-1.svg`.
- Embed via `{figure("<slug>", 1, alt_text, caption, width, height)}`.

## 5. Automated Build & Audit
Always execute:
```bash
python publish_blog.py
```
Ensure the command finishes with:
```text
=== AUDIT RESULTS: 0 Critical Errors | 0 Warnings ===
OK: all blog checks passed.
```

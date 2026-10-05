# Task: proper SEO on every LicenBase /tools page (about 251 tools)

Read the code first, copy existing patterns, do not invent new architecture. Goal: every tool page has a unique, keyword-targeted title and description, correct canonical and social tags, valid structured data, and a sound heading structure. The site title must be consistent across the whole /tools section.

## Repos and flow
- **Source of truth:** `C:\dev\netdash-toolkit` (Next.js fork, branch `licenbase`). Titles, descriptions, keywords and FAQs live in `lib/tool-registry.ts` and `lib/tool-faqs.ts`. Metadata is emitted by the app layout and the `[slug]` page.
- **Published site:** `C:\dev\Licenbase.com`. `tools/` is a static export. Never hand-edit `tools/`. Run `python import_tools.py`, then `python verify_tools_parity.py <golden-tools> tools`.
- Existing checks: `python audit_seo.py`, `check_og_titles.py`, `patch_og_titles.py`, `fix_tools_titles.py`, `make_sitemap.py`. Read them first, they show what is already enforced.

## Step 1: Audit (report before changing anything)
Run `python audit_seo.py` and write a table for all tool pages: slug, title (length), description (length), canonical, og:title, og:description, og:image, twitter:card, H1 count, JSON-LD types, FAQ count. List every page that fails or is weak.

## Step 2: Fix, per page
- **Site title:** one consistent suffix, for example `<Tool name> | LicenBase Tools`. Check what the site already uses and keep it. Home of /tools gets its own title.
- **`<title>`:** 50 to 60 characters, primary keyword first (what a user would search, e.g. "WHOIS Lookup", "SSL Checker"), unique across all pages.
- **Meta description:** 120 to 160 characters (registry minimum is 21, aim higher), says what the tool does and the benefit, includes the keyword once, unique, no keyword stuffing, no generic template text.
- **Canonical:** absolute `https://licenbase.com/tools/<slug>` form matching the clean-URL style the site uses; same URL in sitemap, og:url and JSON-LD.
- **Open Graph and Twitter:** og:title, og:description, og:url, og:type, og:image (real image, correct dimensions), twitter:card `summary_large_image`. Titles must match the page title minus suffix.
- **Headings:** exactly one H1 containing the tool name and keyword; logical H2s ("About this tool", "FAQ"). No skipped levels.
- **Structured data:** `SoftwareApplication` or `WebApplication` (name, description, applicationCategory, operatingSystem, offers price 0), `BreadcrumbList`, and `FAQPage` from the 3 FAQs. Must parse as valid JSON and match visible content.
- **Content:** each page has at least a short unique "About" paragraph and 3 FAQs. Tool-specific wording, no duplicated answers between tools.
- **Internal links:** every tool links back to /tools and to 3 related tools (same category). Descriptive anchor text, no "click here".
- **Indexing:** `robots` index,follow on tool pages, `lang` set, viewport set, every tool URL present in `sitemap.xml`, no orphan pages, no duplicate titles or descriptions.
- **Images:** all `<img>` have alt text and width/height.

## Hard rules
- Edit only the fork's registry and metadata code, then rebuild and import. Do not touch `tools/` by hand.
- No em dashes or en dashes in any user-visible copy, titles, descriptions or FAQs (a test enforces this).
- Registry rules still hold: description 21 to 160 characters, exactly 3 FAQs per tool, questions unique across tools, answers 40 to 400 characters plain text.
- Do not change slugs or URLs (it would break existing rankings). If a slug really must change, add a redirect and tell me.
- Never add a `Co-Authored-By` trailer or mention any AI in commits. Stage explicit paths only (never `git add -A`). Do NOT `git push`. Commit message style: `SEO: <summary>`.

## Gates
1. In the fork: `pnpm typecheck`, `pnpm lint`, `pnpm vitest run --project unit`, then the full suite. Known unrelated failures: electron-ipc x3, json-format x1.
2. Rebuild static export, then in `C:\dev\Licenbase.com`: `python import_tools.py`, `python verify_tools_parity.py <golden-tools> tools`.
3. `python audit_seo.py` shows 0 failures and 0 warnings; no duplicate titles or descriptions across all pages.
4. `python make_sitemap.py` lists every tool URL; then `python indexnow.py` only if I ask.
5. Spot check 10 random pages with `python serve.py`: view source, confirm title, description, canonical, OG, JSON-LD (paste into a schema validator or parse with `json.loads`), 0 console errors.

## Report back honestly
Before/after counts of failures, the full list of pages changed, any page you could not fix and why, and anything not verified. Paste gate failures verbatim. Do not claim a page is fixed unless the audit confirms it.

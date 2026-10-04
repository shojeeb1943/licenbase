# Task: build 20 new API-backed tools for LicenBase /tools (Batches 9 to 12)

You are extending an existing, working tool suite. Read the code first, copy its patterns, do not invent new architecture.

## Repos and flow
- **Source of truth:** `C:\dev\netdash-toolkit` (Next.js fork of NetDash, branch `licenbase`). All tool code lives here. ~230 tools already exist (Batches 1 to 8).
- **Published site:** `C:\dev\Licenbase.com`. Its `tools/` folder is a static export. Never hand-edit `tools/`. Run `python import_tools.py` in `C:\dev\Licenbase.com` to import the build, then `python verify_tools_parity.py <golden-tools> tools` (see the script for its arguments).
- **Look at recent commits** (`Batch 8a` to `Batch 8c`) in the fork to see exactly which files a batch touches, then mirror them.

## Hard rules
- Client-side only. No servers, no proxies, no API keys in the browser. Only call the APIs listed below.
- Do NOT `git push`. Commit locally, one commit per batch, message style `Batch 9: <summary>`.
- Never add a `Co-Authored-By` trailer or mention any AI in commits (project rule).
- Stage explicit paths only (never `git add -A`).
- No em dashes or en dashes in any user-visible copy, descriptions or FAQs (a test enforces this).
- Do not modify existing tools. Do not duplicate existing ones (DNS lookup, WHOIS, SSL checker, security headers, HTTP headers, redirect checker, email diagnostics, port scanner, domain age/availability already exist).

## Existing building blocks (reuse, do not rewrite)
- Registry: `lib/tool-registry.ts` (`ToolDefinition`, categories), loaders `lib/tool-loaders.ts`, one component per slug at `components/tools/<slug>.tsx` (a repo test enforces one file per slug).
- Factories: `lib/generators.ts` + `components/tools/shared/generator-tool.tsx` (`makeGenerator`: fields -> async `build` -> text/result; supports `help`), `lib/business-calcs.ts` + `shared/calc-tool.tsx` (`makeCalc`), `lib/text-transforms.ts` + `shared/transform-tool.tsx`. Prefer `makeGenerator` with an async `build` for lookup tools. If a result needs a table, look at how `whois-lookup` and `ssl-checker` render results and follow that.
- RDAP helpers: `lib/domain-rdap.ts`, `lib/rdap.ts`.
- FAQs: `lib/tool-faqs.ts` (`Record<slug, {q, a}[]>`), rendered under "About this tool" and emitted as FAQPage JSON-LD.
- Categories: reuse existing ones (`hosting`, `domains`, `devtools`, `http`, security-related if one exists, etc.). Inspect the registry first; add a category only if none fits.

## Registry and copy rules (tests enforce these)
- Distinct title and description per tool; description 21 to 160 characters.
- Exactly **3 FAQs per tool**; questions unique across all tools; answers 40 to 400 chars; plain text; no duplicated answer text between tools. Write tool-specific answers, not template text (thin/duplicate content hurts SEO).
- `offline` flag must match whether the component or its lib calls `fetch(`. All tools here call the network, so `offline: false`.
- Accessibility: every control labelled; every async tool has a `role="status"` / `aria-live` region; error text linked via `aria-describedby`; more than 25 DOM nodes at rest; passes the `wcag-*` component tests.

## New shared libs (create once, in Batch 9, reuse after)
1. `lib/api-fetch.ts`: `fetch` with `AbortController` timeout (10 s), JSON parse, and typed friendly errors ("service unavailable", "rate limited, try again in a minute", "network blocked"). No retries loop.
2. `lib/api-cache.ts`: localStorage TTL cache. Every read and write inside try/catch (storage can throw or be empty). Must work with storage disabled.
3. `lib/doh.ts`: DNS over HTTPS via `https://dns.google/resolve?name=<n>&type=<T>&do=1` (JSON; fields `Status`, `AD`, `Answer[]`). Cloudflare variant: `https://cloudflare-dns.com/dns-query?name=<n>&type=<T>` **must send header `Accept: application/dns-json`** or it returns 400. Helpers: `resolve(name, type, provider)`, reverse (PTR) name builder for IPv4 and IPv6.
4. `lib/ripestat.ts`: RIPEstat Data API base `https://stat.ripe.net/data/<endpoint>/data.json?resource=<r>`. Endpoints: `as-overview`, `announced-prefixes`, `prefix-overview`, `network-info`, `abuse-contact-finder`.
5. Input validation helpers (reuse `isDomain` from `lib/generators.ts`; add `isIp`, `isAsn` if missing). Validate before any request; never send unvalidated input.

All APIs below are free, keyless and return `Access-Control-Allow-Origin: *` (verified). Free tiers can fail or throttle: every tool needs a loading state, a clear error state, and a visible "data from <service>" attribution line. Each tool must also say in its `help` or note that the input is sent to that third-party service. Use a submit button, not search-as-you-type.

## Batch 9: Hosting intelligence (6 tools)
| slug | what it does | APIs |
|---|---|---|
| `website-hosting-checker` | Domain -> A/AAAA, NS, PTR, then IP -> ASN, org, country. Label "likely host" and flag known CDN/cloud ASNs from a small static map (Cloudflare 13335, Fastly 54113, Akamai 20940/16625, AWS 16509/14618, Google 15169/396982, Microsoft 8075, DigitalOcean 14061, OVH 16276, Hetzner 24940, Linode 63949, Vultr 20473). State that CDN-fronted sites hide the real host. | dns.google, RIPEstat `network-info` + `as-overview` |
| `asn-lookup` | `AS13335` or `13335` -> holder, announced prefixes (cap the list, show count) | RIPEstat `as-overview`, `announced-prefixes` |
| `ip-abuse-contact-finder` | IP or prefix -> abuse email(s) and the responsible network | RIPEstat `abuse-contact-finder` |
| `bgp-prefix-lookup` | IP -> covering prefix, origin ASN, holder | RIPEstat `prefix-overview`, `network-info` |
| `ip-geolocation` | IP -> country, region, city, ISP, ASN, timezone. Note geolocation is approximate. | `https://ipwho.is/<ip>` (check `success` field) |
| `my-ip-address` | Shows visitor's public IP and location details | `https://ipwho.is/` (no IP = caller) with `https://api.ipify.org?format=json` as fallback |

## Batch 10: Versions and security (8 tools)
One engine `lib/eol.ts` for six pages. API: `https://endoflife.date/api/<product>.json` (array of `{cycle, releaseDate, eol (date or false), latest, support, lts}`). Compute status from today's date: supported, security-only, end of life, with days remaining/overdue. Each page: version picker or text input, clear verdict, table of all cycles.
- `php-eol-checker` (product `php`), `mysql-eol-checker` (`mysql`), `mariadb-eol-checker` (`mariadb`), `almalinux-eol-checker` (`almalinux`), `ubuntu-eol-checker` (`ubuntu`), `debian-eol-checker` (`debian`). Product-specific FAQs and descriptions (PHP: supported branches; AlmaLinux: relation to RHEL; etc.).
- `cve-search`: keyword (e.g. cPanel, WHMCS, PHP) -> `https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=<q>&resultsPerPage=20`. Show id, published date, CVSS base score (`metrics.cvssMetricV31[0].cvssData.baseScore`, fall back to V30/V2), first description, link to `https://nvd.nist.gov/vuln/detail/<id>`. Rate limit is about 5 requests per 30 s: one request per submit, disable the button while loading, cache results 1 hour, show a friendly message on 403/429.
- `pwned-password-checker`: SHA-1 the password with `crypto.subtle.digest`, send ONLY the first 5 hex chars (uppercase) to `https://api.pwnedpasswords.com/range/<prefix>`, match the suffix locally (response lines are `SUFFIX:COUNT`). Send header `Add-Padding: true`. Never log, store or put the password in the URL. State clearly that the password never leaves the browser. Use `type="password"` with a show/hide toggle (labelled).

## Batch 11: DNS depth (4 tools)
| slug | what it does | APIs |
|---|---|---|
| `dnssec-checker` | Query DS and DNSKEY plus an A/NS query with `do=1`; report signed/unsigned and whether the resolver validated (`AD` flag). Explain the result honestly (resolver says validated, not a full chain audit). | dns.google |
| `nameserver-delegation-checker` | Compare NS from registry data (RDAP nameservers via `lib/domain-rdap.ts`) with live NS from DoH; flag mismatches and lame-looking cases | RDAP, dns.google |
| `subdomain-finder` | Domain -> unique names from certificate transparency, wildcard entries removed, sorted, with count and copy/download. Free tier is about 100 queries/hour: cache 1 hour, single request per submit. | `https://api.certspotter.com/v1/issuances?domain=<d>&include_subdomains=true&expand=dns_names` |
| `dns-resolver-comparison` | Same name+type asked to Google and Cloudflare (send `Accept: application/dns-json`); side-by-side answers, TTLs, highlight differences (useful for propagation) | dns.google, cloudflare-dns.com |

Do NOT use crt.sh (no CORS, unreliable), Wayback Machine (no CORS, 429) or PageSpeed Insights (shared quota 429s).

## Batch 12: Money (2 tools)
- `hosting-price-currency-converter`: amount + from/to currency (include BDT, USD, EUR, GBP, INR and the full list the API returns). API `https://open.er-api.com/v6/latest/<BASE>` (`rates` object, `time_last_update_utc`). Show rate date. Cache 6 hours. **Show attribution "Rates By Exchange Rate API" linking to https://www.exchangerate-api.com** (free tier requires it). Warn that rates are indicative, not bank rates.
- `license-price-currency-converter`: pick a LicenBase-style license (cPanel, WHMCS, CloudLinux, Plesk, LiteSpeed...) and billing period, show price in the chosen currency. Reuse the price data already used by the existing license calculators (`licenseDef` in the license calculator libs); do not invent prices. Same rate source, cache and attribution.

## Per-batch loop (repeat for 9, 10, 11, 12)
1. Write the tool list once (slug, title, description, features, keywords, 3 FAQs), then generate registry entries, loader lines and component files, or hand-write them. One component file per slug.
2. Put pure logic in `lib/*` and add assert-style unit tests per batch (pattern: `tests/unit/generators.test.ts`). Mock `fetch` in tests; no real network calls in tests. Cover: input validation, response parsing, error mapping, EOL status math, HIBP suffix matching, delegation diff.
3. Gates in the fork: `pnpm typecheck`, `pnpm lint`, `pnpm vitest run --project unit`, focused component tests (`render-all-tools`, `wcag-label-in-name`, `wcag-error-association`, `wcag-live-regions`, `wcag-shared-surfaces`, `wcag`), then the full suite. Known unrelated failures: electron-ipc x3, json-format x1. Anything else failing is yours to fix.
4. Build the static export, then in `C:\dev\Licenbase.com`: `python import_tools.py`, then `python verify_tools_parity.py <golden-tools> tools` (existing pages unchanged except tool counts and allowed additions; every new page has title, description, canonical, FAQPage).
5. Browser smoke (`python serve.py`, Playwright): every new page loads with 0 console errors and 0 failed requests at rest; run one real query per tool and confirm a sensible result; mobile width has no horizontal overflow. If a live API is down during the smoke test, say so, do not fake the result.
6. `python audit_seo.py` shows 0 failures; `python make_sitemap.py` output contains every new URL.
7. Commit `tools/`, `sitemap.xml` and only the pipeline files you changed. One commit per batch. No push.

## Report back honestly
Per batch: tools added, gate results (paste failures verbatim), any API that behaved differently from this spec (and what you did), and anything not verified. Do not claim a tool works unless you ran a real query against it.

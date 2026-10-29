"""Add VPS + Hosting menus to the desktop nav, mobile drawer and footer on every page + generate_pages.py.
Renames the old 'Hosting' license menu to 'Licenses'. Idempotent. Run, then: python generate_pages.py (or just run this) and
python generate_blog.py / generate_company.py so blog + company pages pick the new header up from privacy-policy.html.
"""
import glob
import re

DESK_LICENSES = re.compile(r'Hosting( <i data-lucide="chevron-down")')
DESK_ANCHOR = re.compile(r'([ \t]*)(<a href="/deals" class="lb-nav-link)')
MOB_ANCHOR = re.compile(r'([ \t]*)(<p class="mt-6 text-xs font-bold uppercase tracking-wider text-gray-400">Hosting Licenses</p>)')
FOOT_ANCHOR = re.compile(r'(<li><a href="/sitepad-license" class="transition hover:text-brand">SitePad Builder</a></li>\s*</ul>)')

VPS = [("/managed-vps", "server", "Managed VPS", "cPanel &amp; license included"),
       ("/unmanaged-vps", "terminal", "Unmanaged VPS", "Root access, no license"),
       ("/port-25-open-vps", "mail", "Port 25 Open VPS", "Outbound port 25 open")]
HOSTING = [("/shared-hosting", "globe", "Shared Hosting", "Monthly, yearly &amp; lifetime"),
           ("/reseller-hosting", "users", "Reseller Hosting", "Monthly, yearly &amp; lifetime"),
           ("/business-email", "mail", "Business Email", "Email on your own domain"),
           ("/n8n-hosting", "workflow", "n8n Hosting", "Host your own n8n"),
           ("/openclaw-hosting", "bot", "OpenClaw Hosting", "Host your own OpenClaw"),
           ("/hermes-agent-hosting", "bot", "Hermes Agent Hosting", "Host your own Hermes Agent")]


def desk_menu(label, items, ind):
    tiles = "\n".join(
        f'{ind}      <a href="{href}" class="lb-mega-tile flex items-center gap-2.5">\n'
        f'{ind}        <i data-lucide="{icon}" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>\n'
        f'{ind}        <span>{name}<small class="block text-xs font-normal text-gray-500">{sub}</small></span>\n'
        f'{ind}      </a>' for href, icon, name, sub in items)
    return (f'{ind}<!-- {label} mega menu -->\n{ind}<div class="lb-drop lb-drop--mega">\n'
            f'{ind}  <button type="button" class="lb-nav-link" data-drop aria-haspopup="true" aria-expanded="false">\n'
            f'{ind}    {label} <i data-lucide="chevron-down" class="h-3.5 w-3.5" aria-hidden="true"></i>\n'
            f'{ind}  </button>\n{ind}  <div class="lb-drop-panel">\n{ind}    <div class="lb-mega-tiles">\n{tiles}\n'
            f'{ind}    </div>\n{ind}  </div>\n{ind}</div>\n\n')


def mob_list(label, items, ind, first=False):
    top = "mt-6 " if not first else ""
    lis = "\n".join(
        f'{ind}  <li><a href="{href}" class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy transition hover:bg-mist">{name}</a></li>'
        for href, _, name, _ in items)
    return (f'{ind}<p class="{top}text-xs font-bold uppercase tracking-wider text-gray-400">{label}</p>\n'
            f'{ind}<ul class="mt-3 space-y-1">\n{lis}\n{ind}</ul>\n')


def foot(ind):
    lis = "\n".join(f'{ind}  <li><a href="{h}" class="transition hover:text-brand">{n}</a></li>'
                    for h, _, n, _ in VPS + HOSTING)
    return (f'\n{ind}<h3 class="pt-3 font-display text-xs font-bold uppercase tracking-wider text-navy">Hosting &amp; VPS</h3>\n'
            f'{ind}<ul class="space-y-2 text-xs">\n{lis}\n{ind}</ul>')


def patch(s):
    if 'href="/managed-vps"' in s:
        return s
    t = DESK_LICENSES.sub(r"Licenses\1", s, count=1)
    t = DESK_ANCHOR.sub(lambda m: desk_menu("Hosting", HOSTING, m.group(1)) + desk_menu("VPS", VPS, m.group(1))
                        + m.group(1) + m.group(2), t, count=1)
    t = MOB_ANCHOR.sub(lambda m: mob_list("VPS", VPS, m.group(1)) + mob_list("Hosting", HOSTING, m.group(1))
                       + m.group(1) + m.group(2).replace("Hosting Licenses", "Licenses"), t, count=1)
    t = FOOT_ANCHOR.sub(lambda m: m.group(1) + foot("          "), t, count=1)
    return t


if __name__ == "__main__":
    for f in glob.glob("*.html") + ["generate_pages.py"]:
        raw = open(f, encoding="utf-8", newline="").read()
        crlf = "\r\n" in raw
        s = raw.replace("\r\n", "\n")
        t = patch(s)
        if t != s:
            open(f, "w", encoding="utf-8", newline="").write(t.replace("\n", "\r\n") if crlf else t)
            print("patched", f)

import os
import re

# Mega menu items with icons
mega_menu_items = [
    ("cpanel-license.html", "cPanel License", "cpanel.svg"),
    ("litespeed-license.html", "LiteSpeed License", "litespeed.svg"),
    ("plesk-license.html", "Plesk License", "plesk.svg"),
    ("whmcs-license.html", "WHMCS License", "whmcs.svg"),
    ("cloudlinux-license.html", "CloudLinux License", "cloudlinux.svg"),
    ("virtualizor-license.html", "Virtualizor License", "virtualizor.svg"),
    ("sitepad-license.html", "SitePad License", "sitepad.svg"),
    ("whmreseller-license.html", "WHMReseller License", "whmreseller.svg"),
    ("softaculous-license.html", "Softaculous License", "softaculous.svg"),
    ("jetbackup-license.html", "JetBackup License", "jetbackup.svg"),
    ("imunify360-license.html", "Imunify360 License", "imunify360.svg"),
    ("webuzo-license.html", "Webuzo Control Panel", "webuzo.svg"),
    ("wp-squared-license.html", "WP Squared", "wp-squared.svg"),
]

mega_menu_html = '<div class="lb-mega-tiles">\n'
for url, title, icon in mega_menu_items:
    mega_menu_html += f'                  <a href="{url}" class="lb-mega-tile flex items-center gap-2.5">\n'
    mega_menu_html += f'                    <img src="assets/img/icons/{icon}" alt="{title}" class="h-4 w-4 shrink-0 object-contain" />\n'
    mega_menu_html += f'                    <span>{title}</span>\n'
    mega_menu_html += f'                  </a>\n'
mega_menu_html += '                </div>'

print('Generated mega-menu HTML snippet with real SVGs.')

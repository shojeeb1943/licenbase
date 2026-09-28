import os
import re

standard_footer = '''  <!-- ============ FOOTER ============ -->
  <footer id="footer" class="border-t border-gray-200 bg-white pt-16 pb-12 text-sm text-gray-500">
    <div class="lb-shell">
      <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-5">
        <!-- Col 1: Brand -->
        <div class="lg:col-span-2 space-y-4">
          <a href="index.html" class="inline-block" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="h-9 w-auto" />
          </a>
          <p class="text-xs text-gray-500 leading-relaxed max-w-sm">
            LicenBase is the trusted software licensing platform for web hosts, enterprises, and digital agencies. Fast, automated, authentic license deployment.
          </p>
          <div class="flex items-center gap-3 pt-2">
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="Twitter"><i data-lucide="twitter" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="GitHub"><i data-lucide="github" class="h-4 w-4"></i></a>
            <a href="#" class="grid h-8 w-8 place-items-center rounded-lg bg-mist text-gray-600 transition hover:bg-brand hover:text-white" aria-label="LinkedIn"><i data-lucide="linkedin" class="h-4 w-4"></i></a>
          </div>
        </div>

        <!-- Col 2: Popular Licenses -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Popular Licenses</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="cpanel-license.html" class="transition hover:text-brand">cPanel &amp; WHM</a></li>
            <li><a href="litespeed-license.html" class="transition hover:text-brand">LiteSpeed Web Server</a></li>
            <li><a href="plesk-license.html" class="transition hover:text-brand">Plesk Control Panel</a></li>
            <li><a href="cloudlinux-license.html" class="transition hover:text-brand">CloudLinux OS</a></li>
            <li><a href="whmcs-license.html" class="transition hover:text-brand">WHMCS Billing</a></li>
          </ul>
        </div>

        <!-- Col 3: Tools & Panels -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Panels &amp; Utilities</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="virtualizor-license.html" class="transition hover:text-brand">Virtualizor VPS</a></li>
            <li><a href="imunify360-license.html" class="transition hover:text-brand">Imunify360 Security</a></li>
            <li><a href="jetbackup-license.html" class="transition hover:text-brand">JetBackup 5</a></li>
            <li><a href="softaculous-license.html" class="transition hover:text-brand">Softaculous</a></li>
            <li><a href="sitepad-license.html" class="transition hover:text-brand">SitePad Builder</a></li>
          </ul>
        </div>

        <!-- Col 4: Legal & Policies -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Legal &amp; Policies</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="terms-of-service.html" class="transition hover:text-brand">Terms of Service</a></li>
            <li><a href="privacy-policy.html" class="transition hover:text-brand">Privacy Policy</a></li>
            <li><a href="refund-policy.html" class="transition hover:text-brand">Refund Policy</a></li>
            <li><a href="license-policy.html" class="transition hover:text-brand">License Policy</a></li>
            <li><a href="https://dashboard.licenbase.com/submitticket.php" class="transition hover:text-brand">Support Center</a></li>
          </ul>
        </div>
      </div>

      <div class="mt-12 flex flex-col items-center justify-between gap-4 border-t border-gray-200 pt-8 text-xs text-gray-400 sm:flex-row">
        <p>© 2026 LicenBase. All rights reserved. Registered trademark of genuine software licenses.</p>
        <p class="flex items-center gap-1"><i data-lucide="lock" class="h-3.5 w-3.5 text-accent"></i> 256-Bit SSL Encrypted &amp; Non-Refundable Digital Provisioning</p>
      </div>
    </div>
  </footer>'''

# Files to update with the standardized footer
target_files = [
    "index.html",
    "terms-of-service.html",
    "privacy-policy.html",
    "refund-policy.html",
    "license-policy.html"
]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex replace any <footer class="bg-navy text-gray-300">...</footer> block
        new_content = re.sub(
            r'<!-- ============ [0-9]+ · FOOTER ============ -->\s*<footer class="bg-navy text-gray-300">[\s\S]*?</footer>|<footer class="bg-navy text-gray-300">[\s\S]*?</footer>',
            standard_footer,
            content,
            flags=re.MULTILINE
        )

        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated footer in {filename}")
        else:
            print(f"No dark footer found in {filename} (might already be updated)")

print("Footer unification complete across all pages.")

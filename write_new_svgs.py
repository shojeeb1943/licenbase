import os
import re
import sys

# 1. Generate the 10 in-article SVGs
svgs = {
    "cpanel-vs-directadmin-vs-plesk-vps-2026-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="pnl1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <linearGradient id="pnl2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="pnl3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg1)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">cPanel vs DirectAdmin vs Plesk: 2026 Comparison</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Architecture, Resource Footprint, Licensing Cost, and Ecosystem</text>

  <!-- Panel 1: cPanel -->
  <rect x="40" y="95" width="220" height="290" fill="#1e293b" stroke="#334155" stroke-width="1.5" rx="8"/>
  <rect x="40" y="95" width="220" height="45" fill="url(#pnl1)" rx="8"/>
  <text x="150" y="124" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">cPanel &amp; WHM</text>
  <text x="60" y="170" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Market Leader &amp; Standard</text>
  <text x="60" y="200" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• RAM Usage: ~1.2 - 2 GB</text>
  <text x="60" y="230" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Best WHMCS Integration</text>
  <text x="60" y="260" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Tiered Account Pricing</text>
  <text x="60" y="290" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Massive Plugin Ecosystem</text>
  <rect x="55" y="330" width="190" height="36" fill="#0f172a" stroke="#f97316" stroke-width="1" rx="6"/>
  <text x="150" y="353" fill="#f97316" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LicenBase: $4.00/mo</text>

  <!-- Panel 2: DirectAdmin -->
  <rect x="290" y="95" width="220" height="290" fill="#1e293b" stroke="#334155" stroke-width="1.5" rx="8"/>
  <rect x="290" y="95" width="220" height="45" fill="url(#pnl2)" rx="8"/>
  <text x="400" y="124" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">DirectAdmin</text>
  <text x="310" y="170" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Ultra-Lightweight Core</text>
  <text x="310" y="200" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• RAM Usage: ~250 - 500 MB</text>
  <text x="310" y="230" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• CustomBuild CLI Engine</text>
  <text x="310" y="260" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Budget VPS Friendly</text>
  <text x="310" y="290" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Simpler UI Hierarchy</text>
  <rect x="305" y="330" width="190" height="36" fill="#0f172a" stroke="#3b82f6" stroke-width="1" rx="6"/>
  <text x="400" y="353" fill="#60a5fa" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Low Footprint Host</text>

  <!-- Panel 3: Plesk -->
  <rect x="540" y="95" width="220" height="290" fill="#1e293b" stroke="#334155" stroke-width="1.5" rx="8"/>
  <rect x="540" y="95" width="220" height="45" fill="url(#pnl3)" rx="8"/>
  <text x="650" y="124" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Plesk Obsidian</text>
  <text x="560" y="170" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Linux &amp; Windows Support</text>
  <text x="560" y="200" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• RAM Usage: ~1.0 - 1.5 GB</text>
  <text x="560" y="230" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• WordPress Toolkit Pro</text>
  <text x="560" y="260" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Docker &amp; Node.js Native</text>
  <text x="560" y="290" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Web Agency Standard</text>
  <rect x="555" y="330" width="190" height="36" fill="#0f172a" stroke="#10b981" stroke-width="1" rx="6"/>
  <text x="650" y="353" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LicenBase: $4.50/mo</text>
</svg>""",

    "10-cpanel-security-settings-change-after-installation-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg2)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">10 Critical cPanel/WHM Post-Install Security Settings</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Baseline Hardening Steps for Linux Web Hosting Servers</text>

  <rect x="50" y="95" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="80" cy="121" r="16" fill="#ef4444"/>
  <text x="80" y="126" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
  <text x="110" y="117" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Disable Root Password SSH</text>
  <text x="110" y="135" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Enforce Ed25519 / RSA SSH Key Auth</text>

  <rect x="50" y="155" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="80" cy="181" r="16" fill="#ef4444"/>
  <text x="80" y="186" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
  <text x="110" y="177" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Enable cPHulk Brute Force</text>
  <text x="110" y="195" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Lockout malicious IPs on failed logins</text>

  <rect x="50" y="215" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="80" cy="241" r="16" fill="#ef4444"/>
  <text x="80" y="246" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
  <text x="110" y="237" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Enable ModSecurity OWASP CRS</text>
  <text x="110" y="255" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Block SQLi, XSS, and exploit probes</text>

  <rect x="50" y="275" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="80" cy="301" r="16" fill="#ef4444"/>
  <text x="80" y="306" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
  <text x="110" y="297" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Disable Compilers for Users</text>
  <text x="110" y="315" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Prevent non-root gcc/g++ binary runs</text>

  <rect x="50" y="335" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="80" cy="361" r="16" fill="#ef4444"/>
  <text x="80" y="366" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">5</text>
  <text x="110" y="357" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Enable Two-Factor Auth (2FA)</text>
  <text x="110" y="375" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Mandatory TOTP for WHM Root logins</text>

  <!-- Right Column -->
  <rect x="415" y="95" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="445" cy="121" r="16" fill="#f97316"/>
  <text x="445" y="126" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">6</text>
  <text x="475" y="117" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Install CSF / Imunify360</text>
  <text x="475" y="135" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Stateful firewall &amp; AI WAF filtering</text>

  <rect x="415" y="155" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="445" cy="181" r="16" fill="#f97316"/>
  <text x="445" y="186" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">7</text>
  <text x="475" y="177" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Disable Insecure TLS Ciphers</text>
  <text x="475" y="195" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Enforce TLS 1.2 &amp; 1.3 only across Apache</text>

  <rect x="415" y="215" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="445" cy="241" r="16" fill="#f97316"/>
  <text x="445" y="246" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">8</text>
  <text x="475" y="237" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Enable Symlink Protection</text>
  <text x="475" y="255" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Block cross-account symlink traversing</text>

  <rect x="415" y="275" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="445" cy="301" r="16" fill="#f97316"/>
  <text x="445" y="306" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">9</text>
  <text x="475" y="297" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Isolate Accounts with CageFS</text>
  <text x="475" y="315" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">CloudLinux virtualized per-user filesystem</text>

  <rect x="415" y="335" width="335" height="52" fill="#1e293b" stroke="#334155" rx="6"/>
  <circle cx="445" cy="361" r="16" fill="#f97316"/>
  <text x="445" y="366" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">10</text>
  <text x="475" y="357" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">Limit Max Outbound Hourly Emails</text>
  <text x="475" y="375" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">Prevent IP blacklisting from hacked scripts</text>
</svg>""",

    "how-to-check-cpu-usage-linux-vps-commands-tips-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg3)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Linux VPS CPU Diagnostic Workflow</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Essential CLI Commands to Identify &amp; Resolve High Load Average</text>

  <!-- Step 1 -->
  <rect x="50" y="100" width="210" height="130" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="8"/>
  <text x="155" y="130" fill="#60a5fa" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. High-Level Load</text>
  <rect x="65" y="145" width="180" height="30" fill="#0f172a" rx="4"/>
  <text x="75" y="165" fill="#22c55e" font-size="12" font-family="monospace">uptime &amp;&amp; htop</text>
  <text x="155" y="195" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Check 1, 5, 15m load average</text>
  <text x="155" y="212" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Compare against CPU core count</text>

  <!-- Arrow 1 -->
  <path d="M 265 165 L 290 165" stroke="#64748b" stroke-width="2" marker-end="url(#arr)"/>

  <!-- Step 2 -->
  <rect x="295" y="100" width="210" height="130" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
  <text x="400" y="130" fill="#fbbf24" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. Process Breakdown</text>
  <rect x="310" y="145" width="180" height="30" fill="#0f172a" rx="4"/>
  <text x="320" y="165" fill="#22c55e" font-size="12" font-family="monospace">ps aux --sort=-%cpu</text>
  <text x="400" y="195" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Identify top CPU consumers</text>
  <text x="400" y="212" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">(PHP-FPM, MySQL, mysqld, gzip)</text>

  <!-- Arrow 2 -->
  <path d="M 510 165 L 535 165" stroke="#64748b" stroke-width="2"/>

  <!-- Step 3 -->
  <rect x="540" y="100" width="210" height="130" fill="#1e293b" stroke="#ec4899" stroke-width="1.5" rx="8"/>
  <text x="645" y="130" fill="#f472b6" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. Disk I/O Bottleneck</text>
  <rect x="555" y="145" width="180" height="30" fill="#0f172a" rx="4"/>
  <text x="565" y="165" fill="#22c55e" font-size="12" font-family="monospace">iotop -oPa</text>
  <text x="645" y="195" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Inspect WA (iowait) % state</text>
  <text x="645" y="212" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Find thrashing disk processes</text>

  <!-- Bottom Details Box -->
  <rect x="50" y="255" width="700" height="135" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="75" y="285" fill="#f8fafc" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Database &amp; Web Server Deep-Dive Commands:</text>
  <text x="75" y="315" fill="#38bdf8" font-size="12" font-family="monospace">mysqladmin proc stat</text>
  <text x="255" y="315" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">— Identify unindexed slow queries locking MySQL tables</text>
  <text x="75" y="345" fill="#38bdf8" font-size="12" font-family="monospace">perf top -a</text>
  <text x="255" y="345" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">— Real-time Linux kernel symbol profile &amp; context switch spikes</text>
  <text x="75" y="375" fill="#38bdf8" font-size="12" font-family="monospace">mpstat -P ALL 2 5</text>
  <text x="255" y="375" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">— Individual core CPU saturation &amp; hardware interrupt stats</text>
</svg>""",

    "cpanel-license-vs-vps-cost-hosting-server-budget-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg4)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">cPanel VPS Server Monthly Budget Breakdown</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Retail Pricing vs. LicenBase Optimized Licensing Stack</text>

  <!-- Retail Stack Box -->
  <rect x="50" y="95" width="330" height="290" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" rx="8"/>
  <rect x="50" y="95" width="330" height="42" fill="#ef4444" rx="8"/>
  <text x="215" y="122" fill="#ffffff" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Standard Retail Stack (Monthly)</text>
  
  <text x="75" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">KVM VPS (4 vCPU / 8GB RAM):</text>
  <text x="330" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$20.00</text>
  
  <text x="75" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">cPanel Premier Retail (100 Acc):</text>
  <text x="330" y="195" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$60.99</text>
  
  <text x="75" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">LiteSpeed 2-Core Retail:</text>
  <text x="330" y="225" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$26.00</text>

  <text x="75" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">CloudLinux Shared Retail:</text>
  <text x="330" y="255" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$16.00</text>

  <line x1="70" y1="280" x2="350" y2="280" stroke="#334155" stroke-width="1"/>
  <text x="75" y="315" fill="#f87171" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Total Monthly Expense:</text>
  <text x="330" y="315" fill="#f87171" font-size="18" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$122.99/mo</text>
  <text x="215" y="355" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Annual Cost: $1,475.88 / yr</text>

  <!-- LicenBase Optimized Box -->
  <rect x="420" y="95" width="330" height="290" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="8"/>
  <rect x="420" y="95" width="330" height="42" fill="#10b981" rx="8"/>
  <text x="585" y="122" fill="#ffffff" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LicenBase Stack (Monthly)</text>
  
  <text x="445" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">KVM VPS (4 vCPU / 8GB RAM):</text>
  <text x="700" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$20.00</text>
  
  <text x="445" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">cPanel VPS (Unlimited Acc):</text>
  <text x="700" y="195" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$4.00</text>
  
  <text x="445" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">LiteSpeed Web Server:</text>
  <text x="700" y="225" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$6.00</text>

  <text x="445" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">CloudLinux OS License:</text>
  <text x="700" y="255" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$7.00</text>

  <line x1="440" y1="280" x2="720" y2="280" stroke="#334155" stroke-width="1"/>
  <text x="445" y="315" fill="#34d399" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Total Monthly Expense:</text>
  <text x="700" y="315" fill="#34d399" font-size="18" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="end">$37.00/mo</text>
  <text x="585" y="355" fill="#10b981" font-weight="bold" font-size="12" font-family="system-ui, sans-serif" text-anchor="middle">Save Over $1,031 / Year (70% Margins)</text>
</svg>""",

    "why-is-my-vps-using-so-much-ram-causes-fixes-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg5)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Understanding Linux VPS RAM Consumption</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Active Process Memory vs. Linux Buffers &amp; Page Cache</text>

  <!-- RAM Bar Visual -->
  <rect x="60" y="100" width="680" height="50" fill="#1e293b" stroke="#475569" rx="6"/>
  <rect x="60" y="100" width="220" height="50" fill="#ef4444" rx="6"/>
  <rect x="280" y="100" width="180" height="50" fill="#f59e0b"/>
  <rect x="460" y="100" width="200" height="50" fill="#3b82f6"/>
  <rect x="660" y="100" width="80" height="50" fill="#10b981" rx="6"/>

  <text x="170" y="130" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">App (PHP/MySQL) 32%</text>
  <text x="370" y="130" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Services &amp; OS 26%</text>
  <text x="560" y="130" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Buffers / Cache 30%</text>
  <text x="700" y="130" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Free 12%</text>

  <!-- 3 Diagnosis Pillars -->
  <rect x="60" y="175" width="210" height="205" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="165" y="205" fill="#f87171" font-size="14" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. PHP-FPM Workers</text>
  <text x="75" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• pm.max_children set too high</text>
  <text x="75" y="260" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Unbounded memory_limit</text>
  <text x="75" y="285" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Leaking WP plugins</text>
  <text x="75" y="315" fill="#38bdf8" font-size="11" font-family="monospace">pm = ondemand</text>
  <text x="75" y="335" fill="#38bdf8" font-size="11" font-family="monospace">pm.process_idle_timeout = 10s</text>

  <rect x="295" y="175" width="210" height="205" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="400" y="205" fill="#fbbf24" font-size="14" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. MySQL Buffer Pool</text>
  <text x="310" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• innodb_buffer_pool_size</text>
  <text x="310" y="260" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Over-allocated thread buffers</text>
  <text x="310" y="285" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• max_connections > 300</text>
  <text x="310" y="315" fill="#38bdf8" font-size="11" font-family="monospace">innodb_buffer_pool = 50%</text>
  <text x="310" y="335" fill="#38bdf8" font-size="11" font-family="monospace">table_open_cache = 2000</text>

  <rect x="530" y="175" width="210" height="205" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="635" y="205" fill="#34d399" font-size="14" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. Cache is Reclaimable</text>
  <text x="545" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Linux holds files in RAM</text>
  <text x="545" y="260" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Auto-freed when apps ask</text>
  <text x="545" y="285" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Check "available" column</text>
  <text x="545" y="315" fill="#38bdf8" font-size="11" font-family="monospace">free -h</text>
  <text x="545" y="335" fill="#38bdf8" font-size="11" font-family="monospace">vm.swappiness = 10</text>
</svg>""",

    "litespeed-vs-nginx-for-wordpress-performance-cost-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="lsGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="ngGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg6)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LiteSpeed Enterprise vs. Nginx for WordPress</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Caching Architecture, .htaccess Compatibility, TTFB &amp; VPS Requirements</text>

  <!-- LiteSpeed Column -->
  <rect x="50" y="95" width="330" height="290" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="8"/>
  <rect x="50" y="95" width="330" height="42" fill="url(#lsGrad)" rx="8"/>
  <text x="215" y="122" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LiteSpeed Enterprise (LSCache)</text>
  <text x="75" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Server-Level LSCache Engine (Fastest TTFB)</text>
  <text x="75" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 100% Native .htaccess Rewrite Support</text>
  <text x="75" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• LSAPI PHP Architecture (50% less RAM)</text>
  <text x="75" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Automatic ESI &amp; WooCommerce Caching</text>
  <text x="75" y="285" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 1-Click cPanel / Plesk Integration</text>
  <rect x="70" y="330" width="290" height="36" fill="#0f172a" stroke="#3b82f6" rx="6"/>
  <text x="215" y="353" fill="#60a5fa" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LicenBase: $6.00/mo (VPS)</text>

  <!-- Nginx Column -->
  <rect x="420" y="95" width="330" height="290" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="8"/>
  <rect x="420" y="95" width="330" height="42" fill="url(#ngGrad)" rx="8"/>
  <text x="585" y="122" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Nginx (FastCGI Microcache)</text>
  <text x="445" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Open-Source &amp; Free Core Binary</text>
  <text x="445" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Requires Manual FastCGI Cache Config</text>
  <text x="445" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• NO .htaccess Support (Manual Nginx rules)</text>
  <text x="445" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Higher Maintenance for Multi-User Hosting</text>
  <text x="445" y="285" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Excellent Standalone Reverse Proxy</text>
  <rect x="440" y="330" width="290" height="36" fill="#0f172a" stroke="#10b981" rx="6"/>
  <text x="585" y="353" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Free / High Manual Config</text>
</svg>""",

    "how-to-install-softaculous-on-cpanel-setup-guide-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg7)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Softaculous cPanel Installation &amp; Setup</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Single-Command Install, IonCube Setup, and License Activation</text>

  <!-- Step 1 -->
  <rect x="50" y="95" width="210" height="150" fill="#1e293b" stroke="#334155" rx="8"/>
  <rect x="50" y="95" width="210" height="35" fill="#3b82f6" rx="8"/>
  <text x="155" y="118" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Step 1: Enable IonCube</text>
  <text x="65" y="150" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">WHM &gt; Tweak Settings &gt; PHP</text>
  <text x="65" y="170" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">Select "ioncube" loader for</text>
  <text x="65" y="190" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">cPanel internal PHP runtime.</text>
  <rect x="60" y="205" width="190" height="25" fill="#0f172a" rx="4"/>
  <text x="70" y="222" fill="#22c55e" font-size="10" font-family="monospace">Save Tweak Settings</text>

  <!-- Step 2 -->
  <rect x="295" y="95" width="210" height="150" fill="#1e293b" stroke="#334155" rx="8"/>
  <rect x="295" y="95" width="210" height="35" fill="#f97316" rx="8"/>
  <text x="400" y="118" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Step 2: Run Installer</text>
  <text x="310" y="150" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">Download and execute official</text>
  <text x="310" y="170" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">install.sh via SSH root terminal.</text>
  <rect x="305" y="200" width="190" height="35" fill="#0f172a" rx="4"/>
  <text x="315" y="215" fill="#22c55e" font-size="9" font-family="monospace">wget -N files.softaculous.com/install.sh</text>
  <text x="315" y="228" fill="#22c55e" font-size="9" font-family="monospace">chmod 755 install.sh; ./install.sh</text>

  <!-- Step 3 -->
  <rect x="540" y="95" width="210" height="150" fill="#1e293b" stroke="#334155" rx="8"/>
  <rect x="540" y="95" width="210" height="35" fill="#10b981" rx="8"/>
  <text x="645" y="118" fill="#fff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Step 3: Activate License</text>
  <text x="555" y="150" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">Bind server IP on LicenBase.</text>
  <text x="555" y="170" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">Run automated activation</text>
  <text x="555" y="190" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">command on server.</text>
  <rect x="550" y="205" width="190" height="25" fill="#0f172a" rx="4"/>
  <text x="560" y="222" fill="#38bdf8" font-size="10" font-family="monospace">450+ 1-Click Apps Unlocked</text>

  <!-- Bottom Verification Box -->
  <rect x="50" y="265" width="700" height="120" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="75" y="295" fill="#f8fafc" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Post-Install Verification &amp; Cron Automation:</text>
  <text x="75" y="325" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Verify WHM Plugins list shows "Softaculous - Instant Installs" in left navigation menu.</text>
  <text x="75" y="348" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Automated nightly script updates run via `/etc/cron.d/softaculous` to patch WordPress/Joomla installer packages.</text>
  <text x="75" y="371" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Backup to Google Drive, Dropbox, AWS S3 &amp; WebDAV enabled across all end-user cPanel accounts.</text>
</svg>""",

    "cloudlinux-vs-almalinux-shared-hosting-2026-guide-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="clGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="alGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg8)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CloudLinux OS vs. AlmaLinux for Shared Hosting</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Multi-Tenant Resource Isolation, Security &amp; Operating System Architecture</text>

  <!-- CloudLinux Column -->
  <rect x="50" y="95" width="330" height="290" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" rx="8"/>
  <rect x="50" y="95" width="330" height="42" fill="url(#clGrad)" rx="8"/>
  <text x="215" y="122" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CloudLinux OS (Enterprise Shared)</text>
  <text x="75" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• LVE Manager: CPU, RAM &amp; IOPS throttling</text>
  <text x="75" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• CageFS: Virtualized isolated per-user jail</text>
  <text x="75" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• MySQL Governor: Throttles runaway SQL queries</text>
  <text x="75" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• HardenedPHP: Secures end-of-life PHP versions</text>
  <text x="75" y="285" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Stops "Bad Neighbor" server downtime 100%</text>
  <rect x="70" y="330" width="290" height="36" fill="#0f172a" stroke="#0284c7" rx="6"/>
  <text x="215" y="353" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LicenBase: $7.00/mo (VPS)</text>

  <!-- AlmaLinux Column -->
  <rect x="420" y="95" width="330" height="290" fill="#1e293b" stroke="#64748b" stroke-width="1.5" rx="8"/>
  <rect x="420" y="95" width="330" height="42" fill="url(#alGrad)" rx="8"/>
  <text x="585" y="122" fill="#ffffff" font-size="16" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">AlmaLinux 8 / 9 (Standard OS)</text>
  <text x="445" y="165" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 100% Free &amp; Open-Source RHEL Clone</text>
  <text x="445" y="195" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Shared global CPU / RAM pool (No limits)</text>
  <text x="445" y="225" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• One abusive user can crash entire server</text>
  <text x="445" y="255" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Standard Linux permissions (No CageFS jail)</text>
  <text x="445" y="285" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Best for Dedicated VPS / Single Agency Apps</text>
  <rect x="440" y="330" width="290" height="36" fill="#0f172a" stroke="#64748b" rx="6"/>
  <text x="585" y="353" fill="#94a3b8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Free Core Base OS</text>
</svg>""",

    "hosting-server-backup-strategy-jetbackup-storage-recovery-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg9)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3-2-1 Enterprise Hosting Backup Architecture</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">JetBackup 5 Engine, Deduplicated Storage, and Point-in-Time Restores</text>

  <!-- VPS Production Server -->
  <rect x="50" y="100" width="200" height="150" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="8"/>
  <text x="150" y="130" fill="#60a5fa" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Production Server</text>
  <text x="70" y="160" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• cPanel / DirectAdmin</text>
  <text x="70" y="185" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• MySQL Databases</text>
  <text x="70" y="210" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• User /home data</text>
  <text x="70" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• SSL / DNS configs</text>

  <!-- Engine Center -->
  <rect x="300" y="100" width="200" height="150" fill="#1e293b" stroke="#f97316" stroke-width="1.5" rx="8"/>
  <text x="400" y="130" fill="#fb923c" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">JetBackup 5 Engine</text>
  <text x="320" y="160" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Incremental Backup</text>
  <text x="320" y="185" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Block-Level Deduplication</text>
  <text x="320" y="210" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• GPG Encryption</text>
  <text x="320" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Multi-Threaded Sync</text>

  <!-- Remote Destinations -->
  <rect x="550" y="100" width="200" height="150" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="8"/>
  <text x="650" y="130" fill="#34d399" font-size="15" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Offsite Destinations</text>
  <text x="570" y="160" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Wasabi / AWS S3</text>
  <text x="570" y="185" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Backblaze B2</text>
  <text x="570" y="210" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Remote SFTP Server</text>
  <text x="570" y="235" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• Local Secondary NVMe</text>

  <!-- Connectors -->
  <path d="M 250 175 L 300 175" stroke="#64748b" stroke-width="2"/>
  <path d="M 500 175 L 550 175" stroke="#64748b" stroke-width="2"/>

  <!-- Bottom Retention Specs -->
  <rect x="50" y="270" width="700" height="120" fill="#1e293b" stroke="#334155" rx="8"/>
  <text x="75" y="300" fill="#f8fafc" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Recommended Retention &amp; Recovery Strategy:</text>
  <text x="75" y="328" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• <tspan fill="#38bdf8" font-weight="bold">Hourly / Daily Snapshots:</tspan> Keep 7 daily backups for instant rollbacks of corrupted WordPress plugins.</text>
  <text x="75" y="353" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• <tspan fill="#38bdf8" font-weight="bold">Weekly &amp; Monthly Archives:</tspan> Keep 4 weekly and 3 monthly snapshots in immutable cold storage.</text>
  <text x="75" y="378" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• <tspan fill="#38bdf8" font-weight="bold">Self-Service Client Restores:</tspan> Empower cPanel clients to restore single files, tables, or mailboxes without support tickets.</text>
</svg>""",

    "cheap-vps-affordable-licenses-low-cost-hosting-server-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg10" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#bg10)" rx="12"/>
  <text x="400" y="45" fill="#f8fafc" font-size="22" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Building a High-Performance Low-Cost Hosting Stack</text>
  <text x="400" y="70" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Budget VPS Foundation + Enterprise Software Licensing Architecture</text>

  <!-- Layer 1: Hardware -->
  <rect x="60" y="100" width="680" height="50" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
  <text x="80" y="130" fill="#60a5fa" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Hardware Layer:</text>
  <text x="210" y="130" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">KVM VPS (Hetzner, OVH, Netcup, Vultr) — 4 vCPU / 8GB RAM / NVMe (~$15 - $22/mo)</text>

  <!-- Layer 2: OS & Kernel -->
  <rect x="60" y="160" width="680" height="50" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" rx="6"/>
  <text x="80" y="190" fill="#38bdf8" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">OS Isolation:</text>
  <text x="210" y="190" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">CloudLinux OS ($7/mo) — CageFS jails, LVE CPU caps, MySQL Governor</text>

  <!-- Layer 3: Control Panel -->
  <rect x="60" y="220" width="680" height="50" fill="#1e293b" stroke="#f97316" stroke-width="1.5" rx="6"/>
  <text x="80" y="250" fill="#fb923c" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Control Panel:</text>
  <text x="210" y="250" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">cPanel &amp; WHM ($4/mo) — Unlimited accounts, automated SSL, complete WHMCS sync</text>

  <!-- Layer 4: Web Engine & Addons -->
  <rect x="60" y="280" width="680" height="50" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
  <text x="80" y="310" fill="#34d399" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Web &amp; Scripts:</text>
  <text x="210" y="310" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">LiteSpeed ($6/mo) + Softaculous ($1.50/mo) + JetBackup ($3/mo) = Total Speed &amp; Security</text>

  <!-- Total Summary Bar -->
  <rect x="60" y="345" width="680" height="45" fill="#0f172a" stroke="#22c55e" stroke-width="1.5" rx="6"/>
  <text x="80" y="373" fill="#22c55e" font-size="15" font-weight="bold" font-family="system-ui, sans-serif">Enterprise Stack Total: ~$36.50/mo</text>
  <text x="720" y="373" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="end">Hosts 80-120 Production Client Websites with 99.99% Uptime</text>
</svg>"""
}

# Write the SVGs
img_dir = "assets/img/blog"
os.makedirs(img_dir, exist_ok=True)
for filename, content in svgs.items():
    path = os.path.join(img_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {path}")

print("All 10 SVGs written successfully!")

# -*- coding: utf-8 -*-
"""Generate high-quality 960x480 SVG diagrams for the 5 SEO blog posts."""
import os
from pathlib import Path

out_dir = Path("assets/img/blog")
out_dir.mkdir(parents=True, exist_ok=True)

def base_svg(title, subtitle, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="cardBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a8a" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="cardGreen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#064e3b" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#022c22" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="cardPurple" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#581c87" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#1e1b4b" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="cardAmber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#78350f" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#451a03" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="cardSlate" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg)"/>

  <!-- Title & Subtitle Header -->
  <rect x="0" y="0" width="960" height="76" fill="#0b1329" fill-opacity="0.6"/>
  <line x1="0" y1="76" x2="960" y2="76" stroke="#1e293b" stroke-width="1"/>
  <text x="480" y="34" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">{title}</text>
  <text x="480" y="58" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">{subtitle}</text>

  {content}
</svg>'''

# 1. cPanel VPS Cost Breakdown
svg1 = base_svg(
    "2026 Cheap Managed cPanel VPS Cost Architecture",
    "Comprehensive comparison of retail managed hosting fees vs unmanaged VPS + LicenBase wholesale licensing",
    '''
    <!-- Column 1: Traditional Retail Managed Hosting -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#d97706" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Retail Managed cPanel VPS ($85 - $150/mo)</text>
      
      <g transform="translate(20, 60)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f43f5e">Cloud Compute (2 vCPU / 4GB RAM)</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#a1a1aa">Bundled proprietary cloud provider markup: ~$35 - $50/mo</text>
      </g>
      
      <g transform="translate(20, 118)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f43f5e">Official cPanel Admin / Pro License</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#a1a1aa">Retail license tier fees: $29.99 - $44.99/mo per instance</text>
      </g>

      <g transform="translate(20, 176)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f43f5e">Mandatory Managed Support Surcharge</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#a1a1aa">Automated updates, basic cPanel monitoring: $30 - $60/mo</text>
      </g>

      <g transform="translate(20, 240)">
        <rect width="350" height="60" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
        <text x="175" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#fef3c7" text-anchor="middle">Annual TCO: $1,020 - $1,800 / year</text>
        <text x="175" y="46" font-family="sans-serif" font-size="11" fill="#fed7aa" text-anchor="middle">Inflated lock-in with bundled account restrictions</text>
      </g>
    </g>

    <!-- Column 2: Self-Optimized LicenBase Architecture -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Unmanaged Cloud VPS + LicenBase ($12 - $17/mo)</text>
      
      <g transform="translate(20, 60)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">Raw NVMe VPS (Hetzner / Contabo / OVH)</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">4 vCPU, 8GB RAM, 100GB NVMe storage: ~$5.50 - $10/mo</text>
      </g>
      
      <g transform="translate(20, 118)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">LicenBase Automated cPanel License</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">Uncapped accounts, genuine IP activation: ~$5.99/mo</text>
      </g>

      <g transform="translate(20, 176)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">Automated Management &amp; Security Tools</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">Auto-updates, CSF Firewall, Munin monitoring: $0/mo free</text>
      </g>

      <g transform="translate(20, 240)">
        <rect width="350" height="60" rx="8" fill="#022c22" stroke="#10b981" stroke-width="1.2"/>
        <text x="175" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#ecfdf5" text-anchor="middle">Annual TCO: $144 - $204 / year</text>
        <text x="175" y="46" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Save over $876 - $1,596 every year (85% savings)</text>
      </g>
    </g>
    '''
)

# 2. Imunify360 vs CloudLinux
svg2 = base_svg(
    "Imunify360 vs. CloudLinux OS: Security Stack Architecture",
    "Application-layer threat scrubbing vs OS-level kernel sandboxing for multi-tenant VPS hosting",
    '''
    <!-- Imunify360 Block -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#0284c7" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Imunify360: Automated Threat Defense</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">Layer: Application &amp; Web Traffic Security (L7)</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; AI Web Application Firewall (WAF) &amp; Bot Blocker</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Real-time automated malware scanning &amp; auto-cleanup</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Proactive PHP Defense (zero-day exploit neutralizer)</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">Retail Price: $12 - $45/mo</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">LicenBase Wholesale: $5.99 - $7.99/mo</text>
      </g>
    </g>

    <!-- CloudLinux Block -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#d8b4fe">CloudLinux OS: Kernel Isolation &amp; Stability</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#f3e8ff">Layer: Operating System &amp; Kernel Isolation (OS)</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Lightweight Virtual Environment (LVE) CPU/RAM caps</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; CageFS: Virtualized per-user filesystem jail</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; MySQL Governor &amp; HardenedPHP legacy security</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#4c1d95" stroke="#c084fc"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">Retail Price: $14 - $18/mo</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#d8b4fe" text-anchor="middle">LicenBase Wholesale: $5.99/mo</text>
      </g>
    </g>
    '''
)

# 3. htaccess Generator & Rewrite Rules
svg3 = base_svg(
    ".htaccess RewriteRule Execution Pipeline",
    "Step-by-step request flow through Apache and LiteSpeed mod_rewrite engine directives",
    '''
    <!-- Step 1: Inbound HTTP Request -->
    <g transform="translate(50, 150)" filter="url(#shadow)">
      <rect width="180" height="220" rx="10" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="90" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1. Inbound Request</text>
      <rect x="15" y="50" width="150" height="40" rx="6" fill="#0f172a"/>
      <text x="90" y="74" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle">http://example.com/page</text>
      
      <text x="15" y="116" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Client browser GET</text>
      <text x="15" y="136" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Passes to Web Server</text>
      <text x="15" y="156" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Checks DocumentRoot</text>
      <text x="15" y="176" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Reads local .htaccess</text>
    </g>

    <!-- Arrow 1 to 2 -->
    <path d="M 235 260 L 275 260" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="255" y="250" font-family="sans-serif" font-size="11" fill="#93c5fd" text-anchor="middle">Pass</text>

    <!-- Step 2: RewriteCond Matching -->
    <g transform="translate(280, 150)" filter="url(#shadow)">
      <rect width="190" height="220" rx="10" fill="url(#cardPurple)" stroke="#a855f7" stroke-width="1.5"/>
      <text x="95" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">2. Condition Evaluation</text>
      <rect x="15" y="50" width="160" height="52" rx="6" fill="#0f172a"/>
      <text x="20" y="70" font-family="monospace" font-size="10" fill="#e9d5ff">RewriteEngine On</text>
      <text x="20" y="90" font-family="monospace" font-size="10" fill="#e9d5ff">RewriteCond %{HTTPS} off</text>

      <text x="15" y="128" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Evaluates test strings</text>
      <text x="15" y="148" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Regex comparison</text>
      <text x="15" y="168" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Flag rules [NC, OR]</text>
      <text x="15" y="188" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Triggers on TRUE</text>
    </g>

    <!-- Arrow 2 to 3 -->
    <path d="M 475 260 L 515 260" stroke="#c084fc" stroke-width="2.5"/>
    <text x="495" y="250" font-family="sans-serif" font-size="11" fill="#d8b4fe" text-anchor="middle">Match</text>

    <!-- Step 3: RewriteRule Transformation -->
    <g transform="translate(520, 150)" filter="url(#shadow)">
      <rect width="190" height="220" rx="10" fill="url(#cardAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="95" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24" text-anchor="middle">3. URL Transformation</text>
      <rect x="15" y="50" width="160" height="52" rx="6" fill="#0f172a"/>
      <text x="20" y="70" font-family="monospace" font-size="10" fill="#fde68a">RewriteRule ^(.*)$</text>
      <text x="20" y="90" font-family="monospace" font-size="10" fill="#fde68a">https://%{HTTP_HOST}/$1</text>

      <text x="15" y="128" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Captures pattern $1..$9</text>
      <text x="15" y="148" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Substitutes target URL</text>
      <text x="15" y="168" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Applies [R=301,L] flags</text>
      <text x="15" y="188" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Stops rule iteration</text>
    </g>

    <!-- Arrow 3 to 4 -->
    <path d="M 715 260 L 755 260" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="735" y="250" font-family="sans-serif" font-size="11" fill="#fde68a" text-anchor="middle">Output</text>

    <!-- Step 4: Final Response / Redirection -->
    <g transform="translate(760, 150)" filter="url(#shadow)">
      <rect width="150" height="220" rx="10" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <text x="75" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">4. Browser Client</text>
      <rect x="15" y="50" width="120" height="40" rx="6" fill="#0f172a"/>
      <text x="75" y="74" font-family="sans-serif" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">HTTP 301 Moved</text>

      <text x="12" y="116" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Permanent cache</text>
      <text x="12" y="136" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Passes SEO equity</text>
      <text x="12" y="156" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Connects via TLS</text>
      <text x="12" y="176" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Clean lock icon</text>
    </g>
    '''
)

# 4. cPanel Webmail Ports 2095 vs 2096
svg4 = base_svg(
    "cPanel Webmail Ports Architecture: 2095 (HTTP) vs. 2096 (HTTPS/TLS)",
    "Port inspection, SSL handshakes, reverse proxy webmail subdomains, and firewall routing",
    '''
    <!-- Port 2095: Insecure HTTP -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#d97706" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Port 2095: Plaintext cPanel Webmail (Insecure)</text>
      
      <g transform="translate(20, 60)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f87171">Connection: Unencrypted Cleartext (HTTP)</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#94a3b8">URL format: http://mail.example.com:2095</text>
      </g>
      
      <g transform="translate(20, 118)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f87171">Security Vulnerability: Credential Sniffing</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#94a3b8">Passwords &amp; email messages transmitted in raw text over LAN</text>
      </g>

      <g transform="translate(20, 176)">
        <rect width="350" height="48" rx="8" fill="#18181b" stroke="#27272a"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#fbbf24">Production Recommendation: Redirect to 2096</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#94a3b8">WHM Tweak Settings &raquo; Require SSL for cPanel/Webmail Services</text>
      </g>

      <g transform="translate(20, 240)">
        <rect width="350" height="60" rx="8" fill="#451a03" stroke="#f59e0b"/>
        <text x="175" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#fef3c7" text-anchor="middle">Deprecated Protocol</text>
        <text x="175" y="46" font-family="sans-serif" font-size="11" fill="#fed7aa" text-anchor="middle">Corporate firewalls frequently block unencrypted email ports</text>
      </g>
    </g>

    <!-- Port 2096: Encrypted HTTPS / TLS -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Port 2096: Encrypted Webmail (TLS / SSL)</text>
      
      <g transform="translate(20, 60)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">Connection: High-Grade TLS 1.3 Encryption</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">URL format: https://mail.example.com:2096</text>
      </g>
      
      <g transform="translate(20, 118)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">Firewall Rules: CSF / Firewalld TCP Inbound</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">Must whitelist TCP port 2096 in CSF TCP_IN configuration</text>
      </g>

      <g transform="translate(20, 176)">
        <rect width="350" height="48" rx="8" fill="#064e3b" stroke="#047857"/>
        <text x="15" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">Firewall Bypass Alternative: Webmail Proxy</text>
        <text x="15" y="40" font-family="sans-serif" font-size="11" fill="#6ee7b7">https://webmail.example.com (routes over standard port 443)</text>
      </g>

      <g transform="translate(20, 240)">
        <rect width="350" height="60" rx="8" fill="#022c22" stroke="#10b981"/>
        <text x="175" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#ecfdf5" text-anchor="middle">Standard Production Webmail Standard</text>
        <text x="175" y="46" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">End-to-end encrypted session with Roundcube Webmail</text>
      </g>
    </g>
    '''
)

# 5. LiteSpeed vs DirectAdmin License Pricing
svg5 = base_svg(
    "LiteSpeed vs. DirectAdmin: VPS Architecture & Cost Optimization",
    "Pairing DirectAdmin control panel with LiteSpeed Web Server to achieve 80% licensing cost reduction",
    '''
    <!-- Box 1: DirectAdmin (Control Panel) -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#0284c7" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">DirectAdmin: Lightweight Control Panel</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">Role: Account, DNS, Email &amp; Database Management</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Ultra-low memory footprint (~15 MB RAM idle)</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Full cPanel backup import compatibility via CustomBuild</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Unlimited domains without per-account micro-tier penalization</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">Retail: $15 - $29/mo | LicenBase: $4.99/mo</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">Cuts control panel licensing by up to 75%</text>
      </g>
    </g>

    <!-- Box 2: LiteSpeed (Web Server) -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">LiteSpeed Enterprise: High-Performance Engine</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">Role: High-Concurrency HTTP/3 Web Acceleration</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Drop-in Apache replacement (reads .htaccess natively)</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Built-in LSCache &amp; ESI engine for instant WordPress loading</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Multiplies VPS tenant density by 300% to 500%</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#022c22" stroke="#10b981"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#ecfdf5" text-anchor="middle">Retail: $10 - $65/mo | LicenBase: $5.99/mo</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Wholesale performance without enterprise cost</text>
      </g>
    </g>
    '''
)

svgs = {
    "cheap-managed-cpanel-vps-hosting-cost-breakdown-2026-1.svg": svg1,
    "imunify360-vs-cloudlinux-pricing-server-security-guide-1.svg": svg2,
    "htaccess-generator-rewrite-rules-optimization-guide-1.svg": svg3,
    "cpanel-webmail-ports-explained-2095-2096-1.svg": svg4,
    "litespeed-vs-directadmin-license-pricing-2026-1.svg": svg5,
}

for name, content in svgs.items():
    p = out_dir / name
    p.write_text(content.strip(), encoding="utf-8")
    print(f"Generated {p} ({p.stat().st_size} bytes)")

print("All 5 SVGs successfully generated.")

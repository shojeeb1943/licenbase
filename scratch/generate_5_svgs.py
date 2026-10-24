import os
from pathlib import Path

out_dir = Path("assets/img/blog")
out_dir.mkdir(parents=True, exist_ok=True)

# Common SVG header & styles
def make_svg(title, subtitle, content_groups):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="cardBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardEmerald" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <linearGradient id="cardPurple" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#581c87"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="cardAmber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg)"/>

  <!-- Title & Subtitle -->
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">{title}</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">{subtitle}</text>

  {content_groups}
</svg>'''

# 1. Imunify360 Pricing & ROI SVG
svg1_content = '''
  <!-- Card 1: Single User -->
  <g transform="translate(50, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Single User VPS</text>
    <text x="20" y="70" font-family="sans-serif" font-size="12" font-weight="bold" fill="#f8fafc">Capacity: 1 Account</text>
    <text x="20" y="92" font-family="sans-serif" font-size="11" fill="#94a3b8">Target: Devs &amp; E-commerce</text>
    
    <rect x="15" y="110" width="230" height="130" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="132" font-family="sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1">Protection Features:</text>
    <text x="25" y="152" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; AI Web Application Firewall</text>
    <text x="25" y="172" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Automated Real-Time Scanner</text>
    <text x="25" y="192" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Proactive PHP Defense</text>
    <text x="25" y="212" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Herd Immunity Botnet Shield</text>

    <rect x="15" y="255" width="230" height="65" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="278" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">LicenBase Wholesale:</text>
    <text x="25" y="300" font-family="monospace" font-size="13" font-weight="bold" fill="#a7f3d0">From $1.50 / month</text>
  </g>

  <!-- Card 2: Up to 30 Users -->
  <g transform="translate(350, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardEmerald)" stroke="#34d399" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Up to 30 Users VPS</text>
    <text x="20" y="70" font-family="sans-serif" font-size="12" font-weight="bold" fill="#f8fafc">Capacity: 1 - 30 Accounts</text>
    <text x="20" y="92" font-family="sans-serif" font-size="11" fill="#94a3b8">Target: Digital Agencies &amp; Resellers</text>
    
    <rect x="15" y="110" width="230" height="130" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="132" font-family="sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1">Protection Features:</text>
    <text x="25" y="152" font-family="sans-serif" font-size="10" fill="#a7f3d0">&bull; Multi-Account Web Isolation</text>
    <text x="25" y="172" font-family="sans-serif" font-size="10" fill="#a7f3d0">&bull; Automated Malware Cleanup</text>
    <text x="25" y="192" font-family="sans-serif" font-size="10" fill="#a7f3d0">&bull; Brute-Force &amp; PAM Defense</text>
    <text x="25" y="212" font-family="sans-serif" font-size="10" fill="#a7f3d0">&bull; WordPress Integrity Verification</text>

    <rect x="15" y="255" width="230" height="65" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="278" font-family="sans-serif" font-size="11" font-weight="bold" fill="#38bdf8">Sysadmin ROI Value:</text>
    <text x="25" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Saves 15-20 hrs/mo cleanup</text>
  </g>

  <!-- Card 3: Unlimited Users -->
  <g transform="translate(650, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#c084fc">Unlimited Users (Metal/VPS)</text>
    <text x="20" y="70" font-family="sans-serif" font-size="12" font-weight="bold" fill="#f8fafc">Capacity: Unlimited Accounts</text>
    <text x="20" y="92" font-family="sans-serif" font-size="11" fill="#94a3b8">Target: Web Hosts &amp; Bare-Metal</text>
    
    <rect x="15" y="110" width="230" height="130" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="132" font-family="sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1">Enterprise Tier:</text>
    <text x="25" y="152" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Fleet-Wide Incident Scrubbing</text>
    <text x="25" y="172" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Zero False-Positive WAF Engine</text>
    <text x="25" y="192" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Direct Official Signature Updates</text>
    <text x="25" y="212" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Instant IP Licensing Delivery</text>

    <rect x="15" y="255" width="230" height="65" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="278" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">LicenBase Advantage:</text>
    <text x="25" y="300" font-family="sans-serif" font-size="11" fill="#a7f3d0">Full updates, no retail markup</text>
  </g>
'''
(out_dir / "imunify360-license-pricing-plans-roi-guide-1.svg").write_text(
    make_svg("Imunify360 License Pricing &amp; Security ROI Architecture", 
             "Account tiers, automated malware defense capabilities, and total operational savings", svg1_content),
    encoding="utf-8"
)

# 2. cPanel VPS Cost & Configuration SVG
svg2_content = '''
  <!-- Column 1: Hypervisor & Hardware -->
  <g transform="translate(50, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">1. Hypervisor &amp; Hardware</text>
    
    <rect x="15" y="55" width="230" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Supported Environments:</text>
    <text x="25" y="98" font-family="monospace" font-size="10" fill="#38bdf8">&bull; KVM / Proxmox VE</text>
    <text x="25" y="116" font-family="monospace" font-size="10" fill="#38bdf8">&bull; Virtualizor / VMware ESXi</text>

    <rect x="15" y="150" width="230" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="173" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Hardware Baselines:</text>
    <text x="25" y="193" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Min: 2 GB RAM (cPanel Solo)</text>
    <text x="25" y="211" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Rec: 4 - 8 GB RAM (Admin/Pro)</text>

    <rect x="15" y="245" width="230" height="75" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="268" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Hypervisor Flag Check:</text>
    <text x="25" y="288" font-family="monospace" font-size="10" fill="#a7f3d0">systemd-detect-virt</text>
    <text x="25" y="306" font-family="sans-serif" font-size="9" fill="#94a3b8">Validates VPS license eligibility</text>
  </g>

  <!-- Column 2: Licensing Tiers -->
  <g transform="translate(350, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardEmerald)" stroke="#34d399" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">2. cPanel VPS License Tiers</text>
    
    <rect x="15" y="55" width="230" height="55" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">cPanel Solo (1 Account)</text>
    <text x="25" y="93" font-family="sans-serif" font-size="10" fill="#6ee7b7">Freelance dev, single store node</text>

    <rect x="15" y="118" width="230" height="55" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="138" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">cPanel Admin (Up to 5)</text>
    <text x="25" y="156" font-family="sans-serif" font-size="10" fill="#6ee7b7">Boutique agencies, internal apps</text>

    <rect x="15" y="181" width="230" height="55" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="201" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">cPanel Pro (Up to 30)</text>
    <text x="25" y="219" font-family="sans-serif" font-size="10" fill="#6ee7b7">Growing reseller &amp; multi-client VPS</text>

    <rect x="15" y="244" width="230" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="265" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Premier Cloud (100+)</text>
    <text x="25" y="283" font-family="sans-serif" font-size="10" fill="#94a3b8">Scalable per-account increments</text>
    <text x="25" y="301" font-family="monospace" font-size="10" fill="#38bdf8">Wholesale pricing at LicenBase</text>
  </g>

  <!-- Column 3: TCO Optimization -->
  <g transform="translate(650, 100)" filter="url(#shadow)">
    <rect width="260" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
    <rect width="260" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#c084fc">3. Monthly TCO Blueprint</text>
    
    <rect x="15" y="55" width="230" height="85" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Monthly Budget Stack:</text>
    <text x="25" y="98" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; 4GB Cloud VPS: ~$12/mo</text>
    <text x="25" y="116" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; cPanel IP License: ~$4/mo</text>

    <rect x="15" y="150" width="230" height="85" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="173" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Performance Add-Ons:</text>
    <text x="25" y="193" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; LiteSpeed: Fast WP caching</text>
    <text x="25" y="211" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; CloudLinux: Resource limits</text>

    <rect x="15" y="245" width="230" height="75" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="268" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Combo Stack Savings:</text>
    <text x="25" y="288" font-family="sans-serif" font-size="10" fill="#a7f3d0">Save up to 40% with bundles</text>
    <text x="25" y="306" font-family="sans-serif" font-size="9" fill="#94a3b8">Instant automated activation</text>
  </g>
'''
(out_dir / "cpanel-vps-cost-configuration-practical-guide-1.svg").write_text(
    make_svg("cPanel VPS Cost &amp; Configuration Sizing Blueprint", 
             "Virtualization environments, license tier capacities, and practical monthly hosting budgets", svg2_content),
    encoding="utf-8"
)

# 3. cPanel Webmail Ports SVG
svg3_content = '''
  <!-- Port 2095 Group -->
  <g transform="translate(60, 100)" filter="url(#shadow)">
    <rect width="380" height="340" rx="12" fill="url(#cardAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="380" height="40" rx="12" fill="#b45309" fill-opacity="0.3"/>
    <text x="24" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#fcd34d">Port 2095 (HTTP Unencrypted)</text>
    
    <rect x="20" y="55" width="340" height="75" rx="8" fill="#451a03" stroke="#78350f"/>
    <text x="35" y="78" font-family="monospace" font-size="11" font-weight="bold" fill="#fcd34d">http://example.com:2095</text>
    <text x="35" y="98" font-family="sans-serif" font-size="10" fill="#fed7aa">Plaintext transport. Browser flags as 'Not Secure'.</text>
    <text x="35" y="116" font-family="sans-serif" font-size="10" fill="#f87171">Not recommended for production passwords.</text>

    <rect x="20" y="140" width="340" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="35" y="163" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Server Redirection Policy:</text>
    <text x="35" y="183" font-family="sans-serif" font-size="10" fill="#94a3b8">WHM &raquo; Tweak Settings &raquo; Redirection:</text>
    <text x="35" y="201" font-family="monospace" font-size="10" fill="#38bdf8">Always redirect to SSL (Port 2096)</text>

    <rect x="20" y="235" width="340" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="35" y="258" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Firewall Diagnostic Check:</text>
    <text x="35" y="278" font-family="monospace" font-size="10" fill="#cbd5e1">grep TCP_IN /etc/csf/csf.conf</text>
    <text x="35" y="296" font-family="sans-serif" font-size="10" fill="#94a3b8">Ensure 2095 is listed in inbound TCP rules</text>
  </g>

  <!-- Port 2096 Group -->
  <g transform="translate(520, 100)" filter="url(#shadow)">
    <rect width="380" height="340" rx="12" fill="url(#cardEmerald)" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="40" rx="12" fill="#059669" fill-opacity="0.3"/>
    <text x="24" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#6ee7b7">Port 2096 (HTTPS Secure / SSL)</text>
    
    <rect x="20" y="55" width="340" height="75" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="35" y="78" font-family="monospace" font-size="11" font-weight="bold" fill="#a7f3d0">https://example.com:2096</text>
    <text x="35" y="98" font-family="sans-serif" font-size="10" fill="#6ee7b7">TLS 1.3 / AES-256 encrypted authentication.</text>
    <text x="35" y="116" font-family="sans-serif" font-size="10" fill="#34d399">Standard production endpoint for Roundcube/Horde.</text>

    <rect x="20" y="140" width="340" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="35" y="163" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">AutoSSL Certificate Binding:</text>
    <text x="35" y="183" font-family="sans-serif" font-size="10" fill="#94a3b8">Secures webmail.domain.com and hostname</text>
    <text x="35" y="201" font-family="monospace" font-size="10" fill="#34d399">/usr/local/cpanel/bin/checkallsslcerts</text>

    <rect x="20" y="235" width="340" height="85" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="35" y="258" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">Troubleshooting SSL Handshakes:</text>
    <text x="35" y="278" font-family="monospace" font-size="10" fill="#6ee7b7">openssl s_client -connect host:2096</text>
    <text x="35" y="296" font-family="sans-serif" font-size="10" fill="#a7f3d0">Validates certificate chain and cipher handshake</text>
  </g>
'''
(out_dir / "cpanel-webmail-ports-ssl-login-issues-fixed-1.svg").write_text(
    make_svg("cPanel Webmail Ports (2095 vs 2096) Diagnostic Architecture", 
             "Comparing unencrypted HTTP vs TLS-secured HTTPS webmail access and firewall rules", svg3_content),
    encoding="utf-8"
)

# 4. LiteSpeed License Comparison SVG
svg4_content = '''
  <!-- Card 1: Free & Starter -->
  <g transform="translate(40, 100)" filter="url(#shadow)">
    <rect width="265" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="265" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8">Site Owner / Free</text>
    
    <rect x="15" y="55" width="235" height="80" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="76" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Hardware Restrictions:</text>
    <text x="25" y="96" font-family="monospace" font-size="10" fill="#38bdf8">&bull; 1 Worker Process</text>
    <text x="25" y="114" font-family="monospace" font-size="10" fill="#38bdf8">&bull; Max RAM: 2 GB RAM limit</text>

    <rect x="15" y="145" width="235" height="80" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="166" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Domain Limitation:</text>
    <text x="25" y="186" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Up to 5 Top-Level Domains</text>
    <text x="25" y="204" font-family="sans-serif" font-size="10" fill="#94a3b8">&bull; Ideal for single-site staging</text>

    <rect x="15" y="235" width="235" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="256" font-family="sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1">Suitability:</text>
    <text x="25" y="276" font-family="sans-serif" font-size="10" fill="#94a3b8">Strict memory caps make it</text>
    <text x="25" y="294" font-family="sans-serif" font-size="10" fill="#94a3b8">unsuitable for commercial hosts</text>
  </g>

  <!-- Card 2: Web Host Lite / Essential -->
  <g transform="translate(345, 100)" filter="url(#shadow)">
    <rect width="265" height="340" rx="12" fill="url(#cardEmerald)" stroke="#34d399" stroke-width="1.5"/>
    <rect width="265" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">Web Host Essential (2-Worker)</text>
    
    <rect x="15" y="55" width="235" height="80" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="76" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">Hardware Capacity:</text>
    <text x="25" y="96" font-family="monospace" font-size="10" fill="#6ee7b7">&bull; 2 Worker Processes</text>
    <text x="25" y="114" font-family="monospace" font-size="10" fill="#6ee7b7">&bull; RAM Cap: Up to 8 GB RAM</text>

    <rect x="15" y="145" width="235" height="80" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="166" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">Domain Capacity:</text>
    <text x="25" y="186" font-family="sans-serif" font-size="10" fill="#6ee7b7">&bull; Unlimited Domains</text>
    <text x="25" y="204" font-family="sans-serif" font-size="10" fill="#6ee7b7">&bull; High-traffic agency sweet spot</text>

    <rect x="15" y="235" width="235" height="85" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="256" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">LicenBase Pricing:</text>
    <text x="25" y="276" font-family="monospace" font-size="12" font-weight="bold" fill="#a7f3d0">From $4.00 / month</text>
    <text x="25" y="296" font-family="sans-serif" font-size="9" fill="#94a3b8">Instant IP automated licensing</text>
  </g>

  <!-- Card 3: Elite / Enterprise -->
  <g transform="translate(650, 100)" filter="url(#shadow)">
    <rect width="265" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
    <rect width="265" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc">Web Host Elite (Uncapped)</text>
    
    <rect x="15" y="55" width="235" height="80" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="76" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Enterprise Scaling:</text>
    <text x="25" y="96" font-family="monospace" font-size="10" fill="#c084fc">&bull; 4, 8, or Uncapped Workers</text>
    <text x="25" y="114" font-family="monospace" font-size="10" fill="#c084fc">&bull; Unlimited Physical RAM</text>

    <rect x="15" y="145" width="235" height="80" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="166" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Performance Edge:</text>
    <text x="25" y="186" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; 10x Apache Throughput</text>
    <text x="25" y="204" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Cuts CPU load by up to 70%</text>

    <rect x="15" y="235" width="235" height="85" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="256" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Full Compatibility:</text>
    <text x="25" y="276" font-family="sans-serif" font-size="10" fill="#a7f3d0">100% .htaccess &amp; rewrite support</text>
    <text x="25" y="294" font-family="sans-serif" font-size="10" fill="#a7f3d0">Native LSCache integration</text>
  </g>
'''
(out_dir / "litespeed-license-comparison-sizing-buying-guide-1.svg").write_text(
    make_svg("LiteSpeed Web Server License Tier Sizing &amp; Comparison", 
             "Worker processes, RAM limitations, and performance tiers for VPS and dedicated nodes", svg4_content),
    encoding="utf-8"
)

# 5. PHP Security & Troubleshooting SVG
svg5_content = '''
  <!-- Layer 1: Web Server Request -->
  <g transform="translate(60, 100)" filter="url(#shadow)">
    <rect width="250" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8">1. Inbound Request Layer</text>
    
    <rect x="15" y="55" width="220" height="80" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Web Server Gateway:</text>
    <text x="25" y="98" font-family="monospace" font-size="10" fill="#38bdf8">cPanel Apache / LiteSpeed</text>
    <text x="25" y="116" font-family="sans-serif" font-size="10" fill="#94a3b8">Dispatches to FastCGI socket</text>

    <rect x="15" y="145" width="220" height="80" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="168" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">WAF &amp; Filtering:</text>
    <text x="25" y="188" font-family="sans-serif" font-size="10" fill="#cbd5e1">Imunify360 Real-Time WAF</text>
    <text x="25" y="206" font-family="sans-serif" font-size="10" fill="#94a3b8">Drops RCE &amp; SQL injection</text>

    <rect x="15" y="235" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="258" font-family="sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1">Socket Communication:</text>
    <text x="25" y="278" font-family="monospace" font-size="9" fill="#7dd3fc">/run/php-fpm/user.sock</text>
    <text x="25" y="296" font-family="sans-serif" font-size="9" fill="#94a3b8">Zero TCP port overhead</text>
  </g>

  <!-- Layer 2: PHP-FPM Master & Pools -->
  <g transform="translate(355, 100)" filter="url(#shadow)">
    <rect width="250" height="340" rx="12" fill="url(#cardEmerald)" stroke="#34d399" stroke-width="1.5"/>
    <rect width="250" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">2. PHP-FPM Pool Engine</text>
    
    <rect x="15" y="55" width="220" height="80" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">Process Sizing Formula:</text>
    <text x="25" y="98" font-family="monospace" font-size="10" fill="#6ee7b7">max_children = RAM / avg_size</text>
    <text x="25" y="116" font-family="sans-serif" font-size="9" fill="#94a3b8">Prevents OOM swap crashes</text>

    <rect x="15" y="145" width="220" height="80" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="168" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a7f3d0">Process Management:</text>
    <text x="25" y="188" font-family="monospace" font-size="10" fill="#6ee7b7">pm = ondemand (Shared)</text>
    <text x="25" y="206" font-family="monospace" font-size="10" fill="#6ee7b7">pm = dynamic (Production)</text>

    <rect x="15" y="235" width="220" height="85" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="258" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Timeout Safeguards:</text>
    <text x="25" y="278" font-family="monospace" font-size="9" fill="#a7f3d0">request_terminate_timeout = 60s</text>
    <text x="25" y="296" font-family="sans-serif" font-size="9" fill="#94a3b8">Kills rogue hanging queries</text>
  </g>

  <!-- Layer 3: CloudLinux Sandbox -->
  <g transform="translate(650, 100)" filter="url(#shadow)">
    <rect width="250" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
    <rect width="250" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc">3. CloudLinux Security Jail</text>
    
    <rect x="15" y="55" width="220" height="80" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">CageFS Virtualized FS:</text>
    <text x="25" y="98" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Isolates /etc/passwd &amp; config</text>
    <text x="25" y="116" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Blocks cross-account leaks</text>

    <rect x="15" y="145" width="220" height="80" rx="8" fill="#1e1b4b" stroke="#3b0764"/>
    <text x="25" y="168" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">LVE Resource Throttling:</text>
    <text x="25" y="188" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; CPU / Memory quota caps</text>
    <text x="25" y="206" font-family="sans-serif" font-size="10" fill="#e9d5ff">&bull; Prevents 508 resource limits</text>

    <rect x="15" y="235" width="220" height="85" rx="8" fill="#022c22" stroke="#065f46"/>
    <text x="25" y="258" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">PHP Hardening Directives:</text>
    <text x="25" y="278" font-family="monospace" font-size="9" fill="#a7f3d0">disable_functions = exec,system</text>
    <text x="25" y="296" font-family="sans-serif" font-size="9" fill="#94a3b8">Prevents shell backdoor execution</text>
  </g>
'''
(out_dir / "php-security-troubleshooting-guide-cpanel-1.svg").write_text(
    make_svg("PHP Security Architecture &amp; PHP-FPM Troubleshooting Blueprint", 
             "FastCGI socket communication, dynamic pool sizing, and CloudLinux CageFS isolation", svg5_content),
    encoding="utf-8"
)

print("Generated all 5 SVG diagrams successfully!")

# -*- coding: utf-8 -*-
"""Generate high-quality 960x480 SVG diagrams for the new 5 SEO blog posts."""
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
    <linearGradient id="cardRed" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#881337" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#3b0717" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg)"/>

  <!-- Title Header -->
  <rect x="0" y="0" width="960" height="76" fill="#0b1329" fill-opacity="0.6"/>
  <line x1="0" y1="76" x2="960" y2="76" stroke="#1e293b" stroke-width="1"/>
  <text x="480" y="34" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">{title}</text>
  <text x="480" y="58" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">{subtitle}</text>

  {content}
</svg>'''

# 1. Cheap Managed VPS with cPanel: Pricing & Server Sizing
svg1 = base_svg(
    "Cheap Managed VPS with cPanel: Hardware & Cost Decision Matrix",
    "Selecting the ideal compute tier, storage type, and licensing model for multi-tenant hosting",
    '''
    <!-- Box 1: Starter Agency Tier -->
    <g transform="translate(50, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Tier 1: Starter Agency</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">Hardware: 2 vCPU / 4GB RAM</text>
      </g>
      <g transform="translate(15, 96)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Storage: 60GB NVMe SSD</text>
      </g>
      <g transform="translate(15, 138)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Capacity: 1 - 5 Client Accounts</text>
      </g>
      <g transform="translate(15, 180)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">cPanel Tier: Admin (5 Accts)</text>
      </g>

      <g transform="translate(15, 240)">
        <rect width="230" height="54" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
        <text x="115" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">VPS Compute: ~$5.50/mo</text>
        <text x="115" y="40" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">cPanel Wholesale: $5.99/mo</text>
      </g>
    </g>

    <!-- Box 2: Growth Business Tier -->
    <g transform="translate(350, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Tier 2: Growth Production</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">Hardware: 4 vCPU / 8GB RAM</text>
      </g>
      <g transform="translate(15, 96)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Storage: 160GB NVMe SSD</text>
      </g>
      <g transform="translate(15, 138)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Capacity: 10 - 30 Client Accounts</text>
      </g>
      <g transform="translate(15, 180)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">cPanel Tier: Pro (30 Accts)</text>
      </g>

      <g transform="translate(15, 240)">
        <rect width="230" height="54" rx="8" fill="#064e3b" stroke="#10b981"/>
        <text x="115" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#ecfdf5" text-anchor="middle">VPS Compute: ~$10.00/mo</text>
        <text x="115" y="40" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">cPanel Wholesale: $5.99/mo</text>
      </g>
    </g>

    <!-- Box 3: High-Density Host -->
    <g transform="translate(650, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#d8b4fe">Tier 3: High-Density VPS</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f3e8ff">Hardware: 8 vCPU / 16GB RAM</text>
      </g>
      <g transform="translate(15, 96)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Storage: 300GB NVMe SSD</text>
      </g>
      <g transform="translate(15, 138)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">Capacity: 50 - 100 Accounts</text>
      </g>
      <g transform="translate(15, 180)">
        <rect width="230" height="36" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">cPanel Tier: Premier Cloud</text>
      </g>

      <g transform="translate(15, 240)">
        <rect width="230" height="54" rx="8" fill="#4c1d95" stroke="#c084fc"/>
        <text x="115" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">VPS Compute: ~$22.00/mo</text>
        <text x="115" y="40" font-family="sans-serif" font-size="11" font-weight="700" fill="#d8b4fe" text-anchor="middle">cPanel Wholesale: $5.99/mo</text>
      </g>
    </g>
    '''
)

# 2. Imunify360 Pricing in 2026: Tier Economics & ROI
svg2 = base_svg(
    "2026 Imunify360 Pricing Tiers & Return on Investment (ROI)",
    "Comprehensive comparison of retail pricing tiers, core feature modules, and wholesale licensing savings",
    '''
    <!-- Box 1: Retail Single User -->
    <g transform="translate(50, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#0284c7" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Single User (1 Account)</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">Retail Price: $12.00 / month</text>
      </g>
      <g transform="translate(15, 94)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; AI Web Application Firewall</text>
      </g>
      <g transform="translate(15, 134)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Real-time malware scanning</text>
      </g>
      <g transform="translate(15, 174)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Proactive PHP Defense</text>
      </g>

      <g transform="translate(15, 230)">
        <rect width="230" height="60" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
        <text x="115" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">LicenBase Wholesale</text>
        <text x="115" y="44" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">$5.99 / mo (50% Off)</text>
      </g>
    </g>

    <!-- Box 2: 30 Users Tier -->
    <g transform="translate(350, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardPurple)" stroke="#c084fc" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#7e22ce" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#d8b4fe">30 Users (Up to 30 Accts)</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f3e8ff">Retail Price: $25.00 / month</text>
      </g>
      <g transform="translate(15, 94)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Herd immunity botnet shield</text>
      </g>
      <g transform="translate(15, 134)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Automated background cleanup</text>
      </g>
      <g transform="translate(15, 174)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; WordPress plugin vulnerability patch</text>
      </g>

      <g transform="translate(15, 230)">
        <rect width="230" height="60" rx="8" fill="#4c1d95" stroke="#c084fc"/>
        <text x="115" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">LicenBase Wholesale</text>
        <text x="115" y="44" font-family="sans-serif" font-size="14" font-weight="700" fill="#d8b4fe" text-anchor="middle">$7.99 / mo (68% Off)</text>
      </g>
    </g>

    <!-- Box 3: Unlimited Users Tier -->
    <g transform="translate(650, 96)" filter="url(#shadow)">
      <rect width="260" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="260" height="40" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Unlimited Users (VPS/Metal)</text>
      
      <g transform="translate(15, 54)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">Retail Price: $45.00 / month</text>
      </g>
      <g transform="translate(15, 94)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Unlimited cPanel accounts</text>
      </g>
      <g transform="translate(15, 134)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Centralized WHM security UI</text>
      </g>
      <g transform="translate(15, 174)">
        <rect width="230" height="34" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="22" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Zero manual cleanup tickets</text>
      </g>

      <g transform="translate(15, 230)">
        <rect width="230" height="60" rx="8" fill="#064e3b" stroke="#10b981"/>
        <text x="115" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#ecfdf5" text-anchor="middle">LicenBase Wholesale</text>
        <text x="115" y="44" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399" text-anchor="middle">$8.99 / mo (80% Off)</text>
      </g>
    </g>
    '''
)

# 3. cPanel VPS Hosting: Requirements & Total Cost
svg3 = base_svg(
    "cPanel VPS Hosting: Hardware Requirements & Stack Architecture",
    "Minimum vs recommended production baseline, hypervisor compatibility, and performance addons",
    '''
    <!-- Box 1: Hardware Baseline -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#0284c7" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Hardware &amp; Hypervisor Baseline</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">Architecture: 64-bit Linux (AlmaLinux 8/9, Rocky 8/9)</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">Minimum: 2 vCPU / 4GB RAM | Recommended: 4 vCPU / 8GB RAM</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">Storage: 40GB minimum, 100GB+ NVMe PCIe recommended</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">Hypervisors: KVM, Proxmox VE, VMware ESXi, Xen HVM</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">Average Cloud Compute Cost</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">Hetzner / Contabo / OVH: $5.50 - $12.00 / mo</text>
      </g>
    </g>

    <!-- Box 2: Total Cost Stack -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Production Software Stack &amp; Total Cost</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">cPanel Cloud License: $5.99/mo (LicenBase Wholesale)</text>
      </g>
      <g transform="translate(20, 102)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">LiteSpeed Web Server: $5.99/mo (Replaces slow Apache)</text>
      </g>
      <g transform="translate(20, 148)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">CloudLinux OS: $5.99/mo (CageFS tenant security jail)</text>
      </g>
      <g transform="translate(20, 194)">
        <rect width="350" height="38" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">CSF Firewall &amp; Automated Cron: $0.00/mo (Free included)</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#022c22" stroke="#10b981"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#ecfdf5" text-anchor="middle">All-Inclusive Production Stack</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Under $30 / mo (vs $180/mo retail managed hosts)</text>
      </g>
    </g>
    '''
)

# 4. CloudLinux License Not Detected: Diagnostics Pipeline
svg4 = base_svg(
    "CloudLinux License Not Detected: Diagnostic & Recovery Pipeline",
    "Systematic resolution path from network verification and clock synchronization to clnreg_ks re-registration",
    '''
    <!-- Step 1: Network Check -->
    <g transform="translate(50, 150)" filter="url(#shadow)">
      <rect width="180" height="220" rx="10" fill="url(#cardBlue)" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="90" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1. Outbound TLS</text>
      <rect x="15" y="50" width="150" height="40" rx="6" fill="#0f172a"/>
      <text x="90" y="74" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle">curl -Iv https://cln...:443</text>
      
      <text x="15" y="116" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Verifies TCP 443 out</text>
      <text x="15" y="136" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Cloud firewall rules</text>
      <text x="15" y="156" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; DNS resolution check</text>
      <text x="15" y="176" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Unblocks port 443</text>
    </g>

    <!-- Arrow 1 to 2 -->
    <path d="M 235 260 L 275 260" stroke="#60a5fa" stroke-width="2.5"/>
    <text x="255" y="250" font-family="sans-serif" font-size="11" fill="#93c5fd" text-anchor="middle">Pass</text>

    <!-- Step 2: System Clock -->
    <g transform="translate(280, 150)" filter="url(#shadow)">
      <rect width="190" height="220" rx="10" fill="url(#cardPurple)" stroke="#a855f7" stroke-width="1.5"/>
      <text x="95" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">2. NTP Clock Sync</text>
      <rect x="15" y="50" width="160" height="52" rx="6" fill="#0f172a"/>
      <text x="20" y="70" font-family="monospace" font-size="10" fill="#e9d5ff">chronyc tracking</text>
      <text x="20" y="90" font-family="monospace" font-size="10" fill="#e9d5ff">chronyc makestep</text>

      <text x="15" y="128" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Checks clock drift</text>
      <text x="15" y="148" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; SSL cert validity</text>
      <text x="15" y="168" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Fixes token rejects</text>
      <text x="15" y="188" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Re-syncs NTP pool</text>
    </g>

    <!-- Arrow 2 to 3 -->
    <path d="M 475 260 L 515 260" stroke="#c084fc" stroke-width="2.5"/>
    <text x="495" y="250" font-family="sans-serif" font-size="11" fill="#d8b4fe" text-anchor="middle">Pass</text>

    <!-- Step 3: Registration & Diagnostic -->
    <g transform="translate(520, 150)" filter="url(#shadow)">
      <rect width="190" height="220" rx="10" fill="url(#cardAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="95" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24" text-anchor="middle">3. CLN Registration</text>
      <rect x="15" y="50" width="160" height="52" rx="6" fill="#0f172a"/>
      <text x="20" y="70" font-family="monospace" font-size="10" fill="#fde68a">clnreg_ks --force</text>
      <text x="20" y="90" font-family="monospace" font-size="10" fill="#fde68a">cldiag --check-license</text>

      <text x="15" y="128" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Registers server IP</text>
      <text x="15" y="148" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Refreshes jwt token</text>
      <text x="15" y="168" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Validates systemid</text>
      <text x="15" y="188" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Tests LVE module</text>
    </g>

    <!-- Arrow 3 to 4 -->
    <path d="M 715 260 L 755 260" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="735" y="250" font-family="sans-serif" font-size="11" fill="#fde68a" text-anchor="middle">OK</text>

    <!-- Step 4: Verification -->
    <g transform="translate(760, 150)" filter="url(#shadow)">
      <rect width="150" height="220" rx="10" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <text x="75" y="32" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">4. Active License</text>
      <rect x="15" y="50" width="120" height="40" rx="6" fill="#0f172a"/>
      <text x="75" y="74" font-family="sans-serif" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">LVE / CageFS OK</text>

      <text x="12" y="116" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; cPanel WHM synced</text>
      <text x="12" y="136" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; Green status badge</text>
      <text x="12" y="156" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; LVE Manager active</text>
      <text x="12" y="176" font-family="sans-serif" font-size="11" fill="#cbd5e1">&bull; MySQL Governor on</text>
    </g>
    '''
)

# 5. PHP Critical RCE CVE-2026: Exploit Anatomy & Hardening
svg5 = base_svg(
    "PHP Critical RCE (CVE-2026-109618 & 109619): Vulnerability Anatomy & Fix",
    "Stream filter buffer overflow & multipart parser heap corruption mitigation on production servers",
    '''
    <!-- Box 1: Threat Model -->
    <g transform="translate(60, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardRed)" stroke="#f43f5e" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#e11d48" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#fda4af">Vulnerability Exploit Mechanism</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#fca5a5">CVE-2026-109618 (CVSS 9.8 Critical)</text>
        <text x="12" y="36" font-family="sans-serif" font-size="10" fill="#cbd5e1">Buffer overflow via php://filter stream wrappers &amp; iconv chains</text>
      </g>
      <g transform="translate(20, 108)">
        <rect width="350" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#fca5a5">CVE-2026-109619 (CVSS 9.4 Critical)</text>
        <text x="12" y="36" font-family="sans-serif" font-size="10" fill="#cbd5e1">Heap corruption in PHP multipart/form-data boundary parsing</text>
      </g>
      <g transform="translate(20, 160)">
        <rect width="350" height="66" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#fca5a5">Exploit Impact:</text>
        <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#cbd5e1">&bull; Unauthenticated remote code execution (RCE)</text>
        <text x="12" y="54" font-family="sans-serif" font-size="10" fill="#cbd5e1">&bull; Direct web shell injection bypassing standard login</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#4c0519" stroke="#f43f5e"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">Affected PHP Versions</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#fda4af" text-anchor="middle">All PHP 8.1, 8.2, 8.3 &amp; 8.4 builds prior to patch</text>
      </g>
    </g>

    <!-- Box 2: Mitigation Defense -->
    <g transform="translate(510, 96)" filter="url(#shadow)">
      <rect width="390" height="340" rx="12" fill="url(#cardGreen)" stroke="#10b981" stroke-width="1.5"/>
      <rect width="390" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
      <text x="20" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399">Patching &amp; Multi-Layer Hardening</text>
      
      <g transform="translate(20, 56)">
        <rect width="350" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">1. Control Panel EasyApache 4 / CloudLinux Patch</text>
        <text x="12" y="36" font-family="monospace" font-size="10" fill="#6ee7b7">yum clean all &amp;&amp; yum update -y ea-php*</text>
      </g>
      <g transform="translate(20, 108)">
        <rect width="350" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">2. Immediate php.ini Stream Wrapper Lockdown</text>
        <text x="12" y="36" font-family="monospace" font-size="10" fill="#6ee7b7">allow_url_include = Off | disable_functions = ...</text>
      </g>
      <g transform="translate(20, 160)">
        <rect width="350" height="66" rx="6" fill="#0f172a" stroke="#1e293b"/>
        <text x="12" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#ecfdf5">3. Virtual Patching &amp; Jail Isolation:</text>
        <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#cbd5e1">&bull; Imunify360 WAF rule #334091 drops stream payloads</text>
        <text x="12" y="54" font-family="sans-serif" font-size="10" fill="#cbd5e1">&bull; CloudLinux CageFS blocks traversal if shell spawns</text>
      </g>

      <g transform="translate(20, 246)">
        <rect width="350" height="54" rx="8" fill="#022c22" stroke="#10b981"/>
        <text x="175" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#ecfdf5" text-anchor="middle">Status: Fully Mitigated</text>
        <text x="175" y="41" font-family="sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Zero downtime updates across all active PHP pools</text>
      </g>
    </g>
    '''
)

svgs = {
    "cheap-managed-vps-with-cpanel-pricing-server-guide-1.svg": svg1,
    "imunify360-pricing-2026-license-costs-features-guide-1.svg": svg2,
    "cpanel-vps-hosting-requirements-licensing-cost-guide-1.svg": svg3,
    "cloudlinux-license-not-detected-cpanel-diagnostics-guide-1.svg": svg4,
    "php-critical-rce-cve-2026-109618-server-security-guide-1.svg": svg5,
}

for name, content in svgs.items():
    p = out_dir / name
    p.write_text(content.strip(), encoding="utf-8")
    print(f"Generated {p} ({p.stat().st_size} bytes)")

print("All 5 new SVGs generated successfully.")

import os
from pathlib import Path

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="cardGsc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardPillar" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardHub" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="500" fill="url(#bg)"/>

  <!-- Main Title -->
  <text x="480" y="38" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">LicenBase SEO Keyword Strategy &amp; Linking Topology</text>
  <text x="480" y="62" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Google Search Console Data Insights &bull; 5 High-Intent Topic Pillars &bull; Commercial Hub Architecture</text>

  <!-- Left: GSC Data Signals -->
  <g transform="translate(40, 90)" filter="url(#shadow)">
    <rect width="250" height="375" rx="12" fill="url(#cardGsc)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="12" fill="#0284c7" fill-opacity="0.2"/>
    <circle cx="24" cy="19" r="6" fill="#38bdf8"/>
    <text x="38" y="24" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8">GSC Performance Data</text>

    <!-- Query 1 -->
    <rect x="14" y="48" width="222" height="56" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="22" y="67" font-family="sans-serif" font-size="11" font-weight="700" fill="#f1f5f9">Imunify360 Pricing</text>
    <text x="22" y="83" font-family="monospace" font-size="10" fill="#38bdf8">121 Imp | Pos 14.17 (Striking)</text>
    <text x="22" y="96" font-family="sans-serif" font-size="9" fill="#94a3b8">Action: Expand pricing &amp; product links</text>

    <!-- Query 2 -->
    <rect x="14" y="112" width="222" height="56" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="22" y="131" font-family="sans-serif" font-size="11" font-weight="700" fill="#f1f5f9">cPanel Cost Breakdown</text>
    <text x="22" y="147" font-family="monospace" font-size="10" fill="#f59e0b">204 Imp | Pos 74.02 (Broad)</text>
    <text x="22" y="160" font-family="sans-serif" font-size="9" fill="#94a3b8">Action: Intent match &amp; VPS sizing</text>

    <!-- Query 3 -->
    <rect x="14" y="176" width="222" height="56" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="22" y="195" font-family="sans-serif" font-size="11" font-weight="700" fill="#f1f5f9">cPanel Webmail Ports</text>
    <text x="22" y="211" font-family="monospace" font-size="10" fill="#10b981">154 Imp | Pos 5.82 (Page 1)</text>
    <text x="22" y="224" font-family="sans-serif" font-size="9" fill="#94a3b8">Action: Optimize Title/Meta for CTR</text>

    <!-- Query 4 & 5 -->
    <rect x="14" y="240" width="222" height="56" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="22" y="259" font-family="sans-serif" font-size="11" font-weight="700" fill="#f1f5f9">cPanel VPS / LiteSpeed</text>
    <text x="22" y="275" font-family="monospace" font-size="10" fill="#a855f7">67 &amp; 34 Imp | Pos 83 &amp; 41</text>
    <text x="22" y="288" font-family="sans-serif" font-size="9" fill="#94a3b8">Action: Tier comparisons &amp; specs</text>

    <!-- Query 6 -->
    <rect x="14" y="304" width="222" height="56" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="22" y="323" font-family="sans-serif" font-size="11" font-weight="700" fill="#f1f5f9">PHP-FPM Troubleshooting</text>
    <text x="22" y="339" font-family="monospace" font-size="10" fill="#10b981">30 Imp | Pos 9.10 (Top 10)</text>
    <text x="22" y="352" font-family="sans-serif" font-size="9" fill="#94a3b8">Action: Link from server tuning hub</text>
  </g>

  <!-- Connectors from Data to Pillars -->
  <path d="M 290, 150 L 350, 150" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
  <path d="M 290, 275 L 350, 275" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
  <path d="M 290, 390 L 350, 390" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3" fill="none"/>

  <!-- Middle: 5 Content Pillars -->
  <g transform="translate(350, 90)" filter="url(#shadow)">
    <rect width="260" height="375" rx="12" fill="url(#cardPillar)" stroke="#60a5fa" stroke-width="1.5"/>
    <rect width="260" height="38" rx="12" fill="#2563eb" fill-opacity="0.25"/>
    <circle cx="24" cy="19" r="6" fill="#60a5fa"/>
    <text x="38" y="24" font-family="sans-serif" font-size="13" font-weight="700" fill="#93c5fd">5 Strategic Content Pillars</text>

    <!-- Pillar 1 -->
    <rect x="14" y="48" width="232" height="56" rx="6" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="22" y="68" font-family="sans-serif" font-size="11" font-weight="700" fill="#bfdbfe">1. Imunify360 Pricing ROI Guide</text>
    <text x="22" y="86" font-family="sans-serif" font-size="10" fill="#93c5fd">Tiers &bull; Standalone vs Stack &bull; ROI</text>

    <!-- Pillar 2 -->
    <rect x="14" y="112" width="232" height="56" rx="6" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="22" y="132" font-family="sans-serif" font-size="11" font-weight="700" fill="#bfdbfe">2. cPanel VPS Hardware Blueprint</text>
    <text x="22" y="150" font-family="sans-serif" font-size="10" fill="#93c5fd">VPS vs Metal &bull; RAM Sizing &bull; TCO</text>

    <!-- Pillar 3 -->
    <rect x="14" y="176" width="232" height="56" rx="6" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="22" y="196" font-family="sans-serif" font-size="11" font-weight="700" fill="#bfdbfe">3. Webmail Ports &amp; SSL CTR Hub</text>
    <text x="22" y="214" font-family="sans-serif" font-size="10" fill="#93c5fd">Ports 2095/2096 &bull; Firewall Rules</text>

    <!-- Pillar 4 -->
    <rect x="14" y="240" width="232" height="56" rx="6" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="22" y="260" font-family="sans-serif" font-size="11" font-weight="700" fill="#bfdbfe">4. LiteSpeed Tier Sizing Guide</text>
    <text x="22" y="278" font-family="sans-serif" font-size="10" fill="#93c5fd">Worker Limits &bull; LSCache &bull; Costs</text>

    <!-- Pillar 5 -->
    <rect x="14" y="304" width="232" height="56" rx="6" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="22" y="324" font-family="sans-serif" font-size="11" font-weight="700" fill="#bfdbfe">5. PHP-FPM Optimization Blueprint</text>
    <text x="22" y="342" font-family="sans-serif" font-size="10" fill="#93c5fd">Pool Sizing &bull; CageFS &bull; Zero Crashing</text>
  </g>

  <!-- Connectors from Pillars to Product Hub -->
  <path d="M 610, 150 L 670, 150" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
  <path d="M 610, 275 L 670, 275" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
  <path d="M 610, 390 L 670, 390" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3" fill="none"/>

  <!-- Right: Commercial Conversion Hub & Internal Links -->
  <g transform="translate(670, 90)" filter="url(#shadow)">
    <rect width="250" height="375" rx="12" fill="url(#cardHub)" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="12" fill="#059669" fill-opacity="0.25"/>
    <circle cx="24" cy="19" r="6" fill="#10b981"/>
    <text x="38" y="24" font-family="sans-serif" font-size="13" font-weight="700" fill="#6ee7b7">Commercial Hub &amp; Conversion</text>

    <!-- Money Page 1 -->
    <rect x="14" y="48" width="222" height="56" rx="6" fill="#022c22" stroke="#065f46"/>
    <text x="22" y="68" font-family="sans-serif" font-size="11" font-weight="700" fill="#a7f3d0">/cpanel-license</text>
    <text x="22" y="86" font-family="sans-serif" font-size="10" fill="#6ee7b7">Target: Cloud &amp; Dedicated Licenses</text>

    <!-- Money Page 2 -->
    <rect x="14" y="112" width="222" height="56" rx="6" fill="#022c22" stroke="#065f46"/>
    <text x="22" y="132" font-family="sans-serif" font-size="11" font-weight="700" fill="#a7f3d0">/imunify360-license</text>
    <text x="22" y="150" font-family="sans-serif" font-size="10" fill="#6ee7b7">Target: Unlimited Malware Defense</text>

    <!-- Money Page 3 -->
    <rect x="14" y="176" width="222" height="56" rx="6" fill="#022c22" stroke="#065f46"/>
    <text x="22" y="196" font-family="sans-serif" font-size="11" font-weight="700" fill="#a7f3d0">/litespeed-license</text>
    <text x="22" y="214" font-family="sans-serif" font-size="10" fill="#6ee7b7">Target: 2, 4, 8 Worker Web Acceleration</text>

    <!-- Money Page 4 -->
    <rect x="14" y="240" width="222" height="56" rx="6" fill="#022c22" stroke="#065f46"/>
    <text x="22" y="260" font-family="sans-serif" font-size="11" font-weight="700" fill="#a7f3d0">/cloudlinux-license &amp; /deals</text>
    <text x="22" y="278" font-family="sans-serif" font-size="10" fill="#6ee7b7">Target: Multi-Tenant &amp; Combo Deals</text>

    <!-- Trust Links -->
    <rect x="14" y="304" width="222" height="56" rx="6" fill="#022c22" stroke="#065f46"/>
    <text x="22" y="324" font-family="sans-serif" font-size="11" font-weight="700" fill="#a7f3d0">Trust &amp; Compliance</text>
    <text x="22" y="342" font-family="sans-serif" font-size="10" fill="#6ee7b7">/about &bull; /contact &bull; /refund-policy</text>
  </g>
</svg>
'''

out_path = Path("assets/img/blog/licenbase-5-seo-blog-topics-content-linking-plans-1.svg")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(svg_content.strip(), encoding="utf-8")
print(f"SVG written to {out_path} ({len(svg_content)} bytes)")

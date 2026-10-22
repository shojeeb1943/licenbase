import os

# 1. cPanel to DirectAdmin Migration SVG
svg_da = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgDA" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0b172a"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shDA" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgDA)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">cPanel to DirectAdmin Migration Pipeline</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Automated backup conversion, user-data mapping, and zero-downtime DNS cutover</text>

  <!-- Step 1: Backup on cPanel -->
  <g transform="translate(50, 105)" filter="url(#shDA)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0369a1" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1. cPanel Source Extraction</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#7dd3fc" font-weight="bold">/scripts/pkgacct username</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Creates full uncompressed or gzip cpmove-username.tar.gz archive.</text>
    <rect x="15" y="125" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Extracted Data:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• MySQL/MariaDB databases</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Dovecot/Maildir email accounts</text>
    <rect x="15" y="210" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="232" font-family="monospace" font-size="10" fill="#38bdf8">rsync -avz /backup/cpmove-* \</text>
    <text x="25" y="252" font-family="monospace" font-size="10" fill="#38bdf8">root@da-server:/home/admin/</text>
  </g>

  <!-- Step 2: Conversion in DA -->
  <g transform="translate(355, 105)" filter="url(#shDA)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#7e22ce" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">2. DirectAdmin Converter</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#d8b4fe" font-weight="bold">da-cpanel-migration tool</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Translates cPanel directory hierarchy into DirectAdmin user structure.</text>
    <rect x="15" y="125" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Structural Conversion:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• public_html -> domains/domain/public_html</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• cPanel cronjobs -> DA crontab</text>
    <rect x="15" y="210" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="232" font-family="monospace" font-size="10" fill="#c084fc">/usr/local/directadmin/scripts/</text>
    <text x="25" y="252" font-family="monospace" font-size="10" fill="#c084fc">cpanel_to_da/cpanel_to_da.sh</text>
  </g>

  <!-- Step 3: Restore & Cutover -->
  <g transform="translate(660, 105)" filter="url(#shDA)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">3. Restore &amp; DNS Cutover</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#6ee7b7" font-weight="bold">Admin Backup/Restore in DA</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Provisions users, maps SSL certificates, and starts services.</text>
    <rect x="15" y="125" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Zero-Downtime Actions:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Reduce TTL to 300s 24h prior</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Final delta rsync of mailboxes</text>
    <rect x="15" y="210" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="232" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Total Cost Advantage:</text>
    <text x="25" y="252" font-family="sans-serif" font-size="10" fill="#cbd5e1">Save 60-70% on monthly licensing with DirectAdmin VPS.</text>
  </g>

  <rect x="50" y="435" width="860" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="70" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">DirectAdmin Licensing:</text>
  <text x="220" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">Get instant automated DirectAdmin licenses for VPS &amp; Bare-Metal at LicenBase.</text>
</svg>'''

# 2. LiteSpeed Worker Sizing SVG
svg_worker = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgWk" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0a1120"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shWk" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgWk)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">LiteSpeed Web Server Worker Architecture &amp; Sizing</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Understanding LSWS event-driven worker processes vs CPU cores and concurrency</text>

  <!-- 3 Sizing Tiers -->
  <g transform="translate(60, 105)" filter="url(#shWk)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1-Worker License</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">Hardware: 1 - 2 vCPUs</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Single event-driven I/O loop handling up to 10,000 concurrent HTTP keep-alives.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Optimal Use Cases:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Small agency / personal VPS</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Up to 50 active WordPress sites</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#082f49"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#38bdf8">LiteSpeed Starter / VPS</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">RAM footprint: &lt; 50MB for core daemon</text>
  </g>

  <g transform="translate(355, 105)" filter="url(#shWk)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">2-Worker License</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d8b4fe">Hardware: 4 - 8 vCPUs</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Two discrete worker processes distributing network I/O and SSL handshake decryption.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Optimal Use Cases:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• High-traffic WooCommerce</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Medium shared hosting node</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#2e1065"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#c084fc">LiteSpeed Web Host Elite</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Ideal sweet spot for price/performance</text>
  </g>

  <g transform="translate(650, 105)" filter="url(#shWk)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">4 to 8-Worker License</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">Hardware: 16+ Cores Dedicated</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Enterprise parallel worker pools with multi-queue NIC affinity for line-rate 10Gbps+ throughput.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Optimal Use Cases:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Mega shared hosting bare-metal</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• News &amp; viral publishing portals</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#064e3b"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#34d399">LiteSpeed Ultra / Enterprise</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Full multi-core CPU utilization</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">LSAPI Note:</text>
  <text x="160" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">PHP workers (LSPHP) are managed separately and dynamically scale up regardless of LSWS core worker tier.</text>
</svg>'''

# 3. Shared vs Dedicated IP SVG
svg_ip = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgIP" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0e1726"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shIP" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgIP)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">cPanel Shared vs Dedicated IP Comparison Matrix</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Evaluating modern SEO, SSL/SNI requirements, and outbound email deliverability</text>

  <!-- Left: Shared IP -->
  <g transform="translate(60, 105)" filter="url(#shIP)">
    <rect width="390" height="315" rx="14" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="390" height="40" rx="14" fill="#334155"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#f8fafc" text-anchor="middle">Shared IP Address (Default)</text>

    <rect x="20" y="55" width="350" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="78" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Web &amp; SSL (SNI Technology):</text>
    <text x="30" y="98" font-family="sans-serif" font-size="11" fill="#cbd5e1">Server Name Indication (SNI) enables hundreds of unique SSL certs on one IP. No dedicated IP needed!</text>

    <rect x="20" y="135" width="350" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="158" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">2. Search Engine Optimization (SEO):</text>
    <text x="30" y="178" font-family="sans-serif" font-size="11" fill="#cbd5e1">Google explicitly confirms shared IPs do not harm SEO rankings. Hostname &amp; content are what rank.</text>

    <rect x="20" y="215" width="350" height="85" rx="8" fill="#450a0a" stroke="#f43f5e"/>
    <text x="30" y="238" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fecaca">3. Email Deliverability Risk:</text>
    <text x="30" y="258" font-family="sans-serif" font-size="11" fill="#fee2e2">Neighboring compromised accounts sending spam can blacklist the shared IP on Spamhaus/Proofpoint.</text>
  </g>

  <!-- Right: Dedicated IP -->
  <g transform="translate(510, 105)" filter="url(#shIP)">
    <rect width="390" height="315" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="390" height="40" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399" text-anchor="middle">Dedicated IP Address</text>

    <rect x="20" y="55" width="350" height="70" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="78" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">1. Total Mail Reputation Control:</text>
    <text x="30" y="98" font-family="sans-serif" font-size="11" fill="#cbd5e1">Isolated rDNS (PTR), SPF, and DKIM. No noisy neighbor spam can burn your sender score.</text>

    <rect x="20" y="135" width="350" height="70" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="158" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Enterprise Security &amp; Compliance:</text>
    <text x="30" y="178" font-family="sans-serif" font-size="11" fill="#cbd5e1">Required for custom payment gateways, financial APIs, and IP-whitelisted banking firewalls.</text>

    <rect x="20" y="215" width="350" height="85" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="30" y="238" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">3. Direct WHM IP Delegation:</text>
    <text x="30" y="258" font-family="sans-serif" font-size="11" fill="#cbd5e1">Configured in WHM "Change Site's IP Address" or assigned directly via WHMCS automated billing.</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">The Modern Consensus:</text>
  <text x="240" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">Shared IP is fine for web traffic; dedicated IP is critical for high-volume transactional email.</text>
</svg>'''

# 4. Bandwidth Monitoring SVG
svg_bw_tools = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgBW" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0b172a"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shBW" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgBW)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Linux VPS Real-Time Bandwidth Monitoring Toolkit</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Comparing iftop, vnStat, nload, and bmon for live network packet inspection</text>

  <!-- 3 Tools -->
  <g transform="translate(60, 105)" filter="url(#shBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">iftop (Socket Level)</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#7dd3fc" font-weight="bold">Command: iftop -i eth0</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Top-like display of bandwidth per active host pair and port connections.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Best For:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Identifying DDoS attack sources</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Pinpointing rogue outbound uploads</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#082f49"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#38bdf8">Key Flag: iftop -P -N</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Shows exact port numbers &amp; IPs</text>
  </g>

  <g transform="translate(355, 105)" filter="url(#shBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">vnStat (Historical Log)</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#6ee7b7" font-weight="bold">Command: vnstat -d / -m</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Daemon-backed network logger that tracks hourly, daily, and monthly transfer totals.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Best For:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Over-quota billing verification</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Monthly bandwidth auditing</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#064e3b"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#34d399">Zero CPU Overhead</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Reads kernel interface statistics</text>
  </g>

  <g transform="translate(650, 105)" filter="url(#shBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#b45309" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24" text-anchor="middle">nload (Visual ASCII)</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#fde68a" font-weight="bold">Command: nload eth0</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Real-time ASCII bar graphs showing current, average, and peak inbound/outbound rates.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Best For:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Live throughput verification</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Immediate NIC saturation check</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#451a03"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#fbbf24">Units: MBit/s or MB/s</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Toggle units via shortcut keys</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Install All via Package Manager:</text>
  <text x="320" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">dnf install epel-release &amp;&amp; dnf install iftop vnstat nload</text>
</svg>'''

# 5. Which cPanel Account Using Most Bandwidth SVG
svg_cpanel_bw = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgCBW" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0a1220"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shCBW" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgCBW)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">cPanel Account Bandwidth Investigation Workflow</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Triage bandwidth spikes from WHM GUI, Apache access logs, and cPanel RRD databases</text>

  <g transform="translate(60, 105)" filter="url(#shCBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1. WHM GUI View</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">WHM &raquo; Account Information</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">View Bandwidth Usage tool displays aggregated monthly megabytes per user.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Protocol Breakdown:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• HTTP / HTTPS Web</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• IMAP / POP3 / SMTP Mail</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#082f49"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#38bdf8">Limits &amp; Throttling</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Auto-suspend or email notice</text>
  </g>

  <g transform="translate(355, 105)" filter="url(#shCBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#7e22ce" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">2. CLI Log Parsing</text>
    <text x="18" y="65" font-family="monospace" font-size="11" fill="#d8b4fe" font-weight="bold">/usr/local/apache/domlogs/</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Inspect domain transfer logs to find massive file downloads or video hotlinking.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Log Analysis Command:</text>
    <text x="25" y="168" font-family="monospace" font-size="10" fill="#cbd5e1">du -sh /var/log/apache2/domlogs/*</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">Identifies top active domain log</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#2e1065"/>
    <text x="25" y="245" font-family="monospace" font-size="11" fill="#c084fc">awk '{s+=$10} END {print s/1024/1024 " MB"}' log</text>
  </g>

  <g transform="translate(650, 105)" filter="url(#shCBW)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">3. Mitigation &amp; Fixes</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">Permanent Defenses</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Prevent sudden bandwidth overage charges with targeted server policies.</text>
    <rect x="15" y="125" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="148" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Actions:</text>
    <text x="25" y="168" font-family="sans-serif" font-size="10" fill="#94a3b8">• Block image hotlinking via .htaccess</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#94a3b8">• Route static assets through Cloudflare</text>
    <rect x="15" y="220" width="220" height="80" rx="8" fill="#064e3b"/>
    <text x="25" y="245" font-family="sans-serif" font-size="11" fill="#34d399" font-weight="bold">CloudLinux Network Bandwidth</text>
    <text x="25" y="265" font-family="sans-serif" font-size="10" fill="#cbd5e1">Enforce per-user Mbit/s throttling</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#fbbf24" font-weight="bold">Fast Terminal Check:</text>
  <text x="250" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">whmapi1 showbw | grep -E "user|totalbytes"</text>
</svg>'''

# 6. Cheapest Way to Run cPanel VPS SVG
svg_cheap_vps = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgCV" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#071322"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shCV" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgCV)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Cheapest cPanel VPS Architecture &amp; Cost Optimization</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Comparing retail hosting stacks against optimized wholesale infrastructure for startups</text>

  <!-- Retail vs Wholesale -->
  <g transform="translate(60, 105)" filter="url(#shCV)">
    <rect width="390" height="315" rx="14" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="390" height="40" rx="14" fill="#991b1b" fill-opacity="0.25"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#fca5a5" text-anchor="middle">Retail Traditional Pricing ($75+/mo)</text>
    <rect x="20" y="55" width="350" height="45" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="82" font-family="sans-serif" font-size="11" fill="#cbd5e1">VPS Compute (4GB RAM, 2 vCPU): <tspan fill="#fca5a5" font-weight="bold">$20.00/mo</tspan></text>
    <rect x="20" y="110" width="350" height="45" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="137" font-family="sans-serif" font-size="11" fill="#cbd5e1">cPanel Admin (5 accounts) Retail: <tspan fill="#fca5a5" font-weight="bold">$31.99/mo</tspan></text>
    <rect x="20" y="165" width="350" height="45" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="192" font-family="sans-serif" font-size="11" fill="#cbd5e1">LiteSpeed + Softaculous: <tspan fill="#fca5a5" font-weight="bold">$25.00/mo</tspan></text>
    <rect x="20" y="225" width="350" height="70" rx="6" fill="#450a0a"/>
    <text x="195" y="255" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fecaca" text-anchor="middle">Total Monthly Burn: $76.99/mo</text>
    <text x="195" y="278" font-family="sans-serif" font-size="11" fill="#fee2e2" text-anchor="middle">Over $920/year before hosting a single paying client!</text>
  </g>

  <g transform="translate(510, 105)" filter="url(#shCV)">
    <rect width="390" height="315" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="390" height="40" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399" text-anchor="middle">LicenBase Wholesale Stack ($17/mo)</text>
    <rect x="20" y="55" width="350" height="45" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="82" font-family="sans-serif" font-size="11" fill="#cbd5e1">Unmanaged VPS (Hetzner / Netcup): <tspan fill="#34d399" font-weight="bold">$7.00/mo</tspan></text>
    <rect x="20" y="110" width="350" height="45" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="137" font-family="sans-serif" font-size="11" fill="#cbd5e1">LicenBase Automated cPanel License: <tspan fill="#34d399" font-weight="bold">$6.00/mo</tspan></text>
    <rect x="20" y="165" width="350" height="45" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="192" font-family="sans-serif" font-size="11" fill="#cbd5e1">LicenBase LiteSpeed + Softaculous: <tspan fill="#34d399" font-weight="bold">$4.50/mo</tspan></text>
    <rect x="20" y="225" width="350" height="70" rx="6" fill="#064e3b"/>
    <text x="195" y="255" font-family="sans-serif" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Total Monthly Stack: $17.50/mo</text>
    <text x="195" y="278" font-family="sans-serif" font-size="11" fill="#d1fae5" text-anchor="middle">77% Savings! Reclaim full margins for your business.</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">Start Today:</text>
  <text x="175" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">Instant automated IP activation across all licenses with zero setup fees at LicenBase.</text>
</svg>'''

# 7. Web Hosts India & Southeast Asia SVG
svg_asia = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgAS" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#081426"/><stop offset="100%" stop-color="#020617"/></linearGradient>
    <filter id="shAS" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <rect width="960" height="480" fill="url(#bgAS)"/>
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Emerging Markets Software Licensing Strategy: India &amp; Southeast Asia</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Navigating USD currency fluctuations, competitive shared hosting ARPU, and wholesale licensing</text>

  <!-- 3 Regional Pillars -->
  <g transform="translate(60, 105)" filter="url(#shAS)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#b45309" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24" text-anchor="middle">1. The Macro Challenge</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fde68a">USD vs INR / IDR / BDT</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Local retail hosting prices are priced in domestic fiat, while retail licenses are billed in expensive US Dollars.</text>
    <rect x="15" y="135" width="220" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="157" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">ARPU Constraints:</text>
    <text x="25" y="177" font-family="sans-serif" font-size="10" fill="#94a3b8">• Shared plans sell for $1 - $3/mo</text>
    <text x="25" y="195" font-family="sans-serif" font-size="10" fill="#94a3b8">• Retail cPanel license wipes margins!</text>
  </g>

  <g transform="translate(355, 105)" filter="url(#shAS)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">2. Architectural Tactics</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">Maximizing Node Density</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Deploy CloudLinux OS + LiteSpeed Web Server to achieve 3x customer density per node.</text>
    <rect x="15" y="135" width="220" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="157" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Multi-Panel Offerings:</text>
    <text x="25" y="177" font-family="sans-serif" font-size="10" fill="#94a3b8">• Offer cPanel for premium users</text>
    <text x="25" y="195" font-family="sans-serif" font-size="10" fill="#94a3b8">• DirectAdmin / Webuzo for budget users</text>
  </g>

  <g transform="translate(650, 105)" filter="url(#shAS)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">3. Wholesale Procurement</text>
    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">LicenBase Provider Partner</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Source licenses through automated bulk distribution with predictable, low-cost pricing.</text>
    <rect x="15" y="135" width="220" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="157" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Key Advantages:</text>
    <text x="25" y="177" font-family="sans-serif" font-size="10" fill="#94a3b8">• Instant IP-based automated updates</text>
    <text x="25" y="195" font-family="sans-serif" font-size="10" fill="#94a3b8">• Flexible billing &amp; bundle stacks</text>
  </g>

  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">Regional Support:</text>
  <text x="200" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">LicenBase supports web hosts across India, Bangladesh, Indonesia, Pakistan, Vietnam, and Malaysia.</text>
</svg>'''

files = [
    ('assets/img/blog/migrate-cpanel-to-directadmin-without-data-loss-1.svg', svg_da),
    ('assets/img/blog/litespeed-worker-sizing-how-many-workers-vps-1.svg', svg_worker),
    ('assets/img/blog/cpanel-shared-vs-dedicated-ip-seo-email-1.svg', svg_ip),
    ('assets/img/blog/monitor-linux-vps-bandwidth-real-time-iftop-vnstat-1.svg', svg_bw_tools),
    ('assets/img/blog/find-cpanel-account-using-most-bandwidth-guide-1.svg', svg_cpanel_bw),
    ('assets/img/blog/cheapest-way-to-run-cpanel-vps-2026-startups-1.svg', svg_cheap_vps),
    ('assets/img/blog/web-hosts-india-southeast-asia-save-licensing-1.svg', svg_asia)
]

for path, content in files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote {path}')

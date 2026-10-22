import os

# 1. WHM DNS Cluster SVG
svg_dns = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="boxBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="boxGreen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <linearGradient id="boxAmber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg)"/>

  <!-- Title -->
  <text x="480" y="44" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">WHM DNS Cluster Synchronization &amp; Troubleshooting Architecture</text>
  <text x="480" y="70" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Zone updates, WHM API tokens, port 2087 connectivity, and cPanel DNSOnly slave nodes</text>

  <!-- Master Node -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="250" height="310" rx="14" fill="url(#boxBlue)" stroke="#38bdf8" stroke-width="2"/>
    <rect width="250" height="40" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <circle cx="28" cy="20" r="7" fill="#38bdf8"/>
    <text x="44" y="25" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Primary cPanel/WHM Server</text>

    <!-- Master details -->
    <rect x="18" y="55" width="214" height="60" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="76" font-family="monospace" font-size="12" fill="#7dd3fc" font-weight="bold">Master Role: Synchronize</text>
    <text x="30" y="96" font-family="sans-serif" font-size="11" fill="#94a3b8">Initiates zone adds/edits/deletes</text>

    <rect x="18" y="125" width="214" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="145" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Key Components:</text>
    <text x="30" y="165" font-family="monospace" font-size="11" fill="#cbd5e1">• /var/cpanel/cluster/</text>
    <text x="30" y="185" font-family="monospace" font-size="11" fill="#cbd5e1">• /scripts/dnscluster sync</text>

    <rect x="18" y="210" width="214" height="80" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="30" y="230" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Security Credentials:</text>
    <text x="30" y="250" font-family="sans-serif" font-size="11" fill="#94a3b8">Remote WHM API Token</text>
    <text x="30" y="270" font-family="sans-serif" font-size="11" fill="#f59e0b">Requires Port 2087 Outbound</text>
  </g>

  <!-- Synchronization Stream in Middle -->
  <g transform="translate(340, 160)">
    <!-- Path to Node 1 -->
    <path d="M 0,50 L 140,0" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" fill="none"/>
    <polygon points="145,0 133,-5 137,4" fill="#38bdf8"/>

    <!-- Path to Node 2 -->
    <path d="M 0,140 L 140,190" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" fill="none"/>
    <polygon points="145,190 137,185 133,195" fill="#38bdf8"/>

    <!-- Diagnostic Hub in Center -->
    <rect x="20" y="55" width="180" height="80" rx="10" fill="url(#boxAmber)" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="110" y="80" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fde68a" text-anchor="middle">Sync Checkpoints</text>
    <text x="110" y="100" font-family="sans-serif" font-size="11" fill="#fed7aa" text-anchor="middle">1. Token ACL Permissions</text>
    <text x="110" y="118" font-family="sans-serif" font-size="11" fill="#fed7aa" text-anchor="middle">2. Port 2087 &amp; SSL Certs</text>
  </g>

  <!-- DNSOnly Node 1 -->
  <g transform="translate(640, 110)" filter="url(#shadow)">
    <rect width="260" height="145" rx="14" fill="url(#boxGreen)" stroke="#10b981" stroke-width="1.5"/>
    <rect width="260" height="35" rx="14" fill="#059669" fill-opacity="0.3"/>
    <circle cx="24" cy="18" r="6" fill="#34d399"/>
    <text x="38" y="22" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">Nameserver 1 (cPanel DNSOnly)</text>

    <text x="18" y="60" font-family="sans-serif" font-size="11" fill="#cbd5e1">Role: <tspan font-family="monospace" fill="#6ee7b7" font-weight="bold">Write-Only / Standalone</tspan></text>
    <text x="18" y="80" font-family="sans-serif" font-size="11" fill="#cbd5e1">Service: <tspan font-family="monospace" fill="#f8fafc">BIND / PowerDNS (/etc/named.conf)</tspan></text>
    <text x="18" y="100" font-family="sans-serif" font-size="11" fill="#cbd5e1">Verification: <tspan font-family="monospace" fill="#f8fafc">rndc reload | named-checkconf</tspan></text>
    <rect x="18" y="115" width="224" height="20" rx="4" fill="#064e3b"/>
    <text x="130" y="129" font-family="sans-serif" font-size="10" fill="#a7f3d0" text-anchor="middle">Authoritative NS1 (ns1.example.com)</text>
  </g>

  <!-- DNSOnly Node 2 -->
  <g transform="translate(640, 275)" filter="url(#shadow)">
    <rect width="260" height="145" rx="14" fill="url(#boxGreen)" stroke="#10b981" stroke-width="1.5"/>
    <rect width="260" height="35" rx="14" fill="#059669" fill-opacity="0.3"/>
    <circle cx="24" cy="18" r="6" fill="#34d399"/>
    <text x="38" y="22" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">Nameserver 2 (cPanel DNSOnly)</text>

    <text x="18" y="60" font-family="sans-serif" font-size="11" fill="#cbd5e1">Role: <tspan font-family="monospace" fill="#6ee7b7" font-weight="bold">Write-Only / Standalone</tspan></text>
    <text x="18" y="80" font-family="sans-serif" font-size="11" fill="#cbd5e1">Service: <tspan font-family="monospace" fill="#f8fafc">BIND / PowerDNS (/var/named/)</tspan></text>
    <text x="18" y="100" font-family="sans-serif" font-size="11" fill="#cbd5e1">Verification: <tspan font-family="monospace" fill="#f8fafc">named-checkzone domain.com zonefile</tspan></text>
    <rect x="18" y="115" width="224" height="20" rx="4" fill="#064e3b"/>
    <text x="130" y="129" font-family="sans-serif" font-size="10" fill="#a7f3d0" text-anchor="middle">Authoritative NS2 (ns2.example.com)</text>
  </g>

  <!-- Bottom Troubleshooting Bar -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="75" y="455" font-family="monospace" font-size="11" fill="#f87171" font-weight="bold">Fast CLI Sync:</text>
  <text x="175" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">/scripts/dnscluster syncall</text>
  <text x="370" y="455" font-family="monospace" font-size="11" fill="#38bdf8">|</text>
  <text x="385" y="455" font-family="monospace" font-size="11" fill="#f87171" font-weight="bold">Rebuild Config:</text>
  <text x="500" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">/scripts/rebuilddnsconfig</text>
  <text x="690" y="455" font-family="monospace" font-size="11" fill="#38bdf8">|</text>
  <text x="705" y="455" font-family="sans-serif" font-size="11" fill="#a7f3d0">LicenBase Engineering</text>
</svg>'''

# 2. MySQL Too Many Connections SVG
svg_mysql = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="gradRed" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#450a0a"/>
    </linearGradient>
    <linearGradient id="gradBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg2)"/>

  <!-- Title -->
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">MySQL &amp; MariaDB Connection Pool Architecture on cPanel</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Understanding Error 1040 (ER_CON_COUNT_ERROR) and connection lifecycle vs RAM sizing</text>

  <!-- Left: Traffic & Web Server Workers -->
  <g transform="translate(60, 105)" filter="url(#shadow2)">
    <rect width="240" height="315" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="240" height="38" rx="14" fill="#334155"/>
    <text x="120" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#f8fafc" text-anchor="middle">Web &amp; PHP Application Layer</text>

    <!-- Content -->
    <rect x="16" y="52" width="208" height="60" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="26" y="73" font-family="sans-serif" font-size="11" font-weight="bold" fill="#38bdf8">Incoming Web Requests</text>
    <text x="26" y="93" font-family="sans-serif" font-size="11" fill="#94a3b8">Apache / LiteSpeed / Nginx</text>

    <rect x="16" y="122" width="208" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="26" y="143" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">PHP Worker Execution</text>
    <text x="26" y="163" font-family="sans-serif" font-size="11" fill="#cbd5e1">• PHP-FPM / LSAPI Pools</text>
    <text x="26" y="183" font-family="sans-serif" font-size="11" fill="#cbd5e1">• WordPress / WHMCS DB calls</text>

    <rect x="16" y="217" width="208" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="26" y="238" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f87171">Connection Creep Pitfalls</text>
    <text x="26" y="258" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Persistent DB connections</text>
    <text x="26" y="278" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Long wait_timeout defaults</text>
  </g>

  <!-- Center Arrow -->
  <g transform="translate(320, 240)">
    <line x1="0" y1="0" x2="60" y2="0" stroke="#f59e0b" stroke-width="4"/>
    <polygon points="65,0 52,-6 52,6" fill="#f59e0b"/>
    <text x="30" y="-12" font-family="monospace" font-size="11" fill="#fcd34d" text-anchor="middle">TCP / Socket</text>
    <text x="30" y="20" font-family="monospace" font-size="10" fill="#94a3b8" text-anchor="middle">Port 3306</text>
  </g>

  <!-- Right: MySQL Engine & Pool -->
  <g transform="translate(400, 105)" filter="url(#shadow2)">
    <rect width="500" height="315" rx="14" fill="url(#gradBlue)" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="500" height="38" rx="14" fill="#1d4ed8" fill-opacity="0.4"/>
    <text x="250" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#93c5fd" text-anchor="middle">MySQL / MariaDB Connection Management</text>

    <!-- Active Connections Pool -->
    <rect x="20" y="52" width="220" height="135" rx="10" fill="#0b1329" stroke="#1e3a8a"/>
    <text x="32" y="75" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">Active Threads (In-Query)</text>
    <text x="32" y="95" font-family="sans-serif" font-size="11" fill="#cbd5e1">Executing SELECT, UPDATE, etc.</text>
    <text x="32" y="115" font-family="sans-serif" font-size="11" fill="#94a3b8">Allocates thread memory:</text>
    <text x="32" y="135" font-family="monospace" font-size="10" fill="#a5f3fc">• read_buffer_size</text>
    <text x="32" y="152" font-family="monospace" font-size="10" fill="#a5f3fc">• sort_buffer_size</text>
    <text x="32" y="170" font-family="monospace" font-size="10" fill="#a5f3fc">• join_buffer_size</text>

    <!-- Sleeping Connections Pool -->
    <rect x="260" y="52" width="220" height="135" rx="10" fill="#0b1329" stroke="#78350f"/>
    <text x="272" y="75" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fbbf24">Sleeping Threads (Idle)</text>
    <text x="272" y="95" font-family="sans-serif" font-size="11" fill="#cbd5e1">State: <tspan font-family="monospace" fill="#fcd34d">"Sleep"</tspan> in processlist</text>
    <text x="272" y="115" font-family="sans-serif" font-size="11" fill="#94a3b8">Holds connection slot open until</text>
    <text x="272" y="135" font-family="monospace" font-size="11" fill="#f87171">wait_timeout (e.g. 28800s!)</text>
    <text x="272" y="155" font-family="sans-serif" font-size="11" fill="#94a3b8">Fix: Reduce to 30s - 60s in /etc/my.cnf</text>

    <!-- Bottom: max_connections Threshold & Error 1040 -->
    <rect x="20" y="200" width="460" height="100" rx="10" fill="url(#gradRed)" stroke="#ef4444" stroke-width="1.5"/>
    <text x="35" y="224" font-family="monospace" font-size="13" font-weight="bold" fill="#fecaca">Ceiling: max_connections = 151 (Default)</text>
    <text x="35" y="246" font-family="sans-serif" font-size="11" fill="#fee2e2">When Active + Sleep reaches max_connections:</text>
    <text x="35" y="268" font-family="monospace" font-size="12" font-weight="bold" fill="#fef08a">➔ ERROR 1040 (HY000): Too many connections</text>
    <text x="35" y="288" font-family="sans-serif" font-size="11" fill="#cbd5e1">Emergency back-door: 1 extra reserved connection for user with SUPER / CONNECTION_ADMIN</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Emergency Root Login:</text>
  <text x="245" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">mysql --protocol=socket -u root</text>
  <text x="500" y="455" font-family="monospace" font-size="11" fill="#fbbf24">|</text>
  <text x="520" y="455" font-family="monospace" font-size="11" fill="#f87171" font-weight="bold">Kill Sleepers:</text>
  <text x="620" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">mysqladmin -u root processlist</text>
</svg>'''

# 3. 508 Resource Limit SVG
svg_508 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bg3)"/>

  <!-- Title -->
  <text x="480" y="40" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">CloudLinux LVE &amp; cPanel 508 Resource Limit Architecture</text>
  <text x="480" y="66" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">How CPU, Memory, Entry Processes (EP), and I/O caps trigger HTTP 508 errors</text>

  <!-- 4 Limit Pillars -->
  <!-- 1. CPU -->
  <g transform="translate(60, 100)" filter="url(#shadow3)">
    <rect width="190" height="230" rx="12" fill="url(#cardGrad)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="190" height="34" rx="12" fill="#0284c7" fill-opacity="0.3"/>
    <text x="95" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8" text-anchor="middle">SPEED / CPU Limit</text>

    <text x="18" y="60" font-family="monospace" font-size="11" fill="#7dd3fc" font-weight="bold">Metric: %CPU (e.g. 100%)</text>
    <text x="18" y="85" font-family="sans-serif" font-size="11" fill="#cbd5e1">Throttles thread execution when account spikes.</text>
    <text x="18" y="125" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Common Cause:</text>
    <text x="18" y="145" font-family="sans-serif" font-size="11" fill="#94a3b8">• Complex WP queries</text>
    <text x="18" y="165" font-family="sans-serif" font-size="11" fill="#94a3b8">• Uncached search bots</text>
    <text x="18" y="185" font-family="sans-serif" font-size="11" fill="#94a3b8">• Heavy PHP computations</text>
    <rect x="15" y="198" width="160" height="22" rx="4" fill="#082f49"/>
    <text x="95" y="213" font-family="sans-serif" font-size="10" fill="#38bdf8" text-anchor="middle">Symptom: Severe Slowdown</text>
  </g>

  <!-- 2. Memory (pMEM / vMEM) -->
  <g transform="translate(280, 100)" filter="url(#shadow3)">
    <rect width="190" height="230" rx="12" fill="url(#cardGrad)" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="190" height="34" rx="12" fill="#7e22ce" fill-opacity="0.3"/>
    <text x="95" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#c084fc" text-anchor="middle">pMEM / Physical RAM</text>

    <text x="18" y="60" font-family="monospace" font-size="11" fill="#d8b4fe" font-weight="bold">Metric: RAM (e.g. 1GB - 2GB)</text>
    <text x="18" y="85" font-family="sans-serif" font-size="11" fill="#cbd5e1">Hard memory limit per cPanel LVE container.</text>
    <text x="18" y="125" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Common Cause:</text>
    <text x="18" y="145" font-family="sans-serif" font-size="11" fill="#94a3b8">• Image resizing plugins</text>
    <text x="18" y="165" font-family="sans-serif" font-size="11" fill="#94a3b8">• Elementor / page builders</text>
    <text x="18" y="185" font-family="sans-serif" font-size="11" fill="#94a3b8">• Memory leak in themes</text>
    <rect x="15" y="198" width="160" height="22" rx="4" fill="#3b0764"/>
    <text x="95" y="213" font-family="sans-serif" font-size="10" fill="#c084fc" text-anchor="middle">Symptom: 500 / 503 / 508</text>
  </g>

  <!-- 3. Entry Processes (EP) -->
  <g transform="translate(500, 100)" filter="url(#shadow3)">
    <rect width="190" height="230" rx="12" fill="url(#cardGrad)" stroke="#f43f5e" stroke-width="2"/>
    <rect width="190" height="34" rx="12" fill="#be123c" fill-opacity="0.4"/>
    <text x="95" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#fb7185" text-anchor="middle">EP / Entry Processes</text>

    <text x="18" y="60" font-family="monospace" font-size="11" fill="#fda4af" font-weight="bold">Metric: Concurrent PHP (20-30)</text>
    <text x="18" y="85" font-family="sans-serif" font-size="11" fill="#cbd5e1">Primary culprit behind instant 508 errors.</text>
    <text x="18" y="125" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Common Cause:</text>
    <text x="18" y="145" font-family="sans-serif" font-size="11" fill="#94a3b8">• Stuck PHP-FPM scripts</text>
    <text x="18" y="165" font-family="sans-serif" font-size="11" fill="#94a3b8">• External HTTP API delays</text>
    <text x="18" y="185" font-family="sans-serif" font-size="11" fill="#94a3b8">• xmlrpc.php bot attacks</text>
    <rect x="15" y="198" width="160" height="22" rx="4" fill="#4c0519"/>
    <text x="95" y="213" font-family="sans-serif" font-size="10" fill="#f43f5e" font-weight="bold" text-anchor="middle">Immediate 508 Trigger!</text>
  </g>

  <!-- 4. IO / IOPS -->
  <g transform="translate(720, 100)" filter="url(#shadow3)">
    <rect width="180" height="230" rx="12" fill="url(#cardGrad)" stroke="#eab308" stroke-width="1.5"/>
    <rect width="180" height="34" rx="12" fill="#a16207" fill-opacity="0.3"/>
    <text x="90" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#facc15" text-anchor="middle">IO / IOPS Throughput</text>

    <text x="16" y="60" font-family="monospace" font-size="11" fill="#fde047" font-weight="bold">Metric: MB/s &amp; IOPS (10MB/s)</text>
    <text x="16" y="85" font-family="sans-serif" font-size="11" fill="#cbd5e1">Disk read/write bandwidth restriction.</text>
    <text x="16" y="125" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Common Cause:</text>
    <text x="16" y="145" font-family="sans-serif" font-size="11" fill="#94a3b8">• Backup plugin zip jobs</text>
    <text x="16" y="165" font-family="sans-serif" font-size="11" fill="#94a3b8">• Massive error_log writes</text>
    <text x="16" y="185" font-family="sans-serif" font-size="11" fill="#94a3b8">• Continuous DB sorting</text>
    <rect x="15" y="198" width="150" height="22" rx="4" fill="#422006"/>
    <text x="90" y="213" font-family="sans-serif" font-size="10" fill="#facc15" text-anchor="middle">Symptom: High I/O Wait</text>
  </g>

  <!-- Bottom Result Box: 508 Banner -->
  <g transform="translate(60, 350)" filter="url(#shadow3)">
    <rect width="840" height="100" rx="12" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="20" y="20" width="180" height="60" rx="8" fill="#e11d48"/>
    <text x="110" y="46" font-family="sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">HTTP 508</text>
    <text x="110" y="68" font-family="sans-serif" font-size="11" fill="#ffe4e6" text-anchor="middle">Resource Limit Reached</text>

    <text x="220" y="42" font-family="sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Fast CLI Diagnosis &amp; Snapshot Inspection:</text>
    <text x="220" y="66" font-family="monospace" font-size="11" fill="#a5f3fc">lveinfo --period=1d --by-usage=ep,pmem,cpu --limit=10</text>
    <text x="220" y="86" font-family="monospace" font-size="11" fill="#86efac">lvechart --user=username --period=today | CloudLinux LVE Manager</text>
  </g>
</svg>'''

with open('assets/img/blog/whm-dns-cluster-not-syncing-diagnose-fix-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_dns)
print('Wrote whm-dns-cluster-not-syncing-diagnose-fix-1.svg')

with open('assets/img/blog/fix-mysql-too-many-connections-cpanel-server-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_mysql)
print('Wrote fix-mysql-too-many-connections-cpanel-server-1.svg')

with open('assets/img/blog/fix-508-resource-limit-reached-error-cpanel-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_508)
print('Wrote fix-508-resource-limit-reached-error-cpanel-1.svg')

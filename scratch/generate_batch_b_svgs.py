import os

# 1. Web Shell Detection SVG
svg_shell = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgShell" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="redCard" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </linearGradient>
    <filter id="sh1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgShell)"/>

  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Linux VPS Hidden Web Shell Detection &amp; Analysis Playbook</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Hunting obfuscated PHP payloads, anomalous mtime stamps, and suspicious web processes</text>

  <!-- Left: Shell Characteristics -->
  <g transform="translate(60, 105)" filter="url(#sh1)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#334155"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#f8fafc" text-anchor="middle">Common Web Shell Patterns</text>

    <rect x="15" y="52" width="220" height="75" rx="8" fill="url(#redCard)" stroke="#f43f5e"/>
    <text x="25" y="73" font-family="monospace" font-size="11" fill="#fecdd3" font-weight="bold">Obfuscation Signatures</text>
    <text x="25" y="93" font-family="monospace" font-size="10" fill="#ffe4e6">• eval(base64_decode(...))</text>
    <text x="25" y="110" font-family="monospace" font-size="10" fill="#ffe4e6">• preg_replace with /e modifier</text>

    <rect x="15" y="137" width="220" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="158" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Stealth Masquerading</text>
    <text x="25" y="178" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Hidden in /wp-content/uploads/</text>
    <text x="25" y="196" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Mimicking core files (.php.jpg)</text>

    <rect x="15" y="222" width="220" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="243" font-family="sans-serif" font-size="11" font-weight="bold" fill="#38bdf8">Timestamp Tampering</text>
    <text x="25" y="263" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Timestomping mtime stamps</text>
    <text x="25" y="281" font-family="sans-serif" font-size="11" fill="#cbd5e1">• Exposed via ctime comparison</text>
  </g>

  <!-- Middle Arrow -->
  <g transform="translate(330, 240)">
    <line x1="0" y1="0" x2="50" y2="0" stroke="#f43f5e" stroke-width="4"/>
    <polygon points="55,0 42,-6 42,6" fill="#f43f5e"/>
    <text x="25" y="-12" font-family="monospace" font-size="11" fill="#fca5a5" text-anchor="middle">Scan</text>
  </g>

  <!-- Right: Command Playbook -->
  <g transform="translate(400, 105)" filter="url(#sh1)">
    <rect width="500" height="315" rx="14" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="500" height="38" rx="14" fill="#881337" fill-opacity="0.3"/>
    <text x="250" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#fca5a5" text-anchor="middle">High-Accuracy Terminal Detection Commands</text>

    <!-- Scan for functions -->
    <rect x="20" y="52" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="73" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Search Dangerous Execution Functions:</text>
    <text x="32" y="93" font-family="monospace" font-size="11" fill="#f1f5f9">grep -rP "(passthru|shell_exec|system|base64_decode)" \</text>
    <text x="45" y="113" font-family="monospace" font-size="11" fill="#fcd34d">/home/*/public_html/wp-content/uploads/ --include="*.php"</text>

    <!-- Scan modified files -->
    <rect x="20" y="135" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="156" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Find PHP Files Modified in the Last 48 Hours:</text>
    <text x="32" y="176" font-family="monospace" font-size="11" fill="#f1f5f9">find /home/*/public_html -type f -name "*.php" -mtime -2 \</text>
    <text x="45" y="196" font-family="monospace" font-size="11" fill="#6ee7b7">! -path "*/wp-content/cache/*" -ls</text>

    <!-- Automated AI Scanner -->
    <rect x="20" y="218" width="460" height="85" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="32" y="239" font-family="sans-serif" font-size="12" font-weight="bold" fill="#7dd3fc">3. Automated Deep Heuristic Quarantine:</text>
    <text x="32" y="259" font-family="monospace" font-size="11" fill="#38bdf8">imunify360-agent malware user scan &lt;username&gt;</text>
    <text x="32" y="279" font-family="sans-serif" font-size="11" fill="#94a3b8">Proactive real-time defense detects zero-day shells instantly.</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Check Listening Network Sockets:</text>
  <text x="315" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">ss -tulpn | grep -v ':(80|443|22|2083|2087)'</text>
  <text x="690" y="455" font-family="monospace" font-size="11" fill="#34d399">|</text>
  <text x="705" y="455" font-family="sans-serif" font-size="11" fill="#a7f3d0">LicenBase Security Guide</text>
</svg>'''

# 2. Session Hijacking & Cookie Theft SVG
svg_session = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgSess" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="sh2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgSess)"/>

  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">cPanel Session Hijacking &amp; Cookie Theft Defense Architecture</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Mitigating infostealer malware, enforcing IP session binding, and hardening cpsession tokens</text>

  <!-- 3 Pillars -->
  <!-- 1. The Vector -->
  <g transform="translate(60, 105)" filter="url(#sh2)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#b91c1c" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#fca5a5" text-anchor="middle">1. Threat Vector: Infostealers</text>

    <text x="18" y="65" font-family="sans-serif" font-size="11" fill="#cbd5e1">Malware (RedLine, Lumma, Vidar) extracts browser sqlite databases:</text>
    <text x="18" y="90" font-family="monospace" font-size="10" fill="#f87171">• cpsession cookies</text>
    <text x="18" y="108" font-family="monospace" font-size="10" fill="#f87171">• WHM root auth tokens</text>
    <text x="18" y="126" font-family="monospace" font-size="10" fill="#f87171">• Saved passwords &amp; autofill</text>

    <rect x="15" y="145" width="220" height="150" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="25" y="168" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Attack Mechanism:</text>
    <text x="25" y="190" font-family="sans-serif" font-size="11" fill="#94a3b8">Attacker imports stolen cookie into anti-detect browser, bypassing standard username/password and MFA!</text>
  </g>

  <!-- 2. WHM Tweak Settings Mitigation -->
  <g transform="translate(355, 105)" filter="url(#sh2)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0284c7" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">2. WHM Security Hardening</text>

    <rect x="15" y="52" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="73" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">Cookie IP Validation</text>
    <text x="25" y="93" font-family="monospace" font-size="10" fill="#f1f5f9">Set to: "strict"</text>
    <text x="25" y="110" font-family="sans-serif" font-size="10" fill="#94a3b8">Kills session if client IP changes.</text>

    <rect x="15" y="132" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="153" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">Session Timeout Quota</text>
    <text x="25" y="173" font-family="monospace" font-size="10" fill="#f1f5f9">Idle: 900s (15 mins)</text>
    <text x="25" y="190" font-family="sans-serif" font-size="10" fill="#94a3b8">Forces re-authentication.</text>

    <rect x="15" y="212" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="233" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7dd3fc">MFA Enforcement</text>
    <text x="25" y="253" font-family="sans-serif" font-size="10" fill="#cbd5e1">Two-Factor Auth (TOTP)</text>
    <text x="25" y="271" font-family="sans-serif" font-size="10" fill="#cbd5e1">Mandatory for all WHM users.</text>
  </g>

  <!-- 3. Infrastructure Defenses -->
  <g transform="translate(650, 105)" filter="url(#sh2)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">3. Architectural Isolation</text>

    <text x="18" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">CageFS Virtualized Filesystem:</text>
    <text x="18" y="85" font-family="sans-serif" font-size="11" fill="#cbd5e1">Prevents compromised cPanel users from snooping on neighboring session directories in /tmp.</text>

    <rect x="15" y="120" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="142" font-family="sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">cPHulk Brute Force:</text>
    <text x="25" y="162" font-family="sans-serif" font-size="10" fill="#94a3b8">Bans IP addresses attempting credential stuffing or cookie replay.</text>

    <rect x="15" y="215" width="220" height="82" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="235" font-family="sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">SSL/TLS Strict HSTS:</text>
    <text x="25" y="255" font-family="sans-serif" font-size="10" fill="#94a3b8">Forces secure-flagged cookies on ports 2083 and 2087.</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">CLI Session Purge:</text>
  <text x="220" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">rm -f /var/cpanel/sessions/raw/*</text>
  <text x="500" y="455" font-family="monospace" font-size="11" fill="#38bdf8">|</text>
  <text x="520" y="455" font-family="monospace" font-size="11" fill="#34d399" font-weight="bold">Check Active Sessions:</text>
  <text x="700" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">whmapi1 list_sessions</text>
</svg>'''

# 3. Imunify360 vs CSF SVG
svg_imunify_csf = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgComp" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="sh3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgComp)"/>

  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Imunify360 vs CSF Firewall: Technical Architecture Comparison</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Comparing Layer 3/4 network firewall rules against full Layer 7 AI proactive security</text>

  <!-- Left: CSF -->
  <g transform="translate(60, 105)" filter="url(#sh3)">
    <rect width="390" height="315" rx="14" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="390" height="40" rx="14" fill="#334155"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#f8fafc" text-anchor="middle">ConfigServer Security &amp; Firewall (CSF)</text>

    <text x="20" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#94a3b8">Network &amp; Port Level Protection (Layer 3/4)</text>

    <rect x="20" y="78" width="350" height="48" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="30" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Iptables / Nftables Packet Filtering</text>
    <text x="30" y="115" font-family="sans-serif" font-size="10" fill="#94a3b8">Controls inbound/outbound ports, SYN floods, ping bans.</text>

    <rect x="20" y="134" width="350" height="48" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="30" y="154" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Login Failure Daemon (LFD)</text>
    <text x="30" y="171" font-family="sans-serif" font-size="10" fill="#94a3b8">Scans log files (SSH, Exim, cPanel) for failed password attempts.</text>

    <rect x="20" y="190" width="350" height="60" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="30" y="210" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f87171">Key Limitations:</text>
    <text x="30" y="228" font-family="sans-serif" font-size="10" fill="#cbd5e1">• No malware scanner or proactive PHP execution blocking</text>
    <text x="30" y="243" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Blind to encrypted HTTPS web exploits &amp; SQL injection</text>

    <rect x="20" y="260" width="350" height="45" rx="6" fill="#1e293b"/>
    <text x="195" y="287" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Cost: Free / Open Source</text>
  </g>

  <!-- Right: Imunify360 -->
  <g transform="translate(510, 105)" filter="url(#sh3)">
    <rect width="390" height="315" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="390" height="40" rx="14" fill="#0284c7" fill-opacity="0.3"/>
    <text x="195" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">Imunify360 Enterprise Defense Stack</text>

    <text x="20" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#7dd3fc">Full-Stack Application &amp; Web Defense (Layer 3-7)</text>

    <rect x="20" y="78" width="350" height="48" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="30" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#38bdf8">Proactive Defense (AI Heuristics)</text>
    <text x="30" y="115" font-family="sans-serif" font-size="10" fill="#94a3b8">Prevents zero-day PHP execution before code runs in memory.</text>

    <rect x="20" y="134" width="350" height="48" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="30" y="154" font-family="sans-serif" font-size="11" font-weight="bold" fill="#34d399">Automated Real-Time Malware Cleanup</text>
    <text x="30" y="171" font-family="sans-serif" font-size="10" fill="#94a3b8">Background file scanner with surgical un-hacked file restores.</text>

    <rect x="20" y="190" width="350" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="30" y="210" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a855f7">Advanced WAF &amp; Captcha Splash Page</text>
    <text x="30" y="228" font-family="sans-serif" font-size="10" fill="#cbd5e1">• ModSecurity integration + Global Herd Immunity IP Cloud</text>
    <text x="30" y="243" font-family="sans-serif" font-size="10" fill="#cbd5e1">• KernelCare live patching without reboots</text>

    <rect x="20" y="260" width="350" height="45" rx="6" fill="#082f49"/>
    <text x="195" y="287" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">LicenBase Automated License: $6.00/mo</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="sans-serif" font-size="11" fill="#f8fafc" font-weight="bold">Best Practice Architecture:</text>
  <text x="240" y="455" font-family="sans-serif" font-size="11" fill="#94a3b8">Run Imunify360 for full web application defense; its native firewall replaces or integrates with CSF.</text>
</svg>'''

# 4. OOM Killer SVG
svg_oom = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgOOM" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#180b0b"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="sh4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgOOM)"/>

  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Linux Kernel OOM Killer Lifecycle on cPanel &amp; WHM</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Understanding oom_score calculation, process termination, and tailwatchd crash recovery</text>

  <!-- Left: Memory Saturation Progression -->
  <g transform="translate(60, 105)" filter="url(#sh4)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#991b1b" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#fca5a5" text-anchor="middle">Memory Exhaustion Stages</text>

    <rect x="15" y="52" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="73" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">1. RAM Exhaustion</text>
    <text x="25" y="91" font-family="sans-serif" font-size="10" fill="#cbd5e1">Physical RAM drops below</text>
    <text x="25" y="106" font-family="monospace" font-size="10" fill="#fde68a">vm.min_free_kbytes</text>

    <rect x="15" y="130" width="220" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="151" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f97316">2. Swap Saturation</text>
    <text x="25" y="169" font-family="sans-serif" font-size="10" fill="#cbd5e1">Swap partition hits 100%.</text>
    <text x="25" y="184" font-family="sans-serif" font-size="10" fill="#cbd5e1">Disk thrashing / CPU I/O wait.</text>

    <rect x="15" y="208" width="220" height="95" rx="8" fill="#450a0a" stroke="#ef4444"/>
    <text x="25" y="228" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fecaca">3. Kernel Invocations</text>
    <text x="25" y="246" font-family="monospace" font-size="10" fill="#fca5a5">out_of_memory() called</text>
    <text x="25" y="264" font-family="sans-serif" font-size="10" fill="#fee2e2">Calculates highest oom_score</text>
    <text x="25" y="282" font-family="monospace" font-size="10" fill="#fef08a">Kills mysqld or httpd!</text>
  </g>

  <!-- Middle Arrow -->
  <g transform="translate(330, 240)">
    <line x1="0" y1="0" x2="50" y2="0" stroke="#f43f5e" stroke-width="4"/>
    <polygon points="55,0 42,-6 42,6" fill="#f43f5e"/>
    <text x="25" y="-12" font-family="monospace" font-size="11" fill="#fca5a5" text-anchor="middle">Kill</text>
  </g>

  <!-- Right: Triage and Prevention -->
  <g transform="translate(400, 105)" filter="url(#sh4)">
    <rect width="500" height="315" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="500" height="38" rx="14" fill="#0369a1" fill-opacity="0.3"/>
    <text x="250" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#7dd3fc" text-anchor="middle">Diagnostics &amp; OOM Prevention Playbook</text>

    <rect x="20" y="52" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="73" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Verify OOM Incident in Kernel dmesg Log:</text>
    <text x="32" y="93" font-family="monospace" font-size="11" fill="#f1f5f9">dmesg -T | grep -i -E "oom|out of memory|killed process"</text>
    <text x="32" y="113" font-family="monospace" font-size="11" fill="#fcd34d">grep -i "killed process" /var/log/messages</text>

    <rect x="20" y="135" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="156" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Protect MySQL by Adjusting oom_score_adj:</text>
    <text x="32" y="176" font-family="monospace" font-size="11" fill="#f1f5f9">echo -1000 &gt; /proc/$(pgrep mysqld)/oom_score_adj</text>
    <text x="32" y="196" font-family="sans-serif" font-size="10" fill="#94a3b8">Immunizes database engine from being killed before PHP workers.</text>

    <rect x="20" y="218" width="460" height="85" rx="8" fill="#1e293b" stroke="#a855f7"/>
    <text x="32" y="239" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c084fc">3. Contain User Leaks with CloudLinux LVE Limits:</text>
    <text x="32" y="259" font-family="sans-serif" font-size="11" fill="#cbd5e1">Caps individual cPanel accounts to 1GB - 2GB RAM. If a user leaks RAM, only that user container is killed, keeping MySQL &amp; Apache 100% operational.</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#fbbf24" font-weight="bold">Check Live Memory:</text>
  <text x="210" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">free -m</text>
  <text x="280" y="455" font-family="monospace" font-size="11" fill="#38bdf8">|</text>
  <text x="300" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Service Watchdog:</text>
  <text x="440" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">/usr/local/cpanel/libexec/tailwatch/tailwatchd --status</text>
</svg>'''

# 5. Linux VPS Swapping SVG
svg_swap = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgSwap" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#071527"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="sh5" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgSwap)"/>

  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Linux Kernel Page Cache &amp; Swappiness Dynamics</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Why Linux VPS swaps pages even when 'free -m' shows plenty of available memory</text>

  <!-- RAM Breakdown -->
  <g transform="translate(60, 105)" filter="url(#sh5)">
    <rect width="400" height="315" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="400" height="40" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="200" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">Physical RAM (free -m Breakdown)</text>

    <rect x="20" y="55" width="360" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="32" y="76" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">Anonymous Memory (Processes)</text>
    <text x="32" y="95" font-family="sans-serif" font-size="11" fill="#cbd5e1">Active PHP-FPM, MySQL, and Nginx heap/stack.</text>
    <text x="32" y="112" font-family="sans-serif" font-size="10" fill="#94a3b8">Cannot be dropped without swapping to disk.</text>

    <rect x="20" y="135" width="360" height="70" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="32" y="156" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fbbf24">Page Cache &amp; Buffers (buff/cache)</text>
    <text x="32" y="175" font-family="sans-serif" font-size="11" fill="#cbd5e1">Disk caching for fast file reading.</text>
    <text x="32" y="192" font-family="sans-serif" font-size="10" fill="#94a3b8">The kernel prefers caching fast disk pages over idle sleep processes!</text>

    <rect x="20" y="215" width="360" height="85" rx="8" fill="#082f49" stroke="#38bdf8"/>
    <text x="32" y="235" font-family="sans-serif" font-size="12" font-weight="bold" fill="#7dd3fc">The vm.swappiness Dial (Default = 60)</text>
    <text x="32" y="254" font-family="sans-serif" font-size="11" fill="#cbd5e1">A balance ratio between reclaiming page cache vs paging anonymous memory to swap.</text>
    <text x="32" y="274" font-family="sans-serif" font-size="10" fill="#fed7aa">Setting to 10 or 1 stops premature swapping on hosting VPS.</text>
  </g>

  <!-- Swap & Remediation -->
  <g transform="translate(500, 105)" filter="url(#sh5)">
    <rect width="400" height="315" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="400" height="40" rx="14" fill="#059669" fill-opacity="0.25"/>
    <text x="200" y="26" font-family="sans-serif" font-size="14" font-weight="700" fill="#34d399" text-anchor="middle">Diagnosis &amp; Swappiness Optimization</text>

    <rect x="20" y="55" width="360" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="32" y="76" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Check Current Swappiness Value:</text>
    <text x="32" y="96" font-family="monospace" font-size="11" fill="#f1f5f9">cat /proc/sys/vm/swappiness</text>
    <text x="32" y="116" font-family="monospace" font-size="11" fill="#94a3b8"># Default on Ubuntu &amp; AlmaLinux is 60</text>

    <rect x="20" y="140" width="360" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="32" y="161" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Reduce Swappiness to 10 Instantly:</text>
    <text x="32" y="181" font-family="monospace" font-size="11" fill="#f1f5f9">sysctl vm.swappiness=10</text>
    <text x="32" y="201" font-family="sans-serif" font-size="10" fill="#94a3b8">Persist in /etc/sysctl.conf: vm.swappiness = 10</text>

    <rect x="20" y="225" width="360" height="75" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="32" y="246" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fbbf24">3. Safely Flush Stale Swap Back into RAM:</text>
    <text x="32" y="266" font-family="monospace" font-size="11" fill="#f1f5f9">swapoff -a &amp;&amp; swapon -a</text>
    <text x="32" y="286" font-family="sans-serif" font-size="10" fill="#94a3b8">Requires sufficient free RAM to hold swapped data.</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#fbbf24" font-weight="bold">Inspect Processes Using Swap:</text>
  <text x="290" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">for f in /proc/*/status; do awk '/VmSwap/{print $2, $3}' $f; done</text>
</svg>'''

with open('assets/img/blog/detect-hidden-web-shells-linux-vps-commands-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_shell)
print('Wrote detect-hidden-web-shells-linux-vps-commands-1.svg')

with open('assets/img/blog/protect-cpanel-session-hijacking-cookie-theft-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_session)
print('Wrote protect-cpanel-session-hijacking-cookie-theft-1.svg')

with open('assets/img/blog/imunify360-vs-csf-firewall-security-stack-comparison-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_imunify_csf)
print('Wrote imunify360-vs-csf-firewall-security-stack-comparison-1.svg')

with open('assets/img/blog/fix-oom-killer-out-of-memory-cpanel-server-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_oom)
print('Wrote fix-oom-killer-out-of-memory-cpanel-server-1.svg')

with open('assets/img/blog/linux-vps-swapping-when-ram-available-fix-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_swap)
print('Wrote linux-vps-swapping-when-ram-available-fix-1.svg')

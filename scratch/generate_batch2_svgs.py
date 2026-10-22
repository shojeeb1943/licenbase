import os

# 1. Failed cPanel Backups SVG
svg_backup = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgBackup" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="boxFail" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </linearGradient>
    <linearGradient id="boxStep" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadowB" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgBackup)"/>

  <!-- Title -->
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">cPanel &amp; WHM Backup Pipeline Failure Checkpoints</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Diagnosing staging space starvation, permission locks, and remote transport aborts</text>

  <!-- 3 Stages of Backup Pipeline -->
  <!-- Stage 1: Local Staging -->
  <g transform="translate(60, 105)" filter="url(#shadowB)">
    <rect width="250" height="315" rx="14" fill="url(#boxStep)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#0369a1" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">Stage 1: Local Staging</text>

    <text x="18" y="65" font-family="monospace" font-size="11" fill="#7dd3fc" font-weight="bold">Path: /backup or /backup/cpbackup</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Dumps MySQL databases, home directories, mailboxes, and DNS zones.</text>

    <rect x="15" y="115" width="220" height="90" rx="8" fill="url(#boxFail)" stroke="#f43f5e" stroke-width="1"/>
    <text x="25" y="137" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fecdd3">Critical Failure Point:</text>
    <text x="25" y="157" font-family="sans-serif" font-size="11" fill="#ffe4e6">• Disk exhaustion on /backup</text>
    <text x="25" y="175" font-family="sans-serif" font-size="11" fill="#ffe4e6">• Requires 1.5x - 2x account size</text>
    <text x="25" y="193" font-family="monospace" font-size="10" fill="#fecaca">Error: No space left on device</text>

    <rect x="15" y="218" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="238" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Log Signature:</text>
    <text x="25" y="258" font-family="monospace" font-size="10" fill="#94a3b8">/usr/local/cpanel/logs/cpbackup/</text>
    <text x="25" y="278" font-family="monospace" font-size="10" fill="#fbbf24">pkgacct: mysqldump exited 1</text>
  </g>

  <!-- Stage 2: Compression & Packaging -->
  <g transform="translate(355, 105)" filter="url(#shadowB)">
    <rect width="250" height="315" rx="14" fill="url(#boxStep)" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#7e22ce" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc" text-anchor="middle">Stage 2: Gzip / Zstd Archiving</text>

    <text x="18" y="65" font-family="monospace" font-size="11" fill="#d8b4fe" font-weight="bold">Command: pigz / gzip / zstd</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Compresses staging folder into standalone cpmove-user.tar.gz archive.</text>

    <rect x="15" y="115" width="220" height="90" rx="8" fill="url(#boxFail)" stroke="#f43f5e" stroke-width="1"/>
    <text x="25" y="137" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fecdd3">Critical Failure Point:</text>
    <text x="25" y="157" font-family="sans-serif" font-size="11" fill="#ffe4e6">• Permission denied on /home/user</text>
    <text x="25" y="175" font-family="sans-serif" font-size="11" fill="#ffe4e6">• Locked files or broken symlinks</text>
    <text x="25" y="193" font-family="monospace" font-size="10" fill="#fecaca">Error: tar: file changed as read</text>

    <rect x="15" y="218" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="238" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Log Signature:</text>
    <text x="25" y="258" font-family="monospace" font-size="10" fill="#94a3b8">queue/current.log</text>
    <text x="25" y="278" font-family="monospace" font-size="10" fill="#fbbf24">Backup timeout: 7200s exceeded</text>
  </g>

  <!-- Stage 3: Remote Transport -->
  <g transform="translate(650, 105)" filter="url(#shadowB)">
    <rect width="250" height="315" rx="14" fill="url(#boxStep)" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#059669" fill-opacity="0.3"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">Stage 3: Transport &amp; Pruning</text>

    <text x="18" y="65" font-family="monospace" font-size="11" fill="#6ee7b7" font-weight="bold">Destinations: S3 / SFTP / WebDAV</text>
    <text x="18" y="90" font-family="sans-serif" font-size="11" fill="#cbd5e1">Streams completed tarball to remote backup destination and purges expired sets.</text>

    <rect x="15" y="115" width="220" height="90" rx="8" fill="url(#boxFail)" stroke="#f43f5e" stroke-width="1"/>
    <text x="25" y="137" font-family="sans-serif" font-size="11" font-weight="bold" fill="#fecdd3">Critical Failure Point:</text>
    <text x="25" y="157" font-family="sans-serif" font-size="11" fill="#ffe4e6">• SSH / SSL Handshake timeout</text>
    <text x="25" y="175" font-family="sans-serif" font-size="11" fill="#ffe4e6">• Remote S3 quota reached</text>
    <text x="25" y="193" font-family="monospace" font-size="10" fill="#fecaca">Error: Transport error: Net::FTP</text>

    <rect x="15" y="218" width="220" height="85" rx="8" fill="#0f172a" stroke="#1e293b"/>
    <text x="25" y="238" font-family="sans-serif" font-size="11" font-weight="bold" fill="#f8fafc">Log Signature:</text>
    <text x="25" y="258" font-family="monospace" font-size="10" fill="#94a3b8">/var/cpanel/backups/</text>
    <text x="25" y="278" font-family="monospace" font-size="10" fill="#fbbf24">Failed to prune destination</text>
  </g>

  <!-- Bottom Run Command -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Force CLI Run:</text>
  <text x="200" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">/usr/local/cpanel/bin/backup --force</text>
  <text x="500" y="455" font-family="monospace" font-size="11" fill="#a855f7">|</text>
  <text x="520" y="455" font-family="monospace" font-size="11" fill="#34d399" font-weight="bold">Check Logs:</text>
  <text x="615" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">tail -f /usr/local/cpanel/logs/cpbackup/*.log</text>
</svg>'''

# 2. Exim Mail Queue SVG
svg_exim = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgExim" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b132b"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="gradAmber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="gradRed" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#be123c"/>
      <stop offset="100%" stop-color="#881337"/>
    </linearGradient>
    <filter id="shadowE" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="480" fill="url(#bgExim)"/>

  <!-- Title -->
  <text x="480" y="42" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">WHM &amp; Exim Mail Queue Triage and Unsticking Lifecycle</text>
  <text x="480" y="68" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Inspecting active messages, handling frozen spam, repairing retry databases, and flushing queues</text>

  <!-- Left: Ingestion & Statuses -->
  <g transform="translate(60, 105)" filter="url(#shadowE)">
    <rect width="250" height="315" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="250" height="38" rx="14" fill="#334155"/>
    <text x="125" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#f8fafc" text-anchor="middle">Queue Message States</text>

    <!-- States -->
    <rect x="15" y="52" width="220" height="55" rx="8" fill="#0f172a" stroke="#10b981"/>
    <text x="25" y="73" font-family="monospace" font-size="11" fill="#34d399" font-weight="bold">Active / Undelivered</text>
    <text x="25" y="93" font-family="sans-serif" font-size="11" fill="#cbd5e1">Queued awaiting DNS or SMTP connection.</text>

    <rect x="15" y="115" width="220" height="85" rx="8" fill="url(#gradAmber)" stroke="#f59e0b"/>
    <text x="25" y="137" font-family="monospace" font-size="11" fill="#fde68a" font-weight="bold">Retry Delay (Deferred)</text>
    <text x="25" y="157" font-family="sans-serif" font-size="11" fill="#fef3c7">Remote server returned 4xx Greylist.</text>
    <text x="25" y="177" font-family="sans-serif" font-size="10" fill="#fde68a">Exim database tracks retry interval.</text>
    <text x="25" y="191" font-family="monospace" font-size="10" fill="#fde68a">/var/spool/exim/db/retry</text>

    <rect x="15" y="208" width="220" height="95" rx="8" fill="url(#gradRed)" stroke="#f43f5e"/>
    <text x="25" y="230" font-family="monospace" font-size="11" fill="#fecdd3" font-weight="bold">*** Frozen *** State</text>
    <text x="25" y="250" font-family="sans-serif" font-size="11" fill="#ffe4e6">Delivery failed; bounce also unroutable.</text>
    <text x="25" y="270" font-family="sans-serif" font-size="11" fill="#ffe4e6">Classic hallmark of outbound spam.</text>
    <text x="25" y="288" font-family="monospace" font-size="10" fill="#fecdd3">exim -bpr | grep frozen</text>
  </g>

  <!-- Middle Arrow -->
  <g transform="translate(330, 240)">
    <line x1="0" y1="0" x2="50" y2="0" stroke="#38bdf8" stroke-width="4"/>
    <polygon points="55,0 42,-6 42,6" fill="#38bdf8"/>
    <text x="25" y="-12" font-family="monospace" font-size="11" fill="#7dd3fc" text-anchor="middle">Triage</text>
  </g>

  <!-- Right: CLI Diagnostic Commands -->
  <g transform="translate(400, 105)" filter="url(#shadowE)">
    <rect width="500" height="315" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="500" height="38" rx="14" fill="#0284c7" fill-opacity="0.25"/>
    <text x="250" y="25" font-family="sans-serif" font-size="13" font-weight="700" fill="#7dd3fc" text-anchor="middle">Precision Exim Queue Command Playbook</text>

    <!-- Inspection block -->
    <rect x="20" y="52" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="73" font-family="sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Inspect Messages Without Modifying Queue:</text>
    <text x="32" y="93" font-family="monospace" font-size="11" fill="#f1f5f9">exim -Mvh &lt;message-id&gt;   <tspan fill="#94a3b8"># View full RFC headers &amp; auth script</tspan></text>
    <text x="32" y="113" font-family="monospace" font-size="11" fill="#f1f5f9">exim -Mvb &lt;message-id&gt;   <tspan fill="#94a3b8"># View message body snippet</tspan></text>

    <!-- Safe flush block -->
    <rect x="20" y="135" width="460" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="32" y="156" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Safely Flush Legitimate Outbound Mail:</text>
    <text x="32" y="176" font-family="monospace" font-size="11" fill="#f1f5f9">exim -qf                 <tspan fill="#94a3b8"># Force delivery run of pending queue</tspan></text>
    <text x="32" y="196" font-family="monospace" font-size="11" fill="#f1f5f9">exim -qff                <tspan fill="#94a3b8"># Force queue delivery, ignoring retry delays</tspan></text>

    <!-- Purge frozen spam block -->
    <rect x="20" y="218" width="460" height="85" rx="8" fill="#1e293b" stroke="#f43f5e"/>
    <text x="32" y="239" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fb7185">3. Purge Frozen Spam &amp; Repair Retry Databases:</text>
    <text x="32" y="259" font-family="monospace" font-size="11" fill="#fecdd3">exiqgrep -z -i | xargs exim -Mrm  <tspan fill="#fca5a5"># Remove frozen spam only</tspan></text>
    <text x="32" y="279" font-family="monospace" font-size="11" fill="#f1f5f9">/usr/sbin/exim_tidydb -t 1d /var/spool/exim retry</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="60" y="435" width="840" height="30" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="455" font-family="monospace" font-size="11" fill="#fbbf24" font-weight="bold">Check Total Count:</text>
  <text x="220" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">exim -bpc</text>
  <text x="320" y="455" font-family="monospace" font-size="11" fill="#38bdf8">|</text>
  <text x="340" y="455" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">Search by Sender:</text>
  <text x="475" y="455" font-family="monospace" font-size="11" fill="#f1f5f9">exiqgrep -f "user@domain.com"</text>
  <text x="730" y="455" font-family="monospace" font-size="11" fill="#34d399">|</text>
  <text x="745" y="455" font-family="sans-serif" font-size="11" fill="#a7f3d0">LicenBase MTA Guide</text>
</svg>'''

with open('assets/img/blog/fix-failed-cpanel-backups-disk-space-logs-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_backup)
print('Wrote fix-failed-cpanel-backups-disk-space-logs-1.svg')

with open('assets/img/blog/troubleshoot-stuck-exim-mail-queue-whm-1.svg', 'w', encoding='utf-8') as f:
    f.write(svg_exim)
print('Wrote troubleshoot-stuck-exim-mail-queue-whm-1.svg')

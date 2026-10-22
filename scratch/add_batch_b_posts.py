# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path("c:/dev/Licenbase.com").resolve()))

import blog_posts

post_shell = {
    "slug": "detect-hidden-web-shells-linux-vps-commands",
    "title": "How to Detect Hidden Web Shells on a Linux VPS: Commands",
    "seo_title": "Detect Hidden Web Shells on Linux VPS: Guide",
    "description": "Learn how to find and remove hidden PHP web shells on a Linux VPS. Practical grep commands, mtime/ctime audits, and automated Imunify360 quarantine.",
    "excerpt": "Detect and eliminate hidden web shells on your Linux VPS using precision shell commands, file timeline analysis, and Imunify360.",
    "category": "How-to",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "Linux VPS hidden web shell detection workflow and command playbook diagram",
    "faq": [
        ("What is a web shell and how does it get onto a Linux server?", "A web shell is a malicious script (typically written in PHP) that provides remote attackers with command execution, file manipulation, and database access over HTTP. They are usually uploaded through unpatched WordPress vulnerabilities, compromised admin credentials, or insecure file upload forms."),
        ("Why can't standard antivirus scanners always find web shells?", "Modern web shells use advanced evasion techniques, including multi-stage base64 encoding, rot13 encryption, string concatenation, variable functions, and timestamp manipulation (timestomping) to blend in with legitimate CMS core files."),
        ("What is the difference between mtime and ctime when hunting web shells?", "mtime (modification time) records when file content was changed, but attackers can easily forge mtime using the Linux 'touch' command. ctime (change time) records when file metadata or inode attributes changed and cannot be easily forged by userland scripts, making it far more reliable for forensic audits."),
        ("How does Imunify360 handle zero-day web shells automatically?", "An Imunify360 license includes Proactive Defense, which analyzes PHP script behavior in memory prior to execution. Even if a web shell is completely obfuscated, if it attempts to spawn a system shell or execute arbitrary remote commands, Imunify360 blocks the execution instantly.")
    ],
    "og": {
        "headline": "Detect Hidden Web Shells",
        "subtitle": "Commands and tools for Linux VPS servers",
        "icon": "shield-check"
    },
    "related": [
        ("imunify360-license", "Imunify360 license"),
        ("cpanel-license", "cPanel & WHM license")
    ],
    "body": """
<p class="text-lg text-gray-600">Discovering that an attacker has established an interactive foothold on your Linux server is every administrator's nightmare. A <strong>web shell</strong> is a malicious script—almost always written in PHP—that converts ordinary HTTP requests into arbitrary command-line execution. Once planted inside a web root, a web shell allows attackers to dump MySQL databases, modify sensitive PHP configuration files, plant SEO spam redirects, and pivot across virtual hosts. Because attackers use polymorphic obfuscation and timestamp spoofing, standard keyword searches frequently fail. This technical guide outlines how to uncover stealthy web shells on a Linux VPS using precision terminal commands, file timeline forensics, and automated <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 proactive defense</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Anatomy of Stealth Web Shells</h2>
  <p>Primitive web shells from a decade ago (such as c99 or r57) were thousands of lines of plain-text PHP code that were trivial for basic ClamAV signatures to flag. Modern web shells, by contrast, are microscopic and heavily obfuscated.</p>
  """ + blog_posts.figure("detect-hidden-web-shells-linux-vps-commands", 1, "Linux VPS hidden web shell detection workflow and command playbook diagram", "Figure 1: Common web shell evasion vectors and terminal forensic investigation workflow.") + """
  <p>Attackers conceal web shells using three distinct strategies:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Microscopic "One-Liners":</strong> Single lines of code that execute arbitrary payload inputs passed via HTTP cookies or headers, such as <code>&lt;?php @eval($_POST['cmd']); ?&gt;</code> or <code>call_user_func($_GET['func'], $_GET['arg']);</code>.</li>
    <li><strong>Obfuscated Execution Wrappers:</strong> Payloads encoded with multi-layer <code>base64_decode()</code>, <code>gzinflate()</code>, and hexadecimal string variables to evade static string pattern matching.</li>
    <li><strong>Timestomping &amp; Masquerading:</strong> Attackers forge the file's modification timestamp (<code>mtime</code>) to match legitimate WordPress core files from 2021, and name the file <code>wp-includes/class-wp-cache.php</code> or hide it inside <code>/wp-content/uploads/2024/05/</code> disguised as a JPEG or text file.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 1: Hunting Dangerous PHP Execution Functions</h2>
  <p>Web shells must ultimately pass strings to the operating system or the PHP evaluation engine. Using regular expression grep queries across your web roots can instantly highlight anomalous execution functions:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Scan all hosted accounts for dangerous OS execution calls in upload directories</p>
    <p>grep -rP "(passthru|shell_exec|system|exec|popen|proc_open)\s*\(" /home/*/public_html/wp-content/uploads/ --include="*.php"</p>
    <p class="text-gray-400 mt-2"># Search for obfuscated evaluation wrappers</p>
    <p>grep -rP "(eval|assert)\s*\(\s*(base64_decode|gzinflate|str_rot13)" /home/*/public_html/ --include="*.php"</p>
  </div>
  <p>Legitimate WordPress plugins rarely—if ever—place PHP executable files inside <code>/wp-content/uploads/</code>. Any PHP file discovered inside an uploads folder should be treated as an immediate high-severity breach indicator.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 2: Detecting Timestomping via ctime vs mtime Forensics</h2>
  <p>When an attacker compromises a site, they frequently run <code>touch -r index.php webshell.php</code> to clone the modification timestamp of a valid file. While this fools basic date sorting (<code>ls -l</code>), Linux maintains a separate attribute: the <strong>inode change time (<code>ctime</code>)</strong>.</p>
  <p>The <code>ctime</code> timestamp updates whenever file ownership, permissions, or inode attributes are modified. Inode change timestamps cannot be easily forged by standard userland scripts:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Find files whose inode changed in the last 72 hours, excluding standard cache</p>
    <p>find /home/*/public_html -type f -name "*.php" -ctime -3 ! -path "*/wp-content/cache/*" -ls</p>
    <p class="text-gray-400 mt-2"># Compare mtime against ctime on a suspicious file</p>
    <p>stat /home/username/public_html/wp-content/uploads/wp-signup.php</p>
  </div>
  <p>If <code>Modify</code> shows a date from three years ago, but <code>Change</code> shows yesterday at 03:14 AM, the file was timestomped.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 3: Checking Active Network Sockets and Running Web Processes</h2>
  <p>Interactive web shells often spawn outbound reverse shells connecting to attacker-controlled listener IPs. Audit active processes and listening sockets for anomalies:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Inspect active network sockets not belonging to standard hosting ports</p>
    <p>ss -tulpn | grep -v -E ":(80|443|22|2083|2087|2082|2086|3306|53|25|587|993|995|110)"</p>
    <p class="text-gray-400 mt-2"># Search for bash or sh processes spawned by web server users (nobody, www-data, cpanel users)</p>
    <p>ps aux | grep -E "(bash|sh|python|perl|nc|ncat)" | grep -v "root"</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Automated Detection and Neutralization with Imunify360</h2>
  <p>Manual command-line hunting is essential for incident forensics, but running shell scripts manually cannot protect servers against continuous zero-day threats. Deploying an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 security license</a> on your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a> delivers complete automated coverage.</p>
  <p>Imunify360 combines real-time inotify file monitoring with <strong>Proactive Defense</strong>. Proactive Defense operates inside the PHP runtime, analyzing script data flow rather than relying solely on file hashes. Even if an attacker develops a brand-new, unseen web shell that is 100% unique, the moment it attempts to invoke unauthorized system calls, Imunify360 neutralizes the process and isolates the file instantly.</p>
  <p>Keep your server bulletproof: acquire a cost-effective <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 license</a> with rapid automated deployment from LicenBase today.</p>
</section>
"""
}

post_session = {
    "slug": "protect-cpanel-session-hijacking-cookie-theft",
    "title": "Protect cPanel from Session Hijacking and Cookie Theft",
    "seo_title": "Protect cPanel from Session Hijacking & Theft",
    "description": "Protect cPanel & WHM from infostealer malware, session hijacking, and stolen cookie replays. Enforce IP binding, short timeouts, and strict security.",
    "excerpt": "Harden cPanel and WHM against cookie theft and session hijacking caused by infostealer malware like RedLine and Lumma.",
    "category": "Guide",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "cPanel and WHM session hijacking defense architecture and cookie hardening diagram",
    "faq": [
        ("How do attackers steal cPanel session cookies?", "Attackers deploy infostealer malware (such as RedLine, Vidar, or Lumma Stealer) onto client computers via phishing or pirated software. The malware extracts saved session tokens (like 'cpsession') and browser cookies from local SQLite databases and transmits them to attacker command-and-control servers."),
        ("Why doesn't Two-Factor Authentication (2FA) stop stolen cookie attacks?", "Two-Factor Authentication is verified only during the initial login handshake to establish the session. Once authenticated, cPanel issues a session token. If an attacker imports that active session token into an anti-detect browser, they bypass the login screen and 2FA prompt completely unless Cookie IP Validation is enforced."),
        ("What does 'Cookie IP Validation' in WHM Tweak Settings do?", "Cookie IP Validation verifies the client IP address on every single HTTP request. When set to 'Strict', if an incoming request carrying a valid session cookie originates from an IP address different from the IP that created the session, cPanel immediately invalidates the cookie and terminates the session."),
        ("How can I immediately kill all active user sessions across WHM via CLI?", "Log into your server via SSH as root and clear the raw session directory with 'rm -f /var/cpanel/sessions/raw/*'. This instantly logs out every connected user from both cPanel and WHM.")
    ],
    "og": {
        "headline": "Defend cPanel Sessions",
        "subtitle": "Stop cookie theft and infostealer replays",
        "icon": "lock"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("imunify360-license", "Imunify360 license")
    ],
    "body": """
<p class="text-lg text-gray-600">Over the past several years, credential theft has shifted from traditional brute-force dictionary attacks to sophisticated <strong>session hijacking and cookie theft</strong>. Armed with modern infostealer Trojans (such as Lumma, RedLine, and Vidar), threat actors silently harvest active browser cookies from administrators and website owners. When an attacker acquires an active <code>cpsession</code> cookie or WHM authentication token, they can replay it inside anti-detect browsers—completely bypassing standard passwords and even Two-Factor Authentication (2FA). Protecting your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a> against session hijacking requires enforcing kernel and control panel security policies that bind sessions strictly to trusted client IPs and minimize session lifespans.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>The Anatomy of an Infostealer Cookie Replay Attack</h2>
  <p>To understand why traditional security controls fail against cookie theft, consider the authentication sequence:</p>
  """ + blog_posts.figure("protect-cpanel-session-hijacking-cookie-theft", 1, "cPanel and WHM session hijacking defense architecture and cookie hardening diagram", "Figure 1: Infostealer cookie extraction and WHM strict IP session validation countermeasures.") + """
  <ol class="list-decimal pl-6 space-y-2 text-gray-700">
    <li>An administrator logs into WHM or cPanel (ports 2083/2087) using valid credentials and completes a 2FA TOTP prompt.</li>
    <li>cPanel generates an authenticated session token, written to <code>/var/cpanel/sessions/raw/</code> on the server and stored in the administrator's browser cookie storage (e.g., <code>cpsession:root:randomhash</code>).</li>
    <li>Infostealer malware executing on the administrator's workstation extracts the browser's encrypted cookie database, unprotects the key, and transmits the payload to a Telegram bot or C2 server.</li>
    <li>The threat actor imports the <code>cpsession</code> cookie into an anti-detect browser (such as AdsPower or Dolphin Anty). Because the server receives a valid session token, it serves the WHM administrative dashboard without requesting a password or 2FA challenge!</li>
  </ol>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Countermeasure 1: Enforce Strict Cookie IP Validation</h2>
  <p>The single most powerful mitigation against session replay is <strong>Cookie IP Validation</strong>. When enabled, cPanel cross-references the IP address sending the HTTP request against the IP address that originally completed the login handshake.</p>
  <p>To configure this in WHM:</p>
  <ol class="list-decimal pl-6 space-y-2 text-gray-700">
    <li>Log into WHM as <code>root</code>.</li>
    <li>Navigate to <em>Home &raquo; Server Configuration &raquo; Tweak Settings</em>.</li>
    <li>Select the <strong>Security</strong> tab.</li>
    <li>Locate <strong>Cookie IP validation</strong>. Set this option to <strong>Strict</strong> (or <em>Loose</em> if administrators use mobile broadband networks with dynamic subnets).</li>
    <li>Click <strong>Save</strong> at the bottom of the page.</li>
  </ol>
  <p>Under <strong>Strict</strong> mode, the moment an attacker in another country attempts to replay the stolen session cookie, cPanel detects the IP mismatch, terminates the session, and logs the security violation.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Countermeasure 2: Restrict Session Inactivity Timeouts</h2>
  <p>By default, administrative sessions may remain valid for several hours of inactivity. Reducing the idle session timeout limits the temporal window an attacker has to exploit stolen cookies.</p>
  <p>In WHM <em>Tweak Settings &raquo; System</em>, adjust these settings:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Session timeout:</strong> Reduce from the default to <strong>900 seconds (15 minutes)</strong> or <strong>1800 seconds (30 minutes)</strong>.</li>
    <li><strong>Keep-alive interval:</strong> Disable keep-alive or reduce interval time to prevent unattended browser tabs from keeping tokens indefinitely refreshed.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Countermeasure 3: Terminating Sessions and Active Auditing via CLI</h2>
  <p>If you suspect an administrative account or customer has had their credentials stolen, immediately terminate all active sessions server-wide from the command line:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># List all active sessions across WHM and cPanel</p>
    <p>whmapi1 list_sessions</p>
    <p class="text-gray-400 mt-2"># Purge all raw active session files immediately</p>
    <p>rm -f /var/cpanel/sessions/raw/*</p>
    <p class="text-gray-400 mt-2"># Restart cPanel services to invalidate cached session handles</p>
    <p>/scripts/restartsrv_cpsrvd</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Architectural Hardening with CageFS and cPHulk</h2>
  <p>On multi-tenant servers, session protection must also prevent lateral movement between hosted users. Deploying a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux OS license</a> with <strong>CageFS</strong> encapsulates each cPanel user in an isolated virtualized filesystem, preventing malicious scripts in one account from accessing <code>/tmp</code> or reading session storage from neighboring accounts.</p>
  <p>Furthermore, ensure <strong>cPHulk Brute Force Protection</strong> is active in WHM to monitor failed login attempts and automatically ban IPs attempting credential stuffing attacks. Pairing hardened session management with an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 security license</a> ensures that even if an attacker gains entry to a website, automated WAF and malware scanning will block subsequent shell uploads and privilege escalation.</p>
</section>
"""
}

post_csf_imunify = {
    "slug": "imunify360-vs-csf-firewall-security-stack-comparison",
    "title": "Imunify360 vs CSF Firewall: Which Security Stack to Pick?",
    "seo_title": "Imunify360 vs CSF Firewall: Security Stack",
    "description": "Compare Imunify360 and CSF (ConfigServer Security & Firewall). Analyze Layer 3/4 network filtering versus Layer 7 proactive web application defense.",
    "excerpt": "Compare Imunify360 and CSF Firewall for hosting servers. Learn key differences between network firewalls and proactive AI defense.",
    "category": "Comparison",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "Imunify360 versus ConfigServer Security and Firewall architectural comparison diagram",
    "faq": [
        ("Can I run Imunify360 and CSF Firewall simultaneously on the same server?", "Yes. Imunify360 can integrate directly with CSF. When CSF is detected, Imunify360 delegates low-level iptables port management to CSF while handling advanced Layer 7 Web Application Firewall (WAF), proactive PHP defense, and malware scanning internally. However, Imunify360's native ipset-based firewall is faster and many hosts choose to run Imunify360 standalone."),
        ("Is CSF Firewall sufficient on its own for a WordPress hosting server?", "No. CSF is primarily a Layer 3 and Layer 4 network packet filter and log watcher (LFD). It excels at blocking unauthorized port scans, SSH brute-force attempts, and SYN floods, but it is completely blind to malicious PHP malware execution, SQL injection, or cross-site scripting inside encrypted HTTPS traffic."),
        ("What makes Imunify360 superior for shared hosting environments?", "Imunify360 includes Proactive Defense, automated real-time malware cleanup, ModSecurity rulesets powered by global herd immunity, live kernel patching without reboots (KernelCare), and an automated CAPTCHA challenge screen that stops bots without human intervention."),
        ("How much does an Imunify360 license cost through LicenBase?", "LicenBase provides genuine automated Imunify360 licenses starting at just $6.00 per month, offering dramatic cost savings over retail pricing for VPS and dedicated hosting providers.")
    ],
    "og": {
        "headline": "Imunify360 vs CSF",
        "subtitle": "Network firewall vs full application security",
        "icon": "shield-check"
    },
    "related": [
        ("imunify360-license", "Imunify360 license"),
        ("cpanel-license", "cPanel & WHM license")
    ],
    "body": """
<p class="text-lg text-gray-600">Selecting the right security stack is one of the most consequential decisions for system administrators running web hosting infrastructure. For over fifteen years, <strong>ConfigServer Security &amp; Firewall (CSF)</strong> has been the standard free, open-source firewall of choice across cPanel servers. However, as web threats have evolved from basic network port scans to complex PHP-based web shells, remote code execution (RCE), and automated bot floods, many hosting providers find that CSF alone is no longer enough. Enter <strong>Imunify360</strong>—CloudLinux's AI-driven, multi-layer security suite. This comparison analyzes the architectural differences between CSF and Imunify360 to help you determine the optimal defense stack for your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel VPS or dedicated server</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Architectural Scope: Layer 3/4 vs Layer 7 Defense</h2>
  <p>The fundamental distinction between CSF and Imunify360 lies in the OSI network layers they inspect:</p>
  """ + blog_posts.figure("imunify360-vs-csf-firewall-security-stack-comparison", 1, "Imunify360 versus ConfigServer Security and Firewall architectural comparison diagram", "Figure 1: Architectural comparison between Layer 3/4 packet filtering (CSF) and Layer 7 deep inspection (Imunify360).") + """
  <p><strong>ConfigServer Security &amp; Firewall (CSF)</strong> operates primarily at <strong>Layers 3 and 4</strong> (Network and Transport). It is a management wrapper around Linux <code>iptables</code> and <code>nftables</code>, bundled with a Login Failure Daemon (<code>lfd</code>). It excels at:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li>Opening and closing TCP/UDP network ports (e.g., SSH, HTTP, SMTP).</li>
    <li>Rate-limiting SYN floods and ICMP ping requests.</li>
    <li>Scanning log files (<code>/var/log/secure</code>, <code>/var/log/exim_mainlog</code>) to block IP addresses that repeatedly fail authentication.</li>
  </ul>
  <p>However, once an HTTP request enters port 443 over TLS encryption, CSF is completely blind to its payload. If a visitor sends an SQL injection query or uploads an obfuscated PHP web shell through an unpatched WordPress plugin, CSF forwards the packet straight to Apache or LiteSpeed.</p>
  <p><strong>Imunify360</strong>, by contrast, delivers <strong>full-stack defense across Layers 3 through 7</strong>. It combines high-performance network filtering with real-time web application firewalling (WAF), automated file malware scanning, memory-level script execution monitoring, and automated CAPTCHA challenges.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Feature-by-Feature Technical Comparison</h2>
  <div class="overflow-x-auto rounded-xl border border-gray-200">
    <table class="w-full min-w-[34rem] text-sm">
      <thead>
        <tr>
          <th class="border-b border-gray-200 bg-gray-50 px-4 py-3 text-left font-bold text-gray-700">Security Capability</th>
          <th class="border-b border-gray-200 bg-gray-50 px-4 py-3 text-left font-bold text-gray-700">CSF + LFD</th>
          <th class="border-b border-gray-200 bg-gray-50 px-4 py-3 text-left font-bold text-gray-700">Imunify360</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Network Firewall</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (iptables/nftables)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (High-speed ipset)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Brute-Force Login Defense</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Regex log monitoring)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Multi-protocol PAM/WAF)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Web Application Firewall (WAF)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-red-500">No (Requires manual ModSec)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Automated low-false-positive WAF)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Proactive PHP Defense</td>
          <td class="border-b border-gray-100 px-4 py-3 text-red-500">No</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Runtime memory heuristic blocking)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Malware Scanner &amp; Cleanup</td>
          <td class="border-b border-gray-100 px-4 py-3 text-red-500">No (Requires ClamAV or Maldet)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Automated real-time file disinfection)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Automated Bot CAPTCHA</td>
          <td class="border-b border-gray-100 px-4 py-3 text-red-500">No (Drops packets immediately)</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Web splash verification)</td>
        </tr>
        <tr>
          <td class="border-b border-gray-100 px-4 py-3 font-semibold text-gray-900">Rebootless Kernel Patching</td>
          <td class="border-b border-gray-100 px-4 py-3 text-red-500">No</td>
          <td class="border-b border-gray-100 px-4 py-3 text-green-600">Yes (Includes KernelCare)</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>The Key Advantage: Proactive Defense &amp; Herd Immunity</h2>
  <p>The definitive feature that sets Imunify360 apart from traditional tools is <strong>Proactive Defense</strong>. While traditional antivirus scanners rely on static signature databases that can take days to update after a new vulnerability is disclosed, Proactive Defense examines the execution behavior of PHP code directly in memory. If a script attempts to execute unauthorized commands or establish an unexpected network socket, Imunify360 blocks the execution instantly—neutralizing zero-day exploits before a signature even exists.</p>
  <p>Additionally, Imunify360 leverages <strong>Global Herd Immunity</strong>. When a botnet attacks an Imunify360-protected server in Tokyo, that attacker's IP address is immediately published to CloudLinux's global threat intelligence cloud, blacklisting the IP across all Imunify360 servers worldwide within milliseconds.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Can You Run CSF and Imunify360 Together?</h2>
  <p>Yes. Imunify360 includes native integration with CSF. If you have an established CSF installation with custom port forwarding or internal IP whitelists, Imunify360 detects CSF upon installation and toggles into <em>CSF Cooperation Mode</em>. In this mode, CSF continues managing network port states and LFD bans, while Imunify360 handles Layer 7 WAF, malware scanning, and proactive execution defense.</p>
  <p>However, for new deployments, running Imunify360 standalone using its native <code>ipset</code> firewall provides superior performance and eliminates configuration redundancy.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Verdict &amp; Recommendation</h2>
  <p>If you run a simple private VPS hosting only your personal static websites and need a lightweight tool to protect SSH and fail2ban, CSF is completely adequate and free. However, if you operate a shared hosting business, agency server, or e-commerce VPS hosting WordPress, Magento, or WHMCS, relying solely on CSF leaves your infrastructure exposed to modern application exploits.</p>
  <p>Upgrading to an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 security license</a> automates malware removal, eliminates false-positive customer lockouts, and protects against zero-day exploits. LicenBase offers genuine, automated Imunify360 licenses starting at just $6.00/month with instant activation.</p>
</section>
"""
}

post_oom = {
    "slug": "fix-oom-killer-out-of-memory-cpanel-server",
    "title": "How to Fix OOM Killer Out of Memory on a cPanel Server",
    "seo_title": "Fix OOM Killer Out of Memory on cPanel Server",
    "description": "Fix Linux Out of Memory (OOM) Killer crashes on cPanel & WHM. Learn how to protect MySQL from termination, adjust oom_score_adj, and tune server RAM.",
    "excerpt": "Diagnose and prevent Linux Out of Memory (OOM) Killer crashes on cPanel servers. Protect MySQL and configure CloudLinux memory caps.",
    "category": "How-to",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "Linux kernel Out of Memory OOM killer lifecycle and cPanel triage diagram",
    "faq": [
        ("What is the Linux OOM Killer and why does it crash MySQL on cPanel?", "The Linux kernel Out of Memory (OOM) Killer is an emergency subsystem that activates when physical RAM and swap are completely exhausted. To prevent a kernel panic, it calculates an 'oom_score' for all running processes and terminates the largest memory consumer—which is almost always MySQL (mysqld) or Apache (httpd)."),
        ("Where are OOM Killer incidents logged on a cPanel server?", "OOM Killer events are logged directly by the Linux kernel. You can inspect recent termination logs by running 'dmesg -T | grep -i oom' or checking '/var/log/messages' (on RHEL/AlmaLinux) or '/var/log/syslog' (on Ubuntu) for 'Out of memory: Kill process'."),
        ("How can I prevent the Linux kernel from killing MySQL during an OOM event?", "You can adjust MySQL's OOM vulnerability score by writing '-1000' to '/proc/$(pgrep mysqld)/oom_score_adj'. An OOM score adjustment of -1000 completely immunizes the process from being terminated by the kernel, forcing it to kill abusive PHP workers instead."),
        ("How does CloudLinux prevent server-wide OOM crashes?", "CloudLinux isolates every cPanel user inside a Lightweight Virtual Environment (LVE) with hard physical memory limits (pMEM). If a user's WordPress site experiences a memory leak, only that specific user's processes are terminated, completely insulating MySQL and the core operating system from running out of RAM.")
    ],
    "og": {
        "headline": "Fix cPanel OOM Killer",
        "subtitle": "Protect MySQL and tune Linux RAM limits",
        "icon": "cpu"
    },
    "related": [
        ("cloudlinux-license", "CloudLinux OS license"),
        ("litespeed-license", "LiteSpeed license")
    ],
    "body": """
<p class="text-lg text-gray-600">You open your server monitoring dashboard to discover that MySQL has abruptly crashed, all hosted websites are displaying database connection errors, and WHM's <code>tailwatchd</code> is frantically attempting to restart the database daemon. When you check your server logs, you encounter the telltale signature: <strong>Out of memory: Kill process (mysqld)</strong>. The Linux kernel <strong>Out of Memory (OOM) Killer</strong> is a safeguard designed to prevent total operating system freezes when RAM is exhausted, but its algorithmic selection of which process to sacrifice often takes down your most critical hosting services. This guide explains how the OOM Killer operates, how to read kernel crash dumps, and how to permanently protect your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a> from memory exhaustion.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>How the Linux Kernel OOM Killer Selects a Victim</h2>
  <p>The Linux memory subsystem allows processes to allocate more virtual memory than physically exists—a concept known as <em>memory overcommit</em>. When multiple processes actively use their allocated memory simultaneously and physical RAM drops below <code>vm.min_free_kbytes</code> while swap is exhausted, the kernel activates <code>out_of_memory()</code>.</p>
  """ + blog_posts.figure("fix-oom-killer-out-of-memory-cpanel-server", 1, "Linux kernel Out of Memory OOM killer lifecycle and cPanel triage diagram", "Figure 1: Linux kernel OOM score calculation and process termination lifecycle.") + """
  <p>To choose which process to terminate, the kernel calculates an <strong><code>oom_score</code></strong> (from 0 to 1000) for every active PID based on:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li>The percentage of physical RAM consumed by the process.</li>
    <li>Process runtime and priority (root system daemons receive minor deductions).</li>
    <li>The process's manual adjustment value in <code>/proc/[PID]/oom_score_adj</code>.</li>
  </ul>
  <p>Because the database daemon (<code>mysqld</code> or <code>mariadbd</code>) maintains a massive InnoDB buffer pool to cache tables in RAM, it almost always has the highest <code>oom_score</code> on the entire server. Consequently, when an abusive PHP script runs wild, the kernel kills MySQL instead of the culprit!</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 1: Confirming the OOM Incident in System Logs</h2>
  <p>SSH into your cPanel server as <code>root</code> and query the kernel buffer to confirm whether an OOM kill occurred:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Check kernel ring buffer for OOM events with human-readable timestamps</p>
    <p>dmesg -T | grep -i -E "oom|out of memory|killed process"</p>
    <p class="text-gray-400 mt-2"># Search system log archives on AlmaLinux / RHEL</p>
    <p>grep -i "killed process" /var/log/messages</p>
  </div>
  <p>The output will reveal the exact timestamp, the memory consumption of all running processes at the moment of collapse, and the victim PID (e.g., <code>Killed process 14298 (mysqld) total-vm:4298516kB, anon-rss:2154820kB</code>).</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 2: Immunize MySQL from OOM Termination</h2>
  <p>To prevent MySQL from being sacrificed when web workers consume excessive memory, you can assign an aggressive negative score adjustment to the database service.</p>
  <p>Create a systemd override for MySQL/MariaDB:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Open systemd override editor for MySQL service</p>
    <p>systemctl edit mysql</p>
    <p class="text-gray-400 mt-2"># (On MariaDB, use: systemctl edit mariadb)</p>
  </div>
  <p>Insert the following configuration snippet and save the file:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p>[Service]</p>
    <p>OOMScoreAdjust=-1000</p>
  </div>
  <p>Reload the systemd daemon: <code>systemctl daemon-reload</code>. Setting <code>OOMScoreAdjust=-1000</code> completely immunizes MySQL from the OOM Killer. If memory exhausts in the future, the kernel will terminate the rogue PHP-FPM or Apache process instead of the database.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 3: Right-Sizing Swap Space</h2>
  <p>Many modern VPS instances are deployed without swap space, making them hyper-sensitive to momentary memory spikes. Adding a fast, NVMe-backed swap file provides the kernel with buffer space to page out idle processes during traffic bursts:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Create a 4GB swapfile</p>
    <p>fallocate -l 4G /swapfile</p>
    <p>chmod 600 /swapfile</p>
    <p>mkswap /swapfile</p>
    <p>swapon /swapfile</p>
    <p class="text-gray-400 mt-2"># Make persistent across reboots in /etc/fstab</p>
    <p>echo '/swapfile none swap sw 0 0' &gt;&gt; /etc/fstab</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Permanent Elimination of OOM Events with CloudLinux</h2>
  <p>While immunizing MySQL and adding swap prevents catastrophic downtime, it does not stop individual customers from leaking memory. The enterprise solution is deploying a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux OS license</a>.</p>
  <p>CloudLinux wraps each cPanel account inside its own Lightweight Virtual Environment (LVE) container with strict <strong>pMEM (Physical Memory)</strong> limits. When an unoptimized WordPress site consumes 1.5GB of RAM, only that specific user's processes are constrained or terminated within their private container. MySQL, Apache, and neighboring cPanel users remain completely unaffected.</p>
  <p>In addition, replacing Apache with a <a href="/litespeed-license" """ + blog_posts.LINK + """>LiteSpeed Web Server license</a> cuts PHP worker memory footprints by up to 50%, dramatically reducing baseline RAM consumption across your server.</p>
</section>
"""
}

post_swap = {
    "slug": "linux-vps-swapping-when-ram-available-fix",
    "title": "Why Is Your Linux VPS Swapping When RAM Seems Available?",
    "seo_title": "Why Linux VPS Swaps When RAM Is Available",
    "description": "Understand why Linux VPS servers use swap space even when free memory is available. Learn how vm.swappiness, page cache, and anonymous memory interact.",
    "excerpt": "Discover why Linux servers swap pages despite having available memory, and tune vm.swappiness for peak hosting performance.",
    "category": "Guide",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "Linux kernel page cache swappiness tuning and memory management architecture diagram",
    "faq": [
        ("Why does my Linux server use swap when 'free -m' shows plenty of available RAM?", "Linux distinguishes between active process memory (anonymous pages) and filesystem cache (page cache). By default, the kernel often decides it is more beneficial for overall system performance to cache frequently accessed disk files in RAM and push idle, sleeping process pages to swap."),
        ("What does the vm.swappiness setting actually control?", "The 'vm.swappiness' kernel parameter (ranging from 0 to 200, typically defaulting to 60) represents the kernel's preference balance between reclaiming page cache versus swapping out anonymous process memory. Lower numbers prioritize keeping process memory in physical RAM."),
        ("What is the optimal swappiness value for a cPanel web hosting server?", "For web hosting servers running cPanel, MySQL, and PHP-FPM, setting vm.swappiness to 10 (or 1 on high-RAM servers) is optimal. This prevents the server from swapping out idle database threads while still preserving swap as an emergency safety valve."),
        ("How can I flush used swap back into physical RAM safely?", "If you have enough free RAM to hold the swapped data, run 'swapoff -a && swapon -a' as root. The kernel will read all swapped pages from disk back into physical RAM and re-enable swap.")
    ],
    "og": {
        "headline": "Why Linux VPS Swaps",
        "subtitle": "Tune vm.swappiness and understand page cache",
        "icon": "cpu"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("cloudlinux-license", "CloudLinux OS license")
    ],
    "body": """
<p class="text-lg text-gray-600">You run <code>free -m</code> on your production Linux VPS and notice something bewildering: your server reports 4 GB of available memory, yet your swap partition is 30% full and disk I/O metrics are spiking. Why would the Linux kernel write memory pages to slow disk swap when fast physical RAM is sitting idle? This counter-intuitive behavior causes immense confusion for hosting providers and system administrators. Understanding the interplay between <strong>Anonymous memory</strong>, <strong>Page Cache</strong>, and the <strong><code>vm.swappiness</code></strong> kernel algorithm is key to optimizing your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a> for maximum responsiveness.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>How the Linux Kernel Values Disk Cache vs Idle RAM</h2>
  <p>To understand swapping behavior, you must look at how the Linux virtual memory manager categorizes RAM:</p>
  """ + blog_posts.figure("linux-vps-swapping-when-ram-available-fix", 1, "Linux kernel page cache swappiness tuning and memory management architecture diagram", "Figure 1: How the Linux kernel balances anonymous process memory against filesystem page cache.") + """
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Anonymous Memory:</strong> Memory allocated by executing programs (such as PHP-FPM workers, MySQL query caches, and Nginx buffers) that is not backed by any file on disk. The only way the kernel can free this memory is by writing it to swap.</li>
    <li><strong>Page Cache &amp; Buffers:</strong> Copies of files recently read from or written to disk. Because reading from physical RAM is orders of magnitude faster than reading from NVMe or SSD drives, Linux aggressively fills every byte of otherwise unused RAM with page cache.</li>
  </ul>
  <p>When the kernel evaluates system performance, it asks a fundamental question: <em>"Is it better to keep an idle, sleeping PHP thread in RAM that hasn't executed a query in 45 minutes, or should I swap that idle thread to disk and use that RAM to cache active MySQL database files?"</em> By default, the kernel chooses to cache the disk files—resulting in swap usage even when memory appears available.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>The Role of the vm.swappiness Kernel Parameter</h2>
  <p>The kernel's willingness to swap out anonymous process memory in favor of retaining page cache is controlled by <code>vm.swappiness</code>. The scale ranges from 0 to 100 (or up to 200 on newer kernels):</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Default (60):</strong> Standard Linux distributions (Ubuntu, AlmaLinux, Debian, CentOS) ship with swappiness set to 60. This aggressive default is designed for desktop or general-purpose machines, but is far too eager to swap on dynamic web servers.</li>
    <li><strong>Hosting Recommendation (10):</strong> Tells the kernel to aggressively favor reclaiming page cache before touching anonymous process memory, keeping PHP-FPM and MySQL threads in low-latency physical RAM.</li>
    <li><strong>Minimal (1):</strong> Tells the kernel to avoid swapping at all costs, utilizing swap only as an absolute emergency buffer to avoid an OOM Killer panic.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 1: Check Swappiness and Identify What is in Swap</h2>
  <p>Connect to your server via SSH as <code>root</code> and inspect your current swappiness value:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Check current kernel swappiness setting</p>
    <p>cat /proc/sys/vm/swappiness</p>
    <p class="text-gray-400 mt-2"># Identify which specific processes are occupying swap space</p>
    <p>for f in /proc/[0-9]*/status; do awk '/VmSwap/{swap=$2} /Name/{name=$2} /Pid/{pid=$2} END{if(swap>0) print swap, "KB -", name, "(PID " pid ")"}' $f; done | sort -n -r | head -n 15</p>
  </div>
  <p>If you discover that <code>mysqld</code> has 500 MB sitting in swap, your database queries will suffer from intermittent disk latency spikes whenever those swapped pages are referenced.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 2: Tune Swappiness for Web Hosting Environments</h2>
  <p>Lower the swappiness value immediately in runtime memory:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Apply immediately without a system reboot</p>
    <p>sysctl vm.swappiness=10</p>
    <p class="text-gray-400 mt-2"># Also tune vfs_cache_pressure to prevent retaining stale directory inodes</p>
    <p>sysctl vm.vfs_cache_pressure=50</p>
  </div>
  <p>To ensure these settings persist across server reboots, append them to <code>/etc/sysctl.conf</code>:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p>echo 'vm.swappiness = 10' &gt;&gt; /etc/sysctl.conf</p>
    <p>echo 'vm.vfs_cache_pressure = 50' &gt;&gt; /etc/sysctl.conf</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 3: Safely Purging Existing Swap into RAM</h2>
  <p>Changing <code>vm.swappiness</code> prevents future premature swapping, but it will not automatically evacuate existing swapped pages back into RAM until those pages are accessed. If your server currently has plenty of free physical memory, you can safely flush swap:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Verify free RAM exceeds current swap usage before running!</p>
    <p>free -m</p>
    <p class="text-gray-400 mt-2"># Flush swap back into physical RAM and re-enable</p>
    <p>swapoff -a &amp;&amp; swapon -a</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Enterprise Density with CloudLinux and LiteSpeed</h2>
  <p>On high-density cPanel hosting servers, fine-tuning kernel swappiness is essential, but isolating resource hogs is what prevents memory crises. Pairing your infrastructure with a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux OS license</a> restricts each user's RAM footprint, preventing rogue background scripts from triggering swap thrashing across the entire machine.</p>
  <p>Furthermore, running a <a href="/litespeed-license" """ + blog_posts.LINK + """>LiteSpeed Web Server license</a> provides native connection handling and efficient memory pooling, allowing you to host significantly more websites on the same hardware without exhausting RAM.</p>
</section>
"""
}

new_posts = [post_shell, post_session, post_csf_imunify, post_oom, post_swap]

for p in new_posts:
    slug = p["slug"]
    title = p["title"]
    seo_title = p["seo_title"]
    desc = p["description"]
    excerpt = p["excerpt"]
    alt = p["image_alt"]
    
    assert len(slug) <= 60, f"Slug too long: {len(slug)} ({slug})"
    assert len(title) <= 70, f"Title too long: {len(title)} ({title})"
    assert len(seo_title) + len(" | LicenBase") <= 60, f"SEO title too long: {len(seo_title) + 11} ({seo_title})"
    assert 110 <= len(desc) <= 160, f"Desc length error: {len(desc)} ({desc})"
    assert 100 <= len(excerpt) <= 140, f"Excerpt length error: {len(excerpt)} ({excerpt})"
    assert 40 <= len(alt) <= 125, f"Alt length error: {len(alt)} ({alt})"
    print(f"Validated: {slug}")

current_slugs = {p["slug"] for p in blog_posts.POSTS}
added = 0
for p in new_posts:
    if p["slug"] not in current_slugs:
        blog_posts.POSTS.append(p)
        added += 1
        print(f"Added {p['slug']} to POSTS list")
    else:
        print(f"Already in POSTS: {p['slug']}")

import pprint

header = '''"""Blog post definitions and metadata for LicenBase."""

LINK = 'class="text-blue-600 font-semibold hover:underline"'
H2 = 'class="text-2xl font-bold text-gray-900 mt-8 mb-3"'
H3 = 'class="text-xl font-bold text-gray-800 mt-6 mb-2"'

def figure(slug, num, alt, caption, w=800, h=420):
    return f\'\'\'<figure class="my-6 rounded-xl overflow-hidden border border-gray-200 bg-gray-900/5 p-2">
  <img src="/assets/img/blog/{slug}-{num}.svg" alt="{alt}" width="{w}" height="{h}" class="w-full h-auto rounded-lg shadow-sm" loading="lazy">
  <figcaption class="text-xs text-gray-500 text-center mt-2 px-2">{caption}</figcaption>
</figure>\'\'\'

POSTS = '''

with open("blog_posts.py", "w", encoding="utf-8") as f:
    f.write(header + pprint.pformat(blog_posts.POSTS, indent=4, width=120) + "\n")

print(f"Successfully updated blog_posts.py with {added} new posts. Total: {len(blog_posts.POSTS)}")

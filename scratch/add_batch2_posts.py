# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path("c:/dev/Licenbase.com").resolve()))

import blog_posts

post_backup = {
    "slug": "fix-failed-cpanel-backups-disk-space-logs",
    "title": "How to Fix Failed cPanel Backups: Disk Space & Logs",
    "seo_title": "How to Fix Failed cPanel Backups: Full Guide",
    "description": "Fix failed cPanel & WHM backups caused by disk exhaustion, permission errors, timeout limits, and corrupted backup transport. Inspect logs and restore backups.",
    "excerpt": "Solve failed cPanel and WHM backups. Troubleshoot disk exhaustion, staging folder permissions, and transport timeout errors.",
    "category": "How-to",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "cPanel and WHM automated backup pipeline troubleshooting workflow diagram",
    "faq": [
        ("Why does my cPanel backup fail with 'No space left on device' when my server has free storage?", "cPanel's backup daemon creates a local staging folder in '/backup' (or inside '/home') to dump databases and compress files before uploading to remote storage. Even if remote storage is unlimited, if the local staging partition lacks 1.5x to 2x the uncompressed size of the largest hosted cPanel account, the backup process aborts immediately."),
        ("Where are the master cPanel backup logs located in WHM?", "cPanel stores dated backup execution logs in '/usr/local/cpanel/logs/cpbackup/'. You can inspect the latest backup run with 'tail -f /usr/local/cpanel/logs/cpbackup/*.log' or check the active execution queue in '/var/cpanel/backups/queue/'."),
        ("How can I manually force a cPanel backup run from the command line?", "Log into your server terminal via SSH as root and execute '/usr/local/cpanel/bin/backup --force'. Running with '--force' ignores scheduled time restrictions and outputs errors directly to the terminal."),
        ("Why is JetBackup 5 recommended over native cPanel backups?", "Native cPanel backups package entire account directories into giant gzip archives, causing massive CPU and disk I/O spikes. A JetBackup 5 license enables block-level incremental backups, meaning only changed file blocks are transferred, reducing backup run times by up to 90% and offloading server I/O.")
    ],
    "og": {
        "headline": "Fix Failed cPanel Backups",
        "subtitle": "Disk space, permissions & backup logs",
        "icon": "database"
    },
    "related": [
        ("jetbackup-license", "JetBackup license"),
        ("cpanel-license", "cPanel & WHM license")
    ],
    "body": """
<p class="text-lg text-gray-600">Automated disaster recovery is the single most critical safety net for web hosting providers and system administrators. When you discover that scheduled cPanel &amp; WHM backups have silently aborted—leaving server images days or weeks out of date—the risk of catastrophic data loss becomes critical. Whether the root cause is a saturated local staging partition, permission deadlocks in <code>/home/user</code>, or SSL handshake timeouts during remote S3/SFTP transport, identifying why cPanel's <code>pkgacct</code> daemon crashed requires understanding the backup execution lifecycle. This troubleshooting guide walks through each stage of the cPanel backup pipeline, reveals how to parse master backup logs, and explains how to restore reliable disaster recovery across your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>The Anatomy of the cPanel Backup Pipeline</h2>
  <p>The native cPanel &amp; WHM backup system operates through a sequential three-phase lifecycle executed by <code>/usr/local/cpanel/bin/backup</code>:</p>
  """ + blog_posts.figure("fix-failed-cpanel-backups-disk-space-logs-1", 1, "cPanel and WHM automated backup pipeline troubleshooting workflow diagram", "Figure 1: The three stages of cPanel backup execution and primary failure points.") + """
  <ol class="list-decimal pl-6 space-y-2 text-gray-700">
    <li><strong>Phase 1: Local Staging:</strong> The backup daemon creates a temporary staging directory (by default under <code>/backup</code>). It invokes <code>mysqldump</code> to export databases, packages email accounts, collects DNS zones, and aggregates metadata into an uncompressed account structure.</li>
    <li><strong>Phase 2: Archiving &amp; Compression:</strong> The daemon spawns <code>gzip</code>, <code>pigz</code>, or <code>zstd</code> to compress the staging directory into a standalone <code>cpmove-user.tar.gz</code> archive.</li>
    <li><strong>Phase 3: Remote Transport &amp; Pruning:</strong> If remote destinations (such as Amazon S3, Google Drive, or remote SFTP/rsync servers) are configured, cPanel transmits the archive over the network and purges expired retention snapshots according to your retention policy.</li>
  </ol>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Failure Point 1: Staging Disk Exhaustion</h2>
  <p>The most frequent cause of backup failure is inadequate free disk space on the local staging partition. Even if your remote Amazon S3 or Wasabi bucket has 50 Terabytes of free space, cPanel <strong>must assemble the uncompressed archive locally</strong> before transferring it.</p>
  <p>If an account has a 40 GB database and 60 GB of user files, the local partition requires at least 150 GB of temporary headspace to dump the SQL tables and compress the archive. When disk space runs out during a MySQL dump, the process aborts with:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-red-400">mysqldump: Error: 'No space left on device' when writing to file '/backup/cpbackup/daily/username/mysql/dbname.sql'</p>
    <p class="text-red-400">[pkgacct] Error: mysqldump returned error code 1</p>
  </div>
  <p>To inspect your backup mount point, connect via SSH as <code>root</code> and check disk allocation:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Check disk space on all mounted filesystems</p>
    <p>df -h</p>
    <p class="text-gray-400 mt-2"># Check inode exhaustion (running out of inodes causes identical failures)</p>
    <p>df -i</p>
  </div>
  <p>In WHM under <em>Home &raquo; Backup &raquo; Backup Configuration</em>, review the <strong>Minimum Free Space</strong> threshold (default 5%). If the partition drops below this percentage, WHM cancels the entire backup run. You can configure cPanel to stage backups directly inside the user's home directory (if <code>/home</code> is on a larger dedicated disk) by toggling <em>Backup Staging Directory</em>.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Failure Point 2: File Permission and Ownership Deadlocks</h2>
  <p>When cPanel packages files, it operates under the user's UID to prevent privilege escalation. If an administrator uploaded files via root SSH into <code>/home/user/public_html</code> with permissions set to <code>root:root 0600</code>, the user-level tar process will fail with <code>Permission denied</code>.</p>
  <p>Similarly, broken symbolic links pointing outside the home directory or circular symlinks created by backup plugins can trap the archiving process in an infinite loop until the backup timeout limit is exceeded.</p>
  <p>Audit and repair home directory permissions using cPanel's internal utilities:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Fix permissions across a specific cPanel account</p>
    <p>/scripts/chownmyhome username</p>
    <p class="text-gray-400 mt-2"># Check for broken symlinks inside public_html</p>
    <p>find /home/username/public_html -xtype l</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Failure Point 3: Remote Transport &amp; S3 Timeouts</h2>
  <p>If local archiving succeeds but backups fail during network transport, the failure is recorded in the transport queue log. Common triggers include:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>S3 API Rate Limits or Clock Skew:</strong> Amazon S3 rejects authentication if the server's local clock drifts more than 15 minutes from UTC. Run <code>chronyc sources</code> or <code>ntpdate -u pool.ntp.org</code> to synchronize system time.</li>
    <li><strong>SFTP Connection Timeouts:</strong> Large monolithic archives take hours to transfer over slow uplinks. If the remote SSH server has a strict <code>ClientAliveInterval</code>, the socket drops mid-transfer. Increase timeout values in WHM <em>Backup Destination &raquo; Timeout Settings</em> to 7200 seconds.</li>
    <li><strong>Destination Pruning Failures:</strong> If cPanel cannot list remote files to delete old retention snapshots, it halts future uploads to avoid exceeding destination storage quotas.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>How to Read Master Backup Logs &amp; Force CLI Runs</h2>
  <p>Whenever backups fail, avoid guessing. Inspect the timestamped log file created during the run:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># List the latest backup logs</p>
    <p>ls -lat /usr/local/cpanel/logs/cpbackup/ | head -n 10</p>
    <p class="text-gray-400 mt-2"># View the most recent execution log</p>
    <p>tail -n 100 /usr/local/cpanel/logs/cpbackup/$(ls -t /usr/local/cpanel/logs/cpbackup/ | head -n 1)</p>
  </div>
  <p>To run an immediate test backup without waiting for the nightly cron schedule:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Force immediate backup execution with verbose console output</p>
    <p>/usr/local/cpanel/bin/backup --force</p>
  </div>
  <p>If the command outputs <em>"Backup is already running"</em>, inspect <code>/var/cpanel/backups/queue/</code>. If an earlier backup process was killed unexpectedly, a stale lockfile may be preventing new executions. Clear stale lockfiles by verifying no <code>cpbackup</code> or <code>pkgacct</code> processes are running via <code>ps aux | grep backup</code>, then remove the lock.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Upgrading to Incremental Backups with JetBackup 5</h2>
  <p>Native cPanel backups use full compression, which hammers server CPU, consumes massive disk I/O, and causes frequent timeouts on servers hosting more than 100 accounts. For enterprise hosting environments, upgrading to a dedicated <a href="/jetbackup-license" """ + blog_posts.LINK + """>JetBackup 5 license</a> eliminates these failure points.</p>
  <p>Unlike cPanel's monolithic tarballs, JetBackup uses <strong>block-level incremental deduplication</strong>. Only modified blocks are copied directly to your storage destination (SSH, S3, Wasabi, Google Cloud). This slashes backup windows from 6 hours down to 20 minutes, eliminates the need for massive local staging space, and allows customers to self-restore single files or databases directly from their cPanel account.</p>
  <p>Need automated, high-speed backup licensing for your cPanel server? Activate an affordable <a href="/jetbackup-license" """ + blog_posts.LINK + """>JetBackup license</a> with instant setup from LicenBase today.</p>
</section>
"""
}

post_exim = {
    "slug": "troubleshoot-stuck-exim-mail-queue-whm",
    "title": "How to Troubleshoot Stuck Exim Mail Queue on WHM",
    "seo_title": "Fix Stuck Exim Mail Queue in WHM & cPanel",
    "description": "Diagnose and unfreeze a stuck Exim mail queue in WHM and cPanel. Learn how to inspect frozen emails, flush pending messages safely, and prevent mail loss.",
    "excerpt": "Diagnose and clear stuck or frozen Exim mail queues on cPanel & WHM without losing legitimate customer messages.",
    "category": "How-to",
    "date": "2026-10-22",
    "updated": "2026-10-22",
    "image_alt": "Exim MTA mail queue processing stages and troubleshooting diagram on cPanel",
    "faq": [
        ("What does '*** frozen ***' mean in the Exim mail queue?", "A message marked as '*** frozen ***' indicates that Exim attempted delivery and failed, and when it tried to send a non-delivery report (NDR / bounce message) back to the sender, that bounce attempt also failed or was unroutable. Exim suspends further delivery attempts on frozen messages until an administrator unfreezes or purges them."),
        ("How do I check the number of messages waiting in the Exim queue?", "From the Linux terminal via SSH as root, run 'exim -bpc'. This outputs the total count of queued messages. To display the full list with message IDs, timestamps, and recipient addresses, run 'exim -bp'."),
        ("Will flushing the queue delete my pending emails?", "No. Running 'exim -qf' forces Exim to start an immediate delivery attempt for all deferred messages in the queue. It will not delete emails. Emails are only removed if you explicitly invoke 'exim -Mrm' or if they exceed Exim's maximum retention timeout."),
        ("How can I find out which cPanel account or PHP script is flooding the Exim queue?", "Inspect a message's RFC headers by running 'exim -Mvh [message-id]'. Look for the 'X-PHP-Script' or 'X-Authenticated-Sender' headers, or search for the cPanel user's working directory in the envelope headers.")
    ],
    "og": {
        "headline": "Fix Stuck Exim Queue",
        "subtitle": "Troubleshoot and flush mail queue in WHM",
        "icon": "server"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("imunify360-license", "Imunify360 license")
    ],
    "body": """
<p class="text-lg text-gray-600">On a cPanel &amp; WHM hosting server, the <strong>Exim Mail Transfer Agent (MTA)</strong> handles thousands of inbound and outbound transactions daily. However, when the mail queue gets stuck—accumulating thousands of deferred or frozen messages—legitimate customer emails stop delivering, server load spikes, and upstream mail providers (like Gmail, Outlook, and Yahoo) begin throttling or blacklisting your server's IP address. Resolving a bloated Exim queue requires surgical triage: you must flush legitimate customer communications while identifying and deleting malicious spam runs without destroying real data. This guide provides an actionable troubleshooting playbook for system administrators to diagnose, clean, and unfreeze a stuck Exim queue on a <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Exim Queue Message States: Active, Deferred, and Frozen</h2>
  <p>To troubleshoot queue delays effectively, administrators must distinguish between the three primary states Exim assigns to queued messages:</p>
  """ + blog_posts.figure("troubleshoot-stuck-exim-mail-queue-whm-1", 1, "Exim MTA mail queue processing stages and troubleshooting diagram on cPanel", "Figure 1: Exim message lifecycle stages, retry delays, and administrative command playbook.") + """
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Active / Pending:</strong> Freshly submitted messages waiting for DNS lookups or remote SMTP socket handshakes. In healthy servers, messages remain in this state for only a few seconds.</li>
    <li><strong>Deferred (Retry Delay):</strong> Delivery was attempted, but the destination server returned a temporary failure (4xx response), such as <code>451 Greylisted</code> or <code>421 Too many concurrent connections</code>. Exim records the failure in its internal retry database (<code>/var/spool/exim/db/retry</code>) and calculates exponential retry intervals.</li>
    <li><strong>Frozen (<code>*** frozen ***</code>):</strong> Delivery failed permanently, and Exim's attempt to return a bounce message to the sender address was also rejected (a classic signature of outbound spam generated with forged sender headers). Exim halts automated processing on frozen emails to prevent mail loops.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 1: Check Queue Size and Identify Top Senders</h2>
  <p>Begin by logging into your server via SSH as <code>root</code> to determine the scale of the queue backlog:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Count total queued messages</p>
    <p>exim -bpc</p>
    <p class="text-gray-400 mt-2"># Display summary breakdown of senders and recipients using eximst</p>
    <p>exim -bp | exiqsumm</p>
  </div>
  <p>The <code>exiqsumm</code> output organizes queued messages by domain, volume, and oldest message age. If a single domain accounts for 8,000 out of 8,500 messages, that domain is either executing a massive newsletter campaign or has been compromised by a spammer.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 2: Inspect Individual Queued Messages Without Deletion</h2>
  <p>Before purging any email, inspect a sample message to verify whether it is legitimate business communication or malicious spam. Pick a message ID from <code>exim -bp</code> and inspect its components:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># View message headers (reveals authenticated sender and originating script)</p>
    <p>exim -Mvh 1t8Zab-0001bc-2d</p>
    <p class="text-gray-400 mt-2"># View message body text</p>
    <p>exim -Mvb 1t8Zab-0001bc-2d</p>
    <p class="text-gray-400 mt-2"># View delivery transaction log (shows exact SMTP rejection response)</p>
    <p>exim -Mvl 1t8Zab-0001bc-2d</p>
  </div>
  <p>In the headers (<code>-Mvh</code>), examine the <code>X-PHP-Script</code> or <code>X-Authenticated-Sender</code> lines. If an infected WordPress plugin is pumping spam through PHP <code>mail()</code>, this header will point directly to the exact file path (e.g., <code>/home/user/public_html/wp-content/uploads/cache.php</code>). If the spam originates from an authenticated mailbox, suspend that specific email user in cPanel immediately.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 3: Safely Flushing Legitimate Messages</h2>
  <p>If the queue accumulated because of a temporary network outage or firewall glitch that is now resolved, you can trigger an immediate delivery run for all legitimate pending messages:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Force delivery run of pending queue</p>
    <p>exim -qf</p>
    <p class="text-gray-400 mt-2"># Force queue run ignoring retry delays (processes greylisted messages immediately)</p>
    <p>exim -qff</p>
  </div>
  <p>To flush messages destined for a specific domain (for example, if Gmail unblocked your IP and you want to deliver queued Google Workspace messages):</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p>exim -R gmail.com</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 4: Purging Frozen Spam and Malicious Backlogs</h2>
  <p>Frozen messages consume disk space and inode allocations in <code>/var/spool/exim/input/</code> while slowing down queue processing. You can safely purge all frozen messages in bulk without touching active, legitimate emails:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Delete all frozen messages from queue</p>
    <p>exiqgrep -z -i | xargs exim -Mrm</p>
    <p class="text-gray-400 mt-2"># Delete all queued messages sent by a compromised local user:</p>
    <p>exiqgrep -f "spammer@compromiseddomain.com" -i | xargs exim -Mrm</p>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Step 5: Repairing Corrupted Exim Retry Databases</h2>
  <p>If Exim refuses to retry messages or continues deferring domains despite successful manual SMTP connections, the local Berkeley DB files in <code>/var/spool/exim/db/</code> may be corrupted. These databases record retry timestamps, rate limits, and host callout caches.</p>
  <p>Clean and rebuild the retry databases safely from the terminal:</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
    <p class="text-gray-400"># Purge expired retry records</p>
    <p>/usr/sbin/exim_tidydb -t 1d /var/spool/exim retry</p>
    <p class="text-gray-400 mt-2"># If the database is completely locked or corrupted, stop Exim and clear hints:</p>
    <p>/scripts/restartsrv_exim --stop</p>
    <p>rm -f /var/spool/exim/db/retry*</p>
    <p>rm -f /var/spool/exim/db/wait*</p>
    <p>/scripts/restartsrv_exim --start</p>
  </div>
  <p>Exim will recreate fresh database files automatically upon startup, clearing all false retry locks.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Proactive Outbound Protection with Imunify360</h2>
  <p>Manually triaging a frozen mail queue after a spam outbreak is exhausting and puts your server's IP reputation at severe risk. Deploying an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 security license</a> provides real-time proactive defense that intercepts malicious PHP mail scripts before they can inject spam into Exim.</p>
  <p>Imunify360's automated malware scanner isolates spam scripts on upload, blocks unauthorized outbound SMTP traffic, and prevents compromised WordPress instances from exhausting your server resources. Explore our genuine <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 licenses</a> and <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel license packages</a> to keep your hosting infrastructure clean and protected.</p>
</section>
"""
}

new_posts = [post_backup, post_exim]

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

# -*- coding: utf-8 -*-
import sys
from pathlib import Path

# Section additions
extra_post3_section = """
<section class="space-y-4">
  <h2 \"\"\" + blog_posts.H2 + \"\"\">Configuring Roundcube Memory Limits &amp; IMAP Session Timeouts</h2>
  <p>Beyond port accessibility and SSL certificates, email clients frequently report webmail timeouts when opening large inboxes with thousands of messages or downloading hefty MIME attachments. Because cPanel executes Roundcube under internal PHP constraints, insufficient memory allocation causes silent worker termination.</p>
  <ul class=\"list-disc pl-6 space-y-2 text-gray-700\">
    <li><strong>Increasing cPanel PHP Memory:</strong> In WHM, navigate to <em>Server Configuration &raquo; Tweak Settings &raquo; System</em> and adjust <code>cPanel PHP max POST size</code> and <code>cPanel PHP max upload size</code> to 64M or 128M to permit smooth attachment processing.</li>
    <li><strong>Dovecot IMAP Idle Tuning:</strong> To prevent premature session disconnection on mobile devices and webmail tabs, ensure <code>imap_idle_notify_interval</code> in <code>/etc/dovecot/dovecot.conf</code> is set to at least 2 minutes, maintaining persistent socket keep-alives without overloading system RAM.</li>
  </ul>
</section>
"""

extra_post4_section = """
<section class="space-y-4">
  <h2 \"\"\" + blog_posts.H2 + \"\"\">LSCache Architecture: ESI &amp; Dynamic WordPress Optimization</h2>
  <p>The decisive technological advantage of LiteSpeed Web Server over NGINX and Apache is its native server-level caching engine: <strong>LiteSpeed Cache (LSCache)</strong>. While traditional PHP caching solutions require invoking the PHP interpreter on every request, LiteSpeed serves fully cached HTML pages directly from memory at the web server layer.</p>
  <ul class=\"list-disc pl-6 space-y-2 text-gray-700\">
    <li><strong>Edge Side Includes (ESI):</strong> On high-traffic WooCommerce stores, cart fragments and private user greetings normally prevent page caching. LSCache utilizes ESI to punch dynamic holes in cached pages, allowing 98% of the page to be served from static cache while injecting private account blocks in real time.</li>
    <li><strong>Built-In Crawler Engine:</strong> LiteSpeed includes an automated crawler that sweeps XML sitemaps during low-traffic overnight hours, ensuring product pages and blog posts remain warm in RAM before human visitors arrive.</li>
  </ul>
</section>
"""

extra_post5_section = """
<section class="space-y-4">
  <h2 \"\"\" + blog_posts.H2 + \"\"\">OPcache Memory Optimization &amp; Script Execution Safeguards</h2>
  <p>PHP Zend OPcache precompiles PHP scripts into shared memory bytecode, eliminating the CPU overhead of parsing and compiling PHP scripts on every HTTP request. However, on multi-tenant cPanel servers, an undersized OPcache memory buffer leads to continuous cache evictions and CPU thrashing.</p>
  <ul class=\"list-disc pl-6 space-y-2 text-gray-700\">
    <li><strong>Production OPcache Configuration:</strong> In WHM MultiPHP INI Editor, allocate at least <code>opcache.memory_consumption = 128</code> (or 256 for large nodes) and set <code>opcache.max_accelerated_files = 10000</code>. This guarantees that all active core WordPress files reside permanently in precompiled memory.</li>
    <li><strong>Preventing Code Staling:</strong> Set <code>opcache.revalidate_freq = 60</code> to instruct PHP to check for modified files once every 60 seconds, balancing instantaneous code updates with maximum bytecode caching throughput.</li>
  </ul>
</section>
"""

# Let's read add_all_5_posts.py and insert these sections right before the last </section> of each post!
content = Path("scratch/add_all_5_posts.py").read_text(encoding="utf-8")

# For post 3: insert extra_post3_section before the closing of post_3 body
target_p3 = """  <p>For more architectural insights, review our companion <a href="/blog/cpanel-webmail-ports-explained-2095-2096" """
assert target_p3 in content, "Target post 3 not found"
replacement_p3 = extra_post3_section.strip() + "\n\n<section class=\"space-y-4\">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">Summary &amp; Related Email Infrastructure</h2>\n" + target_p3
content = content.replace(target_p3, replacement_p3, 1)

# For post 4: insert extra_post4_section before the closing of post_4 body
target_p4 = """  <p>Retail licenses for LiteSpeed Enterprise typically range from $10 to $65+ per month per server."""
assert target_p4 in content, "Target post 4 not found"
replacement_p4 = extra_post4_section.strip() + "\n\n<section class=\"space-y-4\">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">LiteSpeed Buying Guide: Wholesale Licensing with LicenBase</h2>\n" + target_p4
# note: in post 4 that heading already existed, let's just insert extra_post4_section before it
content = content.replace("""<section class="space-y-4">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">LiteSpeed Buying Guide: Wholesale Licensing with LicenBase</h2>\n  <p>Retail licenses for LiteSpeed Enterprise typically range""",
                          extra_post4_section.strip() + "\n\n<section class=\"space-y-4\">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">LiteSpeed Buying Guide: Wholesale Licensing with LicenBase</h2>\n  <p>Retail licenses for LiteSpeed Enterprise typically range", 1)

# For post 5: insert extra_post5_section before the closing of post_5 body
target_p5 = """  <p>On standard Linux distributions (AlmaLinux, CentOS, Ubuntu), every user account can read shared directories"""
assert target_p5 in content, "Target post 5 not found"
content = content.replace("""<section class="space-y-4">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">Isolating Multi-Tenant Environments with CloudLinux CageFS</h2>""",
                          extra_post5_section.strip() + "\n\n<section class=\"space-y-4\">\n  <h2 \"\"\" + blog_posts.H2 + \"\"\">Isolating Multi-Tenant Environments with CloudLinux CageFS</h2>", 1)

Path("scratch/add_all_5_posts.py").write_text(content, encoding="utf-8")
print("Updated scratch/add_all_5_posts.py with expanded sections!")

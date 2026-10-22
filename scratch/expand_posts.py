# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path("c:/dev/Licenbase.com").resolve()))

import blog_posts

# 1. Expand litespeed-worker-sizing-how-many-workers-vps
extra_litespeed = """
<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>How CloudLinux and cPanel Integrate with Worker Sizing</h2>
  <p>When running LiteSpeed on top of a <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel license</a> alongside a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux OS license</a>, worker sizing intersects directly with CageFS and CloudLinux LVE limits. Because CloudLinux encapsulates each user's PHP workers inside isolated container boundaries, LiteSpeed's primary event daemon does not get bogged down by individual runaway scripts.</p>
  <p>In high-density shared hosting environments, a 2-Worker LiteSpeed setup paired with CloudLinux allows system administrators to easily double or triple tenant density compared to traditional Apache configurations. Each LiteSpeed worker efficiently offloads static files and cached requests, ensuring that CPU cycles remain available for database-intensive queries and dynamic application execution.</p>
</section>
"""

# 2. Expand monitor-linux-vps-bandwidth-real-time-iftop-vnstat
extra_bandwidth = """
<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Automating Bandwidth Alerts and Rate Limiting</h2>
  <p>While interactive terminal utilities like <code>iftop</code> and <code>nload</code> are invaluable during live emergencies, proactive network monitoring prevents unexpected bandwidth overages before they impact your hosting budget. Administrators can configure automated email notifications or Slack alerts by parsing <code>vnstat --json</code> output in a daily cron job.</p>
  <p>If recurring bandwidth abuse is traced back to a specific IP range or malicious bot network, you can immediately enforce rate limiting at the network layer using <code>iptables</code> or <code>nftables</code>, or drop the abusive connections directly via your software firewall. Combining real-time command-line inspection with automated traffic accounting ensures that your virtual private server maintains optimal latency and uninterrupted network throughput.</p>
</section>
"""

# 3. Expand cheapest-way-to-run-cpanel-vps-2026-startups
extra_cheapest = """
<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Long-Term Scalability and Growth Planning</h2>
  <p>Starting with an ultra-affordable $17.50/month cPanel VPS does not mean you are trapped on low-tier hardware forever. The beauty of decoupling unmanaged cloud compute from independent software licensing is seamless scalability. As your client base expands from 5 websites to 50 or 250 websites, you can resize your underlying cloud server with a single click in your cloud provider's console without modifying your licensing architecture.</p>
  <p>When you need to upgrade your account tier—from cPanel Admin to cPanel Pro or Premier—LicenBase allows you to adjust your license tier dynamically. By keeping your monthly fixed costs as low as possible during the startup phase, your hosting company generates immediate net cash flow from your very first customer, creating a resilient, profitable foundation for sustained business growth.</p>
</section>
"""

for p in blog_posts.POSTS:
    if p["slug"] == "litespeed-worker-sizing-how-many-workers-vps":
        # Ensure it has links to at least 2 product pages and extra word count
        p["body"] = p["body"].replace(
            """<p>LicenBase provides automated, low-cost <a href="/litespeed-license" """,
            extra_litespeed + """\n<p>LicenBase provides automated, low-cost <a href="/litespeed-license" """
        )
        print("Expanded litespeed-worker-sizing-how-many-workers-vps")
    elif p["slug"] == "monitor-linux-vps-bandwidth-real-time-iftop-vnstat":
        p["body"] = p["body"].replace(
            """<section class="space-y-4">\n  <h2 """ + blog_posts.H2 + """>Server Management with LicenBase</h2>""",
            extra_bandwidth + """\n<section class="space-y-4">\n  <h2 """ + blog_posts.H2 + """>Server Management with LicenBase</h2>"""
        )
        print("Expanded monitor-linux-vps-bandwidth-real-time-iftop-vnstat")
    elif p["slug"] == "cheapest-way-to-run-cpanel-vps-2026-startups":
        p["body"] = p["body"].replace(
            """<section class="space-y-4">\n  <h2 """ + blog_posts.H2 + """>The Verdict: 77% Recurring Monthly Savings</h2>""",
            extra_cheapest + """\n<section class="space-y-4">\n  <h2 """ + blog_posts.H2 + """>The Verdict: 77% Recurring Monthly Savings</h2>"""
        )
        print("Expanded cheapest-way-to-run-cpanel-vps-2026-startups")

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

print("Saved updated blog_posts.py")

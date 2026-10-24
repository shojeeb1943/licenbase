# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path("c:/dev/Licenbase.com").resolve()))

import blog_posts

# Remove old meta blog post if present
old_slug = "licenbase-5-seo-blog-topics-content-linking-plans"
blog_posts.POSTS = [p for p in blog_posts.POSTS if p["slug"] != old_slug]
print(f"Removed '{old_slug}'. Current total: {len(blog_posts.POSTS)}")

# Clean up files associated with the old post
old_files = [
    Path("blog/licenbase-5-seo-blog-topics-content-linking-plans.html"),
    Path("assets/img/blog/licenbase-5-seo-blog-topics-content-linking-plans-1.svg"),
    Path("assets/img/blog/licenbase-5-seo-blog-topics-content-linking-plans-feature.webp"),
    Path("assets/img/blog/licenbase-5-seo-blog-topics-content-linking-plans-thumb.webp"),
    Path("assets/img/og/blog-licenbase-5-seo-blog-topics-content-linking-plans.png"),
]
for f in old_files:
    if f.exists():
        f.unlink()
        print(f"Deleted old file: {f}")

# ---------------------------------------------------------------------------
# POST 1: Imunify360 Pricing Guide
# ---------------------------------------------------------------------------
post_1 = {
    "slug": "imunify360-license-pricing-plans-roi-guide",
    "title": "Imunify360 License Pricing Guide: Plans, Features & ROI",
    "seo_title": "Imunify360 Pricing Guide: Plans & ROI",
    "description": "Compare Imunify360 license pricing plans for VPS and dedicated servers. Discover automated malware scrubbing features, cost breakdowns, and sysadmin ROI.",
    "excerpt": "A complete guide to Imunify360 license tiers, comparing Single User, 30 Users, and Unlimited plans with practical server security ROI.",
    "category": "Guide",
    "date": "2026-10-24",
    "updated": "2026-10-24",
    "image_alt": "Imunify360 license tier pricing comparison and automated security architecture diagram",
    "faq": [
        ("What are the main Imunify360 license tiers?",
         "Imunify360 offers three core licensing tiers based on the number of accounts hosted on the machine: Single User (1 account), 30 Users (up to 30 accounts), and Unlimited Users (for unlimited accounts on VPS or bare-metal dedicated servers)."),
        ("Does Imunify360 replace ModSecurity and ClamAV?",
         "Yes. Imunify360 replaces standard ModSecurity rules with an AI-driven Web Application Firewall (WAF) and supersedes basic scanners like ClamAV with an automated real-time malware scanner that detects zero-day exploits and automatically cleans infected code without corrupting website files."),
        ("How does Imunify360 licensing differ between VPS and Dedicated servers?",
         "Single User and 30 Users licenses are strictly cloud/VPS licenses. For unvirtualized bare-metal hardware running high tenant counts, an Unlimited Dedicated license is required. LicenBase provides automated IP licensing for both VPS and Metal at wholesale pricing."),
        ("Can I automate Imunify360 license activation with LicenBase?",
         "Yes. LicenBase provides genuine automated IP licensing. Once you assign your server IP, a single curl command activates the license, connecting your node directly to official vendor update mirrors for real-time threat signatures and WAF rulesets.")
    ],
    "og": {
        "headline": "Imunify360 Pricing & ROI",
        "subtitle": "Plans, tiers and automated server security",
        "icon": "shield-check"
    },
    "related": [
        ("imunify360-license", "Imunify360 license"),
        ("cloudlinux-license", "CloudLinux OS license")
    ],
    "body": """
<p class="text-lg text-gray-600">Securing a multi-tenant web hosting server against modern automated attack vectors requires more than traditional reactive firewalls and basic signature matching. Imunify360 is widely regarded as the gold standard in comprehensive Linux server defense, integrating an AI-driven Web Application Firewall (WAF), real-time file system scanning, automated malware cleanup, and proactive PHP script execution monitoring. However, navigating vendor licensing tiers and evaluating actual operational return on investment (ROI) can be confusing for growing hosting companies and system administrators. This guide breaks down Imunify360 license tiers, contrasts piecemeal tools against full-stack security, and illustrates how wholesale licensing through an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 license</a> from LicenBase maximizes server protection while lowering operational overhead.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Imunify360 Licensing Tiers Breakdown</h2>
  <p>Imunify360 licensing is structured around user account capacity and underlying virtualization environments. Selecting the right tier ensures you do not overpay for unused account headroom while guaranteeing complete coverage across all hosted domains.</p>
  <div class="overflow-x-auto rounded-xl border border-gray-200">
    <table class="w-full min-w-[34rem] text-sm text-left">
      <thead class="bg-gray-50 border-b border-gray-200 text-xs font-bold uppercase text-gray-700">
        <tr>
          <th class="px-4 py-3">License Plan</th>
          <th class="px-4 py-3">Account Limit</th>
          <th class="px-4 py-3">Server Architecture</th>
          <th class="px-4 py-3">Target Deployment</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-100">
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Single User</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">1 cPanel/Plesk User</td>
          <td class="px-4 py-3 text-gray-600">Cloud / VPS</td>
          <td class="px-4 py-3 text-gray-700">Dedicated e-commerce VPS, corporate sites, staging</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Up to 30 Users</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 30 Users</td>
          <td class="px-4 py-3 text-gray-600">Cloud / VPS</td>
          <td class="px-4 py-3 text-gray-700">Digital agencies, boutique reseller hosts, multi-client nodes</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Unlimited (VPS)</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Unlimited Accounts</td>
          <td class="px-4 py-3 text-gray-600">Cloud / VPS (KVM, Proxmox)</td>
          <td class="px-4 py-3 text-gray-700">High-density shared hosting virtual machines</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Unlimited (Metal)</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Unlimited Accounts</td>
          <td class="px-4 py-3 text-gray-600">Bare-Metal Dedicated</td>
          <td class="px-4 py-3 text-gray-700">Enterprise dedicated nodes, bare-metal shared hosting</td>
        </tr>
      </tbody>
    </table>
  </div>
  """ + blog_posts.figure("imunify360-license-pricing-plans-roi-guide", 1, "Imunify360 license tier pricing comparison and automated security architecture diagram", "Figure 1: Imunify360 multi-tiered licensing structure and automated defensive feature matrix.") + """
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Core Security Features: What You Get Beyond a Standard Firewall</h2>
  <p>Many server administrators attempt to secure their servers by combining free, disconnected utilities such as ConfigServer Security &amp; Firewall (CSF), standard ModSecurity with OWASP rules, and scheduled ClamAV cron jobs. While cost-effective on the surface, this piecemeal approach creates substantial administrative overhead and fails to stop sophisticated obfuscated web shells.</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>AI-Driven Web Application Firewall (WAF):</strong> Imunify360 analyzes incoming HTTP/HTTPS traffic dynamically, blocking Layer 7 application attacks, SQL injections, and cross-site scripting (XSS) before scripts execute. Its machine-learning engine achieves an industry-low false-positive rate.</li>
    <li><strong>Proactive PHP Defense:</strong> Instead of relying purely on static regex signatures, Proactive Defense monitors PHP script execution calls in memory in real time. Even if malware is heavily obfuscated with <code>base64_decode</code> or <code>gzinflate</code>, unauthorized system calls are blocked instantly.</li>
    <li><strong>Automated File De-obfuscation &amp; Decontamination:</strong> Unlike ClamAV, which merely flags or quarantines whole files (often breaking client websites), Imunify360 surgical cleanup removes malicious injected snippets while preserving genuine application logic intact.</li>
    <li><strong>Herd Immunity Global Threat Intelligence:</strong> When an IP address attacks an Imunify360-protected server anywhere in the world, that threat actor is automatically greylisted or blacklisted across all participating servers globally within seconds.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Calculating the Operational ROI of Automated Defense</h2>
  <p>To evaluate whether an Imunify360 license makes financial sense, examine the actual labor costs associated with manual malware incident response. In a typical shared hosting fleet of 200–500 websites, out-of-date WordPress plugins and compromised customer passwords cause an average of 4 to 8 active infections per week.</p>
  <div class="bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-100 overflow-x-auto">
# Manual Malware Remediation Math per Incident:
# Initial ticket triage: 15 minutes
# SSH log inspection &amp; malicious cron identification: 30 minutes
# Database scrubbing &amp; core file replacement: 45 minutes
# Customer communication &amp; post-cleanup re-check: 15 minutes
# Total sysadmin labor: 1.75 hours x $35/hr = $61.25 per compromised site!
  </div>
  <p>With an automated Imunify360 license operating in real-time, the file system intercepts file uploads before they execute, quarantines malicious code automatically, and notifies the customer via the cPanel user interface without requiring tier-2 sysadmin intervention. By preventing just a single malware infection per month, the software pays for itself multiple times over.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>How to Save on Imunify360 Licensing with LicenBase</h2>
  <p>Purchasing retail licenses directly at vendor list price can quickly eat into the profit margins of growing hosting businesses. LicenBase offers independent automated IP licensing for Imunify360 starting at just <strong>$1.50/month</strong>, providing 100% genuine official binary updates, uninterrupted threat feed synchronization, and instantaneous IP activation. For maximum server performance and account density, pair Imunify360 with a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux license</a> to enforce hard tenant memory and CPU limits, and review our <a href="/deals" """ + blog_posts.LINK + """>discount combo stacks</a> to bundle your entire server management suite at wholesale rates.</p>
  <p>Read our in-depth <a href="/blog/imunify360-pricing-features-license-costs-guide" """ + blog_posts.LINK + """>Imunify360 pricing features guide</a> for deeper comparisons, and consult our transparent <a href="/license-policy" """ + blog_posts.LINK + """>License Policy</a> and <a href="/refund-policy" """ + blog_posts.LINK + """>Refund Policy</a> or speak with our team on our <a href="/contact" """ + blog_posts.LINK + """>support page</a>.</p>
</section>
"""
}

# ---------------------------------------------------------------------------
# POST 2: cPanel VPS Cost & Configuration Guide
# ---------------------------------------------------------------------------
post_2 = {
    "slug": "cpanel-vps-cost-configuration-practical-guide",
    "title": "cPanel VPS Cost & Configuration Guide: Practical Setup",
    "seo_title": "cPanel VPS Cost & Configuration: Setup Guide",
    "description": "Calculate total cPanel VPS hosting costs, RAM sizing, and virtualization setups. Discover practical configuration steps and ways to reduce licensing overhead.",
    "excerpt": "A practical guide to cPanel VPS hardware sizing, hypervisor selection, tier pricing, and total cost optimization for hosting servers.",
    "category": "Guide",
    "date": "2026-10-24",
    "updated": "2026-10-24",
    "image_alt": "cPanel VPS hardware architecture, hypervisor configuration and cost breakdown diagram",
    "faq": [
        ("What are the minimum hardware specifications to run cPanel on a VPS?",
         "cPanel requires AlmaLinux, Rocky Linux, or Ubuntu LTS on a 64-bit architecture with a minimum of 2 GB of RAM (4 GB recommended for production), 1 vCPU, and at least 20 GB of storage. For servers hosting 10 or more active accounts, 8 GB of RAM and 4 vCPUs provide optimal responsiveness."),
        ("How does cPanel detect whether a server is a VPS or Bare-Metal Dedicated?",
         "During boot and license verification, cPanel queries system hypervisor flags using tools equivalent to 'systemd-detect-virt'. If it detects KVM, VMware, Xen, Hyper-V, or OpenVZ, it accepts a Cloud (VPS) license. If no hypervisor signature is found, a Metal (Dedicated) license is required."),
        ("What is the most cost-effective way to run multiple cPanel VPS instances on a dedicated server?",
         "Instead of buying an expensive Metal Premier license, install a type-1 hypervisor like Proxmox VE or a VPS orchestrator like Virtualizor on your bare-metal server. Then split the physical server into virtual machines running cPanel Cloud licenses, reducing software costs by up to 50%."),
        ("Can I upgrade from cPanel Solo to Admin or Pro without reinstalling software?",
         "Yes. All cPanel tiers run identical software binaries. When you upgrade your license from Solo (1 account) to Admin (5 accounts) or Pro (30 accounts), the new limit takes effect immediately after running '/usr/local/cpanel/cpkeyclt' via SSH without downtime.")
    ],
    "og": {
        "headline": "cPanel VPS Cost & Setup",
        "subtitle": "Hardware sizing, hypervisors and pricing",
        "icon": "server"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("virtualizor-license", "Virtualizor license")
    ],
    "body": """
<p class="text-lg text-gray-600">Deploying cPanel &amp; WHM on a Virtual Private Server (VPS) is the industry's preferred architecture for hosting web applications, client portfolios, and reseller accounts. However, since cPanel shifted its pricing model to account-based tiering, setting up a cPanel VPS without clear planning can lead to unexpected billing overhead or hardware bottlenecks. Many sysadmins struggle to find the right balance between virtualization overhead, base operating system requirements, and licensing tiers. This comprehensive guide provides a practical blueprint for calculating total cPanel VPS costs, sizing server hardware accurately, and configuring an optimized production environment using a wholesale <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel license</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Virtualization Environments &amp; Hypervisor Compatibility</h2>
  <p>To qualify for cPanel's lower-cost Cloud (VPS) licensing, your server instance must run on an active hypervisor. cPanel checks virtualization flags during initialization:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Check virtualization type on your Linux server:
systemd-detect-virt
# Expected output for VPS licenses: kvm, qemu, vmware, xen, or lxc
  </div>
  <p>The standard virtualization platforms supported for production cPanel deployments include:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>KVM / Proxmox VE:</strong> Full hardware virtualization offering dedicated kernel execution, memory reservation, and complete support for Linux namespaces and Docker containers.</li>
    <li><strong>Virtualizor Orchestration:</strong> Deploying a <a href="/virtualizor-license" """ + blog_posts.LINK + """>Virtualizor license</a> allows server operators to slice bare-metal servers into automated VPS nodes, allowing system administrators to deploy cPanel Cloud licenses affordably.</li>
    <li><strong>Public Cloud Hypervisors:</strong> Amazon Web Services (AWS EC2), DigitalOcean Droplets, Linode/Akamai instances, and Google Compute Engine all qualify as Cloud VPS environments.</li>
  </ul>
  """ + blog_posts.figure("cpanel-vps-cost-configuration-practical-guide", 1, "cPanel VPS hardware architecture, hypervisor configuration and cost breakdown diagram", "Figure 1: Hypervisor architecture, account tier limits, and practical monthly hosting budgets.") + """
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Practical Hardware Sizing Matrix for Production</h2>
  <p>Under-provisioning RAM is the leading cause of cPanel VPS crashes. Because WHM runs essential daemons—such as <code>named</code> (DNS), <code>cpanel-dovecot</code> (IMAP/POP3), <code>exim</code> (Mail), <code>mariadb</code>, and <code>cpanel-apache</code>—the server has an unavoidable baseline memory footprint.</p>
  <div class="overflow-x-auto rounded-xl border border-gray-200">
    <table class="w-full min-w-[34rem] text-sm text-left">
      <thead class="bg-gray-50 border-b border-gray-200 text-xs font-bold uppercase text-gray-700">
        <tr>
          <th class="px-4 py-3">cPanel Tier</th>
          <th class="px-4 py-3">Max Accounts</th>
          <th class="px-4 py-3">Minimum RAM</th>
          <th class="px-4 py-3">Recommended Sizing</th>
          <th class="px-4 py-3">Typical Monthly Compute Cost</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-100">
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">cPanel Solo</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">1 Account</td>
          <td class="px-4 py-3 text-gray-600">2 GB RAM</td>
          <td class="px-4 py-3 text-gray-700">2 vCPUs, 4 GB RAM, 40 GB NVMe</td>
          <td class="px-4 py-3 text-emerald-700 font-semibold">$8 – $12 / mo</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">cPanel Admin</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 5 Accounts</td>
          <td class="px-4 py-3 text-gray-600">4 GB RAM</td>
          <td class="px-4 py-3 text-gray-700">4 vCPUs, 8 GB RAM, 80 GB NVMe</td>
          <td class="px-4 py-3 text-emerald-700 font-semibold">$15 – $24 / mo</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">cPanel Pro</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 30 Accounts</td>
          <td class="px-4 py-3 text-gray-600">8 GB RAM</td>
          <td class="px-4 py-3 text-gray-700">4–6 vCPUs, 16 GB RAM, 160 GB NVMe</td>
          <td class="px-4 py-3 text-emerald-700 font-semibold">$30 – $50 / mo</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Premier Cloud</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">100+ Accounts</td>
          <td class="px-4 py-3 text-gray-600">16 GB RAM</td>
          <td class="px-4 py-3 text-gray-700">8 vCPUs, 32 GB RAM, 500 GB NVMe</td>
          <td class="px-4 py-3 text-emerald-700 font-semibold">$60 – $100 / mo</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Total Cost of Ownership: Building an Affordable Stack</h2>
  <p>To operate a production-ready cPanel server without paying bloated retail markups, smart hosts combine affordable unmanaged cloud VPS slices with automated wholesale licensing from LicenBase:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Cloud VPS Slice (4 GB RAM, 2 vCPU):</strong> Approx. $10.00 – $14.00/month from competitive cloud infrastructure providers (Hetzner, OVH, Vultr).</li>
    <li><strong>Automated cPanel IP License:</strong> Starting at just <strong>$4.00/month</strong> via LicenBase, including official unmodified vendor binaries and direct mirror updates.</li>
    <li><strong>Accelerated Web Server:</strong> Adding a <a href="/litespeed-license" """ + blog_posts.LINK + """>LiteSpeed license</a> reduces CPU consumption by up to 70%, allowing you to host twice as many websites on the same VPS slice.</li>
    <li><strong>Total Monthly Cost:</strong> Under $25/month for a rock-solid, production-grade cPanel hosting environment.</li>
  </ul>
  <p>Learn more about structuring your hardware and software overhead in our <a href="/blog/cpanel-cost-breakdown-license-fees-vps-hosting" """ + blog_posts.LINK + """>cPanel cost breakdown guide</a>, explore our wholesale <a href="/deals" """ + blog_posts.LINK + """>combo stacks</a>, and check our <a href="/license-policy" """ + blog_posts.LINK + """>License Policy</a> or <a href="/about" """ + blog_posts.LINK + """>About LicenBase</a> page.</p>
</section>
"""
}

# ---------------------------------------------------------------------------
# POST 3: cPanel Webmail Ports (2095 & 2096)
# ---------------------------------------------------------------------------
post_3 = {
    "slug": "cpanel-webmail-ports-ssl-login-issues-fixed",
    "title": "cPanel Webmail Ports (2095 & 2096): Fix SSL & Login Issues",
    "seo_title": "cPanel Webmail Ports (2095 & 2096): SSL Fixes",
    "description": "Troubleshoot cPanel Webmail port 2095 and 2096 connection timeouts, SSL certificate mismatches, and firewall blockages with proven command line fixes.",
    "excerpt": "Master cPanel Webmail port configuration for 2095 and 2096, fix SSL handshake errors, open firewall rules, and resolve login timeouts.",
    "category": "How-to",
    "date": "2026-10-24",
    "updated": "2026-10-24",
    "image_alt": "cPanel Webmail port 2095 vs 2096 architecture and SSL connection troubleshooting workflow",
    "faq": [
        ("What is the difference between port 2095 and port 2096 in cPanel?",
         "Port 2095 is the unencrypted HTTP port for cPanel Webmail, transmitting credentials in plaintext. Port 2096 is the encrypted HTTPS/SSL port, securing authentication with modern TLS ciphers. Production servers should always redirect traffic from 2095 to 2096."),
        ("Why does my browser display an SSL warning when accessing Webmail on port 2096?",
         "This warning typically occurs when accessing webmail via the client domain (e.g., https://example.com:2096) before an AutoSSL certificate has been issued for the domain, or when the server falls back to an untrusted self-signed server hostname certificate."),
        ("How can I check if port 2096 is blocked by a firewall?",
         "You can test connectivity from your local terminal using netcat or curl: 'nc -zv yourdomain.com 2096' or 'curl -Iv https://yourdomain.com:2096'. On the server, verify that port 2096 is included in the TCP_IN configuration in /etc/csf/csf.conf."),
        ("How do I force all cPanel Webmail connections to use secure SSL?",
         "Log into WHM as root, navigate to 'Home » Server Configuration » Tweak Settings » Redirection', and set 'Require SSL for cPanel Services' to 'On', and enable 'Always redirect to SSL/TLS'.")
    ],
    "og": {
        "headline": "cPanel Webmail Ports Fix",
        "subtitle": "Port 2095/2096 SSL & connection fixes",
        "icon": "globe"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("imunify360-license", "Imunify360 license")
    ],
    "body": """
<p class="text-lg text-gray-600">Accessing webmail is one of the most critical daily functions for business email users on cPanel &amp; WHM servers. Whether utilizing Roundcube, Horde, or standard browser redirects, connecting to email requires establishing an HTTP or HTTPS handshake through designated network daemon ports: <strong>Port 2095</strong> and <strong>Port 2096</strong>. When users experience "Connection Refused", "Connection Timed Out", or alarming browser SSL certificate warnings, email communication halts. This guide demystifies the technical roles of cPanel webmail ports 2095 and 2096, provides step-by-step firewall diagnostic commands, and demonstrates how to resolve SSL/TLS certificate mismatches on your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Port 2095 vs. Port 2096: Technical Differences</h2>
  <p>cPanel runs an internal web daemon called <code>cpsrvd</code> that listens specifically for administrative and client portal connections. Webmail traffic is routed through two distinct ports based on encryption state:</p>
  <div class="overflow-x-auto rounded-xl border border-gray-200">
    <table class="w-full min-w-[34rem] text-sm text-left">
      <thead class="bg-gray-50 border-b border-gray-200 text-xs font-bold uppercase text-gray-700">
        <tr>
          <th class="px-4 py-3">Port Number</th>
          <th class="px-4 py-3">Protocol</th>
          <th class="px-4 py-3">Encryption State</th>
          <th class="px-4 py-3">Security Assessment &amp; Best Practice</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-100">
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Port 2095</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">HTTP</td>
          <td class="px-4 py-3 text-red-600 font-medium">Unencrypted Plaintext</td>
          <td class="px-4 py-3 text-gray-700">Insecure. Usernames and passwords transmitted in cleartext. Always enforce SSL redirection.</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Port 2096</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">HTTPS</td>
          <td class="px-4 py-3 text-emerald-600 font-medium">Encrypted TLS 1.3 / AES-256</td>
          <td class="px-4 py-3 text-gray-700">Standard production port. Required for enterprise compliance and browser security.</td>
        </tr>
      </tbody>
    </table>
  </div>
  """ + blog_posts.figure("cpanel-webmail-ports-ssl-login-issues-fixed", 1, "cPanel Webmail port 2095 vs 2096 architecture and SSL connection troubleshooting workflow", "Figure 1: Architectural differences between port 2095 and port 2096 with firewall and SSL validation paths.") + """
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Diagnosing Port 2096 Connection Timeouts and Firewall Blocks</h2>
  <p>If an email user reports that <code>https://example.com:2096</code> fails to load, the issue is almost always a network firewall policy either on the server or on the user's local corporate/school Wi-Fi network.</p>
  <p>Step 1: Test connectivity directly from your terminal using <code>curl</code>:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Test whether port 2096 accepts TCP handshakes:
curl -Iv https://yourdomain.com:2096
# If curl hangs, port 2096 is blocked by a network firewall.
  </div>
  <p>Step 2: Verify that ConfigServer Security &amp; Firewall (CSF) has port 2096 open in <code>/etc/csf/csf.conf</code>:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Ensure 2095 and 2096 are present in TCP_IN:
grep -E "^TCP_IN" /etc/csf/csf.conf
# If missing, add 2095,2096 to TCP_IN and reload CSF:
csf -r
  </div>
  <p>If the client operates behind a strict corporate proxy that blocks non-standard ports (ports other than 80 and 443), enable <strong>Proxy Subdomains</strong> in WHM. This maps webmail traffic through standard port 443 via <code>https://webmail.example.com</code>, bypassing port 2096 restrictions seamlessly.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Fixing SSL Certificate Mismatches and Browser Warnings</h2>
  <p>When connecting to <code>https://example.com:2096</code>, users frequently encounter <code>NET::ERR_CERT_COMMON_NAME_INVALID</code>. This occurs when cPanel's service daemon serves the server's master hostname certificate rather than the client's individual domain certificate.</p>
  <p>To ensure valid SSL certificates across all webmail domains, execute cPanel's automated certificate verification tool via SSH as <code>root</code>:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Force AutoSSL to inspect and replace expired or missing service certificates:
/usr/local/cpanel/bin/checkallsslcerts --force
  </div>
  <p>Pairing your email infrastructure with proactive malware defense from an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 license</a> prevents compromised email accounts from sending unauthorized spam bursts that trigger IP blacklisting.</p>
<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Configuring Roundcube Memory Limits &amp; IMAP Session Timeouts</h2>
  <p>Beyond port accessibility and SSL certificates, email clients frequently report webmail timeouts when opening large inboxes with thousands of messages or downloading hefty MIME attachments. Because cPanel executes Roundcube under internal PHP constraints, insufficient memory allocation causes silent worker termination.</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Increasing cPanel PHP Memory:</strong> In WHM, navigate to <em>Server Configuration &raquo; Tweak Settings &raquo; System</em> and adjust <code>cPanel PHP max POST size</code> and <code>cPanel PHP max upload size</code> to 64M or 128M to permit smooth attachment processing.</li>
    <li><strong>Dovecot IMAP Idle Tuning:</strong> To prevent premature session disconnection on mobile devices and webmail tabs, ensure <code>imap_idle_notify_interval</code> in <code>/etc/dovecot/dovecot.conf</code> is set to at least 2 minutes, maintaining persistent socket keep-alives without overloading system RAM.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Summary &amp; Related Email Infrastructure</h2>
  <p>For more architectural insights, review our companion <a href="/blog/cpanel-webmail-ports-explained-2095-2096" """ + blog_posts.LINK + """>cPanel webmail ports reference</a>, check our wholesale <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel licensing solutions</a>, or reach out to our team on the <a href="/contact" """ + blog_posts.LINK + """>contact page</a>.</p>
</section>
"""
}

# ---------------------------------------------------------------------------
# POST 4: LiteSpeed License Comparison
# ---------------------------------------------------------------------------
post_4 = {
    "slug": "litespeed-license-comparison-sizing-buying-guide",
    "title": "LiteSpeed License Comparison: Sizing & Buying Guide",
    "seo_title": "LiteSpeed License Comparison: Sizing & Buying",
    "description": "Compare LiteSpeed Web Server license tiers: Free Starter, Web Host Lite, Essential, and Elite. Learn worker process sizing, RAM limits, and caching ROI.",
    "excerpt": "Compare LiteSpeed Web Server license tiers, worker process capacities, RAM thresholds, and WordPress performance benchmarks.",
    "category": "Comparison",
    "date": "2026-10-24",
    "updated": "2026-10-24",
    "image_alt": "LiteSpeed Web Server license tier comparison matrix and worker process sizing diagram",
    "faq": [
        ("What is a LiteSpeed 'Worker Process' and why does it matter?",
         "A LiteSpeed worker process is an independent OS-level process responsible for handling HTTP/HTTPS requests. More workers enable the server to distribute concurrent SSL handshakes and heavy dynamic PHP requests across multiple CPU cores, preventing request queue latency during traffic spikes."),
        ("What happens if a server exceeds the RAM limit on a LiteSpeed tier?",
         "LiteSpeed license tiers like Web Host Lite (up to 8 GB RAM) enforce a hard memory threshold. If the physical or virtual server has more RAM than the license allows, the LiteSpeed daemon will refuse to start or fall back to limited functionality. You must either reduce assigned RAM or upgrade your license tier."),
        ("Does LiteSpeed Enterprise support Apache .htaccess rewrite rules?",
         "Yes. LiteSpeed Enterprise is engineered as a direct drop-in replacement for Apache. It natively reads and parses /etc/httpd/conf/httpd.conf, .htaccess rules, ModSecurity configurations, and EasyApache modules without requiring custom rewrite conversions."),
        ("How does LiteSpeed Cache (LSCache) outperform NGINX FastCGI cache?",
         "LSCache communicates directly with the LiteSpeed web server kernel via server-level tags. When an e-commerce product or blog post is updated in WordPress, LSCache purges only the specific related cache tags instantaneously, eliminating the stale cache issues and full-purge overhead typical of NGINX.")
    ],
    "og": {
        "headline": "LiteSpeed Comparison",
        "subtitle": "Worker sizing, RAM limits & buying guide",
        "icon": "zap"
    },
    "related": [
        ("litespeed-license", "LiteSpeed license"),
        ("cloudlinux-license", "CloudLinux OS license")
    ],
    "body": """
<p class="text-lg text-gray-600">Upgrading your web server architecture from traditional Apache to LiteSpeed Web Server is one of the single most effective optimizations for increasing WordPress speed, handling concurrent traffic spikes, and slashing server CPU load. However, LiteSpeed Enterprise utilizes a distinct licensing framework governed by worker process counts, memory limits, and domain capacity. Selecting the wrong tier can either cause license activation failures due to RAM constraints or leave your multi-core CPU underutilized. This comparison guide breaks down every LiteSpeed license tier, explains worker process mechanics, and provides a clear purchasing roadmap with an automated <a href="/litespeed-license" """ + blog_posts.LINK + """>LiteSpeed license</a> from LicenBase.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>LiteSpeed License Tiers: Side-by-Side Comparison</h2>
  <p>LiteSpeed divides its licenses into personal and commercial hosting editions. Understanding the architectural constraints of each tier ensures optimal performance:</p>
  <div class="overflow-x-auto rounded-xl border border-gray-200">
    <table class="w-full min-w-[36rem] text-sm text-left">
      <thead class="bg-gray-50 border-b border-gray-200 text-xs font-bold uppercase text-gray-700">
        <tr>
          <th class="px-4 py-3">License Tier</th>
          <th class="px-4 py-3">Worker Processes</th>
          <th class="px-4 py-3">RAM Limit</th>
          <th class="px-4 py-3">Domains</th>
          <th class="px-4 py-3">Ideal Workload</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-100">
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Site Owner</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">1 Worker</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 2 GB RAM</td>
          <td class="px-4 py-3 text-gray-600">Up to 5 Domains</td>
          <td class="px-4 py-3 text-gray-700">Single e-commerce site, development sandbox</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Web Host Lite</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">1 Worker</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 8 GB RAM</td>
          <td class="px-4 py-3 text-emerald-600 font-medium">Unlimited</td>
          <td class="px-4 py-3 text-gray-700">Small shared hosting VPS, boutique agencies</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Web Host Essential</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">2 Workers</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">Up to 8 GB RAM</td>
          <td class="px-4 py-3 text-emerald-600 font-medium">Unlimited</td>
          <td class="px-4 py-3 text-gray-700">High-concurrency WordPress agency nodes</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Web Host Professional</td>
          <td class="px-4 py-3 text-gray-600 font-mono text-xs">2 Workers</td>
          <td class="px-4 py-3 text-emerald-600 font-mono text-xs font-semibold">Unlimited RAM</td>
          <td class="px-4 py-3 text-emerald-600 font-medium">Unlimited</td>
          <td class="px-4 py-3 text-gray-700">Mid-sized hosting servers (16 GB–32 GB RAM)</td>
        </tr>
        <tr>
          <td class="px-4 py-3 font-semibold text-gray-900">Web Host Elite</td>
          <td class="px-4 py-3 text-purple-600 font-mono text-xs font-semibold">4 Workers</td>
          <td class="px-4 py-3 text-emerald-600 font-mono text-xs font-semibold">Unlimited RAM</td>
          <td class="px-4 py-3 text-emerald-600 font-medium">Unlimited</td>
          <td class="px-4 py-3 text-gray-700">Enterprise multi-tenant hosting, high traffic</td>
        </tr>
      </tbody>
    </table>
  </div>
  """ + blog_posts.figure("litespeed-license-comparison-sizing-buying-guide", 1, "LiteSpeed Web Server license tier comparison matrix and worker process sizing diagram", "Figure 1: LiteSpeed license tiers mapped across worker counts, memory ceilings, and hosting density.") + """
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Understanding Worker Process Sizing &amp; CPU Cores</h2>
  <p>A common misconception is that a 1-worker LiteSpeed license can only run on a 1-core VPS. In reality, a single LiteSpeed worker process can fully utilize an event-driven loop capable of serving thousands of simultaneous connections across any number of CPU cores. However, adding additional worker processes delivers two substantial performance benefits:</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Parallel TLS Handshakes:</strong> Cryptographic SSL handshakes consume considerable CPU cycles. Multi-worker licenses (2, 4, or 8 workers) parallelize TLS handshakes across distinct system threads without queue blocking.</li>
    <li><strong>Mitigating Hanging FastCGI Scripts:</strong> If a customer's slow database query briefly stalls worker processing, secondary workers continue answering inbound HTTP traffic seamlessly.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>LSCache Architecture: ESI &amp; Dynamic WordPress Optimization</h2>
  <p>The decisive technological advantage of LiteSpeed Web Server over NGINX and Apache is its native server-level caching engine: <strong>LiteSpeed Cache (LSCache)</strong>. While traditional PHP caching solutions require invoking the PHP interpreter on every request, LiteSpeed serves fully cached HTML pages directly from memory at the web server layer.</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Edge Side Includes (ESI):</strong> On high-traffic WooCommerce stores, cart fragments and private user greetings normally prevent page caching. LSCache utilizes ESI to punch dynamic holes in cached pages, allowing 98% of the page to be served from static cache while injecting private account blocks in real time.</li>
    <li><strong>Built-In Crawler Engine:</strong> LiteSpeed includes an automated crawler that sweeps XML sitemaps during low-traffic overnight hours, ensuring product pages and blog posts remain warm in RAM before human visitors arrive.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>LiteSpeed Buying Guide: Wholesale Licensing with LicenBase</h2>
  <p>Retail licenses for LiteSpeed Enterprise typically range from $10 to $65+ per month per server. LicenBase provides automated IP licensing for LiteSpeed starting at just <strong>$4.00/month</strong>, featuring instant automated IP assignment, official binary updates directly from LiteSpeed repositories, and complete support for the LSCache plugin ecosystem.</p>
  <p>Pairing LiteSpeed with a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux license</a> provides optimal server stabilization by throttling abusive tenants with LVE quotas. Explore our wholesale <a href="/deals" """ + blog_posts.LINK + """>combo stacks</a>, and check our <a href="/license-policy" """ + blog_posts.LINK + """>License Policy</a> and <a href="/refund-policy" """ + blog_posts.LINK + """>Refund Policy</a>.</p>
</section>
"""
}

# ---------------------------------------------------------------------------
# POST 5: PHP Security & Troubleshooting Guide for cPanel Servers
# ---------------------------------------------------------------------------
post_5 = {
    "slug": "php-security-troubleshooting-guide-cpanel",
    "title": "PHP Security & Troubleshooting Guide for cPanel Servers",
    "seo_title": "PHP Security & Troubleshooting: cPanel Guide",
    "description": "Harden PHP execution, size PHP-FPM pools to eliminate 502/504 errors, and prevent malware traversal on cPanel servers with CageFS and security directives.",
    "excerpt": "Harden PHP execution, tune PHP-FPM pools, eliminate gateway timeouts, and secure cPanel servers with CloudLinux CageFS.",
    "category": "Guide",
    "date": "2026-10-24",
    "updated": "2026-10-24",
    "image_alt": "PHP security architecture, PHP-FPM pool optimization and CageFS isolation diagram",
    "faq": [
        ("What is the formula to calculate pm.max_children in PHP-FPM?",
         "The standard production formula is: pm.max_children = (Total Available RAM - OS and Service Buffer RAM) / Average PHP Process Memory Size. For example, on a server with 8 GB RAM dedicated to PHP and an average process size of 64 MB: 8,192 MB / 64 MB = 128 max_children."),
        ("What causes 502 Bad Gateway and 504 Gateway Timeout errors in PHP-FPM?",
         "A 502 Bad Gateway usually indicates that the PHP-FPM worker process crashed due to hitting 'memory_limit' or a segmentation fault. A 504 Gateway Timeout indicates that the PHP script exceeded 'request_terminate_timeout' or 'max_execution_time' waiting for a slow MySQL query or external API call."),
        ("Why is CloudLinux CageFS essential for PHP security on shared cPanel servers?",
         "Standard Linux permissions allow PHP scripts running under one user account to inspect /tmp, view process lists in /proc, and read server configuration files. CloudLinux CageFS places each user inside an isolated virtualized filesystem jail, preventing cross-account data theft completely."),
        ("Which dangerous PHP functions should be disabled in php.ini for production?",
         "Unless specifically needed by administrative tools, disable shell execution functions by setting: disable_functions = exec,system,passthru,shell_exec,proc_open,popen,curl_multi_exec,parse_ini_file,show_source.")
    ],
    "og": {
        "headline": "PHP Security & Tuning Guide",
        "subtitle": "PHP-FPM pools, CageFS & crash prevention",
        "icon": "cpu"
    },
    "related": [
        ("cpanel-license", "cPanel & WHM license"),
        ("cloudlinux-license", "CloudLinux OS license")
    ],
    "body": """
<p class="text-lg text-gray-600">PHP powers the overwhelming majority of dynamic web applications hosted on cPanel &amp; WHM servers, including WordPress, WooCommerce, Joomla, and custom frameworks. However, because PHP scripts execute untrusted customer code, an unhardened PHP environment represents the single largest attack surface on a hosting server. Furthermore, poorly tuned PHP-FPM (FastCGI Process Manager) pool settings frequently lead to debilitating 502 Bad Gateway errors, high memory thrashing, and server-wide Out-Of-Memory (OOM) crashes. This technical guide outlines the architecture of secure PHP execution, provides mathematical sizing formulas for PHP-FPM worker pools, and demonstrates how to isolate users with CloudLinux CageFS on your <a href="/cpanel-license" """ + blog_posts.LINK + """>cPanel server</a>.</p>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Sizing PHP-FPM Pools to Eliminate 502/504 Errors</h2>
  <p>The default PHP-FPM configurations in cPanel EasyApache 4 are conservative templates that frequently bottleneck under production traffic. When incoming HTTP requests exceed the available worker processes, connections queue up until the web server aborts with a 504 Gateway Timeout.</p>
  <p>To configure your pools accurately, calculate <code>pm.max_children</code> based on physical memory reality rather than guesswork:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Step 1: Determine average PHP process memory size on your server:
ps -C php-fpm -o rss= | awk '{sum+=$1} END {print sum/NR/1024 " MB"}'
# Example result: ~65 MB per active worker

# Step 2: Calculate pm.max_children:
# Total RAM (16 GB) - OS &amp; DB Buffer (4 GB) = 12 GB available for PHP
# 12,288 MB / 65 MB = ~189 pm.max_children
  </div>
  <p>For high-density multi-tenant shared hosting, set <code>pm = ondemand</code>. This ensures worker processes are spawned only when an active request hits the pool and terminated after <code>pm.process_idle_timeout = 10s</code>, keeping idle memory consumption near zero.</p>
  """ + blog_posts.figure("php-security-troubleshooting-guide-cpanel", 1, "PHP security architecture, PHP-FPM pool optimization and CageFS isolation diagram", "Figure 1: Inbound request routing through WAF, PHP-FPM pool management, and CageFS filesystem sandboxing.") + """
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Hardening php.ini: Disabling High-Risk Execution Directives</h2>
  <p>Compromised WordPress sites and rogue file uploaders routinely attempt to execute shell backdoors. Preventing arbitrary command execution requires disabling critical execution functions across all active PHP versions in WHM MultiPHP INI Editor:</p>
  <div class="bg-gray-900 rounded-lg p-3 font-mono text-xs text-gray-200">
# Recommended production php.ini hardening directives:
disable_functions = exec,passthru,shell_exec,system,proc_open,popen,show_source
allow_url_fopen = Off
allow_url_include = Off
expose_php = Off
max_execution_time = 60
memory_limit = 256M
  </div>
  <p>Disabling <code>allow_url_include</code> prevents Remote File Inclusion (RFI) attacks, while turning off <code>expose_php</code> prevents automated botnets from fingerprinting server software versions in HTTP response headers.</p>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>OPcache Memory Optimization &amp; Script Execution Safeguards</h2>
  <p>PHP Zend OPcache precompiles PHP scripts into shared memory bytecode, eliminating the CPU overhead of parsing and compiling PHP scripts on every HTTP request. However, on multi-tenant cPanel servers, an undersized OPcache memory buffer leads to continuous cache evictions and CPU thrashing.</p>
  <ul class="list-disc pl-6 space-y-2 text-gray-700">
    <li><strong>Production OPcache Configuration:</strong> In WHM MultiPHP INI Editor, allocate at least <code>opcache.memory_consumption = 128</code> (or 256 for large nodes) and set <code>opcache.max_accelerated_files = 10000</code>. This guarantees that all active core WordPress files reside permanently in precompiled memory.</li>
    <li><strong>Preventing Code Staling:</strong> Set <code>opcache.revalidate_freq = 60</code> to instruct PHP to check for modified files once every 60 seconds, balancing instantaneous code updates with maximum bytecode caching throughput.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 """ + blog_posts.H2 + """>Isolating Multi-Tenant Environments with CloudLinux CageFS</h2>
  <p>On standard Linux distributions (AlmaLinux, CentOS, Ubuntu), every user account can read shared directories like <code>/tmp</code> and inspect other users' running processes in <code>/proc</code>. If an attacker breaches one website, they can view configuration files and database credentials for neighboring sites.</p>
  <p>Deploying a <a href="/cloudlinux-license" """ + blog_posts.LINK + """>CloudLinux license</a> solves this fundamentally through <strong>CageFS</strong>—a virtualized per-user filesystem jail. Each tenant sees only their own files, a safe skeleton of system binaries, and an empty <code>/tmp</code> directory. Even if an attacker gains shell execution inside PHP, they cannot traverse to other customer directories or access server configuration files.</p>
  <p>For targeted troubleshooting on broken sockets and error logs, consult our practical <a href="/blog/how-to-fix-php-fpm-errors-cpanel" """ + blog_posts.LINK + """>PHP-FPM errors troubleshooting guide</a>, secure your stack with an <a href="/imunify360-license" """ + blog_posts.LINK + """>Imunify360 license</a>, and review our <a href="/license-policy" """ + blog_posts.LINK + """>License Policy</a> or speak with our engineers on our <a href="/contact" """ + blog_posts.LINK + """>contact page</a>.</p>
</section>
"""
}

new_posts = [post_1, post_2, post_3, post_4, post_5]

# Validation
for p in new_posts:
    slug = p["slug"]
    title = p["title"]
    seo_title = p["seo_title"]
    desc = p["description"]
    excerpt = p["excerpt"]
    alt = p["image_alt"]

    assert len(slug) <= 60, f"Slug too long: {len(slug)} ({slug})"
    assert len(title) <= 70, f"Title too long: {len(title)} ({title})"
    assert len(seo_title) + len(" | LicenBase") <= 60, f"SEO title too long: {len(seo_title) + 12} ({seo_title})"
    assert 110 <= len(desc) <= 160, f"Desc length error: {len(desc)} ({desc})"
    assert 100 <= len(excerpt) <= 140, f"Excerpt length error: {len(excerpt)} ({excerpt})"
    assert 40 <= len(alt) <= 125, f"Alt length error: {len(alt)} ({alt})"
    print(f"Validated post: {slug}")

# Append all 5 posts
current_slugs = {p["slug"] for p in blog_posts.POSTS}
for p in new_posts:
    if p["slug"] in current_slugs:
        for idx, existing in enumerate(blog_posts.POSTS):
            if existing["slug"] == p["slug"]:
                blog_posts.POSTS[idx] = p
                print(f"Updated post: {p['slug']}")
                break
    else:
        blog_posts.POSTS.append(p)
        print(f"Appended post: {p['slug']}")

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

print(f"Successfully serialized blog_posts.py. Total posts: {len(blog_posts.POSTS)}")

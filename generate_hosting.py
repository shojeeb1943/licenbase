import html as _html
import json
import os
import re as _re

from blog_posts import POSTS as _BLOG_POSTS
from hosting_plans import LIFETIME_NOTE, PLANS

GTM_ID = "GTM-MWQQGP5R"
GTM_HEAD = """  <script src="/assets/js/consent.js"></script>
  <!-- Google Tag Manager (Non-blocking) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function loadGTM() {
      if (window.gtmLoaded) return;
      window.gtmLoaded = true;
      window.dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
      var f = document.getElementsByTagName('script')[0],
          j = document.createElement('script');
      j.async = true;
      j.src = 'https://www.googletagmanager.com/gtm.js?id=' + 'GTM-MWQQGP5R';
      f.parentNode.insertBefore(j, f);
    }
    if ('requestIdleCallback' in window) {
      requestIdleCallback(function() { setTimeout(loadGTM, 1500); });
    } else {
      setTimeout(loadGTM, 2000);
    }
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {
      window.addEventListener(e, loadGTM, { once: true, passive: true });
    });
  </script>
  <!-- End Google Tag Manager -->
"""
GTM_BODY = """  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=""" + GTM_ID + """" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
"""

# Country list for schema shipping / merchant policies
_COUNTRIES = ["US", "GB", "CA", "AU", "DE", "IN", "BD"]
OFFER_EXTRA = {
    "shippingDetails": {
        "@type": "OfferShippingDetails",
        "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "USD"},
        "shippingDestination": [{"@type": "DefinedRegion", "addressCountry": c} for c in _COUNTRIES],
        "deliveryTime": {
            "@type": "ShippingDeliveryTime",
            "handlingTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitCode": "DAY"},
            "transitTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitCode": "DAY"},
        },
    },
    "hasMerchantReturnPolicy": {
        "@type": "MerchantReturnPolicy",
        "applicableCountry": _COUNTRIES,
        "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted",
        "merchantReturnLink": "https://licenbase.com/refund-policy",
    },
}

HOSTING_PRODUCTS = [
    {
        "filename": "managed-vps.html",
        "slug": "managed-vps",
        "name": "Managed VPS",
        "seo_title": "Cheap Managed VPS with cPanel License | LicenBase",
        "og_title": "Cheap Managed VPS with cPanel License Included",
        "seo_desc": "High-performance managed VPS hosting with cPanel & WHM license included from $19/mo. Dedicated NVMe storage, 24/7 admin support, free migration & instant setup.",
        "seo_h2": "High-Performance Managed KVM VPS with Free cPanel & WHM License",
        "seo_p1": "Running a business website or digital agency shouldn't require juggling separate server and control panel invoices. LicenBase Managed VPS bundles enterprise-grade KVM virtual servers with genuine cPanel & WHM licenses activated directly on your server's dedicated IP address. Every instance is built on PCIe Gen4 NVMe storage and high-frequency AMD EPYC processors, delivering lightning-fast database queries and sub-second page loads.",
        "seo_p2": "Our team of experienced Linux systems administrators handles the heavy lifting: initial control panel hardening, web server optimization, firewall configuration, automated nightly backups, and seamless site migrations from your old host. With root access available upon request, you get the dedicated performance of a private server paired with the peace of mind of round-the-clock proactive management.",
        "title": "Managed VPS with License Included",
        "meta_desc": "High-performance managed VPS hosting with cPanel & WHM license included from $19/mo. Dedicated NVMe storage, 24/7 admin support, free migration & instant setup.",
        "badge": "Fully Managed KVM Cloud Virtual Private Servers",
        "icon": "server",
        "headline": "Managed Cloud VPS",
        "headline_sub": "cPanel & WHM License Included.",
        "hero_desc": "Deploy fully managed, high-performance KVM virtual private servers with genuine cPanel & WHM licenses bundled directly into your plan. Enjoy dedicated NVMe storage, free white-glove migration, and 24/7 server administrator management.",
        "specs": ["cPanel License Included", "Gen4 NVMe Storage", "Full Root / WHM Access", "Free Site Migration", "24/7 Proactive Management", "99.99% Network Uptime"],
        "terms": ["monthly", "yearly"],
        "faqs": [
            {
                "q": "What does Managed VPS with license mean?",
                "a": "A Managed VPS means our certified Linux engineers take care of OS updates, security hardening, firewall configuration, web server optimization, and automated backups for you. In addition, your cPanel & WHM license is bundled into the monthly price and activated directly on your server's dedicated IP address."
            },
            {
                "q": "Do I still get root access to my managed server?",
                "a": "Yes! Unlike other hosting providers who lock you out of root access on managed servers, LicenBase provides full root SSH access and WHM administrative credentials so you retain complete control over your server environment."
            },
            {
                "q": "Will you help migrate my existing cPanel accounts?",
                "a": "Yes, we provide 100% free white-glove cPanel account migrations. Once your server is provisioned, simply open a support ticket with your previous host's credentials and our team will handle the migration with zero downtime."
            },
            {
                "q": "How is billing handled? Can I upgrade resources anytime?",
                "a": "Managed VPS plans are billed monthly or annually with significant discounts on yearly commitments. You can seamlessly scale your CPU cores, RAM, and NVMe disk space anytime from your client portal without reinstalling your OS."
            },
            {
                "q": "Where are the data centers located?",
                "a": "Our enterprise KVM virtualization clusters are hosted in Tier-3/4 redundant facilities across North America, Europe, and Asia with low-latency carrier-neutral gigabit uplinks and enterprise DDoS protection."
            },
            {
                "q": "What backup options are included?",
                "a": "Every managed VPS includes automated weekly server snapshots. Daily off-site JetBackup snapshots can be enabled from your dashboard for complete disaster recovery protection."
            }
        ],
        "related": [
            {"title": "Unmanaged VPS", "price": "From $4.50/mo", "url": "/unmanaged-vps", "desc": "Raw KVM cloud compute with full root access for custom stacks.", "icon": "server"},
            {"title": "cPanel License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "cpanel.svg"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Drop-in Apache replacement for 10x faster PHP and WordPress.", "icon": "litespeed.svg"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "AI firewall, proactive defense, and automated malware cleanup.", "icon": "imunify360.png"}
        ]
    },
    {
        "filename": "unmanaged-vps.html",
        "slug": "unmanaged-vps",
        "name": "Unmanaged VPS",
        "seo_title": "Cheap Unmanaged VPS – High Performance KVM | LicenBase",
        "og_title": "Cheap Unmanaged VPS with Root Access",
        "seo_desc": "High-performance unmanaged KVM VPS hosting from $4.50/mo. Full root access, Gen4 NVMe storage, 1 Gbps port, instant OS provisioning & automated DDoS protection.",
        "seo_h2": "High-Speed Unmanaged KVM Cloud VPS with Complete Root Control",
        "seo_p1": "For systems administrators, developers, and hosting professionals who want total control over their stack, LicenBase Unmanaged VPS provides clean, unthrottled KVM virtualization. You get pure compute power with zero bloatware or mandatory license bundles. Choose your preferred Linux distribution—including AlmaLinux, Rocky Linux, Ubuntu, Debian, or custom ISOs—and install whatever software stack your project demands.",
        "seo_p2": "Every unmanaged virtual server is backed by enterprise-grade hardware nodes featuring PCIe Gen4 NVMe storage in RAID-10 arrays and redundant 1 Gbps uplinks. With automated provisioning, self-service reboot and OS reinstall tools via our control panel, and optional wholesale licenses available directly from LicenBase at anytime, you get maximum flexibility at unbeatable prices.",
        "title": "Unmanaged VPS with Root Access",
        "meta_desc": "High-performance unmanaged KVM VPS hosting from $4.50/mo. Full root access, Gen4 NVMe storage, 1 Gbps port, instant OS provisioning & automated DDoS protection.",
        "badge": "Pure Hardware Compute · 100% Unrestricted Root Access",
        "icon": "terminal",
        "headline": "Unmanaged KVM VPS",
        "headline_sub": "Full Root Access & Pure Performance.",
        "hero_desc": "Deploy raw cloud compute power on high-frequency enterprise KVM nodes. Get 100% root access, dedicated Gen4 NVMe storage, unmetered network performance, and the freedom to configure your own software stack.",
        "specs": ["100% Root Access", "Gen4 NVMe RAID-10", "1 Gbps Network Port", "AlmaLinux / Ubuntu / Debian", "Virtualizor Control Panel", "Automated DDoS Defense"],
        "terms": ["monthly", "yearly"],
        "faqs": [
            {
                "q": "What does Unmanaged VPS mean?",
                "a": "An Unmanaged VPS provides raw virtualized server resources with full root access, where you are responsible for installing your operating system, software packages, security updates, and server maintenance."
            },
            {
                "q": "Can I install my own control panel or bring my own license?",
                "a": "Absolutely! You can install any software, panel, or docker container you wish. If you need cPanel, LiteSpeed, CloudLinux, Plesk, or Webuzo, you can purchase authentic discounted IP-bound licenses directly from LicenBase."
            },
            {
                "q": "Which operating systems are supported?",
                "a": "We provide instant 1-click OS templates for AlmaLinux 8/9, Rocky Linux 8/9, Ubuntu 22.04/24.04 LTS, Debian 11/12, and support mounting custom ISO images directly through the Virtualizor web portal."
            },
            {
                "q": "How fast is server provisioning after payment?",
                "a": "Our automated cloud provisioning engine boots your KVM virtual private server in under 60 seconds after payment confirmation, delivering your root credentials immediately by email."
            },
            {
                "q": "Is DDoS protection included on unmanaged servers?",
                "a": "Yes! All LicenBase VPS instances are shielded by automated multi-terabit inline DDoS mitigation that inspects and filters volumetric attacks before they reach your server."
            },
            {
                "q": "Can I add extra IPv4 addresses to my VPS?",
                "a": "Yes, additional dedicated clean IPv4 addresses can be ordered at checkout or added at any time from your client management portal."
            }
        ],
        "related": [
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Fully managed server with free cPanel license and 24/7 admin support.", "icon": "server"},
            {"title": "Port 25 Open VPS", "price": "From $12.00/mo", "url": "/port-25-open-vps", "desc": "Specialized cloud VPS with unblocked outbound port 25 for mail.", "icon": "mail"},
            {"title": "cPanel License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Unlimited cPanel accounts with instant IP activation.", "icon": "cpanel.svg"},
            {"title": "Virtualizor License", "price": "$3.50/mo", "url": "/virtualizor-license", "desc": "Automated virtual machine orchestration and hypervisor control.", "icon": "virtualizor.png"}
        ]
    },
    {
        "filename": "port-25-open-vps.html",
        "slug": "port-25-open-vps",
        "name": "Port 25 Open VPS",
        "seo_title": "Port 25 Open VPS – Unrestricted SMTP Servers | LicenBase",
        "og_title": "Port 25 Open VPS – Unrestricted SMTP Servers",
        "seo_desc": "Deploy high-speed VPS hosting with outbound port 25 unblocked from $12/mo. Clean dedicated IPv4, custom rDNS/PTR delegation, SPF/DKIM support & 99.99% uptime.",
        "seo_h2": "Unrestricted Outbound Port 25 VPS for Legitimate SMTP & Email Infrastructure",
        "seo_p1": "Most modern cloud and VPS providers enforce blanket outbound port 25 blocks that make self-hosting email servers or high-volume transactional relays impossible. LicenBase Port 25 Open VPS servers provide unlocked outbound port 25 connectivity out of the box, engineered specifically for businesses, newsletters, SaaS platforms, and agencies running legitimate mail servers.",
        "seo_p2": "Every mail-enabled instance includes clean dedicated IPv4 addresses from reputable IP subnets, complete self-service reverse DNS (PTR) delegation directly from your portal, and full compatibility with Postfix, Exim, Haraka, Mailcow, and cPanel mail stacks. Combine unmatched mail throughput with pure NVMe storage for rapid email queue processing and rock-solid inbox deliverability.",
        "title": "Port 25 Open VPS for Mail Infrastructure",
        "meta_desc": "Deploy high-speed VPS hosting with outbound port 25 unblocked from $12/mo. Clean dedicated IPv4, custom rDNS/PTR delegation, SPF/DKIM support & 99.99% uptime.",
        "badge": "Unblocked SMTP & Mail Infrastructure Servers",
        "icon": "mail",
        "headline": "Port 25 Open VPS",
        "headline_sub": "Unrestricted Outbound SMTP Relay.",
        "hero_desc": "Build and scale your own mail servers with unblocked outbound port 25. Enjoy clean dedicated IPv4 addresses, custom PTR/rDNS delegation, automated DNS records, and blazing-fast NVMe storage.",
        "specs": ["Outbound Port 25 Unblocked", "Clean Dedicated IPv4", "Self-Service PTR / rDNS", "Postfix & Exim Optimized", "SPF, DKIM & DMARC Ready", "99.99% Network Uptime"],
        "terms": ["monthly", "yearly"],
        "faqs": [
            {
                "q": "Is outbound port 25 really unblocked by default?",
                "a": "Yes! Unlike providers that require months of verification or completely block port 25, our Port 25 Open VPS instances have outbound TCP port 25 active upon deployment for legitimate email use."
            },
            {
                "q": "Can I configure custom reverse DNS (rDNS / PTR records)?",
                "a": "Yes! Proper PTR records are crucial for inbox deliverability. You can set and update the reverse DNS record for any of your dedicated IP addresses directly from your LicenBase control panel."
            },
            {
                "q": "Are the IP addresses clean with good sender reputation?",
                "a": "Yes. We actively monitor our subnets to ensure our IPs are free from public blacklists (Spamhaus, Barracuda, Invaluement) prior to provisioning."
            },
            {
                "q": "What is the acceptable use policy for Port 25 servers?",
                "a": "Port 25 VPS servers are intended for legitimate marketing, transactional emails, newsletter broadcasts, and mail server operations. Sending unsolicited bulk spam or malicious phishing emails is strictly prohibited and will result in immediate termination."
            },
            {
                "q": "Which mail software can I install on the server?",
                "a": "You have full root access to install any mail transfer agent (MTA) or platform, including Postfix, Exim, Haraka, Mailcow, Postal, PMTA, or full control panels like cPanel/WHM."
            },
            {
                "q": "Can I order additional IP addresses for IP rotation?",
                "a": "Yes, you can order additional clean dedicated IPv4 addresses and configure multi-IP rotation directly within your MTA software."
            }
        ],
        "related": [
            {"title": "Business Email", "price": "From $1.50/mo", "url": "/business-email", "desc": "Custom domain mailboxes with 99.9% inbox deliverability.", "icon": "mail"},
            {"title": "Unmanaged VPS", "price": "From $4.50/mo", "url": "/unmanaged-vps", "desc": "High-performance KVM cloud VPS for generic web workloads.", "icon": "terminal"},
            {"title": "cPanel License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "cPanel & WHM with built-in Exim mail server and AutoSSL.", "icon": "cpanel.svg"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Managed cloud VPS with cPanel license and 24/7 admin support.", "icon": "server"}
        ]
    },
    {
        "filename": "shared-hosting.html",
        "slug": "shared-hosting",
        "name": "Shared Hosting",
        "seo_title": "Cheap Shared Hosting – Fast NVMe & cPanel | LicenBase",
        "og_title": "Cheap Shared Hosting with Monthly, Yearly & Lifetime Plans",
        "seo_desc": "Ultra-fast shared hosting with cPanel, LiteSpeed & NVMe storage from $2.99/mo or $129 lifetime. Free SSL, 1-click apps & 99.9% uptime.",
        "seo_h2": "Ultra-Fast NVMe Shared Web Hosting with Monthly, Yearly & Lifetime Billing",
        "seo_p1": "Experience web hosting engineered for speed, stability, and simplicity. LicenBase Shared Hosting leverages enterprise LiteSpeed web servers and pure PCIe NVMe solid-state storage to deliver up to 20x faster page loading speeds than conventional Apache hosting. With the industry-standard cPanel control panel included, managing your files, databases, domain names, and business emails takes just seconds.",
        "seo_p2": "Say goodbye to recurring annual price hikes: LicenBase is one of the few premium hosting platforms offering flexible Monthly, Yearly, and genuine one-time Lifetime billing options. Every plan comes packed with free automated Let's Encrypt SSL certificates, over 450 one-click script installers via Softaculous, proactive malware scanning, and reliable 24/7 technical assistance.",
        "title": "High-Speed NVMe Shared Web Hosting",
        "meta_desc": "Ultra-fast shared hosting with cPanel, LiteSpeed & NVMe storage from $2.99/mo or $129 lifetime. Free SSL, 1-click apps & 99.9% uptime.",
        "badge": "High-Speed LiteSpeed & cPanel Web Hosting",
        "icon": "globe",
        "headline": "High-Speed Shared Hosting",
        "headline_sub": "Fast NVMe Storage & Lifetime Plans.",
        "hero_desc": "Host your websites, blogs, and eCommerce stores on ultra-fast LiteSpeed servers with NVMe SSD storage. Choose flexible monthly, yearly, or one-time lifetime billing with zero recurring fees.",
        "specs": ["LiteSpeed Web Server", "Gen4 NVMe SSD Storage", "cPanel Control Panel", "Free Unlimited SSL", "1-Click Softaculous Apps", "Lifetime Billing Option"],
        "terms": ["monthly", "yearly", "lifetime"],
        "faqs": [
            {
                "q": "What is the difference between Monthly, Yearly, and Lifetime plans?",
                "a": "Monthly and Yearly plans renew periodically according to your chosen term. A Lifetime plan is a genuine one-time payment: you pay once up front and keep your hosting account permanently active with zero renewal fees."
            },
            {
                "q": "Why is LiteSpeed web hosting faster than standard hosting?",
                "a": "LiteSpeed is an ultra-fast event-driven drop-in replacement for Apache. It handles thousands of concurrent visitors with minimal memory overhead and integrates with the LSCache plugin for sub-second WordPress loading."
            },
            {
                "q": "Is cPanel included with shared hosting accounts?",
                "a": "Yes! Every shared hosting account includes genuine cPanel with full access to File Manager, MySQL databases, phpMyAdmin, email accounts, and DNS zone management."
            },
            {
                "q": "Can I install WordPress, Joomla, or eCommerce scripts easily?",
                "a": "Yes! We include Softaculous 1-Click App Installer, which lets you install over 450 web applications—including WordPress, WooCommerce, Joomla, and PrestaShop—in under 10 seconds."
            },
            {
                "q": "Are SSL certificates included for free?",
                "a": "Yes! Automated Let's Encrypt / AutoSSL certificates are issued and renewed automatically for all your primary domains, addon domains, and subdomains."
            },
            {
                "q": "Do you provide website migration from my current host?",
                "a": "Yes, our support team offers free cPanel website migration. Simply provide your cPanel backup or login details, and we will transfer your site seamlessly."
            }
        ],
        "related": [
            {"title": "Reseller Hosting", "price": "From $28.00/mo", "url": "/reseller-hosting", "desc": "White-label cPanel reseller hosting with lifetime plans.", "icon": "users"},
            {"title": "Business Email", "price": "From $1.50/mo", "url": "/business-email", "desc": "Custom domain business email with 99.9% deliverability.", "icon": "mail"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Dedicated KVM resources bundled with cPanel license.", "icon": "server"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "10x faster PHP & WordPress speeds with LSCache.", "icon": "litespeed.svg"}
        ]
    },
    {
        "filename": "reseller-hosting.html",
        "slug": "reseller-hosting",
        "name": "Reseller Hosting",
        "seo_title": "Cheap Reseller Hosting – White-Label WHM | LicenBase",
        "og_title": "Cheap Reseller Hosting with White-Label WHM & Lifetime Plans",
        "seo_desc": "Start your web hosting agency with white-label cPanel reseller hosting from $28/mo or $360 lifetime. Private nameservers, NVMe disk & 24/7 support.",
        "seo_h2": "White-Label cPanel & WHM Reseller Hosting with Lifetime Options",
        "seo_p1": "Launch your own independent web hosting brand or streamline hosting for your agency clients with LicenBase Reseller Hosting. Powered by WebHost Manager (WHM) and CloudLinux OS, our reseller infrastructure lets you create customized cPanel packages, allocate disk space and bandwidth quotas, and rebrand client control panels with your company's logo and private nameservers.",
        "seo_p2": "With overselling enabled across all tiers, you maximize your profit margins by selling your full allocation of resources without artificial limits. Choose between convenient monthly billing or lock in permanent agency margins with our one-time Lifetime reseller plans. All accounts benefit from LiteSpeed web caching, automated daily backups, and free WHM account migration assistance.",
        "title": "White-Label cPanel & WHM Reseller Hosting",
        "meta_desc": "Start your web hosting agency with white-label cPanel reseller hosting from $28/mo or $360 lifetime. Private nameservers, NVMe disk & 24/7 support.",
        "badge": "100% White-Label Web Hosting Reseller Platform",
        "icon": "users",
        "headline": "White-Label Reseller Hosting",
        "headline_sub": "Build Your Own Hosting Brand.",
        "hero_desc": "Start your own hosting business or host all your agency clients under one roof. Full WHM root control, 100% white-label branding, private nameservers, and lifetime billing options.",
        "specs": ["Full WebHost Manager (WHM)", "Overselling Enabled", "100% White-Label Branding", "Private Custom Nameservers", "LiteSpeed Acceleration", "Lifetime Plans Available"],
        "terms": ["monthly", "yearly", "lifetime"],
        "yearly_label": "Yearly (5 Mo Free · Save 42%)",
        "faqs": [
            {
                "q": "What is white-label reseller hosting?",
                "a": "White-label reseller hosting means your clients will never see the LicenBase name. You get private custom nameservers (ns1.yourbrand.com), customized cPanel branding with your company logo, and an independent client portal."
            },
            {
                "q": "What does overselling enabled mean?",
                "a": "Overselling enabled allows you to allocate more disk space and bandwidth to client plans than your physical quota, as long as the total actual usage does not exceed your plan's aggregate limit. This maximizes your agency profits."
            },
            {
                "q": "How does the Lifetime Reseller plan work?",
                "a": "Our Lifetime Reseller plan requires a single one-time payment. You never have to pay recurring monthly or annual hosting bills for that account, allowing your agency to generate pure recurring revenue from client hosting fees."
            },
            {
                "q": "Can I connect WHMCS or billing software?",
                "a": "Yes! You can connect WHMCS, Blesta, or ClientExec to your WHM API to completely automate account provisioning, suspension, upgrades, and invoicing."
            },
            {
                "q": "Is CloudLinux OS isolation included?",
                "a": "Yes! All reseller nodes run CloudLinux with CageFS, ensuring tenant isolation so that high traffic or security issues on one client account never impact other clients on your server."
            },
            {
                "q": "Do you help transfer my accounts from my previous reseller?",
                "a": "Yes! We provide complimentary WHM-to-WHM bulk migration. Our engineers will transfer all your cPanel accounts, databases, and emails seamlessly with zero downtime."
            }
        ],
        "related": [
            {"title": "Shared Hosting", "price": "From $2.99/mo", "url": "/shared-hosting", "desc": "Affordable NVMe web hosting for individual websites.", "icon": "globe"},
            {"title": "WHMReseller License", "price": "$1.50/mo", "url": "/whmreseller-license", "desc": "Unlock Master & Alpha reseller capabilities inside WHM.", "icon": "whmreseller.png"},
            {"title": "WHMCS License", "price": "From $4.00/mo", "url": "/whmcs-license", "desc": "Automate billing, domain management, and client support.", "icon": "whmcs.svg"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Dedicated cloud VPS with cPanel license and 24/7 admin.", "icon": "server"}
        ]
    },
    {
        "filename": "business-email.html",
        "slug": "business-email",
        "name": "Business Email",
        "seo_title": "Cheap Business Email Hosting – Custom Domain | LicenBase",
        "og_title": "Professional Business Email Hosting on Your Custom Domain",
        "seo_desc": "Professional business email hosting on your custom domain from $2.49/mo. 5GB storage, ClamAV antivirus, mobile IMAP sync, auto-responders & 99.99% uptime.",
        "seo_h2": "Professional Business Email Hosting on Your Custom Domain",
        "seo_p1": "Enhance your business credibility with a personalized email using your domain name instead of free email IDs. A unique email identity helps customers establish their brand, project corporate reliability, and make a lasting impression on clients. LicenBase Business Email delivers dedicated, ad-free mailboxes engineered for fast delivery and seamless multi-device synchronization.",
        "seo_p2": "Built around high-performance storage infrastructure with a 99.99% uptime SLA, each account receives 5 GB of dedicated space, inbuilt ClamAV antivirus protection, and automated auto-responder tools. Easily scale from a single professional address up to 49 mailboxes with flexible per-address billing and 24/7 technical assistance.",
        "title": "Business Email Hosting on Custom Domain",
        "meta_desc": "Professional business email hosting on your custom domain from $2.49/mo. 5GB storage, ClamAV antivirus, mobile IMAP sync, auto-responders & 99.99% uptime.",
        "badge": "Personalized Domain Business Email Hosting",
        "icon": "mail",
        "headline": "Business Email Hosting",
        "headline_sub": "Personalized Email with 5GB Storage & Mobile Access.",
        "hero_desc": "Enhance your business credibility with personalized email using your domain name instead of free email IDs. Includes 5GB storage per account, ClamAV antivirus, multi-device mobile sync, and 99.99% uptime.",
        "specs": [
            "1 Email Account Included",
            "Upgradable to 49 Accounts",
            "5 GB Storage per Account",
            "Inbuilt Virus Protection (ClamAV)",
            "Mobile & Tablet IMAP Support",
            "99.99% Uptime Guarantee"
        ],
        "terms": ["monthly", "yearly"],
        "features_grid": {
            "eyebrow": "Business Email Hosting Features",
            "title": "Business Email Hosting Features",
            "subtitle": "Discover the high-performance features built into your LicenBase business email account.",
            "cards": [
                {
                    "icon": "mail",
                    "title": "Personalized Business Email",
                    "desc": "Enhance your business credibility with a personalized email using your domain name instead of free email IDs. A unique email identity helps customers establish their brand and make a lasting impression on clients."
                },
                {
                    "icon": "smartphone",
                    "title": "Mobile Access",
                    "desc": "Business Email with IMAP lets your customers connect their default app on iPhone, Android or Windows. Get the maximum flexibility to answer and manage your email while you're on the move."
                },
                {
                    "icon": "hard-drive",
                    "title": "Abundant Storage",
                    "desc": "Get 5 GB space in our all-new business email hosting offering that is built around state-of-the-art storage devices with 99.99% uptime. Our robust storage architecture ensures that your data is always safe and available."
                },
                {
                    "icon": "activity",
                    "title": "99.99% Uptime",
                    "desc": "We built our infrastructure with a focus on stability, scalability, and security, ensuring top performance. Our advanced datacenter, featuring the latest hardware and networking technology, guarantees 99.99% uptime."
                },
                {
                    "icon": "shield-check",
                    "title": "Stay Protected",
                    "desc": "We offer an advanced anti-virus from ClamAV along with spam protection. Our customized email account protects you from spam barrages that free account users often face. Thus, your customers are covered from all online threats and junk mails."
                },
                {
                    "icon": "send",
                    "title": "Auto-Responder",
                    "desc": "An auto responder is a fantastic feature setup for your email address that sends out an instant pre-written email to your recipient(s) when a message hits your inbox. You can find out more about setting up autoresponders on our knowledge base."
                }
            ]
        },
        "why_choose": {
            "eyebrow": "Signing Certificate & Enterprise Security",
            "title": "Why Use an Email Hosting",
            "subtitle": "Enterprise reliability, privacy-first mail protection, and seamless collaboration built for modern businesses.",
            "cards": [
                {
                    "icon": "archive",
                    "title": "Secure Email Archiving & Recovery",
                    "desc": "Securely store and retrieve emails with automated archiving, ensuring data protection and compliance."
                },
                {
                    "icon": "users",
                    "title": "Seamless Collaboration Tools",
                    "desc": "Enhance teamwork with integrated tools for file sharing, real-time communication, and task management."
                },
                {
                    "icon": "shield",
                    "title": "Ad-Free & Reliable Email Hosting",
                    "desc": "Enjoy clean, distraction-free inbox management with zero advertising, zero tracking, and 99.99% reliable email delivery."
                },
                {
                    "icon": "globe",
                    "title": "Stay Connected Anytime, Anywhere",
                    "desc": "Stay connected anywhere with synchronized email access across multiple devices."
                },
                {
                    "icon": "shield-alert",
                    "title": "Malware Protection",
                    "desc": "Protect your inbox with advanced spam filters and malware protection to prevent cyber threats."
                },
                {
                    "icon": "headset",
                    "title": "24/7 Dedicated Expert Support",
                    "desc": "Get round-the-clock technical assistance to resolve email hosting issues instantly."
                }
            ]
        },
        "steps": [
            {
                "num": "1",
                "title": "Choose Domain & Accounts",
                "desc": "Select your plan, connect your custom domain name, and configure 1 to 49 personalized email addresses."
            },
            {
                "num": "2",
                "title": "Automated Mail Provisioning",
                "desc": "Our cloud engine automatically partitions your 5GB storage, configures DNS authentication, and activates ClamAV protection."
            },
            {
                "num": "3",
                "title": "Connect on Mobile, Tablet & Web",
                "desc": "Access your inbox instantly via modern Webmail or sync your default mail app on iPhone, Android, or Windows."
            }
        ],
        "faqs": [
            {
                "q": "How many email accounts are included in this package?",
                "a": "The package includes 1 business email account with 5 GB storage. You can easily upgrade up to 49 email accounts with different flexible billing per address directly from your client management portal."
            },
            {
                "q": "Can I use my existing domain name for personalized email?",
                "a": "Yes! You can connect any domain you own to create personalized business email addresses (e.g. name@yourbrand.com). A unique email identity establishes credibility and makes a lasting impression on clients."
            },
            {
                "q": "Can I access my business email on mobile phones and tablets?",
                "a": "Yes! Our email hosting supports standard IMAP, POP3, and SMTP protocols. You can easily connect your default email apps on iPhone (iOS), Android, Windows, macOS, Outlook, and Thunderbird."
            },
            {
                "q": "How does ClamAV antivirus and spam protection work?",
                "a": "We provide inbuilt ClamAV antivirus filtering along with advanced spam protection to shield your inboxes from online threats, junk mail barrages, and malware attachments."
            },
            {
                "q": "How much storage is included per email account?",
                "a": "You get 5 GB of high-speed cloud storage per email account, built around state-of-the-art storage architecture with a 99.99% uptime guarantee."
            },
            {
                "q": "What is an auto-responder and how does it work?",
                "a": "An auto-responder sends an instant pre-written email to your recipients whenever a message arrives in your inbox—perfect for out-of-office notifications, customer receipts, or support confirmations."
            }
        ],
        "related": [
            {"title": "Shared Hosting", "price": "From $2.99/mo", "url": "/shared-hosting", "desc": "Web hosting with cPanel, LiteSpeed & free email accounts.", "icon": "globe"},
            {"title": "Port 25 Open VPS", "price": "From $12.00/mo", "url": "/port-25-open-vps", "desc": "Dedicated server with unblocked outbound port 25 for relays.", "icon": "mail"},
            {"title": "Reseller Hosting", "price": "From $28.00/mo", "url": "/reseller-hosting", "desc": "White-label hosting to sell web hosting & email to clients.", "icon": "users"},
            {"title": "cPanel License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Host unlimited email accounts on your own private server.", "icon": "cpanel.svg"}
        ]
    },
    {
        "filename": "n8n-hosting.html",
        "slug": "n8n-hosting",
        "name": "n8n Hosting",
        "seo_title": "n8n Hosting – Self-Hosted Workflow Automation | LicenBase",
        "og_title": "Managed n8n Hosting – Self-Hosted Workflow Automation",
        "seo_desc": "Deploy dedicated n8n workflow hosting from $9/mo or $420 lifetime. Unlimited executions, PostgreSQL, daily backups, 99.99% uptime SLA & instant setup.",
        "seo_h2": "Production-Ready Dedicated n8n Workflow Automation Cloud Hosting",
        "seo_p1": "Take complete ownership of your workflow automations without being penalized by per-execution billing limits. LicenBase n8n Hosting provisions a dedicated, fully managed environment running the powerful open-source n8n workflow engine on high-speed NVMe servers. Automate cross-platform pipelines, connect custom APIs, and execute complex conditional logic with zero restrictions.",
        "seo_p2": "Unlike multi-tenant cloud platforms that throttle executions during peak periods, every LicenBase n8n instance features dedicated compute allocations, a pre-configured PostgreSQL database, priority queue capabilities for heavy task concurrency, and automated SSL encryption. Easily install community nodes, trigger secure webhooks, and enjoy automated daily database snapshots.",
        "title": "Dedicated Cloud Hosting for n8n Workflow Automation",
        "meta_desc": "Deploy dedicated n8n workflow hosting from $9/mo or $420 lifetime. Unlimited executions, PostgreSQL, daily backups, 99.99% uptime SLA & instant setup.",
        "badge": "Dedicated Self-Hosted n8n Workflow Automation Platform",
        "icon": "workflow",
        "headline": "Dedicated n8n Hosting",
        "headline_sub": "Self-Hosted Automation with Unlimited Runs.",
        "hero_desc": "Host your own n8n automation engine on dedicated cloud instances from $9/mo or $420 lifetime. Execute unlimited workflow runs, integrate services, connect webhooks, and automate forever.",
        "specs": ["Unlimited Executions", "Unlimited Workflows", "Unlimited Storage", "PostgreSQL Database", "Custom Subdomain & Free SSL", "Daily Automated Backups"],
        "terms": None,
        "faqs": [
            {
                "q": "Why choose self-hosted n8n over n8n Cloud?",
                "a": "Self-hosted n8n gives you complete data privacy, unlimited workflow executions, and zero arbitrary plan limits. On n8n Cloud, you pay heavily for high execution volumes, whereas on LicenBase you only pay for the underlying server resources."
            },
            {
                "q": "Can I install community and custom npm nodes?",
                "a": "Yes! Because you have your own dedicated container environment, you can install any public community node, private npm package, or custom Python script without restrictions."
            },
            {
                "q": "What database is used for storing workflow data?",
                "a": "All production n8n plans are backed by a dedicated PostgreSQL database container with connection pooling, avoiding the corruption and concurrency issues associated with SQLite."
            },
            {
                "q": "Can I connect my own custom domain with SSL?",
                "a": "Yes, you can bind your instance to your custom domain or subdomain (e.g., auto.yourcompany.com). An automated Let's Encrypt SSL certificate is provisioned and renewed automatically."
            },
            {
                "q": "How does high-volume execution work across tiers?",
                "a": "On our Professional, Growth, and Lifetime tiers, we configure dedicated compute allocations and priority worker queues so long-running or webhook-intensive tasks never block the main web UI or trigger timeout errors."
            },
            {
                "q": "Are automated backups included?",
                "a": "Yes! Daily automated snapshots of your workflow configurations, execution history, and database credentials are taken and stored on isolated off-site backup storage."
            }
        ],
        "related": [
            {"title": "OpenClaw Hosting", "price": "From $9.00/mo", "url": "/openclaw-hosting", "desc": "High-concurrency web scraping and browser automation cloud.", "icon": "bot"},
            {"title": "Hermes Agent Hosting", "price": "From $9.00/mo", "url": "/hermes-agent-hosting", "desc": "Continuous cloud runtime for autonomous AI agents.", "icon": "bot"},
            {"title": "Unmanaged VPS", "price": "From $4.50/mo", "url": "/unmanaged-vps", "desc": "Pure KVM compute with full root access for custom stacks.", "icon": "terminal"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Fully managed KVM cloud VPS with cPanel license included.", "icon": "server"}
        ]
    },
        {
        "filename": "openclaw-hosting.html",
        "slug": "openclaw-hosting",
        "name": "OpenClaw Hosting",
        "seo_title": "OpenClaw Hosting – Multi-Channel AI Bot Cloud | LicenBase",
        "og_title": "OpenClaw Hosting – Dedicated Multi-Channel AI Bot Platform",
        "seo_desc": "Deploy OpenClaw AI bots on high-performance cloud hosting from $14/mo or $380 lifetime. Connect GPT-4o, Claude, Llama & Kimi to WhatsApp, Telegram & Discord.",
        "seo_h2": "Autonomous Multi-Channel AI Bot Cloud Hosting with Lifetime Billing",
        "seo_p1": "Automate customer support, lead qualification, conversational sales, and repetitive workflows with dedicated cloud infrastructure for OpenClaw AI agents. Connect leading frontier models including OpenAI GPT-4o, Anthropic Claude, Meta Llama, and Moonshot Kimi directly to your favorite business messaging channels.",
        "seo_p2": "Enjoy zero per-message surcharges and complete architectural control. OpenClaw provides direct integrations across WhatsApp, Telegram, Discord, and 40+ messaging networks with customizable bot personas, full administrative dashboards, automated skills, and 99.99% guaranteed uptime.",
        "title": "OpenClaw Multi-Channel AI Bot Cloud Hosting",
        "meta_desc": "Deploy OpenClaw AI bots on high-performance cloud hosting from $14/mo or $380 lifetime. Connect GPT-4o, Claude, Llama & Kimi to WhatsApp, Telegram & Discord.",
        "badge": "Multi-Channel Autonomous AI Bot Platform",
        "icon": "bot",
        "headline": "OpenClaw AI Hosting",
        "headline_sub": "Autonomous Multi-Channel AI Bots.",
        "hero_desc": "Run autonomous AI bots and smart conversational agents 24/7 across WhatsApp, Telegram, Discord, and 40+ channels. Powered by GPT-4o, Claude, Llama, and Kimi with zero message fees.",
        "specs": ["GPT-4o, Claude, Llama & Kimi", "WhatsApp, Telegram, Discord & 40+ Channels", "Unlimited Skills & Workflows", "Custom Bot Personas", "99.99% Uptime SLA", "Free Installation & White-Glove Setup"],
        "terms": ["monthly", "lifetime"],
        "faqs": [
            {
                "q": "What is OpenClaw AI hosting?",
                "a": "OpenClaw hosting provides a dedicated, high-availability cloud environment engineered to host and run autonomous AI chatbots and workflows connected to LLMs like GPT-4o, Claude, and Llama."
            },
            {
                "q": "Which messaging channels are supported by OpenClaw?",
                "a": "OpenClaw natively supports 40+ channels including WhatsApp Business API, Telegram Bot API, Discord, Slack, Messenger, email, and REST webhooks."
            },
            {
                "q": "Can I connect my own AI API keys or models?",
                "a": "Yes. OpenClaw lets you bring your own API keys for OpenAI (GPT-4o), Anthropic (Claude 3.5 Sonnet / Opus), Meta Llama, and Moonshot Kimi, or route requests through custom local or cloud inference endpoints."
            },
            {
                "q": "Is free setup and migration assistance included?",
                "a": "Yes, our technical team provides complimentary white-glove setup, assisting you with channel webhook configurations and prompt persona onboarding."
            },
            {
                "q": "How does the Lifetime license work?",
                "a": "The OpenClaw Lifetime plan is a single one-time payment of $380 with zero recurring subscription fees. It includes unlimited storage, unlimited skills, lifetime platform updates, and priority technical support."
            }
        ],
        "related": [
            {"title": "n8n Cloud Hosting", "price": "From $9.00/mo", "url": "/n8n-hosting", "desc": "Self-hosted workflow automation with unlimited runs.", "icon": "workflow"},
            {"title": "Hermes Agent Hosting", "price": "From $12.00/mo", "url": "/hermes-agent-hosting", "desc": "Autonomous LLM reasoning & agent execution environment.", "icon": "brain"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Dedicated KVM resources bundled with cPanel license.", "icon": "server"},
            {"title": "Shared Hosting", "price": "From $2.99/mo", "url": "/shared-hosting", "desc": "High-speed NVMe hosting with cPanel & LiteSpeed.", "icon": "globe"}
        ]
    },
    {
        "filename": "hermes-agent-hosting.html",
        "slug": "hermes-agent-hosting",
        "name": "Hermes Agent Hosting",
        "seo_title": "Hermes Agent Hosting – Autonomous AI Agent Cloud | LicenBase",
        "og_title": "Hermes Agent Hosting – Autonomous AI Agent Infrastructure",
        "seo_desc": "Deploy autonomous AI agents with dedicated Hermes Agent cloud hosting from $14/mo or $380 lifetime. Auto-deployed, private SSL subdomain & 99.99% SLA.",
        "seo_h2": "Dedicated Cloud Infrastructure for Hermes Agent & Autonomous AI Workflows",
        "seo_p1": "Running autonomous AI agents and long-horizon tasks requires continuous, persistent execution environments that never sleep or drop context. LicenBase Hermes Agent Hosting provides dedicated cloud sandboxes purpose-built for executing agentic reasoning loops, background tool calls, local code interpreters, and multi-agent coordination frameworks.",
        "seo_p2": "Each instance is pre-configured with modern Python 3.11+, persistent NVMe scratch disks for state management, ready-to-use vector databases, and secure webhook and REST API endpoints. With automated process supervisors guaranteeing that your agent daemons stay online 24/7, you can deploy autonomous agents with absolute confidence.",
        "title": "Hermes Agent Cloud Hosting Infrastructure",
        "meta_desc": "Deploy autonomous AI agents with dedicated Hermes Agent cloud hosting from $14/mo or $380 lifetime. Auto-deployed, private SSL subdomain & 99.99% SLA.",
        "badge": "Continuous Cloud Runtime for Autonomous AI Agents",
        "icon": "bot",
        "headline": "Hermes Agent Hosting",
        "headline_sub": "Autonomous AI Agent Cloud Infrastructure.",
        "hero_desc": "Deploy dedicated cloud sandboxes optimized for Hermes Agent and autonomous AI agent workflows. Auto-deployed in minutes with private SSL subdomain, BYOK support, and full start/stop daemon controls.",
        "specs": ["Auto-deployed in minutes", "Private SSL-secured subdomain", "Bring your own LLM key", "Start / stop / restart controls", "99.99% uptime SLA", "Zero recurring fees lifetime option"],
        "terms": ["monthly", "lifetime"],
        "faqs": [
            {
                "q": "What is Hermes Agent Hosting?",
                "a": "It is a specialized cloud compute environment configured to host long-running autonomous AI agents, tool-calling frameworks, code sandboxes, and vector databases with persistent memory."
            },
            {
                "q": "Why not run agents on serverless functions?",
                "a": "Serverless platforms enforce harsh execution timeouts (usually 5 to 15 minutes) and suffer from cold-start penalties and stateless memory wipes. Hermes Agent Hosting provides 24/7 continuous execution with persistent local disk storage."
            },
            {
                "q": "How does the BYOK (Bring Your Own Key) model work?",
                "a": "You supply your own OpenAI, Anthropic, or open-source API keys directly into your private environment. LicenBase charges zero token markups or per-call query surcharges."
            },
            {
                "q": "Can I control my agent daemons directly?",
                "a": "Yes! You have full web and API start, stop, and restart controls over your agent background services, as well as real-time terminal log streaming."
            },
            {
                "q": "What is included with the Lifetime Plan?",
                "a": "The Hermes Agent Lifetime plan is a single one-time payment of $380 with zero recurring monthly or annual bills. You receive persistent cloud resources, lifetime platform updates, and priority engineering support."
            }
        ],
        "related": [
            {"title": "OpenClaw Hosting", "price": "From $14.00/mo", "url": "/openclaw-hosting", "desc": "Multi-channel AI bot & agent automation cloud.", "icon": "bot"},
            {"title": "n8n Cloud Hosting", "price": "From $9.00/mo", "url": "/n8n-hosting", "desc": "Self-hosted workflow automation for pipeline processing.", "icon": "workflow"},
            {"title": "Unmanaged VPS", "price": "From $4.50/mo", "url": "/unmanaged-vps", "desc": "Pure KVM compute with full root access.", "icon": "terminal"},
            {"title": "Managed VPS", "price": "From $19.00/mo", "url": "/managed-vps", "desc": "Fully managed KVM cloud VPS with cPanel license.", "icon": "server"}
        ]
    }
]

def money(v):
    return f"${v:,.2f}"

def generate_hosting_page(p):
    plans = PLANS.get(p["slug"], [])
    terms = p.get("terms", ["monthly", "yearly"])

    if p["slug"] in ("n8n-hosting", "openclaw-hosting", "hermes-agent-hosting"):
        # 4 distinct package cards in a responsive grid
        card_items = []
        for t in plans:
            is_pop = t.get("popular", False)
            pop_border = "border-2 border-brand shadow-xl relative scale-[1.02] z-10" if is_pop else "border border-gray-200 shadow-md"
            pop_badge = '<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">Most Popular</div>' if is_pop else ""
            btn_class = "lb-btn lb-btn--primary w-full shadow-md shadow-brand/20" if is_pop else "lb-btn lb-btn--secondary w-full"

            features_li = "".join([
                f'<li class="flex items-start gap-2.5 text-sm text-gray-600"><i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent mt-0.5" aria-hidden="true"></i><span>{feat}</span></li>'
                for feat in t.get("specs", [])
            ])

            savings_html = f'<div class="mt-2 text-xs font-semibold text-accentDeep bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full inline-block">{t["savings"]}</div>' if "savings" in t else ""

            card_items.append(f"""
        <div class="flex flex-col justify-between rounded-3xl bg-white p-6 sm:p-7 {pop_border} transition-all duration-300 hover:shadow-2xl">
          <div>
            {pop_badge}
            <div class="flex items-center justify-between">
              <span class="rounded-full bg-brandSoft px-3 py-1 text-xs font-bold uppercase tracking-wide text-brand">{t["badge"]}</span>
              <span class="inline-flex items-center gap-1 text-xs font-semibold text-accent">Instant Setup</span>
            </div>

            <h3 class="mt-4 font-display text-2xl font-bold text-navy">{t["name"]}</h3>
            <p class="mt-1 text-xs font-semibold text-brand">{t.get("tagline", "")}</p>
            <p class="mt-2 text-xs leading-relaxed text-gray-500">{t["desc"]}</p>

            <div class="mt-5 border-y border-gray-100 py-4 bg-mist/40 -mx-6 px-6 sm:-mx-7 sm:px-7">
              <div class="flex items-baseline gap-1">
                <span class="font-display text-4xl font-extrabold tracking-tight text-navy">{t["price_str"]}</span>
                <span class="text-sm font-semibold text-gray-500">/{t.get("period_label", "mo")}</span>
              </div>
              <p class="mt-1 text-xs font-medium text-gray-600">{t.get("cycle_label", "")}</p>
              {savings_html}
            </div>

            <ul class="mt-6 space-y-3">
              {features_li}
            </ul>
          </div>

          <div class="mt-8 pt-4 border-t border-gray-100">
            <a href="{t['url']}" class="{btn_class}">
              <span>Order {t['name']}</span>
              <i data-lucide="arrow-right" class="h-4 w-4"></i>
            </a>
            <p class="mt-2 text-center text-[11px] text-gray-400">Instant Automated Provisioning · Guaranteed Uptime</p>
          </div>
        </div>
            """)

        grid_cls = "grid gap-8 sm:grid-cols-2 max-w-4xl mx-auto" if len(plans) == 2 else "grid gap-6 sm:grid-cols-2 xl:grid-cols-4"
        tiers_html = f'<div class="{grid_cls}">{"".join(card_items)}</div>'
    elif p["slug"] == "port-25-open-vps":
        tiers_html = """
<div id="vps-plans-widget" style="width: 100%; max-width: 1200px; margin: 2rem auto; box-sizing: border-box; font-family: inherit;">
  <div id="vps-plans-state" style="text-align: center; padding: 2.5rem 1rem; color: #64748b; font-size: 0.95rem;">
    Loading available VPS plans...
  </div>
</div>

<script>
(function () {
  var PORT25_PLAN_IDS = [];
  var DASH = 'https://dashboard.licenbase.com/index.php?m=vpsorder';

  var container = document.getElementById('vps-plans-widget');

  function esc(s) {
    if (s == null) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function parsePrice(s) {
    if (!s) return Infinity;
    var n = parseFloat(String(s).replace(/[^0-9.]/g, ''));
    return isNaN(n) ? Infinity : n;
  }

  function renderFallback() {
    container.innerHTML =
      '<div style="text-align: center; padding: 2.5rem 1.5rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 1rem;">' +
        '<p style="font-size: 1rem; color: #1e293b; font-weight: 600; margin: 0 0 1rem 0;">Explore VPS Plans</p>' +
        '<a href="' + esc(DASH) + '" style="display: inline-block; background: #2563eb; color: #ffffff; padding: 0.75rem 1.75rem; border-radius: 0.5rem; font-weight: 700; text-decoration: none; font-size: 0.9rem;">View plans &rarr;</a>' +
      '</div>';
  }

  fetch(DASH + '&action=plans&src=mkt', { credentials: 'omit' })
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function (data) {
      if (!data || !Array.isArray(data.locations)) {
        renderFallback();
        return;
      }

      var allItems = [];
      var activeLocations = [];
      var dupMap = {};

      data.locations.forEach(function (loc) {
        var locName = loc.name || '';
        var locFlag = loc.flag || '';
        var locPlansCount = 0;

        (loc.dcs || []).forEach(function (dc) {
          if (dc.soldout) return;
          var dcId = dc.id;
          var dcCpu = dc.cpu || '';

          (dc.plans || []).forEach(function (plan) {
            var planId = plan.id;
            if (PORT25_PLAN_IDS.length > 0 && PORT25_PLAN_IDS.indexOf(planId) === -1) {
              return;
            }
            var p1 = (plan.prices && (plan.prices['1'] || plan.prices[1])) || '';
            var item = {
              dcId: dcId,
              dcCpu: dcCpu,
              planId: planId,
              name: plan.name || '',
              cpu: plan.cpu,
              ram: plan.ram,
              disk: plan.disk,
              eth: plan.eth || '',
              location: locName,
              flag: locFlag,
              priceStr: p1,
              priceNum: parsePrice(p1)
            };

            allItems.push(item);
            locPlansCount++;

            var dupKey = locName + '||' + item.name + '||' + p1;
            dupMap[dupKey] = (dupMap[dupKey] || 0) + 1;
          });
        });

        if (locPlansCount > 0) {
          activeLocations.push({
            name: locName,
            flag: locFlag
          });
        }
      });

      if (!allItems.length) {
        renderFallback();
        return;
      }

      var currentLoc = 'all';

      container.innerHTML =
        '<div id="vps-loc-tabs" style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; align-items: center; margin-bottom: 2rem;"></div>' +
        '<div id="vps-plans-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.5rem;"></div>';

      var tabsContainer = document.getElementById('vps-loc-tabs');
      var gridContainer = document.getElementById('vps-plans-grid');

      function getTabStyle(isActive) {
        if (isActive) {
          return 'background: #2563eb; color: #ffffff; border: 1px solid #2563eb; padding: 0.45rem 0.85rem; border-radius: 9999px; font-size: 0.825rem; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; box-shadow: 0 2px 4px rgba(37,99,235,0.2); transition: all 0.15s ease;';
        }
        return 'background: #ffffff; color: #475569; border: 1px solid #cbd5e1; padding: 0.45rem 0.85rem; border-radius: 9999px; font-size: 0.825rem; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; transition: all 0.15s ease;';
      }

      function renderTabs() {
        var tabsHtml = '';
        var isAllActive = (currentLoc === 'all');
        tabsHtml += '<button type="button" data-loc="all" style="' + getTabStyle(isAllActive) + '">All</button>';

        activeLocations.forEach(function (loc) {
          var isActive = (currentLoc === loc.name);
          var flagImg = loc.flag
            ? '<img src="https://flagcdn.com/w20/' + esc(loc.flag.toLowerCase()) + '.png" alt="" width="16" height="12" style="width: 16px !important; height: 12px !important; min-width: 16px !important; max-height: 12px !important; display: inline-block !important; object-fit: cover; border-radius: 2px; vertical-align: middle; margin-right: 6px; flex-shrink: 0;">'
            : '';
          tabsHtml +=
            '<button type="button" data-loc="' + esc(loc.name) + '" style="' + getTabStyle(isActive) + '">' +
              flagImg +
              '<span>' + esc(loc.name) + '</span>' +
            '</button>';
        });

        tabsContainer.innerHTML = tabsHtml;

        var buttons = tabsContainer.querySelectorAll('button[data-loc]');
        buttons.forEach(function (btn) {
          btn.addEventListener('click', function () {
            currentLoc = btn.getAttribute('data-loc');
            renderTabs();
            renderGrid();
          });
        });
      }

      function renderGrid() {
        var filtered = allItems.filter(function (item) {
          if (currentLoc === 'all') return true;
          return item.location === currentLoc;
        });

        filtered.sort(function (a, b) {
          return a.priceNum - b.priceNum;
        });

        if (!filtered.length) {
          gridContainer.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: #64748b;">No plans currently available in this location.</div>';
          return;
        }

        var out = '';
        filtered.forEach(function (p) {
          var orderUrl = DASH + '&dc=' + encodeURIComponent(p.dcId) + '&tarif=' + encodeURIComponent(p.planId);
          var flagEl = p.flag
            ? '<img src="https://flagcdn.com/w20/' + esc(p.flag.toLowerCase()) + '.png" alt="" width="16" height="12" style="width: 16px !important; height: 12px !important; min-width: 16px !important; max-height: 12px !important; display: inline-block !important; object-fit: cover; border-radius: 2px; vertical-align: middle; margin: 0 !important; padding: 0 !important; flex-shrink: 0;">'
            : '';

          var dupKey = p.location + '||' + p.name + '||' + p.priceStr;
          var cpuLine = (dupMap[dupKey] > 1 && p.dcCpu)
            ? '<div style="font-size: 0.75rem; color: #64748b; margin-top: -0.25rem; margin-bottom: 0.6rem; line-height: 1.3;">' + esc(p.dcCpu) + '</div>'
            : '';

          out +=
            '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">' +
              '<div>' +
                '<div style="margin-bottom: 0.75rem;">' +
                  '<span style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.75rem; font-weight: 700; color: #2563eb; background: #eff6ff; padding: 0.25rem 0.65rem; border-radius: 9999px; text-transform: uppercase;">' +
                    flagEl +
                    '<span>' + esc(p.location) + '</span>' +
                  '</span>' +
                '</div>' +
                '<h4 style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin: 0 0 0.5rem 0;">' + esc(p.name) + '</h4>' +
                cpuLine +
                '<div style="font-size: 1.65rem; font-weight: 800; color: #0f172a; margin-bottom: 1rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem;">' +
                  esc(p.priceStr) + '<span style="font-size: 0.875rem; font-weight: 500; color: #64748b;"> / mo</span>' +
                '</div>' +
                '<ul style="list-style: none; padding: 0; margin: 0 0 1.5rem 0; font-size: 0.875rem; color: #475569; display: grid; gap: 0.5rem;">' +
                  '<li><strong>' + esc(p.cpu) + '</strong> vCPU</li>' +
                  '<li><strong>' + esc(p.ram) + ' GB</strong> RAM</li>' +
                  '<li><strong>' + esc(p.disk) + ' GB</strong> Disk</li>' +
                  '<li><strong>' + esc(p.eth) + '</strong> Network</li>' +
                '</ul>' +
              '</div>' +
              '<a href="' + esc(orderUrl) + '" style="display: block; text-align: center; background: #2563eb; color: #ffffff; padding: 0.75rem 1rem; border-radius: 0.5rem; font-weight: 700; text-decoration: none; font-size: 0.9rem;">Order now &rarr;</a>' +
            '</div>';
        });

        gridContainer.innerHTML = out;
      }

      renderTabs();
      renderGrid();
    })
    .catch(function () {
      renderFallback();
    });
})();
</script>
"""
    else:
        # Billing Switcher Tabs
        tabs_html = ""
        if terms and len(terms) > 1:
            yearly_label = p.get("yearly_label", "Yearly (Save ~17%)")
            labels = {"monthly": "Monthly Billing", "yearly": yearly_label, "lifetime": "Lifetime Plan (Pay Once)"}
            tab_buttons = "".join(
                f'<button type="button" data-term="{t}" aria-pressed="{"true" if t == terms[0] else "false"}" '
                f'class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 {"bg-brand text-white shadow-md shadow-brand/20" if t == terms[0] else "text-gray-600 hover:text-navy"}">{labels.get(t, t.title())}</button>'
                for t in terms
            )
            tabs_html = f"""
        <div class="mb-10 flex justify-center">
          <div role="group" aria-label="Billing period switcher" class="inline-flex rounded-2xl border border-gray-200 bg-mist p-1.5 shadow-inner">
            {tab_buttons}
          </div>
        </div>
        """

        # Multi-term cards
        grid_cols = "md:grid-cols-2" if len(plans) == 2 else ("md:grid-cols-3" if len(plans) == 3 else "max-w-xl mx-auto")
        tiers_html = f'{tabs_html}<div class="grid gap-8 {grid_cols}">'

        for t in plans:
            pop_border = "border-2 border-brand shadow-xl relative scale-[1.02] z-10" if t.get("popular") else "border border-gray-200 shadow-md"
            pop_badge = f'<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">Most Popular</div>' if t.get("popular") else ""

            features_li = "".join([
                f'<li class="flex items-start gap-3 text-sm text-gray-600"><i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent mt-0.5" aria-hidden="true"></i><span>{feat}</span></li>'
                for feat in t.get("specs", [])
            ])

            btn_class = "lb-btn lb-btn--primary w-full shadow-md" if t.get("popular") else "lb-btn lb-btn--secondary w-full"

            # Price elements for each term
            price_elements = ""
            for term in (terms or []):
                hidden_class = "" if term == terms[0] else "hidden "
                if term in t["prices"]:
                    period_label = "per month" if term == "monthly" else ("per year" if term == "yearly" else "one-time")
                    price_str = f"${t['prices'][term]:,.2f}"
                    discount_sub = ""
                    if term == "yearly" and "yearly_base" in t:
                        badge_text = t.get("discount_badge", "Save 17%")
                        discount_sub = f'<span class="ml-2 text-xs font-semibold text-accentDeep bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-full">{badge_text}</span><span class="ml-1 text-xs line-through text-gray-400">${t["yearly_base"]:,.2f}</span>'
                    price_elements += f"""
                    <div data-price="{term}" class="{hidden_class}mt-6 flex flex-wrap items-baseline gap-1 border-b border-gray-100 pb-6">
                      <span class="font-display text-4xl font-extrabold tracking-tight text-navy">{price_str}</span>
                      <span class="text-sm font-semibold text-gray-500">/{period_label}</span>
                      {discount_sub}
                    </div>
                    """
                else:
                    price_elements += f"""
                    <div data-price="{term}" class="{hidden_class}mt-6 flex items-baseline gap-1 border-b border-gray-100 pb-6">
                      <span class="font-display text-3xl font-bold tracking-tight text-navy">Contact Sales</span>
                    </div>
                    """

            # CTA buttons for each term
            cta_buttons = ""
            for term in (terms or []):
                hidden_class = "" if term == terms[0] else "hidden "
                term_url = t.get("urls", {}).get(term, t.get("url"))
                term_label = f"Order {t['name']}"
                if term == "monthly":
                    term_label = f"Order {t['name']} (Monthly)"
                elif term == "yearly":
                    term_label = f"Order {t['name']} (Annual)"
                elif term == "lifetime":
                    term_label = f"Order {t['name']} (Lifetime)"

                cta_buttons += f"""
                <div data-cta="{term}" class="{hidden_class}w-full">
                  <a href="{term_url}" class="{btn_class}">
                    <span>{term_label}</span>
                    <i data-lucide="arrow-right" class="h-4 w-4"></i>
                  </a>
                </div>
                """

            tiers_html += f"""
            <div class="flex flex-col justify-between rounded-3xl bg-white p-7 sm:p-9 {pop_border} transition-all duration-300 hover:shadow-2xl">
              <div>
                {pop_badge}
                <div class="flex items-center justify-between">
                  <span class="rounded-full bg-brandSoft px-3 py-1 text-xs font-bold uppercase tracking-wide text-brand">{t["badge"]}</span>
                  <span class="inline-flex items-center gap-1 text-xs font-semibold text-accent">Instant Setup</span>
                </div>

                <h3 class="mt-4 font-display text-2xl font-bold text-navy">{t["name"]}</h3>
                <p class="mt-2 text-xs leading-relaxed text-gray-500">{t["desc"]}</p>

                {price_elements}

                <ul class="mt-6 space-y-3.5">
                  {features_li}
                </ul>
              </div>

              <div class="mt-8 pt-4 border-t border-gray-100">
                {cta_buttons}
                <p class="mt-2.5 text-center text-[11px] text-gray-400">Instant Automated Provisioning · Guaranteed Uptime</p>
              </div>
            </div>
            """

        tiers_html += "</div>"

        # Lifetime Note if applicable
        if terms and "lifetime" in terms and LIFETIME_NOTE:
            tiers_html += f'<p class="mt-6 text-center text-xs text-gray-500 hidden" data-lifetime-note>{LIFETIME_NOTE}</p>'

    # Dedicated Comparison Matrix Section for Shared Hosting
    matrix_section_html = ""
    if p["slug"] == "shared-hosting":
        matrix_section_html = """
  <!-- ============ 03-MATRIX · QUICK COMPARISON MATRIX ============ -->
  <section id="comparison-matrix" class="py-20 lg:py-28 bg-mist/60 border-b border-gray-200">
    <div class="lb-shell max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="lb-eyebrow">Plan Specification Breakdown</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Quick Comparison Matrix
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Compare specifications, compute power, and pricing across all shared hosting tiers. Switch between recurring subscriptions and lifetime packages below.
        </p>

        <!-- Toggle Switcher -->
        <div class="mt-8 flex justify-center">
          <div role="group" aria-label="Comparison Table Switcher" class="inline-flex rounded-2xl border border-gray-200 bg-white p-1.5 shadow-sm">
            <button type="button" data-matrix-toggle="recurring" aria-pressed="true" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 bg-brand text-white shadow-md shadow-brand/20">
              Recurring Subscriptions (Monthly &amp; Annual)
            </button>
            <button type="button" data-matrix-toggle="lifetime" aria-pressed="false" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 text-gray-600 hover:text-navy">
              Lifetime Plans (Pay Once · No Renewals)
            </button>
          </div>
        </div>
      </div>

      <!-- Panel 1: Subscription Plans Table -->
      <div data-matrix-panel="recurring" class="transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Recurring Subscription Plans</h3>
              <p class="text-xs text-gray-500">Billed monthly or annually with ~17% annual discount included.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              Save ~17% on Annual Billing
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Plan Name</th>
                <th class="py-4 px-5 font-bold">Storage</th>
                <th class="py-4 px-5 font-bold">vCPU / RAM</th>
                <th class="py-4 px-5 font-bold">Monthly Price</th>
                <th class="py-4 px-5 font-bold">12-Mo Base</th>
                <th class="py-4 px-5 font-bold">Discounted Year</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Personal NVMe</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Unlimited Websites · LiteSpeed Cache</span>
                </td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">10 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$2.99 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$35.88</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$29.78 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=27&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Personal</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Professional NVMe</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Popular</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">High Performance · 2x RAM Allocation</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">30 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$4.99 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$59.88</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$49.70 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=28&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Professional</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Turbo NVMe</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Maximum Capacity · Imunify360 Security</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$7.99 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$95.88</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$79.58 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=29&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Turbo</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Panel 2: Lifetime Plans Table -->
      <div data-matrix-panel="lifetime" class="hidden transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Lifetime Plans (One-Time Purchase)</h3>
              <p class="text-xs text-gray-500">Pay once and keep your hosting account permanently active. Zero monthly or annual renewal fees.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              Pay Once · Host Forever
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Lifetime Plan</th>
                <th class="py-4 px-5 font-bold">Storage</th>
                <th class="py-4 px-5 font-bold">vCPU / RAM</th>
                <th class="py-4 px-5 font-bold">One-Time Price</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Personal NVMe - Lifetime</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Permanent Single Payment · No Renewals</span>
                </td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">10 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$129.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=31" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Personal Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Professional NVMe - Lifetime</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Popular</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">30 GB NVMe · Permanent Business Hosting</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">30 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$229.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=32" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Professional Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Turbo NVMe - Lifetime</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Unlimited NVMe · Permanent VIP Tier</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$399.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=30" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Turbo Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Public Catalog Footer Strip -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
            <i data-lucide="shopping-bag" class="h-5 w-5"></i>
          </span>
          <div>
            <h4 class="text-sm font-bold text-navy">Looking for custom addons or domain registration?</h4>
            <p class="text-xs text-gray-500">Explore the complete storefront catalog with instant ordering and configuration.</p>
          </div>
        </div>
        <a href="https://dashboard.licenbase.com/store/shared-hosting" class="inline-flex items-center gap-2 rounded-xl bg-mist px-4 py-2.5 text-xs font-bold text-navy border border-gray-200 transition hover:bg-white hover:text-brand hover:border-brand/40 shadow-xs">
          <span>Open Shared Hosting Store</span>
          <i data-lucide="external-link" class="h-3.5 w-3.5"></i>
        </a>
      </div>
    </div>
  </section>
"""
    elif p["slug"] == "reseller-hosting":
        matrix_section_html = """
  <!-- ============ 03-MATRIX · QUICK COMPARISON MATRIX ============ -->
  <section id="comparison-matrix" class="py-20 lg:py-28 bg-mist/60 border-b border-gray-200">
    <div class="lb-shell max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="lb-eyebrow">Agency Specification Breakdown</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Quick Comparison Matrix
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Compare cPanel account quotas, NVMe disk allocations, compute power, and pricing across all reseller tiers. Switch between recurring subscriptions and lifetime packages below.
        </p>

        <!-- Toggle Switcher -->
        <div class="mt-8 flex justify-center">
          <div role="group" aria-label="Comparison Table Switcher" class="inline-flex rounded-2xl border border-gray-200 bg-white p-1.5 shadow-sm">
            <button type="button" data-matrix-toggle="recurring" aria-pressed="true" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 bg-brand text-white shadow-md shadow-brand/20">
              Recurring Subscriptions (Monthly &amp; Annual)
            </button>
            <button type="button" data-matrix-toggle="lifetime" aria-pressed="false" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 text-gray-600 hover:text-navy">
              Lifetime Plans (Pay Once · No Renewals)
            </button>
          </div>
        </div>
      </div>

      <!-- Panel 1: Subscription Plans Table -->
      <div data-matrix-panel="recurring" class="transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Recurring Agency Subscriptions</h3>
              <p class="text-xs text-gray-500">Billed monthly or annually with 5 Months Free (~42% discount) on yearly terms.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              5 Months Free on Annual Billing
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Plan Name</th>
                <th class="py-4 px-5 font-bold">Accounts</th>
                <th class="py-4 px-5 font-bold">NVMe Disk</th>
                <th class="py-4 px-5 font-bold">vCPU / RAM</th>
                <th class="py-4 px-5 font-bold">Monthly Price</th>
                <th class="py-4 px-5 font-bold">12-Mo Base</th>
                <th class="py-4 px-5 font-bold">Yearly (5 Mo Free)</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Bronze Reseller</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">20 cPanel Accounts · WHM Control</span>
                </td>
                <td class="py-5 px-5 font-semibold text-navy whitespace-nowrap">20 Accounts</td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">20 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$28.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$336.00</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$196.00 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=33&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Bronze</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Silver Reseller</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Popular</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">50 cPanel Accounts · Unlimited NVMe</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">50 Accounts</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$65.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$780.00</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$455.00 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=34&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Silver</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Gold Enterprise Reseller</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">100 cPanel Accounts · Master Fleet Scale</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">100 Accounts</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$95.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-5 line-through text-gray-400 whitespace-nowrap">$1,140.00</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$665.00 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=35&billingcycle=monthly" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Gold Enterprise</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Panel 2: Lifetime Plans Table -->
      <div data-matrix-panel="lifetime" class="hidden transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Lifetime Reseller Plans (One-Time Purchase)</h3>
              <p class="text-xs text-gray-500">Pay once and keep your WHM reseller account permanently active. Lock in 100% agency hosting margins.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              Pay Once · Host Clients Forever
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Lifetime Plan</th>
                <th class="py-4 px-5 font-bold">Accounts</th>
                <th class="py-4 px-5 font-bold">NVMe Disk</th>
                <th class="py-4 px-5 font-bold">vCPU / RAM</th>
                <th class="py-4 px-5 font-bold">One-Time Price</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Bronze Reseller - Lifetime</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Permanent WHM Agency Account · Zero Renewals</span>
                </td>
                <td class="py-5 px-5 font-semibold text-navy whitespace-nowrap">20 Accounts</td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">20 GB NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$360.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=36" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Bronze Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Silver Reseller - Lifetime</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Popular</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">50 Accounts · Unlimited NVMe · Permanent Agency Pick</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">50 Accounts</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$665.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=37" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Silver Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Gold Enterprise Reseller - Lifetime</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">100 Accounts · Unlimited NVMe · Permanent Enterprise Fleet</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">100 Accounts</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited NVMe</td>
                <td class="py-5 px-5 whitespace-nowrap">2 vCPU / 2 GB</td>
                <td class="py-5 px-5 font-extrabold text-navy text-lg whitespace-nowrap">$980.00 <span class="text-xs font-normal text-gray-500">USD</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=38" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Gold Enterprise Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Public Catalog Footer Strip -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
            <i data-lucide="shopping-bag" class="h-5 w-5"></i>
          </span>
          <div>
            <h4 class="text-sm font-bold text-navy">Looking for custom WHM allocations or private IP blocks?</h4>
            <p class="text-xs text-gray-500">Explore the complete storefront catalog with instant ordering and configuration.</p>
          </div>
        </div>
        <a href="https://dashboard.licenbase.com/store/reseller-hosting" class="inline-flex items-center gap-2 rounded-xl bg-mist px-4 py-2.5 text-xs font-bold text-navy border border-gray-200 transition hover:bg-white hover:text-brand hover:border-brand/40 shadow-xs">
          <span>Open Reseller Hosting Store</span>
          <i data-lucide="external-link" class="h-3.5 w-3.5"></i>
        </a>
      </div>
    </div>
  </section>
"""
    elif p["slug"] == "n8n-hosting":
        matrix_section_html = """
  <!-- ============ 03-MATRIX · QUICK COMPARISON MATRIX ============ -->
  <section id="comparison-matrix" class="py-20 lg:py-28 bg-mist/60 border-b border-gray-200">
    <div class="lb-shell max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="lb-eyebrow">Workflow Automation Breakdown</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Quick Comparison Matrix
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Compare execution power, database architecture, SLA support, and pricing across all four n8n hosting packages. Switch between recurring subscriptions and the lifetime package below.
        </p>

        <!-- Toggle Switcher -->
        <div class="mt-8 flex justify-center">
          <div role="group" aria-label="Comparison Table Switcher" class="inline-flex rounded-2xl border border-gray-200 bg-white p-1.5 shadow-sm">
            <button type="button" data-matrix-toggle="recurring" aria-pressed="true" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 bg-brand text-white shadow-md shadow-brand/20">
              Recurring Subscriptions (Monthly · Annual · 2-Year)
            </button>
            <button type="button" data-matrix-toggle="lifetime" aria-pressed="false" class="rounded-xl px-5 py-2.5 text-xs sm:text-sm font-bold transition-all duration-200 text-gray-600 hover:text-navy">
              Lifetime Plan (Pay Once · Automate Forever)
            </button>
          </div>
        </div>
      </div>

      <!-- Panel 1: Subscription Plans Table -->
      <div data-matrix-panel="recurring" class="transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Recurring Automation Subscriptions</h3>
              <p class="text-xs text-gray-500">Flexible monthly, annual, and 2-year billing with price lock guarantees.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              Save up to $18/yr on Multi-Term Plans
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Plan Name</th>
                <th class="py-4 px-5 font-bold">Billing Cycle</th>
                <th class="py-4 px-5 font-bold">Workflows &amp; Runs</th>
                <th class="py-4 px-5 font-bold">Storage &amp; DB</th>
                <th class="py-4 px-5 font-bold">SLA &amp; Support</th>
                <th class="py-4 px-5 font-bold">Price</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <!-- Starter -->
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Starter</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Great for Getting Started</span>
                </td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">Monthly</td>
                <td class="py-5 px-5 whitespace-nowrap font-medium text-navy">Unlimited</td>
                <td class="py-5 px-5 whitespace-nowrap">Unlimited NVMe · Postgres</td>
                <td class="py-5 px-5 whitespace-nowrap">99.99% SLA · 24/7 Chat</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$9.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=39" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Starter</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <!-- Professional -->
              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Professional</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Popular</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">Best Value for Teams · Free Upgrades</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Annually <span class="block text-[11px] font-medium text-emerald-600">$7.50/mo equiv.</span></td>
                <td class="py-5 px-5 whitespace-nowrap font-bold text-navy">Unlimited</td>
                <td class="py-5 px-5 whitespace-nowrap">Unlimited NVMe · Postgres</td>
                <td class="py-5 px-5 whitespace-nowrap">Priority Support · Advanced Monitoring</td>
                <td class="py-5 px-5 font-bold text-accentDeep whitespace-nowrap">$90.00 <span class="text-xs font-normal text-gray-500">/ yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=40" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Professional</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>

              <!-- Growth -->
              <tr class="hover:bg-mist/30 transition-colors">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold">Growth</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-400 mt-0.5">Dedicated Performance · 2-Yr Price Lock</span>
                </td>
                <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">Every 2 Years <span class="block text-[11px] font-medium text-brand">$7.50/mo equiv.</span></td>
                <td class="py-5 px-5 whitespace-nowrap font-medium text-navy">Unlimited</td>
                <td class="py-5 px-5 whitespace-nowrap">Unlimited NVMe · Postgres</td>
                <td class="py-5 px-5 whitespace-nowrap">Priority Support · Advanced Monitoring</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">$180.00 <span class="text-xs font-normal text-gray-500">/ 2yr</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=41" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                    <span>Order Growth</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Panel 2: Lifetime Plan Table -->
      <div data-matrix-panel="lifetime" class="hidden transition-all duration-300">
        <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
          <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
            <div>
              <h3 class="font-display text-base font-bold text-navy">Lifetime Plan (One-Time Purchase)</h3>
              <p class="text-xs text-gray-500">Pay once, automate forever. Zero renewal bills, lifetime updates, and priority support.</p>
            </div>
            <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
              Pay Once, Automate Forever · Zero Recurring Fees
            </span>
          </div>

          <table class="w-full text-left text-sm border-collapse">
            <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
              <tr>
                <th class="py-4 px-6 font-bold">Lifetime Plan</th>
                <th class="py-4 px-5 font-bold">Billing Term</th>
                <th class="py-4 px-5 font-bold">Workflows &amp; Runs</th>
                <th class="py-4 px-5 font-bold">Updates &amp; SLA</th>
                <th class="py-4 px-5 font-bold">Support</th>
                <th class="py-4 px-5 font-bold">One-Time Price</th>
                <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-600">
              <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
                <td class="py-5 px-6 font-semibold text-navy">
                  <div class="flex items-center gap-2">
                    <span class="text-base font-bold text-navy">Lifetime</span>
                    <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Best Deal</span>
                  </div>
                  <span class="block text-xs font-normal text-gray-500 mt-0.5">Pay Once, Automate Forever · Unlimited Everything</span>
                </td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">One-Time Purchase</td>
                <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">Unlimited Everything</td>
                <td class="py-5 px-5 whitespace-nowrap">Lifetime Updates · 99.99% SLA</td>
                <td class="py-5 px-5 whitespace-nowrap font-medium text-navy">Priority Support</td>
                <td class="py-5 px-5 font-extrabold text-navy whitespace-nowrap text-lg">$420.00 <span class="text-xs font-normal text-gray-500 block">no renewals</span></td>
                <td class="py-5 px-6 text-right whitespace-nowrap">
                  <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=42" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                    <span>Order Lifetime</span>
                    <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Public Catalog Footer Strip -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
            <i data-lucide="workflow" class="h-5 w-5"></i>
          </span>
          <div>
            <h4 class="text-sm font-bold text-navy">Looking for custom worker nodes or private multi-tenant clusters?</h4>
            <p class="text-xs text-gray-500">Explore the complete n8n hosting catalog with instant automated provisioning.</p>
          </div>
        </div>
        <a href="https://dashboard.licenbase.com/store/n8n-hosting" class="inline-flex items-center gap-2 rounded-xl bg-mist px-4 py-2.5 text-xs font-bold text-navy border border-gray-200 transition hover:bg-white hover:text-brand hover:border-brand/40 shadow-xs">
          <span>Open n8n Hosting Store</span>
          <i data-lucide="external-link" class="h-3.5 w-3.5"></i>
        </a>
      </div>
    </div>
  </section>
"""
    elif p["slug"] == "openclaw-hosting":
        matrix_section_html = """
  <!-- ============ 03-MATRIX · QUICK COMPARISON MATRIX ============ -->
  <section id="comparison-matrix" class="py-20 lg:py-28 bg-mist/60 border-b border-gray-200">
    <div class="lb-shell max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="lb-eyebrow">AI Agent Platform Breakdown</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Quick Comparison Matrix
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Compare specifications, model integrations, channel access, and pricing between monthly subscription and lifetime packages.
        </p>
      </div>

      <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
        <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
          <div>
            <h3 class="font-display text-base font-bold text-navy">OpenClaw Cloud Packages</h3>
            <p class="text-xs text-gray-500">Transparent pricing with zero per-message fees or token surcharges.</p>
          </div>
          <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
            Instant Deployment &amp; Free White-Glove Setup
          </span>
        </div>

        <table class="w-full text-left text-sm border-collapse">
          <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
            <tr>
              <th class="py-4 px-6 font-bold">Package</th>
              <th class="py-4 px-5 font-bold">Billing Cycle</th>
              <th class="py-4 px-5 font-bold">Supported Models</th>
              <th class="py-4 px-5 font-bold">Support &amp; Updates</th>
              <th class="py-4 px-5 font-bold">Price</th>
              <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 text-gray-600">
            <tr class="hover:bg-mist/30 transition-colors">
              <td class="py-5 px-6 font-semibold text-navy">
                <span class="text-base font-bold">OpenClaw Hosting</span>
                <span class="block text-xs font-normal text-gray-400 mt-0.5">Monthly Cloud Subscription</span>
              </td>
              <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">Monthly Recurring</td>
              <td class="py-5 px-5 whitespace-nowrap">GPT-4o, Claude, Llama, Kimi</td>
              <td class="py-5 px-5 whitespace-nowrap">Standard Support · Free Setup</td>
              <td class="py-5 px-5 font-bold text-navy whitespace-nowrap text-base">$14.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
              <td class="py-5 px-6 text-right whitespace-nowrap">
                <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=43" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                  <span>Order Monthly</span>
                  <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                </a>
              </td>
            </tr>

            <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
              <td class="py-5 px-6 font-semibold text-navy">
                <div class="flex items-center gap-2">
                  <span class="text-base font-bold text-navy">OpenClaw Hosting Lifetime</span>
                  <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Best Deal</span>
                </div>
                <span class="block text-xs font-normal text-gray-500 mt-0.5">Pay Once, Run Forever · Zero Renewal Fees</span>
              </td>
              <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">One-Time Payment</td>
              <td class="py-5 px-5 whitespace-nowrap font-medium text-navy">GPT-4o, Claude, Llama, Kimi</td>
              <td class="py-5 px-5 whitespace-nowrap font-semibold text-accentDeep">Lifetime Priority Support &amp; Updates</td>
              <td class="py-5 px-5 font-extrabold text-navy whitespace-nowrap text-lg">$380.00 <span class="text-xs font-normal text-gray-500 block">one-time</span></td>
              <td class="py-5 px-6 text-right whitespace-nowrap">
                <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=44" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                  <span>Order Lifetime</span>
                  <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Public Catalog Footer Strip -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
            <i data-lucide="bot" class="h-5 w-5"></i>
          </span>
          <div>
            <h4 class="text-sm font-bold text-navy">Need custom bot skills or multi-agent orchestration?</h4>
            <p class="text-xs text-gray-500">Explore the complete OpenClaw hosting storefront with instant automated provisioning.</p>
          </div>
        </div>
        <a href="https://dashboard.licenbase.com/store/openclaw-hosting" class="inline-flex items-center gap-2 rounded-xl bg-mist px-4 py-2.5 text-xs font-bold text-navy border border-gray-200 transition hover:bg-white hover:text-brand hover:border-brand/40 shadow-xs">
          <span>Open OpenClaw Store</span>
          <i data-lucide="external-link" class="h-3.5 w-3.5"></i>
        </a>
      </div>
    </div>
  </section>
"""
    elif p["slug"] == "hermes-agent-hosting":
        matrix_section_html = """
  <!-- ============ 03-MATRIX · QUICK COMPARISON MATRIX ============ -->
  <section id="comparison-matrix" class="py-20 lg:py-28 bg-mist/60 border-b border-gray-200">
    <div class="lb-shell max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="lb-eyebrow">Autonomous AI Agent Platform Breakdown</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Quick Comparison Matrix
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Compare specifications, deployment controls, subdomain access, and pricing between monthly subscription and lifetime packages.
        </p>
      </div>

      <div class="overflow-x-auto rounded-3xl border border-gray-200 bg-white shadow-md">
        <div class="px-6 py-4 bg-mist/50 border-b border-gray-200 flex flex-wrap items-center justify-between gap-2">
          <div>
            <h3 class="font-display text-base font-bold text-navy">Hermes Agent Cloud Packages</h3>
            <p class="text-xs text-gray-500">Transparent pricing with zero per-message fees or token surcharges.</p>
          </div>
          <span class="rounded-full bg-emerald-50 border border-emerald-200 px-3 py-1 text-xs font-bold text-accentDeep">
            Instant Deployment &amp; Private SSL Subdomain
          </span>
        </div>

        <table class="w-full text-left text-sm border-collapse">
          <thead class="bg-gray-50/80 border-b border-gray-200 text-xs uppercase tracking-wider text-gray-700">
            <tr>
              <th class="py-4 px-6 font-bold">Package</th>
              <th class="py-4 px-5 font-bold">Billing Cycle</th>
              <th class="py-4 px-5 font-bold">LLM Model Keys</th>
              <th class="py-4 px-5 font-bold">Price</th>
              <th class="py-4 px-6 font-bold text-right">Direct Cart Link</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 text-gray-600">
            <tr class="hover:bg-mist/30 transition-colors">
              <td class="py-5 px-6 font-semibold text-navy">
                <span class="text-base font-bold">Hermes Agent</span>
                <span class="block text-xs font-normal text-gray-400 mt-0.5">Monthly Cloud Subscription</span>
              </td>
              <td class="py-5 px-5 font-medium text-navy whitespace-nowrap">Monthly Recurring</td>
              <td class="py-5 px-5 whitespace-nowrap">Bring Your Own Key (BYOK)</td>
              <td class="py-5 px-5 font-bold text-navy whitespace-nowrap text-base">$14.00 <span class="text-xs font-normal text-gray-500">/ mo</span></td>
              <td class="py-5 px-6 text-right whitespace-nowrap">
                <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=45" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-sm inline-flex items-center gap-1.5">
                  <span>Order Monthly</span>
                  <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                </a>
              </td>
            </tr>

            <tr class="hover:bg-brandSoft/20 bg-brandSoft/10 transition-colors border-l-4 border-l-brand">
              <td class="py-5 px-6 font-semibold text-navy">
                <div class="flex items-center gap-2">
                  <span class="text-base font-bold text-navy">Hermes Agent Lifetime</span>
                  <span class="rounded-full bg-brand px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white shadow-xs">Best Deal</span>
                </div>
                <span class="block text-xs font-normal text-gray-500 mt-0.5">Pay Once, Run Forever · Zero Renewal Fees</span>
              </td>
              <td class="py-5 px-5 font-bold text-navy whitespace-nowrap">One-Time Payment</td>
              <td class="py-5 px-5 whitespace-nowrap font-medium text-navy">Bring Your Own Key (BYOK)</td>
              <td class="py-5 px-5 font-extrabold text-navy whitespace-nowrap text-lg">$380.00 <span class="text-xs font-normal text-gray-500 block">one-time</span></td>
              <td class="py-5 px-6 text-right whitespace-nowrap">
                <a href="https://dashboard.licenbase.com/cart.php?a=add&pid=46" class="lb-btn lb-btn--primary py-2 px-4 text-xs font-bold shadow-md shadow-brand/20 inline-flex items-center gap-1.5">
                  <span>Order Lifetime</span>
                  <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Public Catalog Footer Strip -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
            <i data-lucide="brain" class="h-5 w-5"></i>
          </span>
          <div>
            <h4 class="text-sm font-bold text-navy">Need dedicated agent clusters or custom vector stores?</h4>
            <p class="text-xs text-gray-500">Explore the complete Hermes Agent hosting storefront with instant automated provisioning.</p>
          </div>
        </div>
        <a href="https://dashboard.licenbase.com/store/hermes-agent" class="inline-flex items-center gap-2 rounded-xl bg-mist px-4 py-2.5 text-xs font-bold text-navy border border-gray-200 transition hover:bg-white hover:text-brand hover:border-brand/40 shadow-xs">
          <span>Open Hermes Agent Store</span>
          <i data-lucide="external-link" class="h-3.5 w-3.5"></i>
        </a>
      </div>
    </div>
  </section>
"""

    # FAQs HTML
    faqs_html = ""
    for idx, faq in enumerate(p["faqs"], 1):
        is_first = idx == 1
        active_cls = " lb-faq-active" if is_first else ""
        open_cls = " lb-faq-open" if is_first else ""
        expanded_val = "true" if is_first else "false"

        faqs_html += f"""
          <div class="lb-faq{active_cls}">
            <button id="faq-question-{idx}" class="lb-faq-btn" type="button" aria-expanded="{expanded_val}" aria-controls="faq-answer-{idx}">
              <span class="lb-faq-icon-wrap"><i data-lucide="help-circle" class="h-5 w-5" aria-hidden="true"></i></span>
              <span class="lb-faq-question">{faq["q"]}</span>
              <span class="lb-faq-chevron" aria-hidden="true"><i data-lucide="chevron-down" class="lb-faq-icon h-5 w-5"></i></span>
            </button>
            <div id="faq-answer-{idx}" class="lb-faq-panel{open_cls}" role="region" aria-labelledby="faq-question-{idx}">
              <div class="lb-faq-answer-wrap">
                <p class="lb-faq-answer">{faq["a"]}</p>
              </div>
            </div>
          </div>
        """

    # Related Products HTML
    icon_map = {
        "/cpanel-license": "cpanel.svg",
        "/litespeed-license": "litespeed.svg",
        "/plesk-license": "plesk.svg",
        "/whmcs-license": "whmcs.png",
        "/cloudlinux-license": "cloudlinux.png",
        "/virtualizor-license": "virtualizor.png",
        "/sitepad-license": "sitepad.png",
        "/whmreseller-license": "whmreseller.png",
        "/softaculous-license": "softaculous.png",
        "/jetbackup-license": "jetbackup.png",
        "/imunify360-license": "imunify360.png",
        "/webuzo-license": "webuzo.png",
        "/wp-squared-license": "wp-squared.svg"
    }
    related_html = ""
    for rel in p["related"]:
        rel_icon_name = icon_map.get(rel['url'])
        if rel_icon_name:
            icon_markup = f'<img src="assets/img/icons/{rel_icon_name}" alt="{rel["title"]}" class="h-7 w-7 object-contain" width="28" height="28" loading="lazy" decoding="async" />'
        else:
            icon_markup = f'<i data-lucide="{rel.get("icon", "server")}" class="h-6 w-6 text-brand"></i>'

        related_html += f"""
        <div class="group relative flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-brand/40 hover:shadow-xl">
          <div>
            <div class="flex items-center justify-between">
              <span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-110">
                {icon_markup}
              </span>
              <span class="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-bold text-accentDeep">{rel['price']}</span>
            </div>
            <h3 class="mt-4 font-display text-lg font-bold text-navy group-hover:text-brand transition-colors">{rel['title']}</h3>
            <p class="mt-2 text-xs leading-relaxed text-gray-500">{rel['desc']}</p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-500">Infrastructure &amp; License</span>
            <a href="{rel['url']}" class="inline-flex items-center gap-1 text-xs font-bold text-brand hover:underline">
              View Details <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
            </a>
          </div>
        </div>
        """

    # Related Guides HTML
    guides = sorted(_BLOG_POSTS, key=lambda b: p["slug"] not in [s for s, _ in b["related"]])
    articles_html = ""
    for art in guides[:3]:
        mins = max(1, round(len(_re.sub(r"<[^>]+>", " ", art["body"]).split()) / 200))
        articles_html += f"""
        <a href="/blog/{art['slug']}" class="group flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:border-brand/30 hover:shadow-lg">
          <div>
            <img src="/assets/img/blog/{art['slug']}-thumb.webp" alt="" width="640" height="336" class="mb-4 w-full rounded-xl border border-gray-100" loading="lazy" decoding="async" />
            <div class="flex items-center justify-between text-xs">
              <span class="rounded-md bg-mist px-2.5 py-1 font-bold text-brand uppercase tracking-wider">{art['category']}</span>
              <span class="text-gray-400 font-medium">{mins} min read</span>
            </div>
            <h3 class="mt-3 font-display text-base font-bold text-navy group-hover:text-brand transition-colors">{_html.escape(art['title'])}</h3>
            <p class="mt-2 text-xs leading-relaxed text-gray-500">{art['excerpt']}</p>
          </div>
          <div class="mt-5 pt-3 border-t border-gray-100">
            <span class="inline-flex items-center gap-1 text-xs font-bold text-brand group-hover:underline">
              Read Guide <i data-lucide="arrow-up-right" class="h-3.5 w-3.5"></i>
            </span>
          </div>
        </a>
        """

    specs_pills = "".join([
        f'<span class="inline-flex items-center gap-1.5 rounded-full bg-white px-3 py-1.5 text-xs font-semibold text-navy border border-gray-200 shadow-sm"><i data-lucide="check" class="h-3.5 w-3.5 text-accent"></i> {spec}</span>'
        for spec in p["specs"]
    ])

    url = "https://licenbase.com/" + p["slug"]
    offers = []
    for plan in plans:
        for term, price in plan["prices"].items():
            offers.append({
                "@type": "Offer",
                "name": f"{plan['name']} ({term.title()})",
                "price": f"{price:.2f}",
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "url": url,
                "seller": {"@type": "Organization", "name": "LicenBase"},
                **OFFER_EXTRA
            })

    ld = [
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": p["name"],
            "description": _html.unescape(p["seo_desc"]),
            "image": f"https://licenbase.com/assets/img/og/{p['slug']}.png",
            "url": url,
            "brand": {"@type": "Brand", "name": "LicenBase"},
            "offers": offers
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://licenbase.com/"},
                {"@type": "ListItem", "position": 2, "name": "Hosting & Infrastructure", "item": "https://licenbase.com/products"},
                {"@type": "ListItem", "position": 3, "name": p["name"], "item": url},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": _html.unescape(f["q"]), "acceptedAnswer": {"@type": "Answer", "text": _html.unescape(f["a"])}}
                for f in p["faqs"]
            ],
        },
    ]
    ld_json = "\n".join(f'  <script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in ld)

    # Most Popular package card for the Hero Section
    pop = next((t for t in plans if t.get("popular")), plans[0] if plans else None)
    if pop:
        pop_specs_html = "".join([
            f'<li class="flex items-center gap-2.5 text-xs sm:text-sm text-gray-700 font-medium">'
            f'<i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent" aria-hidden="true"></i>'
            f'<span>{feat}</span></li>'
            for feat in pop.get("specs", [])[:5]
        ])
        price_val = pop.get("price") or pop["prices"].get("monthly") or list(pop["prices"].values())[0]
        price_period = pop.get("period_label") or ("per month" if "monthly" in pop.get("prices", {}) else ("per year" if "yearly" in pop.get("prices", {}) else "starting price"))
        if price_period == "yr":
            price_period = "year"
        elif price_period == "mo":
            price_period = "month"
        pop_url = pop.get("url") or pop.get("urls", {}).get("monthly") or list(pop.get("urls", {}).values())[0]
        hero_popular_card = f"""
        <!-- Visual Hero Card: Most Popular Package -->
        <div class="relative mx-auto w-full max-w-lg">
          <div class="absolute -inset-1 rounded-3xl bg-gradient-to-r from-brand to-accent opacity-20 blur-xl"></div>
          <div class="relative rounded-3xl border-2 border-brand/30 bg-white p-7 sm:p-9 shadow-2xl transition-all duration-300 hover:border-brand/60">
            <!-- Header Badges -->
            <div class="flex items-center justify-between border-b border-gray-100 pb-5">
              <span class="inline-flex items-center gap-1.5 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">
                Most Popular Choice
              </span>
              <span class="inline-flex items-center gap-1 text-xs font-semibold text-accentDeep bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full">
                Instant Setup
              </span>
            </div>

            <!-- Plan Info -->
            <div class="mt-5">
              <div class="flex items-center gap-3">
                <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand shrink-0">
                  <i data-lucide="{p['icon']}" class="h-5 w-5"></i>
                </span>
                <div>
                  <h3 class="font-display text-2xl font-extrabold text-navy">{pop["name"]}</h3>
                  <span class="text-xs font-bold uppercase tracking-wide text-brand">{pop["badge"]}</span>
                </div>
              </div>
              <p class="mt-2 text-xs leading-relaxed text-gray-500">{pop["desc"]}</p>

              <!-- Price Box -->
              <div class="mt-4 flex items-baseline gap-1.5 border-y border-gray-100 py-3.5 bg-mist/60 -mx-7 px-7 sm:-mx-9 sm:px-9">
                <span class="font-display text-4xl sm:text-5xl font-extrabold tracking-tight text-navy">${price_val:,.2f}</span>
                <span class="text-xs sm:text-sm font-semibold text-gray-500">/{price_period}</span>
                <span class="ml-auto rounded-md bg-emerald-100 px-2 py-0.5 text-[11px] font-bold text-accentDeep">Best Value</span>
              </div>

              <!-- Feature Highlights -->
              <ul class="mt-4 space-y-2">
                {pop_specs_html}
              </ul>

              <!-- Order Button -->
              <div class="mt-6">
                <a href="{pop_url}" class="lb-btn lb-btn--primary w-full py-3.5 text-sm font-bold shadow-lg shadow-brand/25 flex items-center justify-center gap-2">
                  <span>Order {pop['name']}</span>
                  <i data-lucide="arrow-right" class="h-4 w-4"></i>
                </a>
                <p class="mt-2 text-center text-[11px] text-gray-400">Instant Automated Provisioning · 24/7 Support</p>
              </div>
            </div>

            <!-- Stats Bar -->
            <div class="mt-5 pt-4 border-t border-gray-100 grid grid-cols-2 gap-3 text-center text-xs">
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <p class="font-bold text-navy text-sm">60 Seconds</p>
                <p class="text-gray-500 text-[11px]">Average Setup Time</p>
              </div>
              <div class="rounded-xl bg-mist p-2.5 border border-gray-100">
                <p class="font-bold text-navy text-sm">99.99%</p>
                <p class="text-gray-500 text-[11px]">Hardware &amp; Network SLA</p>
              </div>
            </div>
          </div>
        </div>
        """
    else:
        hero_popular_card = ""

    # 03c Features Section
    features_section_html = ""
    if "features_grid" in p:
        fg = p["features_grid"]
        f_cards = []
        for card in fg.get("cards", []):
            f_cards.append(f"""
        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-200 hover:shadow-md hover:border-brand/40">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="{card.get('icon', 'check-circle')}" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">{card['title']}</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">{card['desc']}</p>
        </div>""")
        f_cards_joined = "".join(f_cards)
        features_section_html = f"""
  <!-- ============ 03c · FEATURES SECTION ============ -->
  <section class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">{fg.get('eyebrow', 'Product Features')}</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          {fg.get('title', 'Hosting Features')}
        </h2>
        <p class="mt-3 text-base text-gray-500">
          {fg.get('subtitle', '')}
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {f_cards_joined}
      </div>
    </div>
  </section>
"""

    # 04 Why Choose Us / Value Proposition
    if "why_choose" in p:
        wc = p["why_choose"]
        wc_cards = []
        for card in wc.get("cards", []):
            wc_cards.append(f"""
        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md hover:border-brand/30">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="{card.get('icon', 'check-circle')}" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">{card['title']}</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">{card['desc']}</p>
        </div>""")
        wc_cards_joined = "".join(wc_cards)
        why_choose_section_html = f"""
  <!-- ============ 04 · WHY CHOOSE US ============ -->
  <section class="py-16 lg:py-24 bg-mist border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">{wc.get('eyebrow', 'Enterprise Reliability')}</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          {wc.get('title', 'Why Choose LicenBase')}
        </h2>
        <p class="mt-3 text-base text-gray-500">
          {wc.get('subtitle', '')}
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {wc_cards_joined}
      </div>
    </div>
  </section>
"""
    else:
        why_choose_section_html = """
  <!-- ============ 04 · WHY CHOOSE US ============ -->
  <section class="py-16 lg:py-24 bg-mist border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Enterprise Reliability</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Why Hosting Providers &amp; Developers Choose LicenBase
        </h2>
        <p class="mt-3 text-base text-gray-500">
          We combine wholesale infrastructure pricing with enterprise-grade uptime, high-frequency NVMe hardware, and dedicated engineering support.
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="cpu" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">High-Frequency AMD EPYC &amp; NVMe</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Built on enterprise Gen4 NVMe storage in RAID-10 and high-frequency processors for blazing database queries and sub-second page loads.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="zap" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Instant Automated Provisioning</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Automated API provisioning spins up your server, generates credentials, and activates network routes immediately with zero manual wait time.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="shield-check" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Inline Automated DDoS Mitigation</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Multi-terabit automated scrubbing centers filter out malicious volumetric attacks in real-time, keeping your applications online.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="network" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Redundant 1 Gbps+ Network Uplinks</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Tier-1 transit providers and direct peering exchanges ensure minimal latency, zero packet loss, and maximum global reach.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="sliders" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">1-Click Control &amp; Rebuilds</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Easily reboot, reinstall operating systems, mount custom ISOs, and inspect live metrics directly from your LicenBase client dashboard.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="headset" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">24/7 Expert Systems Support</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Our experienced Linux systems administrators and network engineers are available around the clock via live chat and ticket desk.
          </p>
        </div>
      </div>
    </div>
  </section>
"""

    # 05 Deployment Steps
    if "steps" in p:
        steps_list = p["steps"]
    else:
        steps_list = [
            {"num": "1", "title": "Select Tier & Resources", "desc": "Pick your plan, choose your preferred billing cycle, and customize your OS or domain settings."},
            {"num": "2", "title": "Automated Provisioning", "desc": "Our cloud engine automatically partitions storage, configures IP routes, and prepares your credentials in seconds."},
            {"num": "3", "title": "Instant Access & Control", "desc": "Log in via SSH or web control panel to deploy your websites, APIs, automation workflows, or mail stacks."}
        ]
    steps_cards = []
    for st in steps_list:
        steps_cards.append(f"""
        <div class="relative rounded-2xl border border-gray-200 bg-mist p-6 text-center">
          <div class="mx-auto grid h-12 w-12 place-items-center rounded-full bg-brand text-lg font-bold text-white shadow-md shadow-brand/20">{st['num']}</div>
          <h3 class="mt-4 font-display text-base font-bold text-navy">{st['title']}</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            {st['desc']}
          </p>
        </div>""")
    steps_cards_joined = "".join(steps_cards)
    deployment_section_html = f"""
  <!-- ============ 05 · DEPLOYMENT WORKFLOW ============ -->
  <section id="deployment" class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Fast &amp; Seamless Deployment</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Simple 3-Step Setup Process
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Get your {p["name"]} infrastructure deployed and running in under 60 seconds.
        </p>
      </div>

      <!-- 3 Steps -->
      <div class="mt-12 grid gap-8 md:grid-cols-3">
        {steps_cards_joined}
      </div>
    </div>
  </section>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
{GTM_HEAD}  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["seo_title"]}</title>
  <meta name="description" content="{p["seo_desc"]}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://licenbase.com/{p["slug"]}" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="LicenBase" />
  <meta property="og:title" content="{p.get('og_title', p['seo_title'])}" />
  <meta property="og:description" content="{p["seo_desc"]}" />
  <meta property="og:url" content="https://licenbase.com/{p["slug"]}" />
  <meta property="og:image" content="https://licenbase.com/assets/img/og/{p["slug"]}.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="{p["name"]} from LicenBase" />
  <meta property="og:locale" content="en_US" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://licenbase.com/assets/img/og/{p["slug"]}.png" />
  <meta name="twitter:image:alt" content="{p["name"]} from LicenBase" />
  <meta name="twitter:title" content="{p.get('og_title', p['seo_title'])}" />
  <meta name="twitter:description" content="{p["seo_desc"]}" />

{ld_json}

  <!-- Favicon & PWA -->
  <link rel="icon" type="image/png" sizes="16x16" href="assets/img/favicon-16x16.png?v=2" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png?v=2" />
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png?v=2" />
  <link rel="icon" type="image/png" sizes="512x512" href="assets/img/favicon-512x512.png?v=2" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png?v=2" />
  <link rel="manifest" href="site.webmanifest" />
  <meta name="theme-color" content="#0a0f1d" />
  <link rel="icon" href="favicon.ico?v=2" sizes="any" />
  <link rel="shortcut icon" href="favicon.ico?v=2" />

  <!-- Fonts (Optimized Non-Blocking) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="font" type="font/woff2" href="https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2" crossorigin />
  <link rel="preload" as="font" type="font/woff2" href="https://fonts.gstatic.com/s/manrope/v20/xn7gYHE41ni1AdIRggexSg.woff2" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Manrope:wght@600..800&display=swap" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Manrope:wght@600..800&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Manrope:wght@600..800&display=swap" /></noscript>

  <!-- Swiper (Non-Blocking) -->
  <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" /></noscript>

  <!-- Precompiled Production CSS -->
  <link rel="stylesheet" href="assets/css/tailwind.min.css?v=1" />
  <link rel="stylesheet" href="assets/css/styles.min.css?v=2" />
</head>

<body class="bg-white font-sans text-navy antialiased">
{GTM_BODY}
  <!-- ============ 01 · TOP BAR & FIXED HEADER ============ -->
  <div class="lb-topbar">
    <div class="lb-shell">
      <header id="site-header" class="lb-header">
        <div class="lb-header-inner">
          <!-- Logo -->
          <a href="/" class="lb-logo" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-logo-img" width="250" height="100" fetchpriority="high" decoding="async" />
          </a>

          <!-- Desktop nav -->
          <nav class="lb-nav" aria-label="Main navigation">
            <!-- Licenses mega menu -->
            <div class="lb-drop lb-drop--mega">
              <button type="button" class="lb-nav-link" data-drop aria-haspopup="true" aria-expanded="false">
                Licenses <i data-lucide="chevron-down" class="h-3.5 w-3.5" aria-hidden="true"></i>
              </button>
              <div class="lb-drop-panel">
                <div class="lb-mega-tiles">
                  <a href="/cpanel-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cpanel.svg" alt="cPanel License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>cPanel License</span>
                  </a>
                  <a href="/litespeed-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>LiteSpeed License</span>
                  </a>
                  <a href="/plesk-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/plesk.svg" alt="Plesk License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>Plesk License</span>
                  </a>
                  <a href="/whmcs-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmcs.svg" alt="WHMCS License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>WHMCS License</span>
                  </a>
                  <a href="/cloudlinux-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cloudlinux.png" alt="CloudLinux License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>CloudLinux License</span>
                  </a>
                  <a href="/virtualizor-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/virtualizor.png" alt="Virtualizor License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>Virtualizor License</span>
                  </a>
                  <a href="/sitepad-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/sitepad.png" alt="SitePad License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>SitePad License</span>
                  </a>
                  <a href="/whmreseller-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmreseller.png" alt="WHMReseller License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>WHMReseller License</span>
                  </a>
                  <a href="/softaculous-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/softaculous.png" alt="Softaculous License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>Softaculous License</span>
                  </a>
                  <a href="/jetbackup-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/jetbackup.png" alt="JetBackup License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>JetBackup License</span>
                  </a>
                  <a href="/imunify360-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/imunify360.png" alt="Imunify360 License" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>Imunify360 License</span>
                  </a>
                  <a href="/webuzo-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/webuzo.png" alt="Webuzo Control Panel" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>Webuzo Control Panel</span>
                  </a>
                  <a href="/wp-squared-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/wp-squared.svg" alt="WP Squared" class="h-4 w-4 shrink-0 object-contain" width="16" height="16" loading="lazy" decoding="async" />
                    <span>WP Squared</span>
                  </a>
                </div>
              </div>
            </div>

            <!-- Hosting mega menu -->
            <div class="lb-drop lb-drop--mega">
              <button type="button" class="lb-nav-link" data-drop aria-haspopup="true" aria-expanded="false">
                Hosting <i data-lucide="chevron-down" class="h-3.5 w-3.5" aria-hidden="true"></i>
              </button>
              <div class="lb-drop-panel">
                <div class="lb-mega-tiles">
                  <a href="/shared-hosting" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="globe" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Shared Hosting<small class="block text-xs font-normal text-gray-500">Monthly, yearly &amp; lifetime</small></span>
                  </a>
                  <a href="/reseller-hosting" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="users" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Reseller Hosting<small class="block text-xs font-normal text-gray-500">Monthly, yearly &amp; lifetime</small></span>
                  </a>
                  <a href="/business-email" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="mail" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Business Email<small class="block text-xs font-normal text-gray-500">Email on your own domain</small></span>
                  </a>
                  <a href="/n8n-hosting" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="workflow" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>n8n Hosting<small class="block text-xs font-normal text-gray-500">Host your own n8n</small></span>
                  </a>
                  <a href="/openclaw-hosting" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="bot" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>OpenClaw Hosting<small class="block text-xs font-normal text-gray-500">Host your own OpenClaw</small></span>
                  </a>
                  <a href="/hermes-agent-hosting" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="bot" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Hermes Agent Hosting<small class="block text-xs font-normal text-gray-500">Host your own Hermes Agent</small></span>
                  </a>
                </div>
              </div>
            </div>

            <!-- VPS mega menu -->
            <div class="lb-drop lb-drop--mega">
              <button type="button" class="lb-nav-link" data-drop aria-haspopup="true" aria-expanded="false">
                VPS <i data-lucide="chevron-down" class="h-3.5 w-3.5" aria-hidden="true"></i>
              </button>
              <div class="lb-drop-panel">
                <div class="lb-mega-tiles">
                  <a href="/managed-vps" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="server" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Managed VPS<small class="block text-xs font-normal text-gray-500">cPanel &amp; license included</small></span>
                  </a>
                  <a href="/unmanaged-vps" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="terminal" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Unmanaged VPS<small class="block text-xs font-normal text-gray-500">Root access, no license</small></span>
                  </a>
                  <a href="/port-25-open-vps" class="lb-mega-tile flex items-center gap-2.5">
                    <i data-lucide="mail" class="h-4 w-4 shrink-0 text-brand" aria-hidden="true"></i>
                    <span>Port 25 Open VPS<small class="block text-xs font-normal text-gray-500">Outbound port 25 open</small></span>
                  </a>
                </div>
              </div>
            </div>

            <a href="/deals" class="lb-nav-link lb-nav-link--plain">Deals</a>
            <a href="/blog/" class="lb-nav-link lb-nav-link--plain">Blog</a>
            <a href="/tools/" class="lb-nav-link lb-nav-link--plain">Tools</a>
            <a href="/contact" class="lb-nav-link lb-nav-link--plain">Contact</a>
          </nav>

          <!-- Right actions -->
          <div class="lb-header-actions">
            <a href="/products" class="lb-header-signin">All Products</a>
            <a href="https://dashboard.licenbase.com/clientarea.php" class="lb-btn lb-btn--primary lb-header-cta">Dashboard</a>
            <button id="menu-open" type="button" class="lb-icon-btn lb-menu-toggle" aria-label="Open menu">
              <i data-lucide="menu" class="h-6 w-6"></i>
            </button>
          </div>
        </div>
      </header>
    </div>
  </div>

  <main id="main">

  <!-- ============ 02 · HERO SECTION ============ -->
  <section class="lb-hero relative overflow-hidden bg-mist border-b border-gray-200">
    <div class="lb-shell py-14 lg:py-20">
      <div class="grid items-center gap-12 lg:grid-cols-2">
        <!-- Copy -->
        <div class="space-y-6">
          <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-semibold text-gray-500">
            <a href="/" class="transition hover:text-brand">Home</a>
            <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
            <a href="/#categories" class="transition hover:text-brand">Hosting &amp; Servers</a>
            <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
            <span class="text-brand font-bold">{p["name"]}</span>
          </nav>

          <div class="inline-flex items-center gap-2.5 rounded-full bg-brandSoft px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-brand">
            <i data-lucide="{p['icon']}" class="h-4 w-4"></i>
            <span>{p["badge"]}</span>
          </div>

          <h1 class="font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl lg:text-5xl leading-[1.12]">
            {p["headline"]}<br />
            <span class="text-brand">{p["headline_sub"]}</span>
          </h1>

          <p class="text-base text-gray-600 leading-relaxed max-w-xl">
            {p["hero_desc"]}
          </p>

          <div class="flex flex-wrap gap-2 pt-2">
            {specs_pills}
          </div>

          <div class="flex flex-wrap items-center gap-4 pt-3">
            <a href="#pricing" class="lb-btn lb-btn--primary px-8 py-3.5 text-base shadow-lg shadow-brand/20">
              <i data-lucide="shopping-cart" class="h-4 w-4"></i>
              <span>View Pricing &amp; Plans</span>
            </a>
            <a href="#deployment" class="lb-btn lb-btn--secondary px-6 py-3.5 text-base">
              <i data-lucide="layers" class="h-4 w-4"></i>
              <span>Setup Process</span>
            </a>
          </div>

          <div class="flex items-center gap-6 pt-2 text-xs font-semibold text-gray-500">
            <span class="inline-flex items-center gap-1.5"><i data-lucide="shield-check" class="h-4 w-4 text-accent"></i> 100% Dedicated Resources</span>
            <span class="inline-flex items-center gap-1.5"><i data-lucide="zap" class="h-4 w-4 text-accent"></i> Instant Provisioning</span>
            <span class="inline-flex items-center gap-1.5"><i data-lucide="headset" class="h-4 w-4 text-accent"></i> 24/7 Expert Support</span>
          </div>
        </div>

        {hero_popular_card}
      </div>
    </div>
  </section>

  <!-- ============ 03 · PRICING SECTION ============ -->
  <section id="pricing" class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Affordable Transparent Pricing</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Choose Your {p["name"]} Plan
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Transparent pricing with zero hidden fees. Instant automated provisioning right after checkout.
        </p>
      </div>

      <!-- Pricing Cards Grid -->
      <div class="mt-12">
        {tiers_html}
      </div>

      <!-- Buying reassurance -->
      <div class="mt-12 grid gap-4 sm:grid-cols-3 max-w-4xl mx-auto">
        <div class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
          <i data-lucide="zap" class="h-5 w-5 text-accent"></i>
          <h3 class="mt-3 text-sm font-bold text-navy">Instant Automated Provisioning</h3>
          <p class="mt-1 text-xs leading-relaxed text-gray-500">Your server or hosting account is set up and delivered automatically as soon as payment clears.</p>
        </div>
        <div class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
          <i data-lucide="shield-check" class="h-5 w-5 text-accent"></i>
          <h3 class="mt-3 text-sm font-bold text-navy">99.99% Uptime Guarantee</h3>
          <p class="mt-1 text-xs leading-relaxed text-gray-500">Backed by enterprise Tier-3/4 data center facilities with redundant power, cooling, and network links.</p>
        </div>
        <div class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
          <i data-lucide="message-circle" class="h-5 w-5 text-accent"></i>
          <h3 class="mt-3 text-sm font-bold text-navy">Not sure which plan?</h3>
          <p class="mt-1 text-xs leading-relaxed text-gray-500">Tell us about your traffic and project needs and we will recommend the perfect tier. <a href="/contact" class="font-semibold text-brand hover:underline">Contact us</a>.</p>
        </div>
      </div>

      <!-- Legal Guarantee Banner -->
      <div class="mt-6 rounded-2xl border border-blue-100 bg-brandSoft/60 p-5 text-center text-xs text-gray-600 max-w-3xl mx-auto flex items-center justify-center gap-2">
        <i data-lucide="info" class="h-4 w-4 text-brand shrink-0"></i>
        <span><strong>Service Guarantee:</strong> All hosting accounts and cloud instances are deployed instantly. For pre-sales technical inquiries or custom enterprise configurations, <a href="/contact" class="font-semibold text-brand hover:underline">contact our engineering team</a>.</span>
      </div>
    </div>
  </section>

  {matrix_section_html}

  <!-- ============ 03b · SEO COPY ============ -->
  <section class="py-16 lg:py-20 bg-white border-b border-gray-200">
    <div class="lb-shell max-w-3xl mx-auto">
      <h2 class="font-display text-2xl font-extrabold tracking-tight text-navy sm:text-3xl">{p["seo_h2"]}</h2>
      <p class="mt-4 text-base leading-relaxed text-gray-600">{p["seo_p1"]}</p>
      <p class="mt-3 text-base leading-relaxed text-gray-600">{p["seo_p2"]}</p>
    </div>
  </section>

  {features_section_html}

  {why_choose_section_html}

  {deployment_section_html}

  <!-- ============ 06 · FAQ SECTION ============ -->
  <section id="faq" class="lb-faq-section bg-mist">
    <span class="lb-faq-dots lb-faq-dots--left" aria-hidden="true"></span>
    <span class="lb-faq-dots lb-faq-dots--right" aria-hidden="true"></span>
    <div class="lb-shell py-16 lg:py-24">
      <div class="mx-auto max-w-5xl">
        <div class="lb-faq-heading text-center">
          <span class="lb-faq-eyebrow">FAQ</span>
          <h2 class="mt-5 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
            Frequently Asked Questions
          </h2>
          <p class="mt-3 text-base text-gray-500">
            Quick answers about deploying and managing your {p["name"]} infrastructure.
          </p>
        </div>

        <div class="lb-stagger mt-10 space-y-3">
          {faqs_html}
        </div>

        <aside class="lb-faq-support" aria-label="Support options">
          <span class="lb-faq-support-icon"><i data-lucide="message-square-text" class="h-6 w-6" aria-hidden="true"></i></span>
          <div class="lb-faq-support-copy">
            <h3 class="font-display text-lg font-bold text-navy">Still have questions about {p["name"]}?</h3>
            <p class="mt-1 text-sm text-gray-500">Our senior server engineering support team is ready to assist you 24/7.</p>
          </div>
          <div class="lb-faq-support-actions">
            <a href="https://dashboard.licenbase.com/submitticket.php" class="lb-btn lb-btn--secondary">Open Ticket</a>
            <a href="#live-chat" data-open-chat class="lb-btn lb-btn--primary">Live Chat</a>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- ============ 07 · RELATED PRODUCTS & LICENSES ============ -->
  <section class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Complete Your Stack</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Complementary Products &amp; Licenses
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Pair your {p["name"]} deployment with industry-standard control panels, web servers, and security tools.
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {related_html}
      </div>
    </div>
  </section>

  <!-- ============ 08 · FROM THE BLOG ============ -->
  <section class="py-16 lg:py-24 bg-mist border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">From the Blog</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Helpful Guides &amp; Tutorials
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Practical setup guides, server optimization walkthroughs, and technical comparisons.
        </p>
      </div>

      <div class="mt-12 grid gap-6 md:grid-cols-3">
        {articles_html}
      </div>
      <p class="mt-8 text-center"><a href="/blog/" class="inline-flex items-center gap-1 text-sm font-bold text-brand hover:underline">View all articles <i data-lucide="arrow-right" class="h-4 w-4"></i></a></p>
    </div>
  </section>

  <!-- ============ 09 · CLOSING CONVERSION CARD ============ -->
  <section class="lb-conversion-section bg-white pb-16 pt-8 lg:pb-24 lg:pt-12">
    <div class="lb-shell">
      <div class="lb-conversion-card">
        <div class="lb-conversion-newsletter">
          <div class="lb-conversion-copy">
            <span class="lb-conversion-mail"><i data-lucide="zap" class="h-7 w-7"></i></span>
            <h2 class="lb-conversion-title">Ready to launch your <span>{p["name"]}?</span></h2>
            <p class="lb-conversion-description">
              Join thousands of web hosts, system administrators, and developers who trust LicenBase for high-performance servers and software licensing.
            </p>
            <div class="mt-8 flex flex-wrap items-center gap-4">
              <a href="#pricing" class="lb-btn lb-btn--primary px-8 py-3.5 text-base shadow-lg shadow-brand/30">Get Started Now</a>
              <a href="https://dashboard.licenbase.com/clientarea.php" class="lb-btn lb-btn--secondary px-6 py-3.5 text-base">Client Area</a>
            </div>
          </div>
          <div class="hidden lg:flex items-center justify-center">
            <div class="rounded-2xl border border-gray-200 bg-white/80 p-6 shadow-xl backdrop-blur-md max-w-xs text-center">
              <div class="mx-auto grid h-14 w-14 place-items-center rounded-2xl bg-emerald-50 text-accentDeep mb-3">
                <i data-lucide="shield-check" class="h-8 w-8"></i>
              </div>
              <p class="font-display font-bold text-navy">Guaranteed Performance</p>
              <p class="text-xs text-gray-500 mt-1">PCIe Gen4 NVMe, AMD EPYC processors, 99.99% network uptime SLA.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  </main>

  <!-- ============ 10 · FOOTER ============ -->
  <footer id="footer" class="border-t border-gray-200 bg-white pt-16 pb-12 text-sm text-gray-500">
    <div class="lb-shell">
      <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-5">
        <!-- Col 1: Brand -->
        <div class="lg:col-span-2 space-y-4">
          <a href="/" class="inline-block" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" width="250" height="100" loading="lazy" decoding="async" />
          </a>
          <p class="text-xs text-gray-500 leading-relaxed max-w-sm">
            LicenBase is the trusted software licensing platform for web hosts, enterprises, and digital agencies. Fast, automated, authentic license deployment.
          </p>
          <div class="flex items-center gap-2 text-xs font-semibold text-gray-600">
            <i data-lucide="mail" class="h-4 w-4 text-brand"></i>
            <a href="mailto:support@licenbase.com" class="transition hover:text-brand">support@licenbase.com</a>
          </div>
        </div>

        <!-- Col 2: Popular Licenses -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Popular Licenses</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/cpanel-license" class="transition hover:text-brand">cPanel &amp; WHM</a></li>
            <li><a href="/litespeed-license" class="transition hover:text-brand">LiteSpeed Web Server</a></li>
            <li><a href="/plesk-license" class="transition hover:text-brand">Plesk Control Panel</a></li>
            <li><a href="/cloudlinux-license" class="transition hover:text-brand">CloudLinux OS</a></li>
            <li><a href="/whmcs-license" class="transition hover:text-brand">WHMCS Billing</a></li>
          </ul>
        </div>

        <!-- Col 3: Panels & Utilities -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Panels &amp; Utilities</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/virtualizor-license" class="transition hover:text-brand">Virtualizor VPS</a></li>
            <li><a href="/imunify360-license" class="transition hover:text-brand">Imunify360 Security</a></li>
            <li><a href="/jetbackup-license" class="transition hover:text-brand">JetBackup 5</a></li>
            <li><a href="/softaculous-license" class="transition hover:text-brand">Softaculous</a></li>
            <li><a href="/sitepad-license" class="transition hover:text-brand">SitePad Builder</a></li>
          </ul>
          <h3 class="pt-3 font-display text-xs font-bold uppercase tracking-wider text-navy">Hosting &amp; VPS</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/shared-hosting" class="transition hover:text-brand">Shared Hosting</a></li>
            <li><a href="/reseller-hosting" class="transition hover:text-brand">Reseller Hosting</a></li>
            <li><a href="/business-email" class="transition hover:text-brand">Business Email</a></li>
            <li><a href="/n8n-hosting" class="transition hover:text-brand">n8n Hosting</a></li>
            <li><a href="/openclaw-hosting" class="transition hover:text-brand">OpenClaw Hosting</a></li>
            <li><a href="/hermes-agent-hosting" class="transition hover:text-brand">Hermes Agent Hosting</a></li>
            <li><a href="/managed-vps" class="transition hover:text-brand">Managed VPS</a></li>
            <li><a href="/unmanaged-vps" class="transition hover:text-brand">Unmanaged VPS</a></li>
            <li><a href="/port-25-open-vps" class="transition hover:text-brand">Port 25 Open VPS</a></li>
          </ul>
        </div>

        <!-- Col 4: Company & Legal -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Company &amp; Trust</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/about" class="transition hover:text-brand">About LicenBase</a></li>
            <li><a href="/contact" class="transition hover:text-brand">Contact Sales &amp; Support</a></li>
            <li><a href="/deals" class="transition hover:text-brand">Combo Deals &amp; Stacks</a></li>
            <li><a href="/free-trial" class="transition hover:text-brand">3-Day Free Trial</a></li>
            <li><a href="/blog/" class="transition hover:text-brand">Blog &amp; Knowledge Base</a></li>
            <li><a href="/tools/" class="transition hover:text-brand">Free Webmaster Tools</a></li>
            <li><a href="/license-policy" class="transition hover:text-brand">License Policy</a></li>
            <li><a href="/refund-policy" class="transition hover:text-brand">Refund Policy</a></li>
            <li><a href="/terms-of-service" class="transition hover:text-brand">Terms of Service</a></li>
            <li><a href="/privacy-policy" class="transition hover:text-brand">Privacy Policy</a></li>
          </ul>
        </div>
      </div>

      <div class="mt-12 border-t border-gray-100 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-600">
        <p>&copy; 2026 LicenBase. All rights reserved. Independent automated software licensing &amp; cloud hosting platform.</p>
        <p class="text-gray-600">All product names, logos, and brands are property of their respective owners.</p>
      </div>
    </div>
  </footer>

  <!-- ============ MOBILE DRAWER ============ -->
  <div id="drawer" class="invisible fixed inset-0 z-50 transition-all duration-300" aria-hidden="true">
    <div id="drawer-backdrop" class="absolute inset-0 bg-navy/60 backdrop-blur-sm opacity-0 transition-opacity"></div>
    <div id="drawer-panel" class="absolute right-0 top-0 h-full w-full max-w-xs bg-white p-6 shadow-2xl translate-x-full transition-transform overflow-y-auto">
      <div class="flex items-center justify-between border-b border-gray-100 pb-4">
        <img src="assets/img/logo.png" alt="LicenBase" class="h-10 w-auto" width="150" height="40" loading="lazy" decoding="async" />
        <button id="menu-close" type="button" class="grid h-9 w-9 place-items-center rounded-lg text-gray-400 hover:bg-mist hover:text-navy" aria-label="Close menu">
          <i data-lucide="x" class="h-5 w-5"></i>
        </button>
      </div>
      <nav class="mt-6 space-y-4 text-sm font-semibold">
        <p class="text-xs font-bold uppercase tracking-wider text-gray-400">Navigation</p>
        <ul class="space-y-2">
          <li><a href="/products" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">All Licenses</a></li>
          <li><a href="/shared-hosting" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Shared Hosting</a></li>
          <li><a href="/reseller-hosting" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Reseller Hosting</a></li>
          <li><a href="/business-email" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Business Email</a></li>
          <li><a href="/managed-vps" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Managed VPS</a></li>
          <li><a href="/unmanaged-vps" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Unmanaged VPS</a></li>
          <li><a href="/port-25-open-vps" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Port 25 Open VPS</a></li>
          <li><a href="/n8n-hosting" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">n8n Hosting</a></li>
          <li><a href="/openclaw-hosting" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">OpenClaw Hosting</a></li>
          <li><a href="/hermes-agent-hosting" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Hermes Agent Hosting</a></li>
          <li><a href="/deals" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Deals &amp; Combos</a></li>
          <li><a href="/blog/" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Blog</a></li>
          <li><a href="/tools/" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Tools</a></li>
          <li><a href="/contact" class="lb-mobile-link block rounded-xl px-3 py-2 text-navy hover:bg-mist">Contact</a></li>
        </ul>
        <p class="mt-6 text-xs font-bold uppercase tracking-wider text-gray-400">Account</p>
        <ul class="mt-3 space-y-1">
          <li><a href="https://dashboard.licenbase.com/clientarea.php" class="lb-mobile-link block rounded-xl bg-brand px-3 py-3 text-center text-[15px] font-semibold text-white transition hover:bg-brandDeep">Dashboard</a></li>
          <li><a href="/products" class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy transition hover:bg-mist">All Products</a></li>
        </ul>
      </nav>
    </div>
  </div>

  <!-- Search overlay -->
  <div id="search-overlay" class="invisible fixed inset-0 z-[70] opacity-0 transition-opacity duration-200" aria-hidden="true">
    <button id="search-backdrop" type="button" class="absolute inset-0 h-full w-full bg-navy/60 backdrop-blur-sm" aria-label="Close search"></button>
    <div class="relative mx-auto mt-24 w-full max-w-2xl px-4">
      <form id="overlay-search" class="lb-hero-visual rounded-2xl bg-white p-3 shadow-2xl" role="search">
        <div class="flex items-center gap-3">
          <i data-lucide="search" class="ml-2 h-5 w-5 shrink-0 text-gray-400"></i>
          <input id="overlay-search-input" type="search" placeholder="Search servers and hosting..." class="w-full bg-transparent py-3 text-[15px] text-navy placeholder:text-gray-400 focus:outline-none" autocomplete="off" />
          <button type="button" id="search-close" class="shrink-0 grid h-9 w-9 place-items-center rounded-lg text-gray-400 hover:bg-mist hover:text-navy" aria-label="Close search">
            <i data-lucide="x" class="h-5 w-5"></i>
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- Back to top -->
  <button id="to-top" type="button" aria-label="Back to top" class="invisible fixed bottom-6 right-6 z-40 grid h-11 w-11 translate-y-2 place-items-center rounded-full bg-navy text-white opacity-0 shadow-xl shadow-navy/30 transition-all duration-300 hover:bg-brand">
    <i data-lucide="arrow-up" class="h-5 w-5"></i>
  </button>

  <!-- Cart toast -->
  <div id="toast" class="pointer-events-none fixed bottom-6 left-1/2 z-[80] -translate-x-1/2 translate-y-3 opacity-0 transition-all duration-300" role="status" aria-live="polite">
    <div class="flex items-center gap-3 rounded-2xl border border-gray-200 bg-white px-5 py-3.5 shadow-2xl shadow-navy/10">
      <span class="grid h-8 w-8 place-items-center rounded-full bg-accentSoft text-accentDeep"><i data-lucide="check" class="h-4 w-4"></i></span>
      <div>
        <p class="text-sm font-bold text-navy">Action Successful</p>
        <p class="text-xs text-gray-500">Redirecting to checkout...</p>
      </div>
    </div>
  </div>

  <!-- Billing Term Switcher Script -->
  <script>
    document.querySelectorAll('[data-term]').forEach(function (b) {{
      b.addEventListener('click', function () {{
        var t = b.dataset.term;
        document.querySelectorAll('[data-term]').forEach(function (x) {{
          var on = x === b;
          x.setAttribute('aria-pressed', on);
          x.classList.toggle('bg-brand', on);
          x.classList.toggle('text-white', on);
          x.classList.toggle('shadow-md', on);
          x.classList.toggle('shadow-brand/20', on);
          x.classList.toggle('text-gray-600', !on);
        }});
        document.querySelectorAll('[data-price]').forEach(function (p) {{
          p.classList.toggle('hidden', p.dataset.price !== t);
        }});
        document.querySelectorAll('[data-cta]').forEach(function (c) {{
          c.classList.toggle('hidden', c.dataset.cta !== t);
        }});
        var n = document.querySelector('[data-lifetime-note]');
        if (n) n.classList.toggle('hidden', t !== 'lifetime');

        // Synchronize with Comparison Matrix panel toggle
        var mTarget = t === 'lifetime' ? 'lifetime' : 'recurring';
        var mBtn = document.querySelector('[data-matrix-toggle="' + mTarget + '"]');
        if (mBtn && mBtn.getAttribute('aria-pressed') !== 'true') {{
          mBtn.click();
        }}
      }});
    }});

    // Comparison Matrix Switcher Script
    document.querySelectorAll('[data-matrix-toggle]').forEach(function (b) {{
      b.addEventListener('click', function () {{
        var target = b.dataset.matrixToggle;
        document.querySelectorAll('[data-matrix-toggle]').forEach(function (x) {{
          var on = x === b;
          x.setAttribute('aria-pressed', on);
          x.classList.toggle('bg-brand', on);
          x.classList.toggle('text-white', on);
          x.classList.toggle('shadow-md', on);
          x.classList.toggle('shadow-brand/20', on);
          x.classList.toggle('text-gray-600', !on);
        }});
        document.querySelectorAll('[data-matrix-panel]').forEach(function (p) {{
          p.classList.toggle('hidden', p.dataset.matrixPanel !== target);
        }});
      }});
    }});
  </script>

  <!-- Deferred Libraries -->
  <script defer src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js" integrity="sha384-hJnF5AwidE18GSWTAGHv3ByzzvfNZ1Tcx5y1UUV3WkauuMCEzBJBMSwSt/PUPXnM" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" integrity="sha384-g4NTh/Iv5PPU4xPyhEWqPcwtNXOvdaDI8LLnyYfyNZOjKJeYQyjzQ9X5275eBjpt" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" integrity="sha384-Z3REaz79l2IaAZqJsSABtTbhjgOUYyV3p90XNnAPCSHg3EMTz1fouunq9WZRtj3d" crossorigin="anonymous"></script>
  <script defer src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js" integrity="sha384-O55L/6rhHr9CFvrxqv5luxOCcmVaBmETbZbJDP+Do8T0pztTACsFBD/IXCNkj7DV" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" integrity="sha384-2UI1PfnXFjVMQ7/ZDEF70CR943oH3v6uZrFQGGqJYlvhh4g6z6uVktxYbOlAczav" crossorigin="anonymous"></script>

  <!-- Lazy-Loaded Tawk.to Live Chat -->
  <script>
    function loadTawk() {{
      if (window.tawkLoaded) return;
      window.tawkLoaded = true;
      window.Tawk_API = window.Tawk_API || {{}};
      window.Tawk_LoadStart = new Date();
      var s1 = document.createElement("script"), s0 = document.getElementsByTagName("script")[0];
      s1.async = true;
      s1.src = 'https://embed.tawk.to/6aa54c1357bdd83448ee36a5/1k2ar2bta';
      s1.charset = 'UTF-8';
      s1.setAttribute('crossorigin', '*');
      s0.parentNode.insertBefore(s1, s0);
    }}
    ['scroll', 'keydown', 'touchstart', 'mousemove', 'click'].forEach(function(e) {{
      window.addEventListener(e, loadTawk, {{ once: true, passive: true }});
    }});
    if ('requestIdleCallback' in window) {{
      requestIdleCallback(function() {{ setTimeout(loadTawk, 3500); }});
    }} else {{
      setTimeout(loadTawk, 4000);
    }}
  </script>

  <script defer src="assets/js/main.min.js?v=2"></script>
</body>
</html>
"""
    with open(p["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {p['filename']}")

if __name__ == "__main__":
    for p in HOSTING_PRODUCTS:
        generate_hosting_page(p)
    print("All 9 hosting and server pages generated successfully!")

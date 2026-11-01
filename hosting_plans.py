"""Plans for all 9 hosting and server pages. Edit THIS file, then run:  python generate_hosting.py

Each plan:
    {"name": "Starter", "badge": "Virtual Private Servers",
     "desc": "Perfect for small business websites and apps.",
     "specs": ["2 vCPU Cores", "4 GB DDR5 RAM", "80 GB NVMe"],
     "prices": {"monthly": 19.00, "yearly": 190.00},
     "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=101",
     "popular": False}
"""

PLANS = {
    "managed-vps": [
        {
            "name": "Managed VPS Starter",
            "badge": "Starter Managed VPS",
            "desc": "Ideal for small business websites, eCommerce stores, and growing client portals.",
            "specs": [
                "2 vCPU AMD EPYC Cores",
                "4 GB High-Speed DDR5 RAM",
                "80 GB Gen4 NVMe Storage",
                "5 TB Monthly Bandwidth @ 1 Gbps",
                "cPanel & WHM License Included",
                "1 Dedicated Clean IPv4 Address",
                "Free White-Glove Migration",
                "24/7 Proactive Server Monitoring"
            ],
            "prices": {"monthly": 19.00, "yearly": 190.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=101",
            "popular": False
        },
        {
            "name": "Managed VPS Pro",
            "badge": "Agency Pick",
            "desc": "Engineered for digital agencies, high-traffic WooCommerce shops, and multi-tenant hosting.",
            "specs": [
                "4 vCPU AMD EPYC Cores",
                "8 GB High-Speed DDR5 RAM",
                "160 GB Gen4 NVMe Storage",
                "10 TB Monthly Bandwidth @ 1 Gbps",
                "cPanel & WHM License Included",
                "1 Dedicated Clean IPv4 Address",
                "LiteSpeed & Redis Cache Tuning",
                "Automated Daily Remote Backups"
            ],
            "prices": {"monthly": 34.00, "yearly": 340.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=102",
            "popular": True
        },
        {
            "name": "Managed VPS Enterprise",
            "badge": "High Compute Power",
            "desc": "Maximum processing power for resource-heavy web applications and mission-critical workloads.",
            "specs": [
                "8 vCPU AMD EPYC Cores",
                "16 GB High-Speed DDR5 RAM",
                "320 GB Gen4 NVMe Storage",
                "15 TB Monthly Bandwidth @ 1 Gbps",
                "cPanel & WHM License Included",
                "2 Dedicated Clean IPv4 Addresses",
                "Dedicated Senior Sysadmin Contact",
                "Instant Disaster Recovery Snapshots"
            ],
            "prices": {"monthly": 65.00, "yearly": 650.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=103",
            "popular": False
        }
    ],
    "unmanaged-vps": [
        {
            "name": "KVM NVMe 1",
            "badge": "Entry Cloud Instance",
            "desc": "Cost-effective KVM cloud instance for lightweight services, proxies, and test nodes.",
            "specs": [
                "1 vCPU AMD EPYC Core",
                "2 GB DDR5 RAM",
                "40 GB Gen4 NVMe Storage",
                "3 TB Monthly Bandwidth @ 1 Gbps",
                "1 Dedicated IPv4 Address",
                "100% Unrestricted Root Access",
                "AlmaLinux, Ubuntu, Debian & Rocky",
                "Automated DDoS Protection"
            ],
            "prices": {"monthly": 4.50, "yearly": 45.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=104",
            "popular": False
        },
        {
            "name": "KVM NVMe 2",
            "badge": "Developer Pick",
            "desc": "Balanced compute and memory power for Docker containers, web servers, and databases.",
            "specs": [
                "2 vCPU AMD EPYC Cores",
                "4 GB DDR5 RAM",
                "80 GB Gen4 NVMe Storage",
                "6 TB Monthly Bandwidth @ 1 Gbps",
                "1 Dedicated IPv4 Address",
                "100% Unrestricted Root Access",
                "Virtualizor VPS Management Panel",
                "Instant OS Reloads & Console"
            ],
            "prices": {"monthly": 8.50, "yearly": 85.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=105",
            "popular": True
        },
        {
            "name": "KVM NVMe 4",
            "badge": "High Concurrency Node",
            "desc": "Dedicated multi-core performance for high-traffic web backends and CI/CD runners.",
            "specs": [
                "4 vCPU AMD EPYC Cores",
                "8 GB DDR5 RAM",
                "160 GB Gen4 NVMe Storage",
                "10 TB Monthly Bandwidth @ 1 Gbps",
                "1 Dedicated IPv4 Address",
                "100% Unrestricted Root Access",
                "Custom ISO Mount & rDNS Control",
                "24/7 Hardware Uptime Monitoring"
            ],
            "prices": {"monthly": 16.00, "yearly": 160.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=106",
            "popular": False
        }
    ],
    "port-25-open-vps": [
        {
            "name": "SMTP Starter VPS",
            "badge": "Entry Mail Relay",
            "desc": "Unblocked port 25 server for transactional emails, notifications, and small newsletters.",
            "specs": [
                "2 vCPU Cores",
                "4 GB High-Speed RAM",
                "60 GB Gen4 NVMe Storage",
                "4 TB Monthly Bandwidth",
                "Outbound Port 25 Unblocked",
                "1 Clean Dedicated IPv4 Address",
                "Self-Service rDNS / PTR Setup",
                "SPF, DKIM & DMARC Ready"
            ],
            "prices": {"monthly": 12.00, "yearly": 120.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=107",
            "popular": False
        },
        {
            "name": "SMTP Pro VPS",
            "badge": "High Volume",
            "desc": "High-throughput mail server engineered for marketing campaigns, SaaS alerts, and relays.",
            "specs": [
                "4 vCPU Cores",
                "8 GB High-Speed RAM",
                "120 GB Gen4 NVMe Storage",
                "8 TB Monthly Bandwidth",
                "Outbound Port 25 Unblocked",
                "2 Clean Dedicated IPv4 Addresses",
                "Instant PTR Record Delegation",
                "Optimized Mail Transfer Agents"
            ],
            "prices": {"monthly": 24.00, "yearly": 240.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=108",
            "popular": True
        },
        {
            "name": "SMTP Fleet VPS",
            "badge": "Enterprise Mail Hub",
            "desc": "Maximum mail queue capacity with multiple clean dedicated IPs for agency delivery fleets.",
            "specs": [
                "8 vCPU Cores",
                "16 GB High-Speed RAM",
                "240 GB Gen4 NVMe Storage",
                "15 TB Monthly Bandwidth",
                "Outbound Port 25 Unblocked",
                "4 Clean Dedicated IPv4 Addresses",
                "Multi-IP Queue Balancing",
                "24/7 Deliverability Support"
            ],
            "prices": {"monthly": 45.00, "yearly": 450.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=109",
            "popular": False
        }
    ],
    "shared-hosting": [
        {
            "name": "Personal NVMe",
            "badge": "Personal & Starter Sites",
            "desc": "High-performance NVMe cloud hosting with LiteSpeed cache and cPanel for personal websites and blogs.",
            "specs": [
                "Unlimited Websites Hosted",
                "10 GB Pure NVMe Storage",
                "2 vCPU | 2 GB Dedicated RAM",
                "IO: 50 MB/s, IOPS: 1024, EP: 30",
                "Daily Automated Remote Backups",
                "1-Click Softaculous / Script Installer",
                "LiteSpeed Web Server with LSCache",
                "cPanel Control Panel Included",
                "Free SSL Certificate"
            ],
            "prices": {"monthly": 2.99, "yearly": 29.78, "lifetime": 129.00},
            "yearly_base": 35.88,
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=27&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=27&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=27&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=31"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/shared-hosting/personal-nvme",
                "yearly": "https://dashboard.licenbase.com/store/shared-hosting/personal-nvme",
                "lifetime": "https://dashboard.licenbase.com/store/shared-hosting/personal-nvme-lifetime"
            },
            "popular": False
        },
        {
            "name": "Professional NVMe",
            "badge": "High Speed",
            "desc": "Blazing-fast LiteSpeed hosting with 30 GB NVMe disk and 2 vCPU compute for business and eCommerce.",
            "specs": [
                "Unlimited Websites Hosted",
                "30 GB Pure NVMe Storage",
                "2 vCPU | 2 GB Dedicated RAM",
                "IO: 50 MB/s, IOPS: 1024, EP: 30",
                "Daily Automated Remote Backups",
                "1-Click Softaculous / Script Installer",
                "LiteSpeed Web Server with LSCache",
                "cPanel Control Panel Included",
                "Free SSL Certificate"
            ],
            "prices": {"monthly": 4.99, "yearly": 49.70, "lifetime": 229.00},
            "yearly_base": 59.88,
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=28&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=28&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=28&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=32"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/shared-hosting/professional-nvme",
                "yearly": "https://dashboard.licenbase.com/store/shared-hosting/professional-nvme",
                "lifetime": "https://dashboard.licenbase.com/store/shared-hosting/professional-nvme-lifetime"
            },
            "popular": True
        },
        {
            "name": "Turbo NVMe",
            "badge": "Maximum NVMe Capacity",
            "desc": "Unlimited NVMe storage powered by LiteSpeed Enterprise, high I/O throughput, and unmetered websites.",
            "specs": [
                "Unlimited Websites Hosted",
                "Unlimited Pure NVMe Storage",
                "2 vCPU | 2 GB Dedicated RAM",
                "IO: 50 MB/s, IOPS: 1024, EP: 30",
                "Daily Automated Remote Backups",
                "1-Click Softaculous / Script Installer",
                "LiteSpeed Web Server with LSCache",
                "cPanel Control Panel Included",
                "Free SSL Certificate"
            ],
            "prices": {"monthly": 7.99, "yearly": 79.58, "lifetime": 399.00},
            "yearly_base": 95.88,
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=29&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=29&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=29&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=30"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/shared-hosting/turbo-nvme",
                "yearly": "https://dashboard.licenbase.com/store/shared-hosting/turbo-nvme",
                "lifetime": "https://dashboard.licenbase.com/store/shared-hosting/turbo-nvme-lifetime"
            },
            "popular": False
        }
    ],
    "reseller-hosting": [
        {
            "name": "Bronze Reseller",
            "badge": "Starter Agency Plan",
            "desc": "Perfect for freelancers and web studios managing up to 20 client cPanel accounts.",
            "specs": [
                "20 cPanel Accounts",
                "20 GB NVMe SSD Disk Space",
                "Unlimited Bandwidth",
                "2 vCPU | 2 GB RAM Per cPanel",
                "24/7 Instant Response Support",
                "WHM (Admin Control Panel)",
                "Daily Automated Remote Backups",
                "Custom Private Nameservers",
                "100% Whitelabel / Unbranded",
                "Free Reseller Migration",
                "Free SSL Certificates"
            ],
            "prices": {"monthly": 28.00, "yearly": 196.00, "lifetime": 360.00},
            "yearly_base": 336.00,
            "discount_badge": "5 Months Free (Save 42%)",
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=33&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=33&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=33&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=36"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/reseller-hosting/bronze-reseller",
                "yearly": "https://dashboard.licenbase.com/store/reseller-hosting/bronze-reseller",
                "lifetime": "https://dashboard.licenbase.com/store/reseller-hosting/bronze-reseller-lifetime"
            },
            "popular": False
        },
        {
            "name": "Silver Reseller",
            "badge": "Agency Standard",
            "desc": "Our most popular agency tier with 50 accounts, unlimited NVMe disk, and high performance.",
            "specs": [
                "50 cPanel Accounts",
                "Unlimited NVMe SSD Disk Space",
                "Unlimited Bandwidth",
                "2 vCPU | 2 GB RAM Per cPanel",
                "24/7 Instant Response Support",
                "WHM (Admin Control Panel)",
                "Daily Automated Remote Backups",
                "Custom Private Nameservers",
                "100% Whitelabel / Unbranded",
                "Free Reseller Migration",
                "Free SSL Certificates"
            ],
            "prices": {"monthly": 65.00, "yearly": 455.00, "lifetime": 665.00},
            "yearly_base": 780.00,
            "discount_badge": "5 Months Free (Save 42%)",
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=34&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=34&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=34&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=37"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/reseller-hosting/silver-reseller",
                "yearly": "https://dashboard.licenbase.com/store/reseller-hosting/silver-reseller",
                "lifetime": "https://dashboard.licenbase.com/store/reseller-hosting/silver-reseller-lifetime"
            },
            "popular": True
        },
        {
            "name": "Gold Enterprise Reseller",
            "badge": "Master Enterprise Fleet",
            "desc": "High-capacity tier for large web agencies hosting 100 client sites with unlimited NVMe.",
            "specs": [
                "100 cPanel Accounts",
                "Unlimited NVMe SSD Disk Space",
                "Unlimited Bandwidth",
                "2 vCPU | 2 GB RAM Per cPanel",
                "24/7 Instant Response Support",
                "WHM (Admin Control Panel)",
                "Daily Automated Remote Backups",
                "Custom Private Nameservers",
                "100% Whitelabel / Unbranded",
                "Free Reseller Migration",
                "Free SSL Certificates"
            ],
            "prices": {"monthly": 95.00, "yearly": 665.00, "lifetime": 980.00},
            "yearly_base": 1140.00,
            "discount_badge": "5 Months Free (Save 42%)",
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=35&billingcycle=monthly",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=35&billingcycle=monthly",
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=35&billingcycle=annually",
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=38"
            },
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/reseller-hosting/gold-enterprise-reseller",
                "yearly": "https://dashboard.licenbase.com/store/reseller-hosting/gold-enterprise-reseller",
                "lifetime": "https://dashboard.licenbase.com/store/reseller-hosting/gold-enterprise-reseller-lifetime"
            },
            "popular": False
        }
    ],
    "business-email": [
        {
            "name": "Business Email Hosting",
            "badge": "Standard Plan · Personalized Domain",
            "desc": "Professional business email hosting on your own domain with 5 GB storage per mailbox, ClamAV antivirus, and multi-device IMAP sync.",
            "specs": [
                "1 Email Accounts included",
                "Upgradable upto 49 Email Accounts + Different billing per address",
                "5GB Email Storage per Account",
                "Inbuilt Virus Protection",
                "Mobile and Tablet Support (iOS, Android, etc.)",
                "Social Media Support (Twitter, Facebook, etc)",
                "Personalized Custom Domain (you@yourdomain.com)",
                "Automated Instant Auto-Responder",
                "Modern Webmail, IMAP, POP3 & SMTP Access",
                "99.99% Datacenter & Mail Uptime Guarantee"
            ],
            "prices": {"monthly": 2.49, "yearly": 28.99},
            "url": "https://dashboard.licenbase.com/store/business-email/business-email-standard",
            "popular": True
        }
    ],
    "n8n-hosting": [
        {
            "name": "Starter",
            "pid": 39,
            "badge": "Solo Automation Node",
            "tagline": "Great for Getting Started",
            "desc": "Dedicated instance for personal workflow pipelines, webhooks, and light automations.",
            "specs": [
                "Great for Getting Started",
                "Unlimited Workflows",
                "Unlimited Executions",
                "Unlimited Storage",
                "Daily Backups",
                "99.99% Uptime SLA",
                "24/7 Live Chat"
            ],
            "price": 9.00,
            "price_str": "$9.00",
            "period_label": "mo",
            "cycle_label": "Billed Monthly",
            "prices": {"monthly": 9.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=39",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=39"
            },
            "store_url": "https://dashboard.licenbase.com/store/n8n-hosting/starter",
            "store_urls": {
                "monthly": "https://dashboard.licenbase.com/store/n8n-hosting/starter"
            },
            "popular": False
        },
        {
            "name": "Professional",
            "pid": 40,
            "badge": "Agency & Team Pick",
            "tagline": "Best Value for Teams",
            "desc": "Engineered for high-volume webhook automations, version upgrades, and advanced monitoring.",
            "specs": [
                "Best Value for Teams",
                "Everything in Starter",
                "Unlimited Workflows",
                "Unlimited Executions",
                "Unlimited Storage",
                "Priority Support",
                "Advanced Monitoring",
                "Free Version Upgrades",
                "Daily Backups",
                "99.99% Uptime SLA",
                "24/7 Live Chat"
            ],
            "price": 90.00,
            "price_str": "$90.00",
            "period_label": "yr",
            "cycle_label": "Billed Annually",
            "savings": "Save $18/yr ($7.50/mo equiv.)",
            "prices": {"yearly": 90.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=40",
            "urls": {
                "yearly": "https://dashboard.licenbase.com/cart.php?a=add&pid=40"
            },
            "store_url": "https://dashboard.licenbase.com/store/n8n-hosting/professional",
            "store_urls": {
                "yearly": "https://dashboard.licenbase.com/store/n8n-hosting/professional"
            },
            "popular": True
        },
        {
            "name": "Growth",
            "pid": 41,
            "badge": "Dedicated Performance",
            "tagline": "Scale with Confidence",
            "desc": "Dedicated compute with 2-year price lock protection for scaling automation pipelines.",
            "specs": [
                "Scale with Confidence",
                "Unlimited Workflows",
                "Unlimited Executions",
                "Dedicated Performance",
                "Priority Support",
                "Advanced Monitoring",
                "Price Lock for 2 Years",
                "Daily Backups",
                "99.99% Uptime SLA",
                "24/7 Live Chat"
            ],
            "price": 180.00,
            "price_str": "$180.00",
            "period_label": "2yr",
            "cycle_label": "Billed Every 2 Years",
            "savings": "Price Lock for 2 Years ($7.50/mo)",
            "prices": {"biennial": 180.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=41",
            "urls": {
                "biennial": "https://dashboard.licenbase.com/cart.php?a=add&pid=41"
            },
            "store_url": "https://dashboard.licenbase.com/store/n8n-hosting/growth",
            "store_urls": {
                "biennial": "https://dashboard.licenbase.com/store/n8n-hosting/growth"
            },
            "popular": False
        },
        {
            "name": "Lifetime",
            "pid": 42,
            "badge": "★ Best Deal · Pay Once",
            "tagline": "Pay Once, Automate Forever",
            "desc": "Pay once and automate forever. Zero renewal bills, lifetime updates, and priority support.",
            "specs": [
                "★ Best Deal — Pay Once, Automate Forever",
                "No renewals. No hidden fees. Ever.",
                "Unlimited Everything — Forever",
                "Lifetime Updates",
                "Lifetime Monitoring",
                "Priority Support",
                "99.99% Uptime SLA",
                "Zero Recurring Fees"
            ],
            "price": 420.00,
            "price_str": "$420.00",
            "period_label": "one-time",
            "cycle_label": "One-Time Purchase",
            "savings": "Zero Recurring Fees Ever",
            "prices": {"lifetime": 420.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=42",
            "urls": {
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=42"
            },
            "store_url": "https://dashboard.licenbase.com/store/n8n-hosting/lifetime",
            "store_urls": {
                "lifetime": "https://dashboard.licenbase.com/store/n8n-hosting/lifetime"
            },
            "popular": False
        }
    ],
    "openclaw-hosting": [
        {
            "name": "OpenClaw Hosting",
            "badge": "Monthly Subscription",
            "tagline": "Autonomous Multi-Channel AI Agent",
            "desc": "Dedicated cloud runtime for autonomous AI bots connected to WhatsApp, Telegram, Discord, and 40+ channels.",
            "specs": [
                "Unlimited storage and resource usage",
                "Unlimited skills and automation",
                "All AI models (GPT-4o, Claude, Llama, Kimi)",
                "WhatsApp, Telegram, Discord and 40+ channels",
                "Full management dashboard",
                "Custom bot personas",
                "99.99% uptime SLA",
                "Free installation and setup"
            ],
            "price": 14.00,
            "price_str": "$14.00",
            "period_label": "mo",
            "cycle_label": "Monthly Recurring Billing",
            "prices": {"monthly": 14.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=43",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=43"
            },
            "popular": False
        },
        {
            "name": "OpenClaw Hosting Lifetime",
            "badge": "★ Best Deal · Pay Once",
            "tagline": "Pay Once, Run Bots Forever",
            "desc": "Lifetime access with all future updates, priority support, and zero renewal fees ever.",
            "specs": [
                "Unlimited storage and resource usage",
                "Unlimited skills and automation",
                "All AI models (GPT-4o, Claude, Llama, Kimi)",
                "WhatsApp, Telegram, Discord and 40+ channels",
                "Full management dashboard",
                "Custom bot personas",
                "99.99% uptime SLA",
                "All future features and updates",
                "Lifetime priority support"
            ],
            "price": 380.00,
            "price_str": "$380.00",
            "period_label": "one-time",
            "cycle_label": "One-Time Purchase",
            "savings": "Zero Recurring Fees Ever",
            "prices": {"lifetime": 380.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=44",
            "urls": {
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=44"
            },
            "popular": True
        }
    ],
    "hermes-agent-hosting": [
        {
            "name": "Hermes Agent",
            "badge": "Monthly Subscription",
            "tagline": "Autonomous AI Agent Cloud",
            "desc": "Dedicated cloud runtime for continuous autonomous AI agents, tool-calling loops, and reasoning workflows.",
            "specs": [
                "Auto-deployed in minutes",
                "Private SSL-secured subdomain",
                "Bring your own LLM key",
                "Start / stop / restart controls",
                "99.99% uptime SLA"
            ],
            "price": 14.00,
            "price_str": "$14.00",
            "period_label": "mo",
            "cycle_label": "Monthly Recurring Billing",
            "prices": {"monthly": 14.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=45",
            "urls": {
                "monthly": "https://dashboard.licenbase.com/cart.php?a=add&pid=45"
            },
            "popular": False
        },
        {
            "name": "Hermes Agent Lifetime",
            "badge": "★ Best Deal · Pay Once",
            "tagline": "Pay Once, Run Agents Forever",
            "desc": "Lifetime access with persistent storage, full daemon controls, zero renewal bills, and priority support.",
            "specs": [
                "Auto-deployed in minutes",
                "Private SSL-secured subdomain",
                "Bring your own LLM key",
                "Start / stop / restart controls",
                "No recurring fees"
            ],
            "price": 380.00,
            "price_str": "$380.00",
            "period_label": "one-time",
            "cycle_label": "One-Time Purchase",
            "savings": "Zero Recurring Fees Ever",
            "prices": {"lifetime": 380.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=46",
            "urls": {
                "lifetime": "https://dashboard.licenbase.com/cart.php?a=add&pid=46"
            },
            "popular": True
        }
    ]
}

LIFETIME_NOTE = "Lifetime plans include full server resources with a single one-time payment. Subject to fair-use terms."

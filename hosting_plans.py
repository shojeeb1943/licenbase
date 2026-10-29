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
            "badge": "Most Popular · Agency Pick",
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
            "badge": "Most Popular · Developer Pick",
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
            "badge": "Most Popular · High Volume",
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
            "badge": "Single Website Starter",
            "desc": "Perfect for personal blogs, portfolios, and lightweight starter projects.",
            "specs": [
                "1 Website Hosted",
                "10 GB NVMe SSD Storage",
                "Unmetered Monthly Bandwidth",
                "Free AutoSSL Certificates",
                "5 Business Email Accounts",
                "cPanel & Softaculous 1-Click Apps",
                "Automated Daily Remote Backups"
            ],
            "prices": {"monthly": 2.50, "yearly": 25.00, "lifetime": 49.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=110",
            "popular": False
        },
        {
            "name": "Professional NVMe",
            "badge": "Most Popular · Unlimited Sites",
            "desc": "Blazing-fast LiteSpeed hosting with unmetered websites for businesses and creators.",
            "specs": [
                "Unlimited Websites Hosted",
                "50 GB NVMe SSD Storage",
                "Unmetered Monthly Bandwidth",
                "Free Unlimited SSL Certificates",
                "Unlimited Business Email Accounts",
                "LiteSpeed Web Server + LSCache",
                "2x CPU & RAM Allocation",
                "Free White-Glove Site Migration"
            ],
            "prices": {"monthly": 4.99, "yearly": 49.00, "lifetime": 89.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=111",
            "popular": True
        },
        {
            "name": "Turbo NVMe",
            "badge": "Maximum Speed & Security",
            "desc": "Highest tier computing power with Imunify360 AI defense and unmetered NVMe disk.",
            "specs": [
                "Unlimited Websites Hosted",
                "Unlimited NVMe SSD Storage",
                "Unmetered Monthly Bandwidth",
                "Free Dedicated IPv4 Address",
                "4x CPU & RAM Allocation",
                "LiteSpeed Enterprise Acceleration",
                "Imunify360 Proactive Defense",
                "Priority 24/7 VIP Support"
            ],
            "prices": {"monthly": 8.99, "yearly": 89.00, "lifetime": 149.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=112",
            "popular": False
        }
    ],
    "reseller-hosting": [
        {
            "name": "Bronze Reseller",
            "badge": "Starter Reseller Plan",
            "desc": "Ideal for freelance web designers and developers hosting their first client websites.",
            "specs": [
                "25 cPanel Accounts",
                "50 GB Pure NVMe Storage",
                "1 TB Monthly Bandwidth",
                "Full WebHost Manager (WHM) Access",
                "Free AutoSSL for All Clients",
                "Private Custom Nameservers",
                "Free Softaculous 1-Click Apps"
            ],
            "prices": {"monthly": 9.00, "yearly": 90.00, "lifetime": 129.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=113",
            "popular": False
        },
        {
            "name": "Silver Reseller",
            "badge": "Most Popular · Agency Standard",
            "desc": "The complete agency standard with overselling enabled and LiteSpeed acceleration.",
            "specs": [
                "60 cPanel Accounts",
                "120 GB Pure NVMe Storage",
                "3 TB Monthly Bandwidth",
                "Full WHM Administrative Access",
                "Overselling Enabled Across Accounts",
                "LiteSpeed Web Server Acceleration",
                "Free Billing Software Integration",
                "Automated Daily Remote Backups"
            ],
            "prices": {"monthly": 16.00, "yearly": 160.00, "lifetime": 219.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=114",
            "popular": True
        },
        {
            "name": "Gold Enterprise Reseller",
            "badge": "Master WHM Enterprise",
            "desc": "Maximum account volume with Master WHM plugins and VIP technical agency support.",
            "specs": [
                "150 cPanel Accounts",
                "250 GB Pure NVMe Storage",
                "6 TB Monthly Bandwidth",
                "Master WHM & WHMReseller Plugin",
                "Overselling Enabled Across Accounts",
                "100% White-Label Branding",
                "Imunify360 Security Suite Included",
                "VIP Priority 24/7 Agency Desk"
            ],
            "prices": {"monthly": 28.00, "yearly": 280.00, "lifetime": 349.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=115",
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
            "name": "n8n Starter",
            "badge": "Solo Automation Node",
            "desc": "Dedicated instance for personal workflow pipelines, webhooks, and light automations.",
            "specs": [
                "Dedicated Cloud Instance",
                "2 vCPU Cores & 4 GB RAM",
                "40 GB NVMe Storage",
                "Unlimited Active Workflows",
                "Pre-configured PostgreSQL Database",
                "Custom Subdomain & Automated SSL",
                "Unlimited Webhook Triggers"
            ],
            "prices": {"monthly": 9.00, "yearly": 90.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=119",
            "popular": False
        },
        {
            "name": "n8n Production",
            "badge": "Most Popular · High Concurrency",
            "desc": "Production-grade queue architecture with Redis and high-speed database execution.",
            "specs": [
                "Dedicated High-Compute Instance",
                "4 vCPU Cores & 8 GB RAM",
                "80 GB NVMe Storage",
                "High-Concurrency Queue Mode",
                "Redis Queue + Dedicated PostgreSQL",
                "Community & Custom Node Support",
                "Zero Cold Starts & Dedicated CPU",
                "Automated Daily Instance Snapshots"
            ],
            "prices": {"monthly": 19.00, "yearly": 190.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=120",
            "popular": True
        },
        {
            "name": "n8n Enterprise Cluster",
            "badge": "Multi-Worker Cluster",
            "desc": "Multi-worker scaling cluster for high-volume enterprise automation pipelines.",
            "specs": [
                "Multi-Worker Scaling Architecture",
                "8 vCPU Cores & 16 GB RAM",
                "160 GB NVMe Storage",
                "High-Availability Redis & DB Cluster",
                "Multi-Tenant Team Collaboration",
                "Dedicated IP & Custom Domain",
                "SLA 99.99% Execution Uptime",
                "24/7 Sysadmin Automation Support"
            ],
            "prices": {"monthly": 39.00, "yearly": 390.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=121",
            "popular": False
        }
    ],
    "openclaw-hosting": [
        {
            "name": "Crawler Node",
            "badge": "Single Browser Node",
            "desc": "Dedicated cloud environment for automated testing, single-worker scrapers, and cron tasks.",
            "specs": [
                "Dedicated Browser Environment",
                "2 vCPU Cores & 4 GB RAM",
                "50 GB NVMe Storage",
                "Pre-installed Chromium & Node Runtime",
                "Headless Browser Automation Ready",
                "Custom Webhook Triggering",
                "Residential & Datacenter Proxy Ready"
            ],
            "prices": {"monthly": 9.00, "yearly": 90.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=122",
            "popular": False
        },
        {
            "name": "Scraper Pro",
            "badge": "Most Popular · High Volume",
            "desc": "Multi-threaded headless browser swarm with anti-fingerprinting stealth plugins.",
            "specs": [
                "High-Concurrency Scraping Node",
                "4 vCPU Cores & 8 GB RAM",
                "100 GB NVMe Storage",
                "Multi-Threaded Headless Browser Swarm",
                "Anti-Fingerprinting Stealth Modules",
                "Redis Queue Task Pipeline",
                "Dedicated 1 Gbps Port",
                "Automated Process Watchdog"
            ],
            "prices": {"monthly": 19.00, "yearly": 190.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=123",
            "popular": True
        },
        {
            "name": "Enterprise Farm",
            "badge": "Distributed Cluster",
            "desc": "Massive extraction capacity for web data intelligence, market scrapers, and datasets.",
            "specs": [
                "Distributed Scraping Cluster",
                "8 vCPU Cores & 16 GB RAM",
                "200 GB NVMe Storage",
                "Massive Concurrent Page Extractions",
                "Zero Browser Memory Leaks",
                "Custom Proxy Rotation Engine",
                "Persistent Storage & Data Pipelines",
                "24/7 Scraping Infrastructure Support"
            ],
            "prices": {"monthly": 39.00, "yearly": 390.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=124",
            "popular": False
        }
    ],
    "hermes-agent-hosting": [
        {
            "name": "Agent Starter",
            "badge": "Autonomous Sandbox",
            "desc": "Dedicated AI agent sandbox for experimentation, local tool calling, and solo agents.",
            "specs": [
                "Dedicated AI Agent Sandbox",
                "2 vCPU Cores & 4 GB RAM",
                "50 GB NVMe Storage",
                "Python 3.11+ & Node Environment",
                "Hermes Agent Framework Pre-installed",
                "ChromaDB / Qdrant Vector Ready",
                "REST & Webhook Execution API"
            ],
            "prices": {"monthly": 9.00, "yearly": 90.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=125",
            "popular": False
        },
        {
            "name": "Agent Pro",
            "badge": "Most Popular · Production Agent",
            "desc": "Persistent agent workstation with long-term memory store and multi-agent coordination.",
            "specs": [
                "Autonomous Agent Workstation",
                "4 vCPU Cores & 8 GB RAM",
                "100 GB NVMe Storage",
                "Multi-Agent Concurrent Orchestration",
                "Persistent State & Long-Term Memory",
                "Redis Memory Cache & Session Store",
                "High-Speed Inference API Endpoints",
                "Automatic Process Respawn Daemon"
            ],
            "prices": {"monthly": 19.00, "yearly": 190.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=126",
            "popular": True
        },
        {
            "name": "Agent Cluster",
            "badge": "Enterprise AI Swarm",
            "desc": "High-compute swarm node for long-running autonomous workflows and agent fleets.",
            "specs": [
                "Enterprise Autonomous Swarm",
                "8 vCPU Cores & 16 GB RAM",
                "200 GB NVMe Storage",
                "Full Local Tool & Code Execution Sandbox",
                "Distributed Task Queue & Scheduler",
                "Dedicated High-Throughput Network",
                "Daily Automated State Snapshots",
                "24/7 AI Infrastructure Specialist Support"
            ],
            "prices": {"monthly": 39.00, "yearly": 390.00},
            "url": "https://dashboard.licenbase.com/cart.php?a=add&pid=127",
            "popular": False
        }
    ]
}

LIFETIME_NOTE = "Lifetime plans include full server resources with a single one-time payment. Subject to fair-use terms."

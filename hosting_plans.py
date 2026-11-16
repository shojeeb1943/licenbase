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
            "name": "Managed Cloud VPS 4",
            "badge": "Essential Cloud",
            "desc": "Balanced compute for business websites, production WordPress, and small apps.",
            "specs": [
                "4 vCPU Cores",
                "8 GB Guaranteed RAM",
                "100 GB High-Speed SSD Storage",
                "200 Mbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 21.60},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-4",
            "popular": False
        },
        {
            "name": "Managed Cloud VPS 6",
            "badge": "Growth Value",
            "desc": "High-concurrency VPS for expanding client portals and dynamic web applications.",
            "specs": [
                "6 vCPU Cores",
                "12 GB Guaranteed RAM",
                "200 GB SSD / 100 GB NVMe Storage",
                "300 Mbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 24.00},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-6",
            "popular": False
        },
        {
            "name": "Managed Cloud VPS 8",
            "badge": "Most Popular Choice",
            "desc": "Engineered for digital agencies, multi-tenant hosting, and busy WooCommerce stores.",
            "specs": [
                "8 vCPU Cores",
                "24 GB Guaranteed RAM",
                "300 GB SSD / 150 GB NVMe Storage",
                "600 Mbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 31.80},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-8",
            "popular": True
        },
        {
            "name": "Managed Cloud VPS 12",
            "badge": "High Compute Power",
            "desc": "Heavy-duty compute for resource-intensive databases, APIs, and multi-site networks.",
            "specs": [
                "12 vCPU Cores",
                "48 GB Guaranteed RAM",
                "400 GB SSD / 200 GB NVMe Storage",
                "800 Mbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 45.00},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-12",
            "popular": False
        },
        {
            "name": "Managed Cloud VPS 16",
            "badge": "Enterprise Power",
            "desc": "Massive multi-core processing power and 64 GB RAM for enterprise workloads.",
            "specs": [
                "16 vCPU Cores",
                "64 GB Guaranteed RAM",
                "500 GB SSD / 250 GB NVMe Storage",
                "1 Gbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 59.50},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-16",
            "popular": False
        },
        {
            "name": "Managed Cloud VPS 18",
            "badge": "Ultimate Beast",
            "desc": "Peak virtualized horsepower with 18 vCPU cores and 96 GB RAM for maximum scale.",
            "specs": [
                "18 vCPU Cores",
                "96 GB Guaranteed RAM",
                "600 GB SSD / 300 GB NVMe Storage",
                "1 Gbit/s Port (Unlimited Traffic)",
                "WHM/cPanel & Necessary Licenses Included",
                "Softaculous & SitePad Website Builder Included",
                "Fully Managed Support: 24/7 Monitoring",
                "Free Full Migration Assistance",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 73.80},
            "url": "https://dashboard.licenbase.com/store/managed-vps/managed-cloud-vps-18",
            "popular": False
        }
    ],
    "unmanaged-vps": [
        {
            "name": "Unmanaged Cloud VPS x4",
            "badge": "Entry NVMe Cloud",
            "desc": "Fast NVMe compute for lightweight services, dev containers, and custom micro-stacks.",
            "specs": [
                "2 Core CPU",
                "4 GB RAM",
                "40 GB NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 5.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x4",
            "popular": False
        },
        {
            "name": "Unmanaged Cloud VPS x8",
            "badge": "Developer Choice",
            "desc": "Solid quad-core performance with 8 GB RAM for web apps, docker swarms, and databases.",
            "specs": [
                "4 Core CPU",
                "8 GB RAM",
                "60 GB NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 11.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x8",
            "popular": False
        },
        {
            "name": "Unmanaged Cloud VPS x12",
            "badge": "Most Popular Choice",
            "desc": "Optimal memory-to-CPU ratio with 12 GB RAM for production backends and API clusters.",
            "specs": [
                "4 Core CPU",
                "12 GB RAM",
                "90 GB NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 17.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x12",
            "popular": True
        },
        {
            "name": "Unmanaged Cloud VPS x16",
            "badge": "High Performance",
            "desc": "High-throughput 6-core compute with 16 GB RAM for high-traffic servers.",
            "specs": [
                "6 Core CPU",
                "16 GB RAM",
                "120 GB High-Speed NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 21.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x16",
            "popular": False
        },
        {
            "name": "Unmanaged Cloud VPS x24",
            "badge": "Heavy Workloads",
            "desc": "Expanded 24 GB RAM and 180 GB NVMe storage for memory-intensive caching and queues.",
            "specs": [
                "6 Core CPU",
                "24 GB RAM",
                "180 GB NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 31.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x24",
            "popular": False
        },
        {
            "name": "Unmanaged Cloud VPS x32",
            "badge": "Maximum Memory",
            "desc": "Top-tier unmanaged instance with 32 GB RAM for demanding virtualization and big data.",
            "specs": [
                "6 Core CPU",
                "32 GB RAM",
                "180 GB NVMe Storage",
                "1 Gbps Port (Unlimited Bandwidth)",
                "FREE Automated Backup Included",
                "Full Root Access (Linux / Windows)",
                "Dedicated IPv4 Included",
                "1-2 Hours Activation Time"
            ],
            "prices": {"monthly": 41.98},
            "url": "https://dashboard.licenbase.com/store/unmanaged-vps/unmanaged-cloud-vps-x32",
            "popular": False
        }
    ],
    "port-25-open-vps": [
        {
            "name": "Port 25 VPS Starter",
            "badge": "Entry Mail Relay",
            "desc": "Unblocked port 25 cloud server for transactional emails, notifications, and mail relays.",
            "specs": [
                "1 vCPU AMD EPYC Core",
                "1 GB High-Speed RAM",
                "10 GB Gen4 NVMe Storage",
                "2 Gbit/s High-Speed Network",
                "Outbound Port 25 Unblocked",
                "1 Clean Dedicated IPv4 Address",
                "Self-Service rDNS / PTR Setup",
                "30+ Global Datacenter Locations"
            ],
            "prices": {"monthly": 9.96, "yearly": 99.60},
            "url": "https://dashboard.licenbase.com/index.php?m=vpsorder&dc=5&tarif=13",
            "popular": False
        },
        {
            "name": "Port 25 Open VPS",
            "badge": "Most Popular Choice",
            "desc": "High-throughput cloud server with unrestricted outbound port 25 for marketing campaigns, SaaS alerts, and relays.",
            "specs": [
                "2 vCPU AMD EPYC Cores",
                "4 GB High-Speed RAM",
                "25 GB Gen4 NVMe Storage",
                "2 Gbit/s High-Speed Network",
                "Outbound Port 25 Unblocked",
                "1 Clean Dedicated IPv4 Address",
                "Instant PTR Record Delegation",
                "30+ Global Datacenter Locations"
            ],
            "prices": {"monthly": 18.23, "yearly": 182.30},
            "url": "https://dashboard.licenbase.com/index.php?m=vpsorder&dc=5&tarif=15",
            "popular": True
        },
        {
            "name": "Port 25 VPS Pro",
            "badge": "High Volume",
            "desc": "Maximum queue capacity with dedicated compute for high-volume email delivery infrastructure.",
            "specs": [
                "4 vCPU AMD EPYC Cores",
                "4 GB High-Speed RAM",
                "40 GB Gen4 NVMe Storage",
                "2 Gbit/s High-Speed Network",
                "Outbound Port 25 Unblocked",
                "1 Clean Dedicated IPv4 Address",
                "Instant PTR Record Delegation",
                "30+ Global Datacenter Locations"
            ],
            "prices": {"monthly": 36.45, "yearly": 364.50},
            "url": "https://dashboard.licenbase.com/index.php?m=vpsorder&dc=5&tarif=16",
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

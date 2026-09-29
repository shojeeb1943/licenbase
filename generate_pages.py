import os

products = [
    {
        "filename": "cpanel-license.html",
        "slug": "cpanel",
        "title": "cPanel & WHM License (VPS & Dedicated)",
        "meta_desc": "Buy genuine cPanel & WHM licenses for VPS ($4.00/mo) and Dedicated Servers ($8.00/mo) with instant activation, unlimited accounts, free SSL, and single-command install.",
        "badge": "Industry Standard Web Hosting Control Panel",
        "icon": "server",
        "headline": "Genuine cPanel & WHM Licenses",
        "headline_sub": "At Unbeatable Wholesale Prices.",
        "hero_desc": "Empower your web hosting infrastructure with genuine, IP-bound cPanel & WHM licenses. Enjoy unlimited cPanel accounts, full root access, automatic core updates, and seamless server automation.",
        "specs": ["Unlimited Accounts", "Official cPanel Updates", "Instant IP Activation", "Free Re-IP Migration", "Dual Verification Cluster", "24/7 Server Support"],
        "tiers": [
            {
                "name": "cPanel VPS License",
                "price": "$4.00",
                "period": "per month",
                "popular": False,
                "badge": "Virtual Private Servers",
                "desc": "Perfect for KVM, OpenVZ, Proxmox, AWS, and Cloud VPS instances of any size.",
                "features": [
                    "Unlimited cPanel & WHM Accounts",
                    "Full Root Administrative WHM Access",
                    "Official cPanel Updates & Security Patches",
                    "FleetSSL / AutoSSL Free Certificate Engine",
                    "Softaculous & SitePad Compatibility",
                    "Instant Automatic IP Activation",
                    "Unlimited Free Server IP Replacements"
                ],
                "btn_text": "Order cPanel VPS",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=1"
            },
            {
                "name": "cPanel Dedicated License",
                "price": "$8.00",
                "period": "per month",
                "popular": True,
                "badge": "Most Popular · Bare Metal",
                "desc": "Engineered for high-traffic bare-metal dedicated servers requiring maximum performance.",
                "features": [
                    "Unlimited cPanel & WHM Accounts",
                    "Optimized for Multi-Core Dedicated Servers",
                    "Full Bare-Metal Root WHM Control",
                    "Official cPanel Updates & Fast Mirrors",
                    "Full Extension & Addon Plugin Support",
                    "Instant 60-Second Server Activation",
                    "Unlimited Free IP Migrations & Swaps"
                ],
                "btn_text": "Order cPanel Dedicated",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=2"
            }
        ],
        "faqs": [
            {
                "q": "How does LicenBase cPanel licensing work?",
                "a": "Our cPanel licenses operate via verified IP-binding technology. Once you purchase and bind your server's public IPv4 address, running our one-line installation command connects your server directly to our high-availability authentication cluster. Your cPanel & WHM installation recognizes the license as 100% active and authentic."
            },
            {
                "q": "Does this license include unlimited accounts?",
                "a": "Yes! Both VPS and Dedicated licenses allow you to create unlimited cPanel user accounts without any per-account tier caps or hidden surcharges."
            },
            {
                "q": "Can I receive official cPanel updates?",
                "a": "Yes. Your cPanel & WHM server will update directly from official vendor repository channels. You can run 'upcp' and receive the latest stable releases, security patches, and feature updates."
            },
            {
                "q": "What happens if I change my server IP?",
                "a": "You can change your registered server IP address anytime for free directly from your LicenBase client area with zero downtime."
            },
            {
                "q": "Can I convert an expired or trial cPanel installation?",
                "a": "Yes! If you already have cPanel installed and your trial or prior license expired, simply run our installation command and your server will immediately activate without data loss or reinstalling."
            },
            {
                "q": "What is the refund policy for cPanel licenses?",
                "a": "Because software licenses are digital products provisioned immediately upon order, all sales are strictly non-refundable once issued. Please review your server requirements before purchasing."
            }
        ],
        "related": [
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Accelerate WordPress and PHP up to 10x with drop-in Apache replacement.", "icon": "zap"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants, stabilize server resources, and prevent noisy neighbor crashes.", "icon": "shield-check"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "Complete AI-powered web application firewall and automated malware removal.", "icon": "lock"},
            {"title": "JetBackup 5", "price": "$1.50/mo", "url": "/jetbackup-license", "desc": "Enterprise automated incremental server backups to S3, Wasabi, or Google Cloud.", "icon": "database"}
        ],
        "articles": [
            {"title": "How to Install cPanel & WHM on AlmaLinux / Rocky Linux", "cat": "Installation Guide", "time": "4 min read", "desc": "Step-by-step guide to installing cPanel & WHM and activating your LicenBase license in under 5 minutes."},
            {"title": "How to Replace or Update Server IP on cPanel", "cat": "Troubleshooting", "time": "3 min read", "desc": "Learn how to update your server IP in the client portal and re-run verification with zero server downtime."},
            {"title": "Hardening cPanel & WHM Security Best Practices", "cat": "Server Optimization", "time": "6 min read", "desc": "Essential security checklist: 2FA, brute force protection (cPHulk), mod_security, and firewall tuning."}
        ]
    },
    {
        "filename": "litespeed-license.html",
        "slug": "litespeed",
        "title": "LiteSpeed Web Server License (2, 4, 8 & X Core)",
        "meta_desc": "Get genuine LiteSpeed Web Server licenses starting at $4.00/mo. Drop-in Apache replacement, LSCache acceleration, HTTP/3, and instant automated activation.",
        "badge": "Ultra-High Performance Web Server",
        "icon": "zap",
        "headline": "LiteSpeed Web Server Licenses",
        "headline_sub": "10x Faster PHP & WordPress Speeds.",
        "hero_desc": "Supercharge your hosting performance with genuine LiteSpeed Enterprise licenses. 100% compatible with Apache .htaccess, HTTP/3 QUIC support, and built-in LSCache acceleration.",
        "specs": ["Apache Drop-in Replacement", "LSCache Included", "HTTP/3 & QUIC Enabled", "DDoS Stream Filtering", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "LiteSpeed 2 Core",
                "price": "$4.00",
                "period": "per month",
                "popular": False,
                "badge": "Starter Servers",
                "desc": "Ideal for small to medium VPS servers running standard web hosting workloads.",
                "features": [
                    "Up to 2 CPU Cores Allocation",
                    "Unlimited Worker Processes",
                    "Full LSCache Plugin Support",
                    "HTTP/3 & QUIC Native Support",
                    "Apache Drop-In Compatibility",
                    "Instant Automatic Activation",
                    "Free Server IP Replacements"
                ],
                "btn_text": "Order 2 Core",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=3"
            },
            {
                "name": "LiteSpeed 4 Core",
                "price": "$7.50",
                "period": "per month",
                "popular": True,
                "badge": "Most Popular · High Traffic",
                "desc": "Optimized for high-concurrency production servers, WooCommerce, and agency nodes.",
                "features": [
                    "Up to 4 CPU Cores Allocation",
                    "Massive Concurrent Connections",
                    "Full E-Commerce Acceleration",
                    "Advanced DDoS Connection Throttling",
                    "Native cPanel / Plesk Integration",
                    "Instant 60-Second Setup",
                    "Unlimited Free IP Changes"
                ],
                "btn_text": "Order 4 Core",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=4"
            },
            {
                "name": "LiteSpeed 8 Core",
                "price": "$10.50",
                "period": "per month",
                "popular": False,
                "badge": "Heavy Workloads",
                "desc": "Built for dedicated servers and large VPS instances with heavy dynamic traffic.",
                "features": [
                    "Up to 8 CPU Cores Allocation",
                    "Enterprise Dynamic Caching",
                    "Maximum PHP Memory & Processors",
                    "High-Bandwidth Media Handling",
                    "Full SSL Handshake Offloading",
                    "Instant Automatic Provisioning",
                    "Free Technical Support"
                ],
                "btn_text": "Order 8 Core",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=5"
            },
            {
                "name": "LiteSpeed X Core",
                "price": "$11.50",
                "period": "per month",
                "popular": False,
                "badge": "Unlimited Cores",
                "desc": "Unrestricted CPU core license for top-tier bare-metal dedicated servers and clusters.",
                "features": [
                    "Unlimited CPU Cores Supported",
                    "Maximum Throughput & Zero Limits",
                    "Full Cluster & Cloud Capability",
                    "Enterprise LSCache Tuning",
                    "Priority Verification Failover",
                    "Instant License Issuance",
                    "Free IP Migration Anytime"
                ],
                "btn_text": "Order X Core",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=6"
            }
        ],
        "faqs": [
            {
                "q": "What is LiteSpeed Web Server and how does it replace Apache?",
                "a": "LiteSpeed Web Server (LSWS) is a high-performance, drop-in replacement for Apache. It reads Apache configuration files directly, supports .htaccess rules without changes, and delivers up to 10x faster static and dynamic response times."
            },
            {
                "q": "Can I upgrade my core license later?",
                "a": "Yes! You can upgrade from 2 Core to 4, 8, or X Core at any time with prorated billing directly in your client portal."
            },
            {
                "q": "Does LiteSpeed include the WordPress LSCache plugin?",
                "a": "Yes! All LicenBase LiteSpeed licenses support the official LSCache plugin for WordPress, Magento, PrestaShop, OpenCart, and Joomla with full server-level caching."
            },
            {
                "q": "How do I install LiteSpeed on cPanel or DirectAdmin?",
                "a": "Simply install the LiteSpeed WHM plugin or run our 1-command installer script. The script automatically handles registration and links with your web control panel."
            },
            {
                "q": "Are licenses refundable after purchase?",
                "a": "No. In accordance with our digital licensing terms, all purchases are non-refundable once issued because keys and IP activations are provisioned instantly."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Optimize server stability and isolate tenants for maximum security.", "icon": "shield-check"},
            {"title": "Imunify360", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "Automated security suite with proactive PHP defense and real-time scanning.", "icon": "lock"},
            {"title": "WHMCS License", "price": "$20.00 one-time", "url": "/whmcs-license", "desc": "Automate billing, client provisioning, and hosting support.", "icon": "credit-card"}
        ],
        "articles": [
            {"title": "How to Replace Apache with LiteSpeed in WHM", "cat": "Tutorial", "time": "3 min read", "desc": "Easy 5-minute migration from Apache to LiteSpeed Web Server with zero website downtime."},
            {"title": "Configuring LSCache for WordPress for 100/100 PageSpeed", "cat": "Performance", "time": "5 min read", "desc": "Mastering object cache, CSS/JS minification, and ESI caching on LiteSpeed servers."},
            {"title": "Troubleshooting LiteSpeed SSL and HTTP/3 QUIC Setup", "cat": "Troubleshooting", "time": "4 min read", "desc": "Verifying UDP port 443 firewall access and enabling HTTP/3 protocol across virtual hosts."}
        ]
    },
    {
        "filename": "plesk-license.html",
        "slug": "plesk",
        "title": "Plesk Control Panel License (VPS & Dedicated)",
        "meta_desc": "Get genuine Plesk Web Host Edition licenses for VPS ($2.50/mo) and Dedicated ($6.50/mo). Unlimited domains, WordPress Toolkit, and instant IP activation.",
        "badge": "Leading Multi-Cloud Control Panel",
        "icon": "layout-grid",
        "headline": "Plesk Web Host Edition Licenses",
        "headline_sub": "Intuitive Management for VPS & Dedicated.",
        "hero_desc": "Manage WordPress, Docker, Node.js, and multi-tenant hosting with Plesk Web Host Edition. Complete with WordPress Toolkit SE, automated SSL, and complete administrative control.",
        "specs": ["Unlimited Domains", "WordPress Toolkit", "Docker & Node.js Ready", "Free Let's Encrypt SSL", "Instant IP Delivery", "Free IP Changes"],
        "tiers": [
            {
                "name": "Plesk VPS Edition",
                "price": "$2.50",
                "period": "per month",
                "popular": False,
                "badge": "Cloud & VPS Instances",
                "desc": "Full Plesk Web Host Edition license tailored for Virtual Private Servers and cloud VMs.",
                "features": [
                    "Unlimited Domains & Subdomains",
                    "WordPress Toolkit Full Capabilities",
                    "Docker, Git & Node.js Extensions",
                    "Automated Let's Encrypt SSL Certificates",
                    "Complete Admin & Reseller Tools",
                    "Instant Automatic Provisioning",
                    "Unlimited Free IP Migrations"
                ],
                "btn_text": "Order Plesk VPS",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=7"
            },
            {
                "name": "Plesk Dedicated Edition",
                "price": "$6.50",
                "period": "per month",
                "popular": True,
                "badge": "Most Popular · Bare Metal",
                "desc": "Engineered for high-capacity dedicated servers running intensive web applications.",
                "features": [
                    "Unlimited Domains & Client Accounts",
                    "Uncapped Multi-Core Server Performance",
                    "Full Bare-Metal Root Control",
                    "Plesk Security Advisor & Firewall",
                    "Complete Extension Catalog Support",
                    "Instant 60-Second Server Activation",
                    "Free IP Migration & Expert Support"
                ],
                "btn_text": "Order Plesk Dedicated",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=8"
            }
        ],
        "faqs": [
            {
                "q": "What edition of Plesk is provided?",
                "a": "LicenBase provides the top-tier Plesk Web Host Edition, which grants unlimited domains, reseller accounts, and full access to WordPress Toolkit and developer extension modules."
            },
            {
                "q": "Does Plesk work on Ubuntu, Debian, AlmaLinux, and Windows?",
                "a": "Yes! Plesk supports all major Linux distributions (Ubuntu, Debian, AlmaLinux, Rocky Linux, RHEL) and Windows Server."
            },
            {
                "q": "Can I migrate my accounts from cPanel to Plesk?",
                "a": "Yes. Plesk includes a built-in Plesk Migrator extension that automatically imports cPanel backups, databases, and emails seamlessly."
            },
            {
                "q": "What is the policy regarding refunds?",
                "a": "As with all digital software licenses, purchases are immediate and non-refundable once activated."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Accelerate WordPress and dynamic PHP sites with LSCache.", "icon": "zap"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants, stabilize server resources, and prevent crashes.", "icon": "shield-check"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "Automated security suite with AI firewall and proactive malware defense.", "icon": "lock"}
        ],
        "articles": [
            {"title": "Installing Plesk on AlmaLinux 9 in 5 Minutes", "cat": "Installation Guide", "time": "4 min read", "desc": "A step-by-step walkthrough to installing Plesk Web Host Edition on modern Linux servers."},
            {"title": "Using Plesk WordPress Toolkit for Mass Management", "cat": "Management", "time": "5 min read", "desc": "How to clone, stage, update plugins, and harden security across dozens of WordPress sites."},
            {"title": "How to Re-IP a Plesk Server with Zero Downtime", "cat": "Troubleshooting", "time": "3 min read", "desc": "Guidelines on updating your server IP and running the licenbase_plesk activation tool."}
        ]
    },
    {
        "filename": "whmcs-license.html",
        "slug": "whmcs",
        "title": "WHMCS License (Owned One-Time & Monthly)",
        "meta_desc": "Buy genuine WHMCS licenses starting at $20.00 one-time. Complete hosting automation, unlimited clients, multi-currency billing, and instant digital delivery.",
        "badge": "Industry Leading Web Hosting Automation",
        "icon": "credit-card",
        "headline": "Genuine WHMCS Licenses",
        "headline_sub": "Automate Billing, Provisioning & Support.",
        "hero_desc": "Run your web hosting or SaaS company on autopilot. Complete client management, automated invoice generation, payment gateways, and automated server provisioning.",
        "specs": ["Unlimited Clients", "All Payment Gateways", "Automated Provisioning", "Support Ticket Desk", "Domain Registrar APIs", "No Per-Client Limits"],
        "tiers": [
            {
                "name": "WHMCS Lifetime Owned",
                "price": "$20.00",
                "period": "one-time payment",
                "popular": True,
                "badge": "Best Value · No Monthly Fees",
                "desc": "Pay once and own your WHMCS licensing without recurring monthly bills or client tier penalties.",
                "features": [
                    "Unlimited Active Clients & Invoices",
                    "All Payment Gateways Included (Stripe, PayPal, Crypto)",
                    "Automated cPanel, Plesk & DirectAdmin Provisioning",
                    "Complete Support Ticket System & Knowledgebase",
                    "Domain Registrar Integrations (Namecheap, ResellerClub)",
                    "No Branding / Powered-By Links",
                    "Instant Domain & IP Activation"
                ],
                "btn_text": "Order WHMCS Owned",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=9"
            },
            {
                "name": "WHMCS Monthly License",
                "price": "$4.00",
                "period": "per month",
                "popular": False,
                "badge": "Pay As You Go",
                "desc": "Flexible monthly subscription for growing hosting providers and development agencies.",
                "features": [
                    "Unlimited Clients & Invoicing",
                    "Full Automated Provisioning Modules",
                    "Payment Gateways & Tax Management",
                    "Integrated Support Desk",
                    "Official WHMCS Updates",
                    "Instant Automatic Provisioning",
                    "Cancel Anytime"
                ],
                "btn_text": "Order WHMCS Monthly",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=10"
            }
        ],
        "faqs": [
            {
                "q": "What is the difference between Owned One-Time and Monthly WHMCS?",
                "a": "The Owned One-Time license is paid once ($20.00) and remains active on your domain with no recurring monthly licensing fees. The monthly option is a flexible pay-as-you-go plan."
            },
            {
                "q": "Are there any limits on the number of clients I can manage?",
                "a": "None! Unlike official retail tiers which cap you at 250 or 1000 clients, LicenBase WHMCS licenses allow unlimited clients without tiered upcharges."
            },
            {
                "q": "Can I install third-party WHMCS modules and themes?",
                "a": "Yes, 100%. LicenBase WHMCS licenses are compatible with all standard WHMCS themes, payment gateway add-ons, registrar modules, and provisioning hooks."
            },
            {
                "q": "How do I activate WHMCS on my server?",
                "a": "Simply install WHMCS on your domain and run our one-line activation script on your server or input the license key provided in your dashboard."
            },
            {
                "q": "Is this purchase refundable?",
                "a": "No. All license sales are digital and final upon delivery in accordance with our strict non-refundable policy."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "Virtualizor License", "price": "$3.50/mo", "url": "/virtualizor-license", "desc": "Powerful VPS management panel with seamless WHMCS automation.", "icon": "cpu"},
            {"title": "Softaculous Auto-Installer", "price": "$1.00/mo", "url": "/softaculous-license", "desc": "450+ 1-click script auto-installations for cPanel and DirectAdmin.", "icon": "layers"},
            {"title": "SitePad Website Builder", "price": "$1.50/mo", "url": "/sitepad-license", "desc": "1000+ drag-and-drop website templates for your hosting clients.", "icon": "globe"}
        ],
        "articles": [
            {"title": "Setting Up Automated cPanel Provisioning in WHMCS", "cat": "Automation Guide", "time": "5 min read", "desc": "How to connect WHM API tokens to WHMCS for instant package setup upon invoice payment."},
            {"title": "How to Configure Payment Gateways in WHMCS", "cat": "Billing Setup", "time": "4 min read", "desc": "Step-by-step setup for Stripe, PayPal Checkout, and automated recurring credit card billing."},
            {"title": "Securing Your WHMCS Installation Checklist", "cat": "Security", "time": "6 min read", "desc": "Moving configuration files outside docroot, IP restricting admin access, and enabling 2FA."}
        ]
    },
    {
        "filename": "cloudlinux-license.html",
        "slug": "cloudlinux",
        "title": "CloudLinux OS License",
        "meta_desc": "Buy genuine CloudLinux OS licenses for $4.00/mo. Isolate tenants with CageFS, control CPU/RAM with LVE Manager, and secure multi-tenant hosting servers.",
        "badge": "The #1 Operating System for Web Hosting",
        "icon": "shield-check",
        "headline": "CloudLinux OS Licenses",
        "headline_sub": "Rock-Solid Multi-Tenant Server Isolation.",
        "hero_desc": "Convert CentOS, AlmaLinux, or RHEL into a bulletproof web hosting platform. Limit tenant resource spikes, virtualize user filesystems with CageFS, and offer multiple hardened PHP versions.",
        "specs": ["CageFS User Isolation", "LVE CPU & RAM Limits", "PHP / Node / Python Selector", "MySQL Governor", "Instant IP Delivery", "Free IP Swaps"],
        "tiers": [
            {
                "name": "CloudLinux Shared License",
                "price": "$4.00",
                "period": "per month",
                "popular": True,
                "badge": "Full Server License",
                "desc": "Complete CloudLinux OS license for any VPS or Bare-Metal Dedicated Server.",
                "features": [
                    "LVE Manager (Per-User CPU, RAM & IO Limits)",
                    "CageFS Virtualized User Isolation",
                    "Hardened PHP Selector (PHP 5.6 through 8.4)",
                    "MySQL Governor (Prevent Database Server Slowdowns)",
                    "Python & Node.js App Selectors",
                    "Instant Automatic IP Activation",
                    "Official CloudLinux Repositories & Kernels"
                ],
                "btn_text": "Order CloudLinux License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=11"
            }
        ],
        "faqs": [
            {
                "q": "What is CloudLinux OS and why do I need it?",
                "a": "CloudLinux OS turns standard Linux into a multi-tenant hosting operating system. By using Lightweight Virtual Environments (LVE), no single website can crash your server by consuming all CPU or RAM."
            },
            {
                "q": "Can I convert an existing CentOS, AlmaLinux, or Rocky Linux server?",
                "a": "Yes! You can convert your live server in-place without losing websites, data, or cPanel configurations using the official 'cldeploy' script and LicenBase activation command."
            },
            {
                "q": "Does this support CageFS and PHP Selector?",
                "a": "Yes, 100%. All CloudLinux OS features including CageFS, PHP Selector, Python/Node.js Selector, and MySQL Governor are fully operational."
            },
            {
                "q": "What happens if I change my server IP?",
                "a": "You can change your IP anytime in the LicenBase client dashboard for free and re-run our activation command in seconds."
            },
            {
                "q": "Are licenses refundable?",
                "a": "No, all digital licenses are non-refundable once provisioned."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "AI firewall, proactive defense, and automatic malware cleanup.", "icon": "lock"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"},
            {"title": "JetBackup 5", "price": "$1.50/mo", "url": "/jetbackup-license", "desc": "Automated incremental backup manager for hosting providers.", "icon": "database"}
        ],
        "articles": [
            {"title": "Converting AlmaLinux 8/9 to CloudLinux OS", "cat": "Installation", "time": "5 min read", "desc": "How to convert an active cPanel or DirectAdmin server to CloudLinux with zero downtime."},
            {"title": "Best Practices for LVE Resource Allocations", "cat": "Configuration", "time": "6 min read", "desc": "Recommended CPU, RAM, IOPS, and EP limits for shared hosting and reseller accounts."},
            {"title": "Deploying CageFS and PHP Selector Step-by-Step", "cat": "Security", "time": "4 min read", "desc": "Isolate user directories and install multiple secure PHP versions with ease."}
        ]
    },
    {
        "filename": "virtualizor-license.html",
        "slug": "virtualizor",
        "title": "Virtualizor VPS Panel License",
        "meta_desc": "Buy genuine Virtualizor licenses for $3.50/mo. Manage KVM, OpenVZ, and LXC virtualization with automated OS templates, WHMCS integration, and instant activation.",
        "badge": "Enterprise Hypervisor & Cloud VPS Manager",
        "icon": "cpu",
        "headline": "Virtualizor VPS Panel Licenses",
        "headline_sub": "Automated Virtual Machine Orchestration.",
        "hero_desc": "Manage VPS nodes with full automation. Deploy KVM, OpenVZ, LXC, and Xen virtual machines, offer client self-service panels, and connect directly to WHMCS for auto-provisioning.",
        "specs": ["KVM, LXC & OpenVZ Support", "Automated OS Templates", "WHMCS Module Integration", "No-VNC & HTML5 Console", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "Virtualizor Node License",
                "price": "$3.50",
                "period": "per month",
                "popular": True,
                "badge": "Full Hypervisor Node",
                "desc": "Unlimited VPS instances per server node with full hypervisor automation.",
                "features": [
                    "Supports KVM, OpenVZ 7, LXC & Xen Hypervisors",
                    "Unlimited Virtual Machines on Node",
                    "Hundreds of Automated OS Templates & ISOs",
                    "Official WHMCS Auto-Provisioning Module",
                    "Automated IP Pool & Network Management",
                    "HTML5 VNC & Remote Management Console",
                    "Instant 60-Second Server Activation"
                ],
                "btn_text": "Order Virtualizor License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=12"
            }
        ],
        "faqs": [
            {
                "q": "How many virtual machines can I create with this license?",
                "a": "Unlimited! One LicenBase Virtualizor license covers the entire physical server node, allowing you to create as many VPS instances as your hardware can handle."
            },
            {
                "q": "Does Virtualizor integrate with WHMCS?",
                "a": "Yes! Virtualizor provides an official, automated WHMCS module that automatically creates, suspends, reboots, and terminates VPS orders upon invoice payment."
            },
            {
                "q": "Which operating systems can be used as the host node?",
                "a": "Virtualizor can be installed on AlmaLinux, CentOS, Rocky Linux, Ubuntu, and Debian bare-metal servers."
            },
            {
                "q": "What is the refund policy?",
                "a": "All digital license activations are strictly non-refundable once delivered."
            }
        ],
        "related": [
            {"title": "WHMCS License", "price": "$20.00 one-time", "url": "/whmcs-license", "desc": "Complete billing automation and client portal for VPS providers.", "icon": "credit-card"},
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel for your VPS clients.", "icon": "server"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants and stabilize server resources.", "icon": "shield-check"},
            {"title": "SitePad Website Builder", "price": "$1.50/mo", "url": "/sitepad-license", "desc": "1000+ drag-and-drop templates for hosting clients.", "icon": "globe"}
        ],
        "articles": [
            {"title": "How to Install Virtualizor KVM on AlmaLinux 9", "cat": "Installation", "time": "5 min read", "desc": "Step-by-step setup of KVM virtualization, bridge networking, and storage pools."},
            {"title": "Connecting Virtualizor with WHMCS for VPS Automation", "cat": "Automation", "time": "4 min read", "desc": "Setting up server groups, API keys, and automated product blueprints in WHMCS."},
            {"title": "Configuring IPv4 & IPv6 Subnet Pools in Virtualizor", "cat": "Networking", "time": "4 min read", "desc": "Easily assign public IP blocks to guest virtual machines automatically."}
        ]
    },
    {
        "filename": "sitepad-license.html",
        "slug": "sitepad",
        "title": "SitePad Website Builder License",
        "meta_desc": "Buy genuine SitePad Website Builder licenses for $1.50/mo. 1,000+ responsive themes, drag & drop editor, cPanel/Plesk integration, and instant activation.",
        "badge": "No-Code Website Builder for Hosting Providers",
        "icon": "globe",
        "headline": "SitePad Website Builder Licenses",
        "headline_sub": "1,000+ Stunning Themes for Your Hosting Clients.",
        "hero_desc": "Give your hosting clients a world-class drag-and-drop website editor. Over 1,000 professional responsive templates, 100+ widgets, and seamless integration into cPanel, Plesk, DirectAdmin, and Webuzo.",
        "specs": ["1,000+ Themes Included", "100+ Visual Drag-and-Drop Widgets", "Direct cPanel & Plesk Integration", "Static HTML Output (Super Fast)", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "SitePad Server License",
                "price": "$1.50",
                "period": "per month",
                "popular": True,
                "badge": "Unlimited Websites & Users",
                "desc": "Covers all hosting accounts and websites on your cPanel, Plesk, or DirectAdmin server.",
                "features": [
                    "Unlimited Client Websites & Domains",
                    "1,000+ Responsive Premium Themes",
                    "100+ Interactive Widgets (Forms, Galleries, Sliders)",
                    "Publishes Static HTML/CSS for 100% Speed & Security",
                    "cPanel, Plesk, DirectAdmin & Webuzo Plugin Support",
                    "Instant Automatic IP Activation",
                    "Free Migration & IP Updates"
                ],
                "btn_text": "Order SitePad License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=13"
            }
        ],
        "faqs": [
            {
                "q": "How does SitePad work on my web hosting server?",
                "a": "SitePad integrates directly into your cPanel or Plesk control panel. Your clients can design professional websites using an intuitive drag-and-drop editor without needing coding knowledge."
            },
            {
                "q": "Does SitePad output dynamic code or static HTML?",
                "a": "SitePad publishes static HTML/CSS/JS files directly to the client's public_html folder. This makes SitePad sites load extraordinarily fast and eliminates common CMS security vulnerabilities."
            },
            {
                "q": "How many users on my server can use SitePad?",
                "a": "Unlimited! One license covers every cPanel or hosting account hosted on that server."
            },
            {
                "q": "Is this license non-refundable?",
                "a": "Yes. All digital license purchases are immediate and non-refundable once activated."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "Softaculous Auto-Installer", "price": "$1.00/mo", "url": "/softaculous-license", "desc": "450+ 1-click script auto-installations for cPanel.", "icon": "layers"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"},
            {"title": "WHMCS License", "price": "$20.00 one-time", "url": "/whmcs-license", "desc": "Complete billing automation and client portal.", "icon": "credit-card"}
        ],
        "articles": [
            {"title": "Installing SitePad on cPanel & WHM Servers", "cat": "Installation", "time": "3 min read", "desc": "Enable the SitePad builder icon for all cPanel users in under 3 minutes."},
            {"title": "How SitePad Generates High-Speed Static Websites", "cat": "Overview", "time": "4 min read", "desc": "Why static HTML architecture out-performs WordPress for simple business sites."},
            {"title": "Customizing Default SitePad Themes for Your Brand", "cat": "Branding", "time": "4 min read", "desc": "Personalize default template categories and feature sets for your agency."}
        ]
    },
    {
        "filename": "whmreseller-license.html",
        "slug": "whmreseller",
        "title": "WHMReseller License",
        "meta_desc": "Buy genuine WHMReseller licenses for $1.50/mo. Enable multi-level Master and Alpha reseller tiers in cPanel & WHM with instant automated activation.",
        "badge": "Multi-Level Master & Alpha Reseller Plugin for WHM",
        "icon": "users",
        "headline": "WHMReseller Plugin Licenses",
        "headline_sub": "Unlock Master & Alpha Reseller Capabilities in WHM.",
        "hero_desc": "Expand your hosting revenue by offering Master Reseller and Alpha Reseller packages. Allow your resellers to create sub-resellers and sub-cPanel accounts safely with automated ACL permissions.",
        "specs": ["Master & Alpha Reseller Tiers", "Full cPanel & WHM Compatibility", "Automated Backup Migrator", "ACL Permission Limits", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "WHMReseller Pro License",
                "price": "$1.50",
                "period": "per month",
                "popular": True,
                "badge": "Full Server License",
                "desc": "Enables Alpha, Master, and standard reseller tiers across your entire WHM server.",
                "features": [
                    "Create Multi-Level Alpha & Master Resellers",
                    "Allow Resellers to Resell Sub-Reseller Accounts",
                    "Built-In Reseller Backup & Account Transfer Tool",
                    "Fine-Grained Account Limit & ACL Enforcement",
                    "Direct Integration into WHM Root Interface",
                    "Instant Automatic IP Activation",
                    "Free IP Migration Anytime"
                ],
                "btn_text": "Order WHMReseller",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=14"
            }
        ],
        "faqs": [
            {
                "q": "What is WHMReseller?",
                "a": "WHMReseller is the most popular WHM plugin that allows hosting providers to sell Master Resellers and Alpha Resellers, giving resellers the ability to create secondary reseller accounts."
            },
            {
                "q": "Does WHMReseller interfere with official cPanel updates?",
                "a": "No. WHMReseller uses official WHM API hooks and works smoothly across all modern cPanel & WHM releases."
            },
            {
                "q": "Can I transfer accounts between resellers easily?",
                "a": "Yes! WHMReseller includes a built-in account manager and migration utility designed specifically for reseller packages."
            },
            {
                "q": "Are licenses refundable?",
                "a": "No, all digital licenses are strictly non-refundable once delivered."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate reseller accounts and stabilize server resources.", "icon": "shield-check"},
            {"title": "WHMCS License", "price": "$20.00 one-time", "url": "/whmcs-license", "desc": "Automate billing, client provisioning, and reseller packages.", "icon": "credit-card"},
            {"title": "Softaculous Auto-Installer", "price": "$1.00/mo", "url": "/softaculous-license", "desc": "450+ 1-click script auto-installations for cPanel.", "icon": "layers"}
        ],
        "articles": [
            {"title": "Installing and Configuring WHMReseller on WHM", "cat": "Installation", "time": "3 min read", "desc": "Quick guide to deploying WHMReseller and configuring Master Reseller packages."},
            {"title": "Setting Up Reseller Account Limits and ACL Protections", "cat": "Configuration", "time": "4 min read", "desc": "Prevent resellers from overselling disk space or manipulating root settings."},
            {"title": "How to Automate WHMReseller Products in WHMCS", "cat": "Billing Integration", "time": "5 min read", "desc": "Connect WHMCS product packages directly to WHMReseller tiers for automated setup."}
        ]
    },
    {
        "filename": "softaculous-license.html",
        "slug": "softaculous",
        "title": "Softaculous Auto-Installer License",
        "meta_desc": "Buy genuine Softaculous Premium licenses for $1.00/mo. 450+ 1-click script auto-installations, WordPress staging, automated backups, and instant activation.",
        "badge": "The Premier 1-Click Application Auto-Installer",
        "icon": "layers",
        "headline": "Softaculous Premium Licenses",
        "headline_sub": "450+ 1-Click Scripts for WordPress, Joomla & More.",
        "hero_desc": "The indispensable auto-installer for web hosting providers. Empower your users to install, clone, stage, and auto-update 450+ web scripts including WordPress, Laravel, PrestaShop, and Node.js.",
        "specs": ["450+ 1-Click Scripts", "WordPress Staging & Cloning", "Automated Script Updates", "cPanel, Plesk & DirectAdmin Ready", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "Softaculous Premium License",
                "price": "$1.00",
                "period": "per month",
                "popular": True,
                "badge": "Full Server License",
                "desc": "Unlimited script installations for all users on your hosting server.",
                "features": [
                    "450+ Web Applications (WordPress, Drupal, Magento, etc.)",
                    "WordPress Auto-Update & Staging Environment",
                    "Automated Backup & Restore to Google Drive / Dropbox / S3",
                    "Compatible with cPanel, Plesk, DirectAdmin & Webuzo",
                    "Custom Script Installer & Package Manager",
                    "Instant Automatic IP Activation",
                    "Unlimited Free Server IP Replacements"
                ],
                "btn_text": "Order Softaculous License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=15"
            }
        ],
        "faqs": [
            {
                "q": "What is Softaculous Premium?",
                "a": "Softaculous Premium is the industry-standard auto-installer that allows web hosting customers to install, upgrade, and manage 450+ popular web applications in just one click."
            },
            {
                "q": "Can clients create WordPress staging environments with Softaculous?",
                "a": "Yes! Softaculous includes full WordPress cloning, staging, and push-to-live features, making development easy for your clients."
            },
            {
                "q": "Does one license cover all cPanel accounts on my server?",
                "a": "Yes. One Softaculous server license covers every domain, sub-domain, and hosting account on that server."
            },
            {
                "q": "Is this license non-refundable?",
                "a": "Yes, all digital licenses are non-refundable once activated."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Accelerate WordPress with LSCache acceleration.", "icon": "zap"},
            {"title": "SitePad Website Builder", "price": "$1.50/mo", "url": "/sitepad-license", "desc": "1000+ drag-and-drop templates for hosting clients.", "icon": "globe"},
            {"title": "JetBackup 5", "price": "$1.50/mo", "url": "/jetbackup-license", "desc": "Automated incremental backup manager for hosting providers.", "icon": "database"}
        ],
        "articles": [
            {"title": "Installing Softaculous on cPanel & WHM in 2 Minutes", "cat": "Installation", "time": "2 min read", "desc": "Single command installation to deploy Softaculous across all WHM users."},
            {"title": "Enabling Automated WordPress Backups & Staging", "cat": "Feature Guide", "time": "4 min read", "desc": "How clients can set up automated nightly backups before plugin updates."},
            {"title": "Managing PHP Extension Dependencies for 1-Click Apps", "cat": "Troubleshooting", "time": "4 min read", "desc": "Ensuring all required PHP extensions are active for popular application scripts."}
        ]
    },
    {
        "filename": "jetbackup-license.html",
        "slug": "jetbackup",
        "title": "JetBackup 5 License",
        "meta_desc": "Buy genuine JetBackup 5 licenses for $1.50/mo. Enterprise automated incremental backups to S3, Wasabi, and FTP with self-service client restore.",
        "badge": "Enterprise Server Backup & Disaster Recovery",
        "icon": "database",
        "headline": "JetBackup 5 Server Licenses",
        "headline_sub": "Blazing Fast Incremental Backups & Restores.",
        "hero_desc": "Protect your hosting clients with enterprise-grade automated incremental backups. Offload snapshots to Amazon S3, Wasabi, Google Drive, or SSH/FTP destinations with granular self-service user restores.",
        "specs": ["Block-Level Incremental Backups", "S3, Wasabi, FTP & Cloud Destinations", "Self-Service cPanel / DirectAdmin Restore", "Point-in-Time Database Rollback", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "JetBackup 5 Server License",
                "price": "$1.50",
                "period": "per month",
                "popular": True,
                "badge": "Full Server License",
                "desc": "Comprehensive backup automation for your cPanel, DirectAdmin, or Linux server.",
                "features": [
                    "Fast Block-Level Incremental Backups (Save 80%+ Storage)",
                    "Unlimited Destination Endpoints (S3, Wasabi, B2, SSH, FTP)",
                    "Granular Self-Service Single File & Database Restores",
                    "Point-in-Time Automated Snapshot Schedules",
                    "cPanel & DirectAdmin Native End-User UI",
                    "Instant Automatic IP Activation",
                    "Free Server IP Transfers"
                ],
                "btn_text": "Order JetBackup License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=16"
            }
        ],
        "faqs": [
            {
                "q": "What makes JetBackup 5 superior to standard cPanel backups?",
                "a": "JetBackup 5 utilizes modern block-level incremental snapshot technology, reducing server CPU/IO overhead by up to 80% and drastically cutting remote storage costs."
            },
            {
                "q": "Can end-users restore their own files and databases?",
                "a": "Yes! JetBackup embeds directly into the client's cPanel or DirectAdmin interface, letting them restore single files, SSL certificates, emails, or databases in seconds without opening a support ticket."
            },
            {
                "q": "Which remote storage providers are supported?",
                "a": "JetBackup 5 natively supports Amazon S3, Wasabi, Backblaze B2, Google Drive, Dropbox, SFTP, and local/NFS mounts."
            },
            {
                "q": "Is this purchase refundable?",
                "a": "No, all digital licenses are non-refundable once activated."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants and stabilize server resources.", "icon": "shield-check"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "AI firewall, proactive defense, and automatic malware cleanup.", "icon": "lock"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"}
        ],
        "articles": [
            {"title": "Configuring Wasabi / S3 Storage Destinations in JetBackup 5", "cat": "Configuration", "time": "4 min read", "desc": "Step-by-step setup of cost-effective cloud object storage for incremental backups."},
            {"title": "Setting Up Automated Retention Rules and Snapshot Schedules", "cat": "Best Practices", "time": "5 min read", "desc": "How to schedule daily, weekly, and monthly backup rotations with minimal IO."},
            {"title": "Disaster Recovery: Full Server Bare-Metal Restore with JetBackup", "cat": "Recovery", "time": "6 min read", "desc": "Restoring an entire server fleet to a new server IP following hardware failure."}
        ]
    },
    {
        "filename": "imunify360-license.html",
        "slug": "imunify360",
        "title": "Imunify360 Security Suite License",
        "meta_desc": "Buy genuine Imunify360 licenses for $1.50/mo. Multi-layered AI security, automated malware scanner & cleanup, proactive PHP defense, and instant activation.",
        "badge": "Complete Multi-Layered Linux Web Server Security",
        "icon": "lock",
        "headline": "Imunify360 Security Licenses",
        "headline_sub": "Automated Malware Scanner & AI Web Application Firewall.",
        "hero_desc": "Defend your Linux web servers against hackers, brute-force attacks, and malware. Complete with artificial intelligence WAF, proactive PHP script defense, automated malware disinfection, and herd immunity.",
        "specs": ["AI-Powered Web Application Firewall", "Real-Time Automated Malware Cleanup", "Proactive PHP Script Defense", "Brute-Force & Botnet Shield", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "Imunify360 Unlimited",
                "price": "$1.50",
                "period": "per month",
                "popular": True,
                "badge": "Unlimited Users & Domains",
                "desc": "Full enterprise security suite for your cPanel, Plesk, DirectAdmin, or Linux server.",
                "features": [
                    "Automated Real-Time Malware Scanner & Cleanup",
                    "AI Web Application Firewall (WAF) & DoS Protection",
                    "Proactive Defense (Blocks Zero-Day PHP Exploits)",
                    "Intrusion Detection & Brute-Force Prevention (IDS/IPS)",
                    "Reputation Management & Google Blacklist Protection",
                    "Instant Automatic IP Activation",
                    "Unlimited Free IP Migrations"
                ],
                "btn_text": "Order Imunify360",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=17"
            }
        ],
        "faqs": [
            {
                "q": "What is Imunify360 and how does it protect my server?",
                "a": "Imunify360 is an all-in-one automated security suite developed specifically for Linux web hosting servers. It combines an advanced AI firewall, proactive PHP script analysis, automated malware cleanup, and reputation management into a single dashboard."
            },
            {
                "q": "Does Imunify360 automatically clean infected files without breaking websites?",
                "a": "Yes! Imunify360's automated malware cleanup surgically removes malicious code snippets from infected WordPress/PHP files while preserving the legitimate code."
            },
            {
                "q": "How does Proactive Defense work?",
                "a": "Proactive Defense inspects PHP script execution in real-time at the opcode level. It detects and blocks zero-day exploits before they can execute, even if the vulnerability is not yet known in signature databases."
            },
            {
                "q": "What is the policy on refunds?",
                "a": "All software licenses on LicenBase are strictly non-refundable once activated."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants, stabilize server resources, and prevent crashes.", "icon": "shield-check"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"},
            {"title": "JetBackup 5", "price": "$1.50/mo", "url": "/jetbackup-license", "desc": "Automated incremental backup manager for hosting providers.", "icon": "database"}
        ],
        "articles": [
            {"title": "Deploying Imunify360 on cPanel & WHM in 3 Minutes", "cat": "Installation", "time": "3 min read", "desc": "One-command deployment and initial firewall tuning guide."},
            {"title": "How Proactive Defense Stops Zero-Day WordPress Exploits", "cat": "Security Architecture", "time": "5 min read", "desc": "Understanding opcode execution analysis and behavior-based attack prevention."},
            {"title": "Configuring Automated Malware Disinfection Policies", "cat": "Best Practices", "time": "4 min read", "desc": "Automating real-time background scans and cleaning notifications."}
        ]
    },
    {
        "filename": "webuzo-license.html",
        "slug": "webuzo",
        "title": "Webuzo Control Panel License",
        "meta_desc": "Buy genuine Webuzo Control Panel licenses for $4.00/mo. Multi-user hosting control panel, Apache/Nginx/LiteSpeed support, 1-click apps, and instant activation.",
        "badge": "Modern Multi-User Cloud Web Hosting Control Panel",
        "icon": "layout-dashboard",
        "headline": "Webuzo Control Panel Licenses",
        "headline_sub": "Lightweight, Fast & Feature-Rich Hosting Management.",
        "hero_desc": "Deploy a lightning-fast, modern control panel on any Linux VPS or dedicated server. Supports multi-user shared hosting, reseller management, multi-PHP selector, Nginx reverse proxy, and 1-click application installers.",
        "specs": ["Multi-User & Reseller Hosting", "Apache, Nginx & LiteSpeed Support", "Multi-PHP Selector (5.6 - 8.4)", "Integrated 1-Click Apps", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "Webuzo Premium License",
                "price": "$4.00",
                "period": "per month",
                "popular": True,
                "badge": "Unlimited Users & Domains",
                "desc": "Complete enterprise Webuzo control panel for any VPS or Bare-Metal Dedicated Server.",
                "features": [
                    "Unlimited User Accounts & Domains",
                    "Full Reseller & Admin Management Tiers",
                    "Apache, Nginx, LiteSpeed & OpenLiteSpeed Web Server",
                    "Multi-PHP Selector with Custom Extensions",
                    "Automated Let's Encrypt SSL Certificates",
                    "Instant Automatic IP Activation",
                    "Free Server IP Replacements"
                ],
                "btn_text": "Order Webuzo License",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=18"
            }
        ],
        "faqs": [
            {
                "q": "What is Webuzo Control Panel?",
                "a": "Webuzo is a modern multi-user hosting control panel built by the creators of Softaculous. It provides an intuitive interface for managing domains, emails, databases, and web servers on Linux servers."
            },
            {
                "q": "Can Webuzo import existing cPanel account backups?",
                "a": "Yes! Webuzo has a built-in cPanel migration tool that imports cPanel cpmove backups with emails, databases, and DNS zones intact."
            },
            {
                "q": "Which web servers are supported in Webuzo?",
                "a": "Webuzo supports Apache, Nginx reverse proxy, Nginx standalone, and LiteSpeed / OpenLiteSpeed."
            },
            {
                "q": "What is the policy regarding refunds?",
                "a": "All digital software licenses are strictly non-refundable once delivered."
            }
        ],
        "related": [
            {"title": "Softaculous Auto-Installer", "price": "$1.00/mo", "url": "/softaculous-license", "desc": "450+ 1-click script auto-installations.", "icon": "layers"},
            {"title": "SitePad Website Builder", "price": "$1.50/mo", "url": "/sitepad-license", "desc": "1000+ drag-and-drop templates for hosting clients.", "icon": "globe"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"},
            {"title": "WHMCS License", "price": "$20.00 one-time", "url": "/whmcs-license", "desc": "Automate billing, client provisioning, and hosting support.", "icon": "credit-card"}
        ],
        "articles": [
            {"title": "How to Install Webuzo on AlmaLinux 9 in 5 Minutes", "cat": "Installation Guide", "time": "3 min read", "desc": "Quick deployment guide for installing Webuzo on a fresh VPS."},
            {"title": "Migrating cPanel Accounts to Webuzo Seamlessly", "cat": "Migration", "time": "5 min read", "desc": "Using the built-in cpmove restoration tool to transfer client accounts."},
            {"title": "Configuring Nginx Reverse Proxy with Apache on Webuzo", "cat": "Performance", "time": "4 min read", "desc": "Boost dynamic website speed with Nginx caching and Apache backend."}
        ]
    },
    {
        "filename": "wp-squared-license.html",
        "slug": "wpsquared",
        "title": "WP Squared (WordPress Hosting Platform by cPanel)",
        "meta_desc": "Buy genuine WP Squared licenses for $4.00/mo. Native WordPress hosting control panel engineered by cPanel, isolated tenants, WP-CLI, and instant IP activation.",
        "badge": "Turnkey Enterprise WordPress Hosting Platform by cPanel",
        "icon": "layout",
        "headline": "WP Squared Platform Licenses",
        "headline_sub": "Engineered by cPanel for Dedicated WordPress Hosting.",
        "hero_desc": "Deliver managed WordPress hosting with unmatched speed and simplicity. Built by cPanel, WP Squared provides full containerized tenant isolation, native WP-CLI tools, automated SSL, and 1-click WordPress staging.",
        "specs": ["Dedicated WordPress Architecture", "Containerized User Isolation", "Native WP-CLI & Staging", "Automated SSL & Security", "Instant IP Delivery", "Free IP Transfers"],
        "tiers": [
            {
                "name": "WP Squared Enterprise",
                "price": "$4.00",
                "period": "per month",
                "popular": True,
                "badge": "Unlimited WordPress Instances",
                "desc": "Complete WP Squared server license for managed WordPress hosting providers and agencies.",
                "features": [
                    "Engineered by cPanel Specifically for WordPress",
                    "Automated WordPress Installation & Smart Updates",
                    "Native 1-Click Staging & Cloning Environments",
                    "Built-In WP-CLI and Developer Tooling",
                    "Isolated Multi-Tenant Security Containerization",
                    "Instant Automatic IP Activation",
                    "Unlimited Free Server IP Replacements"
                ],
                "btn_text": "Order WP Squared",
                "btn_link": "https://dashboard.licenbase.com/cart.php?a=add&pid=19"
            }
        ],
        "faqs": [
            {
                "q": "What is WP Squared?",
                "a": "WP Squared is a dedicated WordPress hosting platform developed by cPanel. It simplifies server management by focusing purely on WordPress performance, isolation, automated updates, and ease of use."
            },
            {
                "q": "Does WP Squared require standard cPanel to be installed?",
                "a": "No. WP Squared is a standalone, lightweight server operating environment designed specifically for hosting WordPress websites without the bloat of traditional multi-purpose panels."
            },
            {
                "q": "Are automatic WordPress core and plugin updates supported?",
                "a": "Yes! WP Squared includes smart update features that test updates in an isolated staging clone before deploying them to your live site."
            },
            {
                "q": "What is the policy regarding refunds?",
                "a": "All digital software license sales on LicenBase are final and strictly non-refundable upon delivery."
            }
        ],
        "related": [
            {"title": "cPanel & WHM License", "price": "From $4.00/mo", "url": "/cpanel-license", "desc": "Industry leading hosting control panel with unlimited accounts.", "icon": "server"},
            {"title": "LiteSpeed Web Server", "price": "From $4.00/mo", "url": "/litespeed-license", "desc": "Ultra-fast Apache drop-in replacement with LSCache acceleration.", "icon": "zap"},
            {"title": "Imunify360 Security", "price": "$1.50/mo", "url": "/imunify360-license", "desc": "AI firewall, proactive defense, and automatic malware cleanup.", "icon": "lock"},
            {"title": "CloudLinux OS", "price": "$4.00/mo", "url": "/cloudlinux-license", "desc": "Isolate tenants, stabilize server resources, and prevent crashes.", "icon": "shield-check"}
        ],
        "articles": [
            {"title": "Getting Started with WP Squared on AlmaLinux 9", "cat": "Installation Guide", "time": "4 min read", "desc": "Complete walkthrough of installing WP Squared and launching your first managed WP instance."},
            {"title": "Using WP Squared Smart Updates & Staging", "cat": "Feature Guide", "time": "5 min read", "desc": "Automate plugin updates safely with visual comparison checks."},
            {"title": "WP-CLI Command Line Mastery for Agencies", "cat": "Developer Guide", "time": "5 min read", "desc": "Automating bulk site maintenance, database search-replaces, and user creation via CLI."}
        ]
    }
]

def generate_page(p):
    tiers_html = ""
    grid_cols = "md:grid-cols-2" if len(p["tiers"]) == 2 else ("md:grid-cols-2 lg:grid-cols-4" if len(p["tiers"]) == 4 else "max-w-xl mx-auto")
    
    if len(p["tiers"]) == 4:
        # 3 standard tiers on top + 1 wide enterprise tier below for X-Core
        top_tiers = p["tiers"][:3]
        x_tier = p["tiers"][3]
        
        top_cards_html = ""
        for t in top_tiers:
            pop_border = "border-2 border-brand shadow-xl relative scale-[1.02] z-10" if t["popular"] else "border border-gray-200 shadow-md"
            pop_badge = f'<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">⭐ Most Popular</div>' if t["popular"] else ""
            features_li = "".join([f'<li class="flex items-start gap-3 text-sm text-gray-600"><i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent mt-0.5" aria-hidden="true"></i><span>{feat}</span></li>' for feat in t["features"]])
            btn_class = "lb-btn lb-btn--primary w-full shadow-md" if t["popular"] else "lb-btn lb-btn--secondary w-full"
            
            top_cards_html += f"""
            <div class="flex flex-col justify-between rounded-3xl bg-white p-7 sm:p-9 {pop_border} transition-all duration-300 hover:shadow-2xl">
              <div>
                {pop_badge}
                <div class="flex items-center justify-between">
                  <span class="rounded-full bg-brandSoft px-3 py-1 text-xs font-bold uppercase tracking-wide text-brand">{t["badge"]}</span>
                  <span class="inline-flex items-center gap-1 text-xs font-semibold text-accent"><i data-lucide="zap" class="h-3.5 w-3.5"></i> Instant Setup</span>
                </div>
                
                <h3 class="mt-4 font-display text-2xl font-bold text-navy">{t["name"]}</h3>
                <p class="mt-2 text-xs leading-relaxed text-gray-500">{t["desc"]}</p>
                
                <div class="mt-6 flex items-baseline gap-1 border-b border-gray-100 pb-6">
                  <span class="font-display text-4xl font-extrabold tracking-tight text-navy">{t["price"]}</span>
                  <span class="text-sm font-semibold text-gray-500">/{t["period"]}</span>
                </div>
                
                <ul class="mt-6 space-y-3.5">
                  {features_li}
                </ul>
              </div>
              
              <div class="mt-8 pt-4 border-t border-gray-100">
                <a href="{t['btn_link']}" class="{btn_class}">
                  <span>{t["btn_text"]}</span>
                  <i data-lucide="arrow-right" class="h-4 w-4"></i>
                </a>
                <p class="mt-2.5 text-center text-[11px] text-gray-400">Strictly Non-Refundable Digital Good</p>
              </div>
            </div>
            """

        x_features_li = "".join([f'<div class="flex items-center gap-2.5 text-xs sm:text-sm font-medium text-gray-700"><i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent"></i><span>{feat}</span></div>' for feat in x_tier["features"]])

        tiers_html = f"""
        <div class="grid gap-8 md:grid-cols-3">
          {top_cards_html}
        </div>

        <!-- Featured Wide Enterprise X-Core Card -->
        <div class="mt-10 rounded-3xl border-2 border-brand/40 bg-gradient-to-br from-white via-brandSoft/20 to-emerald-50/30 p-8 sm:p-10 shadow-xl transition-all duration-300 hover:shadow-2xl hover:border-brand">
          <div class="grid gap-8 lg:grid-cols-[1fr_auto] lg:items-center">
            <div class="space-y-4">
              <div class="flex flex-wrap items-center gap-3">
                <span class="inline-flex items-center gap-1.5 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">
                  <i data-lucide="sparkles" class="h-3.5 w-3.5"></i> Enterprise Unlimited
                </span>
                <span class="inline-flex items-center gap-1 text-xs font-bold text-accentDeep bg-emerald-100/70 px-3 py-1 rounded-full">
                  <i data-lucide="zap" class="h-3.5 w-3.5"></i> Zero CPU Core Limits
                </span>
              </div>

              <div>
                <h3 class="font-display text-2xl sm:text-3xl font-extrabold text-navy">
                  {x_tier["name"]} — Maximum Server Scale
                </h3>
                <p class="mt-2 text-sm text-gray-600 max-w-2xl leading-relaxed">
                  {x_tier["desc"]} Built for high-traffic bare-metal clusters, massive multi-tenant agencies, and enterprise web applications requiring unrestricted performance.
                </p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                {x_features_li}
              </div>
            </div>

            <!-- Price & CTA Box -->
            <div class="flex flex-col justify-center rounded-2xl bg-white p-6 sm:p-8 border border-gray-200 shadow-lg text-center min-w-[280px]">
              <span class="text-xs font-bold uppercase tracking-wider text-gray-400">Unrestricted Plan</span>
              <div class="mt-2 flex items-baseline justify-center gap-1">
                <span class="font-display text-4xl sm:text-5xl font-extrabold tracking-tight text-navy">{x_tier["price"]}</span>
                <span class="text-sm font-semibold text-gray-500">/{x_tier["period"]}</span>
              </div>
              <p class="mt-1 text-xs text-accentDeep font-semibold flex items-center justify-center gap-1">
                <i data-lucide="check" class="h-3.5 w-3.5"></i> Instant 60s Activation
              </p>
              <a href="{x_tier['btn_link']}" class="lb-btn lb-btn--primary mt-6 w-full py-3.5 text-sm font-bold shadow-md shadow-brand/20">
                <span>{x_tier["btn_text"]}</span>
                <i data-lucide="arrow-right" class="h-4 w-4"></i>
              </a>
              <p class="mt-2 text-[11px] text-gray-400">Strictly Non-Refundable Digital Good</p>
            </div>
          </div>
        </div>
        """
    else:
        tiers_html = f'<div class="grid gap-8 {grid_cols}">'
        for t in p["tiers"]:
            pop_border = "border-2 border-brand shadow-xl relative scale-[1.02] z-10" if t["popular"] else "border border-gray-200 shadow-md"
            pop_badge = f'<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-brand px-3.5 py-1 text-xs font-bold uppercase tracking-wider text-white shadow-sm">⭐ Most Popular</div>' if t["popular"] else ""
            
            features_li = "".join([f'<li class="flex items-start gap-3 text-sm text-gray-600"><i data-lucide="check-circle-2" class="h-4 w-4 shrink-0 text-accent mt-0.5" aria-hidden="true"></i><span>{feat}</span></li>' for feat in t["features"]])
            
            btn_class = "lb-btn lb-btn--primary w-full shadow-md" if t["popular"] else "lb-btn lb-btn--secondary w-full"
            
            tiers_html += f"""
            <div class="flex flex-col justify-between rounded-3xl bg-white p-7 sm:p-9 {pop_border} transition-all duration-300 hover:shadow-2xl">
              <div>
                {pop_badge}
                <div class="flex items-center justify-between">
                  <span class="rounded-full bg-brandSoft px-3 py-1 text-xs font-bold uppercase tracking-wide text-brand">{t["badge"]}</span>
                  <span class="inline-flex items-center gap-1 text-xs font-semibold text-accent"><i data-lucide="zap" class="h-3.5 w-3.5"></i> Instant Setup</span>
                </div>
                
                <h3 class="mt-4 font-display text-2xl font-bold text-navy">{t["name"]}</h3>
                <p class="mt-2 text-xs leading-relaxed text-gray-500">{t["desc"]}</p>
                
                <div class="mt-6 flex items-baseline gap-1 border-b border-gray-100 pb-6">
                  <span class="font-display text-4xl font-extrabold tracking-tight text-navy">{t["price"]}</span>
                  <span class="text-sm font-semibold text-gray-500">/{t["period"]}</span>
                </div>
                
                <ul class="mt-6 space-y-3.5">
                  {features_li}
                </ul>
              </div>
              
              <div class="mt-8 pt-4 border-t border-gray-100">
                <a href="{t['btn_link']}" class="{btn_class}">
                  <span>{t["btn_text"]}</span>
                  <i data-lucide="arrow-right" class="h-4 w-4"></i>
                </a>
                <p class="mt-2.5 text-center text-[11px] text-gray-400">Strictly Non-Refundable Digital Good</p>
              </div>
            </div>
            """
        tiers_html += "</div>"

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

    related_html = ""
    icon_map = {
        "cpanel-license.html": "cpanel.svg",
        "litespeed-license.html": "litespeed.svg",
        "plesk-license.html": "plesk.svg",
        "whmcs-license.html": "whmcs.svg",
        "cloudlinux-license.html": "cloudlinux.png",
        "virtualizor-license.html": "virtualizor.png",
        "sitepad-license.html": "sitepad.png",
        "whmreseller-license.html": "whmreseller.png",
        "softaculous-license.html": "softaculous.png",
        "jetbackup-license.html": "jetbackup.png",
        "imunify360-license.html": "imunify360.png",
        "webuzo-license.html": "webuzo.png",
        "wp-squared-license.html": "wp-squared.svg"
    }
    for rel in p["related"]:
        rel_icon = icon_map.get(rel['url'], 'cpanel.svg')
        related_html += f"""
        <div class="group relative flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-brand/40 hover:shadow-xl">
          <div>
            <div class="flex items-center justify-between">
              <span class="grid h-11 w-11 place-items-center rounded-xl bg-mist border border-gray-100 p-2 shadow-sm transition-transform group-hover:scale-110">
                <img src="assets/img/icons/{rel_icon}" alt="{rel['title']}" class="h-7 w-7 object-contain" />
              </span>
              <span class="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-bold text-accentDeep">{rel['price']}</span>
            </div>
            <h3 class="mt-4 font-display text-lg font-bold text-navy group-hover:text-brand transition-colors">{rel['title']}</h3>
            <p class="mt-2 text-xs leading-relaxed text-gray-500">{rel['desc']}</p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-400">IP-Bound License</span>
            <a href="{rel['url']}" class="inline-flex items-center gap-1 text-xs font-bold text-brand hover:underline">
              View Details <i data-lucide="arrow-right" class="h-3.5 w-3.5"></i>
            </a>
          </div>
        </div>
        """

    articles_html = ""
    for art in p["articles"]:
        articles_html += f"""
        <div class="group flex flex-col justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:border-brand/30 hover:shadow-lg">
          <div>
            <div class="flex items-center justify-between text-xs">
              <span class="rounded-md bg-mist px-2.5 py-1 font-bold text-brand uppercase tracking-wider">{art['cat']}</span>
              <span class="text-gray-400 font-medium">{art['time']}</span>
            </div>
            <h3 class="mt-3 font-display text-base font-bold text-navy group-hover:text-brand transition-colors">{art['title']}</h3>
            <p class="mt-2 text-xs leading-relaxed text-gray-500">{art['desc']}</p>
          </div>
          <div class="mt-5 pt-3 border-t border-gray-100">
            <a href="#" class="inline-flex items-center gap-1 text-xs font-bold text-brand hover:underline">
              Read Guide <i data-lucide="arrow-up-right" class="h-3.5 w-3.5"></i>
            </a>
          </div>
        </div>
        """

    specs_pills = "".join([f'<span class="inline-flex items-center gap-1.5 rounded-full bg-white px-3 py-1.5 text-xs font-semibold text-navy border border-gray-200 shadow-sm"><i data-lucide="check" class="h-3.5 w-3.5 text-accent"></i> {spec}</span>' for spec in p["specs"]])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["title"]} — LicenBase</title>
  <meta name="description" content="{p["meta_desc"]}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://licenbase.com/{p["filename"][:-5]}" />

  <!-- Open Graph -->
  <meta property="og:type" content="product" />
  <meta property="og:site_name" content="LicenBase" />
  <meta property="og:title" content="{p["title"]} — LicenBase" />
  <meta property="og:description" content="{p["meta_desc"]}" />
  <meta property="og:url" content="https://licenbase.com/{p["filename"][:-5]}" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{p["title"]} — LicenBase" />
  <meta name="twitter:description" content="{p["meta_desc"]}" />

  <!-- Favicon -->
  <link rel="icon" type="image/png" sizes="16x16" href="assets/img/favicon-16x16.png?v=2" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png?v=2" />
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png?v=2" />
  <link rel="icon" type="image/png" sizes="512x512" href="assets/img/favicon.png?v=2" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png?v=2" />
  <link rel="icon" href="favicon.ico?v=2" sizes="any" />
  <link rel="shortcut icon" href="favicon.ico?v=2" />

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet" />

  <!-- Swiper -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

  <!-- Custom styles -->
  <link rel="stylesheet" href="assets/css/styles.css?v=5" />

  <!-- Tailwind (Play CDN) -->
  <script src="https://cdn.tailwindcss.com/3.4.16"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: '#1E40AF',
            brandDeep: '#1E3A8A',
            brandSoft: '#EFF4FF',
            navy: '#111827',
            navyLight: '#1F2937',
            accent: '#10B981',
            accentDeep: '#047857',
            accentSoft: '#ECFDF5',
            mist: '#F8FAFC',
          }},
          fontFamily: {{
            sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
            display: ['Manrope', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
          }},
        }},
      }},
    }};
  </script>
</head>

<body class="bg-white font-sans text-navy antialiased">

  <!-- ============ 01 · TOP BAR & FIXED HEADER ============ -->
  <div class="lb-topbar">
    <div class="lb-shell">
      <header id="site-header" class="lb-header">
        <div class="lb-header-inner">
          <!-- Logo -->
          <a href="/" class="lb-logo" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-logo-img" />
          </a>

          <!-- Desktop nav -->
          <nav class="lb-nav" aria-label="Main navigation">
            <!-- Software mega menu -->
            <div class="lb-drop lb-drop--mega">
              <button type="button" class="lb-nav-link" data-drop aria-haspopup="true" aria-expanded="false">
                Software <i data-lucide="chevron-down" class="h-3.5 w-3.5" aria-hidden="true"></i>
              </button>
              <div class="lb-drop-panel">
                <div class="lb-mega-soon">
                  <p>New products coming soon.</p>
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
                  <a href="/cpanel-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cpanel.svg" alt="cPanel License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>cPanel License</span>
                  </a>
                  <a href="/litespeed-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/litespeed.svg" alt="LiteSpeed License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>LiteSpeed License</span>
                  </a>
                  <a href="/plesk-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/plesk.svg" alt="Plesk License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Plesk License</span>
                  </a>
                  <a href="/whmcs-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmcs.svg" alt="WHMCS License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WHMCS License</span>
                  </a>
                  <a href="/cloudlinux-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/cloudlinux.png" alt="CloudLinux License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>CloudLinux License</span>
                  </a>
                  <a href="/virtualizor-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/virtualizor.png" alt="Virtualizor License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Virtualizor License</span>
                  </a>
                  <a href="/sitepad-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/sitepad.png" alt="SitePad License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>SitePad License</span>
                  </a>
                  <a href="/whmreseller-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/whmreseller.png" alt="WHMReseller License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WHMReseller License</span>
                  </a>
                  <a href="/softaculous-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/softaculous.png" alt="Softaculous License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Softaculous License</span>
                  </a>
                  <a href="/jetbackup-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/jetbackup.png" alt="JetBackup License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>JetBackup License</span>
                  </a>
                  <a href="/imunify360-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/imunify360.png" alt="Imunify360 License" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Imunify360 License</span>
                  </a>
                  <a href="/webuzo-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/webuzo.png" alt="Webuzo Control Panel" class="h-4 w-4 shrink-0 object-contain" />
                    <span>Webuzo Control Panel</span>
                  </a>
                  <a href="/wp-squared-license" class="lb-mega-tile flex items-center gap-2.5">
                    <img src="assets/img/icons/wp-squared.svg" alt="WP Squared" class="h-4 w-4 shrink-0 object-contain" />
                    <span>WP Squared</span>
                  </a>
                </div>
              </div>
            </div>

            <a href="/deals" class="lb-nav-link lb-nav-link--plain">Deals</a>
          </nav>

          <!-- Right actions -->
          <div class="lb-header-actions">
            <a href="https://dashboard.licenbase.com/clientarea.php" class="lb-header-signin">Dashboard</a>
            <a href="/products" class="lb-btn lb-btn--primary lb-header-cta">Get Started</a>
            <button id="menu-open" type="button" class="lb-icon-btn lb-menu-toggle" aria-label="Open menu">
              <i data-lucide="menu" class="h-6 w-6"></i>
            </button>
          </div>
        </div>
      </header>
    </div>
  </div>

  <!-- ============ 02 · HERO SECTION ============ -->
  <section class="lb-hero relative overflow-hidden bg-mist border-b border-gray-200">
    <div class="lb-shell py-14 lg:py-20">
      <div class="grid items-center gap-12 lg:grid-cols-2">
        <!-- Copy -->
        <div class="space-y-6">
          <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-semibold text-gray-500">
            <a href="/" class="transition hover:text-brand">Home</a>
            <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
            <a href="/#categories" class="transition hover:text-brand">Hosting Licenses</a>
            <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
            <span class="text-brand font-bold">{p["slug"].upper()}</span>
          </nav>

          <div class="inline-flex items-center gap-2.5 rounded-full bg-brandSoft px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-brand">
            <img src="assets/img/icons/{'wp-squared.svg' if p['slug'] in ('wpsquared', 'wp-squared') else ('cloudlinux.png' if p['slug'] == 'cloudlinux' else ('virtualizor.png' if p['slug'] == 'virtualizor' else ('imunify360.png' if p['slug'] == 'imunify360' else ('jetbackup.png' if p['slug'] == 'jetbackup' else ('softaculous.png' if p['slug'] == 'softaculous' else ('sitepad.png' if p['slug'] == 'sitepad' else ('whmreseller.png' if p['slug'] == 'whmreseller' else ('webuzo.png' if p['slug'] == 'webuzo' else p['slug'] + '.svg'))))))))}" alt="{p['slug']}" class="h-4 w-4 object-contain" />
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
              <span>View Pricing & Order</span>
            </a>
            <a href="#installation" class="lb-btn lb-btn--secondary px-6 py-3.5 text-base">
              <i data-lucide="terminal" class="h-4 w-4"></i>
              <span>Install Command</span>
            </a>
          </div>

          <div class="flex items-center gap-6 pt-2 text-xs font-semibold text-gray-500">
            <span class="inline-flex items-center gap-1.5"><i data-lucide="shield-check" class="h-4 w-4 text-accent"></i> 100% Genuine</span>
            <span class="inline-flex items-center gap-1.5"><i data-lucide="zap" class="h-4 w-4 text-accent"></i> Instant Activation</span>
            <span class="inline-flex items-center gap-1.5"><i data-lucide="refresh-cw" class="h-4 w-4 text-accent"></i> Free Re-IP Migration</span>
          </div>
        </div>

        <!-- Visual Hero Card -->
        <div class="relative mx-auto w-full max-w-lg">
          <div class="absolute -inset-1 rounded-3xl bg-gradient-to-r from-brand to-accent opacity-20 blur-xl"></div>
          <div class="relative rounded-3xl border border-gray-200 bg-white p-7 sm:p-9 shadow-2xl">
            <div class="flex items-center justify-between border-b border-gray-100 pb-5">
              <div class="flex items-center gap-3">
                <span class="grid h-12 w-12 place-items-center rounded-2xl bg-mist border border-gray-100 p-2 shadow-sm">
                  <img src="assets/img/icons/{'wp-squared.svg' if p['slug'] in ('wpsquared', 'wp-squared') else ('cloudlinux.png' if p['slug'] == 'cloudlinux' else ('virtualizor.png' if p['slug'] == 'virtualizor' else ('imunify360.png' if p['slug'] == 'imunify360' else ('jetbackup.png' if p['slug'] == 'jetbackup' else ('softaculous.png' if p['slug'] == 'softaculous' else ('sitepad.png' if p['slug'] == 'sitepad' else ('whmreseller.png' if p['slug'] == 'whmreseller' else ('webuzo.png' if p['slug'] == 'webuzo' else p['slug'] + '.svg'))))))))}" alt="{p['slug']}" class="h-8 w-8 object-contain" />
                </span>
                <div>
                  <h2 class="font-display text-lg font-bold text-navy">{p["title"].split('(')[0]}</h2>
                  <p class="text-xs text-gray-400">Verified IP-Bound Authentication</p>
                </div>
              </div>
              <span class="inline-flex items-center gap-1 rounded-full bg-emerald-50 px-3 py-1 text-xs font-bold text-accentDeep border border-emerald-200">
                <span class="h-2 w-2 rounded-full bg-accent animate-pulse"></span> Active Status
              </span>
            </div>

            <!-- Terminal Snippet Preview -->
            <div class="mt-6 rounded-xl bg-navy p-4 text-left font-mono text-xs text-gray-300 shadow-inner">
              <div class="flex items-center justify-between border-b border-gray-800 pb-2 text-[11px] text-gray-500">
                <span>Fast Installer</span>
                <span>bash</span>
              </div>
              <p class="mt-3 text-emerald-400">$ curl -fsSL 'https://verify.licenbase.com/install/{p["slug"]}' | bash</p>
              <p class="mt-1 text-gray-400">[LicenBase] IP Authentication Successful.</p>
              <p class="mt-1 text-gray-400">[LicenBase] License verified & active.</p>
              <p class="mt-2 text-brandSoft">$ licenbase_{p["slug"]}</p>
            </div>

            <div class="mt-6 grid grid-cols-2 gap-3 text-center text-xs">
              <div class="rounded-xl bg-mist p-3 border border-gray-100">
                <p class="font-bold text-navy text-sm">60 Seconds</p>
                <p class="text-gray-500 mt-0.5">Average Setup Time</p>
              </div>
              <div class="rounded-xl bg-mist p-3 border border-gray-100">
                <p class="font-bold text-navy text-sm">99.9%</p>
                <p class="text-gray-500 mt-0.5">Auth Cluster Uptime</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ 03 · PRICING SECTION ============ -->
  <section id="pricing" class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Affordable Wholesale Pricing</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Choose Your {p["slug"].upper()} License Tier
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Transparent pricing with zero hidden fees. Instant automated provisioning right after checkout.
        </p>
      </div>

      <!-- Pricing Cards Grid -->
      <div class="mt-12">
        {tiers_html}
      </div>

      <!-- Legal Guarantee Banner -->
      <div class="mt-12 rounded-2xl border border-blue-100 bg-brandSoft/60 p-5 text-center text-xs text-gray-600 max-w-3xl mx-auto flex items-center justify-center gap-2">
        <i data-lucide="info" class="h-4 w-4 text-brand shrink-0"></i>
        <span><strong>Digital Goods Policy:</strong> All licenses are activated immediately on your server IP. Purchases are strictly non-refundable once issued. For questions, contact our 24/7 team.</span>
      </div>
    </div>
  </section>

  <!-- ============ 04 · WHY CHOOSE US ============ -->
  <section class="py-16 lg:py-24 bg-mist border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Enterprise Reliability</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Why Thousands of Sysadmins Trust LicenBase
        </h2>
        <p class="mt-3 text-base text-gray-500">
          We combine wholesale pricing with enterprise-grade authentication uptime and dedicated support.
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="shield-check" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">100% Genuine Software</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            No cracked binaries, nulled scripts, or security backdoors. All updates pull directly from official software repositories.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="zap" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Instant Automated Delivery</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Automated API provisioning binds your server IP instantly upon order completion with zero human delays.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="refresh-cw" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Free Unlimited IP Replacements</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Migrating to a new server or data center? Update your IP address for free anytime directly from your dashboard.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="server" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">Dual Verification Cluster</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Our multi-region redundant licensing proxies guarantee 99.9% uptime so your server licenses never fail validation.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="terminal" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">1-Command Automated Setup</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Simply run our verified curl script and let our automation tool handle configuration and verification in seconds.
          </p>
        </div>

        <div class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="grid h-12 w-12 place-items-center rounded-xl bg-brandSoft text-brand">
            <i data-lucide="headset" class="h-6 w-6"></i>
          </div>
          <h3 class="mt-4 font-display text-lg font-bold text-navy">24/7 Server Engineer Support</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Our experienced Linux systems administrators are available around the clock via live chat and ticket desk.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ 05 · INSTALLATION & CLI PROCESS ============ -->
  <section id="installation" class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Fast & Seamless Deployment</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Purchase & Installation Process
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Get your server activated in under 60 seconds using our simple 3-step workflow.
        </p>
      </div>

      <!-- 3 Steps -->
      <div class="mt-12 grid gap-8 md:grid-cols-3">
        <div class="relative rounded-2xl border border-gray-200 bg-mist p-6 text-center">
          <div class="mx-auto grid h-12 w-12 place-items-center rounded-full bg-brand text-lg font-bold text-white shadow-md shadow-brand/20">1</div>
          <h3 class="mt-4 font-display text-base font-bold text-navy">Order & Bind IP</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Select your tier, enter your server public IPv4 address, and complete payment.
          </p>
        </div>

        <div class="relative rounded-2xl border border-gray-200 bg-mist p-6 text-center">
          <div class="mx-auto grid h-12 w-12 place-items-center rounded-full bg-brand text-lg font-bold text-white shadow-md shadow-brand/20">2</div>
          <h3 class="mt-4 font-display text-base font-bold text-navy">Run Install Command</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Log in via SSH as root and execute our single-line installer command below.
          </p>
        </div>

        <div class="relative rounded-2xl border border-gray-200 bg-mist p-6 text-center">
          <div class="mx-auto grid h-12 w-12 place-items-center rounded-full bg-brand text-lg font-bold text-white shadow-md shadow-brand/20">3</div>
          <h3 class="mt-4 font-display text-base font-bold text-navy">Instant Verification</h3>
          <p class="mt-2 text-xs leading-relaxed text-gray-500">
            Use the CLI command to check license status and update core components anytime.
          </p>
        </div>
      </div>

      <!-- Command Terminal Box -->
      <div class="mt-10 mx-auto max-w-3xl rounded-2xl border border-gray-800 bg-navy p-6 shadow-2xl text-white">
        <div class="flex items-center justify-between border-b border-gray-800 pb-4">
          <div class="flex items-center gap-2">
            <span class="h-3 w-3 rounded-full bg-red-500"></span>
            <span class="h-3 w-3 rounded-full bg-yellow-500"></span>
            <span class="h-3 w-3 rounded-full bg-green-500"></span>
            <span class="ml-2 font-mono text-xs text-gray-400">root@server:~#</span>
          </div>
          <span class="text-xs font-semibold text-gray-400">LicenBase Automated Deployment</span>
        </div>

        <!-- Install Command -->
        <div class="mt-6">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400">Install Command</span>
            <button type="button" onclick="navigator.clipboard.writeText('curl -fsSL \'https://verify.licenbase.com/install/{p['slug']}\' | bash'); this.innerText = 'Copied! ✓'; setTimeout(() => this.innerText = 'Copy Command', 2000)" class="inline-flex items-center gap-1.5 rounded-lg bg-gray-800 px-3 py-1 text-xs font-semibold text-gray-200 hover:bg-brand hover:text-white transition">
              <i data-lucide="copy" class="h-3.5 w-3.5"></i> Copy Command
            </button>
          </div>
          <div class="mt-2 rounded-xl bg-gray-900 p-4 font-mono text-xs text-emerald-400 overflow-x-auto select-all border border-gray-800">
            <p class="text-gray-500 text-[11px] mb-1"># Run as root in your server terminal:</p>
            <p class="whitespace-nowrap"><span class="text-gray-400">$</span> curl -fsSL 'https://verify.licenbase.com/install/{p["slug"]}' | bash</p>
          </div>
        </div>

        <!-- CLI Command -->
        <div class="mt-6">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400">CLI Command</span>
            <button type="button" onclick="navigator.clipboard.writeText('licenbase_{p['slug']}'); this.innerText = 'Copied! ✓'; setTimeout(() => this.innerText = 'Copy CLI', 2000)" class="inline-flex items-center gap-1.5 rounded-lg bg-gray-800 px-3 py-1 text-xs font-semibold text-gray-200 hover:bg-brand hover:text-white transition">
              <i data-lucide="copy" class="h-3.5 w-3.5"></i> Copy CLI
            </button>
          </div>
          <div class="mt-2 rounded-xl bg-gray-900 p-4 font-mono text-xs text-brandSoft overflow-x-auto select-all border border-gray-800">
            <p class="text-gray-500 text-[11px] mb-1"># Verify, renew, or re-check license anytime:</p>
            <p><span class="text-gray-400">$</span> licenbase_{p["slug"]}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ 06 · FAQ (HOMEPAGE DESIGN) ============ -->
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
            Quick answers about purchasing and managing your {p["slug"].upper()} license.
          </p>
        </div>

        <div class="lb-stagger mt-10 space-y-3">
          {faqs_html}
        </div>

        <aside class="lb-faq-support" aria-label="Support options">
          <span class="lb-faq-support-icon"><i data-lucide="message-square-text" class="h-6 w-6" aria-hidden="true"></i></span>
          <div class="lb-faq-support-copy">
            <h3 class="font-display text-lg font-bold text-navy">Still have questions about {p["slug"].upper()}?</h3>
            <p class="mt-1 text-sm text-gray-500">Our senior server engineering support team is ready to assist you.</p>
          </div>
          <div class="lb-faq-support-actions">
            <a href="https://dashboard.licenbase.com/submitticket.php" class="lb-btn lb-btn--secondary">Open Ticket</a>
            <a href="#live-chat" data-open-chat class="lb-btn lb-btn--primary">Live Chat</a>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- ============ 07 · RELATED PRODUCTS ============ -->
  <section class="py-16 lg:py-24 bg-white border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Complete Your Stack</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Complementary Hosting Licenses
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Pair your {p["slug"].upper()} installation with industry-standard security, performance, and automation tools.
        </p>
      </div>

      <div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {related_html}
      </div>
    </div>
  </section>

  <!-- ============ 08 · RELATED ARTICLES & GUIDES ============ -->
  <section class="py-16 lg:py-24 bg-mist border-b border-gray-200">
    <div class="lb-shell">
      <div class="text-center max-w-3xl mx-auto">
        <span class="lb-eyebrow">Knowledgebase</span>
        <h2 class="mt-4 font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">
          Helpful Guides & Tutorials
        </h2>
        <p class="mt-3 text-base text-gray-500">
          Master your server infrastructure with our expert administration tutorials.
        </p>
      </div>

      <div class="mt-12 grid gap-6 md:grid-cols-3">
        {articles_html}
      </div>
    </div>
  </section>

  <!-- ============ 09 · CLOSING CONVERSION CARD ============ -->
  <section class="lb-conversion-section bg-white pb-16 pt-8 lg:pb-24 lg:pt-12">
    <div class="lb-shell">
      <div class="lb-conversion-card">
        <div class="lb-conversion-newsletter">
          <div class="lb-conversion-copy">
            <span class="lb-conversion-mail"><i data-lucide="zap" class="h-7 w-7"></i></span>
            <h2 class="lb-conversion-title">Ready to activate your <span>{p["slug"].upper()} license?</span></h2>
            <p class="lb-conversion-description">
              Join thousands of web hosts, system administrators, and digital agencies who trust LicenBase for their licensing infrastructure.
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
              <p class="font-display font-bold text-navy">100% Genuine Guaranteed</p>
              <p class="text-xs text-gray-500 mt-1">Official vendor mirrors, zero nulled binaries, guaranteed authenticity.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ 10 · FOOTER ============ -->
  <footer id="footer" class="border-t border-gray-200 bg-white pt-16 pb-12 text-sm text-gray-500">
    <div class="lb-shell">
      <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-5">
        <!-- Col 1: Brand -->
        <div class="lg:col-span-2 space-y-4">
          <a href="/" class="inline-block" aria-label="LicenBase home">
            <img src="assets/img/logo.png" alt="LicenBase" class="lb-footer-logo h-18 w-auto" />
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
            <li><a href="/cpanel-license" class="transition hover:text-brand">cPanel & WHM</a></li>
            <li><a href="/litespeed-license" class="transition hover:text-brand">LiteSpeed Web Server</a></li>
            <li><a href="/plesk-license" class="transition hover:text-brand">Plesk Control Panel</a></li>
            <li><a href="/cloudlinux-license" class="transition hover:text-brand">CloudLinux OS</a></li>
            <li><a href="/whmcs-license" class="transition hover:text-brand">WHMCS Billing</a></li>
          </ul>
        </div>

        <!-- Col 3: Tools & Panels -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Panels & Utilities</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/virtualizor-license" class="transition hover:text-brand">Virtualizor VPS</a></li>
            <li><a href="/imunify360-license" class="transition hover:text-brand">Imunify360 Security</a></li>
            <li><a href="/jetbackup-license" class="transition hover:text-brand">JetBackup 5</a></li>
            <li><a href="/softaculous-license" class="transition hover:text-brand">Softaculous</a></li>
            <li><a href="/sitepad-license" class="transition hover:text-brand">SitePad Builder</a></li>
          </ul>
        </div>

        <!-- Col 4: Legal & Policies -->
        <div class="space-y-3">
          <h3 class="font-display text-xs font-bold uppercase tracking-wider text-navy">Legal & Policies</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/terms-of-service" class="transition hover:text-brand">Terms of Service</a></li>
            <li><a href="/privacy-policy" class="transition hover:text-brand">Privacy Policy</a></li>
            <li><a href="/refund-policy" class="transition hover:text-brand">Refund Policy</a></li>
            <li><a href="/license-policy" class="transition hover:text-brand">License Policy</a></li>
            <li><a href="https://dashboard.licenbase.com/submitticket.php" class="transition hover:text-brand">Support Center</a></li>
          </ul>
        </div>
      </div>

      <div class="mt-12 flex flex-col items-center justify-between gap-4 border-t border-gray-200 pt-8 text-xs text-gray-400 sm:flex-row">
        <p>© 2026 LicenBase. All rights reserved. Registered trademark of genuine software licenses.</p>
        <p class="flex items-center gap-1"><i data-lucide="lock" class="h-3.5 w-3.5 text-accent"></i> 256-Bit SSL Encrypted & Non-Refundable Digital Provisioning</p>
      </div>
    </div>
  </footer>

  <!-- Mobile Drawer -->
  <div id="mobile-menu" class="invisible fixed inset-0 z-[60] opacity-0 transition-opacity duration-200" aria-hidden="true">
    <div id="drawer-backdrop" class="absolute inset-0 bg-navy/50 backdrop-blur-sm"></div>
    <div class="relative ml-auto flex h-full w-full max-w-xs flex-col bg-white shadow-2xl">
      <div class="flex items-center justify-between border-b border-gray-100 px-5 py-4">
        <a href="/" class="lb-logo" aria-label="LicenBase home">
          <img src="assets/img/logo.png" alt="LicenBase" class="h-7 w-auto" />
        </a>
        <button id="menu-close" type="button" class="grid h-9 w-9 place-items-center rounded-lg text-gray-500 hover:bg-mist" aria-label="Close menu">
          <i data-lucide="x" class="h-5 w-5"></i>
        </button>
      </div>
      <nav class="flex-1 overflow-y-auto px-4 py-4 text-sm" aria-label="Mobile Navigation">
        <p class="px-3 text-xs font-bold uppercase tracking-wider text-gray-400">Hosting Licenses</p>
        <ul class="mt-2 space-y-1">
          <li><a href="/products" class="lb-mobile-link block rounded-xl px-3 py-2 font-bold text-brand hover:bg-mist">📦 All Products</a></li>
          <li><a href="/deals" class="lb-mobile-link block rounded-xl px-3 py-2 font-bold text-brand hover:bg-mist">🔥 Combo Deals</a></li>
          <li><a href="/cpanel-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">cPanel & WHM</a></li>
          <li><a href="/litespeed-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">LiteSpeed Web Server</a></li>
          <li><a href="/plesk-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Plesk Control Panel</a></li>
          <li><a href="/whmcs-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">WHMCS License</a></li>
          <li><a href="/cloudlinux-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">CloudLinux OS</a></li>
          <li><a href="/virtualizor-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Virtualizor</a></li>
          <li><a href="/imunify360-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Imunify360</a></li>
          <li><a href="/jetbackup-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">JetBackup</a></li>
          <li><a href="/softaculous-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Softaculous</a></li>
          <li><a href="/sitepad-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">SitePad</a></li>
          <li><a href="/webuzo-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">Webuzo Panel</a></li>
          <li><a href="/wp-squared-license" class="lb-mobile-link block rounded-xl px-3 py-2 font-medium text-navy hover:bg-mist">WP Squared</a></li>
        </ul>
        <div class="mt-4 border-t border-gray-100 pt-4">
          <ul class="space-y-1">
            <li><a href="https://dashboard.licenbase.com/clientarea.php" class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy hover:bg-mist">Dashboard</a></li>
            <li><a href="/products" class="lb-mobile-link block rounded-xl bg-brand px-3 py-2.5 text-center font-semibold text-white hover:bg-brandDeep">Get Started</a></li>
          </ul>
        </div>
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
          <input id="overlay-search-input" type="search" placeholder="Search licenses..." class="w-full bg-transparent py-3 text-[15px] text-navy placeholder:text-gray-400 focus:outline-none" autocomplete="off" />
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

  <!-- Libraries -->
  <script src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js" integrity="sha384-hJnF5AwidE18GSWTAGHv3ByzzvfNZ1Tcx5y1UUV3WkauuMCEzBJBMSwSt/PUPXnM" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" integrity="sha384-g4NTh/Iv5PPU4xPyhEWqPcwtNXOvdaDI8LLnyYfyNZOjKJeYQyjzQ9X5275eBjpt" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" integrity="sha384-Z3REaz79l2IaAZqJsSABtTbhjgOUYyV3p90XNnAPCSHg3EMTz1fouunq9WZRtj3d" crossorigin="anonymous"></script>
  <script src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js" integrity="sha384-O55L/6rhHr9CFvrxqv5luxOCcmVaBmETbZbJDP+Do8T0pztTACsFBD/IXCNkj7DV" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" integrity="sha384-2UI1PfnXFjVMQ7/ZDEF70CR943oH3v6uZrFQGGqJYlvhh4g6z6uVktxYbOlAczav" crossorigin="anonymous"></script>

  <!--Start of Tawk.to Script-->
  <script type="text/javascript">
  var Tawk_API=Tawk_API||{{}}, Tawk_LoadStart=new Date();
  (function(){{
  var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
  s1.async=true;
  s1.src='https://embed.tawk.to/6aa54c1357bdd83448ee36a5/1k2ar2bta';
  s1.charset='UTF-8';
  s1.setAttribute('crossorigin','*');
  s0.parentNode.insertBefore(s1,s0);
  }})();
  </script>
  <!--End of Tawk.to Script-->

  <script src="assets/js/main.js?v=6"></script>
</body>
</html>
"""
    with open(p["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {p['filename']}")

for p in products:
    generate_page(p)

print("All 13 product pages generated successfully!")

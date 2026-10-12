from pathlib import Path

OUT_DIR = Path("assets/img/blog")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SVGS = {
    # 1. cpanel-price-hike-2026-alternatives-cost-calculator
    "cpanel-price-hike-2026-alternatives-cost-calculator-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t1 d1">
  <title id="t1">cPanel Price Hike 2026 and Cost Savings Breakdown</title>
  <desc id="d1">Comparison of rising retail cPanel licensing fees versus wholesale IP licensing economics.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">WebPros Official Retail Model</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Compounding Annual Price Hikes</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo: $17.49/mo ($210/year)</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 accts): $29.99/mo ($360/year)</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 accts): $44.99/mo ($540/year)</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Premier (100 accts): $63.99/mo ($768/year)</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Surcharge per extra account: +$0.45/acct/mo</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Punishing Margins for Hosting Providers</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Wholesale IP Licensing</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Flat-Rate High Volume Efficiency</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel VPS License: Just $4.00/month ($48/year)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 100% Official Upstream cPanel Updates</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Zero Migration Friction &amp; Zero Downtime</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Instant Automated IP Activation via SSH</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Save up to $720/year per Server Instance</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Save Up to 75% on Server Software Overhead</text>
</svg>""",

    # 2. cpanel-vs-directadmin-pricing-features-vps-comparison
    "cpanel-vs-directadmin-pricing-features-vps-comparison-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t2 d2">
  <title id="t2">cPanel vs DirectAdmin 2026 Comparison</title>
  <desc id="d2">Detailed technical and financial comparison between cPanel and DirectAdmin control panels.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#3B82F6"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">cPanel &amp; WHM</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#2563EB">The Global Industry Standard</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Client UX: Universal market familiarity</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Ecosystem: LiteSpeed, CloudLinux, Imunify</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Automation: Native AutoSSL &amp; Exim routing</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• RAM Footprint: ~1.2 GB base memory</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• LicenBase Rate: From $4.00/month</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#EFF6FF"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#1D4ED8" text-anchor="middle">Best for Commercial Customer Hosting</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#8B5CF6"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">DirectAdmin</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#7C3AED">Lightweight C++ Alternative</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Client UX: Evolution skin, clean interface</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Flexibility: CustomBuild web server stacks</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Automation: WHMCS billing module supported</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• RAM Footprint: ~450 MB lightweight footprint</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• LicenBase Rate: From $4.00/month</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#F5F3FF"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#6D28D9" text-anchor="middle">Best for Resource-Constrained Small VPS</text>
</svg>""",

    # 3. litespeed-vs-apache-wordpress-performance-cost-guide
    "litespeed-vs-apache-wordpress-performance-cost-guide-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t3 d3">
  <title id="t3">LiteSpeed vs Apache Speed and ROI Comparison</title>
  <desc id="d3">Performance benchmarks and hardware cost savings of LiteSpeed Enterprise versus standard Apache.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Apache + PHP-FPM</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Process-Bound Web Architecture</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Concurrency: 300 to 500 requests/second</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• TTFB: 350ms to 800ms under load</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• WooCommerce ESI: Complex third-party caching</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Server RAM: High memory consumption spikes</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Hardware Cost: Requires upgrading VPS tiers</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Bottlenecks Under Traffic Spikes</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LiteSpeed Enterprise + LSCache</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Asynchronous Event-Driven Engine</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Concurrency: 5,000+ requests/second</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• TTFB: 40ms to 90ms instant response</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Native ESI: Cached store with dynamic carts</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Server RAM: Predictable, lightweight usage</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Hardware ROI: Postpones costly VPS upgrades</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Up to 10x Throughput at $4/mo License</text>
</svg>""",

    # 4. whmcs-pricing-tiers-explained-how-to-avoid-costly-upgrades
    "whmcs-pricing-tiers-explained-how-to-avoid-costly-upgrades-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t4 d4">
  <title id="t4">WHMCS Pricing Tiers and Cost Reduction Framework</title>
  <desc id="d4">Breakdown of WHMCS active client tiers and strategies to avoid unexpected tier upgrade penalties.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#F59E0B"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Official WHMCS Client Tiers</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#D97706">Recurring Monthly Escalations</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Plus Tier (&lt;250 clients): ~$24.95/month</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Professional (&lt;500 clients): ~$39.95/month</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Business (&lt;1000 clients): ~$59.95/month</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Active client traps: Suspended accts count</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Annual Cost: $300 to $720+ every single year</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEF3C7"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#92400E" text-anchor="middle">Punishes Growing Web Hosting Startups</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Uncapped Licensing</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Flat-Rate Freedom for Providers</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Monthly Option: Flat $4.00/month</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Owned Lifetime Option: $20.00 one-time</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Zero Client Count Caps or Artificial Limits</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Official Upstream Upgrades &amp; Security Fixes</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 100% Native Gateway &amp; Provisioning Modules</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Scale to Thousands of Clients Without Extra Fees</text>
</svg>""",

    # 5. cpanel-lisansi-fiyat-artisi-turkiye-hosting-rehberi
    "cpanel-lisansi-fiyat-artisi-turkiye-hosting-rehberi-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t5 d5">
  <title id="t5">Türkiye cPanel Fiyat Artışı ve Tasarruf Rehberi</title>
  <desc id="d5">Türkiye hosting firmaları ve web ajansları için cPanel fiyat artışı analizi ve LicenBase toptan lisanslama modeli.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Resmi Perakende / Bayi Fiyatları</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Döviz Kuru ve Hesap Başı Ücretler</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo (1 Hesap): $17.49/ay (~610 TL)</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 Hesap): $29.99/ay (~1.050 TL)</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 Hesap): $44.99/ay (~1.575 TL)</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Premier (100 Hesap): $63.99/ay (~2.240 TL)</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Yıllık Toplam: 12.000 TL - 26.000 TL / sunucu</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Ajans ve Reseller Kâr Marjını Eritiyor</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Toptan IP Lisanslama</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Sabit Maliyetli Orijinal Çözüm</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel VPS Lisansı: Sadece $4.00/ay (~140 TL)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Orijinal cPanel Dosyaları ve Resmi Güncellemeler</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Crack veya Nulled Değil, 100% Güvenli Altyapı</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Türkiye Veri Merkezleri ve Bulut VPS ile Uyumlu</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Sunucu Başına Yılda 20.000 TL Net Tasarruf</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Yıllık %75'in Üzerinde Maliyet Avantajı</text>
</svg>""",

    # 6. litespeed-lisansi-fiyatlari-wordpress-hizlandirma-rehberi
    "litespeed-lisansi-fiyatlari-wordpress-hizlandirma-rehberi-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t6 d6">
  <title id="t6">LiteSpeed Web Server Hız ve Lisans Maliyet Analizi</title>
  <desc id="d6">WordPress ve WooCommerce için LiteSpeed Enterprise hız performansı ve donanım tasarrufu karşılaştırması.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#3B82F6"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Standart Apache Web Server</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#2563EB">Yüksek Donanım Tüketimi</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Eşzamanlı İstek: 300 - 500 RPS kapasitesi</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Yanıt Süresi (TTFB): 400ms - 900ms arası</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• CPU Tüketimi: E-ticaret trafiğinde %100 yük</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Çözüm Yolu: Daha pahalı VPS işlemcisi kiralamak</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Ek Bulut Donanım Maliyeti: +500 TL ila 1.500 TL/ay</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#EFF6FF"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#1D4ED8" text-anchor="middle">Trafik Anında Sunucu Kilitlenmesi</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LiteSpeed Enterprise + LSCache</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Sunucu Düzeyinde Hız ve Tasarruf</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Eşzamanlı İstek: 5.000+ RPS yüksek kapasite</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Yanıt Süresi (TTFB): 30ms - 80ms yıldırım hız</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• WooCommerce ESI: Dinamik sepet önbellekleme</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• CPU Yükü: İşlemci kullanımını %70 azaltır</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• LicenBase Fiyatı: Ayda sadece $4.00 (~140 TL)</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Aynı VPS ile 5 Kat Fazla Ziyaretçi Barındırın</text>
</svg>""",

    # 7. turkiye-reseller-hosting-icin-en-iyi-lisans-paketleri
    "turkiye-reseller-hosting-icin-en-iyi-lisans-paketleri-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t7 d7">
  <title id="t7">Türkiye Reseller Hosting Lisanslama Yığını</title>
  <desc id="d7">Türkiye'de profesyonel bayi hosting altyapısı kurarken gereken lisanslar ve kombine tasarruf rehberi.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="205" height="350" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="205" height="6" rx="3" fill="#3B82F6"/>
  <text x="55" y="70" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">1. Kontrol Paneli</text>
  <text x="55" y="92" font-family="Inter, sans-serif" font-size="12" fill="#2563EB">cPanel &amp; WHM</text>
  <path d="M55 110 h175" stroke="#F1F5F9" stroke-width="1"/>
  <text x="55" y="140" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Müşteri alışkanlığı</text>
  <text x="55" y="170" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Tek tıkla hesap açma</text>
  <text x="55" y="200" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Otomatik AutoSSL</text>
  <text x="55" y="230" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Kolay DNS ve e-posta</text>
  <rect x="55" y="315" width="175" height="36" rx="6" fill="#EFF6FF"/>
  <text x="142" y="337" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">$4.00/ay</text>

  <rect x="270" y="35" width="205" height="350" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="270" y="35" width="205" height="6" rx="3" fill="#10B981"/>
  <text x="285" y="70" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">2. Web Hızlandırma</text>
  <text x="285" y="92" font-family="Inter, sans-serif" font-size="12" fill="#059669">LiteSpeed Server</text>
  <path d="M285 110 h175" stroke="#F1F5F9" stroke-width="1"/>
  <text x="285" y="140" font-family="Inter, sans-serif" font-size="12" fill="#475569">• 10 kat hızlı WP</text>
  <text x="285" y="170" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LSCache desteği</text>
  <text x="285" y="200" font-family="Inter, sans-serif" font-size="12" fill="#475569">• .htaccess %100 uyum</text>
  <text x="285" y="230" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Düşük CPU kullanımı</text>
  <rect x="285" y="315" width="175" height="36" rx="6" fill="#D1FAE5"/>
  <text x="372" y="337" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">$4.00/ay</text>

  <rect x="500" y="35" width="205" height="350" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="500" y="35" width="205" height="6" rx="3" fill="#8B5CF6"/>
  <text x="515" y="70" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">3. Hesap İzolasyonu</text>
  <text x="515" y="92" font-family="Inter, sans-serif" font-size="12" fill="#7C3AED">CloudLinux OS</text>
  <path d="M515 110 h175" stroke="#F1F5F9" stroke-width="1"/>
  <text x="515" y="140" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LVE CPU/RAM sınırı</text>
  <text x="515" y="170" font-family="Inter, sans-serif" font-size="12" fill="#475569">• CageFS güvenlik kafesi</text>
  <text x="515" y="200" font-family="Inter, sans-serif" font-size="12" fill="#475569">• PHP Selector modülü</text>
  <text x="515" y="230" font-family="Inter, sans-serif" font-size="12" fill="#475569">• MySQL Governor</text>
  <rect x="515" y="315" width="175" height="36" rx="6" fill="#F5F3FF"/>
  <text x="602" y="337" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#6D28D9" text-anchor="middle">$4.00/ay</text>

  <rect x="730" y="35" width="190" height="350" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="730" y="35" width="190" height="6" rx="3" fill="#F59E0B"/>
  <text x="745" y="70" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">4. Otomasyon</text>
  <text x="745" y="92" font-family="Inter, sans-serif" font-size="12" fill="#D97706">WHMCS Faturalama</text>
  <path d="M745 110 h160" stroke="#F1F5F9" stroke-width="1"/>
  <text x="745" y="140" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Otomatik hesap açma</text>
  <text x="745" y="170" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Destek bilet sistemi</text>
  <text x="745" y="200" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Domain kayıt modülü</text>
  <text x="745" y="230" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Sınırsız müşteri</text>
  <rect x="745" y="315" width="160" height="36" rx="6" fill="#FEF3C7"/>
  <text x="825" y="337" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">$4/ay veya $20 ömürlük</text>
</svg>"""
}

for name, svg_code in SVGS.items():
    file_path = OUT_DIR / f"{name}.svg"
    file_path.write_text(svg_code.strip(), encoding="utf-8")
    print(f"Created SVG: {file_path}")

print("All 7 SVGs created successfully!")

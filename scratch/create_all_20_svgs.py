from pathlib import Path

OUT_DIR = Path("assets/img/blog")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SVGS = {
    # 1. cpanel-license-price-india-vps-guide
    "cpanel-license-price-india-vps-guide-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t1 d1">
  <title id="t1">cPanel License Price in India Comparison</title>
  <desc id="d1">Comparison of official retail cPanel license pricing in INR versus LicenBase wholesale pricing.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Official US Retail / Indian Resellers</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">High Markup &amp; Additional Taxes</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo: ~₹1,750/mo ($17.49 + 18% GST)</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 accts): ~₹2,950/mo</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 accts): ~₹4,450/mo</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Bank Forex Markup: 3.5% + GST on foreign cards</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Total Annual Cost: ₹25,000 to ₹50,000+ per VPS</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Heavy Monthly Burden for Agencies</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Wholesale IP Licensing</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Authentic cPanel at Wholesale Rates</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel VPS License: $4.00/mo (~₹330/mo)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 100% Genuine Software from Official Mirrors</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Automated Instant IP Activation (60 seconds)</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Works on AWS Mumbai, DigitalOcean Bangalore</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Saves over 75% on Annual Infrastructure Budget</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Save ₹15,000+ Every Year per Server</text>
</svg>""",

    # 2. cheap-cpanel-license-choose-reliable-vps-guide
    "cheap-cpanel-license-choose-reliable-vps-guide-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t2 d2">
  <title id="t2">How to Choose a Reliable Cheap cPanel License</title>
  <desc id="d2">Decision criteria framework when selecting an affordable cPanel license for VPS servers.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#3B82F6"/>
  <text x="60" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">1. Software Source</text>
  <text x="60" y="95" font-family="Inter, sans-serif" font-size="12" fill="#2563EB">Authenticity Verification</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Downloads from cPanel</text>
  <text x="60" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Zero patched binaries</text>
  <text x="60" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• No hidden backdoors</text>
  <text x="60" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Pure genuine RPMs</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#EFF6FF"/>
  <text x="170" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">Official Binary Integrity</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="370" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">2. IP Validation</text>
  <text x="370" y="95" font-family="Inter, sans-serif" font-size="12" fill="#059669">Fast cpkeyclt Sync</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Bound to public IPv4</text>
  <text x="370" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Standard cpkeyclt command</text>
  <text x="370" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Instant activation &lt;60s</text>
  <text x="370" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Easy IP change support</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#ECFDF5"/>
  <text x="480" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">Automated Provisioning</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#8B5CF6"/>
  <text x="680" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">3. Ecosystem Support</text>
  <text x="680" y="95" font-family="Inter, sans-serif" font-size="12" fill="#7C3AED">Integrated Addons</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LiteSpeed Web Server</text>
  <text x="680" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• CloudLinux OS support</text>
  <text x="680" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Softaculous 1-click tools</text>
  <text x="680" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• 24/7 technical assistance</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#F5F3FF"/>
  <text x="790" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#6D28D9" text-anchor="middle">Complete Hosting Stack</text>
</svg>""",

    # 3. cpanel-license-not-working-server-admin-fixes
    "cpanel-license-not-working-server-admin-fixes-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t3 d3">
  <title id="t3">cPanel License Troubleshooting Flowchart</title>
  <desc id="d3">Systematic troubleshooting workflow for resolving cPanel licensing errors on Linux VPS.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Run cpkeyclt Command</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">/usr/local/cpanel/cpkeyclt</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Check Port 873 &amp; 443</text>
  <text x="480" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">rSync &amp; HTTPS Firewall</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Verify Outbound IPv4</text>
  <text x="780" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">curl -4 ifconfig.me</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">Common Fixes Checklist</text>
  <text x="90" y="275" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Firewall: Open outbound TCP port 873 in CSF / firewalld</text>
  <text x="90" y="305" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ System Clock: Sync time using chronyc makestep or ntpdate</text>
  <text x="90" y="335" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Licensing IP: Ensure registered IP matches the primary server public IP</text>
</svg>""",

    # 4. how-to-fix-high-cpu-usage-linux-vps-tricks
    "how-to-fix-high-cpu-usage-linux-vps-tricks-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t4 d4">
  <title id="t4">Linux VPS High CPU Troubleshooting Pipeline</title>
  <desc id="d4">Pipeline for diagnosing, isolating, and solving high CPU usage on Linux VPS.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#EF4444"/>
  <text x="60" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">1. Identification</text>
  <text x="60" y="95" font-family="Inter, sans-serif" font-size="12" fill="#DC2626">Locate Heavy Processes</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• htop (interactive inspection)</text>
  <text x="60" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• ps aux --sort=-%cpu</text>
  <text x="60" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• iotop (check disk wait iowait)</text>
  <text x="60" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• vmstat 1 5 (system health)</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#FEE2E2"/>
  <text x="170" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#991B1B" text-anchor="middle">Find Runaway PIDs</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#F59E0B"/>
  <text x="370" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">2. Service Tuning</text>
  <text x="370" y="95" font-family="Inter, sans-serif" font-size="12" fill="#D97706">Tune PHP &amp; MySQL</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Optimize pm.max_children</text>
  <text x="370" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Block xmlrpc.php floods</text>
  <text x="370" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Enable slow_query_log</text>
  <text x="370" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Kill hanging MySQL queries</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#FEF3C7"/>
  <text x="480" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">Resolve Root Causes</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="680" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">3. Acceleration</text>
  <text x="680" y="95" font-family="Inter, sans-serif" font-size="12" fill="#059669">Upgrade Architecture</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LiteSpeed Web Server (LSCache)</text>
  <text x="680" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Slashes CPU load by 50-70%</text>
  <text x="680" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• CloudLinux LVE tenant limits</text>
  <text x="680" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Protects server from spikes</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#D1FAE5"/>
  <text x="790" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">Permanent Stability</text>
</svg>""",

    # 5. licenca-cpanel-barata-escolher-servidor-vps
    "licenca-cpanel-barata-escolher-servidor-vps-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t5 d5">
  <title id="t5">Guia de Escolha de Licença cPanel VPS no Brasil</title>
  <desc id="d5">Comparativo de custos em Reais entre varejo tradicional e LicenBase atacado.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Varejo Oficial / Revendas Locais</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Câmbio Flutuante + IOF Bancário</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo: ~R$ 95/mês (US$ 17.49)</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 contas): ~R$ 165/mês</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 contas): ~R$ 250/mês</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Premier (100 contas): ~R$ 350/mês</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Custo anual pesado para agências digitais</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Alto Custo em Dólar</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Atacado por IP</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Software 100% Original e Atualizado</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Licença cPanel VPS: apenas US$ 4/mês (~R$ 22)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Atualizações oficiais diretas da cPanel</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Ativação instantânea no IPv4 do servidor</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Suporte técnico especializado 24/7</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Economia real de até 80% todo mês</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Economize mais de R$ 1.500/ano</text>
</svg>""",

    # 6. preco-licenca-litespeed-vale-a-pena-wordpress
    "preco-licenca-litespeed-vale-a-pena-wordpress-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t6 d6">
  <title id="t6">LiteSpeed Web Server vs Apache WordPress Benchmark</title>
  <desc id="d6">Comparativo de requisições por segundo e velocidade TTFB entre Apache e LiteSpeed Enterprise.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#94A3B8"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Apache Tradicional + PHP-FPM</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#64748B">Alto Consumo de Memória</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Requisições por segundo: ~300 a 600 RPS</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• TTFB médio no WordPress: 350ms a 800ms</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Cache dinâmico: requer plugins pesados</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Concorrência alta: sobrecarga de CPU rápida</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Requer servidores VPS maiores e caros</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#F1F5F9"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">Desempenho Limitado</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LiteSpeed Enterprise + LSCache</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Alta Concorrência &amp; Cache Nativo</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Requisições por segundo: 3.500 a 8.000+ RPS</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• TTFB ultrarrápido: 45ms a 120ms</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Cache a nível de servidor sem carregar PHP</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Suporte ESI nativo para WooCommerce</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Licença LicenBase: a partir de US$ 4/mês</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">10x Mais Rápido &amp; Baixo Custo</text>
</svg>""",

    # 7. como-corrigir-erros-licenca-cpanel-solucoes
    "como-corrigir-erros-licenca-cpanel-solucoes-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t7 d7">
  <title id="t7">Diagnóstico de Erros de Licença cPanel no Linux</title>
  <desc id="d7">Fluxo prático para validar licença e desbloquear o WHM rapidamente.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">1. Executar cpkeyclt</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">/usr/local/cpanel/cpkeyclt</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">2. Porta 873 no Firewall</text>
  <text x="480" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Liberar rSync e HTTPS</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">3. Validar IP e Relógio</text>
  <text x="780" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">IP público e NTP time</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">Ações Imediatas para Restaurar o cPanel</text>
  <text x="90" y="275" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ CSF Firewall: adicionar porta 873 em TCP_OUT e reiniciar com csf -r</text>
  <text x="90" y="305" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Sincronização NTP: ajustar data e hora com chronyc makestep</text>
  <text x="90" y="335" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Atualização IP LicenBase: conferir IPv4 ativo no painel de controle</text>
</svg>""",

    # 8. como-resolver-alto-uso-cpu-ram-vps-linux
    "como-resolver-alto-uso-cpu-ram-vps-linux-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t8 d8">
  <title id="t8">Diagnóstico de CPU e RAM no Linux VPS</title>
  <desc id="d8">Procedimento de inspeção e controle de memória e CPU em servidores Linux.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#3B82F6"/>
  <text x="60" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">1. Monitoramento</text>
  <text x="60" y="95" font-family="Inter, sans-serif" font-size="12" fill="#2563EB">Ferramentas de Terminal</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• htop (uso interativo)</text>
  <text x="60" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• free -h (memória e swap)</text>
  <text x="60" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• ps aux --sort=-%mem</text>
  <text x="60" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• vmstat 1 5 (pressão de IO)</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#EFF6FF"/>
  <text x="170" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">Mapear Consumo</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#F59E0B"/>
  <text x="370" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">2. Ajustes PHP &amp; BD</text>
  <text x="370" y="95" font-family="Inter, sans-serif" font-size="12" fill="#D97706">Limitar Concorrência</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Ajustar pm.max_children</text>
  <text x="370" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Configurar pm = ondemand</text>
  <text x="370" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• innodb_buffer_pool_size</text>
  <text x="370" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Bloquear requisições maliciosas</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#FEF3C7"/>
  <text x="480" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">Otimizar Recursos</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="680" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">3. Softwares Líderes</text>
  <text x="680" y="95" font-family="Inter, sans-serif" font-size="12" fill="#059669">LiteSpeed &amp; CloudLinux</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LiteSpeed corta CPU em 70%</text>
  <text x="680" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• CloudLinux isola contas no LVE</text>
  <text x="680" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Impede quedas gerais do VPS</text>
  <text x="680" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LicenBase atacado a US$ 4/mês</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#D1FAE5"/>
  <text x="790" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">Estabilidade Máxima</text>
</svg>""",

    # 9. cpanel-license-dam-koto-bangladesh-vps
    "cpanel-license-dam-koto-bangladesh-vps-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t9 d9">
  <title id="t9">বাংলাদেশে cPanel লাইসেন্সের দামের তুলনা</title>
  <desc id="d9">অফিসিয়াল রিটেইল মূল্য বনাম LicenBase পাইকারি লাইসেন্সের খরচ তুলনা।</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, 'Nirmala UI', sans-serif" font-size="18" font-weight="700" fill="#0F172A">অফিসিয়াল রিটেইল / দেশীয় রিসেলার</text>
  <text x="70" y="100" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#DC2626">ডলার রেট ও ব্যাংকিং চার্জ</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel Solo: প্রায় ২,১০০ টাকা/মাস ($17.49)</text>
  <text x="70" y="190" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel Admin (৫ অ্যাকাউন্ট): প্রায় ৩,৬০০ টাকা/মাস</text>
  <text x="70" y="225" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel Pro (৩০ অ্যাকাউন্ট): প্রায় ৫,৪০০ টাকা/মাস</text>
  <text x="70" y="260" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel Premier: প্রায় ৭,৭০০ টাকা/মাস</text>
  <text x="70" y="295" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• বার্ষিক লাইসেন্স খরচ ৩০,০০০ - ৬০,০০০+ টাকা</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">অতিরিক্ত ডলার খরচ ও বাজেট সংকট</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, 'Nirmala UI', sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase পাইকারি রেট</text>
  <text x="540" y="100" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#059669">১০০% আসল ও ইনস্ট্যান্ট অ্যাক্টিভেশন</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel VPS লাইসেন্স: মাত্র ৪ ডলার/মাস (~৪৮০ টাকা)</text>
  <text x="540" y="190" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel অফিশিয়াল মিরর থেকে অটো আপডেট</text>
  <text x="540" y="225" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• ৬০ সেকেন্ডে আইপি দিয়ে লাইসেন্স সক্রিয়</text>
  <text x="540" y="260" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• ২৪/৭ নিরবচ্ছিন্ন লাইসেন্স সাপোর্ট</text>
  <text x="540" y="295" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• বছরে ২০,০০০ থেকে ৫০,০০০ টাকা সাশ্রয়</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">৭৫% এর বেশি খরচ বাঁচান</text>
</svg>""",

    # 10. cpanel-license-kaj-korche-na-somadhan
    "cpanel-license-kaj-korche-na-somadhan-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t10 d10">
  <title id="t10">cPanel লাইসেন্স এরর সমাধানের ধাপসমূহ</title>
  <desc id="d10">টার্মিনালে cPanel লাইসেন্স সক্রিয় ও যাচাই করার ধারাবাহিক নির্দেশিকা।</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, 'Nirmala UI', sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">১. cpkeyclt কমান্ড দিন</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">/usr/local/cpanel/cpkeyclt</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, 'Nirmala UI', sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">২. ফায়ারওয়াল পোর্ট ৮৭৩</text>
  <text x="480" y="110" font-family="Inter, 'Nirmala UI', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">rSync আউটবাউন্ড চেক</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, 'Nirmala UI', sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">৩. আইপি ও ঘড়ি চেক</text>
  <text x="780" y="110" font-family="Inter, 'Nirmala UI', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">পাবলিক IPv4 ও NTP সময়</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, 'Nirmala UI', sans-serif" font-size="15" font-weight="700" fill="#0F172A">দ্রুত লাইসেন্স সচল করার চেকলিস্ট</text>
  <text x="90" y="275" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">✔ CSF ফায়ারওয়ালে 873 পোর্ট যুক্ত করুন এবং csf -r চালান</text>
  <text x="90" y="305" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">✔ chronyc makestep দিয়ে সার্ভার সময় সিঙ্ক করুন</text>
  <text x="90" y="335" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">✔ LicenBase ড্যাশবোর্ডে সার্ভারের সঠিক পাবলিক আইপি মিলিয়ে নিন</text>
</svg>""",

    # 11. linux-vps-slow-cpu-ram-disk-komanor-upay
    "linux-vps-slow-cpu-ram-disk-komanor-upay-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t11 d11">
  <title id="t11">Linux VPS পারফরম্যান্স অপ্টিমাইজেশন ট্রিকস</title>
  <desc id="d11">সিপিইউ, মেমরি ও ডিস্কের সমস্যা চিহ্নিতকরণ এবং কার্যকর অপ্টিমাইজেশন।</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#3B82F6"/>
  <text x="60" y="70" font-family="Inter, 'Nirmala UI', sans-serif" font-size="16" font-weight="700" fill="#0F172A">১. সিপিইউ ট্রাবলশুটিং</text>
  <text x="60" y="95" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#2563EB">প্রসেস ও থ্রেড বিশ্লেষণ</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• htop চালিয়ে টপ প্রসেস খুঁজুন</text>
  <text x="60" y="185" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• ps aux --sort=-%cpu</text>
  <text x="60" y="220" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• xmlrpc.php বট ট্রাফিক ব্লক</text>
  <text x="60" y="255" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• হ্যাং প্রসেস বন্ধে kill -9</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#EFF6FF"/>
  <text x="170" y="334" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">সিপিইউ লোড কমান</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#F59E0B"/>
  <text x="370" y="70" font-family="Inter, 'Nirmala UI', sans-serif" font-size="16" font-weight="700" fill="#0F172A">২. মেমরি ও সোয়াপ</text>
  <text x="370" y="95" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#D97706">র‍্যাম অপ্টিমাইজেশন</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• free -h দিয়ে র‍্যাম পর্যবেক্ষণ</text>
  <text x="370" y="185" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• pm.max_children সঠিক মান</text>
  <text x="370" y="220" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• MariaDB বাফার পুল টিউনিং</text>
  <text x="370" y="255" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• swappiness মান ১০ এ সেট করুন</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#FEF3C7"/>
  <text x="480" y="334" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">মেমরি লিক বন্ধ করুন</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="680" y="70" font-family="Inter, 'Nirmala UI', sans-serif" font-size="16" font-weight="700" fill="#0F172A">৩. ডিস্ক ও সফটওয়্যার</text>
  <text x="680" y="95" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#059669">LiteSpeed স্পিড বুস্ট</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• journalctl লগ ফাইল পরিষ্কার</text>
  <text x="680" y="185" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• dnf clean / apt autoremove</text>
  <text x="680" y="220" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• LiteSpeed LSCache ব্যবহার</text>
  <text x="680" y="255" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" fill="#475569">• CloudLinux দিয়ে রিসোর্স ভাগ</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#D1FAE5"/>
  <text x="790" y="334" font-family="Inter, 'Nirmala UI', sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">সর্বোচ্চ সার্ভার স্পিড</text>
</svg>""",

    # 12. litespeed-bonam-nginx-wordpress-konti-bhalo
    "litespeed-bonam-nginx-wordpress-konti-bhalo-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t12 d12">
  <title id="t12">LiteSpeed বনাম Nginx ওয়ার্ডপ্রেস তুলনা</title>
  <desc id="d12">ওয়ার্ডপ্রেস পারফরম্যান্স, ক্যাশিং ও ফিচারের তুলনামূলক চার্ট।</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#94A3B8"/>
  <text x="70" y="75" font-family="Inter, 'Nirmala UI', sans-serif" font-size="18" font-weight="700" fill="#0F172A">Nginx ওয়েব সার্ভার (ওপেন সোর্স)</text>
  <text x="70" y="100" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#64748B">দ্রুতগতির তবে জটিল কনফিগারেশন</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• .htaccess সাপোর্ট করে না (ম্যানুয়াল রিরাইট)</text>
  <text x="70" y="190" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• প্রতিটি পরিবর্তনের পর সার্ভার রিলোড লাগে</text>
  <text x="70" y="225" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• উকমার্সের জন্য ESI ক্যাশ সেটআপ জটিল</text>
  <text x="70" y="260" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel এর সাথে প্লাগ-অ্যান্ড-প্লে নয়</text>
  <text x="70" y="295" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• নন-টেকনিক্যাল ইউজারদের জন্য কঠিন</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#F1F5F9"/>
  <text x="245" y="349" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">ম্যানুয়াল ও জটিল ব্যবস্থাপনা</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, 'Nirmala UI', sans-serif" font-size="18" font-weight="700" fill="#0F172A">LiteSpeed Enterprise + LSCache</text>
  <text x="540" y="100" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#059669">ওয়ার্ডপ্রেসের জন্য চূড়ান্ত গতি</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• ১০০% নেটিভ .htaccess সাপোর্ট (রিস্টার্ট লাগে না)</text>
  <text x="540" y="190" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• অফিসিয়াল LSCache প্লাগইনে সর্বোচ্চ স্পিড</text>
  <text x="540" y="225" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• উকমার্সের কার্ট ও ডায়নামিক পেজ ক্যাশ</text>
  <text x="540" y="260" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• cPanel WHM এ ১-ক্লিকে ইনস্টল ও পরিচালনা</text>
  <text x="540" y="295" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" fill="#475569">• LicenBase এ মাত্র ৪ ডলার/মাস থেকে শুরু</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, 'Nirmala UI', sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">ওয়ার্ডপ্রেসের জন্য সেরা পছন্দ</text>
</svg>""",

    # 13. harga-lisensi-cpanel-panduan-murah-vps
    "harga-lisensi-cpanel-panduan-murah-vps-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t13 d13">
  <title id="t13">Perbandingan Harga Lisensi cPanel VPS di Indonesia</title>
  <desc id="d13">Harga resmi eceran cPanel dalam Rupiah versus harga grosir otomatis LicenBase.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Harga Eceran Distributor Resmi</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Konversi Dolar AS + Biaya Valas</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo (1 akun): ~ Rp 285.000/bln</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 akun): ~ Rp 490.000/bln</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 akun): ~ Rp 735.000/bln</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Premier: ~ Rp 1.050.000/bln</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Pengeluaran tahunan tinggi bagi agensi</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Beban Finansial Server Tinggi</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Grosir IP Otomatis</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Software Resmi 100% Asli &amp; Aman</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Lisensi cPanel VPS: $4.00/bln (~ Rp 65.000)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Download resmi dari mirror cPanel</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Aktivasi instan berbasis IP publik (&lt;60 detik)</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Kompatibel dengan semua cloud &amp; VPS provider</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Hemat biaya operasional hingga 75%</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Hemat Jutaan Rupiah Setiap Tahun</text>
</svg>""",

    # 14. cara-mengatasi-error-lisensi-cpanel-vps
    "cara-mengatasi-error-lisensi-cpanel-vps-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t14 d14">
  <title id="t14">Alur Mengatasi Error Lisensi cPanel di VPS Linux</title>
  <desc id="d14">Langkah cepat diagnosa dan perbaikan lisensi cPanel dan WHM.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">1. Jalankan cpkeyclt</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">/usr/local/cpanel/cpkeyclt</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">2. Buka Port 873 &amp; 443</text>
  <text x="480" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Firewall CSF / firewalld</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">3. Cek IP &amp; Waktu Jam</text>
  <text x="780" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Sinkronisasi NTP</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">Panduan Perbaikan Mandiri</text>
  <text x="90" y="275" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Firewall: Tambahkan port 873 pada TCP_OUT di CSF lalu jalankan csf -r</text>
  <text x="90" y="305" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Waktu Jam: Pastikan jam server akurat dengan perintah chronyc makestep</text>
  <text x="90" y="335" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ IP LicenBase: Pastikan alamat IPv4 server cocok dengan yang terdaftar</text>
</svg>""",

    # 15. cara-mengatasi-cpu-vps-100-persen-linux
    "cara-mengatasi-cpu-vps-100-persen-linux-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t15 d15">
  <title id="t15">Alur Mengatasi Penggunaan CPU VPS 100% di Linux</title>
  <desc id="d15">Langkah identifikasi dan isolasi proses berat prosesor pada server VPS.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#EF4444"/>
  <text x="60" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">1. Identifikasi</text>
  <text x="60" y="95" font-family="Inter, sans-serif" font-size="12" fill="#DC2626">Cari Proses Macet</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• htop (monitoring visual)</text>
  <text x="60" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• ps aux --sort=-%cpu</text>
  <text x="60" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• iotop (cek disk wait)</text>
  <text x="60" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Temukan PID mencurigakan</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#FEE2E2"/>
  <text x="170" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#991B1B" text-anchor="middle">Tangkap Sumber CPU</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#F59E0B"/>
  <text x="370" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">2. Optimasi PHP &amp; BD</text>
  <text x="370" y="95" font-family="Inter, sans-serif" font-size="12" fill="#D97706">Tuning Konfigurasi</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Batasi pm.max_children</text>
  <text x="370" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Blokir serangan xmlrpc.php</text>
  <text x="370" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Hentikan query MySQL lambat</text>
  <text x="370" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Bunuh proses dengan kill -9</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#FEF3C7"/>
  <text x="480" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">Turunkan Beban Server</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="680" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">3. Solusi Modern</text>
  <text x="680" y="95" font-family="Inter, sans-serif" font-size="12" fill="#059669">LiteSpeed &amp; CloudLinux</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LiteSpeed LSCache hemat CPU</text>
  <text x="680" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• CloudLinux isolasi akun di LVE</text>
  <text x="680" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Server tetap aman &amp; stabil</text>
  <text x="680" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Lisensi murah LicenBase $4/bln</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#D1FAE5"/>
  <text x="790" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">Server Cepat &amp; Tangguh</text>
</svg>""",

    # 16. litespeed-license-pricing-costs-vps-requirements
    "litespeed-license-pricing-costs-vps-requirements-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t16 d16">
  <title id="t16">LiteSpeed Web Server Licensing Tiers &amp; Requirements</title>
  <desc id="d16">Overview of LiteSpeed Enterprise licensing tiers, worker processes, and hardware caps.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="260" height="6" rx="3" fill="#3B82F6"/>
  <text x="60" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Site Owner / Lite</text>
  <text x="60" y="95" font-family="Inter, sans-serif" font-size="12" fill="#2563EB">1 Worker Process</text>
  <path d="M60 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="60" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• 1 to 14 Domains</text>
  <text x="60" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Unlimited Server RAM</text>
  <text x="60" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Full LSCache Acceleration</text>
  <text x="60" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LicenBase rate: $4.00/mo</text>
  <rect x="60" y="310" width="220" height="38" rx="8" fill="#EFF6FF"/>
  <text x="170" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">Small VPS / Agencies</text>

  <rect x="350" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="350" y="35" width="260" height="6" rx="3" fill="#10B981"/>
  <text x="370" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Web Host Essential</text>
  <text x="370" y="95" font-family="Inter, sans-serif" font-size="12" fill="#059669">1 Worker / Unlimited Sites</text>
  <path d="M370 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="370" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Unlimited Domains</text>
  <text x="370" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Unlimited Server RAM</text>
  <text x="370" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Handles 10k-20k daily visitors</text>
  <text x="370" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• LicenBase rate: $4.00/mo</text>
  <rect x="370" y="310" width="220" height="38" rx="8" fill="#ECFDF5"/>
  <text x="480" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">Most Popular Hosting Tier</text>

  <rect x="660" y="35" width="260" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="660" y="35" width="260" height="6" rx="3" fill="#8B5CF6"/>
  <text x="680" y="70" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Professional &amp; Ent</text>
  <text x="680" y="95" font-family="Inter, sans-serif" font-size="12" fill="#7C3AED">2 to 4+ Worker Processes</text>
  <path d="M680 115 h220" stroke="#F1F5F9" stroke-width="1"/>
  <text x="680" y="150" font-family="Inter, sans-serif" font-size="12" fill="#475569">• High-Core Dedicated Nodes</text>
  <text x="680" y="185" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Massive WooCommerce load</text>
  <text x="680" y="220" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Peak concurrency handling</text>
  <text x="680" y="255" font-family="Inter, sans-serif" font-size="12" fill="#475569">• Wholesale savings up to 75%</text>
  <rect x="660" y="310" width="260" height="38" rx="8" fill="#F5F3FF"/>
  <text x="790" y="334" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#6D28D9" text-anchor="middle">Enterprise High Concurrency</text>
</svg>""",

    # 17. softaculous-license-vs-free-alternatives-costs
    "softaculous-license-vs-free-alternatives-costs-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t17 d17">
  <title id="t17">Softaculous Premium vs Free Installer Alternatives</title>
  <desc id="d17">Feature breakdown comparing Softaculous Premium against free tools.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#94A3B8"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Softaculous Free / CLI Tools</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#64748B">Limited Capabilities &amp; High Support Burden</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Free version limited to only ~50 scripts</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• No automated WordPress staging or cloning</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• WP-CLI has no GUI for shared hosting clients</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• No pre-upgrade automated safety backups</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Increased customer support ticket volume</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#F1F5F9"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">Restricted Feature Set</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Softaculous Premium (LicenBase)</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">Full 450+ Script Library at Just $1/mo</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 450+ 1-click install scripts (WordPress, Laravel)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 1-click WordPress staging, clone &amp; push-to-live</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Automatic pre-update backups &amp; rollbacks</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Full cPanel, Plesk &amp; DirectAdmin integration</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Wholesale rate: only $1.00 per month</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Essential for Every Hosting Server</text>
</svg>""",

    # 18. cloudlinux-license-guide-pricing-install-errors
    "cloudlinux-license-guide-pricing-install-errors-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t18 d18">
  <title id="t18">CloudLinux OS Architecture and Conversion Workflow</title>
  <desc id="d18">Overview of LVE tenant isolation and in-place cldeploy conversion.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">1. Download cldeploy</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">wget cldeploy script</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">2. Run In-Place Conversion</text>
  <text x="480" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">sh cldeploy -i &amp;&amp; reboot</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">3. CageFS &amp; LVE Governor</text>
  <text x="780" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Isolate each cPanel tenant</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">CloudLinux Server Hardening Capabilities</text>
  <text x="90" y="275" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ LVE Limits: Strict CPU (%), RAM (GB), IOPS, and entry process caps per user</text>
  <text x="90" y="305" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ CageFS: Virtual filesystem preventing users from viewing other accounts</text>
  <text x="90" y="335" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ HardenedPHP: Automated security patches for legacy PHP versions</text>
</svg>""",

    # 19. whmcs-license-activation-failed-fixes-guide
    "whmcs-license-activation-failed-fixes-guide-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t19 d19">
  <title id="t19">WHMCS License Activation Failed Diagnostic Flowchart</title>
  <desc id="d19">Troubleshooting steps to resolve WHMCS licensing failures and verification timeouts.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="60" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
  <text x="180" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">1. Trigger Reissue</text>
  <text x="180" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Reset IP / Domain / Directory</text>

  <line x1="300" y1="95" x2="360" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="360,95 352,90 352,100" fill="#94A3B8"/>

  <rect x="360" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">2. Test Port 443 cURL</text>
  <text x="480" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">curl -Iv licensing endpoint</text>

  <line x1="600" y1="95" x2="660" y2="95" stroke="#94A3B8" stroke-width="2"/>
  <polygon points="660,95 652,90 652,100" fill="#94A3B8"/>

  <rect x="660" y="50" width="240" height="90" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <text x="780" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">3. Check configuration.php</text>
  <text x="780" y="110" font-family="Inter, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Verify license key string</text>

  <rect x="60" y="210" width="840" height="160" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="90" y="245" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#0F172A">Essential WHMCS Diagnostics</text>
  <text x="90" y="275" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ License Reissue: Click Reissue in client portal when server IP or directory changes</text>
  <text x="90" y="305" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ Outbound HTTPS: Ensure firewall allows outgoing cURL requests on TCP port 443</text>
  <text x="90" y="335" font-family="Inter, sans-serif" font-size="13" fill="#475569">✔ LicenBase Rates: Authentic WHMCS licenses starting at $4/mo or $20 lifetime owned</text>
</svg>""",

    # 20. ucuz-cpanel-lisansi-vps-fiyatlar-secim-rehberi
    "ucuz-cpanel-lisansi-vps-fiyatlar-secim-rehberi-1": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="960" height="420" role="img" aria-labelledby="t20 d20">
  <title id="t20">Türkiye VPS Sunucuları İçin cPanel Lisansı Fiyat Karşılaştırması</title>
  <desc id="d20">Resmi bayi fiyatları ile LicenBase toptan IP lisanslama maliyet karşılaştırması.</desc>
  <rect width="960" height="420" rx="20" fill="#F8FAFC"/>
  <rect x="40" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="40" y="35" width="410" height="6" rx="3" fill="#EF4444"/>
  <text x="70" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">Resmi Bayi / Perakende Fiyatları</text>
  <text x="70" y="100" font-family="Inter, sans-serif" font-size="13" fill="#DC2626">Döviz Kuru Artışı ve Yüksek Maliyet</text>
  <path d="M70 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="70" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Solo (1 hesap): ~ 600 TL/ay ($17.49)</text>
  <text x="70" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Admin (5 hesap): ~ 1.050 TL/ay</text>
  <text x="70" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Pro (30 hesap): ~ 1.550 TL/ay</text>
  <text x="70" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel Premier: ~ 2.200 TL/ay</text>
  <text x="70" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Ajanslar ve hosting firmaları için yüksek yük</text>
  <rect x="70" y="325" width="350" height="38" rx="8" fill="#FEE2E2"/>
  <text x="245" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#991B1B" text-anchor="middle">Yüksek Perakende Maliyeti</text>

  <rect x="510" y="35" width="410" height="350" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="510" y="35" width="410" height="6" rx="3" fill="#10B981"/>
  <text x="540" y="75" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#0F172A">LicenBase Toptan IP Lisanslama</text>
  <text x="540" y="100" font-family="Inter, sans-serif" font-size="13" fill="#059669">%100 Orijinal Yazılım &amp; Güncellemeler</text>
  <path d="M540 120 h350" stroke="#F1F5F9" stroke-width="1"/>
  <text x="540" y="155" font-family="Inter, sans-serif" font-size="13" fill="#475569">• cPanel VPS Lisansı: sadece $4.00/ay (~140 TL)</text>
  <text x="540" y="190" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Resmi cPanel sunucularından doğrudan kurulum</text>
  <text x="540" y="225" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 60 saniyede IP üzerinden anında aktivasyon</text>
  <text x="540" y="260" font-family="Inter, sans-serif" font-size="13" fill="#475569">• 7/24 kesintisiz çalışma ve uzman destek</text>
  <text x="540" y="295" font-family="Inter, sans-serif" font-size="13" fill="#475569">• Yıllık sunucu giderlerinde %70'e varan tasarruf</text>
  <rect x="540" y="325" width="350" height="38" rx="8" fill="#D1FAE5"/>
  <text x="715" y="349" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Yılda 10.000 TL'den Fazla Tasarruf</text>
</svg>"""
}

for name, svg in SVGS.items():
    file_path = OUT_DIR / f"{name}.svg"
    file_path.write_text(svg, encoding="utf-8")
    print(f"Wrote {file_path}")

print(f"\nSuccessfully generated {len(SVGS)} SVGs!")

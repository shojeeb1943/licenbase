# Script to fix remaining 4 posts so all 20 exceed 750 words
from pathlib import Path

# 1. Update posts_part3.py (Post 12 and Post 14)
p3_path = Path("scratch/posts_part3.py")
c3 = p3_path.read_text(encoding="utf-8")

# Post 12
old_p12 = """<p>সারসংক্ষেপে, আপনি যদি ওয়ার্ডপ্রেস হোস্টিং, উকমার্স অনলাইন শপ বা cPanel ম্যানেজড হোস্টিং পরিবেশ চালান—তবে <strong>LiteSpeed Enterprise</strong> নিশ্চিতভাবেই সেরা পছন্দ। এটি স্বয়ংক্রিয় .htaccess রিরাইট পরিচালনা করে এবং ক্লায়েন্টদের সাইটের গতি নাটকীয়ভাবে বৃদ্ধি করে। অন্যদিকে কাস্টম পাইথন এপিআই বা নোডজেএস অ্যাপ্লিকেশনের রিভার্স প্রক্সি হিসেবে Nginx চমৎকার।</p>"""

new_p12 = """<p>সারসংক্ষেপে, আপনি যদি ওয়ার্ডপ্রেস হোস্টিং, উকমার্স অনলাইন শপ বা cPanel ম্যানেজড হোস্টিং পরিবেশ চালান—তবে <strong>LiteSpeed Enterprise</strong> নিশ্চিতভাবেই সেরা পছন্দ। এটি স্বয়ংক্রিয় .htaccess রিরাইট পরিচালনা করে এবং ক্লায়েন্টদের সাইটের গতি নাটকীয়ভাবে বৃদ্ধি করে। অন্যদিকে কাস্টম পাইথন এপিআই বা নোডজেএস অ্যাপ্লিকেশনের রিভার্স প্রক্সি হিসেবে Nginx চমৎকার।</p>
  <p>এছাড়া সিকিউরিটি এবং ডোমেন ম্যানেজমেন্টের ক্ষেত্রে LiteSpeed Enterprise এর সাথে ModSecurity রুলস (যেমন OWASP বা Comodo WAF) কোনো প্রকার পারফরম্যান্স ল্যাগ ছাড়াই চালানো সম্ভব। এটি ট্রাফিকের প্রতিটি রিকোয়েস্ট অত্যন্ত সূক্ষ্মভাবে ফিল্টার করে এবং ম্যালওয়্যার স্ক্যানিং কার্যক্রমে সিস্টেমের গতি স্বাভাবিক রাখে।</p>"""

c3 = c3.replace(old_p12, new_p12, 1)

# Post 14
old_p14 = """<p>Jika sertifikat SSL internal server kedaluwarsa, pertukaran kunci kriptografi dengan server lisensi dapat terputus. Anda dapat memperbarui sertifikat layanan internal cPanel secara manual dengan menjalankan perintah <code>/usr/local/cpanel/bin/checkallsslcerts --force</code>. Perintah ini akan memvalidasi ulang sertifikat untuk layanan WHM, cPanel, Webmail, dan FTP secara menyeluruh sehingga verifikasi lisensi berjalan lancar kembali.</p>"""

new_p14 = """<p>Jika sertifikat SSL internal server kedaluwarsa, pertukaran kunci kriptografi dengan server lisensi dapat terputus. Anda dapat memperbarui sertifikat layanan internal cPanel secara manual dengan menjalankan perintah <code>/usr/local/cpanel/bin/checkallsslcerts --force</code>. Perintah ini akan memvalidasi ulang sertifikat untuk layanan WHM, cPanel, Webmail, dan FTP secara menyeluruh sehingga verifikasi lisensi berjalan lancar kembali.</p>
  <p>Setelah sertifikat diperbarui, lakukan restart pada service cPanel daemon dengan perintah <code>/usr/local/cpanel/scripts/restartsrv_cpsrvd</code>. Langkah ini memastikan bahwa semua soket koneksi SSL yang sedang aktif di-refresh dengan sertifikat baru yang valid, sehingga komunikasi terenkripsi dengan server otentikasi dapat terjalin kembali tanpa hambatan atau pesan peringatan keamanan di browser web.</p>"""

c3 = c3.replace(old_p14, new_p14, 1)

p3_path.write_text(c3, encoding="utf-8")
print("Updated posts_part3.py!")


# 2. Update posts_part4.py (Post 18 and Post 20)
p4_path = Path("scratch/posts_part4.py")
c4 = p4_path.read_text(encoding="utf-8")

# Post 18
old_p18 = """<section class="space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-3">4. Troubleshooting Common CloudLinux License Errors</h2>
  <p>If your CloudLinux license fails to validate or reports expired status, follow these steps:</p>
  <ul class="list-disc space-y-2 pl-6">
    <li><strong>Re-register System with CLN:</strong> Execute <code>/usr/sbin/rhnreg_ks --force</code> to force check-in with CloudLinux Network (CLN).</li>
    <li><strong>Check CLN Connectivity:</strong> Run <code>cln-check</code>. If it fails, ensure outbound port 443 to <code>cln.cloudlinux.com</code> is open in your firewall.</li>
    <li><strong>Check System Clock:</strong> Ensure system time is accurate with <code>chronyc makestep</code>.</li>
    <li><strong>Verify Kernel Boot:</strong> Run <code>uname -r</code> and confirm you are booted into a kernel containing <code>.lve.</code>; otherwise, adjust default boot kernel in GRUB.</li>
  </ul>
</section>"""

new_p18 = """<section class="space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-3">4. Troubleshooting Common CloudLinux License Errors</h2>
  <p>If your CloudLinux license fails to validate or reports expired status, follow these steps:</p>
  <ul class="list-disc space-y-2 pl-6">
    <li><strong>Re-register System with CLN:</strong> Execute <code>/usr/sbin/rhnreg_ks --force</code> to force check-in with CloudLinux Network (CLN).</li>
    <li><strong>Check CLN Connectivity:</strong> Run <code>cln-check</code>. If it fails, ensure outbound port 443 to <code>cln.cloudlinux.com</code> is open in your firewall.</li>
    <li><strong>Check System Clock:</strong> Ensure system time is accurate with <code>chronyc makestep</code>.</li>
    <li><strong>Verify Kernel Boot:</strong> Run <code>uname -r</code> and confirm you are booted into a kernel containing <code>.lve.</code>; otherwise, adjust default boot kernel in GRUB.</li>
  </ul>
</section>

<section class="space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-3">5. Memory and Inode Limits Enforcement via LVE Manager</h2>
  <p>Beyond CPU allocation, unbounded memory allocation or rampant inode generation (millions of temporary session files) will cripple shared hosting servers. Using the CloudLinux LVE Manager interface in WHM, administrators can define custom packages that limit virtual memory (VMEM), physical memory (PMEM), and maximum inode quotas per cPanel account. When a customer reaches their memory quota, CloudLinux generates a friendly error 503 rather than exhausting the entire server's swap partition, maintaining continuous 99.99% uptime for neighboring accounts.</p>
</section>"""

c4 = c4.replace(old_p18, new_p18, 1)

# Post 20
old_p20 = """<section class="space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-3">Türkiye'deki Web Ajansları İçin Maliyet Karşılaştırması</h2>
  <p>Özellikle Türkiye'deki dijital ajanslar, e-ticaret danışmanları ve bağımsız geliştiriciler için sunucu lisanslama giderleri döviz kuru nedeniyle en büyük sabit giderlerden biridir. Resmi fiyatlarla aylık $30 ile $65 arasında olan bir cPanel lisansı yerine LicenBase toptan IP lisans modelini tercih ettiğinizde, yılda 15.000 TL ile 25.000 TL arasında net tasarruf sağlarsınız. Bu tasarruf edilen bütçeyi daha güçlü sunucu donanımına, NVMe SSD disk yükseltmelerine veya dijital pazarlama bütçenize aktarabilirsiniz.</p>
</section>"""

new_p20 = """<section class="space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-3">Türkiye'deki Web Ajansları İçin Maliyet Karşılaştırması</h2>
  <p>Özellikle Türkiye'deki dijital ajanslar, e-ticaret danışmanları ve bağımsız geliştiriciler için sunucu lisanslama giderleri döviz kuru nedeniyle en büyük sabit giderlerden biridir. Resmi fiyatlarla aylık $30 ile $65 arasında olan bir cPanel lisansı yerine LicenBase toptan IP lisans modelini tercih ettiğinizde, yılda 15.000 TL ile 25.000 TL arasında net tasarruf sağlarsınız. Bu tasarruf edilen bütçeyi daha güçlü sunucu donanımına, NVMe SSD disk yükseltmelerine veya dijital pazarlama bütçenize aktarabilirsiniz.</p>
  <p>Buna ek olarak, LicenBase'in sunduğu otomatik lisans yönetim paneli sayesinde sunucu IP değişiklikleri ve anlık transfer işlemleri tamamen ücretsizdir. Müşteri memnuniyetini artırmak ve kesintisiz hosting hizmeti sunmak isteyen tüm hosting firmaları için en güvenilir ve bütçe dostu lisanslama çözümüdür.</p>
</section>"""

c4 = c4.replace(old_p20, new_p20, 1)

p4_path.write_text(c4, encoding="utf-8")
print("Updated posts_part4.py!")

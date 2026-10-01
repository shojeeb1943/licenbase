"""Build about.html and contact.html (same shell as the blog pages: header/footer come from privacy-policy.html).
Only facts already stated elsewhere on the site are used (policies, support channels, product list).
Run:  python generate_company.py
"""
import html
from pathlib import Path

from generate_blog import BASE, crumbs, load_template, meta_block

EMAIL = "support@licenbase.com"
TICKET = "https://dashboard.licenbase.com/submitticket.php"
CLIENT_AREA = "https://dashboard.licenbase.com/clientarea.php"
LINK = 'class="font-semibold text-brand hover:underline"'
H2 = 'class="font-display text-2xl font-bold tracking-tight text-navy"'
CARD = 'class="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm"'

PRODUCTS = [
    ("cPanel & WHM", "cpanel-license"), ("LiteSpeed Web Server", "litespeed-license"),
    ("CloudLinux OS", "cloudlinux-license"), ("Plesk", "plesk-license"), ("WHMCS", "whmcs-license"),
    ("Imunify360", "imunify360-license"), ("JetBackup", "jetbackup-license"),
    ("Softaculous", "softaculous-license"), ("Virtualizor", "virtualizor-license"),
    ("SitePad", "sitepad-license"), ("WHMReseller", "whmreseller-license"),
    ("Webuzo", "webuzo-license"), ("WP Squared", "wp-squared-license"),
]

ABOUT_DESC = "LicenBase sells hosting software licenses for VPS and dedicated servers, including cPanel, LiteSpeed, CloudLinux and Plesk, activated on your server IP."
CONTACT_DESC = f"Contact LicenBase for pre-sales questions, order help and license support. Open a support ticket or email {EMAIL}."


def hero(crumb, h1, intro):
    return f"""
  <section class="border-b border-gray-200 bg-mist py-12 lg:py-16">
    <div class="lb-shell">
      <div class="max-w-3xl">
        <nav aria-label="Breadcrumb" class="mb-4 flex items-center gap-2 text-xs font-semibold text-gray-500">
          <a href="/" class="transition hover:text-brand">Home</a>
          <i data-lucide="chevron-right" class="h-3.5 w-3.5 text-gray-400"></i>
          <span class="text-brand">{crumb}</span>
        </nav>
        <h1 class="font-display text-3xl font-extrabold tracking-tight text-navy sm:text-4xl lg:text-5xl">{h1}</h1>
        <p class="mt-4 text-base leading-relaxed text-gray-600 sm:text-lg">{intro}</p>
      </div>
    </div>
  </section>
"""


def about_main():
    tiles = "".join(
        f'<a href="/{slug}" class="rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm font-semibold text-navy transition hover:border-brand/30 hover:text-brand">{html.escape(name)}</a>'
        for name, slug in PRODUCTS)
    steps = "".join(
        f'<div {CARD}><span class="grid h-8 w-8 place-items-center rounded-full bg-brandSoft text-sm font-bold text-brand">{n}</span><h3 class="mt-3 font-bold text-navy">{t}</h3><p class="mt-1 text-sm text-gray-600">{d}</p></div>'
        for n, (t, d) in enumerate([
            ("Choose a license", "Pick the product and plan that match your server, for example a cPanel VPS or dedicated license."),
            ("Provide your server IP", "Server licenses are bound to the public IP address of your server."),
            ("Activate", "The license is provisioned automatically once payment clears. Manage it from your client area."),
        ], 1))
    return hero("About", "About LicenBase",
                "LicenBase is a marketplace for hosting software licenses, built for hosting providers, resellers, agencies and anyone running their own VPS or dedicated server.") + f"""
  <section class="py-12 lg:py-16">
    <div class="lb-shell">
      <div class="mx-auto max-w-3xl space-y-12 leading-relaxed text-gray-700">

        <section class="space-y-4">
          <h2 {H2}>What we do</h2>
          <p>We sell licenses for the software that web hosting runs on: control panels, web servers, security, backup and billing tools. Licenses are provisioned automatically and tied to your server's IP address, so there is no key to copy around and no waiting for a manual setup.</p>
          <div class="grid gap-3 sm:grid-cols-2">{tiles}</div>
          <p><a href="/products" {LINK}>Browse all products</a> or see our <a href="/deals" {LINK}>combo deals</a>.</p>
        </section>

        <section class="space-y-4">
          <h2 {H2}>How it works</h2>
          <div class="grid gap-4 sm:grid-cols-3">{steps}</div>
        </section>

        <section class="space-y-4">
          <h2 {H2}>How our licenses are sourced</h2>
          <p>Hosting platform licenses on LicenBase, such as cPanel, LiteSpeed, CloudLinux and Plesk, are sourced and provisioned through independent licensing providers and authorized distributor networks. LicenBase is not directly affiliated with the software vendors, and all product names and trademarks belong to their owners.</p>
          <p>The details, including IP binding, migrations and compliance, are set out in our <a href="/license-policy" {LINK}>License Policy</a>.</p>
        </section>

        <section class="space-y-4">
          <h2 {H2}>Clear terms before you buy</h2>
          <p>Digital licenses are non-refundable once issued, but if a key does not work you can report it within 72 hours for a replacement or store credit. Read the full <a href="/refund-policy" {LINK}>Refund Policy</a>, <a href="/terms-of-service" {LINK}>Terms of Service</a> and <a href="/privacy-policy" {LINK}>Privacy Policy</a>.</p>
        </section>

        <section class="space-y-4 rounded-2xl border border-gray-200 bg-mist p-6">
          <h2 {H2}>Talk to us</h2>
          <p>Questions before you order, or need help with a license? Email <a href="mailto:{EMAIL}" {LINK}>{EMAIL}</a> or visit the <a href="/contact" {LINK}>contact page</a>.</p>
        </section>

      </div>
    </div>
  </section>
"""


def contact_main():
    def ch(icon, title, text, href, label):
        return f"""<div {CARD}>
            <span class="grid h-10 w-10 place-items-center rounded-xl bg-brandSoft text-brand"><i data-lucide="{icon}" class="h-5 w-5"></i></span>
            <h2 class="mt-4 font-display text-lg font-bold text-navy">{title}</h2>
            <p class="mt-2 text-sm leading-relaxed text-gray-600">{text}</p>
            <a href="{href}" class="lb-btn lb-btn--secondary mt-5 w-full text-center">{label}</a>
          </div>"""
    cards = "".join([
        ch("life-buoy", "Support ticket", "Best for existing orders: license activation, IP changes and technical problems. A ticket keeps your order details and our replies in one place.", TICKET, "Open a ticket"),
        ch("mail", "Email", f"For pre-sales questions, billing and anything else. Write to {EMAIL}.", f"mailto:{EMAIL}", "Send an email"),
        ch("layout-dashboard", "Client area", "Sign in to view your orders and licenses, and to manage your account.", CLIENT_AREA, "Go to dashboard"),
    ])
    return hero("Contact", "Contact LicenBase",
                "Pre-sales questions, order help or a license problem? Pick the channel that fits and we will get back to you.") + f"""
  <section class="py-12 lg:py-16">
    <div class="lb-shell">
      <div class="grid gap-6 md:grid-cols-3">
          {cards}
      </div>

      <div class="mx-auto mt-14 grid max-w-4xl gap-8 md:grid-cols-2">
        <section class="space-y-3 leading-relaxed text-gray-700">
          <h2 {H2}>What to include</h2>
          <p>You will get a faster answer if you send:</p>
          <ul class="list-disc space-y-2 pl-6">
            <li>Your order number, if you have one</li>
            <li>The product and plan (for example cPanel VPS)</li>
            <li>Your server's public IP address</li>
            <li>Your operating system and a short description of the problem</li>
          </ul>
        </section>
        <section class="space-y-3 leading-relaxed text-gray-700">
          <h2 {H2}>Before you write</h2>
          <ul class="list-disc space-y-2 pl-6">
            <li>Not working key? Report it within 72 hours. See the <a href="/refund-policy" {LINK}>Refund Policy</a>.</li>
            <li>Moving a server or changing IP? See the <a href="/license-policy" {LINK}>License Policy</a>.</li>
            <li>Setting up cPanel? Our <a href="/blog/install-cpanel-license-vps" {LINK}>installation guide</a> covers the common errors.</li>
            <li>Choosing a product? Compare <a href="/products" {LINK}>all licenses</a>.</li>
          </ul>
        </section>
      </div>
    </div>
  </section>
"""


def build(tpl, *, file, path, title, og_title, desc, image, image_alt, ld, main):
    head_a, head_b, tail = tpl
    head = meta_block(title=title, desc=desc, path=path, image=f"{BASE}/assets/img/og/{image}.png",
                      image_alt=image_alt, og_type="website", og_title=og_title, ld=ld)
    Path(file).write_text(head_a + head + head_b + "\n" + main + "\n" + tail, encoding="utf-8", newline="\n")
    print("wrote", file)


if __name__ == "__main__":
    tpl, tpl_contact = load_template(None), load_template("contact")
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "LicenBase", "url": BASE + "/",
           "logo": BASE + "/assets/img/logo.png", "email": EMAIL}
    build(tpl, file="about.html", path="/about", title="About LicenBase | Hosting Software Licenses",
          og_title="About LicenBase", desc=ABOUT_DESC, image="about",
          image_alt="About LicenBase – hosting software licenses",
          ld=[crumbs([("Home", "/"), ("About", "/about")]),
              {"@context": "https://schema.org", "@type": "AboutPage", "name": "About LicenBase", "url": BASE + "/about", "about": org}],
          main=about_main())
    build(tpl_contact, file="contact.html", path="/contact", title="Contact LicenBase | Sales &amp; License Support",
          og_title="Contact LicenBase", desc=CONTACT_DESC, image="contact",
          image_alt="Contact LicenBase – sales and license support",
          ld=[crumbs([("Home", "/"), ("Contact", "/contact")]),
              {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact LicenBase", "url": BASE + "/contact",
               "mainEntity": {**org, "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "email": EMAIL, "url": TICKET}}}],
          main=contact_main())

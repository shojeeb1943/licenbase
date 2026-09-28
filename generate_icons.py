import os

os.makedirs('assets/img/icons', exist_ok=True)

icons = {
    'litespeed.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <path d="M48 8C48 8 72 32 72 54C72 68 62 80 48 80C34 80 24 68 24 54C24 42 34 24 48 8Z" fill="#0070BA"/>
  <path d="M64 28C64 28 88 52 88 70C88 82 80 92 68 92C56 92 48 82 48 70C48 58 56 42 64 28Z" fill="#00A2FF" opacity="0.9"/>
  <path d="M36 40C36 40 52 56 52 68C52 76 46 82 38 82C30 82 24 76 24 68C24 60 30 50 36 40Z" fill="#38BDF8" opacity="0.8"/>
</svg>''',

    'cloudlinux.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <path d="M78 58C78 48 70 40 60 40C58.5 40 57 40.3 55.6 40.8C52.8 30.8 43.6 24 33 24C19.7 24 9 34.7 9 48C9 49.3 9.1 50.6 9.4 51.8C4.1 54.4 0.5 59.8 0.5 66C0.5 74.8 7.7 82 16.5 82H76C83.7 82 90 75.7 90 68C90 62.8 87.2 58.2 82.8 55.7" fill="#1B4D89"/>
  <circle cx="66" cy="34" r="12" fill="#F4911E"/>
  <path d="M66 16V22M66 46V52M48 34H54M78 34H84M53.3 21.3L57.5 25.5M74.5 42.5L78.7 46.7M53.3 46.7L57.5 42.5M74.5 25.5L78.7 21.3" stroke="#F4911E" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    'whmcs.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#52BBE6"/>
  <path d="M22 32L36 50L22 68H32L41 56L50 68H60L46 50L60 32H50L41 44L32 32H22Z" fill="white"/>
  <path d="M62 32H72V68H62V32Z" fill="white"/>
  <circle cx="80" cy="63" r="5" fill="#FF6C2C"/>
</svg>''',

    'imunify360.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <path d="M50 10L18 24V48C18 68 32 86 50 92C68 86 82 68 82 48V24L50 10Z" fill="#10B981"/>
  <path d="M50 18L24 30V48C24 64 35 79 50 84C65 79 76 64 76 48V30L50 18Z" fill="#047857"/>
  <circle cx="50" cy="50" r="16" stroke="#ECFDF5" stroke-width="4" stroke-dasharray="6 4" fill="none"/>
  <path d="M42 50L48 56L60 42" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

    'jetbackup.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#4F46E5"/>
  <path d="M26 62C26 62 36 44 50 44C64 44 74 62 74 62" stroke="white" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M50 24V52M50 24L38 36M50 24L62 36" stroke="#38BDF8" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="50" cy="74" r="5" fill="#38BDF8"/>
</svg>''',

    'virtualizor.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#7C3AED"/>
  <path d="M24 34L50 20L76 34L50 48L24 34Z" fill="#DDD6FE"/>
  <path d="M24 48L50 62L76 48" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M24 64L50 78L76 64" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>''',

    'softaculous.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#0D9488"/>
  <path d="M50 18C50 18 34 32 34 56C34 68 42 78 50 82C58 78 66 68 66 56C66 32 50 18 50 18Z" fill="white"/>
  <circle cx="50" cy="46" r="7" fill="#F59E0B"/>
  <path d="M28 66C24 72 26 78 26 78C26 78 32 78 38 72" fill="#F59E0B"/>
  <path d="M72 66C76 72 74 78 74 78C74 78 68 78 62 72" fill="#F59E0B"/>
</svg>''',

    'sitepad.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#EA580C"/>
  <rect x="22" y="24" width="56" height="42" rx="6" fill="white"/>
  <rect x="22" y="24" width="56" height="10" rx="4" fill="#C2410C"/>
  <circle cx="28" cy="29" r="2" fill="white"/>
  <circle cx="34" cy="29" r="2" fill="white"/>
  <circle cx="40" cy="29" r="2" fill="white"/>
  <path d="M48 48L68 68L78 58L58 38L48 48Z" fill="#F97316" stroke="white" stroke-width="2"/>
  <path d="M44 52L48 48L46 54L44 52Z" fill="#7C2D12"/>
</svg>''',

    'webuzo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#6366F1"/>
  <circle cx="50" cy="50" r="28" stroke="white" stroke-width="5" fill="none"/>
  <path d="M34 50L44 60L66 38" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="50" cy="22" r="5" fill="#38BDF8"/>
  <circle cx="78" cy="50" r="5" fill="#38BDF8"/>
  <circle cx="50" cy="78" r="5" fill="#38BDF8"/>
  <circle cx="22" cy="50" r="5" fill="#38BDF8"/>
</svg>''',

    'wp-squared.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#E11D48"/>
  <circle cx="46" cy="50" r="24" stroke="white" stroke-width="4" fill="none"/>
  <path d="M32 40L42 64L48 50L54 64L64 40" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="70" y="38" fill="white" font-family="sans-serif" font-size="22" font-weight="bold">2</text>
</svg>''',

    'whmreseller.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#2563EB"/>
  <circle cx="50" cy="32" r="12" fill="white"/>
  <circle cx="30" cy="68" r="10" fill="#93C5FD"/>
  <circle cx="70" cy="68" r="10" fill="#93C5FD"/>
  <path d="M50 44V54M50 54L30 58M50 54L70 58" stroke="white" stroke-width="3" stroke-linecap="round"/>
</svg>'''
}

for name, code in icons.items():
    path = os.path.join('assets/img/icons', name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code.strip())
    print(f'Generated {name}')

print('All 13 product SVGs ready in assets/img/icons/')

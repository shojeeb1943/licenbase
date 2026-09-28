import os
import urllib.request

os.makedirs('assets/img/icons', exist_ok=True)

# Official & high quality vector definitions
icons = {
    'cpanel.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#1A120B"/>
  <path d="M22 34H42C48 34 52 38 52 44C52 50 48 54 42 54H32V66H22V34Z" fill="#FF6C2C"/>
  <path d="M50 34H70C76 34 80 38 80 44C80 50 76 54 70 54H60V66H50V34Z" fill="#FF8A50"/>
  <path d="M30 66H46C52 66 56 70 56 76C56 82 52 86 46 86H22L30 66Z" fill="#FF6C2C"/>
  <path d="M58 66H74C80 66 84 70 84 76C84 82 80 86 74 86H50L58 66Z" fill="#FF8A50"/>
</svg>''',

    'plesk.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#00263E"/>
  <path d="M26 24H44C54 24 62 30 62 40C62 50 54 56 44 56H36V76H26V24Z" fill="#53BCE6"/>
  <circle cx="44" cy="40" r="6" fill="#00263E"/>
  <path d="M48 48L74 76H60L40 54L48 48Z" fill="#00A3E0"/>
  <path d="M62 24H74V50H62V24Z" fill="#FFFFFF" opacity="0.9"/>
</svg>''',

    'litespeed.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#0B192C"/>
  <path d="M50 12C50 12 76 36 76 58C76 72 65 84 50 84C35 84 24 72 24 58C24 45 35 28 50 12Z" fill="#0070BA"/>
  <path d="M65 30C65 30 86 52 86 68C86 80 77 88 66 88C55 88 48 80 48 68C48 56 56 42 65 30Z" fill="#00A2FF" opacity="0.9"/>
  <path d="M38 42C38 42 54 56 54 68C54 75 48 80 41 80C34 80 28 75 28 68C28 60 33 50 38 42Z" fill="#38BDF8"/>
  <path d="M46 34L58 20L54 40L68 36L42 68L48 46L36 50L46 34Z" fill="#FFFFFF"/>
</svg>''',

    'cloudlinux.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#0F2744"/>
  <path d="M74 58C74 49 67 42 58 42C56.6 42 55.3 42.3 54 42.7C51.5 33.7 43.2 28 33.6 28C21.6 28 12 37.6 12 49.6C12 50.8 12.1 52 12.4 53.1C7.6 55.4 4.4 60.3 4.4 65.8C4.4 73.7 10.9 80.2 18.8 80.2H72.2C79.1 80.2 84.8 74.5 84.8 67.6C84.8 62.9 82.3 58.8 78.3 56.5" fill="#2B72C4"/>
  <circle cx="66" cy="34" r="10" fill="#F4911E"/>
  <path d="M66 18V23M66 45V50M50 34H55M77 34H82M54.7 22.7L58.2 26.2M73.8 41.8L77.3 45.3M54.7 45.3L58.2 41.8M73.8 26.2L77.3 22.7" stroke="#F4911E" stroke-width="2.5" stroke-linecap="round"/>
</svg>''',

    'whmcs.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#52BBE6"/>
  <path d="M20 32L34 52L20 72H31L40 58L49 72H60L46 52L60 32H49L40 46L31 32H20Z" fill="white"/>
  <path d="M63 32H73V72H63V32Z" fill="white"/>
  <circle cx="81" cy="66" r="5.5" fill="#FF6C2C"/>
</svg>''',

    'imunify360.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#064E3B"/>
  <path d="M50 14L22 26V48C22 66 34 82 50 88C66 82 78 66 78 48V26L50 14Z" fill="#10B981"/>
  <path d="M50 22L28 32V48C28 62 37 76 50 81C63 76 72 62 72 48V32L50 22Z" fill="#047857"/>
  <circle cx="50" cy="50" r="15" stroke="#A7F3D0" stroke-width="3" stroke-dasharray="5 3" fill="none"/>
  <path d="M42 50L48 56L60 42" stroke="white" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

    'jetbackup.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#1E1B4B"/>
  <path d="M26 64C26 64 36 46 50 46C64 46 74 64 74 64" stroke="#818CF8" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M50 20V50M50 20L36 34M50 20L64 34" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="50" cy="74" r="6" fill="#38BDF8"/>
</svg>''',

    'virtualizor.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#4C1D95"/>
  <path d="M22 34L50 18L78 34L50 50L22 34Z" fill="#C4B5FD"/>
  <path d="M22 48L50 64L78 48" stroke="white" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M22 64L50 80L78 64" stroke="white" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>''',

    'softaculous.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#115E59"/>
  <path d="M50 16C50 16 32 32 32 56C32 69 40 80 50 84C60 80 68 69 68 56C68 32 50 16 50 16Z" fill="#CCFBF1"/>
  <circle cx="50" cy="46" r="8" fill="#F59E0B"/>
  <path d="M24 68C20 74 24 80 24 80C24 80 30 80 36 74" fill="#F59E0B"/>
  <path d="M76 68C80 74 76 80 76 80C76 80 70 80 64 74" fill="#F59E0B"/>
</svg>''',

    'sitepad.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#9A3412"/>
  <rect x="20" y="22" width="60" height="46" rx="6" fill="white"/>
  <rect x="20" y="22" width="60" height="12" rx="4" fill="#EA580C"/>
  <circle cx="27" cy="28" r="2.5" fill="white"/>
  <circle cx="34" cy="28" r="2.5" fill="white"/>
  <circle cx="41" cy="28" r="2.5" fill="white"/>
  <path d="M46 50L68 72L80 60L58 38L46 50Z" fill="#F97316" stroke="white" stroke-width="2.5"/>
  <path d="M42 54L46 50L44 56L42 54Z" fill="#7C2D12"/>
</svg>''',

    'webuzo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#3730A3"/>
  <circle cx="50" cy="50" r="28" stroke="#A5B4FC" stroke-width="4.5" fill="none"/>
  <path d="M34 50L44 60L66 38" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="50" cy="22" r="5.5" fill="#38BDF8"/>
  <circle cx="78" cy="50" r="5.5" fill="#38BDF8"/>
  <circle cx="50" cy="78" r="5.5" fill="#38BDF8"/>
  <circle cx="22" cy="50" r="5.5" fill="#38BDF8"/>
</svg>''',

    'wp-squared.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#881337"/>
  <circle cx="45" cy="50" r="25" stroke="#FECDD3" stroke-width="4" fill="none"/>
  <path d="M30 38L40 64L47 48L54 64L64 38" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="70" y="36" fill="#FB7185" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="900">2</text>
</svg>''',

    'whmreseller.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#1E3A8A"/>
  <circle cx="50" cy="30" r="12" fill="#60A5FA"/>
  <circle cx="28" cy="70" r="10" fill="#93C5FD"/>
  <circle cx="72" cy="70" r="10" fill="#93C5FD"/>
  <path d="M50 42V54M50 54L28 60M50 54L72 60" stroke="white" stroke-width="3.5" stroke-linecap="round"/>
</svg>'''
}

for name, code in icons.items():
    path = os.path.join('assets/img/icons', name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code.strip())

print('Verified all 13 SVG icons.')

import os
import glob

html_files = glob.glob("*.html")
py_files = ["generate_pages.py", "build_real_svg_pages.py"]

all_files = html_files + [f for f in py_files if os.path.exists(f)]

count = 0
for filename in all_files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    # Replace in header signin link
    new_content = new_content.replace(
        '<a href="https://dashboard.licenbase.com/clientarea.php" class="lb-header-signin">Sign In</a>',
        '<a href="https://dashboard.licenbase.com/clientarea.php" class="lb-header-signin">Dashboard</a>'
    )
    # Replace in mobile menu drawer
    new_content = new_content.replace(
        'class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy hover:bg-mist">Sign In</a>',
        'class="lb-mobile-link block rounded-xl px-3 py-2.5 font-semibold text-navy hover:bg-mist">Dashboard</a>'
    )
    new_content = new_content.replace(
        'class="lb-mobile-link block rounded-xl px-3 py-3 text-[15px] font-semibold text-navy transition hover:bg-mist">Sign In</a>',
        'class="lb-mobile-link block rounded-xl px-3 py-3 text-[15px] font-semibold text-navy transition hover:bg-mist">Dashboard</a>'
    )

    if new_content != content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filename}")

print(f"Successfully renamed 'Sign In' to 'Dashboard' across {count} files.")

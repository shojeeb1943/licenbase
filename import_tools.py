"""Rebuild /tools from the LicenBase NetDash fork and import it. Idempotent.

    python import_tools.py [--src C:\dev\netdash-toolkit] [--no-build]

1. emit the LicenBase header/footer/CTA into the fork (lib/lb-chrome.generated.ts) and refresh assets/css|js/tools-*
2. pnpm build:app in the fork (static export to out/)
3. replace tools/ with out/
4. brand_tools.py, fix_tools_titles.py, make_sitemap.py (all idempotent; the fork already emits the branding, so they mostly no-op)
"""
import argparse, os, shutil, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument('--src', default=r'C:\dev\netdash-toolkit')
ap.add_argument('--no-build', action='store_true', help='reuse the existing out/ folder')
args = ap.parse_args()
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)


def run(cmd, cwd=None):
    print('>', cmd)
    if subprocess.run(cmd, cwd=cwd, shell=True).returncode:
        sys.exit(f'FAILED: {cmd}')


out = os.path.join(args.src, 'out')
if not args.no_build:
    # a leftover .next from `next dev` leaks hot-update and fallback chunks into the export
    for d in ('.next', 'out'):
        shutil.rmtree(os.path.join(args.src, d), ignore_errors=True)
    run(f'python build_tools_header.py --emit-ts "{args.src}"')
    run('pnpm build:app', cwd=args.src)
if not os.path.isfile(os.path.join(out, 'index.html')):
    sys.exit(f'no build at {out}')

shutil.rmtree('tools', ignore_errors=True)
shutil.copytree(out, 'tools')
run('python brand_tools.py')
run('python fix_tools_titles.py')
run('python make_sitemap.py')
print('imported', sum(1 for _ in os.scandir('tools')), 'entries into tools/')

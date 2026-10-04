r"""Rebuild /tools from the LicenBase NetDash fork and import it. Idempotent.

    python import_tools.py [--src C:\dev\netdash-toolkit] [--no-build] [--force]

0. refuse to run in a state that loses work or ships unfinished work (see preflight; --force skips it)
1. emit the LicenBase header/footer/CTA and the tab icon into the fork (lib/lb-chrome.generated.ts, app/icon.svg,
   public/favicon.svg) from the site's own files, and refresh assets/css|js/tools-*
2. pnpm build:app in the fork (static export to out/)
3. replace tools/ with out/
4. brand_tools.py, fix_tools_titles.py, make_sitemap.py (all idempotent; the fork already emits the branding, so they mostly no-op)
5. verify_tools_branding.py; if it fails, tools/ is restored to the last commit so a bad build can never be committed

Never edit tools/ by hand: this script deletes it. Change the fork (and COMMIT it) or the files in assets/.
"""
import argparse, os, shutil, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument('--src', default=r'C:\dev\netdash-toolkit')
ap.add_argument('--no-build', action='store_true', help='reuse the existing out/ folder')
ap.add_argument('--force', action='store_true', help='skip the preflight checks and the automatic rollback')
args = ap.parse_args()
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

# files this script regenerates inside the fork on every run: they may legitimately differ from the last commit
GENERATED = {'lib/lb-chrome.generated.ts', 'app/icon.svg', 'public/favicon.svg'}


def run(cmd, cwd=None):
    print('>', cmd)
    if subprocess.run(cmd, cwd=cwd, shell=True).returncode:
        sys.exit(f'FAILED: {cmd}')


def git(*a, cwd=None):
    return subprocess.run(['git', *a], cwd=cwd, capture_output=True, text=True).stdout


def preflight():
    problems = []
    # 1. tools/ is generated: uncommitted changes there are either a hand edit or another unfinished import,
    #    and the rmtree below would destroy them
    dirty = [l for l in git('status', '--porcelain', '--', 'tools').splitlines() if l.strip()]
    if dirty:
        problems.append(f'tools/ has {len(dirty)} uncommitted change(s), e.g. {dirty[0].strip()}. Commit or discard them first.')
    if not args.no_build:
        # 2. the build reads the fork's working tree, so uncommitted edits there would ship unreviewed,
        #    and a checkout that lacks a fix would silently ship the old behaviour
        branch = git('rev-parse', '--abbrev-ref', 'HEAD', cwd=args.src).strip()
        if branch != 'licenbase':
            problems.append(f'the fork is on branch "{branch}", expected "licenbase".')
        changed = [l for l in git('status', '--porcelain', cwd=args.src).splitlines() if l[3:].strip() not in GENERATED]
        if changed:
            problems.append(f'the fork has {len(changed)} uncommitted change(s), e.g. {changed[0].strip()}. Commit them in {args.src} first.')
    if problems:
        print('Refusing to import:')
        for p in problems:
            print(' -', p)
        print('Fix the above, or rerun with --force if you really mean it.')
        sys.exit(2)


if not args.force:
    preflight()

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
shutil.copytree(out, 'tools', dirs_exist_ok=True)
run('python brand_tools.py')
run('python fix_tools_titles.py')
run('python make_sitemap.py')

if subprocess.run([sys.executable, 'verify_tools_branding.py']).returncode:
    if args.force:
        sys.exit('Branding check FAILED (--force: tools/ left as built).')
    # preflight guaranteed tools/ was clean, so this only discards the bad build
    subprocess.run(['git', 'checkout', '--', 'tools'])
    subprocess.run(['git', 'clean', '-fdq', 'tools'])
    sys.exit('Branding check FAILED: tools/ was restored to the last commit. Fix the cause (usually an uncommitted or reverted change in the fork) and rerun.')
print('imported', sum(1 for _ in os.scandir('tools')), 'entries into tools/')

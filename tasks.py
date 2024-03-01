from invoke import task
import yaml

from tasklib.html import *
from tasklib.util import *
from tasklib.walk import *

repo_root = Path(__file__).parent


@task
def update_modules(ctx, root):
    """Update all of the module directories with settings files, scripts, etc. """

    for dir_ in walk_modules(root):
        make_dirs(dir_)
        write_classpath(dir_)
        write_settings(dir_)
        write_gitignore(dir_)
        write_launch(dir_)
        copy_devcontainer(repo_root, dir_)
        # copy_scripts(dir_)
        disable_eclipse(dir_)


#
# Push to the final module repos. 
#


@task
def push(ctx, root, build_dir=None):
    """Upload the module in the current dir to Github"""

    if build_dir is None:
        build_dir = repo_root / "_build"

    build_dir = Path(build_dir)

    for dir_ in walk_modules(root):
        create_repo(ctx, dir_, build_dir)
        # make_repo_template(dir_)


#
# Misc
#


@task
def move_pde_assign(ctx, root):
    pde = list(Path(root).glob('**/*.pde'))
    for f in pde:
        new_path = Path(str(f).replace("Level0", "Level0PDE"))
        new_path.parent.mkdir(parents=True, exist_ok=True)
        f.rename(new_path)


def _proc_html(f):
    l, m, ls, a = get_lmla(f)

    print("Downloading ", f)
    web_dir = f.parent / '.web'
    web_dir.mkdir(exist_ok=True)

    urls = extract_urls(f.read_text())

    try:
        if not urls or len(urls) < 1:
            # Thre is no link in the recipe text, so it
            # is the text itself.
            download_webpage_assets(f.read_text(), web_dir)
        else:
            download_webpage_assets(urls[0], web_dir)

    except Exception as e:
        print("ERROR: Failed to download ", f)
        print(e)

    # f.rename(web_dir / f.name)


@task
def fetch_web(ctx, root):
    """Walk the levels looking for html files and download the assets"""
    root = Path(root)

    for f in root.glob("**/*.html"):
        if '/bin/' in str(f):
            continue

        if '/.web/' in str(f):
            continue

        _proc_html(f)


@task
def create_meta(ctx, root):
    """Create the .meta files for the assignments, while hold information
    used in creating README, images, and assigment pages."""

    import yaml

    metas = []

    for l in walk_assignments(Path(root)):
        java = list(l.glob('*.java'))
        pde = list(l.glob('*.pde'))
        web = (l / '.web').exists()
        r = process_dir(root, l)
        if r:
            (l / '.meta').write_text(yaml.dump(r, indent=2))
            # print("Wrote ",  (l/'.meta') )
            metas.append(r)
        else:
            print("No meta ", l)

    (repo_root / 'meta.yaml').write_text(yaml.dump(metas, indent=2))

@task
def make_readme(cts, root):
    """Process the web pages in the .web directories"""
    root = Path(root)

    for f in root.glob("**/.meta"):
        m = yaml.load(f.read_text(), Loader=yaml.SafeLoader)

        adir = f.parent
        images_dir = adir / 'images'

        images_dir.mkdir(parents=True, exist_ok=True)

        for r in m['resources']:
            r = Path(r)
            shutil.copy(r, images_dir / r.name)

        (f.parent / 'README.md').write_text(m['text'])
import os
import sys
import copy

from sphinx import quickstart
from sphinx.quickstart import generate

d = {}

additional_config = """
# ----- blockdiag settings
extensions.extend([
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
])

blockdiag_fontpath = '/fonts/ipag00303/ipag.ttf'
seqdiag_fontpath = '/fonts/ipag00303/ipag.ttf'
actdiag_fontpath = '/fonts/ipag00303/ipag.ttf'
nwdiag_fontpath = '/fonts/ipag00303/ipag.ttf'

blockdiag_antialias = True
seqdiag_antialias = True
actdiag_antialias = True
nwdiag_antialias = True

# ----- Read the Docs Theme
html_theme = "sphinx_rtd_theme"

# ----- pdf print styles settings
def setup(app):
    app.add_stylesheet('css/print-reset.css')
    app.add_stylesheet('css/print-theme-default.css')
    app.add_javascript('js/print.js')

"""

additional_make = """
livehtml:
\tsphinx-autobuild -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
"""


def patch_generate(original_d, overwrite=True, silent=False, templatedir=None):
    global d
    d = copy.copy(original_d)
    generate(original_d, overwrite, silent=False, templatedir=None)


def main(argv=sys.argv[1:]):
    # Patch original generate function
    quickstart.generate = patch_generate

    # Run sphinx-quickstart
    return_code = quickstart.main(argv)

    if return_code: 
        return return_code

    # TODO: quickstart.get_parser を拡張する
    # Sphinx 1.6.5 で下記対応がなされているが、pip install した Sphinx 1.6.5 で
    # このコードが存在しないため、反映されたら実装をする
    # https://github.com/sphinx-doc/sphinx/commit/101b2893516dbbfb92767efff1c30488e651ccfc
    # いまいまは直書きで対応する
    #
    # https://github.com/pashango2/sphinx-qsp
    # これにPR送ってもよし
    srcdir = d['sep'] and os.path.join(d['path'], 'source') or d['path']
    conf_path = os.path.join(srcdir, 'conf.py')
    make_path = os.path.join(d['path'], 'Makefile')

    with open(conf_path, 'a') as f:
        f.write(additional_config)

    if d.get('makefile', False):
        with open(make_path, 'a') as f:
            f.write(additional_make)

    # Copy files for pdf print style
    if d.get('pdf_print_style', False):
        source = d['sep'] and os.path.join(d['path'], 'source') or d['path']
        prefix = d['dot'] or '_'
        shutil.copytree('/files/css', f'{source}/{prefix}static/css')
        shutil.copytree('/files/js', f'{source}/{prefix}static/js')

    if return_code:
        return return_code

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

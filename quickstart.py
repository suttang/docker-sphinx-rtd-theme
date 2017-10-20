import sys
import os
import shutil

from sphinx_qsp import quickstart_plus


def main(argv=None):
    sphinx_blockdiag_extension = quickstart_plus.Extension(
        "ext_blockdiag", "use blockdiag diagrams",
        conf_py="""
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

"""
    )

    sphinx_rtd_theme_extension = quickstart_plus.Extension(
        "ext_rtd_theme", "use Read the Doc theme",
        conf_py="""
# ----- Read the Docs Theme
html_theme = "sphinx_rtd_theme"

"""
    )

    sphinx_pdf_print_style = quickstart_plus.Extension(
        "pdf_print_style", "use PDF print styles",
        conf_py="""
# ----- pdf print styles settings
def setup(app):
    app.add_stylesheet('css/print-reset.css')
    app.add_stylesheet('css/print-theme-default.css')
    app.add_javascript('js/print.js')

"""
    )

    sphinx_autobuild_extension = quickstart_plus.AutoBuildExtension(
        "ext_autobuild", "Watch a directory and rebuild the documentation",
        makefile="""
livehtml:
\tsphinx-autobuild -b html {0} $(ALLSPHINXOPTS) $(BUILDDIR)/html
""",
        new_makefile="""
livehtml:
\tsphinx-autobuild -b html {0} $(SOURCEDIR) $(BUILDDIR)/html
""",
    )

    quickstart_plus.qsp_extensions = [
        sphinx_blockdiag_extension,
        sphinx_rtd_theme_extension,
        sphinx_autobuild_extension,
        sphinx_pdf_print_style
    ]

    # Run sphinx-quickstart-plus.
    quickstart_plus.main(argv)

    # Copy files for pdf print style
    d = quickstart_plus.hook_d
    if d['pdf_print_style']:
        source = d['sep'] and os.path.join(d['path'], 'source') or d['path']
        prefix = d['dot'] or '_'
        shutil.copytree('/files/css', f'{source}/{prefix}static/css')
        shutil.copytree('/files/js', f'{source}/{prefix}static/js')


if __name__ == '__main__':
    main(sys.argv)

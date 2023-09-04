# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Problem Package Format'
copyright = 'unknown'
author = 'various'

release = 'draft'
version = '0.9.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'myst_parser'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinxdoc'

# -- Options for EPUB output
epub_show_urls = 'footnote'
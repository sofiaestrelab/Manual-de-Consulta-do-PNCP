# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information
project = 'Manual de Consulta do PNCP'
copyright = '2026, Ministério da Gestão e Inovação em Serviços Públicos - MGI'
author = 'COPNCP/CGGES/DELOG/SEGES/MGI'

# The full version, including alpha/beta/rc tags
release = '2.0'
version = '2.0'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

# Language
language = 'pt_BR'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for singlehtml output
singlehtml_show_toc = True

# -- Options for PDF output
latex_documents = [
    ('index', 'manual-pncp.tex', 'Manual de Consulta do PNCP',
     'COPNCP/CGGES/DELOG/SEGES/MGI', 'manual'),
]
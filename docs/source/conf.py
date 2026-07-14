import os
import sys

# Adiciona o diretório atual ao path
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

# Caminhos
templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for singlehtml output
singlehtml_show_toc = True

# -- Exclude build files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Source file patterns
source_suffix = '.rst'
master_doc = 'index'
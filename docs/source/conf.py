import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from . import __version__, __author__, __copyright__

project = 'Manual de Consulta do PNCP'
copyright = __copyright__
author = __author__

release = __version__
version = __version__

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']
html_static_path = ['_static']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv',
    'venv',
    'env',
    '*.pdf',
    '**/__pycache__',
    '*.pyc',
]

source_suffix = {
    '.rst': 'restructuredtext',
}

language = 'pt_BR'
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}

html_context = {
    'display_github': True,
    'github_user': 'SEU_USUARIO_GITHUB',
    'github_repo': 'NOME_DO_REPOSITORIO',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

autodoc_member_order = 'bysource'

autosummary_generate = True
autosummary_imported_members = False

nitpicky = True

smartquotes = True
smartquotes_action = 'qDe'

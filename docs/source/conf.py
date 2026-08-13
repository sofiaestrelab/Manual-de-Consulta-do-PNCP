import os
import sys

# -- Permite destacar as linhas das tabelas via .CSS
from docutils import nodes
from docutils.parsers.rst import roles

def destaque_amarelo_claro_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(text, text, classes=['destaque-amarelo-claro'])
    return [node], []

roles.register_local_role('destaque-amarelo-claro', destaque_amarelo_claro_role)

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath('.'))

# Informações projeto
project = 'Manual de Consulta do PNCP'
copyright = '2026, Ministério da Gestão e Inovação em Serviços Públicos - MGI'
author = 'COPNCP/CGGES/DELOG/SEGES/MGI'

release = '2.0'
version = '2.0'

# Extensões
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

language = 'pt_BR'

# -- Permite destacar as linhas "kbd" das tabelas via .CSS
html_static_path = ['_static']
html_css_files = ['custom.css',]

# Caminhos
templates_path = ['_templates']
html_static_path = ['_static']

# HTML output
html_theme = 'sphinx_rtd_theme'

# Não incluir arquivos de build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Arquivo principal
master_doc = 'index'

# Source file patterns
source_suffix = '.rst'

# html_logo = "_static/img/logo-pncp-transparente-branco.png"

# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
# }

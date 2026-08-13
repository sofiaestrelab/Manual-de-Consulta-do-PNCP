# conf.py
import os
import sys
from . import __version__, __author__, __copyright__ 

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath('.'))
from . import __version__, __author__, __copyright__

# -- Project information
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
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',  
    'sphinx_rtd_theme',
]

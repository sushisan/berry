project = 'The Berry Script Language'
copyright = '2022, Guan Wenliang & Stephan Hadinger'
author = 'Guan Wenliang & Stephan Hadinger'
release = '1.1.0'

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.mathjax',
        'sphinx.ext.viewcode',
        'sphinx.ext.imgmath', 
        'sphinx.ext.todo',
        'breathe'
]
templates_path = ['_templates']
exclude_patterns = ['conf.py', 'Doxyfile']

import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

import subprocess
subprocess.call('doxygen', shell=True)


import sphinx_typo3_theme

html_theme = 'sphinx_typo3_theme'
html_logo = '../berry-logo.png'
html_theme_options = {
'logo_title' : 'The Berry Script Language',
'logo_alt' : 'Berry',
'logo_url' : 'https://github.com/berry-lang/berry'

source_suffix = {
    '.rst': 'restructuredtext',
}
# Breathe Configuration
breathe_projects = {"berry" : "../src"}
breathe_default_project = "berry"
breathe_projects_source = {
    "berry" : (
        "../", ["src/berry.h"]
    )
}

# exclude prefix
c_id_attributes = ["BERRY_API"]
c_paren_attributes = ["BERRY_API"]

cpp_id_attributes = ["BERRY_API"]
cpp_paren_attributes = ["BERRY_API"]

# add Berry lexer for highlighting
import sys
def setup(sphinx):
    sys.path.insert(0, os.path.abspath('../tools/highlighters/Pygments'))
    from berry import BerryLexer
    sphinx.add_lexer("berry", BerryLexer)

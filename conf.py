# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ROS RVIZ GAZEBO PYTHON'
copyright = '2023, Ammar Iqbal'
author = 'Ammar Iqbal'
release = '1.0'

import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('.'))
subprocess.call('doxygen Doxyfile.in', shell=True)
#-- Project information -----------------------------------------------------


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.doctest',
'sphinx.ext.intersphinx',
'sphinx.ext.todo',
'sphinx.ext.coverage',
'sphinx.ext.mathjax',
'sphinx.ext.ifconfig',
'sphinx.ext.viewcode',
'sphinx.ext.githubpages',
"sphinx.ext.napoleon",
'sphinx.ext.inheritance_diagram',
'breathe'
]


highlight_language = 'c++'
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# -- Options for intersphinx extension ---------------------------------------
# Example configuration for intersphinx: refer to the Python standard library. 
intersphinx_mapping = {'https://docs.python.org/': None}
# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing. 
todo_include_todos = True
# -- Options for breathe
breathe_projects = {
"ROS_RVIZ_GAZEBO_PYTHON": "_build/xml/"
}
breathe_default_project = "ROS_RVIZ_GAZEBO_PYTHON"
breathe_default_members = ('members', 'undoc-members')

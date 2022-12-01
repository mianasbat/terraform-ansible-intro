# Configuration file for the Sphinx documentation builder.
# 
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Terraform-Ansible-Intro'
copyright = '2022, Dr. Mian Asbat Ahmad'
author = 'Dr. Mian Asbat Ahmad'
release = '0.0.1'


# import myst_parser



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
#    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }

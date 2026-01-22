# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths if you later include custom Python modules
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Reinstall Quicken Desktop Guide'
copyright = '2025, Quicken'
author = 'Quicken Support Team'

# The full version, including alpha/beta/rc tags
release = '2025.1'

# -- General configuration ---------------------------------------------------

# Extensions (keep empty for simple documentation sites)
extensions = []

# Enable raw HTML usage in .rst files (for buttons, styling, etc.)
raw_enabled = True

# Templates path
templates_path = ['_templates']

# Files and folders to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (default theme works well for support guides)
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly page titles
html_title = "Reinstall Quicken 2022 or Quicken Classic Desktop – Download & Install Guide"
html_short_title = "Quicken Reinstall Guide"

# Optional favicon (place file in root or _static folder)
html_favicon = 'favicon.ico'

# Hide “View page source” link
html_show_sourcelink = False

# Allow raw HTML inside rst files (important for CTA buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static files (CSS, images, JS)
# html_static_path = ['_static']

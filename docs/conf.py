import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

project = "Dictionary Generator"
author = "The Casual Dev"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []
html_theme = "furo"
html_static_path = ["_static"]

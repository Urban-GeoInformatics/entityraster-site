"""Sphinx configuration for the entityraster documentation site."""

project = "entityraster"
author = "Kamyar Hasanzadeh"
copyright = "2026, Kamyar Hasanzadeh"
release = "0.1.0"

extensions = ["myst_parser", "sphinx_copybutton", "sphinx_design"]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
master_doc = "index"
exclude_patterns = ["_build", "**/._*", "._*", "requirements.txt"]

html_theme = "pydata_sphinx_theme"
html_title = f"entityraster {release}"
html_static_path = ["_static"]
html_theme_options = {
    "github_url": "https://github.com/Urban-GeoInformatics/entityraster",
    "navigation_with_keys": False,
}

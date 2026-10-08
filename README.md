# entityraster-site

Public site for [entityraster](https://github.com/Urban-GeoInformatics/entityraster).

- `index.html`: landing page (GitHub Pages).
- `docs-html/`: the built documentation (Sphinx: user guide, examples gallery, API reference, FAQ, glossary). Every example in it was executed when it was built.
- `.readthedocs.yaml`: Read the Docs publishes `docs-html/` as it is, so the build does not need the library repository.

To update the documentation: build it in the library repository (`uv run --extra docs sphinx-build -W -b html docs docs/_build/html`),
delete `docs-html/` here, copy the new build into it, and push.

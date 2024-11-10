# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = project
SOURCEDIR     = source
BUILDDIR      = html

# Put it first so that "make" without argument is like "make help".
help:
    @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: sphinx-apidoc
sphinx-apidoc:
    sphinx-apidoc -f -o source/modules -M "./source/modules"
    rm source/modules/modules.rst

.PHONY: html
html: sphinx-apidoc
    $(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)"
    @echo
    @echo "Build finished. The HTML pages are in $(BUILDDIR)."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
    @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

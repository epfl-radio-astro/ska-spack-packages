# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPoetryPluginExport(PythonPackage):
    """Poetry plugin to export the dependencies to various formats"""

    homepage = "https://python-poetry.org/"
    pypi = "poetry-plugin-export/poetry-plugin-export-1.0.7.tar.gz"

    version("1.0.7", sha256="f6ac707ae227b06b2481249ed2678ff6b810b3487cac0fbb66eb0dc2bfd6ecf1")
    version("1.1.2", sha256="5e92525dd63f38ce74a51ed68ea91d753523f21ce5f9ef8d3b793e2a4b2222ef")

    depends_on("python@3.7:3", type=("build", "run"))
    depends_on("py-poetry-core@1.1:1", type=("build", "run"))
    depends_on("py-poetry-core@1.3.2", when="@1.1.2", type=("build", "run"))

    # depends_on("py-poetry@1.2:1", type="run") # circular dependency

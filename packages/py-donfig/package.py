# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDonfig(PythonPackage):
    """
    Donfig is a python library meant to make configuration easier for other python packages.
    """

    homepage = "https://github.com/pytroll/donfig"
    pypi = "donfig/donfig-0.7.0.tar.gz"

    version("0.7.0", sha256="7e3993981b7312edb16098989e4cb084ff58c1b1d8e9878c7c0107eabf18dbfa")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

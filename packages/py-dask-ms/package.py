# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskMs(PythonPackage):
    """
    Constructs xarray Datasets from CASA Tables via python-casacore.
    """

    homepage = "https://github.com/ratt-ru/dask-ms"
    pypi = "dask-ms/dask-ms-0.2.15.tar.gz"

    version("0.2.15", sha256="d3b3052b886afdbe5f06017d0f7010a4593fe0b8c1711b7063523d083ee2d8d7")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-poetry@1.2.2", type=("build", "run"))
    depends_on("py-donfig@0.7.0:", type=("run"))
    depends_on("py-python-casacore", type=("run"))
    depends_on("py-fsspec@2023.1.0", type=("run"))



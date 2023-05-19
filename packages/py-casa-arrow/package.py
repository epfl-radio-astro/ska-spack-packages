# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCasaArrow(PythonPackage):
    """
    C++ and Python Arrow Bindings for casacore.
    """

    git = "https://github.com/ratt-ru/casa-arrow.git"

    version("master", branch="master")

    depends_on("py-cython@0.29.33:")
    depends_on("py-numpy@1.24.1:1")
    #pyarrow @ https://ratt-public-data.s3.af-south-1.amazonaws.com/wheels/pyarrow-12.0.0.dev13242%2Bgdbb4473-cp38-cp38-manylinux_2_28_x86_64.whl
    depends_on("py-pyarrow@12.0.0") #EO force to version 12, check local package!!
    depends_on("py-pytest@7.2.1:")
    #python-casacore>=3.5.2,<4.0.0
    depends_on("py-python-casacore@3.5.2:")
    depends_on("duckdb")
    depends_on("py-requests")
    depends_on("py-appdirs")
    depends_on("casacore")



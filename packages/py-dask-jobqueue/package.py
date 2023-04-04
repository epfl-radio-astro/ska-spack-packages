# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskJobqueue(PythonPackage):
    """
    Easy deployment of Dask Distributed on job queuing systems such as PBS, Slurm, or SGE.
    """

    homepage = "https://github.com/dask/dask-jobqueue"
    pypi = "dask-jobqueue/dask-jobqueue-0.8.1.tar.gz"

    version("0.8.1", sha256="16fd1b646a073ad3de75dde12a0dfe529b836f21a3bdbcee2a88bef24e9112a7")

    depends_on("py-setuptools", type="build")

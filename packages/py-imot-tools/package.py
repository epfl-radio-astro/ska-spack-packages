# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyImotTools(PythonPackage):
    """ImoT_tools packages together useful tools common to ImagingOfThings projects."""

    homepage = "https://github.com/imagingofthings/ImoT_tools"
    git = "https://github.com/imagingofthings/ImoT_tools.git"

    version("dev", branch="dev")

    depends_on('py-setuptools', type='build')
    depends_on('python@3.6:', type=('build', 'run'))

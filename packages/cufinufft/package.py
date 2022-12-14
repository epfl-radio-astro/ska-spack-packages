# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

#
# EO: Warning: we build from Simon Frasch's fork!
#

class Cufinufft(MakefilePackage):
    """cuFINUFFT is a very efficient GPU implementation of the 1-, 2-, and 3-dimensional nonuniform FFT of types 1 and 2, in single and double precision, based on the CPU code FINUFFT."""

    git = "https://github.com/AdhocMan/cufinufft.git"

    version('t3_d3', branch='t3_d3')

    depends_on("cuda")

    def edit(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        install_tree(".", prefix)

# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Finufft(MakefilePackage):
    """FINUFFT: Flatiron Institute Nonuniform Fast Fourier Transform library"""

    homepage = "https://github.com/flatironinstitute/finufft"
    git = "https://github.com/flatironinstitute/finufft.git"
    url = "https://github.com/flatironinstitute/finufft/archive/refs/tags/v2.1.0.tar.gz"

    version("2.1.0", sha256="52f25f0ace06a6dd514a29e728ad31e317b76631912bf0bc53cbf06355e24ad7")

    depends_on("fftw")

    def build(self, spec, prefix):
        make("clean")
        make("lib")

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def edit(self, spec, prefix):
        cpu_arch = spec.architecture
        config = [
            "export CFLAGS=\"-O3 -funroll-loops -march=${cpu_arch} -fcx-limited-range -fPIC\""
        ]

        with open('make.inc', 'w') as inc:
            for var in config:
                inc.write('{0}\n'.format(var))

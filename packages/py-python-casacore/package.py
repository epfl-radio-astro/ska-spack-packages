# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonCasacore(PythonPackage):
    """
    ADD DESCRIPTION
    """

    homepage = "https://github.com/casacore/python-casacore"
    pypi = "python-casacore/python-casacore-3.5.2.tar.gz"

    version("3.5.2", sha256="ad70c8e08893eec928b3e38c099bda8863f5aa9d099fd00694ad2b0d48eba08f")

    depends_on("python@3.7:",   type=("build", "run"))
    depends_on("casacore",      type=("build", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("boost +python", type=("build", "run"))
    depends_on("wcslib",        type=("build", "run"))
    depends_on("cfitsio",       type=("build", "run"))


    def patch(self):
        filter_file("boost_python-py", "boost_python", "setup.py")

    def setup_build_environment(self, env):
        L_boost    = self.spec["boost"].libs.directories[0]
        L_casacore = self.spec["casacore"].prefix.lib
        I_wcslib   = self.spec["wcslib"].prefix.include
        I_cfitsio  = self.spec["cfitsio"].prefix.include
        env.prepend_path("LD_LIBRARY_PATH", L_boost)
        env.prepend_path("LD_LIBRARY_PATH", L_casacore)
        env.append_flags("CXXFLAGS", f"-I{I_wcslib}")
        env.append_flags("CXXFLAGS", f"-I{I_cfitsio}")

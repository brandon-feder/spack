# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTinycss2(PythonPackage):
    """tinycss2 is a low-level CSS parser and generator written in Python: it can parse
    strings, return objects representing tokens and blocks, and generate CSS strings
    corresponding to these objects."""

    homepage = "https://www.courtbouillon.org/tinycss2"
    pypi     = "tinycss2/tinycss2-1.1.1.tar.gz"

    version('1.1.1', sha256='b2e44dd8883c360c35dd0d1b5aad0b610e5156c2cb3b33434634e539ead9d8bf')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-flit-core@3.2:3', type='build')
    depends_on('py-webencodings@0.4:', type=('build', 'run'))

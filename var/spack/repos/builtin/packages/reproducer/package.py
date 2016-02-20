# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install xerces-c
#
# You can always get back here to change things with:
#
#     spack edit xerces-c
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Reproducer(Package):
    """

    """

    #depends_on("netlib-blas+fpic")
    #depends_on("netlib-lapack+shared")
    depends_on("py-scipy")
    depends_on("py-numpy")


    homepage = "https://xerces.apache.org/xerces-c"
    url      = "https://www.apache.org/dist/xerces/c/3/sources/xerces-c-3.1.2.tar.gz"
    version('3.1.2', '9eb1048939e88d6a7232c67569b23985')
    version('3.1.3', '70320ab0e3269e47d978a6ca0c0e1e2d')
      
    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix,
                  "--disable-network")
        make("clean")
        make()
        make("install")


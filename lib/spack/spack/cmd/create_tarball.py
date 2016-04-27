##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import argparse
import os
import sys
import llnl.util.tty as tty

import spack
import spack.cmd
from spack.util.executable import which
from spack.binary_distribution import tarball_name

description = "Create tarballs for given packages"

def setup_parser(subparser):
    subparser.add_argument(
        'packages', nargs=argparse.REMAINDER, help="specs of packages to package")


def create_tarball(parser, args):
    if not args.packages:
        tty.die("tarball creation requires at least one package argument")

    specs = spack.cmd.parse_specs(args.packages)
    for spec in specs:
        # ----------- Make sure the spec only resolves to ONE thing
        q = spack.installed_db.query(spec)
        if len(q) == 0:
            tty.die("No installed packages match spec %s" % spec)

        if len(q) > 1:
            tty.error("Multiple matches for spec %s.  Choose one:" % spec)
            for s in q:
                sys.stderr.write(s.format())
                sys.stderr.write("\n")

            sys.exit(1)
        package = q[0]
#        package = spack.repo.get(spec)
        tar = which('tar', required=True)
        tarfile = tarball_name(package)
        dirname = os.path.dirname(package.prefix)
        basename = os.path.basename(package.prefix)
        tar("--directory=%s" %dirname, "-cvzf", tarfile, basename)


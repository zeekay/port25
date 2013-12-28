#!/usr/bin/env python

# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
from distutils.core import setup

__docformat__ = 'restructuredtext'

import os
import sys
from os import path

from port25 import __author__, __license__, __version__

setup(name='port25',
      version=__version__,
      author=__author__,
      author_email='zk@monoid.io',
      url='http://github.com/zeekay/port25',
      description="The python API for Port25's PowerMTA.",
      long_description="The python API for Port25's PowerMTA.  It wraps around the C API, but makes it more pythonic.",
      platforms = ['any'],
      license = __license__,
      packages=['port25'],
      classifiers = [
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python'
      ],
      test_suite = 'nose.collector',
      )

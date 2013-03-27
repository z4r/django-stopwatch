from setuptools import setup, find_packages
import sys
import os
import multiprocessing, logging  # http://www.eby-sarna.com/pipermail/peak/2010-May/003348.html
__author__ = "Andrea de Marco <andrea.demarco@buongiorno.com>"
__version__ = '0.1'
__classifiers__ = [
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]
__copyright__ = "2013, %s " % __author__
__license__ = """
   Copyright (C) %s

      This program is free software: you can redistribute it and/or modify
      it under the terms of the GNU General Public License as published by
      the Free Software Foundation, either version 3 of the License, or
      (at your option) any later version.

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
""" % __copyright__

__docformat__ = 'restructuredtext en'

__doc__ = """
:abstract: STOPWATCH: Statistics for API
:version: %s
:author: %s
:copyright: %s
""" % (__version__, __author__, __license__)


wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'django-stopwatch'

author, email = __author__.rsplit(' ', 1)
email = email.strip('<>')

version = __version__
classifiers = __classifiers__

readme = open(os.path.join(wd, 'README.rst'), 'r').readlines()
description = readme[1]
long_description = ''.join(readme)

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
    test_reqs = open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')).read()
except (IOError, OSError):
    test_reqs = reqs = ''

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    url='https://github.com/z4r/django-stopwatch',
    maintainer=author,
    maintainer_email=email,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=reqs,
    tests_require=test_reqs,
    test_suite='testrunner.run_tests',
    license='Apache License 2.0',
)

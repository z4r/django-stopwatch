from setuptools import setup, find_packages
import os
import multiprocessing, logging  # http://www.eby-sarna.com/pipermail/peak/2010-May/003348.html

localdir = os.path.dirname(os.path.abspath(__file__))
name = 'django-stopwatch'
pkg = __import__('stopwatch')

author, email = pkg.__author__.rsplit(' ', 1)
email = email.strip('<>')

version = pkg.__version__
classifiers = pkg.__classifiers__

readme = open(os.path.join(localdir, 'README.rst'), 'r').readlines()
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

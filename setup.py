#!/usr/bin/python
# -*- encoding: utf-8; -*-
# flake8: noqa

from setuptools import setup, find_packages
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

long_description = """
# Shortening Words

Transform word of multiple words into a short version giving a desire length.

The mininum size is number of words plus the end periods.

Example:
"Security Agreement Required" and length 1 will produce
"S. A. R." with length 8
"""

setup(
    name='shortening-words',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Shortening Words',
    long_description=long_description,

    url='https://github.com/Tomohare/shortening_words',
    author='Fabricio Santolin da Silva',
    author_email='fabricio.santolin-da-silva@al-enterprise.com',
    maintainer='Fabricio Santolin da Silva',
    maintainer_email='fabricio.santolin-da-silva@al-enterprise.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.9',
    ],

    keywords='shortening',
    packages=['shortening_words'],
    install_requires=['pyphen'],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for hydroparser
"""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('hydroparser/hydroparser.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "hydroparser",
    packages = ["hydroparser"],
    install_requires = ['openpyxl','win-unicode-console'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
    ],
    keywords='hydrology parsing tables',
    entry_points = {
        "console_scripts": ['hydroparser = hydroparser.hydroparser:main']
        },
    version = version,
    description = "Python command line application with GUI filedialog element for parsing some hydrology data to xlsx file",
    long_description = long_descr,
    author = "Oleksandr Zabolotniy",
    author_email = "pirogovich13@gmail.com",
    url = "https://github.com/sashkozab/hydroparser",
    license='MIT',
    )

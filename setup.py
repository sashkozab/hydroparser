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
    entry_points = {
        "console_scripts": ['hydroparser = hydroparser.hydroparser:main']
        },
    version = version,
    description = "Python command line application with GUI filedialog element for parsing some hydrology data to xlsx file",
    long_description = long_descr,
    author = "Oleksandr Zabolotniy",
    author_email = "pirogovich13@gmail.com",
    url = "https://github.com/sashkozab/hydroparser",
    )

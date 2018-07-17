#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

import usr

setup(
    name='usr',
    version=usr.__version__,
    packages=find_packages()
)

# pylint: skip-file

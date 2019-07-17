from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="testpkg",
    version="0.1a",
    description="test package for conda build",
    long_description="",
    long_description_content_type="text/markdown",
    author="Maksim Novikov",
    author_email="mnovikov.work@gmail.com",
    packages=find_packages(),
    install_requires=[],
)

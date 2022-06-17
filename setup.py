"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='formFactors',
    version='0.1.0',
    packages=['formFactors'],
    url='https://github.com/EmCeBeh/formFactors',  # Optional
    install_requires=['numpy', 'scipy', 'uncertainties'],  # Optional
    license='',
    author='Martin Borchert',
    author_email='martin.b@robothek.de',
    description='Collection formfactors from various sources. Only for internal use! No right to distrubute!',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
)
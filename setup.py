#!/usr/bin/env python
# For some reason, building exes with py2exe doesnt work right now.
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

scripts = ['fap']

setup(name='Fapcode',
      version='0.1',
      long_description='Simple Ook fork accepting Fap',
      author='David Francos Cuartero (XayOn)',
      console = [{"script": "fap" }],
      author_email='xayon@davidfrancos.net',
      url='http://github.com/Degeneratedlabs/fapcode',
      mantainer='David Francos Cuartero (XayOn)',
      mantainer_email='xayon@xayon.net',
      description="FapCode Ook fork interpreter",
      scripts=scripts,
)

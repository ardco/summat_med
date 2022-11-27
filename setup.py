# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in summat_med/__init__.py
from summat_med import __version__ as version

setup(
	name='summat_med',
	version=version,
	description='customized for sammat stock reports',
	author='hadeel.milad@ard.ly',
	author_email='hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

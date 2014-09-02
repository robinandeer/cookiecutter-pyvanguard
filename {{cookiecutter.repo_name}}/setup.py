#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Based on https://github.com/pypa/sampleproject/blob/master/setup.py."""
from __future__ import unicode_literals
# To use a consistent encoding
from codecs import open
import os
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

# Shortcut for building/publishing to Pypi
if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist bdist_wheel upload')
  sys.exit()


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):

  """Set up the py.test test runner."""

  def finalize_options(self):
    """Set options for the command line."""
    TestCommand.finalize_options(self)
    self.test_args = []
    self.test_suite = True

  def run_tests(self):
    """Execute the test runner command."""
    # Import here, because outside the required eggs aren't loaded yet
    import pytest
    sys.exit(pytest.main(self.test_args))

# Get the long description from the relevant file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


setup(
  name='{{ cookiecutter.repo_name }}',

  # Versions should comply with PEP440. For a discussion on
  # single-sourcing the version across setup.py and the project code,
  # see http://packaging.python.org/en/latest/tutorial.html#version
  version='{{ cookiecutter.version }}',

  description='{{ cookiecutter.description }}',
  long_description=long_description,
  # What does your project relate to? Separate with spaces.
  keywords='{{ cookiecutter.repo_name }} development',
  author='{{ cookiecutter.full_name }}',
  author_email='{{ cookiecutter.email }}',
  license='MIT',

  # The project's main homepage
  url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',

  packages=find_packages(exclude=('tests*', 'docs', 'examples')),

  # If there are data files included in your packages that need to be
  # installed, specify them here.
  include_package_data=True,
  zip_safe=False,
  package_data={
    '': ['README.md', 'LICENSE', 'AUTHORS'],
  },

  # Although 'package_data' is the preferred approach, in some case you
  # may need to place data files outside of your packages.
  # In this case, 'data_file' will be installed into:
  # '<sys.prefix>/my_data'
  # data_files=[('my_data', ['data/data_file'])],

  install_requires=[
    'setuptools',
  ],
  tests_require=[
    'pytest',
  ],
  cmdclass=dict(
    test=PyTest,
  ),

  # To provide executable scripts, use entry points in preference to the
  # "scripts" keyword. Entry points provide cross-platform support and
  # allow pip to create the appropriate form of executable for the
  # target platform.
  entry_points=dict(
    console_scripts=[
      '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name|replace('-', '_') }}.__main__:cli',
    ],
  ),

  # See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    # How mature is this project? Common values are:
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',

    'Environment :: Console',
  ],
)

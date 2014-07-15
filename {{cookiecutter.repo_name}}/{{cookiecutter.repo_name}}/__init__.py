# -*- coding: utf-8 -*-
"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by {{ cookiecutter.full_name }}
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""
# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t={{ cookiecutter.project_name }}
from __future__ import absolute_import, unicode_literals
import pkgutil

__all__ = [
  '__title__', '__summary__', '__uri__', '__version__', '__author__',
  '__email__', '__license__', '__copyright__'
]

__title__ = '{{ cookiecutter.repo_name }}'
__summary__ = 'Command line utility written in Python'
__uri__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'

__version__ = pkgutil.get_data(__package__, 'VERSION').decode('utf-8').strip()

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

__license__ = 'MIT'
__copyright__ = 'Copyright 2014 {{ cookiecutter.full_name }}'

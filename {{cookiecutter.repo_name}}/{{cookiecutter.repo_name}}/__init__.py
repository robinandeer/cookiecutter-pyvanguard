# -*- coding: utf-8 -*-
"""
{{ cookiecutter.repo_name }}
~~~~~~~~~~~~~

{{ cookiecutter.description }}

:copyright: (c) {{ cookiecutter.year }} by {{ cookiecutter.full_name }}
:licence: MIT, see LICENCE for more details
"""
from __future__ import absolute_import, unicode_literals

__all__ = [
  '__title__', '__summary__', '__uri__', '__version__', '__author__',
  '__email__', '__license__', '__copyright__'
]

# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t={{ cookiecutter.project_name }}
__banner__ = r"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by {{ cookiecutter.full_name }}
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""

__title__ = '{{ cookiecutter.repo_name }}'
__summary__ = '{{ cookiecutter.description }}'
__uri__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'

__version__ = '{{ cookiecutter.version }}'

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

__license__ = 'MIT'
__copyright__ = 'Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}'

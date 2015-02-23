# -*- coding: utf-8 -*-
"""
test_{{ cookiecutter.repo_name|replace('-', '_') }}
----------------------------------

Tests for `{{ cookiecutter.repo_name|replace('-', '_') }}` module.
"""
import pytest
import {{ cookiecutter.repo_name|replace('-', '_') }}


class Test{{ cookiecutter.repo_name|capitalize }}(object):
    @classmethod
    def set_up(self):
        pass

    def test_something(self):
        pass

    @classmethod
    def tear_down(self):
        pass

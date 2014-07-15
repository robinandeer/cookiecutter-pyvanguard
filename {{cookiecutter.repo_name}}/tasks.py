#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from invoke import run, task


@task
def test():
  run('python setup.py test', pty=True)


@task
def clean():
  """clean - remove build artifacts"""
  run('rm -r build/')
  run('rm -rf dist/')
  run('rm -rf {{ cookiecutter.repo_name }}.egg-info')
  run('find . -name __pycache__ -delete')
  run("find . -name '*.pyc' -delete")
  run("find . -name '*.pyo' -delete")
  run("find . -name '*~' -delete")
  print('Cleaned up.')


@task
def lint():
  """lint - check style with flake8"""
  run('flake8 {{ cookiecutter.repo_name }} tests')


@task
def test():
  """test - run tests quickly with the default Python"""
  run('python setup.py test')


@task(name='test-all')
def testall():
  """test-all - run tests on every Python version with tox"""
  run('tox')


@task
def coverage():
  """coverage - check code coverage quickly with the default Python"""
  run('coverage run --source {{ cookiecutter.repo_name }} setup.py test')
  run('coverage report -m')
  run('coverage html')
  run('open htmlcov/index.html')


@task(clean)
def publish(test=False):
  """publish - package and upload a release to the cheeseshop"""
  run('python setup.py register sdist upload')
  run('python setup.py register bdist_wheel upload')

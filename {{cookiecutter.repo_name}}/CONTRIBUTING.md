# Contributing
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs
Report bugs at [{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues][issues].

If you are reporting a bug, please include:

* Your operating system name and version
* Any details about your local setup that might be helpful in troubleshooting
* Detailed steps to reproduce the bug

### Fix Bugs
Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it. A good idea is also to review the comment thread to see if it already referenced in any open rull requests.

### Implement Features
Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

### Write Documentation
{{ cookiecutter.project_name }} could always use more documentation, whether as part of the official {{ cookiecutter.project_name }} docs, in inline docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback
The best way to send feedback is to file an issue at [{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues][issues].

If you are proposing a feature:

* Explain in detail how it would work
* Keep the scope as narrow as possible, to make it easier to implement (atomic)
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started!
Ready to contribute? Here's how to set up `{{ cookiecutter.project_name }}` for local development.

1. Fork the [{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}][repo] repo on GitHub

2. Clone your fork locally:

  ```bash
  $ git clone git@github.com:<your github username>/{{ cookiecutter.repo_name }}.git
  ```

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

  ```bash
  $ mkvirtualenv {{ cookiecutter.repo_name }}
  $ cd {{ cookiecutter.repo_name }}/
  $ pip install --editable .
  ```

4. Create a branch for local development:

  ```bash
  $ git checkout -b name-of-your-bugfix-or-feature
  ```

  Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox:

  ```bash
  $ flake8 {{ cookiecutter.repo_name }} tests
  $ python setup.py test
  $ tox
  ```

  To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub:

  ```bash
  $ git add .
  $ git commit -m "Detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
  ```

7. Submit a pull request through the GitHub website. It's absolutely OK to open the pull request early and update with additional commits over time.


## Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.md.

3. The pull request should work for Python 2.7, 3.4, and PyPy. Check the [Travis page][travis] and make sure that the tests pass for all supported Python versions.

## Tips
To run a subset of tests:

```bash
$ py.test tests.test_{{ cookiecutter.repo_name }}
```


[issues]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
[repo]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
[travis]: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pull_requests

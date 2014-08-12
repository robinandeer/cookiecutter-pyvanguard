# Contributing
All contributions are much welcome and greatly appreciated! Expect to be credited for you effort.

This document is adapted from the cookiecutter [CONTRIBUTING.rst][cookie-contrib].


## General
Generally try to limit the scope of any Pull Request to an atomic update if possible. This way, it's much easier to assess and review your changes.

You should expect a considerably faster turn around if you submit two or more PRs instead of baking them all into one major PR.


## Issue tracker
{{ cookiecutter.repo_name }} uses the excellent [GitHub issue tracker][issues].

Personally, I also recommend giving [ZenHub][zenhub] a try. After installing the Google Chrome plugin, visit the [{{ cookiecutter.repo_name }} boards][repo-boards]. This way, it's very easy to get an overview of the current bug/feature request situation.


## Types of Contributions
There are many ways you can help out and improve this repository.

### Report Bugs
Report bugs at [{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues][issues].

Consider including the following data in your bug report:

- Your operating system name and version
- Any details about your local setup that might be helpful in troubleshooting
- If you can, provide detailed steps to reproduce the bug
- If you don't have steps to reproduce the bug, just note your observations in as much detail as you can. Questions to start a discussion about the issue are welcome.

### Fix Bugs
Look through the [GitHub issues][issues] for bugs. Anything tagged with "bug" is open to whoever wants to implement it. A good idea is also to review the comment thread to see if the issue is already referenced in any open pull requests.

### Implement Features
Look through the [GitHub issues][issues] for features. Anything tagged with "feature" is open to whoever wants to implement it.

### Write Documentation
{{ cookiecutter.project_name }} could always use more documentation, whether as part of the official {{ cookiecutter.project_name }} docs, in inline docstrings, or even on the web in blog posts, articles, and such.

If you have written your own tutorial or review of the software, please consider adding a refferal link to the repository.

### Submit Feedback
The best way to send feedback is to [open a new issue][issues].

If you are requesting a feature:

- Explain in detail how it would work
- Keep the scope as narrow as possible, to make it easier to implement (atomic)


## Get Started!
Ready to contribute? Here's how to set up `{{ cookiecutter.project_name }}` for local development.

> Over time my ambition is to provide a reproducable and automated setup through Vagrant.

1. Fork the [{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}][repo] repo on GitHub

2. Clone your fork locally:

  ```bash
  $ git clone git@github.com:<your github username>/{{ cookiecutter.repo_name }}.git
  ```

  I would personally recommend [GitHub for Mac][gh-mac] to easily manage pull requests and [SourceTree][sourcetree] as an excellent GUI for git.

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

5. Make you changes locally

6. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox:

  ```bash
  $ flake8 {{ cookiecutter.repo_name }} tests
  $ invoke test
  $ tox
  ```

  To get flake8 and tox, just pip install them into your virtualenv.

7. Commit your changes and push your branch to GitHub:

  ```bash
  $ git add .
  $ git commit -m "Detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
  ```

8. Check that the test coverage hasn't dropped:

	```bash
	$ invoke coverage
	```

9. Submit a pull request through the GitHub website. I would encourage you to submit your pull request early in the process. This makes it easier to maintain an overview of current development and opens up for continous discussion.


## Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.md.

3. The pull request should work for Python 2.7, 3.4, and PyPy. Check the [Travis page][travis] and make sure that the tests pass for all supported Python versions.


## Coding conventions
Generally I recommend two ways to stay up-to-date on {{ cookiecutter.repo_name }} coding standards.

1. Read and pay attention to current code in the repository

2. Install a plugin for [EditorConfig][editorconfig] and let it handle some of the detailed settings for you.


## Tips
To run a particular test:

```bash
$ python -m pytest tests.test_find.TestFind.test_find_template
```

To run a subset of tests:

```bash
$ python -m pytest tests.test_find
```


[cookie-contrib]: https://github.com/audreyr/cookiecutter/blob/master/CONTRIBUTING.rst
[editorconfig]: http://editorconfig.org/
[gh-mac]: https://mac.github.com/
[issues]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
[repo]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
[repo-boards]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues#boards
[sourcetree]: http://www.sourcetreeapp.com/
[travis]: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pull_requests
[zenhub]: https://www.zenhub.io/

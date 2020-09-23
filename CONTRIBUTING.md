# Development & Contribution guide

Below are all the details you need to get started helping with the SDU project.


## Table of contents
- [Submitting issues](#submitting-issues)
- [Submitting Pull requests](#submitting-pull-requests)
- [Roadmap](#roadmap)
- [Setting up your development environment](#setting-up-your-development-environment)
  - [Prerequisites](#prerequisites)
  - [Installing development dependencies](#installing-development-dependencies)
- [Folder & File Structure](#folder--file-structure)

## Submitting issues

There is a template setup for bug reports, feature requests and questions on github, simply go:

- [Here for bug reports](https://github.com/Descent098/sdu/issues/new?labels=bug&template=bug_report.md&title=%5BBUG%5D)
- [Here for feature requests](https://github.com/Descent098/sdu/issues/new?labels=enhancement&template=feature_request.md&title=%5BFeature%5D)
- [Here for questions](https://github.com/Descent098/sdu/issues/new?labels=documentation&template=question.md&title=%5Bquestion%5D)

## Submitting Pull requests

When you try to submit a pull request there will be an automated template generated that you need to fill out. 

On top of that here are the required standards:

- [ ] Commenting is present in all Classes, modules, and functions. Use [numpydocs style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)
- [ ] Any new functionality has associated tests
- [ ] Functionality has been validated on Linux/Mac and windows (pytest greenlight from github actions on the PR is good enough)
- [ ] Validated this change does not break backwards compatibility without good reason

## Roadmap

For current roadmap, and development planning details see [our roadmap](https://github.com/Descent098/sdu/projects). This is how releases are planned and will give you an overview of what is being worked on for the current/future releases.

## Setting up your development environment

### Prerequisites

You will need the following to work on sdu:

- Python 3.6+ (Earlier versions do not have f-strings)
- Pip for python 3
- Windows or *nix (Linux or Mac OS) operating system

### Installing development dependencies

There are a few dependencies you will need to use this package fully, they are specified in the extras require parameter in setup.py but you can install them manually:

```
nox   	# Used to run automated processes
pytest 	# Used to run the test code in the tests directory
pdoc3	# Generates API documentation
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, testing, and build + distribution (through PyPi) automation.



## Folder & File Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*

### /sdu

*Contains all the first party modules used in sdu*

### /tests

*Contains tests to be run before release* 

### Files in root directory

**setup.py**: Contains all the configuration for installing the package via pip.

**LICENSE**: This file contains the licensing information about the project.

**CHANGELOG.md**: Used to create a changelog of features you add, bugs you fix etc. as you release.

**CONTRIBUTING.md**: This file, contains details about development processes

**.deepsource.toml**: [Deepsource](https://deepsource.io/gh/Descent098/sdu/) is used for code quality and security validation

**noxfile.py**: Used to configure various automated processes using [nox](https://nox.readthedocs.io/en/stable/), these include;

- Building release distributions
- Releasing distributions on PyPi
- Running test suite agains a number of python versions (3.5-current)

If anything to do with deployment or releases is failing, this is likely the suspect.

There are 4 main sessions built into the noxfile and they can be run using ```nox -s <session name>``` i.e. ```nox -s test```:

- build: Creates a source distribution, builds the markdown docs to html, and creates a universal wheel distribution for PyPi.
- release: First runs the build session, then asks you to confirm all the pre-release steps have been completed, then runs *twine* to upload to PyPi
- test: Runs the tests specified in /tests using pytest, and runs it on python versions 3.5-3.8 (assuming they are installed)
- docs: Serves the docs on a local http server so you can validate they have the content you want without having to fully build them.

**.gitignore**: A preconfigured gitignore file (info on .gitignore files can be found here: https://www.atlassian.com/git/tutorials/saving-changes/gitignore)


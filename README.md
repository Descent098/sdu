# Script Development Utilities

A set of utilities to make developing scripts simpler and easier

## Table of contents
- [Goals](#goals)
- [Installation](#installation)
    - [From PyPi](#from-pypi)
    - [From source](#from-source)
- [Usage & Documentation](#usage--documentation)
- [Modules](#modules)
  - [autocomplete](#autocomplete)
  - [cli](#cli)
  - [paths](#paths)
  - [type_conversions](#type_conversions)
  - [validation](#validation)
- [Development-Contribution guide](#development-contribution-guide)
- [Installing development dependencies](#installing-development-dependencies)
- [Folder & File Structure](#folder--file-structure)

## Goals

There are several goals with this project:

1. Provide a useful API for well developed functions with error catching and testing for commonly annoying situations

2. Provide cross-platform implementations of functions (where possible)

3. Give people access to source code to learn how the functions work and just pull what's needed

4. Serve as a repository of general knowledge to share solutions to issues with people

## Installation

### From PyPi

1. Run ```pip install sdu``` or ```sudo pip3 install sdu```

### From source

1. Clone this repo: (put github/source code link here)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory



## Usage & Documentation

See API documentation ([https://kieranwood.ca/sdu](https://kieranwood.ca/sdu)).

## Modules

### autocomplete

This module is used to generate autocomplete files for bash


### cli

A module for helpful utilities with generating CLI's such as:


- Clearing the terminal

### paths
This module contains many useful utilities for dealing with system paths such as:
- A pre and post processing pipeline for system paths
- Ability to add paths to the PATH variable

### type_conversions

Quick and common conversions between types with sensible options such as:

- Converting a dictionary (and second dimension dictionary keys) to defaultdict(s)

### validation

Contains a set of common validation schemes such as:

- Validating number input is between a set value at the command line

- Validate provided string is an accepted value

## Development-Contribution guide

### Installing development dependencies

There are a few dependencies you will need to use this package fully, they are specified in the extras require parameter in setup.py but you can install them manually:

```
nox   	# Used to run automated processes
pytest 	# Used to run the test code in the tests directory
pdoc3	# Generates API documentation
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, testing, and build + distribution (through PyPi) automation.



### Folder & File Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*

#### /sdu

*Contains all the first party modules used in sdu*

#### /tests

*Contains tests to be run before release* 

**setup.py**: Contains all the configuration for installing the package via pip.

**LICENSE**: This file contains the licensing information about the project.

**CHANGELOG.md**: Used to create a changelog of features you add, bugs you fix etc. as you release.

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



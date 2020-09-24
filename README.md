![sdu logo](https://raw.githubusercontent.com/Descent098/sdu/master/sdu.png)

[![DeepSource](https://deepsource.io/gh/Descent098/sdu.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Descent098/sdu/?ref=repository-badge)

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
- [Contributing](#contributing)

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

For usage please see the  API documentation ([https://kieranwood.ca/sdu](https://kieranwood.ca/sdu)).

For details on how contributing to the project, please see [CONTRIBUTING.md](https://github.com/Descent098/sdu/blob/master/CONTRIBUTING.md), for details on upcoming changes see [our roadmap](https://github.com/Descent098/sdu/projects).

For most recent changes see [CHANGELOG.md](https://github.com/Descent098/sdu/blob/master/CHANGELOG.md).

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

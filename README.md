# Script Development Utilities

An API for accelerating script development and generalizing tedious tasks.



## Quick-start



### Installation

#### From PyPi

1. Run ```pip install sdu``` or ```sudo pip3 install sdu```



#### From source

1. Clone this repo: (put github/source code link here)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory



#### Usage

See API documentation ([https://kieranwood.ca/sdu](https://kieranwood.ca/sdu)).


## Development-Contribution guide



### Installing development dependencies

There are a few dependencies you will need to use this package fully, they are specified in the extras require parameter in setup.py but you can install them manually:

```
nox   	# Used to run automated processes
pytest 	# Used to run the test code in the tests directory
pdoc3	# Generates API documentation
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, testing, and build + distribution (through PyPi) automation.



### Folder Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*



#### /sdu

*Contains all the first party modules used in sdu*



#### /tests

*Contains tests to be run before release* 



#### Root Directory

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



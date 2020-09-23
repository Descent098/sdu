"""A set of utilities to make developing scripts simpler and easier

There are several goals with this project:

1. Provide a useful API for well developed functions with error catching and testing for commonly annoying situations
2. Provide cross-platform implementations of functions (where possible)
3. Give people access to source code to learn how the functions work and just pull what's needed
4. Serve as a repository of general knowledge to share solutions to issues with people

Installation
-----------
**From PyPi:**

Run 
```pip install sdu``` 

or 

```sudo pip3 install sdu```

**From source:**

1. Clone the repo:

    ```git clone https://github.com/Descent098/sdu```

2. CD into the **/sdu** directory and run:

    ```pip install .``` or ```sudo pip3 install .```

Modules
-------
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

"""
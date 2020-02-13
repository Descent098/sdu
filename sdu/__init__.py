r"""A set of utilities to make developing scripts simpler and easier

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
paths:
    This module contains many useful utilities for dealing with system paths.

terminal:
    A module for helpful utilities with generating CLI's

validation:
    Contains a set of common validation schemes.

type_conversions:
    This module is for quick and common conversions between types with sensible options

Examples
--------

**A random number guessing game using sdu validation.**

```
import random

from sdu.validation import validate_number_selection

number = random.randint(0,10)

selection = validate_number_selection(maximum = 10, minimum = 0, message="guess a number between 0-10: ")

while selection != number:
    if selection < number:
        print('Too Low')

    elif selection > number:
        print('Too High')

    selection = validate_number_selection(maximum = 10, minimum = 0, message="guess a number between 0-10: ")

print('You win!') # After number has been guessed correctly
```


**Clearing terminal after filling it with hello's**

```
from sdu.terminal import clear_terminal

print('hello\n'*250) # Fill screen with hello's

clear_terminal() # Clears the terminal NOTE: cross platform
```


**An example of path processing on a windows machine (because of the wildcard and OS results will vary)**

```
from sdu.paths import process_paths

paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']

print(process_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
```


**An example of the preprocessing to postprocessing pipeline on a windows machine (because of the wildcard and OS results will vary)**

```
from sdu.paths import preprocess_paths, postprocess_paths

paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']

print(preprocess_paths(paths)) # Prints: ['~/Desktop/Development/Canadian Coding/SSB', '~/Desktop/Development/*' , '~/Desktop/Development/Personal/noter', '.']

print(postprocess_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
```


**Print a shopping list with each item on a new line**
```
from sdu.type_conversions import stringify_list

shopping_list = ["eggs", "ham", "spam"]

print((stringify_list(shopping_list, seperator='\n', spacing=0))) # Prints list with each item on new line
```
"""
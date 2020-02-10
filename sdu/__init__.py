"""A set of utilities to make developing scripts simpler and easier

Installation
-----------
**From PyPi:**

    Run ```pip install sdu``` or ```sudo pip3 install sdu```

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

Examples
--------
A random number guessing game using sdu validation.

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

"""
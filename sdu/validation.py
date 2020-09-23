"""Contains a set of common validation schemes such as:

- Validating number input is between a set value at the command line
- Validate provided string is an accepted value

Functions
---------
validate_number_selection -> int or float:
    Used to validate user input is within range *minimum <= input <= maximum*

validate_choices -> str:
    Used to validate users input is one of the validators

confirm -> bool:
    Used to validate users input is yes or no

Examples
--------
### Validate a selection between option 1 or 2 and exclude floating points

```
from sdu.validation import validate_number_selection

# Validates selection made between 1-2 and is not a floating point value
selection = validate_number_selection(maximum = 2, minimum = 1, message="Select option 1 or 2: ", no_float = True)

if selection == 1:
    print('selection 1 made')

elif selection == 2:
    print('selection 2 made')
```

### Asking user which condiment they want

```
from sdu.validation import validate_choices

# Stays in loop until user enters one of the valid_choices
condiment = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo']) # Prints: What condiment do you want?(ketchup or mayo)
```

### Ask someone to confirm if they want fries with that

```
from sdu.validation import confirm

with_fries = confirm('Do you want fries with that?')

if with_fries:
    print('Here are your fries')
else:
    print('No fry for you')
```

"""

from typing import Union

import colored

def validate_number_selection(maximum = 1, minimum=0, message = "Please select one of the above options: ", no_float = False) -> Union[int, float]:
    """
    Used to validate user input is within range minimum < input < maximum. Keeps user in loop
    until input is within range.

    Parameters
    ----------
    maximum:  (int|float)
        The maximum value allowed

    minimum: (int|float)
        The minimum value allowed

    message: (str)
        What to prompt user with when function is called

    no_float: bool
        If true then floating point values are not allowed

    Returns
    -------
    int or float:
        The validated result from the user

    Examples
    --------
    Validate a selection between option 1 or 2 and exclude floating points

    ```
    from sdu.validation import validate_number_selection

    # Validates selection made between 1-2 and is not a floating point value
    selection = validate_number_selection(maximum = 2, minimum = 1, message="Select option 1 or 2: ", no_float = True)

    if selection == 1:
        print('selection 1 made')

    elif selection == 2:
        print('selection 2 made')
    ```
    """

    valid_answer = False

    while not valid_answer:
        try: # Catches if answer is not int or float
            selection = input(message)
            if "." in selection:
                if no_float:
                    print("Decimal values are not permitted")
                else:
                    selection = float(selection)
            else:
                selection = int(selection)
        except ValueError:
            print("Invalid input please try again")

        if selection > maximum: # More than maximum
            print("Invalid input the selection made was larger than {}".format(maximum))

        elif selection < minimum:#Less than minimum
            print("Invalid input the selection made was smaller than {}".format(minimum))

        else: # If answer is valid and in range
            return selection


def validate_choices(message:str, valid_choices:list, display_choices:bool = True) -> str:
    """Used to validate users input is one of the validators.
    
    Parameters
    ----------
    message:  (str)
        The message to print along with the choices on user prompt.

    valid_choices: (list|tuple)
        The valid choices the user can pick from

    display_choices: (bool)
        If True then on user prompt the choices will be displayed

    Examples
    --------
    Asking user which condiment they want

    ```
    from sdu.validation import validate_choices

    # Stays in loop until user enters one of the valid_choices
    condiment = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo']) # Prints: What condiment do you want?(ketchup or mayo)
    ```

    Notes
    -----
    - User input and choices are both stripped of whitespace and converted to lowercase
    - If display_choicesis True then the a '?:' is appended to the end of the message

    Returns
    -------
    str:
        The valid choice the user selected
    """

    for count, choice in enumerate(valid_choices): # Preprocessing choices to lowercase and stripping whitespace
        valid_choices[count] = choice.lower().strip()
    
    stringified_choices = " or ".join(valid_choices)

    while 1:
        if display_choices:
            response = input(message + f"({stringified_choices})?: ")

        else:
            response = input(message)

        if response.lower().strip() in valid_choices:
            return response
        else:
            print(f"Selection provided was not one of the choices; {stringified_choices}")


def confirm(message:str) -> bool:
    """Used to validate users input is yes or no
    
    Parameters
    ----------
    message: (str)
        The message to display for confirmation

    Examples
    --------
    Ask someone if they want fries with that.

    ```
    from sdu.validation import confirm

    with_fries = confirm('Do you want fries with that?')

    if with_fries:
        print('Here are your fries')
    else:
        print('No fry for you')
    ```

    Returns
    -------
    bool:
        Returns True if response is yes and False if no."""

    validators = ["y", "yes"]
    invalidators = ["n", "no"]
    valid_input = False

    while not valid_input:
        response = input(message + "(y or n): ")
        if response.lower().strip() in validators:
            return True
        elif response.lower().strip() in invalidators:
            return False
        else:
            print(f"{colored.fg(1)}Please respond with either yes or no\n{colored.fg(15)}")

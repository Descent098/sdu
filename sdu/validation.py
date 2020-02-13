r"""A set of common validation schemes.

Functions
---------
validate_number_selection -> int|float:
    Used to validate user input is within range minimum < input < maximum. Keeps user in loop
    until input is within range.

Examples
--------
Random number guessing game

```
import random

from sdu.validation import validate_number_selection

number = random.randint(0,10)

selection = -1 # initialize variable

while selection != number:
    selection = validate_number_selection(maximum = 10, minimum = 0, message="guess a number between 0-10: ")

print('You win!')
```

Asking user which condiment they want

```
from sdu.validation import validate_choices

# Stays in loop until user enters one of the valid_choices
condiment = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo'])
```

"""

from .type_conversions import stringify_list

def validate_number_selection(maximum = 1, minimum=0, message = "Please select one of the above options: ") -> int:
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

    Examples
    --------
    Random number guessing game

    ```
    import random
    
    from sdu.validation import validate_number_selection

    number = random.randint(0,10)

    selection = -1 # initialize variable

    while selection != number:
        selection = validate_number_selection(maximum = 10, minimum = 0, message="guess a number between 0-10: ")

    print('You win!')
    ```
    
    Returns
    -------
    int|float:
        The validated result from the user
    """

    valid_answer = False

    while valid_answer == False:
        try: # Catches if answer is not int or float
            selection = eval(input(message))
        except:
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
    condiment = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo'])
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
    
    stringified_choices = stringify_list(valid_choices, seperator=" or")

    while 1:
        if display_choices:
            response = input(message + f"({stringified_choices})?: ")

        else:
            response = input(message)

        if response.lower().strip() in valid_choices:
            return response
        else:
            print(f"Message provided was not one of the choices; {stringified_choices}")

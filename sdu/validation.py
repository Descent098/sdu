"""A set of common validation schemes.

Functions
---------
validate_number_selection -> int|float:
    Used to validate user input is within range minimum < input < maximum. Keeps user in loop
    until input is within range.
"""

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

    Returns
    -------
    int|float:
        The validated result from the user

    Examples
    --------
    Random number guessing game

    ```
    >> import random
    
    >> from sdu.validation import validate_number_selection

    >> number = random.randint(0,10)

    >> selection = -1 # initialize variable

    >> while selection != number:
        selection = validate_number_selection(maximum = 10, minimum = 0, message="guess a number between 0-10: ")

    >> print('You win!')
    ```

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
r"""This module is for quick and common conversions between types with sensible options.

Functions
---------
stringify_list -> str:
    Takes in a one-dimensional list and creates a nicely formatted string out of it.

Examples
--------
Print a shopping list with each item on a new line.

```
from sdu.type_conversions import stringify_list

shopping_list = ["eggs", "ham", "spam"]

print((stringify_list(shopping_list, seperator='\n', spacing=0))) # Prints list with each item on new line
```
"""

# Internal Dependencies
import logging

def stringify_list(input_list:list, seperator:str = ' ', spacing:int = 1) -> str:
    """Takes a list and stringifies it to a readable format
    
    Parameters
    ----------
    input_list:(list|tuple)
        The list to stringify
    
    seperator:(str)
        What to delimit each element of the list with. Default is single space.
    
    spacing:(int)
        The amount of spaces to add after each seperator (set to 0 for no spacing). Default is single space.

    Examples
    --------
    ```
    from sdu.type_conversions import stringify_list
    
    print(stringify_list(['Hello','world'] , spacing = 2, seperator = ',')) # Prints: 'Hello,  world' 
    ```

    Notes
    -----
    - Input list/tuple must be one dimensional

    Returns
    -------
    str:
        The formatted string representation of the list/tuple
    """
    logging.info(f"Beginning list ({input_list}) stringification with '{seperator}' seperators")
    spacing = " " * spacing
    if not (type(input_list) == list or type(input_list) == tuple):
        raise ValueError("Expected list of arguments, got string instead")

    stringified = ""

    for count, argument in enumerate(input_list): # Preprocess arguments into appropriate string form
        if count == len(input_list) - 1:
            stringified += argument
            break
        stringified += f"{argument}{seperator}{spacing}"
    
    logging.debug(f"Stringified: {stringified}")

    return stringified

"""This module is for quick and common conversions between types with sensible options such as:

- Converting a dictionary to a defaultdictionary

Functions
---------
dict_to_defaultdict -> defaultdict:
    Takes in a dictionary, and a default Callable then converts the dict to a defaultdict

Examples
--------
### Convert a user dictionary to a defaultdict
```
from sdu.type_conversions import dict_to_defaultdict

user = {'Name':'John',
'Phone':{ # This will be converted to a defaultdict also
    'Manufacturer':'Nokia',
    'Model':'Cityman 100',
    'Release Date': 1998,
    },
'Age':13}

print(dict_to_defaultdict(user)) # defaultdict(<function <lambda> at 0x000002CF4C278E50>, {'Name': 'John', 'Phone': defaultdict(<function <lambda> at 0x000002CF4C278E50>, {'Manufacturer': 'Nokia', 'Model': 'Cityman 100', 'Release Date': 1998}), 'Age': 13})
```
"""

# Internal Dependencies
import logging
from typing import Callable
from collections import defaultdict


def dict_to_defaultdict(original_dict:dict, default:Callable = lambda:False) -> defaultdict:
    """Takes in a dictionary, and a default Callable then converts the dict to a defaultdict

    Parameters
    ----------
    original_dict : dict
        The original dictionary to convert to a defaultdict
    default : Callable, optional
        The argument to pass to the defaultdict constructor, by default it's lambda:False

    Notes
    -----
    This function will convert second dimension dictionaries (nested dictionaries) to defaultdicts also

    Returns
    -------
    defaultdict
        The original dict, converted to a defaultdict

    Examples
    --------
    Convert a user dictionary to a defaultdict
    ```
    from sdu.type_conversions import dict_to_defaultdict

    user = {'Name':'John',
    'Phone':{ # This will be converted to a defaultdict also
        'Manufacturer':'Nokia',
        'Model':'Cityman 100',
        'Release Date': 1998,
        },
    'Age':13}

    print(dict_to_defaultdict(user)) # defaultdict(<function <lambda> at 0x000002CF4C278E50>, {'Name': 'John', 'Phone': defaultdict(<function <lambda> at 0x000002CF4C278E50>, {'Manufacturer': 'Nokia', 'Model': 'Cityman 100', 'Release Date': 1998}), 'Age': 13})
    ```
    """
    logging.info(f"Beginning defaultdict conversion of {original_dict}")
    result = defaultdict(default)
    for key in original_dict:
        if type(original_dict[key]) == dict:
            logging.debug(f"Found dict at {key}: {original_dict[key]}")
            temp_dict = defaultdict(default)
            for current_key in original_dict[key]:
                temp_dict[current_key] = original_dict[key][current_key]
            logging.debug(f"Inner dict at {key} converted to: {temp_dict}")
            original_dict[key] = temp_dict
        result[key] = original_dict[key]
    logging.info(f"Returning {result}")
    return result

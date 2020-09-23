"""This set of test to tests the type_conversions module and it's functions"""
# Internal Dependencies
from collections import defaultdict  # Used to validate output of dict_to_defaultdict()

# Internal Dependencies
from sdu.type_conversions import *  # Functionality being tested


def test_dict_to_defaultdict():
    """Testing the dict_to_defaultdict() method in sdu.type_conversions
    Cases
    -----
    - Validating that a dictionary is converted to a defaultdict
    - Validating that a second dimensional dict is converted to a defaultdict
    """
    test = {'Name':'John',
    'Phone':{ # This will be converted to a defaultdict also
        'Manufacturer':'Nokia',
        'Model':'Cityman 100',
        'Release Date': 1998,
        },
    'Age':13}

    # Building the correct output to validate against
    correct_output = defaultdict(lambda: False)
    correct_output["Name"] = "John"
    correct_output["Age"] = 13

    # Building the Phone key for the correct_output inner dict
    correct_output_inner_dict = defaultdict(lambda: False)
    correct_output_inner_dict["Manufacturer"] = "Nokia"
    correct_output_inner_dict["Model"] = "Cityman 100"
    correct_output_inner_dict["Release Date"] = 1998

    # Assigning the inner dict to the Phone key
    correct_output["Phone"] = correct_output_inner_dict

    test = dict_to_defaultdict(test)

    assert type(test) == defaultdict
    assert type(test["Phone"]) == defaultdict
    assert test == correct_output

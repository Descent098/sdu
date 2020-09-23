"""This set of test to tests the validation module and it's functions"""

# Standard Library Dependencies
from unittest import mock     # Used to fake results

# Internal Dependencies
from sdu.validation import *  # Functionality that's being tested

@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["-1", "11", "5"])  # Capture input() output
def test_validate_number_selection_invalid(mock_choice, mock_print):
    """Validates that invalid cases are caught for sdu.validation.validate_number_selection

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock

    Cases
    -----
    - Input lower than minimum
    - Input higher than maximum
    """
    minimum = 0
    maximum = 10
    message = ""
    result = validate_number_selection(minimum = minimum, maximum = maximum, message = message)
    assert result == 5
    assert mock_print.call_count == 2 # Check that all calls were made


@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["0", "5", "10"]) # Capture input() output
def test_validate_number_selection_valid(mock_choice, mock_print):
    """Validates that valid cases work for sdu.validation.validate_number_selection

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock

    Cases
    -----
    - Input is minumim
    - Input is in middle of range
    - Input is maximum
    """
    minimum = 0
    maximum = 10
    message = ""

    # Validate minimum is in range
    result = validate_number_selection(minimum = minimum, maximum = maximum, message = message)
    assert result == 0

    # Validate a random middle term is in range
    result = validate_number_selection(minimum = minimum, maximum = maximum, message = message)
    assert result == 5

    # Validate maximum is in range
    result = validate_number_selection(minimum = minimum, maximum = maximum, message = message)
    assert result == 10

@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["zz", "qq", "Ketchup"]) # Capture input() output
def test_validate_choices_invalid(mock_choice, mock_print):
    """Validates that invalid cases are caught for sdu.validation.validate_choices

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock

    Cases
    -----
    - Two different invalid choices; zz and qq
    """
    result = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo'])
    mock_print.assert_called_with("Selection provided was not one of the choices; ketchup or mayo")
    assert mock_print.call_count == 2 # Check that all calls were made
    assert result == "Ketchup"

@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["Ketchup", "mayo "]) # Capture input() output
def test_validate_choices_valid(mock_choice, mock_print):
    """Validates that valid cases work for sdu.validation.validate_choices

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock
    
    Cases
    -----
    - Both Valid choices; Ketchup and mayo 
    """
    result = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo'])
    assert result == "Ketchup"
    result = validate_choices('What condiment do you want', valid_choices=['Ketchup', 'Mayo'])
    assert result == "mayo "


@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["q", "l", "z", "y"]) # Capture input() output
def test_confirm_invalid(mock_choice, mock_print):
    """Validates that invalid cases are caught for sdu.validataion.confirm

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock
    
    Cases
    -----
    - Three Invalid inputs; q, 1, z
    """
    result = confirm("Question")
    
    mock_print.assert_called_with("\x1b[38;5;1mPlease respond with either yes or no\n\x1b[38;5;15m")

    assert mock_print.call_count == 3 # Check that all calls were made
    assert result


@mock.patch('sdu.validation.print') # Capture print() output
@mock.patch('sdu.validation.input', side_effect = ["y", "n"]) # Capture input() output
def test_confirm_valid(mock_choice, mock_print):
    """Validates if valid cases are working for sdu.validataion.confirm

    Parameters
    ----------
    mock_choice : 
        contains info about patched input() mock
    mock_print :
        contains info about patched print() mock

    Cases
    -----
    - Both valid options; y, n
    """
    result = confirm("Question")
    assert result
    result = confirm("Question")
    assert not result

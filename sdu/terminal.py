r"""Utilities for generating CLI's

Functions
---------
clear_terminal:
    Clears the current terminal.

select_directory -> str:
    Allows user to select a directory and returns the path as a string.

center_text -> str:
    Takes a string and returns the centered result as a string.

Examples
--------
Clearing terminal after filling it with hello's

```
from sdu.terminal import clear_terminal

print('hello\n'*250) # Fill screen with hello's

clear_terminal() # Clears the terminal NOTE: cross platform
```

Ask someone if they want fries with that.

```
from sdu.terminal import confirm

with_fries = confirm('Do you want fries with that?')

if with_fries:
    print('Here are your fries')
else:
    print('No fry for you')
```

Notes
-----
- Unless otherwise specified all functions are cross-platform (*nix/MacOS & Windows)
"""

# Standard lib dependencies
import os

# Internal Dependencies
from .validation import validate_number_selection

# External Dependencies
import colored

def clear_terminal() -> None:
    """Clears the current terminal.
    
    Examples
    --------
    Clearing terminal after filling it with hello's

    ```
    from sdu.terminal import clear_terminal
    
    print('hello\n'*250) # Fill screen with hello's

    clear_terminal() # Clears the terminal NOTE: cross platform
    ```
    """
    if os.name=='nt': # PORT: Windows
        os.system('cls')

    else: # PORT: *nix
        os.system('clear')

def _cli_directory() -> str:
    """Provides a full CLI for selecting and/or creating directories
    
    Examples
    --------
    Taking input to save content to a directory

    ```
    import os

    save_folder = _cli_directory()

    with open('save_folder{}blah.txt'.format(os.sep), 'w') as output_file:
        output_file.write('blah')
    ```

    Returns
    -------
    str: 
        The path to the directory chosen"""
    selected_directory = False # Remains false while no existing directory has been selected

    while not selected_directory:
        current_dir_contents = ' | '.join(map(str, os.listdir()))
        clear_terminal()

        # Prints the current files and folders in directory
        print("Current directory is {} \n\nThe directory contains: \n{}".format(os.getcwd(), current_dir_contents))

        choice = input("\nNote: you can use .. to go up a directory and mkdir to create a directory \nPlease select a directory: ")

        if "mkdir" in choice.lower():  # Create a directory Dialouge
            directory_name = str(input("What would you like to call the directory?: "))
            try:
                os.mkdir(directory_name)
            except expression as identifier:
                print("Invalid selection made \nError: {}".format(identifier))

        elif choice.lower() == "here":  # If they've selected the right folder
            chosen_directory = os.getcwd()
            return chosen_directory

        elif not choice.lower() == "here":  # If user wants to navigate to a different folder
            try:
                os.chdir(choice)
                selection = validate_number_selection(maximum = 2, minimum = 1,
                message="Current Path: {} \nWould you like to use the current path? (1)Yes (2)No :".format(os.getcwd()) )

                if selection == 1:
                    chosen_directory = os.getcwd()
                    return chosen_directory
                    selected_directory = True
                else:
                    continue
            except NotADirectoryError:
                print("Invalid selection made, choice is not a directory")

def select_directory(gui=False) -> str:
    """Allows user to select a directory and returns the path as a string.

    Parameters
    ----------
    gui:(bool)
        Specify whether or not you want a tkinter dialogue box for picking
        the directory or a cli based directory selection.
        
    Examples
    --------
    Taking input to save content to a directory

    ```
    import os

    save_folder = select_directory(gui=True)

    with open('save_folder{}blah.txt'.format(os.sep), 'w') as output_file:
        output_file.write('blah')
    ```

    Returns
    -------
    str:
        The path to the directory selected
    """

    if gui == False: #Terminal/cmd based path selector
        return _cli_directory()

    if gui == True: # GUI based file selector
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = str(filedialog.askdirectory(
                title="Specify Directory",
                mustexist=False))
        return file_path

def center_text(message = "Hello World!") -> str:
    """Takes a string and returns the centered result as a string.

    Parameters
    ----------
    message: (str)
        The message to center

    Examples
    --------
    Printing someones name centered in terminal.

    ```
    from sdu.terminal import center_text

    name = input('what is your name?:')

    print(center_text(name))
    ```

    Returns
    -------
    str:
        The message string centered.

    """
    import shutil
    columns = shutil.get_terminal_size().columns
    return(message.center(columns))

def confirm(message:str) -> bool:
    """Used to validate users input is yes or no.
    
    Parameters
    ----------
    message: (str)
        The message to display for confirmation

    Examples
    --------
    Ask someone if they want fries with that.

    ```
    from sdu.terminal import confirm

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


if __name__ == "__main__":
    confirm("Yeet?")
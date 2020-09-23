"""A module for helpful utilities with generating CLI's such as:

- Clearing the terminal
- Centering text
- Choosing a directory (from gui and CLI)

Functions
---------
clear_terminal:
    Clears the current terminal

select_directory -> str:
    Allows user to select a directory and returns the path as a string

center_text -> str:
    Takes a string and returns the centered result as a string

Aliases
-------
All the functions below are aliases to existing functions to
make usage simpler

remove_directory:
    an alias for shutil.rmtree which deletes directories

Examples
--------
### Clearing terminal after filling it with hello's

```
from sdu.cli import clear_terminal

print('hello\n'*250) # Fill screen with hello's

clear_terminal()
```

### Taking input to save content to a directory

```
import os
from sdu.cli import select_directory

save_folder = select_directory()

with open(f'{save_folder}{os.sep}blah.txt', 'w') as output_file:
    output_file.write('blah')
```

### Printing someones name centered in terminal

```
from sdu.cli import center_text

name = input('what is your name?:')

print(center_text(name))
```

### Removing a directory

```
from sdu.cli import remove_directory

remove_directory("/path/to/delete")
```
"""

# Standard lib dependencies
import os  # Used to validate and grab paths
from shutil import rmtree as remove_directory

# Internal Dependencies
from sdu.validation import validate_number_selection  # Used to validate number selections in functions

# External Dependencies
import colored  # Used to colour stdout output for emphasis

def clear_terminal() -> None:
    """Clears the current terminal.
    
    Examples
    --------
    Clearing terminal after filling it with hello's

    ```
    from sdu.cli import clear_terminal
    
    print('hello'*250) # Fill screen with hello's

    clear_terminal() # Clears the terminal NOTE: cross platform
    ```
    """
    if os.name=='nt': # PORT: Windows
        os.system('cls')

    else: # PORT: *nix
        os.system('clear')

def _cli_directory(starting_dir:str = ".") -> str:
    """Provides a full CLI for selecting and/or creating directories
    
    Examples
    --------
    Taking input to save content to a directory

    ```
    import os
    from sdu.cli import _cli_directory

    save_folder = _cli_directory()

    with open('save_folder{}blah.txt'.format(os.sep), 'w') as output_file:
        output_file.write('blah')
    ```

    Returns
    -------
    str: 
        The path to the directory chosen"""
    selected_directory = False # Remains false while no existing directory has been selected
    original_dir = os.path.abspath(".")
    choice = "" # Initialize choice to an empty string
    controls = f"""Controls: 
    Type .. to go up a directory 
    Type the name of a directory to change into it
    Type mkdir to create a directory
    Type ls to show all files in current folder

    {colored.fg(2)}Type here or . to select current directory{colored.fg(15)}
    """

    if not starting_dir == ".":
        os.chdir(starting_dir)

    while not selected_directory:
        if choice == "ls":
            current_dir_contents = ' | '.join(map(str, [directory for directory in os.listdir()]))
        else:
            current_dir_contents = ' | '.join(map(str, [directory for directory in os.listdir() if os.path.isdir(directory)]))
        clear_terminal()

        # Prints the current files and folders in directory
        print(f"{controls}\n\nCurrent directory is {os.getcwd()} \n\nThe directory contains: \n{current_dir_contents}")

        choice = input("\n> ")

        if "mkdir" in choice.lower():  # Create a directory Dialouge
            directory_name = str(input("What would you like to call the directory?: "))
            try:
                os.mkdir(directory_name)
            except Exception as identifier:
                print("Invalid selection made \nError: {}".format(identifier))

        elif choice.lower() == "here" or choice.lower() == ".":  # If they've selected the right folder
            chosen_directory = os.getcwd()
            return chosen_directory

        elif not choice.lower() == "here" or choice.lower() == ".":  # If user wants to navigate to a different folder
            try:
                os.chdir(choice)
            except NotADirectoryError:
                continue
            except FileNotFoundError:
                continue


def select_directory(gui:bool = False, starting_dir:str = ".") -> str:
    """Allows user to select a directory and returns the path as a string.

    Parameters
    ----------
    gui:(bool)
        Specify whether or not you want a tkinter dialogue box for picking
        the directory or a cli based directory selection

    starting_dir:(str)
        The directory for the selection to start from

    Examples
    --------
    Taking input to save content to a directory

    ```
    import os
    from sdu.cli import select_directory

    save_folder = select_directory()

    with open(f'{save_folder}{os.sep}blah.txt', 'w') as output_file:
        output_file.write('blah')
    ```

    Returns
    -------
    str:
        The path to the directory selected
    """

    if gui == False: #Terminal/cmd based path selector
        return _cli_directory(starting_dir = starting_dir)

    if gui == True: # GUI based file selector
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = str(filedialog.askdirectory(title="Specify Directory", mustexist = False, initialdir = starting_dir))
        return file_path

def center_text(message:str) -> str:
    """Takes a string and returns the centered result as a string.

    Parameters
    ----------
    message: (str)
        The message to center

    Examples
    --------
    Printing someones name centered in terminal.

    ```
    from sdu.cli import center_text

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

if __name__ == "__main__":
    save_folder = select_directory(starting_dir=f"{os.environ['USERPROFILE']}\\Desktop")

    with open(f'{save_folder}{os.sep}blah.txt', 'w') as output_file:
        output_file.write('blah')

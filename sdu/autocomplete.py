"""This module is used to generate autocomplete files for various systems (bash, zsh etc.)

Module Variables
----------------

command (namedtuple):
    Defines the schema for commands that is used
    to generate autocomplete files.

Examples
--------

### Creating a bash autocomplete file
```
from sdu.autocomplete import generate_bash_autocomplete, command

root = 'command' # Replace this with the name of your root command (what you type in terminal to use cli)

commands =  [ # Used for autocompletion generation
    command("docs", ["-a", "--api", "-o", "--offline"]),
    command("register", [])
]

# Output is too long to display in this docstring
print(generate_bash_autocomplete(root, commands)) 
```
"""

# Standard lib dependencies

import logging                        # Used to log valueable logging info
from collections import namedtuple    # Used to setup command schema for feeding autocomplete

command = namedtuple("command", ["name", "arguments"])


def _generate_root_autocomplete(root:str, commands:list , arguments:list = []) -> str:
    """Generates the first portion of a bash autocomplete file"""
    logging.info("Beginning bash root command autocomplete generation")
    arguments = _stringify_list(arguments)

    root_template = f"""_{root}()
    {{
        local cur
        cur=\"${{COMP_WORDS[COMP_CWORD]}}\"

        if [ $COMP_CWORD -eq 1 ]; then
            COMPREPLY=( $( compgen -fW '{arguments} {_stringify_list(commands)}' -- $cur) )
        else
            case ${{COMP_WORDS[1]}} in
    """

    for command in commands:
        root_template += f"""
                {command})
                _{root}_{command}
            ;;
        """

    root_template+="""
            esac

        fi
    }
    """

    logging.debug(f"Root Template: {root_template}")


    return root_template

def _generate_command_autocomplete(root:str, command:str, arguments:list) -> str:
    """Generates a bash autocomplete section for a single command"""
    logging.info(f"Beginning command autocomplete generation for command {command} with arguments {arguments}")

    if arguments:
        arguments = _stringify_list(arguments)
    else:
        arguments = " "
    command_result = f"""_{root}_{command}()
    {{
        local cur
        cur=\"${{COMP_WORDS[COMP_CWORD]}}\"

        if [ $COMP_CWORD -ge 2 ]; then
            COMPREPLY=( $( compgen -W '{arguments}' -- $cur) )
        fi
    }}
    """

    logging.debug(f"Command Result: {command_result}")

    return command_result


def _stringify_list(arguments:list) -> str:
    """Takes a list and stringifies it to a useable format for autocomplete files
    
    Examples
    --------
    ```
    >> _stringify_list(["-a", "--api", "-o", "--offline"]) # Returns: '-a --api -o --offline' 
    ```
    """
    logging.info(f"Beginning list ({arguments})  stringification")
    if not (type(arguments) == list or type(arguments) == tuple):
        raise ValueError("Expected list of arguments, got string instead")

    stringified = ""

    for argument in arguments: # Preprocess arguments into appropriate string form
        stringified += f" {argument}"
    
    logging.debug(f"Stringified: {stringified}")

    return stringified


def generate_bash_autocomplete(root:str, commands:list) -> str:
    """Takes a list of commands (namedtuple type) and returns the text necessary
    for a bash autocomplete file

    Parameters
    ----------
    root: (str)
        The string signifying the base programs name

    commands: (list[namedtuple])
        A list of the commands to generate the autocomplete file for
    
    Examples
    --------
    ```
    >> commands =  [ # Used for autocompletion generation
        command("docs", ["-a", "--api", "-o", "--offline"]),
        command("register", [])
    ]

    >> # Output is too long to display in this docstring
    >> print(generate_bash_autocomplete(commands)) 
    ```
    """
    logging.info("Beginning bash autocompletion generation")

    if not type(commands) == list:
        raise ValueError("Expected list of commands, got string instead")

    sub_commands = [root] # list of just top level sub-commands
    for command in commands: # Iterate through and pull just subcommands from commands list
        sub_commands.append(command.name)

    arguments = ["-h", "--help", "-v", "--version"]
    for command in commands:
        for argument in command.arguments:
            arguments.append(argument)
    
    autocomplete_text = _generate_root_autocomplete(root, sub_commands, arguments)

    for command in commands:
        autocomplete_text += _generate_command_autocomplete(root, command.name, command.arguments)


    autocomplete_text += f"\ncomplete -o bashdefault -o default -o filenames -F _{root} {root}\n"

    logging.debug(f"Autocomplete Text: {autocomplete_text}")

    return autocomplete_text

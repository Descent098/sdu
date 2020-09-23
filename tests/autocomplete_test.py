import pytest
from sdu.autocomplete import generate_bash_autocomplete, command, _stringify_list

def test_stringify_list():
    """Testing the _stringify_list() function from sdu/autocompletion.py
    
    Cases
    -----
    - List case (expected input)
    - Empty list case
    - Tuple case (expected input)
    - String case (Error)
    """

    # List case
    assert _stringify_list(["-a", "--api", "-o", "--offline"]) == ' -a --api -o --offline'

    # Empty list case
    assert _stringify_list([]) == ''

    # Tuple case
    assert _stringify_list(("-a", "--api", "-o", "--offline")) == ' -a --api -o --offline'

    # String case
    with pytest.raises(ValueError):
        _stringify_list(" -a --api -o --offline")

def test_bash_generation():
    """Validates that the generate_bash_autocomplete() function in sdu/autocompletion.py
    generates the correct file."""

    commands =  [
        command("docs", ["-a", "--api", "-o", "--offline"]),
        command("register", []),
        command("config", ["-e", "--export", "-i", "--import"])
        ]

    correct_output = f'''_ahd()
    {{
        local cur
        cur="${{COMP_WORDS[COMP_CWORD]}}"

        if [ $COMP_CWORD -eq 1 ]; then
            COMPREPLY=( $( compgen -fW \' -h --help -v --version -a --api -o --offline -e --export -i --import  ahd docs register config\' -- $cur) )
        else
            case ${{COMP_WORDS[1]}} in
    
                ahd)
                _ahd_ahd
            ;;
        
                docs)
                _ahd_docs
            ;;
        
                register)
                _ahd_register
            ;;
        
                config)
                _ahd_config
            ;;
        
            esac

        fi
    }}
    _ahd_docs()
    {{
        local cur
        cur="${{COMP_WORDS[COMP_CWORD]}}"

        if [ $COMP_CWORD -ge 2 ]; then
            COMPREPLY=( $( compgen -W \' -a --api -o --offline\' -- $cur) )
        fi
    }}
    _ahd_register()
    {{
        local cur
        cur="${{COMP_WORDS[COMP_CWORD]}}"

        if [ $COMP_CWORD -ge 2 ]; then
            COMPREPLY=( $( compgen -W \' \' -- $cur) )
        fi
    }}
    _ahd_config()
    {{
        local cur
        cur="${{COMP_WORDS[COMP_CWORD]}}"

        if [ $COMP_CWORD -ge 2 ]; then
            COMPREPLY=( $( compgen -W \' -e --export -i --import\' -- $cur) )
        fi
    }}
    
complete -o bashdefault -o default -o filenames -F _ahd ahd
'''

    assert generate_bash_autocomplete("ahd", commands) == correct_output 

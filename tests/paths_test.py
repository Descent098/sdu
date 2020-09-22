"""This set of test tests the paths module and it's functions"""

import os

import glob

from sdu.paths import *

def test_preprocess_paths():
    """Validates that input paths are serialized in a normalized format across OS's.
    
    Cases
    -----
    - Relative paths; .
    - Home directory; ~
    - Wildcards; *
    - Windows (only on windows machine)
    - *nix/MacOS (only on *nix/MacOS machine)
    """

    if os.name == "nt": # Test windows cases
        win_paths = ['~/Documents', f'{os.getenv("USERPROFILE")}\\Desktop\\Development\\*', '~\\Downloads', '.']
        
        assert preprocess_paths(win_paths) == ["~/Documents","~/Desktop/Development/*","~/Downloads","."]
    
    else: # Test *nix cases
        nix_paths = ['~/Documents', f"{os.getenv('HOME')}/Desktop/Development/*", '~/Downloads', '.']

        assert preprocess_paths(nix_paths) == ["~/Documents","~/Desktop/Development/*","~/Downloads","."]


def test_postprocess_paths():
    """Validates that pre-processed paths are deserialized properly on a per OS basis.
    
    Cases
    -----
    - Relative paths; .
    - Home directory; ~
    - Wildcards; *
    - Windows (only on windows machine)
    - *nix/MacOS (only on *nix/MacOS machine)
    """
    
    paths = ['~/Documents', '~/Desktop/*' , '~/Downloads' , '.']
    
    if os.name == "nt": # Windows case
        correct_paths = [f"{os.getenv('USERPROFILE')}\\Documents"]
        for current_path in glob.glob(f"{os.getenv('USERPROFILE')}\\Desktop\\*"):
            if os.path.isdir(current_path):
                correct_paths.append(current_path)
        correct_paths.append(f"{os.getenv('USERPROFILE')}\\Downloads")
        correct_paths.append(os.path.abspath("."))
        assert postprocess_paths(paths) == correct_paths
    
    else: # Test *nix cases
        correct_paths = [f"{os.getenv('HOME')}/Documents"]
        for current_path in glob.glob(f"{os.getenv('HOME')}/Desktop/*"):
            if os.path.isdir(current_path):
                correct_paths.append(current_path)
        correct_paths.append(f"{os.getenv('HOME')}/Downloads")
        correct_paths.append(os.path.abspath("."))
        assert postprocess_paths(paths) == correct_paths

def test_process_paths():
    """Validates that input paths are serialized in a normalized format across OS's.
    
    Cases
    -----
    - Relative paths; .
    - Home directory; ~
    - Wildcards; *
    - Windows (only on windows machine)
    - *nix/MacOS (only on *nix/MacOS machine)
    """

    paths = ['~/Documents', '~/Desktop/*' , '~\\Downloads' , '.']
    
    if os.name == "nt": # Windows case
        correct_paths = [f"{os.getenv('USERPROFILE')}\\Documents"]
        for current_path in glob.glob(f"{os.getenv('USERPROFILE')}\\Desktop\\*"):
            if os.path.isdir(current_path):
                correct_paths.append(current_path)
        correct_paths.append(f"{os.getenv('USERPROFILE')}\\Downloads")
        correct_paths.append(os.path.abspath("."))
        assert process_paths(paths) == correct_paths
    
    else: # Test *nix cases
        correct_paths = [f"{os.getenv('HOME')}/Documents"]
        for current_path in glob.glob(f"{os.getenv('HOME')}/Desktop/*"):
            if os.path.isdir(current_path):
                correct_paths.append(current_path)
        correct_paths.append(f"{os.getenv('HOME')}/Downloads")
        correct_paths.append(os.path.abspath("."))
        assert process_paths(paths) == correct_paths
"""Utilities for dealing with system paths.

Functions
---------
preprocess_paths -> list:
    Preprocesses paths to normalize them as standard unix-style paths. See notes for details

postprocess_paths -> list:
    Postprocesses existing paths to be used by dispatcher.
        This means things like expanding wildcards, and processing correct path seperators.

process_paths -> list:
    Takes a list or tuple of paths and normalizes and globs them. See notes for details.

Examples
--------
An example of the preprocessing to postprocessing pipeline on a windows machine (because of the wildcard and OS results will vary)

```
from sdu.paths import preprocess_paths, postprocess_paths

paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']

print(preprocess_paths(paths)) # Prints: ['~/Desktop/Development/Canadian Coding/SSB', '~/Desktop/Development/*' , '~/Desktop/Development/Personal/noter', '.']

print(postprocess_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
```

An example of path processing on a windows machine (because of the wildcard and OS results will vary)

```
from sdu.paths import process_paths

paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']

print(process_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
```

See Also
--------
Glob module information: https://docs.python.org/3/library/glob.html

"""

# Standard lib dependencies
import re
import os
import glob
import copy
import logging


def preprocess_paths(paths:list) -> list:
    """Preprocesses paths to normalize them as standard unix-style paths.

    Parameters
    ----------
    paths : (list|tuple)
        A list or tuple of paths, can be relative or absolute. See Notes for details.
    
    Example
    -------
    An example of the preprocessing function on a windows machine.

    ```
    paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']
    
    print(preprocess_paths(paths)) # Prints: ['~/Desktop/Development/Canadian Coding/SSB', '~/Desktop/Development/*' , '~/Desktop/Development/Personal/noter', '.']
    ```

    Notes 
    -----
    - This function does not change '.' paths unless they include a relative path to a separate folder. i.e. a plain '.' is untouched but './folder-name' is converted to an absolute path.
    - This function leaves in *'s, and brackets since the postprocessing function globs paths and uses those characters for processing.
    - This function will take the HOME(*nix) or USERPROFILE(windows) environment variables and convert them to a ~

    Returns
    -------
    list:
        The normalized & preprocessed paths
    """
    logging.info(f"Beginning path preprocessing on {paths}")
    result = list(copy.deepcopy(paths))

    for index, directory in enumerate(result):
        directory = directory.strip()
        logging.debug(f"Directory: {directory}")
        # Convert relative directories to absolute directories
        if directory.startswith(".") and (len(directory) > 1):
            directory = os.path.abspath(directory)
        # Replace HOME values
        if not directory.startswith("~"):
            if not os.name == "nt": # Not windows
                directory = directory.replace(os.getenv('HOME'),"~")

        # Replace backslashes (windows) with slashes (*nix)
        directory = directory.replace("\\", "/")

        # Replace old path with preprocessed form
        result[index] = directory

    # Remove the %USERPROFILE% from windows paths
    regex = r"([A-Z]:/Users/.*)"
    matches = re.finditer(regex, "\n".join(result), re.MULTILINE | re.IGNORECASE)
    matches = [match.group() for match in matches]
    for path in matches:
        path_index = result.index(path)
        path = path.split("/")[2::] # Remove drive letter and username
        path[0] = "~"
        result[path_index] = "/".join(path)

    logging.debug(f"Result: {result}")

    return result

def postprocess_paths(paths:list, include_files = False, silent = True) -> list:
    """Postprocesses existing paths (assuming they've been preprocessed) for use in environment.
    This means things like expanding wildcards, and processing correct path seperators.
    
    Parameters
    ----------
    paths : (list|tuple)
        A list or tuple of paths, can be relative or absolute. See Notes for details.

    include_files : (bool)
        Whether to include file results into resulting list

    silent : (bool)
        Whether to throw an error if one of the paths is invalid

    Example
    -------
    An example of the preprocessing to postprocessing pipeline on a windows machine (because of the wildcard and OS results will vary)

    ```
    paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']
    
    print(preprocess_paths(paths)) # Prints: ['~/Desktop/Development/Canadian Coding/SSB', '~/Desktop/Development/*' , '~/Desktop/Development/Personal/noter', '.']
    print(postprocess_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
    ```

    Notes
    -----
    - In most cases you don't explicitly need to preprocess paths if they are unix paths,
        but I would recommend it since the function is designed to work on preprocessed paths.
    - Entering in raw windows paths as arguments will likely result in partially, or fully garbled paths.
        Although in some cases python will interpret the data properly and work, it is better to always use the preprocessor.

    Returns
    -------
    list:
        The list of useable paths (post-normalization & globing)

    See Also
    --------
    Glob module information: https://docs.python.org/3/library/glob.html
    """
    logging.info(f"Beginning path postprocessing on {paths}")

    result = []
    for directory in paths:
        directory = directory.strip()
        if os.name == "nt":
            directory = directory.replace("/", "\\")
        if directory.startswith("."):
            try:
                if directory[1] == "/" or directory[1] == "\\":
                    directory = f"{os.curdir}{directory[1::]}"
            except IndexError:
                directory = os.path.abspath(".")

        if "~" in directory:
            if os.name == "nt":
                directory = directory.replace("~",f"{os.getenv('USERPROFILE')}")
            else:
                directory = directory.replace("~", f"{os.getenv('HOME')}")
        
        if "*" in directory or "[" in directory:
            wildcard_paths = glob.glob(directory.strip())
            for wildcard_directory in wildcard_paths:
                if os.path.isdir(wildcard_directory):
                    result.append(wildcard_directory)
        else:
            if not silent:
                if os.path.isdir(directory):
                    raise NotADirectoryError(f"Directory was not found on system: {directory}")
            if os.path.isdir(directory):
                result.append(directory)

    logging.debug(f"Result: {result}")
    return result

def process_paths(paths:list) -> list:
    """Takes a list or tuple of paths and normalizes and globs them. See notes for details.

    Parameters
    ----------
    paths : (list|tuple)
        A list or tuple of paths, can be relative or absolute. See Notes for details.

    Example
    -------
    An example of path processing on a windows machine (because of the wildcard and OS results will vary)

    ```
    paths = ['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']
    
    print(process_paths(paths)) # Prints: ['C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal', 'C:\\Users\\Kieran\\Desktop\\Development\\pystall', 'C:\\Users\\Kieran\\Desktop\\Development\\python-package-template', 'C:\\Users\\Kieran\\Desktop\\Development\\Work', 'C:\\Users\\Kieran\\Desktop\\Development\\Personal\\noter', 'C:\\Users\\Kieran\\Desktop\\sdu'] 
    ```

    Notes
    -----
    - Since this function runs the preprocess_paths() & postprocess_paths() functions all 
        implications are carried through to this function including:

        - This function does not change '.' paths unless they include a relative path to a separate folder. i.e. a plain '.' is untouched but './folder-name' is converted to an absolute path.
        - This function leaves in *'s, and brackets and globs paths using those characters for processing.
        - This function will take the HOME(*nix) or USERPROFILE(windows) environment variables and interpret them appropriately per OS.
    
    See Also
    --------
    Glob module information: https://docs.python.org/3/library/glob.html
    """

    if not type(paths) == list and not type(paths) == tuple:
        raise ValueError("Paths must be specified as a list or tuple")
    result = copy.deepcopy(paths)
    result = preprocess_paths(result)
    result = postprocess_paths(result)
    return result

if __name__ == "__main__":
    print(process_paths(['~/Desktop/Development/Canadian Coding/SSB', 'C:\\Users\\Kieran\\Desktop\\Development\\*', '~\\Desktop\\Development\\Personal\\noter', '.']))

"""This module contains many useful utilities for dealing with system paths.

Functions
---------
preprocess_paths -> str:
    Preprocesses paths from input and splits + formats them into a useable list for later parsing.

postprocess_paths -> list:
    Postprocesses existing paths to be useable by system. This means things like expanding wildcards,
     and processing correct path seperators (os agnostic).

"""

import logging

def preprocess_paths(paths:str) -> str:
    """Preprocesses paths from input and splits + formats them
    into a useable list for later parsing.
    
    Example
    -------
    ```
    >> paths = '~/Desktop/Development/Canadian Coding/SSB, C:\\Users\\Kieran\\Desktop\\Development\\*, ~\\Desktop\\Development\\Personal\\noter, .'
    
    >> paths = _preprocess_paths(paths)
    print(paths) # Prints: '~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,.'
    ```

    Returns
    -------
    str:
        The preprocessed paths
    """
    logging.info(f"Beginning path preprocessing on {paths}")
    result = paths.split(",")
    for index, directory in enumerate(result):
        directory = directory.strip()
        logging.debug(f"Directory: {directory}")
        if directory.startswith(".") and (len(directory) > 1):
            directory = os.path.abspath(directory)
        if not "~" in directory:
            if os.name == "nt":
                directory = directory.replace(os.getenv('USERPROFILE'),"~")

            else:
                directory = directory.replace(os.getenv('HOME'),"~")
            directory = directory.replace("\\", "/")
            result[index] = directory
        else:
            directory = directory.replace("\\", "/")
            result[index] = directory

    logging.debug(f"Result: {result}")
    result = ",".join(result)

    return result

def postprocess_paths(paths:str) -> list:
    """Postprocesses existing paths to be used by dispatcher.
    This means things like expanding wildcards, and processing correct path seperators.
    
    Example
    -------
    ```
    paths = 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB, C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\website, ~/Desktop/Development/Personal/noter, C:\\Users\\Kieran\\Desktop\\Development\\*'
    
    paths = _preprocess_paths(paths)
    print(_postprocess_paths(paths)) 
    # Prints: ['C:/Users/Kieran/Desktop/Development/Canadian Coding/SSB', ' C:/Users/Kieran/Desktop/Development/Canadian Coding/website', ' C:/Users/Kieran/Desktop/Development/Personal/noter', 'C:/Users/Kieran/Desktop/Development/Canadian Coding', 'C:/Users/Kieran/Desktop/Development/Personal', 'C:/Users/Kieran/Desktop/Development/pystall', 'C:/Users/Kieran/Desktop/Development/python-package-template', 'C:/Users/Kieran/Desktop/Development/Work']
    ```

    Returns
    -------
    list:
        The list of useable paths (post-normalization)
    """
    logging.info(f"Beginning path postprocessing on {paths}")

    paths = paths.split(",")
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
        
        if "*" in directory:

            wildcard_paths = glob.glob(directory.strip())

            for wildcard_directory in wildcard_paths:
                wildcard_directory = wildcard_directory.replace("\\", "/")
                result.append(wildcard_directory)
        else:
            result.append(directory)

    logging.debug(f"Result: {result}")
    return result
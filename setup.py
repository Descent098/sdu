"""Contains all the configuration for the package on pip"""
import setuptools

def get_content(*filename:str) -> str:
    """ Gets the content of a file or files and returns
    it/them as a string
    Parameters
    ----------
    filename : (str)
        Name of file or set of files to pull content from 
        (comma delimited)
    
    Returns
    -------
    str:
        Content from the file or files
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content

setuptools.setup(
    name = "sdu", 
    version = "0.1.0", 
    author = "Kieran Wood",
    author_email = "kieran@canadiancoding.ca",
    description = "A set of utilites to make developing scripts simpler and easier",
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type = "text/markdown",
    url = "https://github.com/Descent098/sdu",
    include_package_data = True,
    packages = setuptools.find_packages(),
    install_requires = ["colored"], # Used to colour output
    extras_require = {
        "dev" : ["nox",   # Used to run automated processes
                "pytest", # Used to run the test code in the tests directory
                "pdoc3"], # Builds API documentation
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
)

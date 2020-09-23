# Changelog

## V0.1.0; September 24th
Focus was on adding more functionality, and modernizing the package setup.

### Features
- Added tests for ```paths```, ```type_conversions``` and ```validation```
- Removed ```type_conversion.stringify_list``` since functionality can be one-lined using ```str.join```
- Added ```type_conversion.dict_to_defaultdict```; Takes in a dictionary, and a default Callable then converts the dict to a defaultdict
- Changed From Apache V2 to MIT liscence
- Added ```paths.add_to_path``` for adding specified paths to system paths
- Added testing for ```sdu.paths```, ```sdu.validation```, ```sdu.autocomplete```, and ```sdu.type_conversions```
- Changed ```sdu.terminal``` to ```sdu.cli```
- Added ```sdu.autocomplete``` for generating bash autocomplete files

### Documentation Improvements
- Changed to second point releases (from 0.0.x to 0.x.0)
- Improved the index documentation to be more clear and concise of an overview
- Added bullet points to each package for a quick overview of what each module can be used for
- Overhauled readme to be more useful

### Bug Fixes
- Fixed some preprocessing bugs with windows in ```path.preprocess_paths()```

## V0.0.1; February 8th 2020

Released existing code for the project, looking to properly implement in v0.1.0

### Features

- Traversing directories in terminal and GUI
- Validating number selections
- Normalized serialization and de-serialization of paths

### Documentation improvements

- Created documentation site
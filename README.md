# Readme

## Requirements
  - Python >= 3.9

## Installation

```sh
# In order to not interfere with the system python installation, we will use venv to have a virtual environment
python -m venv env
# activate the created virtual environment
source env/bin/activate
# install all requirements
pip install -r requirements.txt
```

## Run unittests

```sh
# change directory to pytest
cd pytest
# Run the tests
python -m pytest tests
# Run the tests with execution times
python -m pytest tests --durations=0 -vv
```

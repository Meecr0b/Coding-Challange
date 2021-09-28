# Readme

## Requirements
  - Python >= 3.9

## Installation

```sh
# In order to not interfere with the system python, we will create a virtual enviroment with venv
python -m venv env
# activate the created virtual environment
source env/bin/activate
# install all requirements
pip install -r requirements.txt
```

## Run unittests

```sh
# Run the tests
python -m pytest tests
# Run the tests with execution times
python -m pytest tests --durations=0 -vv
```

## Howto use the merge function

in order to use the merge function, you have to import it
```python
from CodingChallange.merge import merge

intervals = [[25,30], [2,19], [14, 23], [4,8]]
merged_intervals = merge(intervals) # => [[2,23], [25,30]]
```

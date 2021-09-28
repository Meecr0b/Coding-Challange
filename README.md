# Readme

## Overview

the merge function will accept a list of intervals as parameter, merge them if they are overlapping, keep non-overlapping elements and return a merged list of intervals.

## Assumptions
 - intervals are only integer values
 - empty list of intervals should return an empty merged list
 - intervals are unordered

## Requirements
  - Python >= 3.9

## Preparation

```sh
# In order to not interfere with the system python, we will create a virtual enviroment with venv inside of the project folder
python -m venv env
# activate the created virtual environment
source env/bin/activate
# install all requirements
pip install -r requirements.txt
```

## Unittests

unittest can be found in the tests directory

### Run unittests

```sh
# Run the tests
python -m pytest tests
# Run the tests with execution times
python -m pytest tests --durations=0 -vv
```

## Howto use the merge function

in order to use the merge function, you have to import it
```python
from CodingChallenge.merge import merge

intervals = [[25,30], [2,19], [14, 23], [4,8]]
merged_intervals = merge(intervals) # => [[2,23], [25,30]]
```

## Run the example

```sh
python example.py
```

from typing import Generator

def merge(intervals: list) -> Generator[list, None, None]:
    # Validate intervals / Fail fast
    if type(intervals) != list:
        raise ValueError('Argument is not a list of intervals')
    # map reduce memory usage compared with a loop
    list(map(validate_interval, intervals))

    # sort on a list of lists will sort by the first index of each list element
    intervals.sort()

    if len(intervals):
        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= end:
                if interval[1] > end:
                    end = interval[1]
            else:
                yield [start, end]
                start = interval[0]
                end = interval[1]
        yield [start, end]

def validate_interval(interval: list) -> None:
    if type(interval) != list:
        raise ValueError('Interval is not a list')
    if len(interval) != 2:
        raise ValueError('Interval should exist of 2 elements')
    if type(interval[0]) != int:
        raise ValueError('First element of interval is not an integer')
    if type(interval[1]) != int:
        raise ValueError('Second element of interval is not an integer')

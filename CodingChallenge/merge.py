from typing import Generator

def merge(intervals: list) -> Generator[list, None, None]:
    """Merge all overlapping elements of a list of intervals, keep non-overlapping elements

    Parameters
    ----------
    intervals : list
         a list of intervals, e.g. [[25,30],[2,19],[14, 23],[4,8]]

    Returns
    -------
    Generator
        a generator over all merged elements
    """

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
            # if new interval is within the old interval
            if interval[0] <= end:
                # increase interval, if the new interval is larged than the old one
                if interval[1] > end:
                    end = interval[1]
            else:
                # yield interval because it is closed
                # generator, because it will use less memory during iteration
                yield [start, end]
                # start a new interval
                start = interval[0]
                end = interval[1]
        # also yield final interval
        yield [start, end]

def validate_interval(interval: list) -> None:
    """Validate a given interval

    Parameters
    ----------
    interval : list
         a interval, e.g. [25, 30]

    Raises
    ------
    ValueError
        will be raised if:
          - Parameter intervals is not a list
          - An element in interval is not a list
          - Interval should exist of 2 elements
          - Any element of an interval is not an integer
    """

    if type(interval) != list:
        raise ValueError('Interval is not a list')
    if len(interval) != 2:
        raise ValueError('Interval should exist of 2 elements')
    if type(interval[0]) != int:
        raise ValueError('First element of interval is not an integer')
    if type(interval[1]) != int:
        raise ValueError('Second element of interval is not an integer')

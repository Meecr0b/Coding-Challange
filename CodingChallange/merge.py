from typing import Generator

def merge(intervals: list) -> Generator[list, None, None]:
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

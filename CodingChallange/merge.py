from typing import Generator

def merge(intervals: list) -> list:
    response = []
    intervals.sort()
    start, end = intervals[0]
    for start_n, end_n in intervals[1:]:
        if start_n <= end:
            if end_n > end:
                end = end_n
        else:
            response.append([start, end])
            start = start_n
            end = end_n
    response.append([start, end])
    return response

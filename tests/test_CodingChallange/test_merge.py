from CodingChallange.merge import merge

def test_merge_example() -> None:
    # The expected result from the example provided
    intervals = [[25,30],[2,19],[14, 23],[4,8]]
    assert list(merge(intervals)) == [[2,23],[25,30]]

def test_merge_nothing_to_merge_ascending_order():
    # This will create a list of intervals with nothing to merge sorted in ascending order
    # [[1, 2], [3, 4], ..., [99, 100]]
    intervals = [[x, x+1] for x in range(1, 100, 2)]
    assert list(merge(intervals)) == [[x, x+1] for x in range(1, 100, 2)]

def test_merge_nothing_to_merge_descending_order():
    # This will create a list of intervals with nothing to merge sorted in descending order
    # [[99, 100], [97, 98], ..., [1, 2]]
    intervals = [[x-1, x] for x in range(100, 0, -2)]
    assert list(merge(intervals)) == [[x, x+1] for x in range(1, 100, 2)]

def test_merge_one_big_interval() -> None:
    # This will create a list of intervals, where the first element already includes all other intervals
    # [[1, 29999999], [2, 29999998], ....]
    intervals_size = 30000000
    intervals = [[x, intervals_size - x] for x in range(1, int(intervals_size/2))]
    assert list(merge(intervals)) == [[1,intervals_size-1]]

def test_merge_maximun_overlapping_intervals() -> None:
    # This will create a list of intervals, where every element overlaps by one
    # [[1, 15000001], [2, 15000002], ....]
    intervals_size = 30000000
    half_intervals_size = intervals_size/2
    intervals = [[x, int(half_intervals_size + x)] for x in range(1, int(half_intervals_size))]
    assert list(merge(intervals)) == [[1,intervals_size-1]]

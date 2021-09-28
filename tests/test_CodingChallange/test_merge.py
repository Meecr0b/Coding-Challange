from CodingChallange.merge import merge

def test_merge_example() -> None:
    intervals = [[25,30],[2,19],[14, 23],[4,8]]
    assert list(merge(intervals)) == [[2,23],[25,30]]

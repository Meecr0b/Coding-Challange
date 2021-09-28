#! /usr/bin/env python

from CodingChallenge.merge import merge

intervals = [[25,30],[2,19],[14, 23],[4,8]]

print("Intervals: %s\nMerged Intervals: %s" % (intervals, list(merge(intervals))))

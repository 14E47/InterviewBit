# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        def merge(intervals):
            intervals.sort(key=lambda x: x.start)
            merged = []
            for i in intervals:
                if len(merged) == 0:
                    merged.append(i)
                else:
                    prev = merged[-1]
                    if i.start > prev.end:
                        merged.append(i)
                    else:
                        merged[-1] = Interval(min(prev.start, i.start), max(prev.end, i.end))
            return merged

        ni_low = min(new_interval.start, new_interval.end)
        ni_high = max(new_interval.start, new_interval.end)
        intervals.append(Interval(ni_low, ni_high))
        res = merge(intervals)

        return res








A = [(1,3),(6,9)]
B = (2,5)
A = [(1,2),(3,5),(6,7),(8,10),(12,16)]
B = (4,9)
# A = [ (1, 2), (3, 6) ]
# B = (10, 8)
c = Solution().insert(A, B)
print(c)
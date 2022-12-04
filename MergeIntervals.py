# I have to say, this is not done intuitively. I had to look up pseudocode to come up with this.
# While my previous submissions for this problem were operational, they were inefficient.
# Most of my previous submissions were done in hopes of optimizing the algorithm by tweaking some parts.
class Solution:
    def merge(self, intervals):
        result = []
        intervals.sort()

        result.append(intervals[0])
        for interval in intervals[1:]:
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result

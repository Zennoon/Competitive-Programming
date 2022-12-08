class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = 0
        setNums = set(nums)
        for num in setNums:
            if nums.count(num) == 1:
                continue
            for c in range(nums.count(num)):
                counter += c
        return counter

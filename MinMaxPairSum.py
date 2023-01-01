class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sums = 0
        nums.sort()
        for index in range(len(nums) // 2):
            sums = max(sums, (nums[index] + nums[len(nums) - index - 1]))
        return sums

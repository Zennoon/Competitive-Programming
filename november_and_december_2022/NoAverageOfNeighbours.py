#Done using the shuffle function

import random
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        while self.averageExists(nums):
            random.shuffle(nums)
        return nums
    def averageExists(self, arr):
        for index in range(1, len(arr) - 1):
            if (arr[index + 1] + arr[index - 1]) / 2 == arr[index]:
                return True

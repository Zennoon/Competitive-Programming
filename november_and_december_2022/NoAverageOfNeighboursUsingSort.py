#Uses Sorting
#I have implemented another algorithm that uses the random.shuffle function
#It can be found in this same repository
class Solution:
    def averageExists(self, arr):
        for i in range(1, len(arr) - 1):
            if (arr[i - 1] + arr[i + 1]) / 2 == arr[i]:
                return True
        return False
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        while self.averageExists(nums):
            for index in range(1, len(nums) - 1):
                if (nums[index - 1] + nums[index + 1]) / 2 == nums[index]:
                    nums[index - 1], nums[index] = nums[index], nums[index - 1]
        return nums

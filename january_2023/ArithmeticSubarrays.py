# My first thought when I understood this problem was that I needed to divide the workload into two functions to make things less complicated.

# The two functions will have these purposes:
# One function to extract the queried list elements and the other one to determine if it is arithmetic.



# Code

class Solution:
    def checkArithmetic(self, nums):
        nums.sort()
        diff = nums[1] - nums[0]
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] != diff:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for index in range(len(l)):
            answer.append(self.checkArithmetic(nums[l[index]:r[index] + 1]))
        return answer



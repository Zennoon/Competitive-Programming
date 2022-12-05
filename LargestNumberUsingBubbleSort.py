class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for index1 in range(len(nums)):
            for index2 in range(0, len(nums) - 1 - index1):
                if nums[index2] + nums[index2 + 1] < nums[index2 + 1] + nums[index2]:
                    temp = nums[index2]
                    nums[index2] = nums[index2 + 1]
                    nums[index2 + 1] = temp

        string = ""
        for index in range(len(nums)):
            string += nums[index]
        return str(int(string))
        

    

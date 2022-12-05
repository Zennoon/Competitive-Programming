import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(self.compare_two_options))
        string = ""
        for num in nums:
            string += num
        return str(int(string))

    def compare_two_options(self, num1, num2):
        return -1 if num1 + num2 > num2 + num1 else 1

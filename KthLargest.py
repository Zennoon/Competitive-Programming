class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=functools.cmp_to_key(self.compare))
        return nums[k - 1]
    def compare(self, num1, num2):
        if int(num1) > int(num2):
            return -1
        return 1

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diff = {}
        counter = 0
        for num in nums:
            if num in diff and diff[num] > 0:
                counter += 1
                diff[num] -= 1
            else:
                if k - num in diff:
                    diff[k - num] += 1
                else:
                    diff[k - num] = 1
        return counter


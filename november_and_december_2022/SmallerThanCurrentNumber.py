class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        returnList = []
        for num in nums:
            counter = 0
            for otherNums in nums:
                if num > otherNums:
                    counter += 1
            returnList.append(counter)
        return returnList
        

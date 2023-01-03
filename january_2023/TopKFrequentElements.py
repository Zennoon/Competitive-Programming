class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for index in range(len(nums)):
            if nums[index] not in freq:
                freq[nums[index]] = 1
            else:
                freq[nums[index]] += 1
        sortd = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        result = []
        counter = 0
        for fr in sortd:
            result.append(fr)
            counter += 1
            if counter == k:
                break
        return result

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        areas = []
        while i != j:
            area = min(height[i], height[j]) * (j - i)
            areas.append(area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max(areas)

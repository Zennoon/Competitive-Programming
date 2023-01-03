# Using the range function with its step attribute to solve this problem

# First I used list item substitution (substituting every third item for the last value in the descendingly ordered list) 
# to solve it which was operational but proved to be inefficient. So I observed the pattern which I recommend you to do 
# as well and found out that this formula is effective

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        answer = 0
        for index in range(1, len(piles) - len(piles) // 3, 2):
            answer += piles[index]
        return answer
```

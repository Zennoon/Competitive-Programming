class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            num = i + 1
            if (num % 3 == 0):
                if (num % 5 == 0):
                    answer.append("FizzBuzz")
                else:
                    answer.append("Fizz")
            elif (num % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(num))
        return answer
        

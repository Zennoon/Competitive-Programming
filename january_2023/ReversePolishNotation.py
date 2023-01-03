import math
class Stack():
    def __init__(self):
        self.stack = []
        self.size_of_stack = 0

    def push_to_top(self, value):
        self.stack.append(value)
        self.size_of_stack += 1
    def pop_from_top(self):
        temp = self.stack[self.size_of_stack - 1]
        self.stack = self.stack[:-1]
        self.size_of_stack -= 1
        return temp
    def peek_from_top(self):
        temp = self.stack[self.size_of_stack - 1]
        return temp

class Solution:
    def evalRPN(self, tokens):
        container = Stack()
        for char in tokens:
            if char in ["+", "-", "*", "/"]:
                c1 = container.pop_from_top()
                c2 = container.pop_from_top()
                exp = c2 + char + c1
                calc = eval(exp)
                container.push_to_top(str(math.trunc(calc)))
            else:
                container.push_to_top(char)
        return int(container.peek_from_top())
      
   
#sol = Solution()
#tokens = ["1", "2", "+", "3", "*"]

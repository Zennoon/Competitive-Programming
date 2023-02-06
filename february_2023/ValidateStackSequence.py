class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.stack = self.stack[:self.size - 1]
        self.size -= 1

    def top(self):
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = Stack()
        for num in pushed:
            stack.push(num)
            while len(popped) != 0 and not stack.is_empty() and popped[0] == stack.top():
                stack.pop()
                popped = popped[1:]
        return len(popped) == 0

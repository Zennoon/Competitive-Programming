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

    def peek(self):
        return self.stack[self.size - 1]

    def isEmpty(self):
        return self.size == 0


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = Stack()
        for char in s:
            if char == ")":
                temp = ""
                while stack.peek() != "(":
                    temp += stack.peek()
                    stack.pop()
                stack.pop()
                for charc in temp:
                    stack.push(charc)
            else:
                stack.push(char)
        result = []
        while not stack.isEmpty():
            result.insert(0, stack.peek())
            stack.pop()
        return "".join(chr for chr in result)

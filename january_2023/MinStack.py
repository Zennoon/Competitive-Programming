class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.temp = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1
        self.temp.append(val)
        self.temp.sort()

    def pop(self) -> None:
        self.temp.remove(self.top())
        self.stack = self.stack[:self.size - 1]
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.temp[0]

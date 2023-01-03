class MyQueue(object):

    def __init__(self):
        self.queue = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.push_to_top(x)

    def pop(self):
        """
        :rtype: int
        """
        temp = Stack()
        while not self.queue.is_empty():
            temp.push_to_top(self.queue.pop_from_top())
        temp_num = temp.pop_from_top()
        while not temp.is_empty():
            self.queue.push_to_top(temp.pop_from_top())
        return temp_num

    def peek(self):
        """
        :rtype: int
        """
        temp = Stack()
        while not self.queue.is_empty():
            temp.push_to_top(self.queue.pop_from_top())
        temp_num = temp.peek_from_top()
        while not temp.is_empty():
            self.queue.push_to_top(temp.pop_from_top())
        return temp_num

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.is_empty()
class Stack():
    def __init__(self):
        self.stack = []
        self.size_of_stack = 0

    def push_to_top(self, value):
        self.stack.append(value)
        self.size_of_stack += 1
    def pop_from_top(self):
        if self.size() == 0:
            return "UnderFlow"
        temp = self.stack[self.size_of_stack - 1]
        self.stack = self.stack[:-1]
        self.size_of_stack -= 1
        return temp
    def peek_from_top(self):
        temp = self.stack[self.size_of_stack - 1]
        return temp
    def size(self):
        return self.size_of_stack
    def is_empty(self):
        return self.size() == 0

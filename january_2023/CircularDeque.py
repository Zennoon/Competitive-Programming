class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.size = 0
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.queue.insert(0, value)
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue = self.queue[1:]
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue = self.queue[:self.size - 1]
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.size - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.maxSize

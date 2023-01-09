import collections
import heapq


class MyCircularDeque:

    def __init__(self, k):
        self.queue = []
        self.size = 0
        self.maxSize = k

    def insertFront(self, value):
        if not self.isFull():
            self.queue.insert(0, value)
            self.size += 1
            return True
        return False

    def insertLast(self, value):
        if not self.isFull():
            self.queue.append(value)
            self.size += 1
            return True
        return False

    def deleteFront(self):
        if not self.isEmpty():
            self.queue = self.queue[1:]
            self.size -= 1
            return True
        return False

    def deleteLast(self):
        if not self.isEmpty():
            self.queue = self.queue[:self.size - 1]
            self.size -= 1
            return True
        return False

    def getFront(self):
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.size - 1]
        return -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        maxHeap = [-1 * count for count in counter.values()]
        heapq.heapify(maxHeap)
        time = 0
        k = len(tasks)
        queue = MyCircularDeque(k)
        while maxHeap or not queue.isEmpty():
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    queue.insertLast([cnt, time + n])

            if (not queue.isEmpty()) and queue.getFront()[1] == time:
                cnt = queue.getFront()[0]
                queue.deleteFront()
                heapq.heappush(maxHeap, cnt)
        return time

from collections import deque


class MyCircularDeque:
    def __init__(self, k: int):
       self.deque = deque(maxlen=k) 

    def insertFront(self, value: int) -> bool:
        return len(self.deque) < self.deque.maxlen and (self.deque.appendleft(value) or True)      

    def insertLast(self, value: int) -> bool:
        return len(self.deque) < self.deque.maxlen and (self.deque.append(value) or True)

    def deleteFront(self) -> bool:   
        return self.deque and (self.deque.popleft() or True)

    def deleteLast(self) -> bool:
        return self.deque and (self.deque.pop() or True)

    def getFront(self) -> int:    
        return not self.deque and -1 or self.deque[0]

    def getRear(self) -> int:
        return not self.deque and -1 or self.deque[-1]

    def isEmpty(self) -> bool:
        return not self.deque

    def isFull(self) -> bool:
        return len(self.deque) == self.deque.maxlen


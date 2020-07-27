from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque

class Stack1:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
class Queue1:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push('dog')
    s.push(True)
    e = Queue()
    e.enqueue(1)
    e.enqueue('dog')
    e.enqueue(3)

    print(e.dequeue())
    print(e.isEmpty())
    print(e.size())

    print(s.pop())
    print(s.size())
    print(s.peek())
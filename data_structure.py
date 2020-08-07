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

# UnorderedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, node_data):
        self.next = node_data

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

if __name__ == '__main__':
    # s = Stack()
    # s.push(4)
    # s.push('dog')
    # s.push(True)
    # e = Queue()
    # e.enqueue(1)
    # e.enqueue('dog')
    # e.enqueue(3)
    #
    # print(e.dequeue())
    # print(e.isEmpty())
    # print(e.size())
    #
    # print(s.pop())
    # print(s.size())
    # print(s.peek(),'\n')

    temp = Node(16)
    print(temp.get_data())
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(97)
    print(mylist.head.get_data())
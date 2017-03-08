#queue implementation using python
class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def enqueue(self,v):
        self.items.append(v)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        print (len(self.items)==0)

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[0]

a=Queue()
a.isEmpty()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.isEmpty()
print(a)
print(a.size())
print(a.top())

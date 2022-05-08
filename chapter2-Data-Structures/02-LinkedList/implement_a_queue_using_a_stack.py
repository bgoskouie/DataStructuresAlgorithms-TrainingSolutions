# Build a Queue From Stacks
# In this exercise we are going to create a queue with just stacks.

# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.stack = Stack()
        # Code here
        
    def size(self):
        return self.stack.size()    
        # Code here
        
    def enqueue(self,item):
        self.stack.push(item)
        # Code here
        
    def dequeue(self):
        temp = Stack()
        value = self.stack.pop()
        while value is not None:
            temp.push(value)
            value = self.stack.pop()
        ret = temp.pop()
        self.stack = Stack()
        value = temp.pop()
        while value is not None:
            self.stack.push(value)
            value = temp.pop()
        return ret
        # Code here


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
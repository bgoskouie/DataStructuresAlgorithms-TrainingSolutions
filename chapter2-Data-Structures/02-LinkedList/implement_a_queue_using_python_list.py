# Functionality
# Once implemented, our queue will need to have the following functionality:

# enqueue - adds data to the back of the queue
# dequeue - removes data from the front of the queue
# front - returns the element at the front of the queue
# size - returns the number of elements present in the queue
# is_empty - returns True if there are no elements in the queue, and False otherwise
# _handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
# Also, if the queue is empty, dequeue and front operations should return None.

# 1. Create the queue class and its __init__ method
# Now give it a try for yourself. In the cell below:

# Define a class named Queue and add the __init__ method
# Initialize the arr attribute with an array containing 10 elements, like this: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Initialize the next_index attribute
# Initialize the front_index attribute
# Initialize the queue_size attribute

# 2. Add the enqueue method
# In the cell below, add the code for the enqueue method.

# The method should:

# Take a value as input and assign this value to the next free slot in the array
# Increment queue_size
# Increment next_index (this is where you'll need to use the modulo operator %)
# If the front index is -1 (because the queue was empty), it should set the front index to 0

# 3. Add the size, is_empty, and front methods
# Just like with stacks, we need methods to keep track of the size of the queue and whether it is empty. We can also add a front method that returns the value of the front element.

# Add a size method that returns the current size of the queue
# Add an is_empty method that returns True if the queue is empty and False otherwise
# Add a front method that returns the value for the front element (whatever item is located at the front_index position). If the queue is empty, the front method should return None.

# 4. Add the dequeue method
# In the cell below, see if you can add the deqeueue method.

# Here's what it should do:

# If the queue is empty, reset the front_index and next_index and then simply return None. Otherwise...
# Get the value from the front of the queue and store this in a local variable (to return later)
# Shift the head over so that it refers to the next index
# Update the queue_size attribute
# Return the value that was dequeued

# 5. Add the _handle_queue_capacity_full method
#First, define the _handle_queue_capacity_full method:
#
#Define an old_arr variable and assign the the current (full) array so that we have a copy of it
#Create a new (larger) array and assign it to arr.
#Iterate over the values in the old array and copy them to the new array. Remember that you'll need two for loops for this.
#Then, in the enqueue method:
#
#Add a conditional to check if the queue is full; if it is, call _handle_queue_capacity_full

class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # TODO: Check if the queue is full; if it is, call the _handle_queue_capacity_full method
        if self.next_index == self.front_index:
            self._handle_queue_capacity_full()
        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        self.old_arr = [0] * len(self.arr)
        for idx, item in enumerate(self.arr):
            self.old_arr[idx] = self.arr[idx]
        self.arr = [0] * 2 * len(self.old_arr)
        val = self.dequeue()
        idx = 0
        while val is not None:
            self.arr[idx] = val
            idx += 1
            val = self.dequeue()
        self.front_index = 0
        self.next_index = idx


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
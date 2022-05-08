# Nested Linked Lists:

# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList:
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        # Create a temporary Node object
        node = self.head
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            #print(node.value)
            node = node.next
        return out

ll1 = LinkedList(Node(1))
# ll1.append(Node(2)), ll1.append(Node(30)), ll1.append(Node(4)), ll1.append(Node(5)), ll1.append(Node(0))
ll1.append(2), ll1.append(30), ll1.append(4), ll1.append(5), ll1.append(0)
print(ll1.to_list())

ll2 = LinkedList(Node(1))
# ll2.append(Node(7)), ll2.append(Node(3)), ll2.append(Node(4)), ll2.append(Node(5)), ll2.append(Node(0))
ll2.append(7), ll2.append(3), ll2.append(4), ll2.append(5), ll2.append(0)
print(ll2.to_list())


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head # 1,2,30,4,5,0
    list2_elt = list2.head # 1,7,3,4,5,0
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is not None and isinstance(list1_elt.value, Node):
            a = 0
        if list2_elt is not None and isinstance(list2_elt.value, Node):
            a = 0
        if list1_elt is None:
            merged.append(list2_elt.value)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt.value)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt.value)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt.value)
            list2_elt = list2_elt.next
    return merged

    # My solutoion:
    # l1 = list1.to_list()
    # l2 = list2.to_list()
    # lst = sorted(l1 + l2)
    # #print(lst)
    # ll = LinkedList(None)
    # for item in lst:
    #     ll.append(item)
    # return ll

ll3 = merge(ll1 , ll2)
print(ll3.to_list())

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value , self._flatten(node.next))

    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        return self._flatten(self.head)


def testing():
    # First Test scenario
    ''' Create a simple LinkedList'''
    linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
    linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here 
    linked_list.append(5)

    ''' Create another simple LinkedList'''
    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    ''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
    nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
    nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here

    # Solution:
    solution = nested_linked_list.flatten() # <-- returns A LinkedList object

    expected_list = [1,2,3,4,5] # <-- Python list

    # Convert the "solution" into a Python list and compare with another Python list
    assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
if __name__ == "__main__":
    a = 0
    testing()
    a = 0

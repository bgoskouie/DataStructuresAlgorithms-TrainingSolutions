class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
parameter: - head of the given linked list
return: - head of the updated list with all even elements placed after odd elements
"""
#--------------------------------------------------#
'''
The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
For this purpose, we will use four helper references, that denotes starting and 
current ending of EVEN and ODD sub-list respectively. 

1. For each Node in the LinkedList, check if its data is even/odd. 
Change the "next" reference (pointer) of each Node, based on the following rules:
 - First even valued Node will be referenced by head of EVEN sub-list
 - Subsequent even valued Node will be appended to the tail of EVEN sub-list

 - First odd valued Node will be referenced by head of ODD sub-list
 - Subsequent odd valued Node will be appended to the tail of ODD sub-list
 
2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
'''
#--------------------------------------------------#
def even_after_odd(head):
    
    if head is None:
        return head
    
    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
    even_head = None                    
    even_tail = None
    
    ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
    odd_head = None
    odd_tail = None
    
    current = head                  # <-- "current" represents the current Node. 
    
    # Loop untill there are Nodes available in the LinkedList
    while current:                  # <-- "current" will be updated at the end of each iteration
        
        next_node = current.next    # <-- "next_node" represents the next Node w.r.t. the current Node
        
        if current.data % 2 == 0:   # <-- current Node is even
            
            # Below 
            if even_head is None:   # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = current     # `even_head` will now point where `current` is already pointing
                even_tail = even_head     
            else:                   # <-- Append the current even node to the tail of EVEN sub-list 
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:    # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = current
                odd_tail = odd_head
            else:                   # <-- Append the current odd node to the tail of ODD sub-list 
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node         # <-- Update "head" Node, for next iteration
    
    if odd_head is None:            # <-- Special case, when there are no odd Nodes 
        return even_head

    odd_tail.next = even_head       # <-- Append the EVEN sub-list to the tail of ODD sub-list
    
    return odd_head

#my solution
def even_after_odd_my_solution(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    lastodd = None
    node = head
    # set node to first even node
    while node is not None and node.data % 2 == 1:
        lastodd = node
        node = node.next
    if node is None:  # all odd in list
        return head
    print(f"STARTING WITH:")
    if lastodd is not None:
        print(f"lastodd.data={lastodd.data}")
    if node is not None:
        print(f"node.data={node.data}")
    if node.next is not None:
        print(f"node.next.data={node.next.data}")  #, node.next={node.next}")    
    while node.next is not None:
        #print(f"new step: last={last}, node={node}, node.next={node.next}")
        if lastodd is not None:
            print(f"NEW STEP: lastodd.data={lastodd.data}, node.data={node.data}, node.next.data={node.next.data}")  #, node.next={node.next}")
        else:
            print(f"NEW STEP: node.data={node.data}, node.next.data={node.next.data}")  #, node.next={node.next}")
        print_linked_list(head)
        #-------------------------
        if node.next.data % 2 == 1:  # odd
            thisn = node.next
            node.next= node.next.next
            if lastodd is None:
                thisn.next = head
                head = thisn
            else:
                thisn.next = lastodd.next
                lastodd.next = thisn
            lastodd = thisn
        else:
            node = node.next
        #-------------------------
        if lastodd is not None:
            print(f"lastodd.data={lastodd.data}")
        if node is not None:
            print(f"node.data={node.data}")
        if node.next is not None:
            print(f"node.next.data={node.next.data}")  #, node.next={node.next}")
        print_linked_list(head)
    return head

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [20, 1, 2, 4, 6, 8]
solution = [1, 20, 2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)
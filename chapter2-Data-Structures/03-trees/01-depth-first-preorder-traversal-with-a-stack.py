# Traverse a tree (depth first search)¶
# Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.

# Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

# Depth first search has 3 types: pre-order, in-order, and post-order.

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# apple, banana, dates, cherry

# Stack
# Notice how we're retracing our steps. It's like we are hiking on a trail, and trying to retrace our steps on the way back. This is an indication that we should use a stack.

# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

'''
# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)

visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)


print(f"""
visit_order {visit_order} 
stack:
{stack}
""")

'''

def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    stack.push(node)
    node = stack.top()
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit): 
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
        """)
        count +=1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node)
            # using top() is redundant, but added for clarity
            node = stack.top() 
            visit_order.append(node.get_value())
            
        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None
        
        
    return visit_order


# pre_order_with_stack_buggy(tree)

# pre-order traversal using a stack, tracking state
# Here's how we implement DFS with a stack, where we also track whether we've already visited the left or right child of the node.

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order

# pre_order_with_stack(tree, debug_mode=True)


def pre_order(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    pre_order_recurrsion(node, state, visit_order, stack, count)

def pre_order_recurrsion(node, state, visit_order, stack, count):
    debug_mode = True
    if node is None:
        return visit_order
    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
        """)
        count +=1

    if node.has_left_child() and not state.get_visited_left():
        state.set_visited_left()
        node = node.get_left_child()
        visit_order.append(node.get_value())
        state = State(node)
        stack.push(state)
    elif node.has_right_child() and not state.get_visited_right():
        state.set_visited_right()
        node = node.get_right_child()
        visit_order.append(node.get_value())
        state = State(node)
    else:
        stack.pop()
        if not stack.is_empty():
            state = stack.top()
            node = state.get_node()
        else:
            node = None
    pre_order_recurrsion(node, state, visit_order, stack, count)


# pre_order(tree)
a = 0

# https://youtu.be/um10vCBP2FE
# https://youtu.be/dN_F1xK6qTE
# https://youtu.be/4ruolshjhq0


def pre_order_soln(tree):
    visit_order = list()
    node = tree.get_root()
    def traverse(node):
        if node:
            # visit
            visit_order.append(node.get_value())
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())
    traverse(node)
    return visit_order

visits = pre_order_soln(tree)
print(visits)


def in_order_soln(tree):
    visit_order = list()
    node = tree.get_root()
    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())
            # visit
            visit_order.append(node.get_value())
            # traverse right
            traverse(node.get_right_child())
    traverse(node)
    return visit_order

visits = in_order_soln(tree)
print(visits)


def post_order_soln(tree):
    visit_order = list()
    node = tree.get_root()
    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())
            # visit
            visit_order.append(node.get_value())
    traverse(node)
    return visit_order

visits = post_order_soln(tree)
print(visits)

a = 0

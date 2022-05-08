


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

from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Tree():
    def __init__(self):
        self.root = None

    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self,new_value):
        node = self.root
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
            return

        while True:
            comp = self.compare(node, new_node)
            if comp == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            if comp == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
            if comp == 0:
                if node.has_right_child():
                    right = node.get_right_child()
                    node.set_right_child(new_node)
                    new_node.set_right_child(right)
                else:
                    node.set_right_child = new_node
                break

    """
    define insert here (can use recursion)
    try one or both ways
    """
    def insert_with_recursion(self,new_value):
        node = self.root
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
            return
        inserted = False
        self.recur(node, new_node, inserted)

    def recur(self, node, new_node, inserted):
        comp = self.compare(node, new_node)
        if comp == -1:
            if node.has_left_child():
                node = node.get_left_child()
            else:
                node.set_left_child(new_node)
                inserted = True
        if comp == 1:
            if node.has_right_child():
                node = node.get_right_child()
            else:
                node.set_right_child(new_node)
                inserted = True
        if comp == 0:
            if node.has_right_child():
                right = node.get_right_child()
                node.set_right_child(new_node)
                new_node.set_right_child(right)
            else:
                node.set_right_child(new_node)
            inserted = True
        if not inserted:
            self.recur(node, new_node, inserted)


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level


        return s



tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)



#########################################################
###########---SEARCH---##################################
class Tree():
    def __init__(self):
        self.root = None

    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return

        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping

    """
    implement search
    """
    def search(self,value):
        node = self.get_root()
        return self.srch(value, node)

    def srch(self, value, node):
        if node is None:
            return False
        if node.get_value() == value:
            return True
        if value > node.get_value():
            return self.srch(value, node.get_right_child())
        elif value < node.get_value():
            return self.srch(value, node.get_left_child())

    def search_sol(self,value):
        node = self.get_root()
        s_node = Node(value)
        while True:
            comp = self.compare(node,s_node)
            if comp == 0:
                return True
            elif comp == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            elif comp == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
            else:
                raise Exception("incorrect comp output")

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s

tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)


# Bonus I didn't do:
# Delete a node from the tree
# https://youtu.be/fJlWvaqqeZg

# # to delete:
# 1. if it is a leaf node, just find the parent and set the associated parent's arm to None
# 2. if it is a node that has one child, then find its parent and set the associted parent's arm to the child (connect grand-pa to grand-child)
# 3. if it s a node that has two children, then
#     a. find which one of parent's arms has connected to it.
#         - if right then we have to replace this one with the smallest node greater than itself. therefore,
#             we should keep looking for nodes on the left child of the "to be deleted" node
#             so we keep going left left left all the way to where left is None and take the latest left
#             put the value of the latest left to the to-be-deleted node
#         - if left, then the to-be-deleted node is smaller than its parent, and we should replace it with
#             the node whose value is the largest than the to-be-deleted-node but smaller than the parent.
#             Thus we keep going right right right on the to-be-deleted node's arms all the way to right = None
#             and take the latest right and put it in place of the to-be-deleted node.
#         Don't forget to delete the node that you just moved. That node definitely has one child! so use rule #2
"""
Heap sorting mechanism:
    Look at the gif file for the agirthm!
    We can use a max heap tree to sort elements
Max heap bin tree:
    a tree in which the root is the largest element
Upheapify:
    Given a node in the bin tree
    you want to upheapify so the max goes up
    compare node value with its parent and swap if node is larger.
    Redo all the way to a point where parent is larger or reaching root.

Downheapify:
    Given a node (usually root) in the bin tree, we will down-heapify within only one route
    of the tree all the way to the bottom.
    Usually done on root.
    compare node value with both its childs' values. and swap te node's value with its child
    if the child is larger than the node. If both children are larger, swap with the larger child.
    Do this all the way to the point where both children are smaller than the node (parent)

Max Heap Sorting Mechanism:
    Given an array
    1- While creating the bin tree, do an upheapify on all nodes
    2- After done with creating the bin tree, create an empty array for sorted elements.
    3- Set last value of the array as tree root, since tree root is the largest element.
    4- Replace tree root with last element of the tree.
    5- Remove last element of the tree (it was the tree root from step 4)
    6- Do a downheapify on the new root (used to be last element of array)
    7- Back to step 3 all the way to when sorted array is full and bin tree is empty

"""

import copy

def heapsort(arr):
    # for i in range(len(arr)):
    heapify(arr, len(arr), 0)

def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node: ignore heapifying the last element of "arr". The n-i to end elements of arr are already sorted!
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    if i >= n:
        return
    root = convert_arr_to_bin_heap_tree(arr[:n-i], upheapify_flag=True)
    # print(root)
    arr[n - i - 1] = root.value
    last_node = root.getLastNode()
    root.swap_value(last_node)
    # print(root)
    root.popLast()  # Deleting the last node that was root that was the largest
    # print(root)
    root.downheapify()
    # print(root)
    convert_bin_tree_to_arr(arr, root)
    # print(root)
    i += 1
    heapify(arr, n, i)
    return arr

def convert_bin_tree_to_arr(arr_in, root):
    # arr = list()
    node = root
    i = 0
    while node is not None:
        if len(arr_in) > i:
            arr_in[i] = node.value
        else:
            arr_in.append(node.value)
        node = node.next()
        i += 1
    # return arr

def convert_arr_to_bin_heap_tree(arr, upheapify_flag=False):
    if len(arr) == 0:
        return None
    root = Node(arr[0])
    if len(arr) == 1:
        return root
    # add_node_to_tree_recur(arr, 1, root, where='left')
    root = add_node_to_tree_recur(arr, 0, None, where='left', upheapify_flag=upheapify_flag)
    return root  # [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]


def add_node_to_tree_recur(arr, index, parent, where='left', upheapify_flag=False):
    if index >= len(arr):
        return parent
    node = Node(arr[index])
    node.setParent(parent, where)
    if upheapify_flag:
        node.upheapify()
    _ = add_node_to_tree_recur(arr, 2 * index + 1, node, where='left', upheapify_flag=upheapify_flag)
    _ = add_node_to_tree_recur(arr, 2 * index + 2, node, where='right', upheapify_flag=upheapify_flag)
    return node
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.cleft = None
        self.cright = None

    def getParent(self):
        return self.parent

    def getCRight(self):
        return self.cright

    def getCLeft(self):
        return self.cleft

    def isaLeftChild(self):
        if self is not None and self.parent is not None and self.parent.cleft == self:
            return True
        return False

    def isaRightChild(self):
        if self is not None and self.parent is not None and self.parent.cright == self:
            return True
        return False

    def setParent(self, parent, where='left'):
        self.parent = parent
        if parent is None:
            return
        if where == 'left':
            parent.setCLeft(self)
        else:
            parent.setCRight(self)

    def setCLeft(self, cleft):
        self.cleft = cleft

    def setCRight(self, cright):
        self.cright = cright

    def __str__(self):
        out = ''
        def get_char_len(node):
            return abs(node.value//10) + 1

        # node = copy.deepcopy(self)
        node = self
        maxL = 1
        while node is not None:
            maxL = max(maxL, get_char_len(node) + int(node.value < 0))
            node = node.next()
        # space between the printed node values including character lengths:
        s = 3 + maxL
        # node = copy.deepcopy(self)
        node = self
        n = self.getLevelToDown()
        for row in range(n):
            # index of the elements in a row
            # there are (2 ** row) number of elements in a row
            # so index runs from 0 to (2 ** row)
            ind = 0
            # Between every elm in row should have this much space
            space = (2 ** (n - 1 - row)) * s
            # row has 2 ** (row) number of elements, so keep doing next
            # 2 ** (row) number of times for each row
            while ind < (2 ** row):
                if node is None:
                    return out
                v_len = get_char_len(node)
                out += " " * (space - v_len)
                out += str(node.value)
                out += " " * space
                node = node.next()
                ind += 1
            out += "\n"
        return out

    def getLevelToDown(self):
        lvl = 0
        node = copy.deepcopy(self)
        while node is not None:
            lvl += 1
            node = node.cleft
        return lvl

    def next(node):
        '''gets a node from the tree and returns the next element in the same tree row'''
        if node.getParent() is None:
            return node.getCLeft()
        up_cnt = 0
        while node.isaRightChild():
            up_cnt += 1
            node = node.getParent()
        if node.getParent() is None:
            # node is root!
            node = node.getCLeft()
        else:
            node = node.getParent().getCRight()
        for i in range(up_cnt):
            node = node.getCLeft()
        return node

    def getLastNode(self):
        node = self
        last_node = node
        while node is not None:
            last_node = node
            node = node.next()
        return last_node

    def popLast(self):
        node = self.getLastNode()
        if node is not None:
            if node.isaLeftChild():
                node.parent.cleft = None
            elif node.isaRightChild():
                node.parent.cright = None

    def upheapify(self):
        '''starting given node to top, sorts the node all the way to root'''
        if self.parent is not None:
            if self.parent.value < self.value:
                self.swap_value(self.parent)
                self.parent.upheapify()


    def downheapify(self):
        '''starting from a given node down, sorts the node all the way to root'''
        if self is not None:
            if self.cleft is not None and self.cright is not None:
                if self.cleft.value > self.cright.value and self.cleft.value > self.value:
                    # cleft is largest:
                    self.swap_value(self.cleft)
                    self.cleft.downheapify()
                if self.cleft.value < self.cright.value and self.cright.value > self.value:
                    # cright is largest:
                    self.swap_value(self.cright)
                    self.cright.downheapify()
            elif self.cleft is not None and self.cleft.value > self.value:
                self.swap_value(self.cleft)
                self.cleft.downheapify()
            elif self.cright is not None and self.cright.value > self.value:
                self.swap_value(self.cright)
                self.downheapify(self.cright)

    def swap_value(self, node):
        if self is not None and node is not None:
            tmp = node.value
            node.value = self.value
            self.value = tmp




def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
root = convert_arr_to_bin_heap_tree(arr)
print(root)
print(root.next().value)
print(root.cleft.next().value)
print(root.cright.next().value)
print(root.cleft.cleft.next().value)
print(root.cleft.cright.next().value)
print(root.cright.cright.next().value)
print(root.cright.cleft.cleft.next() is None)
arr2 = copy.deepcopy(arr)
convert_bin_tree_to_arr(arr2, root)
print(arr2 == arr)
heapsort(arr)
print(arr)
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)


arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)


arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
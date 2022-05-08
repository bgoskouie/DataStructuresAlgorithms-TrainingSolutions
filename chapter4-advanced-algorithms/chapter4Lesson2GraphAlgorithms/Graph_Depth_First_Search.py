# Graph Depth First Search
# In this exercise, you'll see how to do a depth first search on a graph. To start, let's create a graph class in Python.

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self,new_node):
        self.children.append(new_node)

    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list

    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

    # Babak's way:
    def traverse(self):
        # can use either regular loop over all nodes and a stack data structure:
        # A stack of nodes being traversed - list .append() and .pop() work as LIFO
        # or use a set of all the visited nodes
        visited_nodes = set()
        visited_nodes.add(self.nodes[0])
        return self.traverse_recur(self.nodes[0], visited_nodes)

    def traverse_recur(self, parent, visited_nodes):
        # actions when travese hits the node:
        print(parent.value)
        visited_nodes.add(parent)
        # finding all the edges:
        for node in parent.children:
            # stop if circling back to same visited node:
            if node in visited_nodes:
                continue
            self.traverse_recur(node, visited_nodes)
            # else, the for loop of a child node has ended and we want to continue execution of the for loop of the parent node rather than returning None

#--------------------------------------------------------------------
# Babak's way (with recursion)
def dfs_search_recursion(root_node, search_value):
    visited_nodes = set()
    visited_nodes.add(root_node)
    return dfs_search_recur(root_node, visited_nodes, search_value)

def dfs_search_recur(parent, visited_nodes, search_value):
    # actions when travese hits the node:
    print(parent.value)
    if parent.value == search_value:
        return parent
    visited_nodes.add(parent)
    # finding all the edges:
    for node in parent.children:
        # if node.value == 'S':
        #     a = 0
        # if parent.value == 'R':
        #     print(f"parent=R, node={node.value}")
        #     a = 0
        if node in visited_nodes:
            continue
        # stop if circling back to same visited node:
        out = dfs_search_recur(node, visited_nodes, search_value)
        if out != None:
            return out
    return None

#--------------------------------------------------------------------
# Solution by Udacity  (Babak thinks is wrong)
def dfs_recursion_start(start_node, search_value):
    visited = set()               # Set to keep track of visited nodes.
    return dfs_recursion(start_node, visited, search_value)

# Recursive function
def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        # found = True              # Don't search in other branches, if found = True
        return node
    visited.add(node)
    # found = False
    result = None
    # Conditional recurse on each neighbour
    for child in node.children:
        if (child not in visited):
                result = dfs_recursion(child, visited, search_value)
                # # Once the match is found, no more recurse
                # if found:
                #     break
    return result

#--------------------------------------------------------------------
# SOLUTION (no recursion)
def dfs_search_while(root_node, search_value):
    stack = [root_node]
    visited = set()
    while len(stack) > 0:
        # the difference between stack and visited is that, a node can be added to stack and popped multiple times. stack can grow and shrink.
        # As soon as a node is added to visited it can't be added to stack or visited. visited list always grows.
        current_node = stack.pop()
        visited.add(current_node)
        if current_node.value == search_value:
            return current_node
        for child in current_node.children:
            # If a node hasn't been visited already
            if (child not in visited) and (child not in stack):
                stack.append(child)

#--------------------------------------------------------------------
# Now let's create the graph.
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')
graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

graph1.traverse()
# Implement DFS
# Using what you know about DFS for trees, apply this to graphs. Implement the dfs_search_while to return the GraphNode with the value search_value starting at the root_node.


# Tests
# print("----------------------")
n = dfs_search_while(nodeS, 'A')
# print("----------------------")
assert nodeA == dfs_search_while(nodeS, 'A')
# print("----------------------")
assert nodeS == dfs_search_while(nodeP, 'S')
# print("----------------------")
assert nodeR == dfs_search_while(nodeH, 'R')
# print("----------------------")



# Testing Babak's recursion solution
# print("----------------------")
n = dfs_search_recursion(nodeS, 'A')
print("----------------------")
assert nodeA == dfs_search_recursion(nodeS, 'A')
# print("----------------------")
n = dfs_search_recursion(nodeP, 'S')
assert nodeS == dfs_search_recursion(nodeP, 'S')
# print("----------------------")
assert nodeR == dfs_search_recursion(nodeH, 'R')


# Testing Babak's recursion solution
n = dfs_recursion_start(nodeS, 'A')
print("----------------------")
assert nodeA == dfs_recursion_start(nodeS, 'A')
# print("----------------------")
n = dfs_recursion_start(nodeP, 'S')
assert nodeS == dfs_recursion_start(nodeP, 'S')
# print("----------------------")
assert nodeR == dfs_recursion_start(nodeH, 'R')

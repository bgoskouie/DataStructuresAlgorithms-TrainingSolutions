# Prim’s Algorithm - Connecting Islands

# Connect Islands using Prim’s Algorithm
# A. Problem Statements
# In an ocean, there are n islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling.

# You can assume that there is at least one possible way in which all islands are connected with each other.

# You will be provided with two input parameters:

# num_islands = number of islands

# bridge_config = list of lists. Each inner list will have 3 elements:

#  a. island A
#  b. island B
#  c. cost of bridge connecting both islands
# Each island is represented using a number

# Example:

# num_islands = 4
# bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# Input parameters explanation:

# 1. Number of islands = 4
# 2. Island 1 and 2 are connected via a bridge with cost = 1
#    Island 2 and 3 are connected via a bridge with cost = 4
#    Island 1 and 4 are connected via a bridge with cost = 3
#    Island 4 and 3 are connected via a bridge with cost = 2
#    Island 1 and 3 are connected via a bridge with cost = 10
# In this example if we are connecting bridges like this...

# between 1 and 2 with cost = 1
# between 1 and 4 with cost = 3
# between 4 and 3 with cost = 2
# ...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.

# B. Hint: Use a Priority Queue or Min-Heap
# In addition to using a graph, you may want to use a custom priority queue for solving this problem. If you do not want to create a custom priority queue, you can use Python's inbuilt heapq implementation.

# Using the heapq module, you can convert an existing list of items into a min-heap. The following two functionalities can be very handy for this problem:

# heappush(heap, item) — add item to the heap
# heappop(heap) — remove the smallest item from the heap
# Let's look at the above methods in action. We start by creating a list of integers.

# heappush -----------------------------------------
import heapq
# initialize an empty list
minHeap = list()
# insert 5 into heap
heapq.heappush(minHeap, 6)
# insert 6 into heap
heapq.heappush(minHeap, 6)
# insert 2 into heap
heapq.heappush(minHeap, 2)
# insert 1 into heap
heapq.heappush(minHeap, 1)
# insert 9 into heap
heapq.heappush(minHeap, 9)
print("After pushing, heap looks like: {}".format(minHeap))
# After pushing, heap looks like: [1, 2, 6, 6, 9]

# heappop -----------------------------------------
# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)
print("Smallest element in the original list was: {}".format(smallest))
print("After popping, heap looks like: {}".format(minHeap))
# Smallest element in the original list was: 1
# After popping, heap looks like: [2, 6, 6, 9]
# heappush and heappop for items with multiple entries
# Note: If you insert a tuple inside the heap, the element at 0th index of the tuple is used for comparision

minHeap = list()
heapq.heappush(minHeap, (0, 1))
heapq.heappush(minHeap, (-1, 5))
heapq.heappush(minHeap, (2, 0))
heapq.heappush(minHeap, (5, -1))
print("After pushing, now heap looks like: {}".format(minHeap))

# After pushing, now heap looks like: [(-1, 5), (0, 1), (2, 0), (5, -1)]
# pop and return smallest element from the heap

smallest = heapq.heappop(minHeap)
print("Smallest element in the original list was: {}".format(smallest))
print("After popping, heap looks like: {}".format(minHeap))

# Smallest element in the original list was: (-1, 5)
# After popping, heap looks like: [(0, 1), (5, -1), (2, 0)]
# Now that you know about heapq, you can use it to solve the given problem. You are also free to create your own implementatin of Priority Queues.

# C. The Idea, based on Prim’s Algorithm:
# Our objective is to find the minimum total_cost to visit all the islands. We will start with any one island, and follow a Greedy approach.
# Step 1 - Create a Graph

# Create a graph with given number of islands, and the cost between each pair of islands. A graph can be represented as a adjacency_matrix, which is a list of lists. For example, given:
# num_islands = 4
# bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

# The graph would look like:
# graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
# where, a sublist at 𝑖𝑡ℎ index represents the adjacency_list of 𝑖𝑡ℎ island. A tuple within a sublist is (neighbor, edge_cost).
# Step 2 - Traverse the graph in a Greedy way.
# Create a blank minHeap, and push any one island (vertex) into it.
# While there are elements remaining in the minHeap, do the following:

# Pop out an island having smallest edge_cost, and reduce the heap size. You can use heapq.heappop() for this purpose.
# If the current island has not been visited before, add the edge_cost to the total_cost. You can use a list of booleans to keep track of the visited islands.
# Find out all the neighbours of the current island from the given graph. Push each neighbour of the current island into the minHeap. You can use heapq.heappush() for this purpose.
# Mark current island as visited tuple in the adjacency_list of the
# When we have popped out all the elements from the minHeap, we will have the minimum total_cost to visit all the islands.

# D. Exercise - Write the function definition here
# Write code in the following function to find and return the minimum cost required to travel all islands via bridges.

import copy
class Graph:
    def __init__(self, num_nodes, edge_configs):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[]] * (num_nodes + 1)
        for edge in edge_configs:
            n1 = edge[0]
            n2 = edge[1]
            cost = edge[2]
            if n1 > num_nodes or n2 > num_nodes or n1 == n2:
                raise Exception("wrong input")
            am_n1 = copy.deepcopy(self.adjacency_matrix[n1])  #[[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
            am_n2 = copy.deepcopy(self.adjacency_matrix[n2])
            am_n1.append((n2, cost))
            am_n2.append((n1, cost))
            self.adjacency_matrix[n1] = am_n1
            self.adjacency_matrix[n2] = am_n2
        a = 0

    def getCostNodePairs(self, index):
        """Gets an index and returns a list of tuples of (cost, node)
        cost should come first cuz heapq minimizes based upon the first index!"""
        if 0 < index < (self.num_nodes + 1):
            return [(cost, node) for node, cost in self.adjacency_matrix[index]]
        else:
            raise Exception(f"index {index} out of range")


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    g = Graph(num_islands, bridge_config)
    minheap = list()
    index = 1
    costNodePairsIndex1 = g.getCostNodePairs(index)
    minheap.extend(costNodePairsIndex1)
    cost = 0
    visited_nodes = set()  # set of visited nodes
    visited_nodes.add(index)

    while len(minheap) > 0:
        popped = heapq.heappop(minheap)
        c = popped[0]
        n = popped[1]
        if n not in visited_nodes:
            # print(f"n={n}, c={c}")
            cost += c
            visited_nodes.add(n)
            cost_node_pars_index = g.getCostNodePairs(n)
            # minheap.extend(cost_node_pars_index)
            for tup in cost_node_pars_index:
                heapq.heappush(minheap, tup)
    return cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
num_islands = 3
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
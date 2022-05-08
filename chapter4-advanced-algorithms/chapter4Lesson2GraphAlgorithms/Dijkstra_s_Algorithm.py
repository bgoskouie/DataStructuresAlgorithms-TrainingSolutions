# Dijkstra's Algorithm
# In the "Greedy Algorithms" lesson, we implemented the Dijkstra's Algorithm
# to find the distance of each node from the given source node.
# In this exercise, you'll implement the same Dijkstra's algorithm
# to find the length of the shortest path between a given pair of nodes,
# but this time we will have a better time complexity.
# First, let's build the graph.

# Graph Representation
# In order to run Dijkstra's Algorithm, we'll need to add distance to each edge.
# We'll use the GraphEdge class below to represent each edge between a pair of nodes.
# You are free to create your own implementation of an undirected graph.

# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance
# The new graph representation should look like this:

# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []
    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))
    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)
class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list
    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)
    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)
# Exercise - Write the function definition here
# Using what you've learned, implement Dijkstra's Algorithm

import sys

#Babak's Solution:
class PriorityQueue:
    """Min heap: when popping, return the smallest element"""
    def __init__(self, nodes_l, default_dist=sys.maxsize):
        self.d = {}
        for node in nodes_l:
            self.d.update({node: default_dist})
    def setNodeDist(self, node, value):
        if node in self.d.keys():
            self.d.update({node: value})
    def getNodeDist(self, node):
        if node in self.d.keys():
            return self.d[node]
    def getNodesList(self):
        return self.d.keys()
    def pop(self):
        # A priority queue must pop the element
        if len(self.d) > 0:
            elm = min(self.d, key=self.d.get)
            dist = self.d[elm]
            self.d.pop(elm)
            return elm, dist
        else:
            return None, None
    def size(self):
        return len(self.d)
    def __str__(self):
        return str(self.d)

#Babak's Solution:
import math
def dijkstra(graph, start_node, end_node):
    pq = PriorityQueue(graph.nodes)
    pq.setNodeDist(start_node, 0)
    while pq.size() > 0:
        # node_min is the closest node to start node that is left in pq.
        # all nodes that are removed from pq were closer.
        node_min, dist = pq.pop()
        if node_min == end_node:
            return dist
        for edge in node_min.edges:
            node = edge.node
            if node not in pq.getNodesList():
                continue
            dist_via_min = edge.distance + dist
            if dist_via_min < pq.getNodeDist(node):
                pq.setNodeDist(node, dist_via_min)



# Udacity solution:
import math   # Need math.inf constant
def dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value 
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity
    distance_dict = {node: math.inf for node in graph.nodes}
    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}
    distance_dict[start_node] = 0
    while distance_dict:
        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)
        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the alreday stored distance, update the distance_dict
        for edge in current_node.edges:
            if edge.node in distance_dict:
                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour
    return shortest_distance[end_node]

# Testing Priority Queue:
q = PriorityQueue([1,2,3,4])
q.setNodeDist(2,22)
print(str(q))
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Test
# Test Case 1:
# Create a graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')
graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# add_edge() function will add an edge between node1 and node2 in both directions
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)
d = dijkstra(graph, node_u, node_y)
# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))
# Test Case 2
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
graph = Graph([node_A, node_B, node_C])

graph.add_edge(node_A, node_B, 5)
graph.add_edge(node_B, node_C, 5)
graph.add_edge(node_A, node_C, 10)

# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))
# Test Case 3
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
node_D = GraphNode('D')
node_E = GraphNode('E')
graph = Graph([node_A, node_B, node_C, node_D, node_E])
graph.add_edge(node_A, node_B, 3)
graph.add_edge(node_A, node_D, 2)
graph.add_edge(node_B, node_D, 4)
graph.add_edge(node_B, node_E, 6)
graph.add_edge(node_B, node_C, 1)
graph.add_edge(node_C, node_E, 2)
graph.add_edge(node_E, node_D, 1)

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))

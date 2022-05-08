# Greedy Technique - Introduction
# A Greedy Technique is the one which picks up the "best" possible solution to a sub-problem available at the moment. Greedy algorithms is the collective name given to algorithms which make use of the Greedy Technique. The step by step process of these algorithms may be different. However, if any algorithm follows the Greedy Technique at each step, it can be called as a Greedy Algorithm.

# Example 1
# As the name suggests, in greedy technique, we get greedy and follow the best possible solution at each step of the algorithm. Consider the following scenario

# The following 4 points - A, B, C, D denote 4 corners of a city. You are standing at A and want to reach D as soon as possible. . However, there are only two ways in which you can do this. You can either go via B or you can go via C.

# Reaching B from A takes 1 min and reaching D from B takes 10 mins.

# Reaching C from A takes 5 min and reaching D from C takes 10 mins.



# Solution using Greedy Approach
# If we follow the greedy technique, we will choose to go via B. If we go to C, it would take 5 mins. However, going to B only takes 1 min. Therefore, while standing at A, going via B seems to be the better solution.

# Thus, in our final solution, we will reach D in 11 minutes if we follow the greedy technique.

# Example 2
# Let's consider the same scenario again but with slight changes. This time, let the time taken to reach D from B be 20 minutes.


# Solution using Greedy Approach
# If we follow the greedy technique again, we will have to go via B because when we are at A going to B seems like a better choice.

# But notice that if we go via B, the total time taken to reach D will be 21 minutes compared to 15 minutes if we go via C. So in this case following the greedy approach does not help us. Rather, it gives us a less efficient solution.

# This is a key point to remember. Greedy Algorithms might not be the most effective at all times. Rather, in most of the cases, greedy solutions tend to have worse efficiency compared to some of the other techniques such as Divide and Conquer, Dynamic Programming etc. However, there are problems where following the greedy approach also results in an efficient - best overall solution.

# Some of the famous greedy algorithms ares:

# Dijkstra's Shortest Path Algorithm
# A* search Algorithm
# Prim's algorithm for Minimal Spanning Tree
# Kruskal's algorithm for Minimal Spanning Tree
# Knapsack Problem
# Travelling Salesman Problem
# We will see implementation of a few these algorithms in the upcoming lessons.

# Takeaways
# In a greedy solution, we go for the best possible choice at each step of the algorithm.

# Because we are not considering future scenarios (and are only concerned with the best choice at each step), a greedy solution might not be the most effective solution for the problem.

# To decide whether or not to use a greedy approach for a particular problem, try to think whether or not the greedy technique will work for all the future steps of the algorithm.

# Dijkstra's Shortest Path Algorithm
# Suppose there is graph having nodes, where each node represents a city. A few pair of nodes are connected to each other, with their distance mentioned on the conneting edge, as shown in the figure below:

# To find the shortest path from a given source to destination node in the example above, a Greedy approach would be - At each current node, keep track of the nearest neighbour. We can determine the path in the reverse order once we have a table of nearest neighbours (optimal previous nodes). For example, C is the optimal previous node for E. This way, the shortest path from A to E would be A --> D --> C --> E, as shown below:

# And, if we wish to print the distance of each node from A, then it would look like:

# Here, the Previous Optimal Node is the "best" node which could lead us to the current node.

# The Problem
# Using Dijkstra's algorithm, find the shortest path to all the nodes starting from a given single source node. You need to print the distance of each node from the given source node. For the example quoted above, the distance of each node from A would be printed as:

# {'A': 0, 'D': 2, 'B': 5, 'E': 4, 'C': 3, 'F': 6}

# The Algorithm
# Create a result dictionary. At the end of the program, result will have the shortest distance (value) for all nodes (key) in the graph. For our example, it will become as {'A': 0, 'B': 5, 'C': 3, 'D': 2, 'F': 6, 'E': 4}

# Start with the source node. Distance from source to source itself is 0.

# The distance to all other nodes from the source is unknown initially, therefore set the initial distance to infinity.

# Create a set unvisited containing nodes that have not been visited. Initially, it will have all nodes of the graph.

# Create a path dictionary that keeps track of the previous node (value) that can lead to the current node (key). At the end of the program, for our example, it will become as {'B': 'A', 'C': 'D', 'D': 'A', 'F': 'C', 'E': 'C'}.

# As long as unvisited is non-empty, repeat the following:
# Find the unvisited node having smallest known distance from the source node.

# For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.

# If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.

# If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.

# Remove the current node from the unvisited set.
# Note - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a O(n^2) time complexity. We will see a better version in the next lesson - "Graph Algorithms" with O(nlogn) time complexity.

# Helper Code
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


''' TO DO: Find the shortest path from the source node to every other node in the given graph '''
import sys

'''Find the shortest path from the source node to every other node in the given graph'''
def dijkstra(graph, source):
    result = {}
    result[source] = 0

    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited:
        min_node = None

        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:

                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        # known distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbours.
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result


# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

print(dijkstra(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}


# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

print(dijkstra(graph, 'A'))        # {'A': 0, 'C': 10, 'B': 5}


# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra(graph, 'A'))       # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
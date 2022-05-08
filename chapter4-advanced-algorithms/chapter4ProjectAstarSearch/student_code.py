import math

def shortest_path(M,start,goal):
    #print("shortest path called-------------------------")
    h = euclidean_distance(M, start, goal)
    frontier = {start: {"f": h, "g": 0, "path": [start]}}
    visited = set()
    visited.add(start)
    return optimum_step(start, M, frontier, visited, goal)


def euclidean_distance(M, node1, node2):
    x1 = M.intersections[node1][0]
    y1 = M.intersections[node1][1]
    x2 = M.intersections[node2][0]
    y2 = M.intersections[node2][1]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def calc_heuristic(M, n, goal):
    # Need to use the Euclidean distance as it is the shortest distance between two points.
    # Other distances like Manhatan distance is not correct to be used here |x1-x2| + |y1-y2|
    # The reason is that, for manhatan distance (h) is not smaller than "all" possible paths, e.g. three nodes 
    # start: n1 (0,10), n2 (7,7), goal: n3 (10,0), are on the path and we want to go from n1 to n3.
    # The Euclidean distance from n1 to n3 is 14.14. The manhatan distance from n1 to n3 is 20, and the real
    # distance is the sum of the Euclideans of n1 to n2 and n2 to n3 which is 15,23.
    # clearly 15.23 < 20 and thus if we use Manhatan distance the problem won't return the right solution under some circumstances.
    # Manhatan distance would still be correct (and better than Euclidean distnance) to use if the grid map allowed motions are in 4 directions.
    # From:  http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
    # On a grid, there are well-known heuristic functions to use.
    # Use the distance heuristic that matches the allowed movement:
    # On a square grid that allows 4 directions of movement, use Manhattan distance (L1).
    # On a square grid that allows 8 directions of movement, use Diagonal distance (L∞).
    # On a square grid that allows any direction of movement, you might or might not want Euclidean distance (L2). If A* is finding paths on the grid but you are allowing movement not on the grid, you may want to consider other representations of the map.
    # On a hexagon grid that allows 6 directions of movement, use Manhattan distance adapted to hexagonal grids.

    # Diagonal distance
    # D = 1
    # D2 = math.sqrt(2)
    # return D*(dx + dy) + (D2 - 2*D)*min(dx, dy)
    # Assuming a rectangle from upper left corner n1 to lower left corner n3, (if dy < dx), the Diagonal distance would be composed of two line segments
    # one diaonal line with distance of D2*dy from n1 to the lower edge of the rectangle (say point n3), going horizontally in the amount of dy and the second segment would be a line (from n3 to n2) in the amount of dx-dy (all horizontal). This is a good metric (heuristic) if 8 directional motion is allowed only.

    return euclidean_distance(M, n, goal)

def get_frontier_node_f(frontier):
    out = dict()
    for node, attr in frontier.items():
        out.update({node: int(100*attr["f"])/100})
    return out

def optimum_step(node, M, frontier, visited, goal):
    if node not in frontier.keys():
        raise Exception(f"node {node} is not in frontier")
    #print("----------------------------------")
    #print(f"frontier={get_frontier_node_f(frontier)},   node={node},   path={frontier[node]['path']}")
    node_path = frontier[node]["path"] 
    if node == goal:
        print(f"goal={goal}, node_path={node_path}")
        return node_path
    neighbors = M.roads[node]
    node_g = frontier[node]["g"]
    for n in neighbors:
        if n not in visited:
            g_delta = calc_heuristic(M, node, n)
            g = node_g + g_delta
            h = calc_heuristic(M, n, goal)
            f = g + h
            if n not in frontier.keys():
                p = node_path + [n]
                frontier.update({n: {"f": f, "g": g, "path": p}})
            else:
                if f < frontier[n]["f"]:
                    p = node_path + [n]
                    frontier.update({n: {"f": f, "g": g, "path": p}})
    visited.add(node)
    frontier.pop(node)
    item_min_f = min(frontier.items(), key=lambda item: item[1]["f"])
    node_min_f = item_min_f[0]
    #print(f"frontier={get_frontier_node_f(frontier)}, node_min_f={node_min_f}")
    return optimum_step(node_min_f, M, frontier, visited, goal)
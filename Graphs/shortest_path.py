'''
shortest path
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function
should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the
number of nodes. If there is no path between A and B, then return -1.
test_00:
edges = [
['w', 'x'],
['x', 'y'],
['z', 'y'],
['z', 'v'],
['w', 'v']
]
shortest_path(edges, 'w', 'z') # -> 2
'''

from collections import deque

def shortest_path(edges,src,dst):
    graph = create_graph(edges)
    queue =deque([(src,0)])
    visited = set()
    visited.add(src)

    while queue:
        current, distance = queue.popleft()

        if current == dst: 
            return distance
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,distance+1))


    return -1

def create_graph(edges):
    graph = {}
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# Test Case 0
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
assert shortest_path(edges, 'w', 'z') == 2  # Shortest path: w -> v -> z

# Test Case 1
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
assert shortest_path(edges, 'y', 'x') == 1  # Shortest path: y -> x

# Test Case 2
edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
assert shortest_path(edges, 'a', 'e') == 3  # Shortest path: a -> c -> d -> e

# Test Case 3
edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
assert shortest_path(edges, 'e', 'c') == 2  # Shortest path: e -> d -> c

# Test Case 4
edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
assert shortest_path(edges, 'b', 'g') == -1  # No path between b and g

# Test Case 5
edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]
assert shortest_path(edges, 'w', 'e') == 1  # Shortest path: w -> e

# Test Case 6
edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]
assert shortest_path(edges, 'n', 'e') == 2  # Shortest path: n -> c -> e

# Test Case 7
edges = [
    ['m', 'n'],
    ['n', 'o'],
    ['o', 'p'],
    ['p', 'q'],
    ['t', 'o'],
    ['r', 'q'],
    ['r', 's']
]
assert shortest_path(edges, 'm', 's') == 6  # Shortest path: m -> n -> o -> p -> q -> r -> s

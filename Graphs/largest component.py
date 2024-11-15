'''
largest component
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size
of the largest connected component in the graph.
test_00:
largest_component({
0: [8, 1, 5],
1: [0],
5: [0, 8],
8: [0, 5],
2: [3, 4],
3: [2, 4],
4: [3, 2]
}) # -> 4
'''
'''
#iterative approach
def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        if node not in visited:
            visited.add(node)
            current_component_size = 1
            vertex_lst = [node]
            while vertex_lst:
                vertex = vertex_lst.pop()
                for neighbour in graph[vertex]:
                    if neighbour not in visited:
                        current_component_size += 1
                        visited.add(neighbour)
                        vertex_lst.append(neighbour)
        
        if current_component_size > largest:
            largest = current_component_size

    return largest
'''
# recursive approach

def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        if node not in visited:
            current_size = get_component_size(node, graph, visited)
            largest = current_size if current_size > largest else largest
    return largest

def get_component_size(node, graph, visited):
    if node in visited:
        return 0

    visited.add(node)
    size = 1
    for neighbour in graph[node]:
        size += get_component_size(neighbour, graph, visited)
    
    return size

# Test Case 0
assert largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) == 4  # The largest component is {0, 1, 5, 8} with size 4

# Test Case 1
assert largest_component({
    1: [2],
    2: [1, 8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
}) == 6  # The largest component is {1, 2, 8, 9, 7, 6} with size 6

# Test Case 2
assert largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}) == 5  # The largest component is {4, 6, 5, 7, 8} with size 5

# Test Case 3 - Empty graph
assert largest_component({}) == 0  # The graph is empty, so the largest component size is 0

# Test Case 4 - Disconnected nodes and components
assert largest_component({
    0: [4, 7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
}) == 3  # The largest component is {0, 4, 7} with size 3

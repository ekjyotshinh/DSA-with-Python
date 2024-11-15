'''
connected components count
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should
return the number of connected components within the graph.
test_00:
connected_components_count({
0: [8, 1, 5],
1: [0],
5: [0, 8],
8: [0, 5],
2: [3, 4],
3: [2, 4],
4: [3, 2]
}) # -> 2
'''
'''
Using iterative approach
def connected_components_count(graph):
    visited = set()
    count = 0
     
    for node in graph:
        if node not in visited:
            count += 1
            visited.add(node)
            vertex_lst = [node]
            while vertex_lst:
                vertex = vertex_lst.pop()
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        vertex_lst.append(neighbor)
    return count 
'''

# using a helper funtion with recursion
def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count

def explore(graph, current, visited):
    if current in visited:
        return False # it was already visited
    
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True # first time finding this sub island/ sub graph


# Test Case 0
assert connected_components_count({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) == 2

# Test Case 1
assert connected_components_count({
    1: [2],
    2: [1, 8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
}) == 1

# Test Case 2
assert connected_components_count({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}) == 3

# Test Case 3 - Empty graph
assert connected_components_count({}) == 0

# Test Case 4 - Disconnected nodes and components
assert connected_components_count({
    0: [4, 7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
}) == 5

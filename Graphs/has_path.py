'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes
(src, dst). The function should return a boolean indicating whether or not there exists a directed path between
the source and destination nodes.
test_00:
graph = {
'f': ['g', 'i'],
'g': ['h'],
'h': [],
'i': ['g', 'k'],
'j': ['i'],
'k': []
}
has_path(graph, 'f', 'k') # True
both DFS and BFS can be used for this
'''

'''
Time complexity
n = # of nodes
e = # of edges
Time: O(e)
Space: O(n)

n = # of nodes
n^2 = # of edges(complete graph), so
Time: O(n^2)
Space: O(n)
'''
from collections import deque
def has_path(graph, src, dst):

    queue = deque([ src ])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False
       
    '''
    #DFS
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor,dst) == True:
            return True
        
    return False
    '''


def test_has_path():
    # Test case 00
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    assert has_path(graph, 'f', 'k') == True, "Test case 00 failed"

    # Test case 01
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    assert has_path(graph, 'f', 'j') == False, "Test case 01 failed"

    # Test case 02
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    assert has_path(graph, 'i', 'h') == True, "Test case 02 failed"

    # Test case 03
    graph = {
        'v': ['x', 'w'],
        'w': [],
        'x': [],
        'y': ['z'],
        'z': []
    }
    assert has_path(graph, 'v', 'w') == True, "Test case 03 failed"

    # Test case 04
    graph = {
        'v': ['x', 'w'],
        'w': [],
        'x': [],
        'y': ['z'],
        'z': []
    }
    assert has_path(graph, 'v', 'z') == False, "Test case 04 failed"

    print("All test cases passed!")

test_has_path()

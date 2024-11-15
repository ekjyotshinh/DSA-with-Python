'''
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function
should return a boolean indicating whether or not there exists a path between node_A and node_B.
test_00:
edges = [
('i', 'j'),
('k', 'i'),
('m', 'k'),
('k', 'l'),
('o', 'n')
]
undirected_path(edges, 'j', 'm') # -> True

Approach --> convert the edge list to the adjacency list

edge :[('i','j')]

graph : {
i:[j],
j:[i]
}

n = # nodes
e = # edges
Time : O(e)
Space: O(n)
'''
from collections import deque

def undirected_path(connections, src, dst):
    graph = build_graph(connections)

    visited = set()
    vertices = [src]
    while vertices:
        vertex = vertices.pop()
        if vertex == dst:
            return True
        for edge in graph[vertex]:
            if edge not in visited:
                vertices.append(edge)
                visited.add(edge)
    return False

# creates an adjacency list for graph
def build_graph(edge):
    graph = {}

    for edge in edge:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def test_undirected_path():
    edges_00 = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    assert undirected_path(edges_00, 'j', 'm') == True  # Test 00

    edges_01 = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    assert undirected_path(edges_01, 'm', 'j') == True  # Test 01

    edges_02 = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    assert undirected_path(edges_02, 'l', 'j') == True  # Test 02

    edges_03 = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    assert undirected_path(edges_03, 'k', 'o') == False  # Test 03

    edges_04 = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    assert undirected_path(edges_04, 'i', 'o') == False  # Test 04

    edges_05 = [
        ('b', 'a'),
        ('c', 'a'),
        ('b', 'c'),
        ('q', 'r'),
        ('q', 's'),
        ('q', 'u'),
        ('q', 't'),
    ]
    assert undirected_path(edges_05, 'a', 'b') == True  # Test 05

    edges_06 = [
        ('b', 'a'),
        ('c', 'a'),
        ('b', 'c'),
        ('q', 'r'),
        ('q', 's'),
        ('q', 'u'),
        ('q', 't'),
    ]
    assert undirected_path(edges_06, 'a', 'c') == True  # Test 06

    edges_07 = [
        ('b', 'a'),
        ('c', 'a'),
        ('b', 'c'),
        ('q', 'r'),
        ('q', 's'),
        ('q', 'u'),
        ('q', 't'),
    ]
    assert undirected_path(edges_07, 'r', 't') == True  # Test 07

    edges_08 = [
        ('b', 'a'),
        ('c', 'a'),
        ('b', 'c'),
        ('q', 'r'),
        ('q', 's'),
        ('q', 'u'),
        ('q', 't'),
    ]
    assert undirected_path(edges_08, 'r', 'b') == False  # Test 08

    edges_09 = [
        ('s', 'r'),
        ('t', 'q'),
        ('q', 'r'),
    ]
    assert undirected_path(edges_09, 'r', 't') == True  # Test 09
    
    print("All test cases passed!")

test_undirected_path()

'''
how high
Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height
of the tree.
The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
If the tree is empty, return -1.
test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# a
# / \
# b c
# / \ \
# d e f
how_high(a) # -> 2
'''
from Binary_Tree import Node 
from collections import deque

def how_high(root):
    if root is None:
        return -1

    return 1 + max(how_high(root.left) , how_high(root.right))

def run_tests():
    # Test 00
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert how_high(a) == 2  # Expected output: 2

    # Test 01
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    assert how_high(a) == 3  # Expected output: 3

    # Test 02
    a = Node('a')
    c = Node('c')
    a.right = c
    assert how_high(a) == 1  # Expected output: 1

    # Test 03
    a = Node('a')
    assert how_high(a) == 0  # Expected output: 0

    # Test 04
    assert how_high(None) == -1  # Expected output: -1

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

'''
all tree paths
Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each
subarray represents a root-to-leaf path in the tree.
The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the out er list does
not matter.
You may assume that the input tree is non-empty.
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
#   a
#  / \
#  b  c
# / \  \
# d  e  f
all_tree_paths(a) # ->
# [
# [ 'a', 'b', 'd' ],
# [ 'a', 'b', 'e' ],
# [ 'a', 'c', 'f' ]
# ]
'''
#n = number of nodes
#Time: ~O(n)
#Space: ~O(n)

from Binary_Tree import Node 
from collections import deque

#DFS
def all_tree_paths(root):
    #base case 1
    if root is None:
        return []
    #base case 2
    if root.left is None and root.right is None:    #leaf node
        return [[root.val]]
    paths = []

    left_sub_paths = all_tree_paths(root.left) 
    for sub_paths in left_sub_paths:
        paths.append([root.val] + sub_paths)

    right_sub_paths = all_tree_paths(root.right) 
    for sub_paths in right_sub_paths:
        paths.append([root.val] + sub_paths)

    return paths


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
    expected_00 = [
        ['a', 'b', 'd'],
        ['a', 'b', 'e'],
        ['a', 'c', 'f']
    ]
    assert all_tree_paths(a) == expected_00  # Expected output

    # Test 01
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i
    expected_01 = [
        ['a', 'b', 'd'],
        ['a', 'b', 'e', 'g'],
        ['a', 'b', 'e', 'h'],
        ['a', 'c', 'f', 'i']
    ]
    assert all_tree_paths(a) == expected_01  # Expected output

    # Test 02
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')
    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v
    expected_02 = [
        ['q', 'r', 't', 'u', 'v'],
        ['q', 's']
    ]
    assert all_tree_paths(q) == expected_02  # Expected output

    # Test 03
    z = Node('z')
    expected_03 = [['z']]
    assert all_tree_paths(z) == expected_03  # Expected output

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

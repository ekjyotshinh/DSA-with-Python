'''
tree levels
Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each
sublist represents a level of the tree.
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
tree_levels(a) # ->
# [
# ['a'],
# ['b', 'c'],
# ['d', 'e', 'f']
# ]
'''
#n = number of nodes
#Time: ~O(n)
#Space: ~O(n)

from Binary_Tree import Node 
from collections import deque


def tree_levels(root):
    #DFS
    levels = []
    fill_levels(root, levels, 0)
    return levels


    '''
    #BFS
    if root is None:
        return []
    levels = []
    queue = deque([(root,0)])
    while queue:
        cur , level_depth = queue.popleft()
        # Ensure the levels list has a sublist for the current depth
        if level_depth == len(levels):
            levels.append([])

        # Append the current node's value to the current level's sublist
        levels[level_depth].append(cur.val)

        if cur.left:
            queue.append((cur.left,level_depth+1))
        if cur.right:
            queue.append((cur.right,level_depth+1))

    return levels
    '''
def fill_levels(root, levels, level_depth):
    if root is None:
        return
    if level_depth == len(levels):
        levels.append([])

    # Append the current node's value to the current level's sublist
    levels[level_depth].append(root.val)
    fill_levels(root.left,levels,level_depth+1)
    fill_levels(root.right,levels,level_depth+1)


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
        ['a'],
        ['b', 'c'],
        ['d', 'e', 'f']
    ]
    assert tree_levels(a) == expected_00  # Expected output

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
        ['a'],
        ['b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    assert tree_levels(a) == expected_01  # Expected output

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
        ['q'],
        ['r', 's'],
        ['t'],
        ['u'],
        ['v']
    ]
    assert tree_levels(q) == expected_02  # Expected output

    # Test 03
    assert tree_levels(None) == []  # Expected output is an empty list

    # Test 04: Single node
    z = Node('z')
    expected_04 = [['z']]
    assert tree_levels(z) == expected_04  # Expected output

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

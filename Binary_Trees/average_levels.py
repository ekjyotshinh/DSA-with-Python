'''
level averages
Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return
a list containing the average value of each level.
test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# 3
# / \
# 11 4
# / \ \
# 4 -2 1
level_averages(a) # -> [ 3, 7.5, 1 ]
'''
#n = number of nodes
#Time: ~O(n)
#Space: ~O(n)

from Binary_Tree import Node 
from collections import deque
from statistics import mean

def level_averages(root):
    #DFS
    levels = []
    fill_levels(root, levels, 0)

    avgs = []
    for lvl in levels:
        avgs.append(mean(lvl))

    return avgs


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
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    expected_00 = [3, 7.5, 1]
    assert level_averages(a) == expected_00  # Expected output

    # Test 01
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g
    expected_01 = [5, 32.5, 17.5, 2]
    assert level_averages(a) == expected_01  # Expected output

    # Test 02
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(45)
    g = Node(-1)
    h = Node(-2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    expected_02 = [-1, -5.5, 14, -1.5]
    assert level_averages(a) == expected_02  # Expected output

    # Test 03
    q = Node(13)
    r = Node(4)
    s = Node(2)
    t = Node(9)
    u = Node(2)
    v = Node(42)
    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v
    expected_03 = [13, 3, 9, 2, 42]
    assert level_averages(q) == expected_03  # Expected output

    # Test 04: Empty tree
    expected_04 = []
    assert level_averages(None) == expected_04  # Expected output

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

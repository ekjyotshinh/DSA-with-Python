'''
tree min value
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the
minimum value within the tree.
You may assume that the input tree is non-empty.
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
#    3
#   / \
#   11 4
#  / \  \
# 4 - 2  1
tree_min_value(a) # -> -2
'''

from Binary_Tree import Node 
from collections import deque



# Example tree_min_value function
def tree_min_value(root):
    #BFS
    if root is None:
        return None
    best_min = float('inf')
    
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.val < best_min:
            best_min = curr.val
        
        if curr.left is not None:
            queue.append(curr.left)
        
        if curr.right is not None:
            queue.append(curr.right)
    
    return best_min


    #DFS
    '''
    if root is None:
        return float('inf')
    
    left_min = tree_min_value(root.left) 
    right_min = tree_min_value(root.right)
    return min(left_min, right_min, root.val)

    '''

# Test Cases

# Test case 00
def test_00():
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
    assert tree_min_value(a) == -2

# Test case 01
def test_01():
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # 5
    # / \
    # 11 3
    # / \ \
    # 4 14 12
    assert tree_min_value(a) == 3

# Test case 02
def test_02():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(-2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    # -1
    # / \
    # -6 -5
    # / \ \
    # -3 -4 -13
    # / \
    # -2 -2
    assert tree_min_value(a) == -13

# Test case 03: Single node tree
def test_03():
    a = Node(42)
    # 42
    assert tree_min_value(a) == 42

# Running the test cases
test_00()
test_01()
test_02()
test_03()

print("All test cases pass")

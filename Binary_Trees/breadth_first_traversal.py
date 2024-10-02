'''
breadth first values
Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing
all values of the tree in breadth-first order.
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
#    a
#   / \
#  b   c
# / \   \
# d  e   f
breadth_first_values(a)
# -> ['a', 'b', 'c', 'd', 'e', 'f']
'''
# for DFS we use queue
# put left child then right child

from Binary_Tree import Node 
from collections import deque

def breadth_first_values(root):
    #iterative

    if root is None:
        return []
    
    queue = deque([root])
    res = []

    while queue:
        curr_node = queue.popleft()
        res.append(curr_node.val)

        if curr_node.left is not None:
            queue.append(curr_node.left)

        if curr_node.right is not None:
            queue.append(curr_node.right)

    return res


# Test Cases

# Test case 00
def test_00():
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
    assert breadth_first_values(a) == ['a', 'b', 'c', 'd', 'e', 'f']

# Test case 01
def test_01():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    assert breadth_first_values(a) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Test case 02
def test_02():
    a = Node('a')
    assert breadth_first_values(a) == ['a']

# Test case 03
def test_03():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    x = Node('x')
    a.right = b
    b.left = c
    c.left = x
    c.right = d
    d.right = e
    assert breadth_first_values(a) == ['a', 'b', 'c', 'x', 'd', 'e']

# Test case 04
def test_04():
    assert breadth_first_values(None) == []

# Running the test cases
test_00()
test_01()
test_02()
test_03()
test_04()

print("All test cases pass")

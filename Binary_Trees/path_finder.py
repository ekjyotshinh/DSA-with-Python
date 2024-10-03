'''
tree path finder
Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array
representing a path to the target value. If the target value is not found in the tree, then return None.
You may assume that the tree contains unique values.
test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#    a
#   / \
#   b  c
#  / \  \
# d   e  f
path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]
'''

from Binary_Tree import Node 
from collections import deque

def path_finder(root, target):
    res = _path_finder(root, target)
    if res is None:
        return None
    else:
        return res[::-1]  # Reverse the result to get root-to-leaf order

def _path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)  # Appending root value to the path (no return required)
        return left_path
    
    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)  # Appending root value to the path (no return required)
        return right_path
    
    return None




# Test case 00
def test_00():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
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
    assert path_finder(a, "e") == ['a', 'b', 'e']

# Test case 01
def test_01():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
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
    assert path_finder(a, "p") == None

# Test case 02
def test_02():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    # a
    # / \
    # b c
    # / \ \
    # d e f
    # / \
    # g h
    assert path_finder(a, "c") == ['a', 'c']

# Test case 03
def test_03():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    # a
    # / \
    # b c
    # / \ \
    # d e f
    # / \
    # g h
    assert path_finder(a, "h") == ['a', 'c', 'f', 'h']

# Test case 04: Single node tree
def test_04():
    x = Node("x")
    # x
    assert path_finder(x, "x") == ['x']

# Test case 05: Empty tree
def test_05():
    assert path_finder(None, "x") == None

# Test case 06: Deep tree with 19500 nodes
def test_06():
    root = Node(0)
    curr = root
    for i in range(1, 19500):
        curr.right = Node(i)
        curr = curr.right

    result = path_finder(root, 162)
    assert result == list(range(0, 163)), f"Expected {list(range(0, 163))} but got {result}"



# Running the test cases
test_00()
test_01()
test_02()
test_03()
test_04()
test_05()
test_06()

print("All test cases pass")


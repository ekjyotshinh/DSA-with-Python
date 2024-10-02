'''
Tree Includes
Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean
indicating whether or not the value is contained in the tree.
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
tree_includes(a, "e") # -> True
'''

from Binary_Tree import Node 
from collections import deque

# Example tree_includes function
def tree_includes(root, target):

    #BFS
    if root is None:
        return False
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if target == curr.val:
            return True
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    return False
    #DFS
    '''
    if root is None:
        return False

    return root.val == target or tree_includes(root.left, target) or tree_includes(root.right, target)
    '''
    
# Test Cases

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
    assert tree_includes(a, "e") == True

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
    assert tree_includes(a, "a") == True

# Test case 02
def test_02():
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
    assert tree_includes(a, "n") == False

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
    assert tree_includes(a, "f") == True

# Test case 04
def test_04():
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
    assert tree_includes(a, "p") == False

# Test case 05: Empty tree
def test_05():
    assert tree_includes(None, "b") == False

# Running the test cases
test_00()
test_01()
test_02()
test_03()
test_04()
test_05()

print("All test cases pass")

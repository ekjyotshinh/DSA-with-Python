'''
Tree Sum
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function
should return the total sum of all values in the tree.
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
#  11  4
#  / \  \
# 4  -2  1
tree_sum(a) # -> 21

'''

from Binary_Tree import Node 
from collections import deque



def tree_sum(root):
    #breadth first approach
    if root is None:
        return 0
    
    queue = deque([root])
    sum = 0
    while queue:
        curr = queue.popleft()
        sum += curr.val

        if curr.left is not None:
            queue.append(curr.left)
        
        if curr.right is not None:
            queue.append(curr.right)

    return sum

    # depth first approach
    '''
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)
    '''



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
    assert tree_sum(a) == 21

# Test case 01
def test_01():
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    assert tree_sum(a) == 10

# Test case 02
def test_02():
    assert tree_sum(None) == 0

# Test case 03: Tree with all negative values
def test_03():
    a = Node(-5)
    b = Node(-3)
    c = Node(-10)
    d = Node(-4)
    e = Node(-7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    # -5
    # / \
    # -3 -10
    # / \
    # -4 -7
    assert tree_sum(a) == -29

# Test case 04: Tree with mixed positive and negative values
def test_04():
    a = Node(7)
    b = Node(-6)
    c = Node(4)
    d = Node(-3)
    e = Node(2)
    f = Node(5)
    g = Node(-2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    f.left = g
    # 7
    # / \
    # -6 4
    # / \ \
    # -3 2 5
    # /
    # -2
    assert tree_sum(a) == 7

# Test case 05: Single node tree (root only)
def test_05():
    a = Node(42)
    # 42
    assert tree_sum(a) == 42

# Test case 06: Larger tree
def test_06():
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)
    e = Node(50)
    f = Node(60)
    g = Node(70)
    h = Node(80)
    i = Node(90)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    # 10
    # / \
    # 20 30
    # / \ / \
    # 40 50 60 70
    # / \
    # 80 90
    assert tree_sum(a) == 450

# Test case 07: Deep tree (one-sided)
def test_07():
    a = Node(5)
    b = Node(3)
    c = Node(1)
    d = Node(-1)
    e = Node(2)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    # 5
    # /
    # 3
    # /
    # 1
    # /
    # -1
    # /
    # 2
    assert tree_sum(a) == 10

# Running the test cases
test_00()
test_01()
test_02()
test_03()
test_04()
test_05()
test_06()
test_07()

print("All test cases pass")





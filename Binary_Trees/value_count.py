'''
tree value count
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number
of times that the target occurs in the tree.
test_00:
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# 12
# / \
# 6 6
# / \ \
# 4 6 12
tree_value_count(a, 6) # -> 3
'''
from Binary_Tree import Node 
from collections import deque


def tree_value_count(root, target):
    #BFS
    if root is None:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.val == target:
            count += 1
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return count


    #DFS
    '''
    if root is None:
        return 0
        
    return (1 if root.val == target else 0) + tree_value_count(root.left,target) + tree_value_count(root.right,target)
    '''
    


# Test Cases

# Test Case 0:
def test_00():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # 12
    # / \
    # 6 6
    # / \ \
    # 4 6 12
    print(tree_value_count(a, 6)) # -> 3

# Test Case 1:
def test_01():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # 12
    # / \
    # 6 6
    # / \ \
    # 4 6 12
    print(tree_value_count(a, 12)) # -> 2

# Test Case 2:
def test_02():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    # 7
    # / \
    # 5 1
    # / \ \
    # 1 8 7
    # / \
    # 1 1
    print(tree_value_count(a, 1)) # -> 4

# Test Case 3:
def test_03():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    # 7
    # / \
    # 5 1
    # / \ \
    # 1 8 7
    # / \
    # 1 1
    print(tree_value_count(a, 9)) # -> 0

# Test Case 4:
def test_04():
    print(tree_value_count(None, 42)) # -> 0

# Run the test cases
if __name__ == "__main__":
    test_00()  # Expected: 3
    test_01()  # Expected: 2
    test_02()  # Expected: 4
    test_03()  # Expected: 0
    test_04()  # Expected: 0

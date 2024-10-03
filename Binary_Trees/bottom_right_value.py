'''
bottom right value
Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the
bottom-most level of the tree.
You may assume that the input tree is non-empty.
test_00:
a = Node(3)
b = Node(11)
c = Node(10)
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
# 11 10
# / \ \
# 4 -2 1
bottom_right_value(a) # -> 1
'''
from Binary_Tree import Node 
from collections import deque
#do a bfs traversal
# bottom most and right most
def bottom_right_value(root):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return cur.val
    

def run_tests():
    # Test 00
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert bottom_right_value(a) == 1  # Expected output: 1

    # Test 01
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    assert bottom_right_value(a) == 6  # Expected output: 6

    # Test 02
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i
    assert bottom_right_value(a) == 7  # Expected output: 7

    # Test 03
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f
    assert bottom_right_value(a) == 'f'  # Expected output: 'f'

    # Test 04
    a = Node(42)
    assert bottom_right_value(a) == 42  # Expected output: 42

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

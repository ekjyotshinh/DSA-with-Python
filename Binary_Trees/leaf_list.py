'''
leaf list
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in
left-to-right order.
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
# a
# / \
# b c
# / \ \
# d e f
leaf_list(a) # -> [ 'd', 'e', 'f' ]
'''
#n = number of nodes
#Time: ~O(n)
#Space: ~O(n)

from Binary_Tree import Node 
from collections import deque
from statistics import mean

#DFS
def leaf_list(root,leaf_lst=[]):
    #iterative
    '''
    if root is None:
        return[]
    leaf_lst = []
    stack = [root]

    while stack:
        cur = stack.pop()

        if cur.right:
            stack.append(cur.right)

        if cur.left:
            stack.append(cur.left)

        if cur.left is None and cur.right is None:
            leaf_lst.append(cur.val)

    return leaf_lst
    '''

    #recursive
    leaf_lst = []
    _leaf_list_helper(root, leaf_lst)
    return leaf_lst

def _leaf_list_helper(node, leaf_lst):
    if node is None:
        return

    if node.left is None and node.right is None:
        leaf_lst.append(node.val)
        return

    if node.left is not None:
        _leaf_list_helper(node.left, leaf_lst)
    if node.right is not None:
        _leaf_list_helper(node.right, leaf_lst)




def run_tests():
    # Test 00
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
    expected_00 = ['d', 'e', 'f']

    assert leaf_list(a) == expected_00  # Expected output

    # Test 01
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
    expected_01 = ['d', 'g', 'h']

    assert leaf_list(a) == expected_01  # Expected output

    # Test 02
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
    expected_02 = [20, 1, 3, 54]

    assert leaf_list(a) == expected_02  # Expected output

    # Test 03
    x = Node('x')
    expected_03 = ['x']
    assert leaf_list(x) == expected_03  # Expected output

    # Test 04: Empty tree
    expected_04 = []
    assert leaf_list(None) == expected_04  # Expected output

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

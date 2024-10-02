'''
depth first values
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing
all values of the tree in depth-first order.
example
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
depth_first_values(a)
# -> ['a', 'b', 'd', 'e', 'c', 'f']
'''
# for DFS we use Stack
# put right child then left child

from Binary_Tree import Node 


def depth_first_values(root):

    #recursive
    
    if root is None:
        return []
    left_vals = depth_first_values(root.left)
    right_vals = depth_first_values(root.right)

    return [root.val, *left_vals, *right_vals]
#same as [root.val ] + left_vals + right_vals

    # iterative
    '''
    if root is None:
        return []
    res = []
    stack = [root]

    while stack:
        curr_node = stack.pop()
        res.append(curr_node.val)

        if curr_node.right is not None:
            stack.append(curr_node.right)
        if curr_node.left is not None:
            stack.append(curr_node.left)

    return res
    '''



def run_tests():
    # Test 00:
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
    print("Test 00:")
    print(depth_first_values(a))  # Expected -> ['a', 'b', 'd', 'e', 'c', 'f']

    # Test 01:
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    print("Test 01:")
    print(depth_first_values(a))  # Expected -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

    # Test 02:
    a = Node('a')
    print("Test 02:")
    print(depth_first_values(a))  # Expected -> ['a']

    # Test 03:
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.right = b
    b.left = c
    c.right = d
    d.right = e
    print("Test 03:")
    print(depth_first_values(a))  # Expected -> ['a', 'b', 'c', 'd', 'e']

    # Test 04:
    print("Test 04:")
    print(depth_first_values(None))  # Expected -> []

if __name__ == "__main__":
    run_tests()

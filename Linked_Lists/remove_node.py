''''
remove node
Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node
containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the
linked list, only remove the first instance of the target in the list.
Do this in-place.
You may assume that the input list is non-empty.
You may assume that the input list contains the target.
'''

from Linked_List import Node


def remove_node(head,target):
    #recursive
    if head is None:
        return None
    if(head.val == target):
        return head.next
    head.next = remove_node(head.next,target)
    return head

    '''
    #iterative
    # Special case: if the head itself is the node to remove
    if head.val == target:
        return head.next
    current = head
    prev = None
    while current is not None:
        if current.val == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
    '''

def run_tests():
    # Test 00:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("c")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    result = remove_node(a, "c")
    print("Test 00:")
    print_linked_list(result)
    # Expected -> a -> b -> d -> e -> f

    # Test 01:
    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z
    result = remove_node(x, "z")
    print("Test 01:")
    print_linked_list(result)
    # Expected -> x -> y

    # Test 02:
    q = Node("q")
    r = Node("r")
    s = Node("s")
    q.next = r
    r.next = s
    # q -> r -> s
    result = remove_node(q, "q")
    print("Test 02:")
    print_linked_list(result)
    # Expected -> r -> s

    # Test 03:
    node1 = Node("h")
    node2 = Node("i")
    node3 = Node("j")
    node4 = Node("i")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # h -> i -> j -> i
    result = remove_node(node1, "i")
    print("Test 03:")
    print_linked_list(result)
    # Expected -> h -> j -> i

    # Test 04:
    t = Node("t")
    # t
    result = remove_node(t, "t")
    print("Test 04:")
    print_linked_list(result)
    # Expected -> None

def print_linked_list(head):
    # Iterative print function to display linked list values
    current = head
    while current is not None:
        if current.next is not None:
            print(current.val, end=" -> ")  # Print value with arrow
        else:
            print(current.val)  # Last node, no arrow
        current = current.next
if __name__ == "__main__":
    run_tests()

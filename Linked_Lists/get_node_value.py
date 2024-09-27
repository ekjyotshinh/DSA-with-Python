'''
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the
value of the linked list at the specified index.
If there is no node at the given index, then return None.
'''
from Linked_List import Node

def get_node_value(head, index):
    '''
    for i in range(index):
        if head.next is not None:
            head = head.next
        else:
            return None
    return head.val
    '''
    '''
    count = 0
    while head is not None:
        if count == index:
            return head.val
        count += 1
        head = head.next
    return None
    '''

    #recursive
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next,index-1)
    


def run_tests():
    # Test 00:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d
    print("Test 00:", get_node_value(a, 2))  # Expected -> 'c'

    # Test 01:
    print("Test 01:", get_node_value(a, 3))  # Expected -> 'd'

    # Test 02:
    print("Test 02:", get_node_value(a, 7))  # Expected -> None

    # Test 03:
    node1 = Node("banana")
    node2 = Node("mango")
    node1.next = node2
    # banana -> mango
    print("Test 03:", get_node_value(node1, 0))  # Expected -> 'banana'

    # Test 04:
    print("Test 04:", get_node_value(node1, 1))  # Expected -> 'mango'

if __name__ == "__main__":
    run_tests()

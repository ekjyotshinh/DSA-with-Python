'''
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list
containing all values of the nodes in the linked list.
'''
from Linked_List import Node

def linked_list_values(head):

    #iterative
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

    #recursive
    '''
    values = []
    _linked_list_values(head, values)
    return values

def _linked_list_values(head, values):
    if head is None:
        return
    values.append(head.val)
    _linked_list_values(head.next, values)
    '''


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
    print("Test 00:", linked_list_values(a)) 
    # Expected -> ['a', 'b', 'c', 'd']

    # Test 01:
    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    print("Test 01:", linked_list_values(x)) 
    # Expected -> ['x', 'y']

    # Test 02:
    q = Node("q")
    # q
    print("Test 02:", linked_list_values(q)) 
    # Expected -> ['q']

    # Test 03:
    print("Test 03:", linked_list_values(None)) 
    # Expected -> []

if __name__ == "__main__":
    run_tests()

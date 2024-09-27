'''
Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a
boolean indicating whether or not the linked list contains the target.
'''

from Linked_List import Node

def linked_list_find(head, target):
    '''
    #iterative
    while(head is not None):
        if head.val == target:
            return True
        head = head.next
    return False
    '''

    #recursive
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next,target)
    


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
    print("Test 00:", linked_list_find(a, "c"))  # Expected -> True

    # Test 01:
    print("Test 01:", linked_list_find(a, "d"))  # Expected -> True

    # Test 02:
    print("Test 02:", linked_list_find(a, "q"))  # Expected -> False

    # Test 03:
    node1 = Node("jason")
    node2 = Node("leneli")
    node1.next = node2
    # jason -> leneli
    print("Test 03:", linked_list_find(node1, "jason"))  # Expected -> True

    # Test 04:
    node1 = Node(42)
    # 42
    print("Test 04:", linked_list_find(node1, 42))  # Expected -> True

    # Test 05:
    print("Test 05:", linked_list_find(node1, 100))  # Expected -> False

if __name__ == "__main__":
    run_tests()

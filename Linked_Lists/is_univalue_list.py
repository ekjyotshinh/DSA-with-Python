'''
Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating
whether or not the linked list contains exactly one unique value.
You may assume that the input list is non-empty.
'''


from Linked_List import Node


def is_univalue_list(head):

    #recursive
    if head.next is None:
        return True
    if head.val != head.next.val:
        return False
    return is_univalue_list(head.next)
    #compare adjacents
    '''
    while head.next is not None:
        if head.val != head.next.val:
            return False
        head = head.next
    return True
    '''
    '''
    #compare everything to first
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True
    '''
    


def run_tests():
    # Test 00:
    a = Node(7)
    b = Node(7)
    c = Node(7)
    a.next = b
    b.next = c
    # 7 -> 7 -> 7
    print("Test 00:", is_univalue_list(a))  
    # Expected: True

    # Test 01:
    a = Node(7)
    b = Node(7)
    c = Node(4)
    a.next = b
    b.next = c
    # 7 -> 7 -> 4
    print("Test 01:", is_univalue_list(a))  
    # Expected: False

    # Test 02:
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)
    u.next = v
    v.next = w
    w.next = x
    x.next = y
    # 2 -> 2 -> 2 -> 2 -> 2
    print("Test 02:", is_univalue_list(u))  
    # Expected: True

    # Test 03:
    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)
    u.next = v
    v.next = w
    w.next = x
    x.next = y
    # 2 -> 2 -> 3 -> 3 -> 2
    print("Test 03:", is_univalue_list(u))  
    # Expected: False

    # Test 04:
    z = Node('z')
    # z
    print("Test 04:", is_univalue_list(z))  
    # Expected: True

if __name__ == "__main__":
    run_tests()

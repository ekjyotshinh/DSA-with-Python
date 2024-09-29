'''
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together
into single sorted linked list. The function should return the head of the merged linked list.
Do this in-place, by mutating the original Nodes.
You may assume that both input lists are non-empty and contain increasing sorted numbers.
'''


from Linked_List import Node


def merge_lists(head1, head2):
    #recursive
    if (head1 is None and head2 is None):
        return None
    
    if (head1 is None):
        return head2
    
    if (head2 is None):
        return head1

    if(head1.val < head2.val):
        result = Node(head1.val)
        head1 = head1.next
    else:
        result = Node(head2.val)
        head2 = head2.next
    result.next = merge_lists(head1,head2)

    return result

    '''
    #iterative
    dummyHead = Node("")
    current = dummyHead
    while(head1 is not None and head2 is not None):
        if(head1.val < head2.val):
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current= current.next
    if(head1 is not None):
        current.next = head1
    if(head2 is not None):
        current.next = head2
    return dummyHead.next
    '''


def print_linked_list(head):
    # Helper function to print linked list values
    current = head
    while current:
        if current.next:
            print(current.val, end=" -> ")
        else:
            print(current.val)
        current = current.next

def run_tests():
    # Test 00:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28
    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25
    result = merge_lists(a, q)
    print("Test 00:")
    print_linked_list(result)
    # Expected: 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28

    # Test 01:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28
    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t
    # 1 -> 8 -> 9 -> 10
    result = merge_lists(a, q)
    print("Test 01:")
    print_linked_list(result)
    # Expected: 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28

    # Test 02:
    h = Node(30)
    # 30
    p = Node(15)
    q = Node(67)
    p.next = q
    # 15 -> 67
    result = merge_lists(h, p)
    print("Test 02:")
    print_linked_list(result)
    # Expected: 15 -> 30 -> 67

if __name__ == "__main__":
    run_tests()

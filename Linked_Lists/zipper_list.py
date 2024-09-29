'''
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two
lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting
list should terminate with the remaining nodes. The function should return the head of the zippered linked list.
Do this in-place, by mutating the original Nodes.
You may assume that both input lists are non-empty.
'''


from Linked_List import Node

def zipper_lists(head1, head2):

    #recursive approach
    if (head1 is None and head2 is None):
        return None
    
    if (head1 is None):
        return head2
    
    if (head2 is None):
        return head1
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_lists(next1,next2)
    return head1




    # my iterative approach
    '''
    dummyHead = Node("")
    current = dummyHead
    while(head1 is not None and head2 is not None):
        # head 1 first
        current.next = head1
        current = current.next
        head1 = head1.next

        # head 2 after head 1
        current.next = head2
        current=current.next
        head2 = head2.next

    if(head1 is not None):
        current.next = head1
    if(head2 is not None):
        current.next = head2
    return dummyHead.next
    '''
    '''
    #structy approach
    tail = head1
    current_1 = head1.next
    current_2 = head2
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
    return head1
    '''


def run_tests():
    # Test 00:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c
    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z
    result = zipper_lists(a, x)
    print("Test 00:")
    print_linked_list(result) 
    # Expected -> a -> x -> b -> y -> c -> z

    # Test 01:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z
    result = zipper_lists(a, x)
    print("Test 01:")
    print_linked_list(result)
    # Expected -> a -> x -> b -> y -> c -> z -> d -> e -> f

    # Test 02:
    s = Node("s")
    t = Node("t")
    s.next = t
    # s -> t
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four
    # 1 -> 2 -> 3 -> 4
    result = zipper_lists(s, one)
    print("Test 02:")
    print_linked_list(result)
    # Expected -> s -> 1 -> t -> 2 -> 3 -> 4

    # Test 03:
    w = Node("w")
    # w
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3
    result = zipper_lists(w, one)
    print("Test 03:")
    print_linked_list(result)
    # Expected -> w -> 1 -> 2 -> 3

    # Test 04:
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3
    w = Node("w")
    # w
    result = zipper_lists(one, w)
    print("Test 04:")
    print_linked_list(result)
    # Expected -> 1 -> w -> 2 -> 3

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

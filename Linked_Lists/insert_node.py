''''
insert node
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value
into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked
list.
Do this in-place.
You may assume that the input list is non-empty and the index is not greater than the length of the input list.
'''

from Linked_List import Node


def insert_node(head, value, index):
    #recursive
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node
    head.next = insert_node(head.next, value, index-1)
    return head
    '''
    #iterative
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    current = head
    for i in range(index-1):
        current = current.next
    nxt = current.next
    current.next = Node(value)
    current.next.next = nxt
    return head
    '''



def print_linked_list(head):
    current = head
    while current is not None:
        if current.next is not None:
            print(current.val, end=" -> ")
        else:
            print(current.val)
        current = current.next

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
    result = insert_node(a, 'x', 2)
    print("Test 00:")
    print_linked_list(result)
    # Expected -> a -> b -> x -> c -> d

    # Test 01:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d
    result = insert_node(a, 'v', 3)
    print("Test 01:")
    print_linked_list(result)
    # Expected -> a -> b -> c -> v -> d

    # Test 02:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d
    result = insert_node(a, 'm', 4)
    print("Test 02:")
    print_linked_list(result)
    # Expected -> a -> b -> c -> d -> m

    # Test 03:
    a = Node("a")
    b = Node("b")
    a.next = b
    # a -> b
    result = insert_node(a, 'z', 0)
    print("Test 03:")
    print_linked_list(result)
    # Expected -> z -> a -> b

if __name__ == "__main__":
    run_tests()

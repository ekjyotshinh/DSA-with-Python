'''
Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the
order of the nodes in the linked list in-place and return the new head of the reversed linked list
'''

from Linked_List import Node


'''
in loop do

current.next = prev #update current pointer to point to previous
prev = current  # update the prec pointer
current = next  # set the new current
next = next.next  # update the next pointer
'''
def reverse_list(head, prev = None):
    '''
    current = head
    prev = None
    while current is not None:
        nxt = current.next      # Store the next node
        current.next = prev     # Reverse the link
        prev = current          # Move prev to current
        current = nxt           # Move to the next node
    return prev
    '''

    #recursive
    if head is None:
        return prev
    nxt = head.next
    head.next = prev
    return reverse_list(nxt,head)


def linked_list_values(head):

    #iterative
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values



def run_tests():
    # Test 00:
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
    reversed_head = reverse_list(a)
    # Expected: f -> e -> d -> c -> b -> a
    print("Test 00:", linked_list_values(reversed_head))  # Helper function to get values

    # Test 01:
    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    reversed_head = reverse_list(x)
    # Expected: y -> x
    print("Test 01:", linked_list_values(reversed_head))  # Helper function to get values

    # Test 02:
    p = Node("p")
    # p
    reversed_head = reverse_list(p)
    # Expected: p
    print("Test 02:", linked_list_values(reversed_head))  # Helper function to get values

if __name__ == "__main__":
    run_tests()

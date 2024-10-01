''''
create linked list
Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each
item of the list as the values of the nodes. The function should return the head of the linked list.
'''

from Linked_List import Node

def create_linked_list(values):
    #recursive
    if(len(values) == 0):
        return None
    head = Node(values[0])
    head.next = create_linked_list(values[1:])
    return head

    #itertative
    '''
    dummy_node = Node("")
    current = dummy_node
    for val in values:
        current.next = Node(val)
        current = current.next
    
    return dummy_node.next
    '''


def print_linked_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)) if result else "null")

def run_tests():
    # test_00
    head_00 = create_linked_list(["h", "e", "y"])
    print_linked_list(head_00)
    # Expected Output: h -> e -> y

    # test_01
    head_01 = create_linked_list([1, 7, 1, 8])
    print_linked_list(head_01)
    # Expected Output: 1 -> 7 -> 1 -> 8

    # test_02
    head_02 = create_linked_list(["a"])
    print_linked_list(head_02)
    # Expected Output: a

    # test_03
    head_03 = create_linked_list([])
    print_linked_list(head_03)
    # Expected Output: null

if __name__ == "__main__":
    run_tests()

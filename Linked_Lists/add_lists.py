''''
add lists
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as
values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return
the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as w ell.
'''

from Linked_List import Node

def add_lists(head1, head2, carry = 0):
    #recursive
    # Base case: both lists are empty and no carry
    if head1 is None and head2 is None and carry == 0:
        return
    
    # Get the values of the current nodes, or 0 if one list is shorter
    digit1 = head1.val if head1 is not None else 0
    digit2 = head2.val if head2 is not None else 0

    # Sum the digits and the carry
    sum = digit1 + digit2 + carry
    # Update the carry
    carry = sum // 10
    # Get the digit to store in the current node using mod
    digit = sum % 10

    result = Node(digit)

    # Prepare the next nodes
    next1=head1.next if head1 is not None else head1
    next2 = head2.next if head2 is not None else head2

    result.next = add_lists(next1, next2, carry)
    
    return result




    '''
    #iterative
    result= Node(0)
    cur = result
    
    current1 = head1
    current2 = head2
    carry = 0

    while current1 is not None or current2 is not None or carry != 0:
        # Get the current digits or 0 if the list has ended
        digit1 = current1.val if current1 is not None else 0
        digit2 = current2.val if current2 is not None else 0

        # Sum the digits and the carry
        sum = digit1 + digit2 + carry

        # Update the carry
        carry = sum // 10

        # Get the digit to store in the current node using mod
        digit = sum % 10

        # Create a new node with the calculated digit
        new_node = Node(digit)
        cur.next = new_node

        # Move the current pointer to the next node
        cur = cur.next

        # Move to the next nodes in the input lists
        current1=current1.next if current1 is not None else current1
        current2 = current2.next if current2 is not None else current2
    
    return result.next
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
    # 621 + 354 = 975
    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(6)
    a1.next = a2
    a2.next = a3

    b1 = Node(4)
    b2 = Node(5)
    b3 = Node(3)
    b1.next = b2
    b2.next = b3

    result_00 = add_lists(a1, b1)
    print_linked_list(result_00)
    # Expected Output: 5 -> 7 -> 9

    # test_01
    # 7541 + 32 = 7573
    a1 = Node(1)
    a2 = Node(4)
    a3 = Node(5)
    a4 = Node(7)
    a1.next = a2
    a2.next = a3
    a3.next = a4

    b1 = Node(2)
    b2 = Node(3)
    b1.next = b2

    result_01 = add_lists(a1, b1)
    print_linked_list(result_01)
    # Expected Output: 3 -> 7 -> 5 -> 7

    # test_02
    # 39 + 47 = 86
    a1 = Node(9)
    a2 = Node(3)
    a1.next = a2

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2

    result_02 = add_lists(a1, b1)
    print_linked_list(result_02)
    # Expected Output: 6 -> 8

    # test_03
    # 89 + 47 = 136
    a1 = Node(9)
    a2 = Node(8)
    a1.next = a2

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2

    result_03 = add_lists(a1, b1)
    print_linked_list(result_03)
    # Expected Output: 6 -> 3 -> 1

    # test_04
    # 999 + 6 = 1005
    a1 = Node(9)
    a2 = Node(9)
    a3 = Node(9)
    a1.next = a2
    a2.next = a3

    b1 = Node(6)

    result_04 = add_lists(a1, b1)
    print_linked_list(result_04)
    # Expected Output: 5 -> 0 -> 0 -> 1

if __name__ == "__main__":
    run_tests()

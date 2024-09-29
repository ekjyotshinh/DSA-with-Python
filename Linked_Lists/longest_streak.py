'''
Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest
consecutive streak of the same value within the list.
'''


from Linked_List import Node


def longest_streak(head):

    longest_streak = 0
    current_streak = 0
    prev = None
    current = head

    while current is not None:
        if prev == current.val:
            current_streak += 1
        else:
            current_streak = 1
        
        if current_streak > longest_streak:
            longest_streak = current_streak
        
        prev = current.val
        current = current.next

    return longest_streak



def run_tests():
    # Test 00:
    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print("Test 00:", longest_streak(a))  # Expected: 3

    # Test 01:
    a = Node(3)
    b = Node(3)
    c = Node(3)
    d = Node(3)
    e = Node(9)
    f = Node(9)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print("Test 01:", longest_streak(a))  # Expected: 4

    # Test 02:
    a = Node(9)
    b = Node(9)
    c = Node(1)
    d = Node(9)
    e = Node(9)
    f = Node(9)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print("Test 02:", longest_streak(a))  # Expected: 3

    # Test 03:
    a = Node(5)
    b = Node(5)
    a.next = b
    print("Test 03:", longest_streak(a))  # Expected: 2

    # Test 04:
    a = Node(4)
    print("Test 04:", longest_streak(a))  # Expected: 1

    # Test 05:
    print("Test 05:", longest_streak(None))  # Expected: 0

if __name__ == "__main__":
    run_tests()

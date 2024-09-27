'''
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should
return the total sum of all values in the linked list.
'''
from Linked_List import Node
def sum_list(head):
    
    sum = 0
    while head is not None:
        sum += head.val
        head = head.next
    return sum

    '''  
    #Recursive  
    if head is None:
        return 0
    return head.val + sum_list(head.next)
    '''

def run_tests():
    # Test 00:
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    # 2 -> 8 -> 3 -> -1 -> 7
    print("Test 00:", sum_list(a)) 
    # Expected -> 19

    # Test 01:
    x = Node(38)
    y = Node(4)
    x.next = y
    # 38 -> 4
    print("Test 01:", sum_list(x)) 
    # Expected -> 42

    # Test 02:
    z = Node(100)
    # 100
    print("Test 02:", sum_list(z)) 
    # Expected -> 100

    # Test 03:
    print("Test 03:", sum_list(None)) 
    # Expected -> 0

if __name__ == "__main__":
    run_tests()

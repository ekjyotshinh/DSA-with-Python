'''
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing
elements that are in both of the two lists.
You may assume that each input list does not contain duplicate elements.
'''
def intersection(a, b):
    # use a set for a faster lookup time
    # n = len of a and m = len of b
    # Time - O(max(n,m))
    # Space - O(n) result in an array
    result = []
    a_set = set()
    for a_num in a:
        a_set.add(a_num)
        # can also
        # a_set = set(a)

    for b_num in b:
        if b_num in a_set:
            result.append(b_num)
    return result
    '''
    # n = len of a and m = len of b
    # Time - O(n*m)
    # Space - O(min(n,m)) result in an array
    res = []
    for a_num in a:
        for b_num in b:
            if a_num == b_num:
                res.append(a_num)
    return res
    '''

def run_tests():
    print("Test 00:", intersection([1, 2, 3], [3, 4, 5]))  # -> [3]
    print("Test 01:", intersection([10, 20, 30], [30, 40, 50]))  # -> [30]
    print("Test 02:", intersection([1, 2, 3], [4, 5, 6]))  # -> []
    print("Test 03:", intersection(['a', 'b', 'c'], ['b', 'c', 'd']))  # -> ['b', 'c']
    print("Test 04:", intersection([7, 8, 9, 10], [10, 11, 12, 7]))  # -> [7, 10]
    print("Test 05:", intersection([], [1, 2, 3]))  # -> [] (empty input list)

if __name__ == "__main__":
    run_tests()

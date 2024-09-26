# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups
# according to the pattern in tests cases
# input format number string but the number can be multiple digits like 100x
# two pointer to figure out the number and then the charater 

#time complexity
#   n = number of groups
#   m = max number of any group
#   time = O(n*m)
#   space = O(n*m)
def uncompress(s):
    # using two pointers
    numbers = '0123456789'  # used to check it a character is a number
    results = []
    i, j = 0, 0
    #i is at the start of the number
    #j is the char that follows the number
    while (j < len(s)):
        if(s[j] not in numbers): # numbers in constant
            times = int(s[i:j]) # we extract the numerical component , j not included but i is included
            for t in range(times):
                results.append(s[j])
            j += 1
            i = j
        else:
            j += 1
    return ''.join(results)

def run_tests():
    print("Test 00:", uncompress("2c3a1t"))  # -> 'ccaaat'
    print("Test 01:", uncompress("4s2b"))    # -> 'ssssbb'
    print("Test 02:", uncompress("2p1o5p"))  # -> 'ppoppppp'
    print("Test 03:", uncompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'

if __name__ == "__main__":
    run_tests()

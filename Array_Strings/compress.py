# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where
# consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character
# occurrences should not be changed.

# two pointers
# i represents the start of a same character and j represents the start of next charater
def compress(s):
    s+='!'  # for the last elememt so that s[i] and s[j] are differnet and j does not go out of bounds
    result = []
    i, j = 0, 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            times = j-i
            if(times == 1):
                result.append(s[i])
            else:
                result.append(str(times) + s[i])
            i = j
    return ''.join(result)



def run_tests():
    print("Test 00:", compress("ccaaat"))  # -> '2c3at'
    print("Test 01:", compress("ssssbb"))  # -> '4s2b'
    print("Test 02:", compress("ppoppppp"))  # -> '2po5p'
    print("Test 03:", compress("nnneeeeeeeeeeeezz"))  # -> '3n12e2z'
    print("Test 04:", compress("abc"))  # -> 'abc' (no change for single occurrences)
    print("Test 05:", compress("aabbcc"))  # -> '2a2b2c'
    print("Test 06:", compress("a"))  # -> 'a' (single character string)
    print("Test 07:", compress("aaaabbbcc"))  # -> '4a3b2c'

if __name__ == "__main__":
    run_tests()

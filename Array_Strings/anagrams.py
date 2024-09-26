#Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not
#the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# 
#   n = length of string 1
#   m = length of string 2
#   Time: O(n + m)
#   Space: O(n + m)

def anagrams(s1, s2):
    # Use hashmap for python we use dictionaries
    #we store the char and the number of times it appears

    if(len(s1) != len(s2)):
        return False
    
    return char_count(s1)  == char_count(s2)

# use a helper funtion to make a hashmap for the strings
def char_count(s):
    count = {}  #creating a dict
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

def run_tests():
    print("Test 00:", anagrams('restful', 'fluster'))  # -> True
    print("Test 01:", anagrams('cats', 'tocs'))  # -> False
    print("Test 02:", anagrams('monkeyswrite', 'newyorktimes'))  # -> True
    print("Test 03:", anagrams('paper', 'reapa'))  # -> False
    print("Test 04:", anagrams('elbow', 'below'))  # -> True
    print("Test 05:", anagrams('tax', 'taxi'))  # -> False
    print("Test 06:", anagrams('taxi', 'tax'))  # -> False
    print("Test 07:", anagrams('night', 'thing'))  # -> True
    print("Test 08:", anagrams('abbc', 'aabc'))  # -> False

if __name__ == "__main__":
    run_tests()

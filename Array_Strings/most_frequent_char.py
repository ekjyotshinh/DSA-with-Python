# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character
# of the string. 
# If there are ties, return the character that appears earlier in the string.
# You can assume that the input string is non-empty.

#time complexity
#time O(n)
# space O(n)
def most_frequent_char(s):
    count = {}
    for char in s:
        if(char in count):
            count[char]+=1  #incrementing it
        else:
            count[char] = 1 # initializing it
        
    most_recent_frequent = s[0]#inititalizing the most frequent value that is also the most recent
    # for tie breaking logic
    for char in s:
        if(count[most_recent_frequent] < count[char]):
            most_recent_frequent = char
    
    return most_recent_frequent

def run_tests():
    print("Test 00:", most_frequent_char('bookeeper'))  # -> 'e'
    print("Test 01:", most_frequent_char('david'))      # -> 'd'
    print("Test 02:", most_frequent_char('abby'))       # -> 'b'
    print("Test 03:", most_frequent_char('mississippi')) # -> 'i'
    print("Test 04:", most_frequent_char('potato'))     # -> 'o'
    print("Test 05:", most_frequent_char('eleventennine')) # -> 'e'
    print("Test 06:", most_frequent_char('riverbed'))   # -> 'r'

if __name__ == "__main__":
    run_tests()

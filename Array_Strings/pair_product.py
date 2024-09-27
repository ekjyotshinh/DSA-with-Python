'''
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple
containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.
Be sure to return the indices, not the elements themselves.
There is guaranteed to be one such pair whose product is the target.
'''


def pair_product(numbers, target):
 # use a hashmap and map the complement(target/number[i]) to the index of this item 
    previous_nums = {}
    for index,num in enumerate(numbers):
        complement = target/num
        if complement in previous_nums:
            return (previous_nums[complement],index)
        else:
            previous_nums[num] = index

'''
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] * numbers[j] == target:
                return (i,j)
'''

def run_tests():
    print("Test 00:", pair_product([3, 2, 5, 4, 1], 8))    # -> (1, 3)
    print("Test 01:", pair_product([3, 2, 5, 4, 1], 15))   # -> (0, 2)
    print("Test 02:", pair_product([4, 7, 9, 2, 5, 1], 10)) # -> (3, 4)
    print("Test 03:", pair_product([1, 6, 7, 2], 14))      # -> (2, 3)
    print("Test 04:", pair_product([9, 9], 81))            # -> (0, 1)
    print("Test 05:", pair_product([6, 4, 2, 8], 48))      # -> (0, 3)

if __name__ == "__main__":
    run_tests()

''' Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a
pair of indices whose elements sum to the given target. The indices returned must be unique.
Be sure to return the indices, not the elements themselves.
There is guaranteed to be one such pair that sums to the target.'''



def pair_sum(numbers, target):
    '''
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] + numbers[j] == target:
                return (i,j)
    '''
# use a hashmap and map the complement(target-number[i]) to the index of this item 

    previous_nums = {}
    for index,num in enumerate(numbers):
        complement = target-num
        if complement in previous_nums:
            return (previous_nums[complement],index)
        else:
            previous_nums[num] = index

def run_tests():
    print("Test 00:", pair_sum([3, 2, 5, 4, 1], 8))    # -> (0, 2)
    print("Test 01:", pair_sum([4, 7, 9, 2, 5, 1], 5))  # -> (0, 5)
    print("Test 02:", pair_sum([4, 7, 9, 2, 5, 1], 3))  # -> (3, 5)
    print("Test 03:", pair_sum([1, 6, 7, 2], 13))       # -> (1, 2)
    print("Test 04:", pair_sum([9, 9], 18))             # -> (0, 1)
    print("Test 05:", pair_sum([6, 4, 2, 8], 12))       # -> (1, 3)

if __name__ == "__main__":
    run_tests()

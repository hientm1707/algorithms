



def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two number such that the add up to a specific target
    """
    indices = {}
    for i, num in enumerate(nums):
        if target - num in indices:
           return i, indices[target - num]
        indices[num] = i
    return -1

def two_sum_duplicates(nums, target):
    """
    Two sum for printing all pairs that adds up to the target
    Yeah we print out the elements, not the indices, cuz indices cannot be duplicated
    Avoid cases like 4 7 4, target = 11
    """
    indices = {}
    pairs = set()
    for i, num in enumerate(nums):
        if target - num in indices:
            pairs.add(tuple(sorted(([num, target - num]))))
        indices[num] = i
    return pairs
    


#Testing code

lst = [1,2,2, 7,8,9,11,215]
nums = [3, 4, 2, 1, 5, 6, 7, 4]

def test():
    first = two_sum(lst, target=13)
    second = two_sum_duplicates(nums, target=7)
    print(first, second)
    
test()
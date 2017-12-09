'''Codefights Interview practice - Hash Tables - "containsCloseNums"'''
def containsCloseNums(nums, k):
    '''containsCloseNums(list, number) -> boolean\n
    Given an array of integers nums and an integer k, determine whether there are
    two distinct indices i and j in the array where nums[i] = nums[j] and the
    absolute difference between i and j is less than or equal to k.'''
    dictionary = {}
    for i, num in enumerate(nums):
        try:
            # previous index - current index <= constant distance?
            if abs(dictionary[num] - i) <= k:
                return True
            dictionary[num] = i
        except KeyError:
            dictionary[num] = i
    return False

NUMS = [0, 1, 2, 3, 5, 2]
K = 3
print(containsCloseNums(NUMS, K)) # True

NUMS = [0, 2, 4, 3, 5, 4]
K = 2
print(containsCloseNums(NUMS, K)) # False

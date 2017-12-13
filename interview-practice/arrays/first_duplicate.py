'''Codefights interview practice - Arrays - "firstDuplicate"'''
def firstDuplicate(array):
    '''firstDuplicate(array) -> element\n
    Return the first duplicate element'''
    dictionary = {}
    for num in array:
        try:
            return dictionary[num]
        except KeyError:
            dictionary[num] = num
    return -1


print(firstDuplicate([2, 3, 3, 1, 5, 2])) # 3
print(firstDuplicate([2, 4, 3, 5, 1])) # -1
print(firstDuplicate([1, 2, 3, 5, 9, 6, 7, 2, 6])) # 2

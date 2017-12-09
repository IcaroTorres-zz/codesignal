'''Codefights Interview practice - Hash Tables - "areFollowingPatters"'''
def areFollowingPatterns(strings, patterns):
    '''areFollowingPatterns(list, list) -> boolean\n
    Return if first given string list is following the "repetition" pattern sugested
    on second given string list'''
    return all(patterns.index(p) == strings.index(s) for s, p in zip(strings, patterns))

#if you are not very familiar with python list comprehension bellow there is the simple version
''' for s,p in zip(string, patters):
        if patterns.index(p) != strings.index(s):
            return False  # If any case of difference between the indices the pattern are broken

    return True  # following patterns if no occurrence of differences
'''
STRINGS = ["cat", "dog", "dog"]
PATTERNS = ["a", "b", "b"]
print(areFollowingPatterns(STRINGS, PATTERNS)) # True

STRINGS = ["cat", "dog", "doggy"]
PATTERNS = ["a", "b", "b"]
print(areFollowingPatterns(STRINGS, PATTERNS)) # False

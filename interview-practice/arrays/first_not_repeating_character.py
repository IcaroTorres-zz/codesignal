'''Codefights interview practice - Arrays - "firstNotRepeatingCharacter"'''
def firstNotRepeatingCharacter(_str):
    '''firstNotRepeatingCharacter(str) -> char\n
    Given a string s, find and return the first instance of a non-repeating
    character in it. If there is no such character, return '_'.'''
    chars = [c for c in _str if _str.index(c) == _str.rindex(c)]
    return "_" if chars == [] else chars[0]


print(firstNotRepeatingCharacter("abacabad"))
print(firstNotRepeatingCharacter("abacabaabacaba"))

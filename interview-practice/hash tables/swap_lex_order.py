'''Codefights interview practice - Hash Tables - "swapLexOrder"'''
def swapLexOrder(string, pairs):
    '''swapLexOrder(str, [[a1, b1], [a2, b2],...]) -> str\n
    Given a string str and array of pairs that indicates which indices
    in the string can be swapped, return the lexicographically largest string
    that results from doing the allowed swaps. You can swap indices any number of times.'''
    length, _str = len(string), list(string)
    sets = [set() for x in range(length)] # a starting list of empty sets for each possible indices
    base = set()
    for a, b in pairs: # 1-based indices a and b
        sets[a - 1].add(b - 1)
        sets[b - 1].add(a - 1)
        base.add(a - 1)
        base.add(b - 1)
    while base:
        curr = {base.pop()}
        tmp = set()
        while curr:
            tmp |= curr
            base -= curr
            curr = {y for x in curr for y in sets[x] if y in base}
        replaces = sorted((_str[i] for i in tmp), reverse=True) # mount decreasing ordered replaces
        for i in sorted(tmp): # update chars -> lexicographically larger
            _str[i] = replaces.pop(0)

    return "".join(_str)

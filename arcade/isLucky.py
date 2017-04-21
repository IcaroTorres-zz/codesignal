# beatiful way
def isLucky(n):
    prev = sum ([ int(i) for i in str(n)[:len(str(n))/2] ])
    nxt  = sum ([ int(i) for i in str(n)[len(str(n))/2:] ])
    return prev==nxt

# ugly way
'''
def isLucky(n):
    for half_1,half_2 in zip(s[:size/2],s[(size/2):]):
        result1 += int(half_1)
        result2 += int(half_2)
    return result1==result2
'''

n = 1230
print isLucky(n)
n = 239017
print isLucky(n)

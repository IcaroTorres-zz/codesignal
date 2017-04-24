# Given some integer, find the maximal number you can obtain by deleting
# exactly one digit of the given number.
def deleteDigit(n):
    # iterate on str(n), do a list removing one character from str(n+0) each
    # time to dont destroy the original str(n), keeping it with the same value
    # till the end of iteration. return the max(list[int(parts of str(n+0))])
    return max([int(str(n+0).replace(i,'',1)) for i in str(n)])

print deleteDigit(10092)

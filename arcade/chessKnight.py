# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# mathematic mode
def chessKnight(cell):

    c,i,j = 0, 'abcdefgh'.index(cell[0]), int(cell[1])-1

    # this sum will return the count of occurrences satisfying all conditions.
    # abs(ni*nj)==2 restrict to one pair of elements with absolute product ==2
    # [-2,-1],[-2,1],[2,1],[2,-1],[-1,-2],[-1,2],[1,2],[1,-2]
    # corresponding to the changes to test by all movements.
    # 0 <= i + ni < 8 test if the new values for lines 'i' are inside the board.
    # 0 <= j + nj < 8 do the same above for columns 'j'.
    # xrange turn able to iterate values inside a negative to positive interval.
    # was used a for loop inside another one for loop, to test all coluns and lines
    for ni in xrange(-2,3):
        for nj in xrange(-2,3):
            if abs(ni*nj)==2 and 0<= i+ni <8 and 0<= j+nj <8:
                c+=1
    return c

# mathematic mode with list comprehension
def chessKnight2(cell):
    i,j = 'abcdefgh'.index(cell[0]), int(cell[1]) - 1

    return sum( 0 <= i + ni < 8 and 0 <= j + nj < 8 and abs(ni * nj) == 2 for ni in xrange(-2, 3) for nj in xrange(-2, 3) )

# manual mode
def chessKnight1(cell):
    r=0
    i, j = 'abcdefgh'.index(cell[0]), int(cell[1]) - 1
    if (i+2)<8 and (j+1)<8:
        r+=1
    if (i+2)<8 and (j-1)>=0:
        r+=1
    if (i-2)>=0 and (j+1)<8:
        r+=1
    if (i-2)>=0 and (j-1)>=0:
        r+=1
    if (i+1)<8 and (j+2)<8:
        r+=1
    if (i+1)<8 and (j-2)>=0:
        r+=1
    if (i-1)>=0 and (j+2)<8:
        r+=1
    if (i-1)>=0 and (j-2)>=0:
        r+=1
    return r



print chessKnight("a1")
print chessKnight2("a1")

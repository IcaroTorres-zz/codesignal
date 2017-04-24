# given an array, return the maximum difference between 2 adjacent valuesin it
def arrayMaximalAdjacentDifference(inputArray):
    dif = 0
    # walking by 2 parts of same list simuntaneosly taking 2 elements at once
    for i,j in zip(inputArray[:-1],inputArray[1:]):
        if i!=j:
            d = abs(i-j) #if not equal take the absolute difference
            if dif < d:
                dif = d # if the new difference is bigger keep this
    return dif

# print arrayMaximalAdjacentDifference([1,5,4,6,7,8,9,2,3,4,0,9,0])

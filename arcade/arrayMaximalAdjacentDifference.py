def arrayMaximalAdjacentDifference(inputArray):
    k=inputArray
    dif = 0
    for i,j in zip(k[:-1],k[1:]):
        if i!=j:
            d = abs(i-j)
            if dif < d:
                dif = d
    return dif

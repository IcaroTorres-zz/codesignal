def matrixElementsSum(matrix):
    sum = 0
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if (matrix[i][j] == 0):
                pass
            elif (i>0) and (i-1 >= 0) and (matrix[i-1][j] == 0):
                matrix[i][j] = 0
            else:
                sum = sum + matrix[i][j]
                print 'result',matrix[i][j]
    return sum

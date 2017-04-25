def spiralNumbers(n):
    # an empty matrix build
    matrix=[]
    for i in range(0,n): # line dimension 'n'
        field = []
        for j in range(0,n): # column dimension 'n'
            field.append(' ') #dummy empty char cell
        matrix.append(field) # line added filled with 'dummy'

    i,j=0,0 # indices to reach inside matrix
    cellValue=1 # value to be assigned inside matrix
    right,down,left,up=1,1,1,1 # matrix boundary limiters
    direction='right' # direction of next assignment


    while cellValue<=n*n: # cellValue to assign <= the number of cells 'n*n'

        matrix[i][j] = cellValue # start the loop with assign
        # after assignment check conditions of matrix
        # and change direction,limiters and indices if needed
        if direction=='right':
            j+=1
            if j==n-right: # reached the right limiter
                direction='down' # change to down
                right+=1 # increase the right limiter
        elif direction=='down':
            i+=1
            if i==n-down: # reached the down limiter
                direction='left' # change to left
                down+=1 # increase the down limiter
        elif direction=='left':
            j-=1
            if j==-1+left: # reached the left limiter
                direction='up' # change to up
                left+=1 # increase the left limiter
        else:
            i-=1
            if i==-0+up: # reached the left limiter
                direction='right' # change to up
                up+=1 # increase the left limiter
        cellValue+=1
    return matrix

print spiralNumbers(3)
'''
    [[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]
'''

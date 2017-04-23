def diagonals(matrix,i,j):
    affected=[]

    for k in range (1,min(8-i,8-j)):
        affected.append(matrix[i+k][j+k])

    for k in range (1,min(i+1,j+1)):
        affected.append(matrix[i-k][j-k])

    for k in range (1,min(8-i,j+1)):
        affected.append(matrix[i+k][j-k])

    for k in range (1,min(i+1,8-j)):
        affected.append(matrix[i-k][j+k])

    return affected

def bishopAndPawn(bishop, pawn):
    board={}
    matrix=[]
    for i,lin in enumerate([8,7,6,5,4,3,2,1]):
        line=[]
        for j,colum in enumerate(['a','b','c','d','e','f','g','h']):
            board[colum+str(lin)]=[i,j]
            line.append(colum+str(lin))
        matrix.append(line)

    if bishop.lower() in board.keys():
        if pawn.lower() in board.keys():
            affected = diagonals(matrix,board[bishop][0],board[bishop][1])

            if matrix[ board[pawn][0] ] [ board[pawn][1] ] in affected:
                return True
            else:
                return False

    return False
print bishopAndPawn('a8','c3')

def sudoku(grid):
    l=list(range(1,10))
    def checkInnerGrids(x,y):
        return sorted([grid[i][j]for i in range(x,x+3) for j in range(y,y+3)])==l

    def checkLinesColumns(i):
        return sorted(grid[i])==l and sorted([grid[x][i] for x in range(9)])==l

    for i in range(0,9,3):
        for j in range(0,9,3):
            if not checkInnerGrids(i,j):
                return False
    for i in range(9):
        if not checkLinesColumns(i):
            return False
    return True

'''Codefights interview practice - Arrays - "sudoku2"'''
def sudoku2(grid):
    '''sudoku2(matriz 9x9) -> boolean\n
    Sudoku is a number-placement puzzle. The objective is to fill a 9 x 9 grid with numbers
    in such a way that each column, each row, and each of the nine 3 x 3 sub-grids that compose
    the grid all contain all of the numbers from 1 to 9 one time.\n
    Return if a given strutured sudoku grid with empty and filled cells still can be a playable
    sudoku grid with no repeatitions'''
    def check_inner_grids(x, y):
        '''check_inner_grids(int, int) -> boolean\n
        Given x line and y column of a grid (matriz indices) representing a inner square grid 3x3,
        return if all elements does not repeat and are a valid playable grid, or if some value
        repeats and makes it a invalid sudoku grid'''
        #if sets length == lists length -> nothing repeats
        a = [grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3) if grid[i][j] != '.']
        b = set([grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3) if grid[i][j] != '.'])
        return len(a) == len(b)

    def check_lines_columns(i):
        '''check_lines_columns(int) -> boolean\n
        Given indice 'i' representing lines and columns in a square grid 3x3,
        return if all elements does not repeat and are a valid playable line and
        column, or if some value repeats and makes it a invalid sudoku grid.'''
        #if sets length == lists length -> nothing repeats
        a = set(j for j in grid[i] if j != '.')
        b = [j for j in grid[i] if j != '.']
        c = set([grid[x][i] for x in range(9) if grid[x][i] != '.'])
        d = [grid[x][i] for x in range(9) if grid[x][i] != '.']
        return len(a) == len(b) and len(c) == len(d)

    # iterate the grid by 3 at once
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_inner_grids(i, j):
                return False
    for i in range(9):
        if not check_lines_columns(i):
            return False

    return True

GRID1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

GRID2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
         ['7', '1', '.', '.', '7', '5', '.', '.', '.'], # 7 repeats this line
         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
         ['.', '.', '.', '.', '.', '2', '.', '.', '.'], # 2 repeats on sub-grid 8 [[6:8] [3:5]]
         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

print(sudoku2(GRID1)) # True
print(sudoku2(GRID2)) # False

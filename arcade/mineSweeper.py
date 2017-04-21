def blank_expanded(matrix):
    temp = []
    n_lentgth = len(matrix[0])+2
    blank_line = [False for nl in range (n_lentgth)]
    temp.append(blank_line)
    for i in matrix:
        temp.append([False]+i+[False])
    temp.append(blank_line)
    return temp

def minesweeper(matrix):
    swepper=[]
    expanded = blank_expanded(matrix)

    for level in range(len(matrix)):
        line = []
        for col in range(len(matrix[level])):
            first_line  = expanded[level][col:col+3]
            second_line = expanded[level+1][col:col+1] + expanded[level+1][col+2:col+3]
            third_line = expanded[level+2][col:col+3]
            cel = sum( cel ==True for cel in first_line) + sum(cel ==True for cel in second_line) + sum (cel ==True for cel in third_line)
            line.append(cel)
        swepper.append(line)
    return swepper



matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print minesweeper(matrix)

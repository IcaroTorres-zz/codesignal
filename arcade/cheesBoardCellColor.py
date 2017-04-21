def chessBoardCellColor(cell1, cell2):
    #lines and cols
    line1,col1 = int(cell1[1]),cell1[0]
    line2,col2 = int(cell2[1]),cell2[0]

    #a dict translating cols to numbers like the lines
    aux = {v:k+1 for k,v in enumerate("ABCDEFGH")}

    #little function to find color by line and col
    def color(line,col):
        # if both line and col is odd or even ==1 else ==-1
        return 1 if (line%2 !=0 and aux[col]%2!=0) or (line%2 ==0 and aux[col]%2==0) else -1

    return color(line1,col1) == color(line2,col2)

print chessBoardCellColor("A1", "C3")

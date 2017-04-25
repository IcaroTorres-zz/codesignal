# to find the number of differentSquares inside a matrix 2x2
def differentSquares(m):

    l=[] # creat a empty list to keep the squares found
    # range len(m)-1 to check current and next index in 'i' and 'j'
    for i in range (len(m)-1):
        for j in range (len(m[i])-1):
            # concatenate each cell value in a string
            s=''
            s+=str(m[i][j])
            s+=str(m[i][j+1])
            s+=str(m[i+1][j])
            s+=str(m[i+1][j+1])
            l.append(s) # put the resulting string inside the list
    # cause we have string values inside the list, we can use set() to hash it
    return  len(set(l))

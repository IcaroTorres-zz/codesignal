'''Codefights interview practice - Arrays - "retateImage"'''
def rotateImage(matriz):
    '''retateImage([2D matriz n*n]) -> rotated [2D matriz n*n]\n
    Given an n x n 2D matrix that represents an image,
    rotate the image by 90 degrees (clockwise).'''
    length = len(matriz)
    image = [['-'] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            image[j][length - (1 + i)] = matriz[i][j]

    return image

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(rotateImage(M))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(rotateImage(M))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

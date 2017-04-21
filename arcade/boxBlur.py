def boxBlur(image):
    final = []
    for level in range(len(image)-1):
        if level -1 >=0 and level +1 <=len(image):
            pixel_list = []
            for col in range(len(image[level])-1):
                if col -1 >=0 and col +1 <= len(image[level]):
                    pixel = sum( image[level-1][col-1:col+2]) + sum(image[level][col-1:col+2]) + sum (image[level+1][col-1:col+2] )
                    pixel = pixel /9
                    print pixel
                    pixel_list.append(pixel)
                    print pixel_list
            print final
            final.append(pixel_list)
            print final
    return final




boxBlur([[36,0,18,9],
 [27,54,9,0],
 [81,63,72,45]])

boxBlur([[7,4,0,1],
 [5,6,2,2],
 [6,10,7,8],
 [1,4,2,0]])

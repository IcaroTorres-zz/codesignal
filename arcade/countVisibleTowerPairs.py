# -*- coding: utf-8 -*-
'''
Define a tower as a straight vertical segment with a bottom end on the X axis.

Consider some towers in pairwise distinct positions. A pair of towers is called visible if the segment that connects the top points of those towers doesn't cross any other tower (but may touch the tops of some towers).

Given positions on which the towers stand and heights of the towers, find the number of visible pairs of towers.

Example

For position = [3, 0, 6, 10] and height = [2, 1, 4, 6], the output should be
countVisibleTowerPairs(position, height) = 5.

Let's number towers from left to right, starting with 1, then these 5 tower pairs will be visible: (0, 1), (0, 2), (0, 3), (1, 2), (2, 3).

Check out the image below to see for yourself:
'''

def countVisibleTowerPairs(position, height):
    #sorted list of towers
    pairs = []
    towers = sorted([[p,h] for p,h in zip(position,height)])
    limit = 0
    threshold = 0


    for i in range(len(towers)-1):
        height_i = towers[i][1]
        position_i = towers[i][0]

        for j in range(i+1,len(towers)):
            if i!=j:
                height_j = towers[j][1]
                position_j = towers[j][0]
                p_dist = abs(position_i*1.0 -position_j*1.0)
                h_dist = abs(height_i*1.0 - height_j*1.0)

                #consecutives
                if abs(j-i)==1:
                    pairs.append([towers[i],towers[j]])
                    limit = height_j
                    threshold = p_dist*1.0/h_dist

                #not consecutives
                #both bigger than limit
                elif height_j>=limit and height_i >= limit:
                    pairs.append([towers[i],towers[j]])
                    limit = height_j
                    threshold = p_dist*1.0/h_dist

                elif height_j<limit and height_i <limit:
                    pass
                elif p_dist*1.0/h_dist <=threshold:
                        pairs.append([i,j])
                        threshold = p_dist*1.0/h_dist
                        limit = max(height_j,limit)

        threshold = 0
    s = []
    for i in pairs:
        if i not in s:
            s.append(i)

    return len(s)



position= [10, -5, 20, -10, 15, 23]
height= [100, 50, 102, 20, 73, 89]
print countVisibleTowerPairs(position,height)

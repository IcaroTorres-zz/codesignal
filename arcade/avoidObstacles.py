# given an array of integers representing the position of obstacles in a straigh
# line starting in '0', find the minimum size of the jump in cells needed to
# avoid all obstacles.
# 0 _ _ 3 _ 5 6 _ _ 9 _ ...

def avoidObstacles(array):
    # to solve this, the secret lies in division with rest. (mod or %)
    # there is no need to sort the input array

    i = 1 #this variable will keep the mod divisor (our jumpsize)

    while True: # we don't know the this loop size. so it will be a 'while'

        found = True # turn this variable as True, changing if we colide

        # for each obstacle
        for k in range (len(array)):
            # this print will help to see the process
            print "i = %s ob = %s mod = %s"%(i,k,array[k],array[k]%i)

            # %i==0 means colision with an obstacle using the jump size == i
            if array[k]%i==0:
                found = False #if we colide with some one, we do not found yet

        '''
        do the same as above
        F = [False if array[k]%i==0 else True for k in range (len(array))]
        found = False if False in F else True
        '''
        
        # %i !=0 to all obstacles means we have found the perfect jump
        # cause obstacles are before or after our jump, not in this way
        if found:
            return i # just return it

        # after all we increase the mod divisor, it means jumpsize
        i+=1

def avoidObstacles2(array):
    i = 1
    while True:
        F = [False if array[k]%i==0 else True for k in range (len(array))]
        if not False in F:
            return i
        i+=1

print avoidObstacles2([5,3,6,7,9])
print avoidObstacles2([2,3,6,7,9,13,16,21])

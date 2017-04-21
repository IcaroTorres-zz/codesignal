def avoidObstacles(inputArray):
    i = 1
    while True:
        found = True
        for k in range (len(inputArray)):
            if inputArray[k]%i==0:
                found = False
        if found:
            return i
        i+=1

print avoidObstacles([5,3,6,7,9])
print avoidObstacles([2,3,6,7,9,13,16,21])

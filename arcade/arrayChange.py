
def dif_inputArray(inputArray,i,count):
    count += (inputArray[i]+1)-inputArray[i+1]
    inputArray[i+1]= inputArray[i]+1
    return count

def arrayChange(inputArray):
    count = 0
    return (sum(dif_inputArray(inputArray,i,count) for i in range (len(inputArray)-1) if inputArray[i]>=inputArray[i+1]))

print arrayChange([1,1,1,1,1,1,2,6,5,4,8,2,3])

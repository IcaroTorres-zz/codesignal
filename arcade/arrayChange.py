# given an array of integers, only adding a value in an index of your choice by
# 1 each time. what is the minimum number of moves needed to make this array
# stricktly increasing?

def diff(inp,i,count):
    count += (inp[i]+1)-inp[i+1] # count of moves is increased by (a+1-b)
    inp[i+1]= inp[i]+1 # the next value will be the previous value + 1
    return count

def arrayChange(inp):
    count = 0 # count of moves
    # sum of moves needed passing by the array only once
    return (sum(diff(inp,i,count) for i in range (len(inp)-1) if inp[i]>=inp[i+1]))

print arrayChange([1,1,1,1,1,1,2,6,5,4,8,2,3])

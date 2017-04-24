# find the max sum value between kth consecutive values in an array
def arrayMaxConsecutiveSum(inputArray, k):
    # result starts in 0
    r = 0
    #sum the firsts kth elements except the last
    s = sum( inputArray[i] for i in range (k-1))

    # this loop pass only once per value. with a good complexity O=n
    # walk this loop finishing the sum of previous kth elements, then compare
    # this sum 's' to the 'r' we already got (starting with 0). if 's' is bigger
    # than 'r', it takes value of 's'. then decrease 's' by value of the first
    # in the last sum made previously.
    for i in range ( k-1,len (inputArray)):
        s += inputArray[i]
        if s > r:
            r = s
        s -= inputArray[i - k + 1]
        # like (3+2+4->9),(9-3->6 | 2+4),(2+4+1 -> 7),(7-2 ->5 | 4+1) ...
    return r

    # this list comprehension do the same with worst complexity
    # return max([sum(inputArray[i:i+k]) for i in range (len(inputArray)-k+1) ])

inputArray=[2, 3, 5, 1, 6]
k=2
print arrayMaxConsecutiveSum(inputArray,k)


##JS
'''
function arrayMaxConsecutiveSum(inputArray, k){
    var s = 0;

    for (var i =0; i < (inputArray.length) - (k-1); i++ ){
        var arr=[]
        var total=0;
        Object.assign(arr,inputArray);
        arr = arr.splice(i,k);
        console.log (arr);


        for(var j in arr) { total +=parseInt(arr[j]); }
        console.log(total);
        if (s < total ){
            s = total;
        }
    }
    return s

}
'''

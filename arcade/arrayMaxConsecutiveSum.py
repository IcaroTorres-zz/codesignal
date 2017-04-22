def arrayMaxConsecutiveSum(inputArray, k):
    r = 0
    s = sum( inputArray[i] for i in range (k-1))
    for i in range ( k-1,len (inputArray)):
        s += inputArray[i]
        if s > r:
            r = s
        s -= inputArray[i - k + 1]
    return r
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

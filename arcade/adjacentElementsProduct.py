def adjacentElementsProduct(inputArray):
    return max([inputArray[i]*inputArray[i+1] for i in range (0, len(inputArray)-1)])

'''
#JS
function adjacentElementsProduct(inputArray) {
    product = null
    for (i=0; i< inputArray.length-1;i++){
        if (product == null || product < inputArray[i]*inputArray[i+1])
            product = inputArray[i]*inputArray[i+1]
    }
    return product
}

#CS
int adjacentElementsProduct(int[] inputArray) {
    int product = inputArray[0]*inputArray[1];
    for (int i =0; i < inputArray.Length-1; i++){
        if (product < inputArray[i]*inputArray[i+1])
            product = inputArray[i]*inputArray[i+1];
    }
    return product;
}

#JAVA

int adjacentElementsProduct(int[] inputArray) {
    int product = inputArray[0]*inputArray[1];
    for (int i =0; i < inputArray.length-1; i++){
        if (product < inputArray[i]*inputArray[i+1])
            product = inputArray[i]*inputArray[i+1];
    }
    return product;
}
'''

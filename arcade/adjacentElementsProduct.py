# return bigger product of adjacent array elements
def adjacentElementsProduct(array):
    # simply walk all elements, with this comprehension. and return max(list)
    return max([array[i]*array[i+1] for i in range (len(array)-1)])

'''
#JS
function adjacentElementsProduct(array) {
    product = null
    for (i=0; i< array.length-1;i++){
        if (product == null || product < array[i]*array[i+1])
            product = array[i]*array[i+1]
    }
    return product
}

#CS
int adjacentElementsProduct(int[] array) {
    int product = array[0]*array[1];
    for (int i =0; i < array.Length-1; i++){
        if (product < array[i]*array[i+1])
            product = array[i]*array[i+1];
    }
    return product;
}

#JAVA

int adjacentElementsProduct(int[] array) {
    int product = array[0]*array[1];
    for (int i =0; i < array.length-1; i++){
        if (product < array[i]*array[i+1])
            product = array[i]*array[i+1];
    }
    return product;
}
'''

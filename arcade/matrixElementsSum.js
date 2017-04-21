function matrixElementsSum(matrix) {
    var sum = 0;
    for (var i = 0; i <matrix.length;i++){
        for (var j = 0; j <matrix[i].length;j++){
            if (matrix[i][j] == 0)
                continue;
            else if ((i>0) && (i-1 >= 0) && (matrix[i-1][j] == 0))
                matrix[i][j] = 0;
            else
                sum = sum + matrix[i][j];
        }
    }
    return sum;
}

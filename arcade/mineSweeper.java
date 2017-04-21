int[][] minesweeper(boolean[][] matrix) {
    int rowLen = matrix.length;
    int colLen = matrix[0].length;

    int[][] result = new int[rowLen][colLen];

    for(int i = 0; i < rowLen; i++) {
        for(int j = 0; j < colLen; j++) {
            int value = 0;

            // top left
            value += i-1 >= 0 && j-1 >= 0 && matrix[i-1][j-1] ?
                1 : 0;

            // top mid
            value += i-1 >= 0 && matrix[i-1][j] ?
                1 : 0;

            // top right
            value += i-1 >= 0 && j+1 < colLen && matrix[i-1][j+1] ?
                1 : 0;

            // left
            value += j-1 >= 0 && matrix[i][j-1] ?
                1 : 0;

            // right
            value += j+1 < colLen && matrix[i][j+1] ?
                1 : 0;

            // bottom left
            value += i+1 < rowLen && j-1 >= 0 && matrix[i+1][j-1] ?
                1 : 0;

            // bottom mid
            value += i+1 < rowLen && matrix[i+1][j] ?
                1 : 0;

            // bottom right
            value += i+1<rowLen && j+1<colLen && matrix[i+1][j+1] ?
                1 : 0;

            result[i][j] = value;
        }
    }

    return result;

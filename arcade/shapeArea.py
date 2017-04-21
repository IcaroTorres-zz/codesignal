def shapeArea(n):
    area = 1
    for i in range (1,n+1):
        part = i-1
        area = area + (4 * part)
    return area

'''
#JS
function shapeArea(n) {
    var area = 1;
    for (var i=1; i< n+1; i++){
        var part = i-1;
        area = area + (4 * part);
    }
    return area;
}

#CS
int shapeArea(int n) {
    int area = 1;
    for (int i=1; i< n+1; i++){
        int part = i-1;
        area = area + (4 * part);
    }
    return area;
}

#JAVA
int shapeArea(int n) {
    int area = 1;
    for (int i=1; i< n+1; i++){
        int part = i-1;
        area = area + (4 * part);
    }
    return area;
}

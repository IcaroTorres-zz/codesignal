function countVisibleTowerPairs(position, height) {
    var result = 0;
    for (var i = 0; i < position.length; i++) {
        for (var j = i + 1; j < position.length; j++) {
            var A = Math.abs(height[j] - height[i]),
                B = Math.abs(position[i] - position[j]),
                C = A / B,
                visible = true;
            for (var k = 0; k < position.length; k++) {
                if ((A * position[k] + B * height[k] + C) * C < 0) {
                    visible = false;
                }
            }
            if (visible) {
                result++;
            }
        }
    }
    return result;
}

var position= [10, -5, 20, -10, 15, 23]
var height= [100, 50, 102, 20, 73, 89]
countVisibleTowerPairs(position,height)

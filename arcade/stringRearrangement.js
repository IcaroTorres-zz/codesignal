function stringsRearrangement(inputArray) {
  var bruteForce = function(depth, inputArray) {
    var swap = function(i, j) {
      tmp = inputArray[i];
      inputArray[i] = inputArray[j];
      inputArray[j] = tmp;
    };
    if (depth === inputArray.length) {
      for (var i = 0; i < inputArray.length - 1; i++) {
        var differences = 0;
        for (var j = 0; j < inputArray[i].length; j++) {
          if (inputArray[i][j] !== inputArray[i + 1][j]) {
            differences++;
          }
        }
        if (differences !== 1) {
          return false;
        }
      }
      return true;
    }
    for (var i = depth; i < inputArray.length; i++) {
      swap(depth, i);
      if (bruteForce(depth + 1, inputArray)) {
        return true;
      }
      swap(depth, i);

    return false;
  };

  return bruteForce(0, inputArray);
}
console.log(stringsRearrangement(["f", "g", "a",
 "h"]));

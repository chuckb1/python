function rotateArray(arr, shiftBy) {
    var lastItem = arr[arr.length - 1]
    for(var i = 0; i < arr.length; i++) {
        arr[i +1] = arr[i];
        console.log(arr);
    
    }
    arr[0] = lastItem;
    return arr;
}
console.log(rotateArray([1,2,3,4,5], 1) == [5,1,2,3,4]);
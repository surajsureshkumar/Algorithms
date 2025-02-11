function binarySearch(arr, target){
    var low = 0
    var high = arr.length -1

    while (low < high){
        let middle = Math.floor((low + high) / 2);

        if ( arr[middle] === target){
            return middle;
        } else if (arr[middle] < target){
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }
    return -1;
}
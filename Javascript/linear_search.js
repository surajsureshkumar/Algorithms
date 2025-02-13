function LinearSearch(){
    let target = 3
    let array = [1,2,3,4,5,6,7,8];

    for(let idx = 0; idx < array.length; idx++){
        if (array[idx] == target){
            return idx;
        }
    }
    return -1
}

foundValue = LinearSearch();
console.log(foundValue)
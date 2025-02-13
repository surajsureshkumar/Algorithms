function InsertionSort(){
    let array = [2,6,5,1,4,3];

    for(let idx = 1; idx < array.length; idx++){
        let currentElement = array[idx];
        let previousElement = idx - 1;

        while (previousElement >=0 && array[previousElement] > currentElement) {
            array[previousElement + 1] = array[previousElement];
            previousElement -= 1;
        }

        array[previousElement + 1] = currentElement;
    }

    return array
}

let sortedArray = InsertionSort()
console.log(sortedArray)
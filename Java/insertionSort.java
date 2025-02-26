import java.util.Arrays;

class InsertionSort{

    static int[] insertionSort(int [] array){
        for(int idx = 0; idx < array.length; idx++){
            int currentElement = array[idx];
            int previousElement = idx - 1;

            while(previousElement >=0 && array[previousElement] > currentElement){
                array[previousElement + 1] = array[previousElement];
                previousElement --;
            }
            array[previousElement + 1] = currentElement;
        }
        return array;
    }

    public static void main(String[] args) {
        int [] array = {38,25,21,26,28};
        InsertionSort.insertionSort(array);
        System.out.println("Sorted Array is "+ Arrays.toString(array));

    }
}
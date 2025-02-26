import java.util.Arrays;

class MergeSort {
    
    public static void divide(int [] array){
        if (array.length <= 1){
            return;
        }
        int middle = (array.length) / 2;
        int [] leftHalf = new int[middle];
        int [] rightHalf = new int[array.length - middle];
        
        for(int idx = 0; idx < middle; idx ++){
            leftHalf[idx] = array[idx];
        }   
        for(int idx = middle; idx < array.length; idx ++){
            rightHalf[idx - middle] = array[idx];
        } 

        divide(leftHalf);
        divide(rightHalf);

       merge(array, leftHalf, rightHalf);
    }

    public static void merge(int[] array, int [] leftArray, int [] rightArray){
        int leftPointer = 0;
        int rightPointer = 0;
        int idx = 0;

        while (leftPointer < leftArray.length && rightPointer < rightArray.length){
            if(leftArray[leftPointer] < rightArray[rightPointer]){
                array[idx] = leftArray[leftPointer];
                leftPointer ++;
            } else{
                array[idx] = rightArray[rightPointer];
                rightPointer++;
            }
            idx++;
        }

        while (leftPointer < leftArray.length){
            array[idx] = leftArray[leftPointer];
            idx++; leftPointer++;
        }

        while (rightPointer < rightArray.length){
            array[idx] = rightArray[rightPointer];
            idx++; rightPointer++;
        }
    }
    
    public static void main(String[] args) {
        int [] array = {38,25,21,26,28};    
        MergeSort.divide(array);
        System.out.println("Sorted Array is " + Arrays.toString(array));
    }
}
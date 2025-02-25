public class BinarySearch{

    int binarySearch(int [] array, int target, int low, int high){
        while (low <= high){
            int middle = (low + high) / 2;

            if (array[middle] == target){
                return middle;
            } else if( array[middle] > target){
                high = middle - 1;
            } else{
                low = middle + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args){
        BinarySearch obj = new BinarySearch();
        int [] array = {1,2,3,4,5,6,7,8,9};
        int arrayLength = array.length - 1;
        int target = 8;

        int valueIndex = obj.binarySearch(array, target, 0, arrayLength);
        if(valueIndex != -1){
            System.out.println("Value found at index" + valueIndex);
        } else {
            System.out.printlnt("Value not found and element not present");
        }
    }
}
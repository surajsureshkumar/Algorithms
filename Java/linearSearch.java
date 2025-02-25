public class LinearSearch{

    int linearSearch(int [] array, int target, int arrayLength){
        for (int idx = 0; idx < arrayLength; idx++){
            if (array[idx] == target){
                return idx;
            }
        }
        return -1;
    }
    
    public static void main(String[] args){
        int [] array = {1,2,3,4,5,6,6,7}
        int arrayLength = array.length;
        LinearSearch obj = new LinearSearch();
        int target = 5;

        int valueFoundAtIndex = obj.linearSearch(array, target, arrayLength);

        if (valueFoundAtIndex != -1){
            System.out.println("Value found at index" + valueFoundAtIndex);
        } else{
            System.out.println("Value not found and might not be present in the array");
        }
    }
}
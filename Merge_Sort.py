class MergeSort():
    """OOP + functional implementation of MergeSort Algorithm"""
    def __init__(self, array: list):
        """Constructor

        Args:
            array (list): constructor
        """
        self.array = array

    def divide(self, array: list) -> list:
        """Function to find the middle index and divide the array into two halves

        Args:
            array (list): unsorted input array

        Returns:
            list: one representing the left half and the the other right half of the array
        """
        middle = len(array) // 2

        left_half = array[:middle]
        right_half = array[middle:]

        return left_half, right_half
    
    def merge(self, left_half_of_the_array: list, right_half_of_the_array: list) -> list:
        """Merge function to merge the two sorted lists

        Args:
            left_half_of_the_array (list): array holding all the sorted left elements
            right_half_of_the_array (list): array holding all the sorted right elements

        Returns:
            list: _description_
        """
        merged_array = [] # array to store the final result
        
        left_index, right_index = 0, 0 # two pointers to iterate through the two halves

        # iterate till you reach the end of either of the list
        while left_index < len(left_half_of_the_array) and right_index < len(right_half_of_the_array):
            # if the element on the left side is smaller than the element of the right side then append the smaller element to the merged array and increment the pointer of the left half
            if left_half_of_the_array[left_index] < right_half_of_the_array[right_index]:
                merged_array.append(left_half_of_the_array[left_index])
                left_index += 1
            # else is the reverse of the above if condition
            else:
                merged_array.append(right_half_of_the_array[right_index])
                right_index += 1
        
        # once we have reached the end of one list, the other list might still be unprocessed, so we will have to append all the remaining elements of the respective half, this needs to be done for the right and left half
        # separately, as any of the pointer can reach the end of the array

        while left_index < len(left_half_of_the_array):
            merged_array.append(left_half_of_the_array[left_index])
            left_index += 1
        
        while right_index < len(right_half_of_the_array):
            merged_array.append(right_half_of_the_array[right_index])
            right_index += 1

        return merged_array

    def sort(self, array:list) -> list:
        """recursive function that calls the divide to recusively divide the array and merge method to return the final sorted array

        Args:
            array (list): _description_

        Returns:
            list: _description_
        """
        # base case 
        if len(array) <= 1:
            return array
        
        left_half, right_half = self.divide(array) # dividing the array into two halves

        sorted_left_half = self.sort(left_half) # recusive division of the array into smaller chunks
        sorted_right_half = self.sort(right_half)

        final_result = self.merge(sorted_left_half, sorted_right_half)

        return final_result

def main():
    """main method, tweak the array according to your need, unit tests can be added by importing the unittest and declaring a new class to write tests"""
    array = [38, 27, 43, 3, 9, 82, 10]
    merge_sort = MergeSort([])
    sorted_array = merge_sort.sort(array)
    print(sorted_array)

if __name__ == "__main__":
    main()
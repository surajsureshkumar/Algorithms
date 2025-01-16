import unittest

class BinarySearch:
    """Implementation of the BinarySearch Algorithm"""
    def __init__(self, array: list):
        self.array = sorted(array)

    def search(self, target_value: int) -> int:
        """_summary_
        This function searches for the target value in a sorted array which is the core component of the binary search algorithm

        Args:
            array (list): data type containing numbers in ascending order
            target (int): value to be found in the array

        Returns:
            int value which is the index of the target element
        """
        lowest_index_number_of_the_array = 0
        highest_index_number_of_the_array = len(self.array) - 1

        while lowest_index_number_of_the_array <= highest_index_number_of_the_array:
            middle_index = ((lowest_index_number_of_the_array + highest_index_number_of_the_array)//2)
            if self.array[middle_index] == target_value:
                return middle_index
            elif self.array[middle_index] > target_value:
                lowest_index_number_of_the_array = middle_index + 1
            else:
                highest_index_number_of_the_array += middle_index - 1

        return -1

# uncomment the below lines for unit test cases 
# class BinarySearchTest(unittest.TestCase):
#     def setUp(self):
#         self.array = [1,2,3,4,5,6,7,8,10]
#         self.binary_search = BinarySearch(self.array)

#     def test_value_found(self):
#         self.assertEqual(self.binary_search.search(4), 3)
#         self.assertEqual(self.binary_search.search(1), 0)

#     def test_empty_array(self):
#         empty_binary_search = BinarySearch([])
#         self.assertEqual(empty_binary_search.search(1), -1)

#     def test_for_single_element(self):
#         single_element = BinarySearch([7])
#         self.assertEqual(single_element.search(7), 0)
    
#     def test_for_large_value(self):
#         large_array = list(range(1000))
#         large_value_binary_search = BinarySearch(large_array)
#         self.assertEqual(large_value_binary_search.search(500), 500)

#     def test_for_duplicate_elements_in_array(self):
#         duplicates_array = [1,2,2,3,4,5]
#         duplicates_binary_search = BinarySearch(duplicates_array)
#         self.assertEqual(duplicates_binary_search.search(2), [1,2])

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    # Uncomment these lines if you want to accept user input
    # user_input = input('Enter a sorted array ( comma separated )')
    # target_value = input("Enter a target value to search in the entered array")
    sorted_array = [1,3,5,7,9,11,13,15]
    target_value = 9
    binary_search = BinarySearch(sorted_array)
    index_of_number = binary_search.search(target_value)

    if index_of_number != -1:
        print(f'Target value {target_value} found at {index_of_number}')
    else:
        print(f'Target value {target_value} not found')

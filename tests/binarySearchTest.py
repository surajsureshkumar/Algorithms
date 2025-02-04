import unittest

from Binary_Search import BinarySearch;
class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.array = [1,2,3,4,5,6,7,8,10]
        self.binary_search = BinarySearch(self.array)

    def test_value_found(self):
        self.assertEqual(self.binary_search.search(4), 3)
        self.assertEqual(self.binary_search.search(1), 0)

    def test_empty_array(self):
        empty_binary_search = BinarySearch([])
        self.assertEqual(empty_binary_search.search(1), -1)

    def test_for_single_element(self):
        single_element = BinarySearch([7])
        self.assertEqual(single_element.search(7), 0)
    
    def test_for_large_value(self):
        large_array = list(range(1000))
        large_value_binary_search = BinarySearch(large_array)
        self.assertEqual(large_value_binary_search.search(500), 500)

    def test_for_duplicate_elements_in_array(self):
        duplicates_array = [1,2,2,3,4,5]
        duplicates_binary_search = BinarySearch(duplicates_array)
        self.assertEqual(duplicates_binary_search.search(2), [1,2])

if __name__ == "__main__":
    unittest.main()
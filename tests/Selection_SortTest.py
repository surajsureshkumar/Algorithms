import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Selection_Sort import SelectionSort

class Test(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.unsorted_array = [3, 5, 7, 56, 33, 2]
        self.empty_array = []
        self.single_element_array = [1]
        self.sorted_array = [1,2,3,4,5]

    def test_unsorted_array(self):
        expected_result = [2, 3, 5, 7, 33, 56]
        algo = SelectionSort(self.unsorted_array)
        self.assertEqual(algo.selection_sort(), expected_result)

    def test_empty_array(self):
        expected_result = []
        algo = SelectionSort(self.empty_array)
        self.assertEqual(algo.selection_sort(), expected_result)

    def test_single_element_array(self):
        expected_result = [1]
        algo = SelectionSort(self.single_element_array)
        self.assertEqual(algo.selection_sort(), expected_result)

    def test_sorted_array(self):
        expected_result = [1,2,3,4,5]
        algo = SelectionSort(self.sorted_array)
        self.assertEqual(algo.selection_sort(), expected_result)

if __name__ == "__main__":
    unittest.main()
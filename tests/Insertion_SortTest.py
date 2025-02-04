import unittest
from pathlib import Path
import sys

current_directory = Path(__file__).resolve().parent
parent_directory = current_directory.parent
sys.path.append(str(parent_directory))

from Insertion_Sort import InsertionSort


class Tests(unittest.TestCase):
    def test_case_unsorted_array(self, arr: list) -> list:
        self.arr = [2,5,1,3,4]
        sort = InsertionSort(self.arr)
        self.assertEqual(sort.insertion_sort(), [1,2,3,4,5])

    def test_case_sorted_array(self, arr: list) -> list:
        self.arr = [10,11,12,13,14,15]
        sort = InsertionSort(self.arr)
        self.assertEqual(sort.insertion_sort(self.arr), [10,11,12,13,14,15])
    
    def test_case_empty_array(self, arr:list) -> list:
        self.arr = []
        sort = InsertionSort(self.arr)
        self.assertEqual(sort.insertion_sort(self.arr), [])
    
    def test_case_array_contains_duplicates(self, arr:list) -> list:
        self.arr = [4,3,2,1,1,1]
        sort = InsertionSort(self.arr)
        self.assertEqual(sort.insertion_sort(self.arr), [1,1,1,2,3,4])

    
if __name__ == "__main__":
    unittest.main()
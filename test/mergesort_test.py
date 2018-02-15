
import sys
sys.path.append('..')

import unittest
from sorting.MergeSort import MergeSort

class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.to_sort = [5, 2, 4, 6, 1, 3]
        self.arr_empty = []
        self.one_elemet = [1]

    def testing_sort(self):
        merge_sort = MergeSort(self.to_sort)
        self.assertEqual(merge_sort.sort(), [1, 2, 3, 4, 5, 6])
     
    def testing_empty(self):
        merge_sort = MergeSort(self.arr_empty)
        self.assertEqual(merge_sort.sort(), [])

    def testing_one(self):
        merge_sort = MergeSort(self.one_elemet)
        self.assertEqual(merge_sort.sort(), [1])

if __name__ == "__main__":
    unittest.main()

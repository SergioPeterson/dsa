
import sys
sys.path.append('..')

import unittest
from sorting.BubbleSort import BubbleSort

class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.to_sort = [5, 2, 4, 6, 1, 3]
        self.arr_empty = []
        self.one_elemet = [1]

    def testing_sort(self):
        bubble_sort = BubbleSort(self.to_sort)
        self.assertEqual(bubble_sort.sort(), [1, 2, 3, 4, 5, 6])
     
    def testing_empty(self):
        bubble_sort = BubbleSort(self.arr_empty)
        self.assertEqual(bubble_sort.sort(), [])

    def testing_one(self):
        bubble_sort = BubbleSort(self.one_elemet)
        self.assertEqual(bubble_sort.sort(), [1])

if __name__ == "__main__":
    unittest.main()

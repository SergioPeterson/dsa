
import sys
sys.path.append('..')

import unittest
from sorting.InsertionSort import InsertionSort

class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.to_sort = [3, 4, 1, 2]
    
    def testing_sort(self):
        insertion_sort = InsertionSort(self.to_sort)
        self.assertEqual(insertion_sort.sort(), [1, 2, 3, 4])
        
if __name__ == "__main__":
    unittest.main()

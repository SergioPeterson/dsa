import unittest
from Bst import *

class TestBst(unittest.TestCase):
    

    def setUp(self):
        self.bst = Bst()
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.insert(4)
        self.bst.insert(21)
        self.bst.insert(15)

    def testing_inorder(self):
        self.assertEqual(self.bst.inorder(), [4, 5, 6, 15, 21])

    def testing_search_1(self):
        self.assertNotEqual(self.bst.search(10)._key, 10)

    def testing_search_2(self):
        self.assertEqual(self.bst.search(2)._key, None)

    def testing_min_max(self):
        self.assertEqual(self.bst.minimum()._key, 4)
        self.assertEqual(self.bst.maximum()._key, 21)

    def testing_successor_predecessor(self):
        self.assertEqual(self.bst.successor(6)._key, 15)
        self.assertEqual(self.bst.predecessor(6)._key, 5)

    def testing_deleting(self):
        self.assertEqual(self.bst.delete(42)._key, None)
        self.bst.delete(15)
        self.assertEqual(self.bst.inorder(), [4, 5, 6, 21])


if __name__ == "__main__":
    unittest.main()

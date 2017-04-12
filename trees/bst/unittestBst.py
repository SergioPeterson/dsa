import unittest
from Bst import *

class TestBst(unittest.TestCase):

    def setUp(self):
        pass

    def testing_inorder(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(21)
        bst.insert(15)
        self.assertEqual(bst.inorder(), [4, 5, 6, 15, 21])

    def testing_search_1(self):
        bst = Bst()
        bst.insert(11)
        bst.insert(10)
        bst.insert(12)
        self.assertEqual(bst.search(10)._key, 10)

    def testing_search_2(self):
        bst = Bst()
        bst.insert(11)
        bst.insert(10)
        bst.insert(12)
        self.assertEqual(bst.search(2)._key, None)

    def testing_min_max(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(21)
        bst.insert(15)
        self.assertEqual(bst.minimum()._key, 4)
        self.assertEqual(bst.maximum()._key, 21)

    def testing_successor_predecessor(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(21)
        bst.insert(15)
        self.assertEqual(bst.successor(6)._key, 15)
        self.assertEqual(bst.predecessor(6)._key, 5)

    def testing_deleting(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(21)
        bst.insert(15)
        self.assertEqual(bst.delete(42)._key, None)
        bst.delete(15)
        self.assertEqual(bst.inorder(), [4, 5, 15, 21])


if __name__ == "__main__":
    unittest.main()

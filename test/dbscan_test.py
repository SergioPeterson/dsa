import sys
sys.path.append('..')

import unittest
from cluster.dbscan.Point import Point
from cluster.dbscan.DBScan import DBScan

class TestDBScan(unittest.TestCase):

    def setUp(self):
        p1 = Point(-4, 4)
        p2 = Point(-3, 1)
        p3 = Point(-1, 2)
        p4 = Point(0, 0)
        p5 = Point(1, 1)
        p6 = Point(2, 2)
        p7 = Point(3, 4)
        p8 = Point(5, 6)
        p9 = Point(3, 8)
        p10 = Point(-2, -4)
        points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        self._dbscan = DBScan(points, 2.5, 2)
    
    def testing_dbscan(self):
        for p in self._dbscan.get_points():
            print(p.get_values()," = ", p.get_cluster())
        self.assertEqual(len(self._dbscan.get_points()), 10) 

if __name__ == "__main__":
    unittest.main()

import sys
sys.path.append('..')

import unittest
from graphs.Graph import Graph
from graphs.ConnectedComponent import ConnectedComponent

class TestCC(unittest.TestCase):
    
    def setUp(self):
        self.G = Graph(6) 
        self.G.add_edge(1, 2)
        self.G.add_edge(1, 3)
        self.G.add_edge(1, 4)
        self.G.add_edge(2, 4)
        self.G.add_edge(3, 4)
        self.G.add_edge(0, 5)

    def testing_path_to(self):
        cc = ConnectedComponent(self.G)
        self.assertEqual(cc.len(), 2)

if __name__ == "__main__":
    unittest.main()

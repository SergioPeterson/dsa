import sys
sys.path.append('..')

import unittest
from graphs.Graph import Graph

class TestGraph(unittest.TestCase):
    
    
    def setUp(self):
        self.G = Graph(5) 
        self.G.add_edge(1, 2)
        self.G.add_edge(1, 3)
        self.G.add_edge(1, 4)
        self.G.add_edge(2, 4)
        self.G.add_edge(3, 4)
    
    def testing_len(self):
        self.assertEqual(self.G.len(), 5)

    
    def testing_nodes_adjacents(self):
        self.assertEqual(self.G[4], [1, 2, 3])
        self.assertEqual(self.G[2], [1, 4])
        self.assertEqual(self.G[0], [])
    
    def testing_degree(self):    
        self.assertEqual(self.G.degree(4), 3)
        self.assertEqual(self.G.max_degree(), 3)

if __name__ == "__main__":
    unittest.main()

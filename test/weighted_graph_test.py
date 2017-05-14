import sys
sys.path.append('..')

import unittest
from graphs.WeightedGraph import WeightedGraph

class WeightedGraphTest(unittest.TestCase):
    
    
    def setUp(self):
        self.G = WeightedGraph(6) 
        self.G.add_edge(0, 1, 1)
        self.G.add_edge(0, 2, 4)
        self.G.add_edge(0, 3, 1)
        self.G.add_edge(0, 4, 3)
        self.G.add_edge(0, 5, 3)
        self.G.add_edge(1, 2, 2)
        self.G.add_edge(1, 4, 4)
        self.G.add_edge(2, 3, 2)
        self.G.add_edge(3, 4, 4)
        self.G.add_edge(3, 5, 5)
        self.G.add_edge(4, 5, 3)
    
    def testing_len(self):
        self.assertEqual(self.G.len(), 6)
 
    def testing_nodes_adjacents(self):
        self.assertEqual(self.G[4], [0, 1, 3, 5])
        self.assertEqual(self.G[2], [0, 1, 3])
        self.assertEqual(self.G[0], [1, 2, 3, 4, 5])  

    def testing_weights(self):
        self.assertEqual(self.G.get_edges(0)[0].get_weight(), 1)
        self.assertEqual(self.G.get_edges(0)[1].get_weight(), 4)
        self.assertEqual(self.G.get_edges(0)[2].get_weight(), 1)
        self.assertEqual(self.G.get_edges(0)[3].get_weight(), 3)
        self.assertEqual(self.G.get_edges(0)[4].get_weight(), 3)

if __name__ == "__main__":
    unittest.main()

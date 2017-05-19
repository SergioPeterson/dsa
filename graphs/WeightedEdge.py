
class WeightedEdge:

    def __init__(self, v, w, weight = 0):
        """
        Initializes a new weighted edge, with v and w
        
        Args:
            param1: v is the first vertice
            param2: w is the second vertice
            param3: weight is the value between them 
        
        """
        self._weight = weight
        self._v = v
        self._w = w
    
    def get_weight(self):
        """
        Magic method that returns the weight of the edge
        """
        return self._weight

    def get_vertices(self):
        """
        Returns the two vertices associated with that edge
        """
        return [self._v, self._w]

# WeightedEdge.py

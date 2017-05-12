
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
    
    def __getitem__(self):
        """
        Magic method that returns the weight of the edge

        Args:
            param1: v is the correspondent vertice
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        
        try:
            return self._weight
        except (TypeError, IndexError):
            pass

    def get_vertices(self):
        return [self._v, self._w]

# WeightedEdge.py

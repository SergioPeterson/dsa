
#
# Author: Luis Alves
#

class Graph:

    def __init__(self, V):
        """
        Constructor responsible to initialize the Graph structure
        # Graph based on 0-index array (e.g Graph(3) == V{0, 1, 2})

        Args:
            param1: V is the number of vertices of the Graph
        
        Raises:
            TypeError: V is not an integer
        """
        
        try:
            self._V = V # better dealing with index
            self._adj = [[] for i in range(self._V)]
        except TypeError:
            pass

    def __getitem__(self, v):
        """
        Magic method that return the list of adjacent vertices of v

        Args:
            param1: v is the correspondent vertice
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        
        try:
            self._adj[v]
        except (TypeError, IndexError):
            pass
        finally:
            return self._adj[v]

    def add_edge(self, v, w):
        """
        Method responsible for adding an edge in an undirected style

        Args:
            param1: v is the first vertice
            param2: w is the second vertice
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        
        try:
            self._adj[v]
            self._adj[w]
        except (TypeError, IndexError):
            pass
        finally:
            self._adj[v].append(w)
            self._adj[w].append(v)

    def degree(self, v):
        """
        Method responsible for returning the degree of the vertice,
        # of edges connected to that vertice

        Args:
            param1: v is the correspondent vertice
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        
        try:
            self._adj[v]
        except (TypeError, IndexError):
            pass
        finally:
            return len(self._adj[v])

    def max_degree(self):
        """
        Method responsible for returning the vertices that has
        the highest degree
        """

        max = 0
        for v in self._adj:
            if len(v) > max:
                max = len(v)
        return max

    def len(self):
        """
        Method responsible for returning the length (# of vertices)
        """
        return self._V


# Graph.py

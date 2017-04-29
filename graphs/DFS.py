import Graph

class DFS:

    def __init__(self, graph, s):   
        """
        Constructor responsible to initialize the DFS structure

        Args:
            param1: The whole graph to be explored using DFS
            param2: s is the initial node where DFS starts
        
        Raises:
            TypeError: s is not an integer
        """ 
        try:
            self._marked = [False for i in range(0, graph.len())]
            self._edge_to = [None for i in range(0, graph.len())]
            self._S = s # start node
            self._dfs(graph, s)
        except TypeError:
            pass

    def _dfs(self, graph, v):
        """
        DFS algorithm itself
        """
        try:
            self._marked[v] = True
            for w in graph[v]:  
                if not self._marked[w]:
                    self._dfs(graph, w)
                    self._edge_to[w] = v
        except (TypeError, IndexError):
            pass

    def has_path_to(self, graph, v):
        """
        Check if v has a path to the initial node passed in the constructor

        Args:
            param1: The whole graph to be explored using DFS
            param2: v is the node to be checked
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        try:
            w = self._edge_to[v]
            while w is not None:
                if w == self._S:
                    return True
                w = self._edge_to[w]
            return False
        except (TypeError, IndexError):
            pass

    def path_to(self, graph, v):
        """
        Returns the path from v to the initial node as a list

        Args:
            param1: The whole graph to be explored using DFS
            param2: v is the node used to calculate the path
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """ 
        try:
            path = [v]
            if self.has_path_to(graph, v):
                w = self._edge_to[v]
                while w is not self._S:
                    path.append(w)
                    w = self._edge_to[w]
                path.append(self._S)
            else:
                return None
        except (TypeError, IndexError):
            pass
        return path

# DFS.py

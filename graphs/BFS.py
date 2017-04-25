
import Graph

class BFS:

    def __init__(self, graph, s):   
        
        try:
            self._marked = [False for i in range(0, graph.len())]
            self._edge_to = [None for i in range(0, graph.len())]
            self._S = s # start node
            self._bfs(graph, s)
        except TypeError:
            pass

    def _bfs(self, graph, v):

        try:
            visited = [v]
            self._marked[v] = True
            while len(visited) !=  0:
                recent_vertex = visited.pop(0)
                for w in graph[recent_vertex]:
                    if self._marked[w] is not True: 
                        visited.append(w)
                        self._marked[w] = True
                        self._edge_to[w] = recent_vertex
        except (TypeError, IndexError):
            pass

    def has_path_to(self, graph, v):
        
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
            return path
        except (TypeError, IndexError):
            pass

# BFS.py

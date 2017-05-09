
class ConnectedComponent:
    
    def __init__(self, graph):
        """
        Constructor responsible to initilize the Connected Componets

        Args:
            param1: The whole graph to be explored using DFS

        Raises:
            TypeError: graph is not appropriate
        """
        try:
            self._visited = [False for i in range(0, graph.len())]
            self._count = 0

            for i in range(0, graph.len()):
                if self._visited[i] is not True and len(graph[i]) is not 0:
                    self._dfs(graph, i)
                    self._count = self._count + 1
        except TypeError:
            pass

    def _dfs(self, graph, v):
        """
        DFS algorithm itself
        """
        try:
            self._visited[v] = True
            for w in graph[v]:
                if not self._visited[w]:
                    self._dfs(graph, w)
        
        except (TypeError, IndexError):
            pass

    def len(self):
        """
        Method responsible for returning the length (# of CC)
        """
        return self._count

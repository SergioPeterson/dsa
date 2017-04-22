import sys
sys.path.append('..')

from Graph import Graph
from DFS import DFS

def main():
    G = Graph(6) 
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(0, 5)

    dfs = DFS(G, 4)
    print("Path from 1-4")
    print(dfs.path_to(G, 1))
    print(dfs.has_path_to(G, 1))    
     
    print("Path from 2-4")
    print(dfs.path_to(G, 2))
    print(dfs.has_path_to(G, 2))
   
    print("Path from 0-4")
    print(dfs.path_to(G, 0))
    print(dfs.has_path_to(G, 0))

if __name__ == "__main__":
    main()

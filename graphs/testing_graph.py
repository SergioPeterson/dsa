from Graph import Graph

def main():
    G = Graph(5) 
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    
    print(G[2])
    print(G[4])
    #print(G[6])
    #print(G["a"])
    print(G.degree(4))
    print(G.max_degree())

if __name__ == "__main__":
    main()

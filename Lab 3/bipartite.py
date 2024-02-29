def dfs (node , graph , visited ):
    if node in visited :
        return True


    visited.add(node)
    print(node,visited,graph.colour)
    col = graph.colour[node]
    for x in graph.list[node]:
        if graph.colour[x]== -1:
            graph.colour[x]= not col
        elif graph.colour[x] == col :
            return False
        if x not in visited:
            if (dfs(x , graph, visited)==False):
                return False
    return  True




def is_bipartite ( graph ):
    visited = set()

    for i in range (graph.size):
        if i not in visited :
            graph.colour[i] = True
            if (dfs(i , graph , visited)==False ):
                
                print("Graph is not bipartite")
                return False
    return True

if __name__== "__main__" :
    g= graph(5)
    g.list={
        0:[1] ,
        1:[2],
        2:[3],
        3:[4],
        4:[0]

    }
    print(is_bipartite(g))

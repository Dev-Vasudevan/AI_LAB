class graph :
    def __init__(self , n ):
        graph.size = n
        graph.mat =[[0*n] for _ in range (n)]
        graph.list = {}
def cycle_starter ( graph ):
    visited = set()
    for i in range (graph.size):
        if i not in visited :
            if (cycle_catcher(i,graph,visited,[])):
                return True

    return False




def cycle_catcher ( node , graph , visited , path):
    if node  in visited:
        return

    visited.add(node)

    flag=True
    path.append(node)
    for des in graph.list[node]:


        if des in path :
            print(path + [des])
            return True
        if des not in visited:
            flag = False

            if (cycle_catcher ( des , graph , visited , path)):
                return True
    if path and flag :
        path.pop()

    return False

if __name__== "__main__" :
    g= graph(6)
    g.list={
        0:[1] ,
        1:[],
        2:[1,3],
        3:[4],
        4:[5],
        5:[3]

    }
    print(cycle_starter(g))







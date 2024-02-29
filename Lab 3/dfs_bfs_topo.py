
class graph:
    def __init__(self,n):
        self.mat=[[0*n]for _ in range (n)]
        self.list = {}
        self.size = n




def dfs (graph):
    stack=[]
    visited=set()
    pop_order = []
    for  node in range(graph.size-1,0,-1):
        if node not in visited:
            # visited.add(node)
            stack.append(node)
            # stack.append(5)
            # visited.add(5)

            while ( stack ):
                if stack[-1] in visited:
                    pop_order.append(stack[-1])
                    stack.pop()
                    continue
                # print("HI")
                print(stack[-1],end=" ")
                des = set(graph.list[stack[-1]])-visited

                visited.add(stack[-1])
                if not visited:
                    pop_order.append(stack[-1])

                    stack.pop()
                    continue
                for x in des:
                    stack.append(x)
    print(" \n Topo sort is : " ,end = "" )
    return pop_order[::-1]

def bfs (graph ):
    queue = [ ]
    visited = []
    for i in range(graph.size-1,0,-1):
        if i not in visited :
            queue.append(i)
            while ( queue ):
                node = queue.pop(0)
                if node in visited :
                    continue

                visited.append(node)

                des =list( set(graph.list[node]).difference( set(visited)))
                queue+=des
    
    return visited


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = graph(6)
    g.list = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [2, 0]}
  
    print(dfs(g))
    print(type(g.list[0]))
    a={1,2,3}
    b={2,3,4}
    print(bfs(g))

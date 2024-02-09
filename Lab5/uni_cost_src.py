class graph:
    def __init__(self,n):
        self.list={}
        self.mat=[[0 for x in range (n)] for _ in range (n)]
        self.size=n

    def create_mat (self):
        for node in self.list:
            for des,wt in self.list[node]:
                self.mat[node][des]=wt

    def add_edge(self, src , des):
        self.list[src]=des

    def display(self):
        print(self.mat)
        print(self.list)



def uni_cost(g):
    pri_queue=[(0,0)]
    # nodes=g.list[0]
    visited=[]
    curr_cost = 0

    while (len(visited)<= g.size):
        print(pri_queue)
        nodes=pri_queue.pop(0)
        visited.append(nodes[0])
        # curr_cost+=nodes[1]
        print(nodes)

        for node,_ in g.list[nodes[0]]:
            if node in visited:
                continue
            pri_queue.append((node , _ +nodes[1]))
        pri_queue.sort(key= lambda x:x[1])

    return nodes[1]

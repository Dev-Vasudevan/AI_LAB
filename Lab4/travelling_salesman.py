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



def Tsp(g ):

    queue = [([i],0) for i in range (g.size)]



    while len(queue)>1 and len(queue[0][0])<=g.size+1  :

        path,wt=queue.pop(0)
        # path=wt_path[0]
        # wt=wt_path[1]
        if (len(path))== g.size :
            cost = g.mat[path[-1]][path[0]]
            item=(path+[path[0]] , cost +wt)
            queue.append(item)
            queue.sort(key= lambda x:x[1])
            continue


        if  g.list[path[-1]]==[[]]:
            continue

        for des,cost in g.list[path[-1]]:
            if des in path:
                continue
            item=(path+[des] , cost +wt)

            queue.append(item)
        queue.sort(key= lambda x:x[1])
    print(queue[0][0])
    return wt

g=graph(4)

g.list=({0:((1,2),(2,3),(3,1)) , 1:((0,2),(2,4),(3,2))  , 2:((0,3),(1,4),(3,3)) , 3:((0,1),(1,2),(2,3))})
g.create_mat()
print(Tsp(g))

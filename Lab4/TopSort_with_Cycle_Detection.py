
class graph:
    def __init__(self,n):
        self.list={}
        self.mat=[[0 for x in range (n)] for _ in range (n)]
        self.size=n

    def create_mat (self):
        for node in self.list:
            for des in self.list[node]:
                self.mat[node][des]=1

    def add_edge(self, src , des):
        self.list[src]=des

    def display(self):
        print(self.mat)
        print(self.list)


    def in_degree(self):
        pri_queue = []
        for i in range(g.size):
            in_degree = 0
            for j in range(g.size):
                if g.mat[j][i]:
                    in_degree += 1
            pri_queue.append([i, in_degree])

        pri_queue.sort(key=lambda x: x[1] )
        return pri_queue
def topo_sort(g):

    pri_q=g.in_degree()
    topo_sorted=[]
    while len((pri_q)):

        node = pri_q.pop(0)
        if (node[1] != 0):
            print("Cycle Exists")
            return -1

        node=node[0]
        topo_sorted.append(node)
        des = g.list[node]
        temp=[]
        for x in des:
            for index in (pri_q):

                if index[0] == x :
                    pri_q.remove(index)
                    index[1]-=1
                    temp.append(index)
        pri_q=pri_q+temp
        pri_q.sort(key=lambda x:x[1] )

    return topo_sorted
g=graph(6)
g2=graph(4)
g2.list={0:[1,2] , 1:[2] , 2:[0,3] , 3:[3] }
g2.create_mat()

g.list={0:[] , 1:[] , 2:[3] , 3:[1] , 4:[0,1], 5:[2,0]}
print(topo_sort(g2))

g.create_mat()
print(topo_sort(g))



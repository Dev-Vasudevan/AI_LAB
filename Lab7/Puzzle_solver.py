

def eval( mat ):
    hue=0
    for i in range (3) :
        for j in range (3):
            if mat[i][j] != goal[i][j]:
                hue +=1
    return hue

def create_mat ( dic ):
    mat = [[0 for _ in range(3)] for __ in range(3)]
    for key,ind in dic.items :
        mat[ind[0]][ind[1]]=key

    return mat

def find_zero (mat ):

    for i in range (3):
        for j in range (3):
            if mat[i][j]==0:
                return ((i,j))

def move( mat , i , j , new_i, new_j):

    new_mat = list(map(list,mat))
    new_mat[new_i][new_j]=mat[i][j]
    new_mat[i][j]=mat[new_i][new_j]
    return tuple(map(tuple,new_mat))

def path (previous , current):
    path=[]
    while current != [[]]:
        path.append(current)
        current=previous[current]
    return path[::-1]

def display(path):
    for puzzle in path :
        for row in puzzle:
            print(row)
        print("\n")
def astar(graph):
    pri_queue = []
    previous = {}
    visited = set()

    print(type(graph))
    pri_queue.append((graph,[[]] , eval(graph)))


    while pri_queue:
        pri_queue.sort(key = lambda x:x[2])
        current,prev,cost = pri_queue.pop(0)
        if current in visited:
            continue
        previous[current]=prev
        visited.add(current)
        i,j= find_zero(current)

        if eval(current)==0:
            return path(previous,current)
        if i<2:
            next = move(current,i,j,i+1,j)
            if next not in visited:
                pri_queue.append((next,current,cost+eval(next)))
        if i>0:
            next = move(current, i, j, i - 1, j)
            if next not in visited:
                pri_queue.append((next, current, cost + eval(next)))
        if j<2:
            next = move(current,i,j,i,j+1)
            if next not in visited:
                pri_queue.append((next,current,cost+eval(next)))
        if j>0:
            next = move(current, i, j, i , j- 1)
            if next not in visited:
                pri_queue.append((next, current, cost + eval(next)))




goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

inital= [[2,8,3],
        [1,6,4],
        [7,0,5]]
display(astar(tuple(map(tuple,inital ))))

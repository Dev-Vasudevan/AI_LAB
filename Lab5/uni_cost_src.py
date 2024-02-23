

def ucs( graph, goal , source  ):
    pri_queue = []
    previous = {}
    visited = set ()

    pri_queue.append((source,"", 0))
    while pri_queue:

        pri_queue.sort ( key = lambda x:x[2])
        current,prev,cost = pri_queue.pop(0)

        if current  in visited:
            continue

        visited.add(current)
        previous[current]=prev

        if current == goal:
            print(cost)
            return path (previous,source , goal)
        for des,ct in graph[current]:
            if des not in visited:
                pri_queue.append((des , current , ct+cost  ))








def path ( previous ,src , goal ):
    path = []
    current = goal
    path.append(current)
    while current != src :
        current = previous[current]
        path.append(current)
    return path[::-1]

graph = {
  'S': [('1', 2), ('3', 5)],
  '1': [('G', 1)],
  '2': [('1', 4)],
  '3': [('1', 5), ('G', 6), ('4', 2)],
  '4': [('5', 3), ('2', 4)],
  '5': [('G', 3), ('2', 6)],
  'G': [('4', 7)]
}
print(ucs(graph,'G','S'))

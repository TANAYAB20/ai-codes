def dij(graph,src):

    distances = {node : float('inf') for node in graph}
    distances[src] = 0
    
    unv_node = list(graph.keys())
    while unv_node:
        curr_node = min(unv_node,key = lambda node:distances[node])
        unv_node.remove(curr_node)
        for v,weight in graph[curr_node].items():
            distance = distances[curr_node]+weight
            if distance<distances[v]:
                distances[v] = distance
    return distances
        
graph = {

    'A' : {'B':7,'C':9,'F':14},
    'B' : {'A':7,'C':10,'D':15},
    'C' : {'A':9,'B':10,'D':11,'F':2},
    'D' : {'B':15,'C':11,'E':6},
    'E' : {'D':6,'F':9},
    'F' : {'A':14,'C':2,'E':9},
}
mst = dij(graph,'A')
print(mst)
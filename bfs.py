graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}
 
def bfs(visited, graph,node):
    visited.append(node)
    queue = []
    queue.append(node)
 
    while queue:
        s = queue.pop(0)
        print(s)
 
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
 
bfs([], graph, 'A')
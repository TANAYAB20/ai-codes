import heapq
def astar(start, goal, graph, heuristic):
    open_list = [(0, start)]
    closed_list = set()
    g_scores = {start: 0}
    parents = {start: None}
    while open_list:
        f_score, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        closed_list.add(current)
        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue
            tentative_g_score = g_scores[current] + graph[current][neighbor]
            if neighbor not in [n[1] for n in open_list]:
                heapq.heappush(open_list, (tentative_g_score + heuristic(neighbor, goal), neighbor))
            elif tentative_g_score < g_scores[neighbor]:
                index = [n[1] for n in open_list].index(neighbor)
                open_list[index] = (tentative_g_score + heuristic(neighbor, goal), neighbor)
            parents[neighbor] = current
            g_scores[neighbor] = tentative_g_score
    return None

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 15, 'E': 20},
    'C': {'F': 5},
    'D': {'G': 25},
    'E': {'G': 20},
    'F': {'G': 10},
    'G': {}
}
def heuristic(node, goal):
    h_scores = {
        'A': 35,
        'B': 30,
        'C': 25,
        'D': 20,
        'E': 15,
        'F': 10,
        'G': 0
    }
    return h_scores[node]
path = astar('A', 'G', graph, heuristic)
print(path)

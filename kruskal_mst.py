def find(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j, parent):
    a = find(i, parent)
    b = find(j, parent)
    parent[a] = b

def kruskalMST(cost):
    V = len(cost)
    mincost = 0
    parent = [i for i in range(V)]

    edge_count = 0
    while edge_count < V - 1:
        min_edge = float('inf')
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i, parent) != find(j, parent) and cost[i][j] < min_edge:
                    min_edge = cost[i][j] 
                    a = i
                    b = j
        union(a, b, parent)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min_edge))
        edge_count += 1
        mincost += min_edge

    print("Minimum cost= {}".format(mincost))

def main():
    V = int(input("Enter the number of vertices: "))
    cost = []
    print("Enter the adjacency matrix for the graph (enter INF for no connection):")
    for i in range(V):
        row = input().split()
        row = [float('inf') if x == "INF" else int(x) for x in row]
        cost.append(row)

    kruskalMST(cost)

if __name__ == "__main__":
    main()


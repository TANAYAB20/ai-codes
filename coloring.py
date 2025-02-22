class GraphColoring: 
    def __init__(self, vertices, graph): 
        self.vertices = vertices 
        self.graph = graph 
        self.colors = [-1] * vertices 
        self.minColors = float('inf') 
 
    def solve(self): 
        self.try_coloring(0, 1) 
 
    def try_coloring(self, vertex, numColors): 
        if numColors >= self.minColors: 
            return 
 
        if vertex == self.vertices: 
            self.minColors = numColors 
            self.print_solution(numColors) 
            return 
 
        for color in range(1, numColors + 1): 
            if self.is_safe(vertex, color): 
                self.colors[vertex] = color 
                self.try_coloring(vertex + 1, numColors) 
                self.colors[vertex] = -1  # Backtrack 
 
        # Try to use a new color 
        self.colors[vertex] = numColors + 1 
        self.try_coloring(vertex + 1, numColors + 1) 
        self.colors[vertex] = -1 
 
    def is_safe(self, vertex, color): 
        for i in range(self.vertices): 
            if self.graph[vertex][i] == 1 and self.colors[i] == color: 
                return False 
        return True 
 
    def print_solution(self, numColors): 
        print("Solution found with", numColors, "colors:") 
        for i in range(self.vertices): 
            print("Vertex", i, "---> Color", self.colors[i]) 
 
 
def main(): 
    print("Enter the number of vertices:") 
    vertices = int(input()) 
    graph = [] 
 
    print("Enter the adjacency matrix:") 
for _ in range(vertices): 
row = list(map(int, input().split())) 
graph.append(row) 
coloring = GraphColoring(vertices, graph) 
coloring.solve() 
if __name__ == "__main__": 
main() 
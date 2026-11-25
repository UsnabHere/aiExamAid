V = 4

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

colors = ['Red', 'Green', 'Blue']
result = [None] * V

def is_safe(vertex, color):
    for i in range(V):
        if graph[vertex][i] == 1 and result[i] == color:
            return False

    return True

def graph_coloring(vertex):
    if vertex == V:
        return True

    for color in colors:
        if is_safe(vertex, color):
            result[vertex] = color

            if graph_coloring(vertex + 1):
                return True

            result[vertex] = None

    return False

if graph_coloring(0):
    print("Graph Coloring Solution:")

    for i in range(V):
        print("Vertex", i, ":", result[i])

else:
    print("No solution exists.")

   

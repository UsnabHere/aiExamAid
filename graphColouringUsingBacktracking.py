graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = 4
colors = [0] * n

def safe(node, color):
    for i in range(n):
        if graph[node][i] == 1 and colors[i] == color:
            return False
    return True

def solve(node):
    if node == n:
        return True

    for color in range(1, 4):
        if safe(node, color):
            colors[node] = color

            if solve(node + 1):
                return True

            colors[node] = 0

    return False

if solve(0):
    print("Colours:", colors)
else:
    print("No solution")

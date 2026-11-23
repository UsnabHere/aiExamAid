from collections import deque

def bfs(a, b, target):
    queue = deque([((0, 0), [(0, 0)])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if x == target or y == target:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        moves = [
            (a, y), (x, b),  # Fill jugs
            (0, y), (x, 0),  # Empty jugs
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        for move in moves:
            if move not in visited:
                queue.append((move, path + [move]))

    return None

result = bfs(4, 3, 2)

if result:
    for step in result:
        print(step)
else:
    print("No solution")

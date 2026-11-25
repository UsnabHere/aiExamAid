from collections import deque

def water_jug(capacity_a, capacity_b, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            print("Solution Found:")
            for step in path:
                print(step)
            print("Final State:", (a, b))
            return

        states = [
            ((capacity_a, b), "Fill Jug A"),
            ((a, capacity_b), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B")
        ]

        amount = min(a, capacity_b - b)
        states.append(((a - amount, b + amount),
                       "Pour A into B"))

        amount = min(b, capacity_a - a)
        states.append(((a + amount, b - amount),
                       "Pour B into A"))

        for new_state, action in states:
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    print("No solution exists.")

water_jug(4, 3, 2)

from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2024, day=18)
data = puzzle.input_data.split("\n")
# data = puzzle.examples[0].input_data.split("\n")

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
SIZE = 71

map = [list("." * SIZE) for _ in range(SIZE)]

i = 0
while True:
    x, y = data[i].split(",")
    map[int(y)][int(x)] = "#"
    seen = {}
    Q = deque([[0, 0]])
    while Q:
        x, y = Q.popleft()
        if (x, y) == (SIZE - 1, SIZE - 1):
            continue
        for dx, dy in DIRS:
            if 0 <= x + dx < SIZE and 0 <= y + dy < SIZE and map[x + dx][y + dy] != "#":
                cost = min(seen.get((x, y), 0) + 1, seen.get((x + dx, y + dy), float("inf")))
                if cost < seen.get((x + dx, y + dy), float("inf")):
                    Q.append((x + dx, y + dy))
                seen[x + dx, y + dy] = cost
    if (SIZE - 1, SIZE - 1) not in seen:
        print(data[i])
        break
    i += 1
print("\n".join(["".join(x) for x in map]))

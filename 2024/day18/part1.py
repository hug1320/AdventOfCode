from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2024, day=18)
data = puzzle.input_data.split("\n")
# data = puzzle.examples[0].input_data.split("\n")

size = 71
map = [list("." * size) for _ in range(size)]

for i in range(1024):
    x, y = data[i].split(",")
    map[int(y)][int(x)] = "#"

print("\n".join(["".join(x) for x in map]))

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

seen = {}
Q = deque([[0, 0]])
while Q:
    x, y = Q.popleft()
    if (x, y) == (size - 1, size - 1):
        continue
    for dx, dy in DIRS:
        if 0 <= x + dx < size and 0 <= y + dy < size and map[x + dx][y + dy] != "#":
            cost = min(seen.get((x, y), 0) + 1, seen.get((x + dx, y + dy), float("inf")))
            if cost < seen.get((x + dx, y + dy), float("inf")):
                Q.append((x + dx, y + dy))
            seen[x + dx, y + dy] = cost


print(seen[size - 1, size - 1])

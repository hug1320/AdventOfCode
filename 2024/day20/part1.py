from aocd.models import Puzzle
from collections import deque, Counter
import copy

puzzle = Puzzle(year=2024, day=20)
data = puzzle.input_data.split("\n")
# data = puzzle.examples[0].input_data.split("\n")
map = [list(line) for line in data]

# print("\n".join(["".join(x) for x in map]))

for i, line in enumerate(data):
    if 'S' in line:
        START = (i, line.index('S'))
        break

SIZE = len(map)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijkstra(map):
    seen = {}
    Q = deque([START])
    while Q:
        x, y = Q.popleft()
        if map[x][y] == "E":
            END = (x, y)
            continue
        for dx, dy in DIRS:
            if 0 <= x + dx < SIZE and 0 <= y + dy < SIZE and map[x + dx][y + dy] != "#":
                cost = min(seen.get((x, y), 0) + 1, seen.get((x + dx, y + dy), float("inf")))
                if cost < seen.get((x + dx, y + dy), float("inf")):
                    Q.append((x + dx, y + dy))
                seen[x + dx, y + dy] = cost
    return seen[END]

result = []
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == "#":
            nmap = copy.deepcopy(map)
            nmap[i][j] = "1"
            # print("\n".join(["".join(x) for x in nmap]))
            result.append(dijkstra(nmap))

print(sum(v for k,v in Counter(result).items() if max(result) - k >= 100))
from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2024, day=16)
data = puzzle.input_data.split("\n")

for i, x in enumerate(data):
    if "S" in x:
        START = (i, x.index("S"))
        break

map = [list(x) for x in data]

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
seen = {}
curr_dir = ">"
seen[(START[0], START[1])] = {DIRS[curr_dir]: 0}

path, paths = [START], {}
Q = deque([[START[0], START[1], curr_dir, 0, path]])
while Q:
    x, y, curr_dir, prev_cost, path = Q.popleft()
    for dir in DIRS:
        dx, dy = DIRS[dir]
        if (dx + DIRS[curr_dir][0], dy + DIRS[curr_dir][1]) == (0, 0):
            continue
        if map[x + dx][y + dy] != "#":
            move_cost = 1 if DIRS[curr_dir] == (dx, dy) else 1001
            next_cost = seen.get((x + dx, y + dy), {0: 0}).get((dx, dy), float("inf"))
            calc_cost = prev_cost + move_cost
            cost = min(next_cost, calc_cost)
            if map[x + dx][y + dy] == "E":
                END = (x + dx, y + dy)
                if cost < next_cost:
                    paths = set(path + [(x + dx, y + dy)])
                elif calc_cost == next_cost:
                    paths.update(path + [(x + dx, y + dy)])
            elif calc_cost <= next_cost:
                Q.append((x + dx, y + dy, dir, cost, path + [(x + dx, y + dy)]))
            seen.setdefault((x + dx, y + dy), {})[dx, dy] = cost


for x in paths:
    map[x[0]][x[1]] = "O"
print("\n".join(["".join(x) for x in map]))
print(len(paths))

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
current_dir = ">"
seen[(START[0], START[1])] = {DIRS[current_dir]: 0}

Q = deque([[START[0], START[1], current_dir]])
while Q:
    x, y, current_dir = Q.popleft()
    for dir in DIRS:
        dx, dy = DIRS[dir]
        if map[x + dx][y + dy] != "#":
            move_cost = 1 if DIRS[current_dir] == (dx, dy) else 1001
            next_cost = seen.get((x + dx, y + dy), {0: 0}).get((dx, dy), float("inf"))
            calc_cost = seen.get((x, y), {0: 0}).get(DIRS[current_dir]) + move_cost
            cost = min(next_cost, calc_cost)
            if map[x + dx][y + dy] == "E":
                END = (x + dx, y + dy)
            elif cost < seen.get((x + dx, y + dy), {0: 0}).get((dx, dy), float("inf")):
                Q.append((x + dx, y + dy, dir))
            seen.setdefault((x + dx, y + dy), {})[dx, dy] = cost


print(min(seen[(END[0], END[1])].values()))

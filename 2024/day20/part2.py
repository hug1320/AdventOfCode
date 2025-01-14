from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2024, day=20)
data = puzzle.input_data.split("\n")
map = [list(line) for line in data]

MIN_SAVED = 100
MAX_CHEAT = 20
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
SIZE = len(map)

for i, line in enumerate(data):
    if "S" in line:
        START = (line.index("S"), i)
    if "E" in line:
        END = (line.index("E"), i)


standard_path = {START: 0}
time_to_reach = 0
pos = START
while pos != END:
    for direction in DIRS:
        newpos = (pos[0] + direction[0], pos[1] + direction[1])
        if newpos not in standard_path and map[newpos[1]][newpos[0]] != "#":
            pos = newpos
            time_to_reach += 1
            standard_path[newpos] = time_to_reach


def reachable(start, max_steps):
    seen = set()
    reachable = {}
    Q = deque([(start, 0)])
    while Q:
        (x, y), steps = Q.popleft()
        if steps > max_steps:
            continue
        if (pos := (x, y)) not in seen:
            seen.add(pos)
            reachable[pos] = steps
            for dx, dy in DIRS:
                if 0 <= (new_x := x + dx) < SIZE and 0 <= (new_y := y + dy) < SIZE:
                    Q.append(((new_x, new_y), steps + 1))

    return reachable


cheats = {}
for start, start_time in standard_path.items():
    shortcuts = reachable(start, MAX_CHEAT)

    for END, cheat_duration in shortcuts.items():
        if END in standard_path and END != start:
            end_time = standard_path[END]
            saved = end_time - (start_time + cheat_duration)

            if saved >= MIN_SAVED:
                cheats[saved] = cheats.get(saved, 0) + 1

print(sum([v for k, v in cheats.items() if k >= MIN_SAVED]))

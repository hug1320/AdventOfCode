from aocd.models import Puzzle
import time
import os

puzzle = Puzzle(year=2024, day=15)
data = puzzle.input_data

map, moves = data.split("\n\n")
moves = "".join(moves.split("\n"))
map = [list(x) for x in map.split("\n")]

for i, x in enumerate(map):
    if "@" in x:
        INIT_POS = (i, x.index("@"))
        break

DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def move(pos, dir, obj):
    x, y = pos
    new_x, new_y = x + dir[0], y + dir[1]
    if map[new_x][new_y] == "#":
        return [x, y]
    elif map[new_x][new_y] == "O":
        if move((new_x, new_y), dir, "O") != [new_x, new_y]:
            map[new_x][new_y] = obj
            map[x][y] = "."
            return [new_x, new_y]
        return [x, y]
    elif map[new_x][new_y] == ".":
        map[new_x][new_y] = obj
        map[x][y] = "."
        return [new_x, new_y]


pos = INIT_POS
for m in moves:
    pos = move(pos, DIRS[m], "@")
    os.system('clear')
    print("\n".join(["".join(x) for x in map]))
    time.sleep(0.01)
print("\n".join(["".join(x) for x in map]))

count = 0
for i, line in enumerate(map):
    for j, x in enumerate(line):
        if x == "O":
            count += i*100 + j
            
print(count)
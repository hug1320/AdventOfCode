from aocd.models import Puzzle
from collections import deque
import time
import os

puzzle = Puzzle(year=2024, day=15)
data = puzzle.input_data

map, moves = data.split("\n\n")
moves = "".join(moves.split("\n"))
replacement = {"O": "[]", "@": "@.", ".": "..", "#": "##", "\n": "\n"}
map = [replacement[x] for x in map]
map = [list(x) for x in "".join(map).split("\n")]
print("\n".join(["".join(x) for x in map]))
    
for i, x in enumerate(map):
    if "@" in x:
        INIT_POS = (i, x.index("@"))
        break
DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def move(pos, dir):
    Q = deque([pos])
    V = deque()
    seen = set()
    while Q:
        x, y = Q.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        V.append((x, y))
        new_x, new_y = x + dir[0], y + dir[1]
        if map[new_x][new_y] == "#":
            return pos
        elif map[new_x][new_y] == "[":
            Q.append((new_x, new_y))
            Q.append((new_x, new_y+1))
        elif map[new_x][new_y] == "]":
            Q.append((new_x, new_y))
            Q.append((new_x, new_y-1))
        elif map[new_x][new_y] == ".":
            continue
    
    while V:
        x, y = V.pop()
        map[x+dir[0]][y+dir[1]] = map[x][y]
        map[x][y] = "."
    return (x+dir[0], y+dir[1])
        

pos = INIT_POS
for m in moves:
    pos = move(pos, DIRS[m])
    os.system('clear')
    print("\n".join(["".join(x) for x in map]))
    time.sleep(0.01)

count = 0
for i, line in enumerate(map):
    for j, x in enumerate(line):
        if x == "[":
            count += i*100 + j
            
print(count)
import numpy as np
import multiprocessing as mp
from multiprocessing.pool import ThreadPool

with open("input") as f:
    map = f.readlines()
    map = np.array([list(line.strip()) for line in map])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
markers = ["u", "r", "d", "l"]

GUARD_INIT = [i[0] for i in np.where(map == "^")]


def check(map):
    guard = GUARD_INIT

    current_dir = 0
    map[tuple(guard)] = markers[current_dir]
    while 0 < guard[0] < map.shape[0] - 1 and 0 < guard[1] < map.shape[1] - 1:
        guard += np.array(directions[current_dir])
        cell = map[tuple(guard)]
        if cell == "#":
            guard -= np.array(directions[current_dir])
            current_dir = (current_dir + 1) % 4
        elif markers[current_dir] == cell:
            return True
        elif cell in markers:
            map[tuple(guard)] = "|" if current_dir % 2 == 0 else "-"
        else:
            map[tuple(guard)] = markers[current_dir]
    return False


def fake_obstacle(pos):
    i, j = pos
    # print(f"Try obstacle at {i},{j}")
    new_map = map.copy()
    new_map[i][j] = "#"
    return check(new_map)


p = mp.Pool()
path_map = map.copy()
check(path_map)
path_map[tuple(GUARD_INIT)] = "^"
positions = np.where((path_map != ".") & (path_map != "#") & (path_map != "^"))
positions = list(zip(*positions))
print(f"{len(positions)} positions to check")
print(sum(p.map(fake_obstacle, positions)))

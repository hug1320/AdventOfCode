import numpy as np

with open("input") as f:
    map = f.readlines()
    map = np.array([list(line.strip()) for line in map])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard = [i[0] for i in np.where(map == "^")]
map[tuple(guard)] = "+"

current_dir = 0
while 0 < guard[0] < map.shape[0] - 1 and 0 < guard[1] < map.shape[1] - 1:
    guard += np.array(directions[current_dir])
    if map[tuple(guard)] == "#":
        guard -= np.array(directions[current_dir])
        current_dir = (current_dir + 1) % 4
    map[tuple(guard)] = "+"

print(np.sum(map == "+"))

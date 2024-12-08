from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=8)
data = puzzle.input_data.split("\n")
data = [list(line.strip()) for line in data]

antennas = {}
h = len(data)
w = len(data[0])
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c != ".":
            if c not in antennas:
                antennas[c] = [(i, j)]
            else:
                antennas[c].append((i, j))

for v in antennas.values():
    for pos in v:
        for j in v:
            if pos == j:
                continue
            data[pos[0]][pos[1]] = "#"
            data[j[0]][j[1]] = "#"
            vect = (pos[0] - j[0], pos[1] - j[1])
            antinode = (pos[0] + vect[0], pos[1] + vect[1]) 
            while 0 <= antinode[0] < h and 0 <= antinode[1] < w:
                data[antinode[0]][antinode[1]] = "#"
                antinode = (antinode[0] + vect[0], antinode[1] + vect[1])

print(sum([line.count("#") for line in data]))

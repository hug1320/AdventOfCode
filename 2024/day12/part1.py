from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2024, day=12)
data = puzzle.input_data.split("\n")

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
price = 0

nb_lines = len(data)
nb_cols = len(data[0])

seen = set()
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if (i, j) in seen:
            continue
        Q = deque([(i, j)])
        area = 0
        perim = 0
        while Q:
            i2, j2 = Q.popleft()
            if (i2, j2) in seen:
                continue
            seen.add((i2, j2))
            area += 1
            for d1, d2 in DIRS:
                if (
                    0 <= i2 + d1 < nb_lines
                    and 0 <= j2 + d2 < nb_cols
                    and data[i2 + d1][j2 + d2] == char
                ):
                    Q.append((i2 + d1, j2 + d2))
                else:
                    perim += 1

        price += area * perim

print(price)

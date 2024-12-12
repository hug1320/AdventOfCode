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
        perim_dict = dict()
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
                    if (d1, d2) not in perim_dict:
                        perim_dict[(d1, d2)] = set()
                    perim_dict[(d1, d2)].add((i2 + d1, j2 + d2))

        sides = 0
        for k, v in perim_dict.items():
            v = [(b, a) for a, b in v] if not k[0] else v
            vs = sorted(v)
            prev_a, prev_b = vs[0]
            for a, b in vs:
                if a != prev_a:
                    sides += 1
                    prev_a, prev_b = a, b
                    continue
                if b != prev_b + 1:
                    sides += 1
                prev_b = b
        price += area * sides

print(price)

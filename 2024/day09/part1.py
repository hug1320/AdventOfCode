from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=9)
data = puzzle.input_data

disk = []
for i, c in enumerate(data):
    if i % 2 == 0:
        disk += [i // 2] * int(c)
    else:
        disk += ["."] * int(c)


blanks = [i for i, c in enumerate(disk) if c == "."]

for i in blanks:
    while disk[-1] == ".":
        disk.pop()
    if len(disk) <= i:
        break
    disk[i] = disk.pop()

print(sum(int(c) * i for i, c in enumerate(disk)))

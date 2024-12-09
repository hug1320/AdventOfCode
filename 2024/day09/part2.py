from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=9)
data = puzzle.input_data

disk = [[str(i // 2)] * int(c) if i % 2 == 0 else ["."] * int(c) for i, c in enumerate(data)]

carry = 0
i = 0
while i + carry < len(disk):
    n = dict(enumerate(disk[::-1]))[i + carry]
    if "." not in n and n:
        for j, m in enumerate(disk[: len(disk) - (i + carry)]):
            if "." in m:
                if len(n) < len(m):
                    disk[j] = n
                    disk.insert(j + 1, m[len(n) :])
                    disk[-(i + carry + 1)] = m[: len(n)]
                    carry += len(m) - len(n)
                    i -= len(m) - len(n)
                    break
                elif len(n) == len(m):
                    disk[j] = n
                    disk[-(i + carry + 1)] = m
                    break
    i += 1

disk = sum(disk, [])
print(sum([int(c) * i for i, c in enumerate(disk) if c != "."]))

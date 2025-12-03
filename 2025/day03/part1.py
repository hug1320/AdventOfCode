with open("input") as f:
    input = f.read().strip().splitlines()
    input = [list(x) for x in input]


def bank_power(line):
    first = max(line[:-1])
    reste = line[(line.index(first) + 1) :]
    second = max(reste)
    return int(first + second)


print(sum([bank_power(x) for x in input]))

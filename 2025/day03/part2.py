with open("input") as f:
    input = f.read().strip().splitlines()
    input = [list(x) for x in input]

DIGITS = 12


def bank_power(line):
    result = []
    reste = line
    for i in range(DIGITS - 1):
        result.append(max(reste[: (-DIGITS + i + 1)]))
        reste = reste[(reste.index(result[i]) + 1) :]
    result.append(max(reste))
    return int("".join(result))


print(sum([bank_power(x) for x in input]))

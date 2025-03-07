def is_safe(line, recursive=False):
    down = line[0] - line[1] <= 0
    for i in range(len(line) - 1):
        delta = line[i] - line[i + 1]
        if delta > -1 or delta < -3 if down else delta < 1 or delta > 3:
            if recursive:
                return False
            else:
                return (
                    is_safe(line[: i - 1] + line[i:], True)
                    or is_safe(line[:i] + line[i + 1 :], True)
                    or is_safe(line[: i + 1] + line[i + 2 :], True)
                )
    return True


with open("input") as f:
    print(sum(is_safe([int(x) for x in line.split(" ")]) for line in f.readlines()))

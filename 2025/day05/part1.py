with open("input") as f:
    input = f.read().strip()
    ranges, ids = [x.split() for x in input.split("\n\n")]
    ids = [int(x) for x in ids]
    ranges = [[int(y) for y in x.split("-")] for x in ranges]

print(sum(any(a <= id <= b for a, b in ranges) for id in ids))

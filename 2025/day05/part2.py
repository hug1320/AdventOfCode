with open("input") as f:
    input = f.read().strip()
    ranges, _ = [x.split() for x in input.split("\n\n")]
    ranges = sorted([list(map(int, r.split("-"))) for r in ranges])

p2 = 0
for i, (a, b) in enumerate(ranges):
    for a2, b2 in ranges[i + 1 :]:
        if a <= a2 <= b:
            b = max(b, b2)
            ranges.remove([a2, b2])
    p2 += b - a + 1

print(p2)

import fuckit

with open("input") as f:
    input = f.read().strip().splitlines()
    input = [[int(i) for i in line.replace(".", "0").replace("@", "1")] for line in input]

HEIGHT, WIDTH = len(input) + 1, len(input[0]) + 1


@fuckit
def voisins(lines, i, j):
    res = 0
    im = (i - 1) % HEIGHT
    jm = min((j - 1) % WIDTH, j)
    res += sum(lines[im][jm : j + 2])
    res += sum(lines[i + 1][jm : j + 2])
    res += lines[i][(j - 1) % WIDTH]
    res += lines[i][j + 1]
    if res < 4:
        lines[i][j] = 0
    return res


p2 = 0
while v := sum((voisins(input, i, j) < 4) for i, line in enumerate(input) for j, value in enumerate(line) if value):
    p2 += v

print(p2)

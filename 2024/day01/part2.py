with open("input") as f:
    input = f.read().splitlines()
    input = [x.split("   ") for x in input]

left = [int(x[0]) for x in input]
right = [int(x[1]) for x in input]

left.sort()
right.sort()

score = 0
for i in left:
    score += right.count(i) * i

print(score)

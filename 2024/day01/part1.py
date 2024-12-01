with open("input") as f:
    input = f.read().splitlines()
    input = [x.split("   ") for x in input]

left = [int(x[0]) for x in input]
right = [int(x[1]) for x in input]

left.sort()
right.sort()

data = zip(left, right)

distance = sum([abs(x[0] - x[1]) for x in data])
print(distance)

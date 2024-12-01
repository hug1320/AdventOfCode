import itertools
import math

fd = open("input")
instructions = fd.readline().strip()
content = [i.split(" = ") for i in fd.read().splitlines()][1:]
nodes = dict([(i[0], tuple(i[1][1:-1].split(", "))) for i in content])


def left(x):
    return nodes[x][0]


def right(x):
    return nodes[x][1]


current = [i for i in nodes.keys() if i.endswith("A")]
length = len(current)
step = 0
steps = [0]*length
for i in itertools.cycle(instructions):
    if i == 'L':
        current = list(map(left, current))
    elif i == 'R':
        current = list(map(right, current))
    step += 1
    for j in range(length):
        if current[j].endswith("Z") and steps[j] == 0:
            steps[j] = step
    if 0 not in steps:
        break

print(math.lcm(*steps))

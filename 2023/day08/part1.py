import itertools

fd = open("input")
instructions = fd.readline().strip()
content = [i.split(" = ") for i in fd.read().splitlines()][1:]
nodes = dict([(i[0], tuple(i[1][1:-1].split(", "))) for i in content])

step = 0
current = "AAA"
for i in itertools.cycle(instructions):
    if i == 'L':
        current = nodes[current][0]
    elif i == 'R':
        current = nodes[current][1]
    step += 1
    if current == 'ZZZ':
        print(step)
        break

fd = open("input")
content = fd.read().split("\n")[:-1]

race = ["".join(k.split()[1:]) for k in content]

def nb_run(race):
    for i in range(int(race[0]) + 1):
        dist = i*(int(race[0]) - i)
        if dist > int(race[1]):
            return int(race[0]) + 1 - 2*i

print(nb_run(race))

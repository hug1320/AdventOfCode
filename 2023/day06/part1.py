fd = open("input")
content = fd.read().split("\n")[:-1]

races = [k.split()[1:] for k in content]
races = zip(races[0], races[1])

def nb_run(race):
    for i in range(int(race[0]) + 1):
        dist = i*(int(race[0]) - i)
        if dist > int(race[1]):
            return int(race[0]) + 1 - 2*i

res = 1
for race in races:
    res = res*nb_run(race)

print(res)

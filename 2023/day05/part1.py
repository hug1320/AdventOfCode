fd = open("input")
seeds = fd.readline().split(" ")[1:]

content = fd.read().split("\n")

def seed_to_loc(seed):
    loc = int(seed)
    step = 1
    skip = 0
    for i in content:
        if i == "":
            pass
        elif i.endswith("map:"):
            step += 1
            skip = 0
        elif not skip:
            line = i.split(" ")
            if 0 <= loc - int(line[1]) < int(line[2]):
                loc = int(line[0])+loc-int(line[1])
                skip = 1
    return loc

print(min(list(map(seed_to_loc, seeds))))

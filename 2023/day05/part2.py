import multiprocessing

fd = open("input")
seeds = fd.readline().split(" ")[1:]

content = fd.read().split("\n")

def seed_to_loc(seed):
    loc = int(seed[0])
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
            dest = int(line[0])
            src = int(line[1])
            mapr = int(line[2])
            if seed[0] < src:

                if seed[0] + seed[1] < src:
                    new_seeds.append([seed[0], seed[1]])

                    if 0 <= loc - src < mapr:
                        loc = dest + loc - src
                        skip = 1

                else:
                    new_seeds.append([seed[0], src-1])
                    seed[1] = seed[1] - (src - seed[0])
                    seed[0] = src

            elif seed[0] > src + mapr:
                pass

            if seed[0]+seed[1] <= dest + mapr:
                new_seed = eval(seed[0], src, mapr)
                new_range = eval(seed[0] + seed[1], src, mapr) - new_seed;
                new_seeds.append([new_seed, new_range]);

                if 0 <= loc - src < mapr:
                    loc = dest + loc - src
                    skip = 1

            new_seed = eval(seed[0], src, mapr)
            new_range = eval(seed[0] + seed[1], src, mapr)
            new_seeds.append([new_seed, new_range])
            seed[0] = src + mapr
            new_seeds.append([seed[0], seed[1]])

    return loc

def eval(a, src, mapr):
    diff = a - src
    if (diff >= 0 and diff <= mapr):
        return (src + diff)
    return a

locations = []
new_seeds = []
for i in range(len(seeds)//2):
    new_seeds += [[int(seeds[2*i]), int(seeds[2*i+1])]]
prev_seeds = []
#while len(prev_seeds)!=len(new_seeds):
#    prev_seeds = new_seeds.copy()
#    pool_obj = multiprocessing.Pool()
#    locations.append(min(pool_obj.map(seed_to_loc, new_seeds)))

while len(prev_seeds)!=len(new_seeds):
    prev_seeds = new_seeds.copy()
    for seed in new_seeds:
        locations.append(seed_to_loc(seed))
    print(new_seeds)

print(min(locations))

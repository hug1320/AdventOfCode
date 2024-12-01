import re

fd = open("input", "r")
content = fd.read()

max_red = 12
max_green = 13
max_blue = 14

games = content.split("\n")

games = [s.split(": ")[-1] for s in games[:-1]]

games = [re.split(", |; ", s) for s in games]

def valide(l):
    for s in l:
        cubes = s.split(" ")
        match cubes[1]:
            case "blue":
                if int(cubes[0]) > max_blue: return False
            case "red":
                if int(cubes[0]) > max_red: return False
            case "green":
                if int(cubes[0]) > max_green: return False
            case _:
                pass
    return True


res = [valide(l) for l in games]

print(sum([i+1 for i in range(len(res)) if res[i]]))

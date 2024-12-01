import re

fd = open("input", "r")
content = fd.read()

games = content.split("\n")
games = [s.split(": ")[-1] for s in games[:-1]]
games = [re.split(", |; ", s) for s in games]

def power(game):

    max_red = 0
    max_green = 0
    max_blue = 0
    
    for s in game:
        cubes = s.split(" ")
        match cubes[1]:
            case "blue":
                if int(cubes[0]) > max_blue:
                    max_blue = int(cubes[0])
            case "red":
                if int(cubes[0]) > max_red:
                    max_red = int(cubes[0])
            case "green":
                if int(cubes[0]) > max_green:
                    max_green = int(cubes[0])
            case _:
                pass
    return max_green*max_red*max_blue


print(sum([power(game) for game in games]))

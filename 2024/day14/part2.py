from aocd.models import Puzzle
import re
import time

puzzle = Puzzle(year=2024, day=14)
data = puzzle.input_data.split("\n")

wide = 101
tall = 103


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x = (self.x + self.vx) % wide
        self.y = (self.y + self.vy) % tall

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()


robots = []
for line in data:
    x, y, vx, vy = re.findall(r"p=(.+),(.+) v=(.+),(.+)", line)[0]
    robots.append(Robot(int(x), int(y), int(vx), int(vy)))

for i in range(10000):
    map = [["." for _ in range(wide)] for _ in range(tall)]
    for robot in robots:
        robot.move()
        map[robot.y][robot.x] = "#"
    if any([map[i].count("#") > 20 for i in range(tall)]) and any([x.count("#") > 20 for x in [[map[j][i] for j in range(tall)] for i in range(wide)]]):
        print("\n".join(["".join(row) for row in map]))
        print(i)
        time.sleep(1)
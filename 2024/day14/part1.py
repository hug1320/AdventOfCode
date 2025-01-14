from aocd.models import Puzzle
import re
from operator import mul
from functools import reduce

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

for i in range(100):
    for robot in robots:
        robot.move()

quadrant = [0] * 4
for robot in robots:
    if robot.x < wide // 2 and robot.y < tall // 2:
        quadrant[0] += 1
    elif robot.x < wide // 2 and robot.y > tall // 2:
        quadrant[1] += 1
    elif robot.x > wide // 2 and robot.y < tall // 2:
        quadrant[2] += 1
    elif robot.x > wide // 2 and robot.y > tall // 2:
        quadrant[3] += 1

print(reduce(mul, quadrant))

# map = [["." for _ in range(wide)] for _ in range(tall)]
# for robot in robots:
#     map[robot.y][robot.x] = "#"
# print("\n".join(["".join(row) for row in map]))

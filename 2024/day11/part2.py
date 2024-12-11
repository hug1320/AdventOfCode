from aocd.models import Puzzle
from functools import cache

puzzle = Puzzle(year=2024, day=11)
data = puzzle.input_data.split(" ")


@cache
def blink(stone, n):
    if n == 75:
        return 1
    new_stones = []
    if stone == "0":
        new_stones.append("1")
    elif (size := len(stone)) % 2 == 0:
        new_stones.append(str(int(stone[: size // 2])))
        new_stones.append(str(int(stone[size // 2 :])))
    else:
        new_stones.append(str(int(stone) * 2024))
    return sum(blink(stone, n + 1) for stone in new_stones)


print(sum(blink(stone, 0) for stone in data))

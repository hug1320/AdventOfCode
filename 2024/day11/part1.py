from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=11)
data = puzzle.input_data.split(" ")


def blink(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == "0":
            new_stones.append("1")
        elif (size := len(stone)) % 2 == 0:
            new_stones.append(str(int(stone[: size // 2])))
            new_stones.append(str(int(stone[size // 2 :])))
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones


for i in range(25):
    data = blink(data)

print(len(data))

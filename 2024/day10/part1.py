from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=10)
data = puzzle.input_data.split("\n")
possible_neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def check_neighbours(x, y, val, founds):
    if val == 9:
        founds.append((x, y))
        return founds
    neighbours = []
    for i, j in possible_neighbours:
        if x + i >= 0 and x + i < len(data) and y + j >= 0 and y + j < len(data[0]):
            if int(data[x + i][y + j]) == val + 1:
                neighbours.append((x + i, y + j))
    return list(set(sum([check_neighbours(x, y, val+1, founds.copy()) for x, y in neighbours], [])))


print(sum([len(check_neighbours(x, y, 0, [])) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == '0']))

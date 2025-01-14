from aocd.models import Puzzle
import re


puzzle = Puzzle(year=2024, day=13)
data = puzzle.input_data.split("\n\n")

count = 0
for game in data:
    M = []
    for line in game.split("\n"):
        M.append(*re.findall(r"X(?:\+|=)(\d+), Y(?:\+|=)(\d+)", line))
    B = M.pop()
    M = [[int(M[j][i]) for j in range(len(M))] for i in range(len(M[0]))]
    B = [int(x) for x in B]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    invM = [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]
    X = (invM[0][0] * B[0] + invM[0][1] * B[1]) / det
    Y = (invM[1][0] * B[0] + invM[1][1] * B[1]) / det
    if X.is_integer() and Y.is_integer():
        count += X * 3 + Y * 1

print(int(count))

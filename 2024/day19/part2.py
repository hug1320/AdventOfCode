from aocd.models import Puzzle
from functools import cache

puzzle = Puzzle(year=2024, day=19)
data = puzzle.input_data

towels, designs = data.split("\n\n")
towels, designs = towels.split(", "), designs.split("\n")

@cache
def check(design):
    if design == "":
        return True
    return sum(check(design[len(towel) :]) for towel in towels if design.startswith(towel))


print(sum(check(design) for design in designs))

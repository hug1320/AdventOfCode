import re

with open("input") as f:
    lines = f.read()
    lines = "ado()" + lines

lines = lines.split("don't()")
lines = sum([line.split("do()")[1:] for line in lines if "do()" in line], [])
mults = sum([re.findall(r"mul\((\d+),(\d+)\)", line) for line in lines], [])


print(sum(int(a) * int(b) for a, b in mults))

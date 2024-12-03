import re

with open('input') as f:
    lines = f.read()
    
mults = re.findall(r'mul\((\d+),(\d+)\)', lines)

print(sum(int(a) * int(b) for a, b in mults))
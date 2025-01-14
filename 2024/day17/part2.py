from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2024, day=17)
data = puzzle.input_data

A, B, C, *instructions = re.findall(r"(\d+)", data)


def passe(A):
    def combo(ope):
        match int(ope):
            case 0 | 1 | 2 | 3:
                return int(ope)
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C

    B = 0
    C = 0
    ip = 0
    out = []
    while ip < len(instructions):
        instr = instructions[ip]
        operand = instructions[ip + 1]
        # print("instruction :", instr)
        # print("operand :", operand)

        match int(instr):
            case 0:
                A = A // (2 ** combo(operand))
            case 1:
                B = B ^ int(operand)
            case 2:
                B = combo(operand) % 8
            case 3:
                if A:
                    ip = int(operand)
                    continue
            case 4:
                B = B ^ C
            case 5:
                out.append(str(combo(operand) % 8))
            case 6:
                B = A // (2 ** combo(operand))
            case 7:
                C = A // (2 ** combo(operand))
        ip += 2
    return out


init_a = 0
for j, c in enumerate(instructions[::-1]):
    i = 0
    while passe(init_a * 8 + i) != instructions[-j - 1 :]:
        i += 1
    init_a = init_a * 8 + i

print(init_a)

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=7)
data = puzzle.input_data.split("\n")


def eval_retard(nums, ops):
    res = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            res += nums[i + 1]
        elif op == "*":
            res *= nums[i + 1]
        else:
            res = int(str(res) + str(nums[i + 1]))
    return res


def check(line):
    def try_ops(ops, pos):
        if pos == len(nums) - 1:
            return eval_retard(nums, ops) == int(result)
        return (
            try_ops(ops + ["+"], pos + 1)
            or try_ops(ops + ["*"], pos + 1)
            or try_ops(ops + ["||"], pos + 1)
        )

    result, calcul = line.split(":")
    nums = [int(num) for num in calcul.strip().split(" ")]
    if try_ops([], 0):
        return int(result)
    return 0


print(sum([check(line) for line in data]))

from functools import cmp_to_key

with open("input") as f:
    lines = f.readlines()
    rules = lines[: lines.index("\n")]
    messages = lines[lines.index("\n") + 1 :]
    rules = [[int(r) for r in rule.strip().split("|")] for rule in rules]
    messages = [[int(num) for num in msg.strip().split(",")] for msg in messages]


def check_msg(msg):
    def order(a, b):
        for left, right in used_rules:
            if a == left and b == right:
                return -1
            elif a == right and b == left:
                return 1

    used_rules = [(a, b) for a, b in rules if a in msg and b in msg]

    valid = all((msg.index(left) < msg.index(right)) for left, right in used_rules)
    if valid:
        return 0
    else:
        msg.sort(key=cmp_to_key(order))
        return msg[len(msg) // 2]


print(sum([check_msg(msg) for msg in messages]))

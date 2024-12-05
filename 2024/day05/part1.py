with open("input") as f:
    lines = f.readlines()
    rules = lines[: lines.index("\n")]
    messages = lines[lines.index("\n") + 1 :]
    rules = [[int(r) for r in rule.strip().split("|")] for rule in rules]
    messages = [[int(num) for num in msg.strip().split(",")] for msg in messages]


def check_msg(msg):
    used_rules = [(a, b) for a, b in rules if a in msg and b in msg]

    valid = all((msg.index(left) < msg.index(right)) for left, right in used_rules)
    if valid:
        return msg[len(msg) // 2]
    else:
        return 0


print(sum([check_msg(msg) for msg in messages]))

fd = open("input")
content = fd.read().split("\n")[:-1]

cards = [k.split(":")[1:] for k in content]
cards = [k[0].split("|") for k in cards]
cards = [[k[0].split(), k[1].split()] for k in cards]
numbers = 0

for k in cards:
    number = 0
    for card in k[1]:
        if card in k[0]:
            number = 1 if number == 0 else number * 2
    numbers += number

print(numbers)

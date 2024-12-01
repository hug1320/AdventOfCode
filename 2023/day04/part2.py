fd = open("input")
content = fd.read().split("\n")[:-1]

cards = [k.split(":")[1:] for k in content]
cards = [k[0].split("|") for k in cards]
cards = [[k[0].split(), k[1].split()] for k in cards]

nb_card = [1]*len(cards)
for i in range(len(cards)):
    matching = 0
    for card in cards[i][1]:
        if card in cards[i][0]:
            matching += 1
    for j in range(1, matching+1):
        nb_card[i+j-1] += nb_card[i-1]

print(sum(nb_card))

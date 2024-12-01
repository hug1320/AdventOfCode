fd = open("input")
content = [tuple(i.split()) for i in fd.read().split("\n")][:-1]


class Main:

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.value = sum([cards.count(i) for i in cards])


res = [Main(i[0], i[1]) for i in content]
res.sort(key=lambda x: (x.value, ["23456789TJQKA".index(x.cards[i]) for i in range(len(x.cards))]))
print(sum([res[i].bid*(i+1) for i in range(len(res))]))

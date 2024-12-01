fd = open("input")
content = [tuple(i.split()) for i in fd.read().split("\n")][:-1]


class Main:

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        count = dict([(i, cards.count(i)) for i in cards])
        sorted_count = sorted(count, key=lambda x: (count[x], "J23456789TQKA".index(x)), reverse=True)
        if 'J' in sorted_count:
            if sorted_count[0] == 'J':
                if len(sorted_count) > 1:
                    count[sorted_count[1]] += count['J']
            else:
                count[sorted_count[0]] += count['J']
            del count['J']
            if count == {}:
                count = {'J': 5}

        self.value = sum([count[i] if i != 'J' else max(count.values()) for i in cards])


res = [Main(i[0], i[1]) for i in content]
res.sort(key=lambda x: (x.value, ["J23456789TQKA".index(x.cards[i]) for i in range(len(x.cards))]))
print(sum([res[i].bid * (i + 1) for i in range(len(res))]))

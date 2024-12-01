fd = open("input" , "r")

content = fd.read()
r = content.split("\n")

numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def only_int (s):
    res = ""
    for c in s:
        try:
            if int(c) >= 0 :
                res = res + c
        except ValueError:
            pass
    return res 

def combine(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return int(s[0]*2)
    else:
        return int(s[0]+s[-1])

def replace(s):
    for cle,valeur in numbers.items():
        while cle in s:
            s = s[:s.index(cle)+1] + str(valeur) + s[s.index(cle)+1:]
    return s

print(sum([combine(only_int(replace(x))) for x in r]))

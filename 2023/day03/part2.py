fd = open("input")
content = fd.read().split("\n")[:-1]

chiffres = [str(k) for k in range(10)]

nb_col = len(content[1])
nb_lin = len(content)

def voisins(j,i):
    return [(j-1,i-1), (j-1, i), (j-1, i+1), (j, i-1), (j, i+1), (j+1, i-1), (j+1, i), (j+1, i+1)]

def nombre_g(t,j,i):
    pos.append((j,i))
    if t[j][i-1] in chiffres:
        return nombre_g(t,j,i-1) + t[j][i]
    else:
        return t[j][i]

def nombre_d(t,j,i):
    try:
        pos.append((j,i))
        if t[j][i+1] in chiffres:
            return t[j][i] + nombre_d(t,j,i+1)
        else:
            return t[j][i]
    except IndexError:
        return t[j][i]

def nombre(t,j,i):
    return int(nombre_g(t,j,i)[:-1] + nombre_d(t,j,i))

pos = []
res = []

for j in range(nb_lin):
    for i in range(nb_col):
        if content[j][i] == "*":
            gear = []
            for k in voisins(j,i):
                if content[k[0]][k[1]] in chiffres and (k[0],k[1]) not in pos:
                    gear.append(nombre(content,k[0],k[1]))
            if len(gear) == 2:
                res.append(gear[0]*gear[1])

print(sum(res))

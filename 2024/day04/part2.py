with open("input") as f:
    data = f.readlines()

word = "MAS"
count = 0 
   
h = len(data)
for i, line in enumerate(data):
    l = len(line)
    for j, c in enumerate(line):
        if c == word[1]:
            xcount = 0
            if 1<=i<h-1 and 1<=j<=l-1 and data[i-1][j-1] == word[0] and data[i+1][j+1] == word[2]:
                xcount += 1
            if 1<=i<h-1 and 1<=j<=l-1 and data[i-1][j+1] == word[0] and data[i+1][j-1] == word[2]:
                xcount += 1
            if 1<=i<h-1 and 1<=j<=l-1 and data[i-1][j-1] == word[2] and data[i+1][j+1] == word[0]:
                xcount += 1
            if 1<=i<h-1 and 1<=j<=l-1 and data[i-1][j+1] == word[2] and data[i+1][j-1] == word[0]:
                xcount += 1
            if xcount >= 2:
                count += 1
     
print(count)
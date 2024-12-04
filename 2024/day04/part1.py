with open("input") as f:
    data = f.readlines()

word = "XMAS"
count = 0 
   
h = len(data)
for i, line in enumerate(data):
    l = len(line)
    count += line.count(word) + line.count(word[::-1])
    for j, c in enumerate(line):
        if c == word[0]:
            if i<h-3 and data[i+1][j] == word[1] and data[i+2][j] == word[2] and data[i+3][j] == word[3]:
                count += 1
            if i>=3 and data[i-1][j] == word[1] and data[i-2][j] == word[2] and data[i-3][j] == word[3]:
                count += 1
            if i>=3 and j>=3 and data[i-1][j-1] == word[1] and data[i-2][j-2] == word[2] and data[i-3][j-3] == word[3]:
                    count += 1
            if i<h-3 and j>=3 and data[i+1][j-1] == word[1] and data[i+2][j-2] == word[2] and data[i+3][j-3] == word[3]:
                count += 1
            if j<l-3 and i<h-3 and data[i+1][j+1] == word[1] and data[i+2][j+2] == word[2] and data[i+3][j+3] == word[3]:
                count += 1
            if i>=3 and j<l-3 and data[i-1][j+1] == word[1] and data[i-2][j+2] == word[2] and data[i-3][j+3] == word[3]:
                count += 1
            
print(count)

### Funny Regex Solution

# import re
# with open("input") as f:
#     data = f.read()
#     lg = len(data.split("\n")[0])
#     data = data.replace("\n", ":")
# count = 0
# count += len(re.findall(r"(?=(XMAS|SAMX))", data))
# count += len(re.findall(f"(?=(X.{{{lg}}}M.{{{lg}}}A.{{{lg}}}S|S.{{{lg}}}A.{{{lg}}}M.{{{lg}}}X))", data))
# count += len(re.findall(f"(?=(X.{{{lg-1}}}M.{{{lg-1}}}A.{{{lg-1}}}S|S.{{{lg-1}}}A.{{{lg-1}}}M.{{{lg-1}}}X))", data))
# count += len(re.findall(f"(?=(X.{{{lg+1}}}M.{{{lg+1}}}A.{{{lg+1}}}S|S.{{{lg+1}}}A.{{{lg+1}}}M.{{{lg+1}}}X))", data))

# print(count)
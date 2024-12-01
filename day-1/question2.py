file = open("input.txt", "r")
list1,list2 = [],[]
score = 0
# reading file contents
while(file):
    line = file.readline()
    if(line == ""):
        break
    list1.append(line.split()[0])
    list2.append(line.split()[1])
# get difference from entries
for x in list1:
    count = list2.count(x)
    score += int(x) * count
print(score)


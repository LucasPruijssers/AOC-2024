file = open("input.txt", "r")
list1,list2 = [],[]
distance = 0
# reading file contents
while(file):
    line = file.readline()
    if(line == ""):
        break
    list1.append(line.split()[0])
    list2.append(line.split()[1])
# order lists ascending
list1.sort()
list2.sort()
# get difference from entries
for i in range(len(list1)):
    distance+= abs(int(list1[i])-int(list2[i]))
print(distance)


def is_ascending(input):
    for i in range(len(input) - 1):
        if(int(input[i]) == int(input[i+1])):
            return False
        if(int(input[i]) > int(input[i+1])):
            return False
        if (abs(int(input[i]) - int(input[i+1])) > 3):
            return False
    return True
def is_descending(input):
    for i in range(len(input) - 1):
        if(int(input[i]) == int(input[i+1])):
            return False
        if(int(input[i]) < int(input[i+1])):
            return False
        if (abs(int(input[i]) - int(input[i+1]) > 3)):
            return False
    return True

file = open("input.txt", "r")
count = 0
while(file):
    line = file.readline()
    if(line == ""):
        break
    levels = line.split()
    if(is_ascending(levels) or is_descending(levels)):
        count += 1
        print(levels)
        print(count)
print(count)


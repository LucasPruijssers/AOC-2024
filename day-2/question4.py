def handle_edgecase_positive(input):
    i = 0
    while i < len(input) - 1:
        if int(input[i]) == int(input[i + 1]) or int(input[i]) > int(input[i + 1]) or abs(int(input[i]) - int(input[i + 1])) > 3:
            input.pop(i)
            break
        else:
            i += 1

def handle_edgecase_negative(input):
    i = 0
    while i < len(input) - 1:
        if int(input[i]) == int(input[i + 1]) or int(input[i]) < int(input[i + 1]) or abs(int(input[i]) - int(input[i + 1])) > 3:
            input.pop(i)
            break
        else:
            i += 1

def is_ascending(input):
    for i in range(len(input) - 1):
        if(int(input[i]) == int(input[i+1]) or int(input[i]) > int(input[i+1]) or abs(int(input[i]) - int(input[i+1])) > 3):
            return False
    return True
def is_descending(input):
    for i in range(len(input) - 1):
        if(int(input[i]) == int(input[i+1]) or int(input[i]) < int(input[i+1]) or abs(int(input[i]) - int(input[i+1]) > 3)):
            return False
    return True

file = open("input.txt", "r")
count = 0
while(file):
    line = file.readline()
    if(line == ""):
        break
    levels = line.split()
    # First we check positive
    positive = levels.copy()
    handle_edgecase_positive(positive)
    if(is_ascending(positive)):
        count+= 1
        continue
    negative = levels.copy()
    handle_edgecase_negative(negative)
    if(is_descending(negative)):
        count+=1
        continue
print(count)



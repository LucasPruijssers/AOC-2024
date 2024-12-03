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

# get all combinations of not safe entries
def checkAllCombinations(list):
    count = 0
    # list contains couple strings of stuff
    for entry in list:
        combinations = []
        for i in range(len(entry)) :
            copy = entry.copy()
            copy.pop(i)
            combinations.append(copy)
        
        for combination in combinations:
            if(question1(combination)):
                count += 1
                break
    return count        

def question1(line):
    if(is_ascending(line) or is_descending(line)):
        return True
    else:
        return False

def question2():
    count = 0
    unsafeEntries = []
    file = open("input.txt", "r")
    while(file):
        line = file.readline()
        if(line == ""):
            break
        levels = line.split()
        if(question1(levels)):
            count+=1
        else:
            unsafeEntries.append(levels)      
    combinations = checkAllCombinations(unsafeEntries)
    total = count + combinations
    print (total)
question2()
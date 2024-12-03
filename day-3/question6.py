import re
def sum(tuples):
    result = 0
    for entry in tuples:
        result += int(entry[0]) * int(entry[1])
    return(result)

def garbageRemoval(string):
    pattern = r"don't\(\).*?do\(\)"
    result = re.sub(pattern, '', string, flags=re.DOTALL)
    return result

def question6():    
    file = open("input.txt", "r")
    txt = file.read()
    filtered_txt = garbageRemoval(txt)
    
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern,filtered_txt)
    filtered_matches = [match[4:-1] for match in matches]
    tuples = []
    for match in filtered_matches:
        x,y = match.split(',')[0],match.split(',')[1]
        tuples.append((x,y))
    result = sum(tuples)
    print(result)

question6()
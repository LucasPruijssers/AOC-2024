import re
def sum(tuples):
    result = 0
    for entry in tuples:
        result += int(entry[0]) * int(entry[1])
    return(result)


def question5():    
    file = open("input.txt", "r")
    txt = file.read()
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern,txt)
    filtered_matches = [match[4:-1] for match in matches]
    tuples = []
    for match in filtered_matches:
        x,y = match.split(',')[0],match.split(',')[1]
        tuples.append((x,y))
    result = sum(tuples)
    print(result)
    

question5()
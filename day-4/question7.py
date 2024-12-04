import re
def horizontal(rows):
    count = 0
    for row in rows:
        instances = re.findall("XMAS",row)
        instances.extend(re.findall("SAMX",row))
        count += len(instances)
    print (count)
    return count
def vertical(rows):
    result = 0
    for row in rows:
        rowIndex = rows.index(row)
        columnIndeces = getIndices(row)
        for columnIndex in columnIndeces:
            # check up if row index > 2
            if rowIndex > 2: 
                if((rows[rowIndex - 1])[columnIndex] == "M" and (rows[rowIndex - 2])[columnIndex] == "A" and (rows[rowIndex - 3])[columnIndex] == "S"):
                    result+=1
            # check down if row index < len(rows) - 2
            if rowIndex < len(rows) - 3:
                if((rows[rowIndex + 1])[columnIndex] == "M" and (rows[rowIndex + 2])[columnIndex] == "A" and (rows[rowIndex + 3])[columnIndex] == "S"):
                    result+=1
    print (result)
    return result
def diagonal(rows):
    result = 0
    for row in rows:
        rowIndex = rows.index(row)
        columnIndeces = getIndices(row)
        for columnIndex in columnIndeces:
            # check up right
            if rowIndex > 2 and columnIndex < len(row) - 2: 
                if((rows[rowIndex - 1])[columnIndex + 1] == "M" and (rows[rowIndex - 2])[columnIndex + 2] == "A" and (rows[rowIndex - 3])[columnIndex + 3] == "S"):
                    result+=1
            # check up left
            if rowIndex > 2 and columnIndex > 2: 
                if((rows[rowIndex - 1])[columnIndex - 1] == "M" and (rows[rowIndex - 2])[columnIndex - 2] == "A" and (rows[rowIndex - 3])[columnIndex - 3] == "S"):
                    result+=1
            # check down right
            if (rowIndex < len(rows) - 3) and (columnIndex < len(row) - 2):
                if((rows[rowIndex + 1])[columnIndex + 1] == "M" and (rows[rowIndex + 2])[columnIndex + 2] == "A" and (rows[rowIndex + 3])[columnIndex + 3] == "S"):
                    result+=1
            # check down left
            if (rowIndex < len(rows) - 3) and (columnIndex > 2):
                if((rows[rowIndex + 1])[columnIndex - 1] == "M" and (rows[rowIndex + 2])[columnIndex - 2] == "A" and (rows[rowIndex + 3])[columnIndex - 3] == "S"):
                    result+=1
    print (result)
    return result

# get all the indices of X in a row
def getIndices(row):
    result = []
    for index, char in enumerate(row):
        if(char == "X"):
            result.append(index)
    return(result)

def question7():
    count = 0
    file = open("day-4/input.txt", "r")
    rows = file.readlines()
    count += horizontal(rows)
    count += vertical(rows)
    count += diagonal(rows)
    print (count)
        
question7()
def diagonal(rows):
    result = 0
    for row in rows:
        rowIndex = rows.index(row)
        columnIndeces = getIndices(row)
        for columnIndex in columnIndeces:
            # row - means up, + means low
            # column - means left, + means right
            # M   S 
            #   A
            # M   S
            if rowIndex > 0 and rowIndex < len(rows) - 1 and columnIndex > 0 and columnIndex < len(row): 
                if((rows[rowIndex - 1])[columnIndex - 1] == "M" and(rows[rowIndex + 1])[columnIndex - 1] == "M"
                   and (rows[rowIndex - 1])[columnIndex + 1] == "S" and(rows[rowIndex + 1])[columnIndex + 1] == "S" ):
                    result+=1
                    continue
            # S   S 
            #   A
            # M   M
            if rowIndex > 0 and rowIndex < len(rows) - 1 and columnIndex > 0 and columnIndex < len(row): 
                if((rows[rowIndex - 1])[columnIndex - 1] == "S" and(rows[rowIndex + 1])[columnIndex - 1] == "M"
                   and (rows[rowIndex - 1])[columnIndex + 1] == "S" and(rows[rowIndex + 1])[columnIndex + 1] == "M" ):
                    result+=1
                    continue
            # S   M 
            #   A
            # S   M
            if rowIndex > 0 and rowIndex < len(rows) - 1 and columnIndex > 0 and columnIndex < len(row): 
                if((rows[rowIndex - 1])[columnIndex - 1] == "S" and(rows[rowIndex + 1])[columnIndex - 1] == "S"
                   and (rows[rowIndex - 1])[columnIndex + 1] == "M" and(rows[rowIndex + 1])[columnIndex + 1] == "M" ):
                    result+=1
                    continue
            # M   M 
            #   A
            # S   S
            if rowIndex > 0 and rowIndex < len(rows) - 1 and columnIndex > 0 and columnIndex < len(row): 
                if((rows[rowIndex - 1])[columnIndex - 1] == "M" and(rows[rowIndex + 1])[columnIndex - 1] == "S"
                   and (rows[rowIndex - 1])[columnIndex + 1] == "M" and(rows[rowIndex + 1])[columnIndex + 1] == "S" ):
                    result+=1
                    continue
    print (result)
    return result

# get all the indices of X in a row
def getIndices(row):
    result = []
    for index, char in enumerate(row):
        if(char == "A"):
            result.append(index)
    return(result)

def question8():
    count = 0
    file = open("day-4/input.txt", "r")
    rows = file.readlines()
    count += diagonal(rows)
    print (count)
        
question8()
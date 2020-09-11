def setMatrixToZero(m):
    rowFlags = []
    columnFlags = []

    for i in range(0, len(m)):
        rowFlags.append(False)

    for j in range(0, len(m[0])):
        columnFlags.append(False)

    # set the flags for rows and columns with a zero in them
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == 0:
                rowFlags[i] = True
                columnFlags[j] = True
    
    # set 0's in the rows
    for i in range(0, len(rowFlags)):
        if (rowFlags[i]):
            setRowToZero(m, i)

    # set 0's in the columns
    for i in range(0, len(columnFlags)):
        if (columnFlags[i]):
            setColumnToZero(m, i)

def setRowToZero(m, row):
    for j in range(0, len(m[0])):
        m[row][j] = 0

def setColumnToZero(m, column):
    for i in range(0, len(m)):
        m[i][column] = 0


m1 = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
setMatrixToZero(m1)
print(m1)
# Make list from input, each item is the data for one seat.
with open('day5input') as f:
    allSeatData = f.read().splitlines()

# Calculates the row of the seat, between 0 and 127.
def calculate_row(seatdata):
    rowlist = range(0,128)
    rowdata = seatdata[:7]
    remainingrows = 128
    for i in rowdata:
        remainingrows = int(remainingrows/2)
        if i == "F":
            rowlist = rowlist[:remainingrows]
        elif i == "B":
            rowlist = rowlist[remainingrows:]
    return rowlist[0]


# Calculate the column of the seat, between 0 and 7.
def calculate_column(seatdata):
    columnlist = list(range(0, 8))
    columndata = seatdata[7:]
    remainingcolumns = 8
    for i in columndata:
        remainingcolumns = int(remainingcolumns / 2)
        if i == "L":
            columnlist = columnlist[:remainingcolumns]
        elif i == "R":
            columnlist = columnlist[remainingcolumns:]
    return columnlist[0]


# Calculate seat ID by following formula.
def calculate_seat_id(seatdata):
    return calculate_row(seatdata) * 8 + calculate_column(seatdata)


# Find the highest seat ID.
highestID = 0
for seatdata in allSeatData:
    currentID = calculate_seat_id(seatdata)
    if currentID > highestID:
        highestID = currentID
print('Highest ID:' + str(highestID))

# Enter all IDs into list.
allSeatIDs = []
for seatdata in allSeatData:
    allSeatIDs.append(calculate_seat_id(seatdata))

# Enter all possible IDs into list.
allPossibleIDs = []
for column in range(0,8):
    for row in range(0,128):
        allPossibleIDs.append(row*8+column)

# Find all possible IDs that aren't in the list of existing IDs.
myPossibleIDs = []
for possibleID in allPossibleIDs:
    if possibleID not in allSeatIDs:
        myPossibleIDs.append(possibleID)

print('Total seat IDs:' + str(len(allSeatIDs)))
print('Total possible IDs:' + str(len(allPossibleIDs)))
print('Total non-included IDs:' + str(len(myPossibleIDs)))

# Check if each missing ID matches the criteria.
for myPossibleID in myPossibleIDs:
    if (myPossibleID+1) in allSeatIDs and (myPossibleID-1) in allSeatIDs:
        print(myPossibleID)

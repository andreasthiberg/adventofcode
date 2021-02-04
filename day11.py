# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

import copy

# Create nested list with all seats.
with open('day11input') as f:
    seatRows = f.read().splitlines()
allSeats = []
for i in range(0,len(seatRows)):
    allSeats.append(list(seatRows[i]))


# Check wether all the surrounding seats are either empty (L) or floor (.)
def check_if_surrounding_seats_empty(y, x):
    global allSeats
    surroundingseatcoordinates = []
    validcoordinates = []
    # Find all adjacent coordinates.
    for i in range(-1, 2):
        for j in range(-1, 2):
            surroundingseatcoordinates.append([y+i, x+j])
    # Select coordinates that aren't outside the map.
    for coord in surroundingseatcoordinates:
        if not (coord[0] < 0 or coord[1] < 0 or coord[0] >= len(allSeats) or coord[1] >= len(allSeats[0])):
            validcoordinates.append(coord)
    # Checks if valid coordinates are empty or floor. If a taken seat is found, return False.
    for coord in validcoordinates:
        if allSeats[coord[0]][coord[1]] == '#':
            return False
    return True

def check_if_four_adjacent_seats_are_occupied(y, x):
    global allSeats
    surroundingseatcoordinates = []
    validcoordinates = []
    # Find all adjacent coordinates.
    for i in range(-1, 2):
        for j in range(-1, 2):
            surroundingseatcoordinates.append([y + i, x + j])
    # Select coordinates that aren't outside the map.
    for coord in surroundingseatcoordinates:
        if not (coord[0] < 0 or coord[1] < 0 or coord[0] >= len(allSeats) or coord[1] >= len(allSeats[0])):
            if not coord == [y, x]:
                validcoordinates.append(coord)
    # Check if at least four surround seats are occupied.
    occupiedTotal = 0
    for coord in validcoordinates:
        if allSeats[coord[0]][coord[1]] == '#':
            occupiedTotal += 1
    if occupiedTotal >= 4:
        return True
    else:
        return False


# Returns the new status of a single seat based on the surrounding seats. Notice coordinates are y,x.
def update_seat(y, x):
    global allSeats
    if allSeats[y][x] == '.':
        return '.'
    if allSeats[y][x] == 'L':
       if check_if_surrounding_seats_empty(y,x):
           return '#'
       else:
           return 'L'
    if allSeats[y][x] == '#':
        if check_if_four_adjacent_seats_are_occupied(y,x):
            return 'L'
        else:
            return '#'



# Store each changed seat into a new list, and then replace the main map with the new one.
# Returns False if nothing changes
def update_all_seats():
    global allSeats
    # Create an empty seat map.
    new_seat_map = copy.deepcopy(allSeats)
    for i in range(0,len(allSeats)):
        for j in range(0,len(allSeats[0])):
            new_seat_map[i][j] = update_seat(i, j)
    if new_seat_map == allSeats:
        print("hej")
        return False
    else:
        allSeats = copy.deepcopy(new_seat_map)
        return True


# Update the list until it no longer changes.
while True:
    if not update_all_seats():
        finalMap = copy.deepcopy(allSeats)
        break

# Count occupied seats in final map.
totalOccupiedSeats = 0
for row in allSeats:
    for seat in row:
        if seat == '#':
            totalOccupiedSeats += 1
print(totalOccupiedSeats)







import copy

# Create nested list with all seats.
with open('day11input') as f:
    seatRows = f.read().splitlines()
allSeats = []
for i in range(0, len(seatRows)):
    allSeats.append(list(seatRows[i]))


# Returns the result of updating a single seat.
def update_seat(y, x):
    global allSeats
    if allSeats[y][x] == '.':
        return '.'
    if allSeats[y][x] == 'L':
        if check_for_all_empty_seats(y, x):
            return '#'
        else:
            return 'L'
    if allSeats[y][x] == '#':
        if check_for_five_occupied_seats(y, x):
            return 'L'
        else:
            return '#'


# Checks if at least five of the seen seats are occupied.
def check_for_five_occupied_seats(y, x):
    seenseats = find_seen_seats(y, x)
    totaloccupied = 0
    for seat in seenseats:
        if seat == '#':
            totaloccupied += 1
    if totaloccupied >= 5:
        return True
    else:
        return False


# Checks if the seen seats are all empty.
def check_for_all_empty_seats(y, x):
    seenseats = find_seen_seats(y, x)
    for seat in seenseats:
        if seat == '#':
            return False
    return True


# Return all seen seats.
def find_seen_seats(y, x):
    seenseats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            seenseats.append(find_seat_in_direction(y, x, i, j))
    return seenseats


# Find the first seen seat in a certain direction. Returns the type.
def find_seat_in_direction(y, x, dy, dx):
    global allSeats
    distance = 1
    while True:
        currentcoords = [y+dy*distance, x+dx*distance]
        if out_of_bounds(*currentcoords):
            return "oob"
        if allSeats[currentcoords[0]][currentcoords[1]] == 'L':
            return 'L'
        if allSeats[currentcoords[0]][currentcoords[1]] == '#':
            return '#'
        distance += 1


# Returns true if coordinates are outside the map.
def out_of_bounds(y, x):
    if y < 0 or y >= len(allSeats):
        return True
    if x < 0 or x >= len(allSeats[0]):
        return True
    return False


# Goes through each seat and updates them, storing the result in a new map. Then replaces the old with the new map.
def update_all_seats():
    global allSeats
    new_seats = copy.deepcopy(allSeats)
    for i in range(0, len(allSeats)):
        for j in range(0, len(allSeats[0])):
            new_seats[i][j] = update_seat(i, j)
    if new_seats == allSeats:
        return False
    else:
        allSeats = new_seats
        return True


# Updates the map until it no longer changes (and update_all_seats returns False)
while True:
    if not update_all_seats():
        finalMap = copy.deepcopy(allSeats)
        print("Done!")
        break
print(allSeats)

# Counts the amount of occupied seats in the final seating map.
occupiedTotal = 0
for i in range(len(allSeats)):
    for j in range(len(allSeats[0])):
        if finalMap[i][j] == "#":
            occupiedTotal += 1
print(occupiedTotal)

with open('day3input') as f:
    slope = f.read().splitlines()

slopeWidth = len(slope[0])
slopeLength = len(slope)
currentX = 1
currentY = 1


# Moves the sled one step down and three to the right.
def move_once(x,y):
    global currentX
    global currentY
    # Move three steps to the right, and start over if the edge is reached.
    currentX += x
    if currentX > slopeWidth:
        currentX = currentX - slopeWidth
    # Move down one step
    currentY += y


# Moves a step and checks for a tree each loop. Ends when the Y-position is below the slope.
def try_slope(x, y):
    global slope
    global slopeLength
    global slopeWidth
    global currentY
    global currentX
    currentY = 1
    currentX = 1
    treecount = 0
    while True:
        move_once(x, y)
        if currentY > slopeLength:
            print('End of slope!')
            print(treecount)
            return treecount
        elif slope[currentY-1][currentX-1] == '#':
            treecount += 1


firstSlope = try_slope(1, 1)
secondSlope = try_slope(3, 1)
thirdSlope = try_slope(5, 1)
fourthSlope = try_slope(7, 1)
fifthSlope = try_slope(1, 2)

print('Result:')
print(firstSlope*secondSlope*thirdSlope*fourthSlope*fifthSlope)

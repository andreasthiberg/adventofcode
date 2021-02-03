with open('day9input') as f:
    numbersList = f.read().splitlines()

numbersList = [int(i) for i in numbersList]


# Checks wether a given item in the list matches the criteria.
def check_if_valid(index):
    startingindex = index-25
    for i in range(25):
        for j in range(25):
            if numbersList[i+startingindex]+numbersList[j+startingindex] == numbersList[index]:
                if numbersList[i+startingindex] != numbersList[j+startingindex]:
                    return True
    return False


# Go through all the numbers until one is found that doesn't match the criteria. Returns that number.
def find_invalid_number():
    global numbersList
    for i in range(25, len(numbersList)):
        if not check_if_valid(i):
            return numbersList[i]


print(find_invalid_number())
invalidNumber = find_invalid_number()


# Find a range of contigous numbers in the list that add up to the given number.
def find_conigious_sum(number):
    for i in range(len(numbersList)):
        currentnumbers = [numbersList[i]]
        currentsum = numbersList[i]
        for j in range(i+1, len(numbersList)):
            currentsum += numbersList[j]
            currentnumbers.append(numbersList[j])
            if currentsum == number:
                return currentnumbers
            elif currentsum > number:
                break


contigousNumbers = find_conigious_sum(invalidNumber)
contigousNumbers.sort()
print(contigousNumbers[0]+contigousNumbers[-1])

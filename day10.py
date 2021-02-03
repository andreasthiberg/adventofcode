import itertools

with open('day10input') as f:
    adapterList = f.read().splitlines()
adapterList = [int(i) for i in adapterList]
adapterList.sort()

# Add adapter and charging port
adapterList.append(adapterList[-1]+3)
adapterList.insert(0, 0)

oneDifference = 0
threeDifference = 0
# Check difference between every number and add to counts.
for i in range(1, len(adapterList)):
    if adapterList[i] - adapterList[i-1] == 3:
        threeDifference += 1
    elif adapterList[i] - adapterList[i-1] == 1:
        oneDifference += 1


def split_into_subsequences(adapterlist):
    newlist = []
    slicestartindex = 0
    for i in range(1, len(adapterlist)):
        if adapterlist[i]-adapterList[i-1] == 3:
            newlist.append(adapterList[slicestartindex:i])
            slicestartindex = i
    return newlist


# Check if a variation matches the criteria.
def check_validity(variation):
    for i in range(1, len(variation)):
        if variation[i]-variation[i-1] > 3:
            return False
    return True


# Check number of possible variation for a short subsequence. Warning - duct-tape code.
def check_variations(subsequence):
    if len(subsequence) == 1 or len(subsequence) == 2:
        return 1
    if len(subsequence) == 3:
        subsequence.pop(1)
        if check_validity(subsequence):
            return 2
        return 1
    if len(subsequence) == 4 or len(subsequence) == 5:
        variations = []
        total = 0
        variations.append(subsequence.copy())
        variations.append([subsequence[0], subsequence[-1]])
        for i in range(1, len(subsequence)-2):
            for x in (itertools.combinations(subsequence[1:-1], i)):
                newlist = [subsequence[0]]
                for y in x:
                    newlist.append(y)
                newlist.append(subsequence[-1])
                variations.append(newlist)
        for variation in variations:
            if check_validity(variation):
                total += 1
        return total


subsequences = split_into_subsequences(adapterList)
variationsTotal = 1
# Multiplies the possible variations for each subset.
for sub in subsequences:
    variationsTotal = variationsTotal * check_variations(sub)
print(variationsTotal)

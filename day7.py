# Create list from input where each item is a complete rule.
with open('day7input') as f:
    rawBagRules = f.read().splitlines()

# Create list where each item is a list with two items - the bigger bag and the contained bags.
splitBagRules = []
for rule in rawBagRules:
    splitBagRules.append(rule.split(" contain "))

validBags = ['shiny gold bag']

# Loops that goes through each rule to see if it fits the bags we currently know can contain a golden bag.
# Those bags are then added to the list of allowed bags. The loop ends when no new bags are found.
while True:
    newBags = []
    validBagsNewVersion = validBags[:]
    for rule in splitBagRules:
        for bag in validBags:
            if bag in rule[1]:
                newBags.append(rule[0][:-1])
    for bag in newBags:
        if bag not in validBagsNewVersion:
            validBagsNewVersion.append(bag)
    if validBagsNewVersion == validBags:
        break
    else:
        validBags = validBagsNewVersion[:]

print('The amount of bags that can fit a shiny gold bag is: ' + str((len(validBags) - 1)))


# Second part.


# Lists all the bags that a single bag contains. Multiple bags of the same color means multiple items.
# Returns list where each item is a a single bag.
def list_bags(rule):
    containedbags = rule[1][:]
    separatedbags = []

    if containedbags[0] == 'n':
        return []
    else:
        sortedbags = (containedbags.split(', '))
        for bag in sortedbags:
            amount = int(bag[0])
            for i in range(amount):
                separatedbags.append(bag[2:])

        # Get rid of the periods.
        separetedbagswithoutperiod = []
        for bag in separatedbags:
            if bag[-1] == '.':
                separetedbagswithoutperiod.append(bag[:-1])
            else:
                separetedbagswithoutperiod.append(bag)
        return separetedbagswithoutperiod


totalBags = []
currentBags = ['shiny gold bags']
newBags = []

# Loop that goes through the rulelist, adding more bags to the total tally.
# Then uses the newly added bags for another round, until there are no new bags.
while True:
    for bag in currentBags:
        for rule in splitBagRules:
            if bag in rule[0]:
                newBags.extend(list_bags(rule))
    for bag in currentBags:
        totalBags.append(bag)
    if newBags == []:
        break
    else:
        currentBags = newBags[:]
        newBags = []

print('The total amount of bags packed into your golden bag is: ' + str(len(totalBags)-1))





# Create list of groups where each item is a smaller list with every person's answer.
with open('day6input') as f:
    rawGroupList = f.read().split('\n\n')
    groupList = []
    rawGroupListWithoutLineBreaks = []
    for group in rawGroupList:
        groupList.append(group.split('\n'))
    for group in rawGroupList:
        rawGroupListWithoutLineBreaks.append(group.replace('\n', ''))

# Calcuate total sum of any questions that someone answered yes to in each group.
totalSumAnyPerson = 0
for group in rawGroupListWithoutLineBreaks:
    totalSumAnyPerson += len(set(group))
print(totalSumAnyPerson)

# Calculate total sum of questions that everyone in a group answered yes to.
totalSumEveryPerson = 0
for group in groupList:
    setList = []
    for i in group:
        setList.append(set(i))
    commonAnswers = set.intersection(*setList)
    totalSumEveryPerson += len(commonAnswers)
print(totalSumEveryPerson)
import copy

# Reads input into list
with open('day8input') as f:
    instructionListRaw = f.read().splitlines()

# Creates list where each input is split into a separate list of two items, type and number.
instructionListSplit = []
for inst in instructionListRaw:
    instructionListSplit.append(inst.split(' '))

# The accumulator variable and the current (index) position.


# Loops that checks if a program loops. First controls the type and acts accordingly.
# The checks the new position against a list of all previous. Returns False if there's a repition.
# If the program has reached the end returns True.

def check_for_loop(instructions):
    currentPos = 0
    allPreviousPositions = []
    while True:
        # Follows intruction.
        allPreviousPositions.append(currentPos)
        if instructions[currentPos][0] == 'acc':
            currentPos += 1
        elif instructions[currentPos][0] == 'jmp':
            currentPos += int(instructionListSplit[currentPos][1])
        elif instructions[currentPos][0] == 'nop':
            currentPos += 1
        # Checks for repeat position or for termination.
        if currentPos in allPreviousPositions:
            return False
        elif currentPos >= (len(instructions)):
            return True


# Checks each variation of given instructions.
def check_varations(instructions):
    for i in range(len(instructions)):
        new_instructions = copy.deepcopy(instructions)
        if instructions[i][0] == 'jmp':
            new_instructions[i][0] = 'nop'
            if check_for_loop(new_instructions):
                count_acc(new_instructions)
        elif instructions[i][0] == 'nop':
            new_instructions[i][0] = 'jmp'
            if check_for_loop(new_instructions):
                count_acc(new_instructions)

def count_acc(instructions):
    acc = 0
    currentPos = 0
    while True:
        print(acc)
        print(currentPos)

        if currentPos >= (len(instructions)):
            return acc
        # Follows instruction.
        if instructions[currentPos][0] == 'acc':
            acc += int(instructions[currentPos][1])
            currentPos += 1
        elif instructions[currentPos][0] == 'jmp':
            currentPos += int(instructionListSplit[currentPos][1])
        elif instructions[currentPos][0] == 'nop':
            currentPos += 1


check_varations(instructionListSplit)








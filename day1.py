# Specifically, they need you to find the two entries that sum to 2020
# and then multiply those two numbers together.

# Add numbers from textfile into a list.
with open('day1input') as f:
    expenses = []
    for line in f:
        expenses.append(int(line))


# Check which two numbers in the list equal 2020 when added together, then print the product of those two numbers.
def checktwonumbers():
    for i in expenses:
        for j in expenses:
            if i + j == 2020:
                print(str(i) + ' + ' + str(j) + ' = ' + str(i+j))
                print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
                return


# The same but for three numbers.
def checkthreenumbers():
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if i + j + k == 2020:
                    print(str(i) + ' + ' + str(j) + ' + ' + str(k) + ' = ' + str(i + j + k))
                    print(str(i) + ' * ' + str(j) + ' * ' + str(k) + ' = ' + str(i * j * k))
                    return


checktwonumbers()
checkthreenumbers()

# First rule: The password policy indicates the lowest and highest number of times
# a given letter must appear for the password to be valid. For example, 1-3 a means that
# the password must contain a at least 1 time and at most 3 times.

# Second rule. Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second character, and so on.
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter.
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

validPasswordCountOne = 0
validPasswordCountTwo = 0

# Enter list of day2input and rules into list.
with open('day2input') as f:
    passwordInfo = f.read().splitlines()


# Checks if a single password meets the first criteria.
def check_password_first_rule(minamount, maxamount, letter, password):
    lettercount = 0
    for i in password:
        if i == letter:
            lettercount += 1
    if minamount <= lettercount <= maxamount:
        return True
    else:
        return False


# Checks if a single password meets the second criteria.
def check_password_second_rule(firstpos, secondpos, letter, password):
    if password[firstpos-1] == letter:
        if password[secondpos-1] == letter:
            return False
        else:
            return True
    else:
        if password[secondpos - 1] == letter:
            return True
        else:
            return False


# For each item in the password list, split it up into variables and run the first checking function.
# Adds one to validPasswordCountOne for each True return.
for i in passwordInfo:
    numberrange, letterpluscolon, password = i.split(' ')
    firstnumber, secondnumber = numberrange.split('-')
    letter = letterpluscolon[0]
    if check_password_first_rule(int(firstnumber), int(secondnumber), letter, password):
        validPasswordCountOne += 1
    if check_password_second_rule(int(firstnumber), int(secondnumber), letter, password):
        validPasswordCountTwo += 1
        print(firstnumber)
        print(secondnumber)
        print(letter)
        print(password)
        print(i)

# Print the results.
print(validPasswordCountOne)
print(validPasswordCountTwo)

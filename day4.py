passportList = []
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Loads source info into list, one block in each item, each value separated by a space (removing linebreaks)
with open('day4input') as f:
    passportData = f.read().split('\n\n')
for i in range(len(passportData)):
    passportData[i] = passportData[i].replace('\n', ' ')


# Adds a passport to the passports-list using a string of data.
def create_passport(data):
    global passportList
    newpassport = {}
    fields = data.split(' ')
    for i in fields:
        singlefield = i.split(':')
        newpassport[singlefield[0]] = singlefield[1]
    passportList.append(newpassport)


# Checks if a given passport dictionary is valid, i.e. has all required fields.
def validity_check(passport):
    global passportList
    global requiredFields

    for field in requiredFields:
        if field not in passport:
            return False

    if not value_check(passport):
        return False

    return True


# Function that checks each value for certain criteria. Each field has its own function.
def value_check(passport):
    if not birth_year_check(passport['byr']):
        return False
    elif not issue_year_check(passport['iyr']):
        return False
    elif not expiration_year_check(passport['eyr']):
        return False
    elif not height_check(passport['hgt']):
        return False
    elif not hair_color_check(passport['hcl']):
        return False
    elif not eye_color_check(passport['ecl']):
        return False
    elif not passport_id_check(passport['pid']):
        return False
    else:
        return True


def birth_year_check(value):
    if not value.isdigit():
        return False
    if 1920 <= int(value) <= 2002:
        return True
    else:
        return False


def issue_year_check(value):
    if not value.isdigit():
        return False
    if 2010 <= int(value) <= 2020:
        return True
    else:
        return False


def expiration_year_check(value):
    if not value.isdigit():
        return False
    if 2020 <= int(value) <= 2030:
        return True
    else:
        return False


def height_check(value):
    if value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193:
        return True
    elif value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76:
        return True
    else:
        return False


def hair_color_check(value):
    if not value[0] == '#':
        return False
    if not len(value) == 7:
        return False
    for char in value[1:]:
        if not 48 <= ord(char) <= 57 and not 97 <= ord(char) <= 102:
            return False
    return True


def eye_color_check(value):
    allowed_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in allowed_colors:
        return True
    else:
        return False


def passport_id_check(value):
    if not value.isdigit():
        return False
    if not len(value) == 9:
        return False
    return True


# Creates passports using all the data.
for data in passportData:
    create_passport(data)

# Checks if each passport is valid, and counts them.
validCount = 0
for passport in passportList:
    if validity_check(passport):
        validCount += 1

print(validCount)

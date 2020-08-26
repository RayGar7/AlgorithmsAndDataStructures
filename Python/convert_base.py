# convert_to_base() converts a string representation of a hex, binary or octogonal to base 10
# num:string is the number to convert to base as an int
# base:int is the base. Logically works for values 16, 8 and 2 and there is an excetion raised for every other kind of value
# current asymptotic time complexity: O(n)
# I will make the assumption that if a user enters a value for num in the form of a hexadecimal number then the base will always be in hexadecimal


def convert_to_base_10(num, base):
    value = 0

    if (type(base) is str):
        base = int(base)

    if (base == 16 or base == 2 or base == 8):
        # convert to uppercase
        num = num.upper()
        i = len(num) - 1
        e = 0
        while i >= 0:
            value += getDigit(num[i]) * base ** e
            i -= 1
            e += 1
    else:
        raise Exception("The base can only be equal to 16, 2, or 8.")

    return value

# Converts a single digit to its int representation


def getDigit(strDigit):
    digits_table = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    return digits_table[strDigit]


# test
#print(convert_to_base_10("1100", "2"))
print(convert_to_base_10("7dE", 16))

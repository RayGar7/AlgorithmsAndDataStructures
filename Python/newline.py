def newline(value, arg):
    """ Adds a newline to the value once after every arg characters """
    # assert arg cannot be equal to zero: it will raise a division by zero excpetion and it also makes no sense
    # assert no negative characters
    new_value = ""
    for i in range(0, len(value)):
        new_value += value[i]
        if (i % arg == 0 and i != 0):
            # insert newline
            new_value += " <br> "
            
    return new_value

print(newline("Hello world!", 5))
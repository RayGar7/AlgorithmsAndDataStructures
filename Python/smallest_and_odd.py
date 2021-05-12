def get_smallest_odd(numlist):
    oddcount = 0
    smallest = float('inf')
    for num in numlist:
        if (num % 2) != 0:
            oddcount += 1
            if num < smallest:
                smallest = num

    return oddcount, smallest
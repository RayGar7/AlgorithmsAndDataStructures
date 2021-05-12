# Complete the hourglassSum function below.
def hourglassSum(arr):
    hour_glasses = []
    print(get_hour_glass(arr, 0, 1))
    r = 0
    c = 0
    
    while (r < 4):
        c = 0
        while (c < 4):
            hour_glasses.append(get_hour_glass(arr, r, c))
            c += 1
        r  += 1
    # now we have an array with the sums of each hourglass
    # so we just have to find the max value which is a trivial operation

    return max(hour_glasses)


# gets the sum for any given hourglass, represented by the first row and column values
# O(1)
def get_hour_glass(arr, start_row, start_column):
    r = start_row
    c = start_column
    sum = 0
    # for any hourglass where i = start_row and j = start_column and m = arr
    # m[ri][cj] is the first cell to add and
    # m[ri+2][cj+2] is the last cell to add

    sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] +arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
    return sum




# sample
sample = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
get_hour_glass(sample, 0, 1)
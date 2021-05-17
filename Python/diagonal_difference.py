# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is abs(15 - 17) = 2. 


def diagonalDifference(arr):
    n = len(arr)
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    
    for i in range(0, n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n-1-i]
    return abs(left_diagonal_sum - right_diagonal_sum)

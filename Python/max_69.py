# Given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.


class Solution:
    def maximum69Number (self, num: int) -> int:
        max_digit = str(num)
        num_str = str(num)
        for i in range(0, len(num_str)):
            if (num_str[i] == '6'):
                max_digit = num_str[0:i] + '9' + num_str[i+1:]
                break
        return int(max_digit)
        
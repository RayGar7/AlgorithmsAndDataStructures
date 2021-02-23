# make a regex that returns true if a string, s, is in 24 hour time format.

# examples of a valid time string:
# 09:21:22
# 9:01:01
# 23:59:59

import re

def is_valid_time(s):
    regex = "^[0-2]{0,1}\d\:[0-5]\d\:[0-5]\d$"


    return True if re.search(regex, s) else False

# all ok
# print(is_valid_time("00:00:00"))
# print(is_valid_time("09:21:22"))
# print(is_valid_time("9:01:01"))
# print(is_valid_time("23:59:59"))
# print(is_valid_time("009:01:01"))
# print(is_valid_time("23:69:59"))
# print(is_valid_time("23:59:69"))
# print(is_valid_time("00:00:00d"))
# print(is_valid_time("00;00;00"))

# make a regex that returns true if a string, s, is in 12 hour format:
# example of a valid time string in 12 hour format

# 01:12:12 PM
# 01:12:12PM
# 01:12:12 AM
# 01:12:12AM
# 12:59:59 PM
# 1:12:12 PM

def is_valid_time_12_hour(s):
    regex = "^((0?\d)|(1(1|2))):[0-5]\d:[0-5]\d(\s)?(A|P)M$"


    return True if re.search(regex, s) else False

print(is_valid_time_12_hour("01:12:12 PM"))
print(is_valid_time_12_hour("01:12:12PM"))
print(is_valid_time_12_hour("01:12:12 AM"))
print(is_valid_time_12_hour("01:12:12AM"))
print(is_valid_time_12_hour("12:59:59 PM"))
print(is_valid_time_12_hour("9:12:12 PM"))
print(is_valid_time_12_hour("09:12:12 PM"))


print(is_valid_time_12_hour("09:12:12"))
print(is_valid_time_12_hour("19:12:12 PM"))
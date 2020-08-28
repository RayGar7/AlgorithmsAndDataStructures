

# "There are three types of edits that can be performed on strings: insert a character, remove a character,
# or replace a character. Given two strings write a function to see if they are one edit awy from being the same character." - Gayle Laakman McDowell
# in "Cracking the Coding Interview" 6th edition
# 8/27/2020 9:04 every test case in the book has passed

def one_away(str1, str2):
    # if strings are zero edits away:
    if str1 == str2:
        return True
    # if either string has one character appended from the other
    if str1 in str2 or str2 in str1:
        return True

    # if either string has a remove edit from the other string
    # ie. pale, ple => true
    if isARemoveEdit(str1, str2) or isARemoveEdit(str2, str1):
        return True

    # replace a character
    if isAReplaceEdit(str1, str2):
        return True

    # if all of these fail return False
    return False


def isAReplaceEdit(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        differentCharacters = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                differentCharacters += 1
                if differentCharacters > 1:
                    return False

        return differentCharacters == 1


def isARemoveEdit(s1, s2):
    if len(s1) != len(s2) - 1:
        return False
    # if s1 is precisely one character shorter than s2:
    # check if every character in s1 is in s2
    for c in s1:
        if c not in s2:
            return False
    return True


print(one_away("abd", "abcd"))

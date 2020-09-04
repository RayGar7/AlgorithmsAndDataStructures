# return true iff str1 and str2 are permutations of each other
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str_dict1 = {}
    str_dict2 = {}
    str_dict1.keys

    for c in str1:
        if c not in str_dict1.keys():
            str_dict1[c] = 1
        else:
            str_dict1[c] += 1

    for c in str2:
        if c not in str_dict2.keys():
            str_dict2[c] = 1
        else:
            str_dict2[c] += 1

    return str_dict1 == str_dict2

# todo write a function to calculate how many permutations a given string has

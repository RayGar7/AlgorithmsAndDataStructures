def all_unique_in_place(s):
    for i in range(0, len(s)):
        if s[i] in s[0:i] + s[i+1:]:
            return False
    return True


print(all_unique_in_place("bat"))
print(all_unique_in_place("b"))
print(all_unique_in_place("bab"))


def all_unique(s):
    s_dict = {}
    for c in s:
        if (c not in s_dict.keys()):
            s_dict[c] = 1
        else:
            return False
    return True


print(all_unique("bat"))
print(all_unique("b"))
print(all_unique("bab"))

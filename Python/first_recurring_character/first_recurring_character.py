# return the first occurence of a character in a string, if there are no duplicate characters in a string return None
# O(n) 
def main(s):
    my_list = []
    for c in s:
        if c not in my_list:
            my_list.append(c)
        else:
            return c

    return None


#print(main("ACB"))

# same problem but in place
# O(n^2)
def in_place(s):
    i = 1
    while i < len(s):
        j = 0
        while j < i:
            if (s[i] == s[j]):
                return s[i]
            j += 1
        i +=1
    return None

print(in_place("BCAA"))
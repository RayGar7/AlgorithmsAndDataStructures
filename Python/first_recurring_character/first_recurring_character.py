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


#print(main("ACCB"))

# same problem but in place
# O(n^2)
# def in_place(s):
#     i = 1
#     while i < len(s):
#         j = 0
#         while j < i:
#             if (s[i] == s[j]):
#                 return s[i]
#             j += 1
#         i +=1
#     return None

# this is the same implementation as the previous problem but with a shorter syntax
def in_place(s):
    for i in range(1, len(s)):
        for j in range(0, i):
            if (s[i] == s[j]):
                return s[i]
    return None
    
# the same problem but with a hash map
# note: geeksforgeeks calls it a hash map but there's no hash function so I don't understand how it can be a hash map
def firstRepeatedChar(str): 
    h = {} 
 
    for ch in str:
        if ch in h.keys():
            return ch
        else:
            h[ch] = 1
 
    return None

print(firstRepeatedChar("BCAA"))
print(firstRepeatedChar("B"))
print(firstRepeatedChar("BB"))
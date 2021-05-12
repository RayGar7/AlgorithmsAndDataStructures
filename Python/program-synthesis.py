# Most candidates cannot solve this problem:
# Input: "aaaabbbcca"
# Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

def program_synthesis(x):
    i = 0
    current_character = x[0]
    current_character_counter = 0
    result = []
    while (i < len(x)):
        if (x[i] == current_character):
            current_character_counter += 1

        elif (x[i] != current_character):
            result.append((current_character, current_character_counter))
            current_character = x[i]
            current_character_counter = 1
        i += 1


    result.append((current_character, current_character_counter))

    return result

print(program_synthesis("aaaabbbcca"))
print(program_synthesis("xxyyz"))
print(program_synthesis("abc"))
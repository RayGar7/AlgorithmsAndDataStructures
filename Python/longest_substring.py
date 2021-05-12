
def lengthOfLongestSubstring(s):
    current_character = s[0]
    current_character_count = 1
    max_count = current_character_count
    i = 1

    while (i < len(s)):
        if (s[i] == current_character):
            current_character_count += 1
            max_count = max_count if max_count >= current_character_count else current_character_count
        else:
            current_character = s[i]
            current_character_count = 1
        i += 1
    return current_character_count
        

        

print(lengthOfLongestSubstring("abcabbcbbbb"))
def urlify(s):
    url = ""
    isPreviousCharacterAWhitespace = False
    for i in range(0, len(s)):
        # If the current character is a whitespace and there is not an extra one in sequence...
        # that means that we should replace the whitespace character with a "%20"
        if(s[i] == " " and not isPreviousCharacterAWhitespace):
            url += "%20"
            isPreviousCharacterAWhitespace = True
        # if the current character is not a whitespace it should be left as is in the url and reset the flag
        # for checking whitespace
        elif(s[i] != " "):
            url += s[i]
            isPreviousCharacterAWhitespace = False

        # else if the current character is a whitespace and the flag is set to true, just ignore it

    # If there is an extra "%20 at the end it needs to be removed"
    if (url[-3:] == "%20"):
        url = url[0:len(url)-3]

    return url


# Show test case from Cracking the Interview
print(urlify("Mr John Smith     "))

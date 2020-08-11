def findduplicate(L):
    templist = []
    duplicates = []
    for x in L:
        if(x in templist):
            duplicates.append(x)
        templist.append(x)
    return duplicates

def findFirstDuplicate(L):
    templist = []
    for x in L:
        if(x in templist):
            return x
        templist.append(x)

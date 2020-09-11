# I've realized that matrix operations are one place where I struggle a lot
# so this file will be a container for me to have as reference for cmon 2Dimensional problems
def checkMembership(M, data):
    for i in range(0, len(M)):
        for j in range(0, len(M[0])):
            if (M[i][j] == data):
                return (i, j)


m1 = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
print(checkMembership(m1, 4)) # (1,0)

print(4 in m1) # will print False because m1 is a list that doesn't have any numbers in it, instead it only has lists, that is why we need to loop through each row to check memberships
# this is wrong I really need help with this kind of problem

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    # Write your code here
    options = 0

    # try something with a sort:
    priceOfJeans = my_sort(priceOfJeans)
    print(priceOfJeans)


    # brute force (only passes 8/13 test cases)
    for i in range(0, len(priceOfJeans)):
        for j in range(0, len(priceOfShoes)):
            if (priceOfJeans[i] + priceOfShoes[j] > budgeted):
                break
            for k in range(0, len(priceOfSkirts)):
                if (priceOfJeans[i] + priceOfShoes[j] + priceOfSkirts[k] > budgeted):
                    break
                for l in range(0, len(priceOfTops)):
                    if (priceOfJeans[i] + priceOfShoes[j] + priceOfSkirts[k] + priceOfTops[l] <= budgeted):
                        options += 1


    return options


# implements selection sort O(n^2)
def my_sort(l):
    sorted_l = l
    for i in range(0, len(sorted_l)):
        min = i
        for j in range(i + 1, len(sorted_l)):
            if (sorted_l[min] > sorted_l[j]): 
                min = j
            
        if (min != i):
            swap(sorted_l, min, i)
        
    return sorted_l


def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def reverse(l):
    reversed_l = []
    i = len(l) - 1
    while (i >= 0):
        reversed_l.append(l[i])
        i -= 1


a1 = [1,2,3,4,5,6,7,8]
a1 = [1,2,3,4,5,6,7,8]
a1 = [1,2,3,4,5,6,7,8]
a1 = [1,2,3,4,5,6,7,8]
print(getNumberOfOptions(a1,a1,a1,a1,100))
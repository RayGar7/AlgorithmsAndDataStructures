def concat(L):
    #mu = len(L)
    
    if (len(L) == 0): return L
    #base case: L is empty
    else: return head(L) + (concat(tail(L)))
    #recursive case: L is not empty and therefore must concatenate the tail



def tail(L): return L[1:]

def head(L): return L[0]

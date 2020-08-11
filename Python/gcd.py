# gcd: int x int -> int
# return the greatest common divisor between two integers m and n
def gcd(m,n):
    r = m % n
    
    if(r == 0):
        return n
    else:
        m = n
        n = r
        gcd(m, n)
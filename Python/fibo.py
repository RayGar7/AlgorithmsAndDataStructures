#fibo: int n -> int fibo(n)
def fibo(n):
    if (n==0): return 0
    elif (n == 1): return 1
    else: return fibo(n-1) + fibo(n-2)


# using the interactive Python interpreter the following test cases produce the results
# fibo(0) == 0
# fibo(1) == 1
# fibo(2) == 1
# fibo(3) == 2
# fibo(4) == 3
# fibo(5) == 5
# fibo(10) == 55

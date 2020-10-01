#A series of numbers in which each number is the
#sum of the two proceeding numbers. The simplest 
#is the number 1, 1, 2, 3, 5, 8...

def fib(n):
    """Fibonacci sequence."""
    if n < 2:
        return n

    #using recursion
    return fib(n-1) + fib(n-2)

print(fib(8))

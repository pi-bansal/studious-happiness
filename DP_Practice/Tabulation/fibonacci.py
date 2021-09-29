def fib(n):
    # All zeroes in initial table
    fib_table = [0] * (n+1)
    fib_table[1] = 1

    # Iterate over range.
    # Tried the enumerate() but it keeps a copy of zeroes
    for i in range(0, n-1):
        #Stop at (n-2) index i.e. till last but one element 
        num = fib_table[i]
        fib_table[i + 1] = fib_table[i + 1] + num
        fib_table[i + 2] = fib_table[i + 2] + num
        print(fib_table[:i+2])
    else:
        # For the last element
        fib_table[-1] +=  fib_table[-2]
    return fib_table

print(fib(5))
print(fib(10))
print(fib(50))
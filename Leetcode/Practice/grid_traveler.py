def grid_traveler(m, n, memo = {}):
    # Why is this slower
    # key = frozenset([m, n])
    key = (m, n)
    if key in memo:
        return memo[key]
    if ( m == 1 and n == 1 ):
        return 1
    if (m == 0 or n == 0):
        return 0
    
    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]


# import timeit
# print(timeit.timeit('[grid_traveler(*coordinates) for coordinates in [(2,3),(3,3),(5,5),(10,10),(20,20)]]', globals=globals()))

print(grid_traveler(2,3))
print(grid_traveler(3,2))
print(grid_traveler(5,5))
print(grid_traveler(100,100))
import sys
sys.setrecursionlimit(1500)

def can_sum(target_sum, numbers, memo = {}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7,[3,4,5]))
print(can_sum(7,[2,4,5]))
print(can_sum(300,[7, 14]))


# import timeit
# print(timeit.timeit('[can_sum(*args) for args in [(7,[3,4,5]),(97,[3,4,5]),(300,[7,14])]]', globals=globals()))
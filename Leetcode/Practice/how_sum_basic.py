def how_sum(target_sum, numbers):
    """Function that return a subset of numbers that adds up to the target_sum"""

    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        return_val = how_sum(remainder, numbers)
        if return_val != False:
            return_val.append(num)
            return return_val
    return False


print(how_sum(7,[3,4,5]))
print(how_sum(7,[2,4,5]))
print(how_sum(300,[7, 14]))

# import timeit
# print(timeit.timeit('[how_sum(*args) for args in [(7,[3,4,5]),(97,[3,4,5]),(300,[7,14])]]', globals=globals()))
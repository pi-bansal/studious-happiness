def best_sum(target_sum, numbers):
    """Function that returns a shortest subset of numbers that adds up to the target_sum"""

    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        result_combination = best_sum(remainder, numbers)
        if result_combination != None:
            result_combination.append(num)
            if (shortest_combination == None) or (len(shortest_combination) > len(result_combination)):
                shortest_combination = result_combination
        
    return shortest_combination


# print(best_sum(7, [5, 3, 4, 7])) #[7]
# print(best_sum(8, [2, 3, 5])) #[3, 5]
# print(best_sum(8, [1, 4, 5])) #[4, 4] - Not highest [5, 1, 1, 1]
print(best_sum(4, [1, 2, 5, 25])) #[25, 25, 25, 25]
# print(best_sum(100, [1, 2, 5, 25])) #[25, 25, 25, 25]

# import timeit
# print(timeit.timeit('[best_sum(*args) for args in [(7,[3,4,5]),(97,[3,4,5]),(300,[7,14])]]', globals=globals()))
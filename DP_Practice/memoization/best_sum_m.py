def best_sum(target_sum, numbers, memo = {}):
    """Function that returns a shortest subset of numbers that adds up to the target_sum"""

    # print('Args: ', target_sum, numbers, memo)

    if target_sum in memo:
        return list(memo[target_sum])

    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        temp_list = []
        result_combination = best_sum(remainder, numbers, memo)
        # print(result_combination, target_sum, remainder, memo)
        if result_combination != None:
            # DON'T use the result_combination directly as it is a return value from the memo.
            # Due to referencing (same address), it changes the existing value in the memo
            temp_list = result_combination[:]
            temp_list.append(num)
            # print(target_sum, memo, shortest_combination, result_combination, temp_list)
            if (shortest_combination == None) or (len(shortest_combination) > len(temp_list)):
                shortest_combination = temp_list
                # shortest_combination = result_combination
    
    memo[target_sum] = shortest_combination
    # memo[target_sum] = shortest_combination
    print( target_sum, memo[target_sum], shortest_combination)
    return memo[target_sum]


# print(best_sum(7, [5, 3, 4, 7])) #[7]
# print(best_sum(8, [2, 3, 5])) #[3, 5]
# print(best_sum(8, [1, 4, 5])) #[4, 4] - Not highest [5, 1, 1, 1]
print(best_sum(5, [1, 2, 5, 25])) #[25, 25, 25, 25]
print(best_sum(100, [1, 2, 5, 25])) #[25, 25, 25, 25]
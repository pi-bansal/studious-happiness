def best_sum(target_sum, numbers):
    # Expected return is an array of integers that add up to target_sum
    if target_sum == 0:
        # Zero using empty array
        return []

    # Init the table with null values
    sum_table = [None] * (target_sum + 1)

    # Seed value for 0
    sum_table[0] = []

    for index in range(target_sum):
        current_sum = sum_table[index]
        
        if current_sum is not None:
            
            for num in numbers:
                result = num + index
                
                if result > target_sum:
                    # Prevent 'Out of bounds'/IndexError
                    continue

                result_combo = current_sum + [num]
                
                if ((sum_table[result] is None) or 
                    (len(sum_table[result]) > len(result_combo))):
                    
                    sum_table[result] = result_combo

    return sum_table[target_sum]


print(best_sum(7, [3, 5, 4]))
print(best_sum(100, [99, 3]))
print(best_sum(100, [1, 2, 5, 25]))
                
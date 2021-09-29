def how_sum(target_sum, numbers):
    # Expected return is an array of integers that add up to target_sum
    if target_sum == 0:
        # Zero using empty array
        return []

    # Init the table with null values
    sum_table = [None] * (target_sum + 1)

    # Seed value for 0
    sum_table[0] = []

    for index in range(target_sum):
        if sum_table[index] is not None:
            for num in numbers:
                result = num + index
                if result == target_sum:
                    return sum_table[index] + [num]
                try:
                    sum_table[result] = sum_table[index] + [num]
                except IndexError:
                    #print('Index out of range')
                    pass
    return sum_table[target_sum]


print(how_sum(7, [3, 5, 4]))
print(how_sum(100, [99, 3]))
print(how_sum(100, [1, 2, 5, 25]))
                
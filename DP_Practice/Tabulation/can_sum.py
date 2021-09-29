def can_sum(target_sum, numbers):

    if target_sum == 0:
        return True

    if target_sum in numbers:
        #Short circuit if target_sum already in numbers
        return True

    
    table_sum = [False] * (target_sum + 1)
    table_sum[0] = True

    for index in range(target_sum):
        if table_sum[index]:
            for num in numbers:
                try:
                    result = num + index
                    if result == target_sum:
                        #Short circuit if result reached target_sum
                        return True
                    else:
                        table_sum[result] = True
                except IndexError:
                    pass
                    # print(f'Sum: {result}, exceeded the target_sum: {target_sum}')
    # return table_sum
    return table_sum[target_sum]
                
print(can_sum(7, [3, 5, 4]))
print(can_sum(100, [99, 3]))
print(can_sum(100, [1, 2, 5, 25]))

def all_construct(target_str, word_bank, memo = {}):

    if target_str in memo:
        return memo[target_str]

    if target_str == '':
        return [[]]
    
    # if target_str in word_bank:
    #     return [[target_str]]

    combinations = []

    for word in word_bank:
        word_len = len(word)
        temp_combination = []
        if target_str[:word_len] == word:
            # temp_combination.append(word)
            # rest_lists = all_construct(target_str[word_len:], word_bank, memo)[:]
            rest_lists = all_construct(target_str[word_len:], word_bank, memo)
            # print(f'Remain list {rest_lists}')
            if rest_lists != []:
                for rest_list in rest_lists:
                    rest_list.insert(0, word)
                combinations.extend(rest_lists)

    memo[target_str] = combinations
    # print(combinations)
    return combinations

print(all_construct('abcd', ['a', 'bc', 'd','fd', 'b', 'cd' ]))
print(all_construct('abcde', ['ab', 'c', 'fd', 'bc' ]))
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        ['e', 'ee', 'eeee', 'eeeee', 'eeeeeee' ]))
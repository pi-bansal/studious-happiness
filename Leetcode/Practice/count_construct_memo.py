# def memoize(f):
#     memo = {}
#     def helper(x, y):
#         if x not in memo:
#             memo[x] = f(x,y)
#         return memo[x]
#     return helper



# @memoize
def count_construct(target_str, word_bank, memo = {}):
    
    if target_str in memo:
        return memo[target_str]
    
    if target_str in word_bank:
        return 1
    if target_str == '':
        return 1

    count = 0
    for word in word_bank:
        word_len = len(word)
        if target_str[:word_len] == word:
            remainder_count = count_construct(target_str[word_len:], word_bank, memo)
            if remainder_count:
                count = count + remainder_count
    memo[target_str] = count
    return count

print(count_construct('abcd', ['a', 'bc', 'd','fd', 'b', 'cd' ]))
print(count_construct('abcde', ['ab', 'c', 'fd', 'bc' ]))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        ['e', 'ee', 'eeee', 'eeeee', 'eeeeeee' ]))
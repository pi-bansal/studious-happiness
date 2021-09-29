def memoize(f):
    memo = {}
    def helper(x, y):
        if x not in memo:
            memo[x] = f(x,y)
        return memo[x]
    return helper



@memoize
def can_construct(target_str, word_bank):
    
    if target_str in word_bank:
        return True
    if target_str == '':
        return True

    for word in word_bank:
        word_len = len(word)
        if (target_str[:word_len] == word and
            can_construct(target_str[word_len:], word_bank)):

            return True
    
    return False

print(can_construct('abcd', ['a', 'bc', 'fd', 'b', 'cd' ]))
print(can_construct('abcd', ['ab', 'c', 'fd', 'bc' ]))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        ['e', 'ee', 'eeee', 'eeeee', 'eeeeeee' ]))
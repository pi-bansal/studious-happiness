def word_construct(target_str, word_bank):

    if target_str == '':
        return []

    target_len = len(target_str)

    table = [None] * ( target_len + 1)
    
    # Could remove the words with length greater than target str? 


    # Empty string is index 0. Lookup will start for the next index (first element of target_str).
    # Word bank will be looped over each index. If the starting of word character is reachable,
    # then it will check whether word is a substring of the target string
    # First index is always reachable
    table[0] = []

    for index in range(target_len):

        #Continue iff the index is reachable
        if table[index] is not None:
            for word in word_bank:
                word_len = len(word)
                
                #Check whether the word is a substring
                end_index = index + word_len
                if target_str[index : end_index] == word:
                    table[end_index] = table[index] + [word]
                    # print(table)

    return table[-1]
        
print(word_construct('abcd', ['a', 'bc', 'fd', 'b', 'cd' ]))
print(word_construct('abcde', ['ab', 'de', 'fd', 'bc' ]))
# print(word_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
#         ['e', 'ee', 'eeee', 'eeeee', 'eeeeeeea' ]))



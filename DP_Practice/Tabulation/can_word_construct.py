def word_construct(target_str, word_bank):

    if target_str == '':
        return True

    target_len = len(target_str)

    table = [False] * ( target_len + 1)
    
    # Could remove the words with length greater than target str? 


    # Empty string is index 0. Lookup will start for the next index (first element of target_str).
    # Word bank will be looped over each index. If the starting of word character is reachable,
    # then it will check whether word is a substring of the target string
    # First index is always reachable
    table[0] = True

    for index in range(target_len):
        if table[index] == True:
            for word in word_bank:
                word_len = len(word)
                
                #Check whether the word is a substring
                if target_str[index : index + word_len] == word:
                    table[index + word_len] = True

    return table[-1]
        
print(word_construct('abcd', ['a', 'bc', 'fd', 'b', 'cd' ]))
print(word_construct('abcde', ['ab', 'de', 'fd', 'bc' ]))
print(word_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        ['e', 'ee', 'eeee', 'eeeee', 'eeeeeeea' ]))



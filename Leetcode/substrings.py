test_str = input('Enter a string:')

str_len = len(test_str)

substrings = [test_str[i:j] for i in range(str_len) for j in range(i + 1, str_len + 1)]
palindromes = [len(substr) for substr in substrings if substr == substr[::-1] ]
print(max(palindromes))
print(substrings)
print(palindromes)
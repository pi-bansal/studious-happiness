class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        i,j = 0, 1
        max_pal = s[0]
        max_len = 1 
        while i < str_len:
            j = i + 1
            while i < j <= str_len:
                if max_len > j-i:
                    j = j + 1
                    continue
                curr_str = s[i:j]
                print(curr_str)
                if curr_str == curr_str[::-1]:
                    print(curr_str, curr_str[::-1])
                    curr_len = j - i
                    if curr_len > max_len:
                        max_len = curr_len
                        max_pal = curr_str
                        print(max_len, max_pal)
                j = j + 1
            i = i + 1

        return max_pal
        # palindromes = [s[i:j] for i in range(str_len) for j in range(i + 1, str_len + 1) if s[i:j] == s[j-1:i+1:-1]]
        # print(palindromes)
        # ordered = sorted(palindromes, key= lambda x: len(x))
        # max = 1
        # str_len = len(s)

        # i = 0
        # while i <= str_len:
        #     j = i + 1
        #     while i < j <= str_len:
        #         print(i,j)
        #         print(s[i:j], s[j:i-2: -1])
        #         if s[i:j] == s [j:i:-1]:
        #             if j - i > max:
        #                 max = j-i 
        #         j = j + 1
        #     i = i + 1
        
        # return max



s = input('Enter the string: ')
sol_obj = Solution()
max = sol_obj.longestPalindrome(s)
print(max)
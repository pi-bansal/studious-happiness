class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        used_index = 0
        res_list = []
        str_len = len(s)
        for i in range(0, str_len):
            curr_char = s[i]
            if curr_char not in result:
                result += curr_char
            else:
                res_list.append(result)
                used_index += s[used_index:].index(curr_char)
                result = s[used_index+1:i]
        else:
            res_list.append(result)

        return max(len(x) for x in res_list)



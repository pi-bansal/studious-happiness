class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        used_index = 0
        res_list = []
        str_len = len(s)
        visited = {}
        for i in range(0, str_len):
            curr_char = s[i]
            
            if curr_char not in result:
                result += curr_char
            else:
                res_list.append(result)
                if visited[curr_char]+1 == i:
                    result = curr_char
                else:
                    result = s[visited[curr_char]:i]
            visited[curr_char] = i
        else:
            res_list.append(result)

        return max(len(x) for x in res_list)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_dict = {}
        req_len = len(arr)/2
        for num in arr:
            if num in count_dict.keys():
                count_dict[num] +=1
            else:
                count_dict[num] = 1
        sorted_count = [v for k,v in sorted(count_dict.items(), key = lambda item: item[1], reverse=True)]
        count, curr_len = 0, 0
        while curr_len < req_len:
            curr_len += sorted_count[count]
            count += 1
        return count
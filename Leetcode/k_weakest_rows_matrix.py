class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        i = 0
        row_map = {}
        for row in mat:
            row_map[i] = row.count(1)
            i +=1
        sorted_row_map = {k:v for k,v in sorted(row_map.items(), key = lambda item: item[1])}
        sorted_list = list(sorted_row_map.keys())
        return sorted_list[:k]
        
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1 + len2
        print(nums1,nums2)
        i = 0
        j = 0
        merged_nums = []
        
        while (i + j + 2) <= total_len and (i < len1 and j < len2):
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i+=1
            else:
                merged_nums.append(nums2[j])
                j+=1
        else:
            if i == len1:
                merged_nums = merged_nums + nums2[j:]
            elif j == len2:
                merged_nums = merged_nums + nums1[i:]

        
        if total_len % 2 == 0:
            median = (merged_nums[total_len//2 -1]  + merged_nums[total_len//2])/2
        else:
            median = merged_nums[(total_len+1)//2 - 1]

        return median
        
x = input('Enter the first list:\n')
nums1 = [int(num) for num in x]        
y = input('Enter the second list:\n')
nums2 = [int(num) for num in y]        
sol_obj = Solution()
median = sol_obj.findMedianSortedArrays(nums1,nums2)
print(median)
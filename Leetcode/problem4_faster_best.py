
#########
#Not completed yet

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1 + len2
        i = 0
        j = 0
        merged_nums = []
        
        prev = 0
        curr = 0

        while (i < len1 and j < len2):
            if nums1[i] < nums2[j]:
                prev = curr
                curr = nums1[i]
                i = i + 1
            else:
                prev = curr
                curr = nums2[j]
                j = j + 1

        
        if total_len % 2 == 0:
            print(prev, curr)
            median = (prev + curr)/2
        else:
            median = curr
        
        return median

x = input('Enter the first list:\n')
nums1 = [int(num) for num in x]        
y = input('Enter the second list:\n')
nums2 = [int(num) for num in y]        
sol_obj = Solution()
median = sol_obj.findMedianSortedArrays(nums1,nums2)
print(median)
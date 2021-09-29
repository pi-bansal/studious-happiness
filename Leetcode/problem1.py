class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in nums:
            nums2 = list(nums)
            nums2.remove(number)
            for number2 in nums2:
                if number + number2 == target:
                    index1 = nums.index(number)
                    index2 = nums2.index(number2) + 1
                    return [index1,index2]
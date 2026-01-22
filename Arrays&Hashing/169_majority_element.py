from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        1. sort the nums array
        2. then we can use two pointers to calculate the length of the continuous same element
        3. if the end pointer is diff from the start, then calculate and move the start pointer to end pointer
        """
        nums.sort()
        start, end = 0, 0
        half = len(nums) / 2

        while end <= len(nums):
            if end == len(nums) or nums[end] != nums[start]:
                temp_len = end - start
                if temp_len > half:
                    return nums[start]
                start = end
            end += 1

        return 0
    
    def majorityElement2(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
    def majorityElement3(self, nums: list[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num] += 1
            if count[num] >= maxCount:
                maxCount = count[num]
                res = num
        
        return res
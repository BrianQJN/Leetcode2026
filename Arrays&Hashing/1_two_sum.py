class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # loop the nums
        # 1. if remain = target - num in left. return the index of num and left
        # 2. if not, add the num and it's index to the left map
        # 3. In this way, we just need one time loop
        seen = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [idx, seen[remain]]
            seen[num] = idx

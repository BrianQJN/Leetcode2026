class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums * 2

        return ans
    
    def getConcatenation2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
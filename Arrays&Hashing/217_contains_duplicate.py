class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        
        time complexity: O(n)
        space complexity: O(n) worst
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicate2(self, nums: list[int]) -> bool:
        """
        time: O(n)
        spaceL: O(n)
        """
        seen = {}
        for num in nums:
            seen_times = seen.get(num, 0)
            if seen_times != 0:
                return True
            seen[num] = seen_times + 1
        return False
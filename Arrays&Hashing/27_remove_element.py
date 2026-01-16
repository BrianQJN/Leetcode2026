class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        1. set the write pointer k = 0
        2. loop the nums array
        3. if nums[i] != val, means we can keep it, so write it to write pointer k position
        4. nums[k] = nums[i] and k + 1
        5. if nums[i] == val, means we can't write it to pointer k
        """
        write_pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_pointer] = nums[i]
                write_pointer += 1
            
        return write_pointer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[swap], nums[i] = nums[i], nums[swap]
                swap += 1
        
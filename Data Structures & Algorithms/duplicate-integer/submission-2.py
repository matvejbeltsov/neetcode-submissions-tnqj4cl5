class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        for num in nums:
            duplicate_set.add(num)
        return True if len(duplicate_set) != len(nums) else False
        
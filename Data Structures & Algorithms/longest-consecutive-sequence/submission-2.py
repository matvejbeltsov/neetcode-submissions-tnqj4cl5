class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0
        
        for num in nums:
            if num - 1 not in set_nums:
                obj = 0
                while num + obj in set_nums:
                    obj += 1
                result = max(result, obj)
        return result    
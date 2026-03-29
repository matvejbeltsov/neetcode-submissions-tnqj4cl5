class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
        for num in set_nums:
            if not num - 1 in set_nums:
                obj = 0
                while num + obj in set_nums:
                    obj += 1
                res = max(res, obj)
        return res
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i, num in enumerate(nums):
            pair = target - num

            if pair in dict_nums:
                return [dict_nums[pair], i]
            
            dict_nums[num] = i
        
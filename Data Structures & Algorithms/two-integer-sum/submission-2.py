class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}


        for idx, num in enumerate(nums):
            pair = target - num

            if pair in dict_nums:
                return [dict_nums[pair], idx]

            dict_nums[num] = idx
